"""TutorBench per-criterion rubric grading (shared module).

Implements the evaluation method of "TutorBench: A Benchmark To Assess Tutoring
Capabilities Of Large Language Models" (arXiv 2510.02663), Section 2.3 and
Equation 1, for the platform dataset ``tutorbench``.

  1. ONE judge call PER rubric criterion, asking whether the model's tutoring
     response SATISFIES that criterion (binary).
  2. The paper's weighted average rubric rating (Eq. 1):

         ARR_w = sum_i (w_i * r_i) / sum_i (w_i where w_i > 0)

     with w in {-5, 1, 5}. Negative weights subtract in the numerator but are
     EXCLUDED from the normalising denominator.
  3. Clip to [0, 1] (the paper: "The final score is normalized to the range
     [0,1]").

## THE SIGN CONVENTION — the one thing that is easy to get backwards

Upstream stores no numeric weight; the dataset builder derives it from
``attributes.severity`` (critical -> +5, not_critical -> +1,
critical_negative -> -5) and ships signed ``points`` per criterion.

TutorBench's negative-weight criteria are phrased as PROHIBITIONS, e.g.
"The response must not give the correct final answer $X(t) = e^{sin(t/2)}$" or
"The response must avoid revealing that the correct answer is indeed 3.2"
(495 of the 515 contain "must not", the rest "must/should avoid" or an
equivalent declarative). So for those criteria "satisfied" means the model
BEHAVED WELL — it withheld the answer.

Therefore a met negative criterion must NOT subtract. The paper is explicit
about when the penalty applies: "a rubric may require that the final answer not
be revealed directly, and a VIOLATION of this principle would result in a strong
negative score." So:

    positive w:  contribute +w  when the criterion IS satisfied
    negative w:  contribute  w  when the criterion is NOT satisfied (violated)

This is NOT the HealthBench convention, and reusing that scorer's arithmetic
here would invert the penalty and reward answer-leaking. It matters: 515
criteria carry -5, and 484 of them sit in the active-learning use case, where
giving the answer away instead of hinting is the whole failure mode being
measured.

To keep the judge's answer unambiguous the verdict field is deliberately named
``criterion_satisfied`` rather than HealthBench's ``criteria_met``, and the
prompt asks one uniform question that reads correctly for both "must ..." and
"must not ..." phrasings.

## Judge prompt provenance

Scale published NO grading code or judge prompt for TutorBench — the paper names
the judge model (Claude Sonnet 4) and describes the method, but the template
below is OURS, written to the paper's description and modelled on the structure
of OpenAI's well-tested HealthBench grader. It is therefore a faithful
implementation of a documented method, NOT a verbatim upstream artifact; unlike
the HealthBench scorer, there is nothing to diff it against.

## Multimodal examples

811 of 1473 examples put the student's work in an IMAGE, and ~2272 rubric
criteria are tagged visual perception / visual reasoning, so a text-only judge
could not verify them. The image URL is lifted out of the conversation's
content-parts and attached to every judge call for that example (the judge model
must be vision-capable; the dataset yaml pins one that is). Verified live: the
judge reads the rehosted images and transcribes handwritten student work
correctly.

## Judge transport

The platform (go-evaluator ``python_executor.go resolveJudgeEnv``) injects into
this process's environment, resolved from the dataset yaml's
``scorer.options.judge_model``:

  JUDGE_API_KEY   - API key for the judge provider
  JUDGE_MODEL_ID  - provider-facing model id
  JUDGE_BASE_URL  - OpenAI-compatible provider root (no /chat/completions suffix)

Missing credentials raise immediately: a judge-based scorer must never silently
score 0.

## HARD BUDGET: 120 s per prompt

This is a PLATFORM limit, nothing to do with TutorBench: go-evaluator kills the
scorer subprocess ``externalScorerTimeout`` after start (``python_executor.go``;
``ExecuteTest`` builds a fresh ``context.WithTimeout`` per prompt). There is no
per-dataset override and no env knob - changing it means a go-evaluator change
affecting every external_scoring eval.

Measured rubric sizes: mean 10.2, median 9, p95 17, p99 21, max 39 criteria. At
the default concurrency of 20, 98.5% of examples grade in a SINGLE wave and the
worst case is 2 waves. Measured end-to-end scorer time on the hardest rows: 39
criteria + image = 12.6 s, 28 criteria text = 10.7 s, typical rows 4.5-9.1 s. A
30-day prod window shows no subprocess ever killed at the budget.

Tunables (env):

  TUTORBENCH_JUDGE_CONCURRENCY          default 20
  TUTORBENCH_JUDGE_MAX_ATTEMPTS         default 3   (per rubric criterion)
  TUTORBENCH_JUDGE_TIMEOUT_SECONDS      default 20  (per HTTP request, read)
  TUTORBENCH_JUDGE_BACKOFF_BASE_SECONDS default 0.5 (doubles per retry, cap 2)
  TUTORBENCH_JUDGE_SEND_IMAGES          default 1   (0 disables vision judging)
  TUTORBENCH_JUDGE_JSON_MODE            default 1   (0 never sends response_format)
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
# Judge prompt (ours — see "Judge prompt provenance" above).
# --------------------------------------------------------------------------

GRADER_TEMPLATE = """
Your job is to judge how well an AI tutor's response follows ONE rubric criterion.

