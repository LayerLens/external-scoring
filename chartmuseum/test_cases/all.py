"""ChartMuseum scorer (lane-1 external_scoring) — LLM-as-judge.

Faithful port of ChartMuseum's official grader (github.com/Liyan06/ChartMuseum,
evaluate.py + prompt.py). EVERY item is LLM-judged — there is NO exact-match
branch. The judge sees TEXT ONLY: the question, the gold answer, and the answer
extracted from the model's `<answer>...</answer>` block. Vision (the chart image)
is in the prompt the model under test saw, never in the judge call.

Pipeline (mirrors AnswerEvaluator.extract_answer + AnswerCompareGenerator):
  1. Extract the model's answer with the upstream regex on `text + '</answer>'`
     (the appended tag tolerates truncated/missing closing tags). Empty if none.
  2. Fill COMPARE_ANSWER_PROMPT verbatim (numeric-tolerance + unit-handling + text
     rules). [QUESTION]=question, [ANSWER1]=gold, [ANSWER2]=extracted model answer.
  3. One OpenRouter chat call, model gpt-4.1-mini-2025-04-14, temperature 0.
  4. Verdict = 1.0 if 'yes' in response.lower() else 0.0  (substring, as upstream).

A hard judge failure (no API key, exhausted retries, malformed payload) surfaces
as an error (print + return 0.0) — never a silent pass.

Contract (scoring_runner.py): ll_run_tests(response_data) -> float|bool.
  response_data["result"]/["parsed_result"]            -> model's single completion
  response_data["prompt"]["truth"]/["parsed_truth"]    -> gold short-text answer
  response_data["prompt"]["metadata"]["question"]      -> question text (copied in
      at build time; falls back to digging the question out of input).
"""
from __future__ import annotations

import os
import re
import time
from typing import Any

import requests

# --- Judge configuration (ChartMuseum official) ---------------------------------
JUDGE_MODEL = "gpt-4.1-mini-2025-04-14"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
# simpleqa (the proven prod scorer) reads `OpenRouterApiKey`; the local go-evaluator
# .env exposes `OPENROUTER_API_KEY`. Accept either so the scorer works in both.
_API_KEY_ENV_NAMES = ("OpenRouterApiKey", "OPENROUTER_API_KEY")

# Retry/backoff kept well within the harness's 30s/prompt budget.
MAX_RETRIES = 3
BACKOFF_SECONDS = 3.0
REQUEST_TIMEOUT_SECONDS = 20

# --- Prompts (copied VERBATIM from ChartMuseum prompt.py) ------------------------
COMPARE_ANSWER_PROMPT = """You are provided with a question and two answers. Please determine if these answers are equivalent. Follow these guidelines:

1. Numerical Comparison:
   - For decimal numbers, consider them as equivalent if their relative difference is sufficiently small.
   For example, the following pairs are equivalent:
    - 32.35 and 32.34
    - 90.05 and 90.00
    - 83.3% and 83.2%
    - 31 and 31%
   The following pairs are not equivalent:
   - 32.35 and 35.25
   - 90.05 and 91.05
   - 83.3% and 45.2%

   Note that if the question asks for years or dates, please do the exact match with no error tolerance.

2. Unit Handling:
   - If only one answer includes units (e.g. '$', '%', '-', etc.), ignore the units and compare only the numerical values
   For example, the following pairs are equivalent:
   - 305 million and 305 million square meters
   - 0.75 and 0.75%
   - 0.6 and 60%
   - $80 and 80
   The following pairs are not equivalent:
   - 305 million and 200 million square meters
   - 0.75 and 0.90%

3. Text Comparison:
   - Ignore differences in capitalization
   - Treat mathematical expressions in different but equivalent forms as the same (e.g., "2+3" = "5")

Question: [QUESTION]
Answer 1: [ANSWER1]
Answer 2: [ANSWER2]

Please respond with:
- "Yes" if the answers are equivalent
- "No" if the answers are different"""


class JudgeError(Exception):
    """Raised when the judge cannot return a usable verdict (surfaced, not swallowed)."""


