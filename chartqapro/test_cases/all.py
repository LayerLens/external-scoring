"""ChartQAPro scorer (lane-1 external_scoring).

Faithful port of the official ChartQAPro grader
(github.com/vis-nlp/ChartQAPro, evaluate_predictions.py ->
`relaxed_correctness_chartqapro` / `evaluate_single_answer`). We reproduce its
relaxed-accuracy + ANLS + multi-answer list logic exactly, reading the structured
gold (full Answer list, per-element Year flags, Question Type) from the prompt's
`metadata` (the dataset builder puts them there; `truth` carries the simple
Answer[-1]).

Grading recipe (per the official grader):
  - Parse BOTH gold and prediction as Python lists via `fix_list_format` +
    `ast.literal_eval` (fallback: single-element list). Score element-wise,
    index-aligned, mean over max(len(gold), len(pred)); a missing/extra element
    scores 0.
  - Per element: if the matching Year flag is "YES" (case-insensitive) -> exact
    case-insensitive string match. Otherwise relaxed accuracy: if both sides
    parse as floats (after stripping '%'), correct iff within 5% relative
    tolerance (target 0 -> must be exactly 0); else ANLS (lowercased, threshold
    0.5).
  - Conversational: gold is the LAST turn's answer; the whole dialogue is in the
    single prompt. The Year flag used is the LAST flag (matches the official
    `year_flags_per_row[-1:]`).

DELIBERATE DEVIATION (documented): the official `evaluate_predictions_chartqapro`
computes `always_use_exact_match = split in ['Fact Checking', 'Multi Choice']`
but then calls `relaxed_correctness_chartqapro(gt, pred, year_flags=...)` WITHOUT
passing it -- so upstream `always_use_exact_match` is a latent NO-OP and Fact
Checking / Multi Choice actually fall through to the relaxed/ANLS path. We follow
the *paper's stated intent* and apply exact (case-insensitive) match for those two
types, which is the correct grading for true/false and option-letter answers. This
is a faithful-to-intent fix of an upstream bug, not a behavior change to the
relaxed path used by every other type.

Contract (scoring_runner.py): ll_run_tests(response_data) -> float.
  response_data["result"]/["parsed_result"]            -> model's single completion
  response_data["prompt"]["truth"]/["parsed_truth"]    -> Answer[-1] (simple gold)
  response_data["prompt"]["metadata"]["answers"]       -> full Answer list (gold)
  response_data["prompt"]["metadata"]["year_flags"]    -> per-element Year flags
  response_data["prompt"]["metadata"]["question_type"] -> Question Type
"""
from __future__ import annotations

import ast
import os
import re
import sys
from typing import Any

# The runner loads this file as a standalone module (not a package). Keep the
# import-path shim for parity with the other scorers even though we have no
# vendored sibling package today (anls is a pip dep).
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

from anls import anls_score  # noqa: E402  # type: ignore[import-untyped]

MAX_RELATIVE_CHANGE = 0.05
EXACT_MATCH_TYPES = {"Fact Checking", "Multi Choice"}


def _fix_list_format(item: str) -> Any:  # noqa: ANN401
    """Verbatim port of the official `fix_list_format`.

    Standardize string representations of lists, adding quotes around bare
    elements, then safely eval to a Python list. Returns the original item on
    failure or when it is not a "[...]"-wrapped string.
    """
    if not isinstance(item, str):
        return item
    match = re.match(r"^\[(.*)\]$", item.strip())
    if not match:
        return item
    content = match.group(1)
    corrected = re.sub(r"(?<!['\w])(\w[^,]*?)(?!['\w])", r"'\1'", content)
    try:
        return ast.literal_eval(f"[{corrected}]")
    except (SyntaxError, ValueError):
        return item


def _parse_to_list(text: str) -> list[str] | None:
    """Verbatim port of the official `parse_to_list`."""
    if not isinstance(text, str):
        return None
    try:
        parsed = ast.literal_eval(text)
    except Exception:  # noqa: BLE001
        return None
    if isinstance(parsed, list):
        return [str(x).strip(" '") for x in parsed]
    return None


def _to_float(text: str) -> float | None:
    """Verbatim port of the official `to_float` (strips a trailing '%')."""
    try:
        return float(text.strip().strip("%"))
    except ValueError:
        return None