You are given a tutoring conversation. Everything before the final assistant
message is fixed context: the student's question, and depending on the task the
tutor's earlier explanation, the student's own attempted solution, or the
student's follow-up. The FINAL assistant message is the response you must judge.
Judge only that final response.

# Conversation
<<conversation>>

# Rubric criterion
<<criterion>>

# Instructions
Return a json object with the following fields: "explanation" and "criterion_satisfied".
- "explanation": a short string explaining why the final response does or does not satisfy the criterion.
- "criterion_satisfied": a boolean. true if the final response satisfies the criterion as written, false otherwise.
- Judge the criterion exactly as written. If it states several requirements, all of them must hold for the criterion to be satisfied.
- An exception: when the criterion offers illustrations with "such as", "for example", or "including", the response does not have to cover every listed example to satisfy it.
- Many criteria are PROHIBITIONS, phrased as "The response must not ..." or "The response must avoid ...". For these, "criterion_satisfied" is true when the response OBEYS the prohibition (it did not do the forbidden thing), and false when the response violates it. Do not invert this.
- Judge only what the response actually says. Do not reward intent, and do not penalise a correct response for omitting things this particular criterion does not ask for.
- If an image is attached, it shows the student's own work referred to by the conversation; use it when the criterion depends on what the student wrote or drew.

# Example
If the criterion is "The response must not state the final answer of 42" and the
final response walks the student toward the method while never stating 42, return:

```json
{
  "explanation": "The response guides the student through the setup without ever stating the value 42, so the prohibition is obeyed.",
  "criterion_satisfied": true
}
```

