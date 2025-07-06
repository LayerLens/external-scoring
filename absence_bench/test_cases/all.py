#!/usr/bin/env python3
"""Absence Bench evaluation logic.

This module provides the `ll_run_tests` entry-point expected by the LayerLens
scoring harness.  It computes a micro-F1 score for a model’s ability to
identify the lines that were deliberately *omitted* from an original context
(e.g. a poem).  The harness will print the resulting score and return it as a
float in the range ``[0, 1]``.
"""
from __future__ import annotations

import json
from typing import Any, Dict, List

# Optional metadata dict (kept for parity with other benchmarks)
METADATA: Dict[str, Any] = {}


# -----------------------------------------------------------------------------
# Core metric implementation
# -----------------------------------------------------------------------------

def evaluate_response(
    response: str,
    metadata: Dict[str, Any],
    *,
    subset: str | None = None,
) -> Dict[str, Any]:
    """Evaluate a single model response.

    Args:
        response: The model's textual answer.
        metadata: Dictionary containing at minimum:
            - ``original_context`` (str): the full original text / sequence / diff.
            - ``omitted_index`` (List[int]): indices of elements or lines that were removed.
        subset: Optional subset identifier (e.g. ``"poetry"``, ``"numerical"``, ``"github_prs"``)
            used to apply task-specific evaluation rules.

    Returns:
        Dict with keys ``tp``, ``fp``, ``fn``, ``micro_f1`` and some
        diagnostic lists.
    """
    original_lines = metadata.get("original_context", "").split("\n")
    omitted_indices: List[int] = metadata.get("omitted_index", [])

    # Normalise *subset* to lowercase for easier comparison
    subset = (subset or "").lower()

    # Guard against None responses
    if response is None:
        response = ""
    response = str(response)
    
    # Some models include a chain-of-thought segment terminated by </think>.
    if "</think>" in response:
        response = response.split("</think>")[-1]

    # Prepare result structure
    results: Dict[str, Any] = {
        "tp": 0,  # correctly identified omitted lines
        "fp": 0,  # lines flagged as omitted but actually present
        "fn": 0,  # omitted lines that the model missed
        "identified_lines": [],
        "unidentified_lines": [],
        "wrongly_identified_lines": [],
    }

    # Special-case handling by subset type
    if subset.startswith("numerical"):
        # Treat each line as an atomic element and expect the model to output
        # the *exact* missing numbers, one per line.
        response_elems = [x.strip() for x in response.split("\n") if x.strip()]
        for idx, element in enumerate(original_lines):
            elem_str = str(element).strip()
            if not elem_str:
                continue
            is_omitted = idx in omitted_indices
            elem_found = elem_str in response_elems
            if elem_found and is_omitted:
                results["tp"] += 1
                results["identified_lines"].append(elem_str)
            elif elem_found and not is_omitted:
                results["fp"] += 1
                results["wrongly_identified_lines"].append(elem_str)
            elif (not elem_found) and is_omitted:
                results["fn"] += 1
                results["unidentified_lines"].append(elem_str)

    else:
        # Shared logic for poetry and GitHub PR subsets (textual lines)
        response_lower = response.lower()

        # GitHub PRs: penalise duplicate lines appearing in response
        repeat_lines: List[str] = []
        if subset.startswith("github"):
            seen: Dict[str, int] = {}
            for l in original_lines:
                seen[l] = seen.get(l, 0) + 1
            repeat_lines = [l for l, c in seen.items() if c > 1]
            for dup_line in repeat_lines:
                clean_dup = dup_line.strip().lower()
                # Count occurrences up to the number of repeats in original diff
                occ = response_lower.count("\n" + clean_dup + "\n")
                if occ:
                    fp_inc = min(occ, seen[dup_line])
                    results["fp"] += fp_inc
                    results["wrongly_identified_lines"].extend([dup_line] * fp_inc)

        for idx, line in enumerate(original_lines):
            if line in repeat_lines:
                # Already accounted for duplicates above
                continue
            clean_line = line.strip().lower()
            if not clean_line:
                # Ignore blank lines
                continue

            line_found = clean_line in response_lower
            is_omitted = idx in omitted_indices

            if line_found and is_omitted:
                results["tp"] += 1
                results["identified_lines"].append(line)
            elif line_found and not is_omitted:
                results["fp"] += 1
                results["wrongly_identified_lines"].append(line)
            elif (not line_found) and is_omitted:
                results["fn"] += 1
                results["unidentified_lines"].append(line)

    # Compute micro-F1 score
    denom = 2 * results["tp"] + results["fp"] + results["fn"]
    results["micro_f1"] = (2 * results["tp"] / denom) if denom else 0.0

    # Special-case: if no lines were omitted, we grade by false-positive rate.
    if not omitted_indices and original_lines:
        results["micro_f1"] = 1 - (results["fp"] / len(original_lines))

    return results


# -----------------------------------------------------------------------------
# Harness entry-point
# -----------------------------------------------------------------------------

def ll_run_tests(response_data: Dict[str, Any]) -> float:  # noqa: N802
    """Entry point used by the evaluation harness.

    The harness passes *response_data* containing at least:
        - ``result`` or ``parsed_result``: the model’s raw output.
        - ``prompt``: a dict which itself contains ``metadata`` with
          ``original_context`` and ``omitted_index``.

    The function prints a JSON blob with a ``score`` field (between 0 and 1)
    plus additional details, then returns the score as a float.
    """
    try:
        # 1. Extract the model response (support both raw and parsed).
        response = response_data.get("parsed_result", response_data.get("result", ""))

        # 2. Extract metadata from the prompt
        prompt_dict = response_data.get("prompt", {})
        metadata = prompt_dict.get("metadata", {})

        # 3. Subset name (e.g. poetry / numerical / github_prs) may be provided by the harness
        subset_name = response_data.get("subset")  # may be None

        # 4. Compute metrics with subset-aware evaluator
        results = evaluate_response(str(response), metadata, subset=subset_name)
        score = float(results.get("micro_f1", 0.0))

        # 5. Emit machine-readable output for downstream aggregation
        print(json.dumps({"score": score, "details": results}, ensure_ascii=False))
        return score

    except Exception as exc:  # pragma: no cover – safety net
        print(json.dumps({"score": 0.0, "details": {"error": str(exc)}}))
        return 0.0
