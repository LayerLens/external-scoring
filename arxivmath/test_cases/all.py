"""ArxivMath scorer (lane-1 external_scoring).

Faithful port of MathArena's deterministic final-answer grader
(github.com/eth-sri/matharena, src/matharena/grader.py -> extract_and_grade,
with the arxivmath competition config: final_answer=true, strict_parsing=false,
exact_match_parsing=false, lean=false, typed_delimited_answers=true).

The parsing/equivalence engine is vendored verbatim under ./mathgrade/ (parser.py
+ parse_manual.py, only the loguru dependency swapped for stdlib logging). We
reproduce the exact arxivmath branch of extract_and_grade here and DROP the
lean/hash/exact-match branches (unused by arxivmath) and the human-review warning
heuristics (they never change is_correct).

MathArena's sympy `.equals()` / `simplify()` can hang on pathological expressions
and the upstream code has NO timeout. The external_scoring harness enforces a hard
30s/prompt wall; we add our own tighter SIGALRM guard so a hang scores 0.0 instead
of blowing the harness budget.

Contract (scoring_runner.py): ll_run_tests(response_data) -> float|bool.
  response_data["result"]/["parsed_result"]  -> the model's single completion
  response_data["prompt"]["truth"]/["parsed_truth"] -> gold final answer (raw LaTeX)
"""
from __future__ import annotations

import os
import signal
import sys
from typing import Any

# Make the vendored ./mathgrade package importable regardless of cwd
# (the runner loads this file as a standalone module, not as a package).
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

from mathgrade.parser import (  # noqa: E402
    check_answers,
    extract_answer,
    parse_answer,
)

# Per-prompt hard cap on the sympy parse+compare (well under the harness's 30s).
GRADE_TIMEOUT_SECONDS = 15


class _GradeTimeout(Exception):
    pass


def _on_alarm(signum: int, frame: Any) -> None:  # noqa: ANN401
    raise _GradeTimeout()


def _grade(model_text: str, gold_answer: str) -> bool:
    """The arxivmath branch of MathArena's extract_and_grade (final-answer path)."""
    gold_answer_is_list = "," in gold_answer

    model_answer, _ = extract_answer(
        model_text,
        strict_parsing=False,
        parse=True,
        list_answer=gold_answer_is_list,
        typed_delimiters=True,
    )
    typed_gold_answer, _ = parse_answer(
        gold_answer,
        list_answer=gold_answer_is_list,
        typed_delimiters=True,
    )
    return bool(check_answers(model_answer, typed_gold_answer))


def ll_run_tests(response_data: dict[str, Any]) -> float:  # noqa: N802
    """Entry point used by the LayerLens external-scoring harness.

    Returns 1.0 if the model's boxed final answer is mathematically equivalent
    to the gold answer (MathArena equivalence), else 0.0.
    """
    try:
        model_text = response_data.get("parsed_result", response_data.get("result", "")) or ""
        prompt = response_data.get("prompt", {})
        gold_answer = prompt.get("parsed_truth", prompt.get("truth", "")) or ""

        if not str(gold_answer).strip():
            print("No gold answer present; scoring 0.0")
            return 0.0

        # Guard the (potentially hanging) sympy work with a hard timeout.
        old_handler = signal.signal(signal.SIGALRM, _on_alarm)
        signal.alarm(GRADE_TIMEOUT_SECONDS)
        try:
            is_correct = _grade(str(model_text), str(gold_answer))
        finally:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, old_handler)

        return 1.0 if is_correct else 0.0

    except _GradeTimeout:
        print(f"Grading exceeded {GRADE_TIMEOUT_SECONDS}s; scoring 0.0")
        return 0.0
    except Exception as exc:  # noqa: BLE001
        print(f"Scorer error: {exc}")
        return 0.0