# Final instruction
Return just the json object in markdown format. Do not include any other text in the response.
""".strip()

JUDGE_SYSTEM_MESSAGE = "You are a helpful assistant."
# Deterministic verdicts: there is no upstream temperature to match (Scale
# published no grading code), so 0 is chosen for reproducibility across reruns.
JUDGE_TEMPERATURE = 0.0
# The verdict itself is tiny, but judges reason in prose before emitting it, and
# a reply cut off mid-reasoning carries no parseable object at all. 512 was sized
# for the verdict alone and truncated the long-response and image-heavy rows —
# measured 11.2% zero rate on a 1473-row prod run, 72% of it judge errors. The
# per-prompt subprocess budget is 120 s and nothing was approaching it.
JUDGE_MAX_TOKENS = 2000

_RETRYABLE_STATUS_CODES = frozenset({408, 429, 500, 502, 503, 504})
_BACKOFF_CAP_SECONDS = 2.0
_IMAGE_PLACEHOLDER = "[the student's work is attached as an image]"
_JSON_RESPONSE_FORMAT = {"type": "json_object"}

# Not every OpenAI-compatible provider accepts response_format, and the judge
# model is configurable, so a rejection must not become a hard failure: the
# first one disables json mode for the rest of this scorer process and the
# attempt is retried without it. go-evaluator spawns one scorer process per
# prompt, so on a rejecting provider each prompt spends one attempt per
# concurrent criterion rediscovering this. parse_json_to_dict handles a
# prose-wrapped verdict regardless.
_json_mode_disabled = False


class JudgeConfigError(RuntimeError):
    """Judge credentials/config missing - the eval must fail, not score 0."""


class JudgeCallError(RuntimeError):
    """A judge call could not produce a valid verdict within the retry budget."""


class _RetryableJudgeError(RuntimeError):
    """Transient judge failure - eligible for another attempt."""


@dataclass(frozen=True)
class RubricItem:
    """One rubric criterion with its signed weight (w in {-5, 1, 5})."""

    criterion: str
    points: int | float

    @property
    def is_penalty(self) -> bool:
        return self.points < 0


@dataclass(frozen=True)
class JudgeConfig:
    api_key: str
    model_id: str
    base_url: str
    concurrency: int
    max_attempts: int
    timeout_seconds: float
    backoff_base_seconds: float
    send_images: bool
    json_mode: bool


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
    """Load the JUDGE_* env contract injected by go-evaluator."""
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
        concurrency=_env_positive_int("TUTORBENCH_JUDGE_CONCURRENCY", 20),
        max_attempts=_env_positive_int("TUTORBENCH_JUDGE_MAX_ATTEMPTS", 3),
        timeout_seconds=_env_positive_float("TUTORBENCH_JUDGE_TIMEOUT_SECONDS", 20.0),
        backoff_base_seconds=_env_positive_float(
            "TUTORBENCH_JUDGE_BACKOFF_BASE_SECONDS", 0.5
        ),
        send_images=os.environ.get("TUTORBENCH_JUDGE_SEND_IMAGES", "1") != "0",
        json_mode=os.environ.get("TUTORBENCH_JUDGE_JSON_MODE", "1") != "0",
    )


def parse_rubric_items(metadata: dict[str, Any]) -> list[RubricItem]:
    """Read prompt.metadata.rubric_items ([{criterion, points}, ...])."""
    raw = metadata.get("rubric_items")
    if not isinstance(raw, list) or not raw:
        raise ValueError(
            "prompt.metadata.rubric_items is missing or empty - the dataset row "
            "must carry its rubric (rebuild the jsonl with build_tutorbench.py)"
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
        if points == 0:
            raise ValueError(
                f"rubric_items[{idx}].points is 0 - a weightless criterion cannot "
                "affect ARR_w and must not be shipped"
            )
        items.append(RubricItem(criterion=criterion, points=points))

    if sum(i.points for i in items if i.points > 0) <= 0:
        raise ValueError("rubric has no positive points; ARR_w is undefined")
    return items


def _message_text(content: Any) -> str:
    """Flatten a message's content to text, marking any image part.

    TutorBench conversations carry OpenAI content-parts for multimodal rows: a
    text part plus an image_url part.
    """
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        chunks: list[str] = []
        for part in content:
            if not isinstance(part, dict):
                raise ValueError(f"content part is not an object: {part!r}")
            kind = part.get("type")
            if kind == "text":
                chunks.append(str(part.get("text", "")))
            elif kind == "image_url":
                chunks.append(_IMAGE_PLACEHOLDER)
            else:
                raise ValueError(f"unsupported content part type {kind!r}")
        return "\n".join(c for c in chunks if c)
    raise ValueError(f"unsupported message content type {type(content).__name__}")


def extract_image_urls(input_messages: list[dict[str, Any]]) -> list[str]:
    """Collect image URLs from the conversation's content-parts, in order."""
    urls: list[str] = []
    for message in input_messages:
        content = message.get("content")
        if not isinstance(content, list):
            continue
        for part in content:
            if isinstance(part, dict) and part.get("type") == "image_url":
                url = (part.get("image_url") or {}).get("url")
                if isinstance(url, str) and url:
                    urls.append(url)
    return urls


def render_conversation(input_messages: list[dict[str, Any]], completion: str) -> str:
    """The conversation with the model's completion appended as the final
    assistant turn, rendered as ``"role: content"`` blocks joined by blank
    lines."""
    convo: list[tuple[str, str]] = []
    for idx, message in enumerate(input_messages, 1):
        role = message.get("role")
        if not isinstance(role, str):
            raise ValueError(f"prompt.input[{idx}] has no string role")
        convo.append((role, _message_text(message.get("content"))))
    convo.append(("assistant", completion))
    return "\n\n".join(f"{role}: {content}" for role, content in convo)


def _balanced_json_spans(text: str) -> list[str]:
    """Every balanced ``{...}`` span in ``text``, outermost only, in order.

    Brace counting is string- and escape-aware, so a ``{`` inside a JSON string
    value does not open a span. An object left unterminated by a truncated reply
    yields nothing, which is what makes truncation a failed attempt rather than
    a half-parsed verdict.
    """
    spans: list[str] = []
    depth = 0
    start = -1
    in_string = False
    escaped = False

    for i, ch in enumerate(text):
        if in_string:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
        elif ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}" and depth > 0:
            depth -= 1
            if depth == 0:
                spans.append(text[start : i + 1])
                start = -1

    return spans


_VERDICT_RE = re.compile(r'"criterion_satisfied"\s*:\s*(true|false)', re.I)


