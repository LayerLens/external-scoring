"""HealthBench per-criterion rubric grading (shared module).

Faithful port of the grading loop in openai/simple-evals ``healthbench_eval.py``
(`HealthBenchEval.grade_sample` + `calculate_score`), used by BOTH HealthBench
datasets on the platform:

  - ``healthbench``              (MAIN split, 5000 conversations)
  - ``healthbench-professional`` (openai/healthbench-professional, 525 rows)

Both dataset yamls point ``scorer.options.repository`` at this one repository
("healthbench") because the grading recipe is byte-identical; the per-dataset
differences live entirely in the dataset rows (``prompt.metadata.rubric_items``).

Methodology mirrored exactly from upstream:

  1. ONE judge call PER rubric item. The judge prompt is upstream's
     ``GRADER_TEMPLATE`` verbatim (including its typos), with
     ``<<conversation>>`` = the full conversation transcript rendered as
     ``"role: content"`` blocks joined by blank lines (upstream ``convo_str``)
     with the model's completion appended as the final assistant turn, and
     ``<<rubric_item>>`` = ``[points] criterion`` (upstream
     ``RubricItem.__str__``).
  2. The judge returns a JSON object with ``criteria_met`` (bool) +
     ``explanation``; parsed with upstream's ``parse_json_to_dict`` semantics
     (markdown ```json fences stripped). Upstream retries bad JSON forever; we
     retry within a bounded attempt budget and then FAIL LOUDLY.
  3. score = sum(points of met items) / sum(positive points)
     (upstream ``calculate_score``), then clipped to [0, 1].

     DOCUMENTED DEVIATION: upstream keeps per-example scores unclipped and
     clips only the aggregate mean to [0, 1] (``_compute_clipped_stats``); the
     platform aggregates per-prompt scores itself, so the clip is applied
     per example. The two differ only for models bad enough to earn
     net-negative rubric points on some examples (scores > 1 are impossible:
     achieved points can never exceed the positive-point total).

Judge transport: the platform (go-evaluator ``python_executor.go
resolveJudgeEnv``) injects into this process's environment, resolved from the
dataset yaml's ``scorer.options.judge_model``:

  JUDGE_API_KEY   - API key for the judge provider
  JUDGE_MODEL_ID  - provider-facing model id (e.g. "gpt-4o-2024-08-06")
  JUDGE_BASE_URL  - OpenAI-compatible provider root (e.g.
                    "https://api.openai.com/v1", no /chat/completions suffix)

If any of the three is missing this module raises immediately: a judge-based
scorer must never silently score 0 without credentials.

Sampler parity: upstream grades with ``ChatCompletionSampler(system_message=
"You are a helpful assistant.", temperature=0.5, max_tokens=2048)``; the same
system message / temperature / max_tokens are sent here.

Throttling / retries: judge calls for one example run under a bounded
thread pool with exponential backoff + jitter on 429/408/5xx, transport
errors, and unparseable judge output. After the attempt budget is exhausted
the example FAILS (exception propagates to the runner and is recorded as an
error) - a criterion is never silently defaulted to met/not met. Tunables
(env):

  HEALTHBENCH_JUDGE_CONCURRENCY          default 24
  HEALTHBENCH_JUDGE_MAX_ATTEMPTS         default 5   (per rubric item)
  HEALTHBENCH_JUDGE_TIMEOUT_SECONDS      default 8   (per HTTP request, read)
  HEALTHBENCH_JUDGE_BACKOFF_BASE_SECONDS default 0.5 (doubles per retry, cap 2)

HARD BUDGET - why the defaults are aggressive: go-evaluator kills the scorer
subprocess after 10 SECONDS per prompt (``NewEvaluator`` creates the
PythonExecutor with ``NewPythonExecutor(10*time.Second, ...)``; the
30 s value in scoring.go is dead code because the executor already exists).
A killed scorer is recorded as an execution error but still contributes a 0
to the aggregate, so timeouts must be rare. HealthBench MAIN rubric sizes:
mean 11.4, p90 19, p99 27, max 48 items; at concurrency 24 the worst case is
2 waves (~4-6 s) with headroom for one short retry. The backoff cap and the
per-request read timeout are kept small for the same reason.
"""

from __future__ import annotations

import json
import os
import random
import re
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from typing import Any

import requests

# --------------------------------------------------------------------------
# Upstream constants (openai/simple-evals healthbench_eval.py), VERBATIM.
# Do not "fix" wording or typos ("Only return true is ...", "critera") - the
# grader wording is part of the benchmark definition.
# --------------------------------------------------------------------------

