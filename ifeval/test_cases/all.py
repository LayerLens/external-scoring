"""Instruction Following Evaluation (IFEval) logic.

This module provides the `ll_run_tests` entry-point expected by the LayerLens
scoring harness. It evaluates whether a model's response follows given instructions
and returns a score between 0 and 1.
"""
from __future__ import annotations

import json
import os
import sys
from typing import Any, Dict

# Add the directory containing this file to sys.path
# This ensures we can import the scoring module regardless of working directory
this_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, this_dir)

# Now import from the scoring module
from scoring.scoring import evaluate_strict, InputCriteria

# Optional metadata dict (kept for parity with other benchmarks)
METADATA: Dict[str, Any] = {}


def ll_run_tests(response_data: Dict[str, Any]) -> float:  # noqa: N802
    """Entry point used by the evaluation harness.

    The harness passes *response_data* containing at least:
        - ``result`` or ``parsed_result``: the model's raw output.
        - ``prompt``: a dict which itself contains ``metadata`` with
          instruction details like "instruction_id_list" and "kwargs".

    Args:
        response_data: Dictionary containing the model response and prompt metadata.

    Returns:
        A float score between 0 and 1 indicating instruction following performance.
    """
    try:
        # 1. Extract the model response (support both raw and parsed)
        response = response_data.get("parsed_result", response_data.get("result", ""))

        # 2. Extract the original prompt and metadata
        prompt_dict = response_data.get("prompt", {})
        metadata = prompt_dict.get("metadata", {})
        
        # Get the instruction ID list and kwargs from metadata
        instruction_id_list = metadata.get("instruction_id_list", [])
        kwargs = metadata.get("kwargs", [])
        
        # Ensure we have corresponding kwargs for each instruction
        if len(kwargs) != len(instruction_id_list):
            kwargs = [{} for _ in range(len(instruction_id_list))]
            
        # 3. Create the input criteria
        criteria = InputCriteria(
            instruction_id_list=instruction_id_list,
            kwargs=kwargs
        )
        
        # 4. Evaluate the response using the strict evaluation function
        result = evaluate_strict(criteria, response)
        
        # 5. Calculate the final score (1.0 if all instructions followed, 0.0 otherwise)
        score = float(result.follow_all_instructions)
        
        # 6. Prepare detailed results
        details = {
            "follow_instructions": result.follow_instructions,
            "follow_all_instructions": result.follow_all_instructions,
            "instruction_ids": instruction_id_list
        }
        
        # 7. Emit machine-readable output for downstream aggregation
        print(json.dumps({"score": score, "details": details}, ensure_ascii=False))
        return score

    except Exception as exc:  # pragma: no cover – safety net
        print(json.dumps({"score": 0.0, "details": {"error": str(exc)}}))
        return 0.0