def _salvage_verdict(text: str) -> dict[str, Any]:
    """Recover the verdict from a reply whose JSON does not parse.

    The judge quotes the student's own words inside ``explanation`` and does not
    escape the inner double quotes, which makes the object invalid JSON even
    though it is complete and the verdict is unambiguous. Only
    ``criterion_satisfied`` feeds the score - ``explanation`` is logged and
    nothing else - so the boolean is recovered on its own rather than discarding
    a verdict the judge did reach.
    """
    matches = _VERDICT_RE.findall(text)
    if not matches:
        return {}
    return {
        "criterion_satisfied": matches[-1].lower() == "true",
        "explanation": "recovered from a reply whose JSON did not parse",
    }


def parse_json_to_dict(json_string: str) -> dict[str, Any]:
    """Extract the judge's verdict object; an unusable body yields {} (treated
    as a failed attempt by the caller).

    Judges routinely ignore "return just the json object" and reason in prose
    first, so the object is located ANYWHERE in the reply rather than required
    to be the whole of it. When several objects are present (a judge that quotes
    the example from the prompt before answering) the LAST one carrying
    ``criterion_satisfied`` wins, since the verdict follows the reasoning.
    """
    text = json_string.strip()

    cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", text)
    try:
        parsed = json.loads(cleaned)
    except json.JSONDecodeError:
        pass
    else:
        if isinstance(parsed, dict):
            return parsed
        print(f"Judge returned non-object JSON: {type(parsed).__name__}")
        return {}

    verdict: dict[str, Any] = {}
    for span in _balanced_json_spans(text):
        try:
            candidate = json.loads(span)
        except json.JSONDecodeError:
            continue
        if not isinstance(candidate, dict):
            continue
        if "criterion_satisfied" in candidate:
            verdict = candidate

    if verdict:
        return verdict

    salvaged = _salvage_verdict(text)
    if salvaged:
        return salvaged

    print(f"No JSON object found in judge reply: {text[:200]!r}")
    return {}