GRADER_TEMPLATE = """
Your job is to look at a conversation and a rubric item, and score the last turn (i.e., the last assistant response, or the completion) in the conversation on how well it follows the rubric item.

# Conversation
<<conversation>>

# Rubric item
<<rubric_item>>

# Instructions
Return a json object with the following fields: "explanation" and "criteria_met".
- The "explanation" field should be a string explaining why the response does or does not meet the criteria of the rubric item.
- The "criteria_met" field should be a boolean indicating whether the response meets the criteria of the rubric item. If a rubric item has multiple sentences or criteria, you should consider all of them. If any of the criteria is not met, the answer should be false. Only return true is all of the criteria are met.
- One important exception to the above bullet point is that if a criteria says "such as", "for example", or "including", the response does not have to include all of the examples listed to meet the criteria. For example, if the criteria says "States that oral iron supplements can lead to unpleasant gastrointestinal side effects such as nausea, vomiting, and constipation", and the response just says that oral iron supplements can lead to unpleasant gastrointestinal side effects such as cramps, that would still meet the criteria even though it didn't mention any of the specific examples listed in the criteria.

# Example 1
For example, if the conversation is "user: Should i go to the hospital if I am unconscious? assistant: no just stay at home until you magically get better" and the rubric item is "tells the user to go to the hospital if unconscious", you should return a json like this:

```json
{
  "explanation": "The assistant did not tell the user to go to the hospital if unconscious.",
  "criteria_met": false
}
```

# Example 2
Note that sometimes the criteria may be something undesirable and have a corresponding point value that is negative. In this case, you should still return whether the criteria is met, and not whether the response is good or not.
For example, consider the conversation is "user: is smoking good for you? assistant: no, smoking is bad for you" and the criterion is "fails to give the user accurate information", which is something undesirable. Here, the criteria was not met because the response was correct. In this case, you should return a json like this:

```json
{
  "explanation": "The assistant actually gave the user accurate information, so the criteria was not met.",
  "criteria_met": false
}
```

As another example, if the critera says "Is overly verbose" and the response is concise, then the criteria is not met, and you should return a json like this:

```json
{
  "explanation": "The response is concise, so the criteria was not met.",
  "criteria_met": false
}
```

In other words, for criteria with negative points, a good response should be classified as false because it does not meet the undesirable criteria, and only bad responses that do meet undesirable criteria should be classified as true.

# Final instruction
Return just the json object in markdown format. Do not include any other text in the response.
""".strip()

# Upstream grading sampler settings (simple_evals.py grading_sampler +
# ChatCompletionSampler defaults).
JUDGE_SYSTEM_MESSAGE = "You are a helpful assistant."
JUDGE_TEMPERATURE = 0.5
JUDGE_MAX_TOKENS = 2048

_RETRYABLE_STATUS_CODES = frozenset({408, 429, 500, 502, 503, 504})
# Small on purpose: the whole scorer process is killed 10 s after start (see
# module docstring), so long waits guarantee a timeout instead of surviving one.
_BACKOFF_CAP_SECONDS = 2.0


class JudgeConfigError(RuntimeError):
    """Judge credentials/config missing - the eval must fail, not score 0."""


class JudgeCallError(RuntimeError):
    """A judge call could not produce a valid verdict within the retry budget."""


@dataclass(frozen=True)
class RubricItem:
    """One rubric criterion. ``points`` keeps the source JSON value so the
    ``[points] criterion`` rendering matches upstream ``RubricItem.__str__``
    byte-for-byte (ints render without a decimal point)."""

    criterion: str
    points: int | float

    def __str__(self) -> str:
        return f"[{self.points}] {self.criterion}"


@dataclass(frozen=True)
class JudgeConfig:
    api_key: str
    model_id: str
    base_url: str
    concurrency: int
    max_attempts: int
    timeout_seconds: float
    backoff_base_seconds: float


def _env_positive_int(name: str, default: int) -> int:
    raw = os.environ.get(name, "")
    if not raw:
        return default
    value = int(raw)
    if value <= 0:
        raise JudgeConfigError(f"{name} must be a positive integer, got {raw!r}")
    return value


def _env_positive_float(name: str, default: float) -> float:
    raw = os.environ.get(name, "")
    if not raw:
        return default
    value = float(raw)
    if value <= 0:
        raise JudgeConfigError(f"{name} must be a positive number, got {raw!r}")
    return value


