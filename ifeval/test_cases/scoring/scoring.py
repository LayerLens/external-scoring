"""Scoring functions for instruction following evaluation."""

import re
from dataclasses import dataclass
from typing import Any, Dict, List

from scoring.instructions_registry import INSTRUCTION_DICT


@dataclass
class InputCriteria:
  """Input criteria for evaluation."""
  instruction_id_list: List[str]
  kwargs: List[Dict[str, Any]]


@dataclass
class OutputResult:
  """Output result of the evaluation."""
  follow_instructions: List[bool]
  follow_all_instructions: bool


def evaluate_strict(criteria: InputCriteria, response: str) -> OutputResult:
  """Evaluates whether a response strictly follows all instructions.

  This is a pure function implementation of the strict evaluation logic from
  evaluation_lib.py. It checks if the given response follows all the instructions
  specified in the criteria.

  Args:
    criteria: The instruction criteria containing instruction IDs and their kwargs.
    response: The model's response text.

  Returns:
    OutputResult containing a list of boolean values indicating which instructions
    were followed, and a boolean indicating if all instructions were followed.
  """
  if not response.strip():
    # Empty response doesn't follow any instructions
    is_following_list = [False] * len(criteria.instruction_id_list)
    return OutputResult(
        follow_instructions=is_following_list,
        follow_all_instructions=False
    )

  is_following_list = []

  # Check each instruction
  for index, instruction_id in enumerate(criteria.instruction_id_list):
    instruction_cls = INSTRUCTION_DICT[instruction_id]
    instruction = instruction_cls(instruction_id)
    instruction.build_description(**criteria.kwargs[index])
    
    # Check if the response follows this instruction
    if response.strip() and instruction.check_following(response):
      is_following_list.append(True)
    else:
      is_following_list.append(False)

  # A response follows all instructions if and only if it follows each individual instruction
  follow_all = all(is_following_list)

  return OutputResult(
      follow_instructions=is_following_list,
      follow_all_instructions=follow_all
  )


def _try_variations(response):
  """Try different variations of the response to check if any of them follow instructions.
  
  Args:
    response: The original response text.
    
  Returns:
    List of response variations to check.
  """
  variations = []
  
  # Original response
  variations.append(response)
  
  # Remove first line if it's empty or just whitespace
  lines = response.splitlines()
  if lines and not lines[0].strip():
    variations.append('\n'.join(lines[1:]))
    
  # Remove last line if it's empty or just whitespace
  if lines and not lines[-1].strip():
    variations.append('\n'.join(lines[:-1]))
    
  # Remove asterisks
  variations.append(re.sub(r'\*', '', response))
  
  return variations


def evaluate_loose(criteria: InputCriteria, response: str) -> OutputResult:
  """Evaluates whether a response loosely follows all instructions.
  
  Unlike the strict evaluation, this function tries multiple variations of the response
  to see if any of them follow the instructions. It's a more lenient evaluation that
  allows for some formatting variations.

  Args:
    criteria: The instruction criteria containing instruction IDs and their kwargs.
    response: The model's response text.

  Returns:
    OutputResult containing a list of boolean values indicating which instructions
    were followed, and a boolean indicating if all instructions were followed.
  """
  if not response.strip():
    # Empty response doesn't follow any instructions
    is_following_list = [False] * len(criteria.instruction_id_list)
    return OutputResult(
        follow_instructions=is_following_list,
        follow_all_instructions=False
    )
  
  # Try different variations of the response
  variations = _try_variations(response)
  
  # Check each variation with strict evaluation and combine results
  # An instruction is followed if ANY variation follows it
  all_results = [evaluate_strict(criteria, variation) for variation in variations]
  
  # For each instruction index, check if ANY variation follows it
  is_following_list = []
  for i in range(len(criteria.instruction_id_list)):
    # Check if instruction i is followed in any variation
    instruction_followed = any(result.follow_instructions[i] for result in all_results)
    is_following_list.append(instruction_followed)
  
  # A response loosely follows all instructions if and only if 
  # it follows each individual instruction in at least one variation
  follow_all = all(is_following_list)
  
  return OutputResult(
      follow_instructions=is_following_list,
      follow_all_instructions=follow_all
  )