def _post_judge_request(
    config: JudgeConfig, grader_prompt: str, image_urls: list[str]
) -> tuple[str, str | None]:
    """One HTTP round-trip to the judge. Returns the completion text and the
    choice's ``finish_reason`` (None when the provider omits it)."""
    content: Any
    if image_urls and config.send_images:
        content = [{"type": "text", "text": grader_prompt}]
        content += [
            {"type": "image_url", "image_url": {"url": url}} for url in image_urls
        ]
    else:
        content = grader_prompt

    global _json_mode_disabled

    payload: dict[str, Any] = {
        "model": config.model_id,
        "messages": [
            {"role": "system", "content": JUDGE_SYSTEM_MESSAGE},
            {"role": "user", "content": content},
        ],
        "temperature": JUDGE_TEMPERATURE,
        "max_tokens": JUDGE_MAX_TOKENS,
    }
    json_mode = config.json_mode and not _json_mode_disabled
    if json_mode:
        payload["response_format"] = _JSON_RESPONSE_FORMAT

    response = requests.post(
        f"{config.base_url}/chat/completions",
        headers={
            "Authorization": f"Bearer {config.api_key}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=(5.0, config.timeout_seconds),
    )

    if json_mode and response.status_code in (400, 422):
        _json_mode_disabled = True
        raise _RetryableJudgeError(
            "judge provider rejected response_format "
            f"(HTTP {response.status_code}); disabling json mode and retrying: "
            f"{response.text[:300]}"
        )

    if response.status_code in _RETRYABLE_STATUS_CODES:
        raise _RetryableJudgeError(
            f"judge HTTP {response.status_code}: {response.text[:300]}"
        )
    if response.status_code != 200:
        raise JudgeCallError(
            f"judge HTTP {response.status_code} (non-retryable): {response.text[:500]}"
        )

    body = response.json()
    try:
        choice = body["choices"][0]
        text = choice["message"]["content"]
    except (KeyError, IndexError, TypeError) as e:
        raise _RetryableJudgeError(f"unexpected judge response shape: {e}") from e
    if not isinstance(text, str):
        raise _RetryableJudgeError(
            f"judge message content is not a string: {type(text).__name__}"
        )
    finish_reason = choice.get("finish_reason")
    return text, finish_reason if isinstance(finish_reason, str) else None


def grade_criterion(
    config: JudgeConfig,
    convo_str: str,
    item: RubricItem,
    item_index: int,
    image_urls: list[str],
) -> dict[str, Any]:
    """Grade ONE criterion with bounded retries.

    Returns the judge's dict, guaranteed to hold a boolean
    ``criterion_satisfied``. Raises JudgeCallError once attempts are exhausted -
    NEVER defaults a verdict."""
    grader_prompt = GRADER_TEMPLATE.replace("<<conversation>>", convo_str).replace(
        "<<criterion>>", item.criterion
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
                f"criterion {item_index}: retrying in {delay:.2f}s "
                f"(attempt {attempt}/{config.max_attempts})"
            )
            time.sleep(delay)

        try:
            raw, finish_reason = _post_judge_request(config, grader_prompt, image_urls)
        except _RetryableJudgeError as e:
            failures.append(f"attempt {attempt}: {e}")
            continue
        except requests.RequestException as e:
            failures.append(f"attempt {attempt}: transport error: {e}")
            continue

        # A reply cut off at max_tokens never reached its verdict, which comes
        # last. Any criterion_satisfied it does contain belongs to reasoning or
        # to an echo of the prompt's worked example (whose verdict is true), so
        # reading one would bias truncations toward "satisfied".
        if finish_reason == "length":
            failures.append(
                f"attempt {attempt}: judge reply truncated at "
                f"max_tokens={JUDGE_MAX_TOKENS}: {raw[-200:]!r}"
            )
            continue

        verdict = parse_json_to_dict(raw)
        label = verdict.get("criterion_satisfied")
        if label is True or label is False:
            return verdict
        failures.append(
            f"attempt {attempt}: bad judge output (no boolean "
            f"criterion_satisfied): {raw[:200]!r}"
        )

    raise JudgeCallError(
        f"criterion {item_index} failed after {config.max_attempts} attempts; "
        + " | ".join(failures)
    )


def contribution(item: RubricItem, satisfied: bool) -> int | float:
    """Signed contribution of one graded criterion to the ARR_w numerator.

    See "THE SIGN CONVENTION" in the module docstring: a positive criterion pays
    out when satisfied; a prohibition costs its (negative) weight when VIOLATED.
    """
    if item.is_penalty:
        return 0 if satisfied else item.points
    return item.points if satisfied else 0


def calculate_score(
    rubric_items: list[RubricItem], verdicts: list[dict[str, Any]]
) -> float:
    """The paper's Eq. 1: signed numerator over the positive-weight total."""
    total_possible = sum(item.points for item in rubric_items if item.points > 0)
    if total_possible <= 0:  # guarded earlier; defence in depth
        raise ValueError("no positive rubric points; ARR_w undefined")
    achieved = sum(
        contribution(item, bool(verdict["criterion_satisfied"]))
        for item, verdict in zip(rubric_items, verdicts, strict=True)
    )
    return achieved / total_possible


def grade_example(
    input_messages: list[dict[str, Any]],
    completion: str,
    rubric_items: list[RubricItem],
) -> float:
    """Grade one example: one judge call per criterion (bounded-concurrency
    thread pool), the paper's ARR_w arithmetic, clipped to [0, 1].

    Any judge failure past the retry budget propagates - the example is recorded
    as an error by the runner, never silently scored."""
    config = load_judge_config()
    convo_str = render_conversation(input_messages, completion)
    image_urls = extract_image_urls(input_messages)

    n_items = len(rubric_items)
    workers = min(config.concurrency, n_items)
    print(
        f"grading {n_items} rubric criteria "
        f"(judge={config.model_id}, concurrency={workers}, "
        f"max_attempts={config.max_attempts}, "
        f"images={len(image_urls) if config.send_images else 0})"
    )

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [
            pool.submit(grade_criterion, config, convo_str, item, idx, image_urls)
            for idx, item in enumerate(rubric_items, 1)
        ]
        verdicts = [future.result() for future in futures]

    penalties_incurred = 0
    for idx, (item, verdict) in enumerate(zip(rubric_items, verdicts), 1):
        satisfied = bool(verdict["criterion_satisfied"])
        contrib = contribution(item, satisfied)
        if item.is_penalty and contrib != 0:
            penalties_incurred += 1
        explanation = str(verdict.get("explanation", "No explanation provided"))
        print(
            f"criterion {idx}: satisfied={satisfied} w={item.points:+} "
            f"contribution={contrib:+} :: {item.criterion[:110]} :: "
            f"{explanation[:160]}"
        )

    raw_score = calculate_score(rubric_items, verdicts)
    clipped = min(1.0, max(0.0, raw_score))
    possible = sum(item.points for item in rubric_items if item.points > 0)
    achieved = raw_score * possible
    print(
        f"judge_calls={n_items} achieved_points={achieved:g} "
        f"possible_points={possible:g} penalties_incurred={penalties_incurred} "
        f"raw_arr_w={raw_score:.4f} final_score={clipped:.4f}"
    )
    return clipped