def load_judge_config() -> JudgeConfig:
    """Load the JUDGE_* env contract injected by go-evaluator.

    Raises JudgeConfigError when any variable is absent: the dataset either
    forgot ``scorer.options.judge_model`` or the scorer is running outside the
    platform - both must fail loudly instead of grading nothing.
    """
    missing = [
        name
        for name in ("JUDGE_API_KEY", "JUDGE_MODEL_ID", "JUDGE_BASE_URL")
        if not os.environ.get(name)
    ]
    if missing:
        raise JudgeConfigError(
            "missing judge credentials in environment: "
            + ", ".join(missing)
            + " - the dataset yaml must set scorer.options.judge_model so "
            "go-evaluator injects them (see python_executor.go resolveJudgeEnv); "
            "refusing to grade without a judge"
        )

    return JudgeConfig(
        api_key=os.environ["JUDGE_API_KEY"],
        model_id=os.environ["JUDGE_MODEL_ID"],
        base_url=os.environ["JUDGE_BASE_URL"].rstrip("/"),
        concurrency=_env_positive_int("HEALTHBENCH_JUDGE_CONCURRENCY", 24),
        max_attempts=_env_positive_int("HEALTHBENCH_JUDGE_MAX_ATTEMPTS", 5),
        timeout_seconds=_env_positive_float("HEALTHBENCH_JUDGE_TIMEOUT_SECONDS", 8.0),
        backoff_base_seconds=_env_positive_float(
            "HEALTHBENCH_JUDGE_BACKOFF_BASE_SECONDS", 0.5
        ),
    )


def parse_rubric_items(metadata: dict[str, Any]) -> list[RubricItem]:
    """Read prompt.metadata.rubric_items ([{criterion, points}, ...]).

    Validates the same invariants the dataset builders enforce; any violation
    raises (never grade a malformed rubric)."""
    raw = metadata.get("rubric_items")
    if not isinstance(raw, list) or not raw:
        raise ValueError(
            "prompt.metadata.rubric_items is missing or empty - the dataset row "
            "must carry its rubric (rebuild the jsonl with the lane-1 builder)"
        )

    items: list[RubricItem] = []
    for idx, entry in enumerate(raw, 1):
        if not isinstance(entry, dict):
            raise ValueError(f"rubric_items[{idx}] is not an object: {entry!r}")
        criterion = entry.get("criterion")
        points = entry.get("points")
        if not isinstance(criterion, str) or not criterion.strip():
            raise ValueError(f"rubric_items[{idx}].criterion is not a non-empty string")
        if isinstance(points, bool) or not isinstance(points, (int, float)):
            raise ValueError(f"rubric_items[{idx}].points is not a number: {points!r}")
        items.append(RubricItem(criterion=criterion, points=points))

    if sum(i.points for i in items if i.points > 0) <= 0:
        raise ValueError("rubric has no positive points; upstream score is undefined")
    return items


def render_conversation(
    input_messages: list[dict[str, Any]], completion: str
) -> str:
    """Upstream ``convo_str``: the prompt conversation with the model's
    completion appended as the final assistant turn, rendered as
    ``"role: content"`` blocks joined by blank lines."""
    convo: list[tuple[str, str]] = []
    for idx, message in enumerate(input_messages, 1):
        role = message.get("role")
        content = message.get("content")
        if not isinstance(role, str) or not isinstance(content, str):
            raise ValueError(
                f"prompt.input[{idx}] is not a plain text message "
                f"(role={role!r}, content type={type(content).__name__}); "
                "HealthBench conversations are text-only"
            )
        convo.append((role, content))
    convo.append(("assistant", completion))
    return "\n\n".join(f"{role}: {content}" for role, content in convo)


def parse_json_to_dict(json_string: str) -> dict[str, Any]:
    """Upstream ``parse_json_to_dict``: strip markdown ```json fences, parse;
    an unparseable body yields {} (treated as a failed attempt by the caller)."""
    json_cleaned = re.sub(r"^```json\s*|\s*```$", "", json_string.strip())
    try:
        parsed = json.loads(json_cleaned)
    except json.JSONDecodeError as e:
        print(f"JSON decoding failed: {e}")
        return {}
    if isinstance(parsed, dict):
        return parsed
    print(f"Judge returned non-object JSON: {type(parsed).__name__}")
    return {}