def _get_api_key() -> str:
    for name in _API_KEY_ENV_NAMES:
        val = os.getenv(name)
        if val:
            return val
    raise JudgeError(
        "No OpenRouter API key in environment "
        f"(checked {', '.join(_API_KEY_ENV_NAMES)})"
    )


def extract_answer(text: str) -> str:
    """Extract <answer>...</answer> (upstream evaluate.py:extract_answer).

    Appends a closing tag so a truncated/missing </answer> still matches; returns
    "" when there is no <answer> tag at all.
    """
    answer_pattern = r"<answer>(.*?)</answer>"
    answer_match = re.search(answer_pattern, text + "</answer>", re.DOTALL)
    return answer_match.group(1).strip() if answer_match else ""


def _build_question(response_data: dict[str, Any]) -> str:
    """Question text: prefer metadata.question (copied in at build time)."""
    prompt = response_data.get("prompt", {}) or {}
    meta = prompt.get("metadata", {}) or {}
    q = meta.get("question")
    if q:
        return str(q)
    # Fallback: dig the user text out of the input (content may be a string or
    # OpenAI content-parts list for the multimodal prompt).
    for msg in prompt.get("input", []) or []:
        if msg.get("role") != "user":
            continue
        content = msg.get("content")
        if isinstance(content, str):
            return content
        if isinstance(content, list):
            for part in content:
                if isinstance(part, dict) and part.get("type") == "text":
                    return str(part.get("text", ""))
    return ""


def call_judge(prompt: str) -> str:
    """One OpenRouter chat call (temp 0), with retry/backoff. Returns raw content.

    Raises JudgeError if no usable response is obtained after retries — the caller
    converts that to a printed error + 0.0 (never a silent pass).
    """
    api_key = _get_api_key()
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    data = {
        "model": JUDGE_MODEL,
        "temperature": 0,
        "messages": [{"role": "user", "content": prompt}],
    }

    last_err = ""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = requests.post(
                OPENROUTER_URL, headers=headers, json=data, timeout=REQUEST_TIMEOUT_SECONDS
            )
            if resp.status_code == 200:
                payload = resp.json()
                return payload["choices"][0]["message"]["content"].strip()
            last_err = f"HTTP {resp.status_code}: {resp.text[:300]}"
            print(f"Judge call attempt {attempt} failed: {last_err}")
        except Exception as exc:  # noqa: BLE001
            last_err = str(exc)
            print(f"Judge call attempt {attempt} errored: {last_err}")
        if attempt < MAX_RETRIES:
            print(f"Retrying judge in {BACKOFF_SECONDS}s...")
            time.sleep(BACKOFF_SECONDS)

    raise JudgeError(f"Judge failed after {MAX_RETRIES} attempts: {last_err}")


def ll_run_tests(response_data: dict[str, Any]) -> float:  # noqa: N802
    """Entry point for the LayerLens external-scoring harness.

    Returns 1.0 if the judge deems the model's extracted answer equivalent to the
    gold answer, else 0.0. Any hard failure prints an error and returns 0.0.
    """
    try:
        model_text = response_data.get("parsed_result", response_data.get("result", "")) or ""
        prompt = response_data.get("prompt", {}) or {}
        gold = prompt.get("parsed_truth", prompt.get("truth", "")) or ""
        question = _build_question(response_data)

        if not str(gold).strip():
            print("No gold answer present; scoring 0.0")
            return 0.0

        model_answer = extract_answer(str(model_text))
        print(f"Question: {question}")
        print(f"Gold: {gold}")
        print(f"Extracted model answer: {model_answer!r}")

        judge_prompt = (
            COMPARE_ANSWER_PROMPT.replace("[QUESTION]", str(question))
            .replace("[ANSWER1]", str(gold))
            .replace("[ANSWER2]", str(model_answer))
        )

        verdict = call_judge(judge_prompt)
        print(f"Judge verdict: {verdict!r}")
        # Replicate upstream substring rule exactly.
        return 1.0 if "yes" in verdict.lower() else 0.0

    except Exception as exc:  # noqa: BLE001
        # Hard failure (incl. JudgeError) is surfaced, never a silent pass.
        print(f"Scorer error: {exc}")
        return 0.0
