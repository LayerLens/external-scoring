"""TutorBench scorer entry point (lane-1 external_scoring).

Serves the platform dataset ``tutorbench`` (1473 rows): its yaml sets
``scorer.options.repository: tutorbench`` and ``scoring_test_mapped_by: all``,
and every dataset row carries its own rubric in
``prompt.metadata.rubric_items`` with SIGNED weights. All grading logic lives in
``rubric_grading.py`` (same directory - only ``{repository}/test_cases`` is
shipped to the evaluator instance, so the shared module must sit here).

Contract (go-evaluator ``python_exec/system/scoring_runner.py``):
``ll_run_tests(response_data) -> float`` where ``response_data`` is one line of
the responses JSONL:

  response_data["prompt"]["input"]                    -> conversation messages
                                                         (incl. the assistant
                                                         turns every example
                                                         carries as fixed
                                                         history, and the
                                                         image_url content-part
                                                         on multimodal rows)
  response_data["prompt"]["metadata"]["rubric_items"] -> [{criterion, points}]
  response_data["result"]                             -> the model's completion

Failures (missing rubric, missing judge credentials, judge retry budget
exhausted) RAISE - the runner records the exception and the prompt shows up as
an error, never as a silent 0. An *empty* completion, by contrast, is a
legitimate model output and is graded normally.

NOTE on the sign convention: TutorBench's negative-weight criteria are
prohibitions, so a SATISFIED penalty criterion means the model behaved well and
must not subtract. See "THE SIGN CONVENTION" in rubric_grading.py - this differs
from the HealthBench scorer and getting it backwards would reward answer-leaking.
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
    """Grade one TutorBench example; returns the clipped [0, 1] ARR_w score."""
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

    print(
        f"TutorBench rubric grading for prompt {prompt.get('id')!r} "
        f"(use_case={metadata.get('use_case')}, modality={metadata.get('modality')}, "
        f"criteria={len(rubric_items)})"
    )
    return grade_example(input_messages, completion, rubric_items)
