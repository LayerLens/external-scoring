"""HealthBench scorer entry point (lane-1 external_scoring).

Serves BOTH platform datasets - ``healthbench`` (MAIN split, 5000 rows) and
``healthbench-professional`` (525 rows): their yamls set
``scorer.options.repository: healthbench`` and
``scoring_test_mapped_by: all``, and every dataset row carries its own rubric
in ``prompt.metadata.rubric_items``. All grading logic lives in
``rubric_grading.py`` (same directory - only ``{repository}/test_cases`` is
shipped to the evaluator instance, so the shared module must sit here).

Contract (go-evaluator ``python_exec/system/scoring_runner.py``):
``ll_run_tests(response_data) -> float`` where ``response_data`` is one line
of the responses JSONL:

  response_data["prompt"]["input"]                  -> conversation messages
                                                       (incl. assistant turns
                                                       for multi-turn examples)
  response_data["prompt"]["metadata"]["rubric_items"] -> [{criterion, points}]
  response_data["result"]                           -> the model's completion

Failures (missing rubric, missing judge credentials, judge retry budget
exhausted) RAISE - the runner records the exception and the prompt shows up
as an error, never as a silent 0. An *empty* completion, by contrast, is a
legitimate model output and is graded normally, exactly like upstream.
"""

from __future__ import annotations

import os
import sys
from typing import Any

# The runner loads this file as a standalone module (not a package), so the
# sibling shared module must be imported via an explicit path entry.
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

from rubric_grading import grade_example, parse_rubric_items  # noqa: E402


def ll_run_tests(response_data: dict[str, Any]) -> float:  # noqa: N802
    """Grade one HealthBench example; returns the clipped [0, 1] rubric score."""
    prompt = response_data.get("prompt")
    if not isinstance(prompt, dict):
        raise ValueError("responses line has no prompt object")

    input_messages = prompt.get("input")
    if not isinstance(input_messages, list) or not input_messages:
        raise ValueError("prompt.input is missing or empty")

    metadata = prompt.get("metadata")
    if not isinstance(metadata, dict):
        raise ValueError("prompt.metadata is missing (rubric_items required)")
    rubric_items = parse_rubric_items(metadata)

    completion = response_data.get("result")
    if completion is None:
        completion = response_data.get("parsed_result")
    if not isinstance(completion, str):
        raise ValueError(
            "responses line has no completion text (result/parsed_result); "
            "refusing to grade a missing completion"
        )

    prompt_id = prompt.get("id")
    print(f"HealthBench rubric grading for prompt {prompt_id!r}")
    return grade_example(input_messages, completion, rubric_items)