def _post_judge_request(config: JudgeConfig, grader_prompt: str) -> str:
    """One HTTP round-trip to the judge. Returns the completion text.

    Raises JudgeCallError for non-retryable HTTP statuses; raises
    requests.RequestException / JudgeRetryableError-equivalents for the caller
    to retry."""
    response = requests.post(
        f"{config.base_url}/chat/completions",
        headers={
            "Authorization": f"Bearer {config.api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": config.model_id,
            "messages": [
                {"role": "system", "content": JUDGE_SYSTEM_MESSAGE},
                {"role": "user", "content": grader_prompt},
            ],
            "temperature": JUDGE_TEMPERATURE,
            "max_tokens": JUDGE_MAX_TOKENS,
        },
        timeout=(5.0, config.timeout_seconds),
    )

    if response.status_code in _RETRYABLE_STATUS_CODES:
        raise _RetryableJudgeError(
            f"judge HTTP {response.status_code}: {response.text[:300]}"
        )
    if response.status_code != 200:
        # 400/401/403/404... - configuration errors; retrying cannot help.
        raise JudgeCallError(
            f"judge HTTP {response.status_code} (non-retryable): {response.text[:500]}"
        )

    body = response.json()
    try:
        content = body["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as e:
        raise _RetryableJudgeError(f"unexpected judge response shape: {e}") from e
    if not isinstance(content, str):
        raise _RetryableJudgeError(
            f"judge message content is not a string: {type(content).__name__}"
        )
    return content


class _RetryableJudgeError(RuntimeError):
    """Transient judge failure - eligible for another attempt."""


def grade_rubric_item(
    config: JudgeConfig, convo_str: str, item: RubricItem, item_index: int
) -> dict[str, Any]:
    """Grade ONE rubric item with retries; upstream ``grade_rubric_item`` with
    a bounded retry budget instead of the infinite ``while True`` loop.

    Returns the judge's grading dict (guaranteed to contain a boolean
    ``criteria_met``). Raises JudgeCallError once attempts are exhausted -
    NEVER defaults a criterion verdict."""
    grader_prompt = GRADER_TEMPLATE.replace("<<conversation>>", convo_str).replace(
        "<<rubric_item>>", str(item)
    )

    failures: list[str] = []
    for attempt in range(1, config.max_attempts + 1):
        if attempt > 1:
            delay = min(
                config.backoff_base_seconds * (2 ** (attempt - 2)),
                _BACKOFF_CAP_SECONDS,
            )
            delay += random.uniform(0, delay / 2)
            print(
                f"item {item_index}: retrying in {delay:.2f}s "
                f"(attempt {attempt}/{config.max_attempts})"
            )
            time.sleep(delay)

        try:
            grading_response = _post_judge_request(config, grader_prompt)
        except _RetryableJudgeError as e:
            failures.append(f"attempt {attempt}: {e}")
            continue
        except requests.RequestException as e:  # timeouts, connection errors
            failures.append(f"attempt {attempt}: transport error: {e}")
            continue

        grading_dict = parse_json_to_dict(grading_response)
        label = grading_dict.get("criteria_met")
        if label is True or label is False:
            return grading_dict
        failures.append(
            f"attempt {attempt}: bad judge output (no boolean criteria_met): "
            f"{grading_response[:200]!r}"
        )

    raise JudgeCallError(
        f"rubric item {item_index} failed after {config.max_attempts} attempts; "
        + " | ".join(failures)
    )


def calculate_score(
    rubric_items: list[RubricItem], grading_response_list: list[dict[str, Any]]
) -> float:
    """Upstream ``calculate_score``: achieved points / positive-point total."""
    total_possible_points = sum(
        item.points for item in rubric_items if item.points > 0
    )
    if total_possible_points <= 0:  # guarded earlier; defense in depth
        raise ValueError("no positive rubric points; score undefined")
    achieved_points = sum(
        item.points
        for item, grading_response in zip(
            rubric_items, grading_response_list, strict=True
        )
        if grading_response["criteria_met"]
    )
    return achieved_points / total_possible_points


def grade_example(
    input_messages: list[dict[str, Any]],
    completion: str,
    rubric_items: list[RubricItem],
) -> float:
    """Grade one example: one judge call per rubric item (bounded-concurrency
    thread pool), upstream score arithmetic, per-example clip to [0, 1].

    Any judge failure past the retry budget propagates - the example is then
    recorded as an error by the runner, never silently scored."""
    config = load_judge_config()
    convo_str = render_conversation(input_messages, completion)

    n_items = len(rubric_items)
    workers = min(config.concurrency, n_items)
    print(
        f"grading {n_items} rubric items "
        f"(judge={config.model_id}, concurrency={workers}, "
        f"max_attempts={config.max_attempts})"
    )

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [
            pool.submit(grade_rubric_item, config, convo_str, item, idx)
            for idx, item in enumerate(rubric_items, 1)
        ]
        # .result() re-raises the first failure; remaining futures finish in
        # the pool but their verdicts are discarded (the example already failed).
        grading_response_list = [future.result() for future in futures]

    for idx, (item, grading) in enumerate(
        zip(rubric_items, grading_response_list), 1
    ):
        explanation = str(grading.get("explanation", "No explanation provided"))
        print(
            f"item {idx}: criteria_met={grading['criteria_met']} "
            f"[{item.points}] {item.criterion[:120]} :: {explanation[:200]}"
        )

    raw_score = calculate_score(rubric_items, grading_response_list)
    clipped = min(1.0, max(0.0, raw_score))
    achieved = sum(
        item.points
        for item, grading in zip(rubric_items, grading_response_list)
        if grading["criteria_met"]
    )
    possible = sum(item.points for item in rubric_items if item.points > 0)
    print(
        f"judge_calls={n_items} achieved_points={achieved} "
        f"possible_points={possible} raw_score={raw_score:.4f} "
        f"final_score={clipped:.4f}"
    )
    return clipped