def _evaluate_single_answer(target: str, prediction: str) -> float:
    """Verbatim port of the official `evaluate_single_answer`.

    Numeric within 5% relative tolerance, else ANLS (lowercased, threshold 0.5).
    """
    t = target.strip().strip("%").strip()
    p = prediction.strip().strip("%").strip()
    t_f = _to_float(t)
    p_f = _to_float(p)
    if t_f is not None and p_f is not None:
        if t_f == 0.0:
            return 1.0 if p_f == 0.0 else 0.0
        change = abs(p_f - t_f) / abs(t_f)
        return 1.0 if change <= MAX_RELATIVE_CHANGE else 0.0
    return float(anls_score(prediction=p.lower(), gold_labels=[t.lower()], threshold=0.5))


def _relaxed_correctness(
    target: str,
    prediction: str,
    year_flags: list[str] | None,
    always_use_exact_match: bool,
) -> float:
    """Port of the official `relaxed_correctness_chartqapro`.

    The ONLY change from upstream: `always_use_exact_match` is actually honored
    (see module docstring -- upstream never passes it, making it a no-op). When
    True, every element uses exact case-insensitive match regardless of its Year
    flag.
    """
    fixed_t = _fix_list_format(target)
    t_list = _parse_to_list(str(fixed_t)) or [str(target)]
    p_list = _parse_to_list(str(prediction)) or [str(prediction)]
    n = len(t_list)

    if year_flags is None:
        year_flags = ["NO"] * n
    # Expand year_flags for questions with multiple answers (upstream behavior).
    if len(year_flags) < n:
        year_flags = year_flags * n

    scores: list[float] = []
    for idx in range(max(len(t_list), len(p_list))):
        if idx >= len(t_list) or idx >= len(p_list):
            # Model predicted more or fewer elements than necessary.
            scores.append(0.0)
            continue
        t_item, p_item = t_list[idx], p_list[idx]
        flag = year_flags[idx] if idx < len(year_flags) else "NO"
        flag_cond = str(flag).upper() == "YES"
        if flag_cond or always_use_exact_match:
            # Exact (case-insensitive) match: years, fact-checking, multi-choice.
            scores.append(1.0 if t_item.strip().lower() == p_item.strip().lower() else 0.0)
        else:
            scores.append(_evaluate_single_answer(t_item, p_item))
    return sum(scores) / len(scores) if scores else 0.0


def ll_run_tests(response_data: dict[str, Any]) -> float:  # noqa: N802
    """Entry point for the LayerLens external-scoring harness.

    Returns the per-prompt ChartQAPro relaxed-accuracy score in [0.0, 1.0]
    (fractional for multi-answer prompts).
    """
    try:
        prediction = response_data.get("parsed_result", response_data.get("result", "")) or ""
        prompt = response_data.get("prompt", {}) or {}
        metadata = prompt.get("metadata", {}) or {}

        # Gold: prefer the structured full Answer list from metadata; fall back
        # to truth/parsed_truth (Answer[-1]) if metadata is absent.
        answers = metadata.get("answers")
        if isinstance(answers, list) and answers:
            gold = str(answers[-1])
        else:
            gold = str(prompt.get("parsed_truth", prompt.get("truth", "")) or "")

        question_type = str(metadata.get("question_type", "") or "")

        year_flags_raw = metadata.get("year_flags")
        year_flags = [str(f) for f in year_flags_raw] if isinstance(year_flags_raw, list) else None
        # Conversational: only the LAST turn's flag is relevant (matches upstream
        # `year_flags_per_row[-1:]`); gold is already Answer[-1].
        if question_type == "Conversational" and year_flags:
            year_flags = year_flags[-1:]

        if not gold.strip():
            print("ChartQAPro: no gold answer present; scoring 0.0")
            return 0.0

        always_exact = question_type in EXACT_MATCH_TYPES

        # Strip trailing periods/newlines exactly like the official driver does
        # to both gold and prediction before grading.
        gold_clean = gold.strip(".").strip("\n")
        pred_clean = str(prediction).strip(".").strip("\n")

        score = _relaxed_correctness(
            gold_clean,
            pred_clean,
            year_flags=year_flags,
            always_use_exact_match=always_exact,
        )
        return float(score)

    except Exception as exc:  # noqa: BLE001
        print(f"ChartQAPro scorer error: {exc}")
        return 0.0
