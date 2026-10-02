"""Unit tests for the TutorBench scorer.

Run from the repo root (needs only ``requests``, the scorer's own dependency):

    python3 tutorbench/tests/test_rubric_grading.py

Lives outside ``test_cases/`` on purpose: go-evaluator ships only
``{repository}/test_cases`` and ``requirements.txt`` to the evaluator instance,
so tests here never reach the scoring sandbox and need no runtime dependency.
"""

from __future__ import annotations

import os
import sys
import unittest
from unittest import mock

sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "test_cases"),
)

import rubric_grading as rg  # noqa: E402


VERDICT = '{"explanation": "ok", "criterion_satisfied": true}'


class ParseJudgeReply(unittest.TestCase):
    """The judge ignores "return just the json object" often enough that the
    verdict has to be found anywhere in the reply."""

    def test_bare_object(self):
        self.assertEqual(rg.parse_json_to_dict(VERDICT)["criterion_satisfied"], True)

    def test_fenced_object(self):
        for fence in ("```json", "```"):
            with self.subTest(fence=fence):
                reply = f"{fence}\n{VERDICT}\n```"
                self.assertEqual(
                    rg.parse_json_to_dict(reply)["criterion_satisfied"], True
                )

    def test_prose_then_fenced_object(self):
        """The prod failure: 118 of 119 judge errors on a 1473-row run."""
        reply = f"Looking at the criterion, the response does X.\n\n```json\n{VERDICT}\n```"
        self.assertEqual(rg.parse_json_to_dict(reply)["criterion_satisfied"], True)

    def test_prose_then_bare_object(self):
        reply = f"Looking at the criterion...\n{VERDICT}"
        self.assertEqual(rg.parse_json_to_dict(reply)["criterion_satisfied"], True)

    def test_trailing_prose_after_object(self):
        reply = f"{VERDICT}\n\nHope that helps."
        self.assertEqual(rg.parse_json_to_dict(reply)["criterion_satisfied"], True)

    def test_last_verdict_wins_when_example_is_echoed(self):
        reply = (
            'The prompt showed {"explanation": "x", "criterion_satisfied": true} '
            'as an example.\n\n```json\n'
            '{"explanation": "actually no", "criterion_satisfied": false}\n```'
        )
        parsed = rg.parse_json_to_dict(reply)
        self.assertEqual(parsed["criterion_satisfied"], False)
        self.assertEqual(parsed["explanation"], "actually no")

    def test_braces_inside_strings_do_not_open_a_span(self):
        reply = (
            'Reasoning about $\\frac{d}{dx}$ here.\n'
            '{"explanation": "the set {1, 2} and a \\" quote", '
            '"criterion_satisfied": false}'
        )
        parsed = rg.parse_json_to_dict(reply)
        self.assertEqual(parsed["criterion_satisfied"], False)
        self.assertIn("{1, 2}", parsed["explanation"])

    def test_unescaped_inner_quotes_still_yield_the_verdict(self):
        """Prod: the judge quotes the student verbatim inside explanation and
        does not escape it, so the object is complete but invalid JSON."""
        reply = (
            '```json\n{\n  "explanation": "The student \'claims a z-score "around 2" '
            'without showing work\' here.",\n  "criterion_satisfied": true\n}\n```'
        )
        self.assertEqual(rg.parse_json_to_dict(reply)["criterion_satisfied"], True)

    def test_salvage_reads_the_verdict_not_the_first_boolean(self):
        reply = (
            'Malformed "criterion_satisfied": true in a quoted example,\n'
            '{"explanation": "broken "quote" here", "criterion_satisfied": false}'
        )
        self.assertEqual(rg.parse_json_to_dict(reply)["criterion_satisfied"], False)

    def test_truncated_object_is_not_half_parsed(self):
        reply = 'Looking at the criterion: {"explanation": "it was cut off'
        self.assertEqual(rg.parse_json_to_dict(reply), {})

    def test_prose_with_no_object_at_all(self):
        self.assertEqual(rg.parse_json_to_dict("Looking at the criterion"), {})

    def test_verdictless_object_does_not_block_salvage(self):
        reply = (
            'Context: {"note": "unrelated"}\n'
            '{"explanation": "student said "x" here", "criterion_satisfied": false}'
        )
        self.assertEqual(rg.parse_json_to_dict(reply)["criterion_satisfied"], False)

    def test_non_object_json_is_rejected(self):
        self.assertEqual(rg.parse_json_to_dict("[1, 2, 3]"), {})


class SignConvention(unittest.TestCase):
    """Guards the inversion the module docstring warns about: a SATISFIED
    prohibition means the model behaved well and must not subtract."""

    def test_positive_pays_out_when_satisfied(self):
        item = rg.RubricItem(criterion="c", points=5)
        self.assertEqual(rg.contribution(item, satisfied=True), 5)
        self.assertEqual(rg.contribution(item, satisfied=False), 0)

    def test_penalty_costs_only_when_violated(self):
        item = rg.RubricItem(criterion="must not reveal", points=-5)
        self.assertEqual(rg.contribution(item, satisfied=True), 0)
        self.assertEqual(rg.contribution(item, satisfied=False), -5)

    def test_arr_w_excludes_negative_weights_from_denominator(self):
        items = [
            rg.RubricItem(criterion="a", points=5),
            rg.RubricItem(criterion="b", points=1),
            rg.RubricItem(criterion="must not", points=-5),
        ]
        verdicts = [
            {"criterion_satisfied": True},
            {"criterion_satisfied": True},
            {"criterion_satisfied": True},
        ]
        self.assertAlmostEqual(rg.calculate_score(items, verdicts), 1.0)

        verdicts[2] = {"criterion_satisfied": False}
        self.assertAlmostEqual(rg.calculate_score(items, verdicts), (6 - 5) / 6)


class JsonModeFallback(unittest.TestCase):
    """A provider that rejects response_format must not become a hard failure."""

    def setUp(self):
        rg._json_mode_disabled = False
        self.addCleanup(setattr, rg, "_json_mode_disabled", False)
        self.config = rg.JudgeConfig(
            api_key="k",
            model_id="m",
            base_url="https://example.invalid/v1",
            concurrency=1,
            max_attempts=3,
            timeout_seconds=1.0,
            backoff_base_seconds=0.01,
            send_images=False,
            json_mode=True,
        )

    @staticmethod
    def _response(status, text="", body=None):
        r = mock.Mock()
        r.status_code = status
        r.text = text
        r.json.return_value = body or {}
        return r

    def test_finish_reason_is_returned_with_the_text(self):
        ok = self._response(
            200,
            body={"choices": [{"message": {"content": VERDICT}, "finish_reason": "length"}]},
        )
        with mock.patch.object(rg.requests, "post", return_value=ok):
            self.assertEqual(
                rg._post_judge_request(self.config, "prompt", []), (VERDICT, "length")
            )

    def test_response_format_is_sent_by_default(self):
        ok = self._response(200, body={"choices": [{"message": {"content": VERDICT}}]})
        with mock.patch.object(rg.requests, "post", return_value=ok) as post:
            rg._post_judge_request(self.config, "prompt", [])
        self.assertEqual(
            post.call_args.kwargs["json"]["response_format"], {"type": "json_object"}
        )

    def test_rejection_disables_json_mode_and_is_retryable(self):
        bad = self._response(400, text="response_format is not supported")
        with mock.patch.object(rg.requests, "post", return_value=bad):
            with self.assertRaises(rg._RetryableJudgeError):
                rg._post_judge_request(self.config, "prompt", [])
        self.assertTrue(rg._json_mode_disabled)

        ok = self._response(200, body={"choices": [{"message": {"content": VERDICT}}]})
        with mock.patch.object(rg.requests, "post", return_value=ok) as post:
            rg._post_judge_request(self.config, "prompt", [])
        self.assertNotIn("response_format", post.call_args.kwargs["json"])

    def test_json_mode_can_be_disabled_by_env(self):
        with mock.patch.dict(
            os.environ,
            {
                "JUDGE_API_KEY": "k",
                "JUDGE_MODEL_ID": "m",
                "JUDGE_BASE_URL": "https://example.invalid/v1",
                "TUTORBENCH_JUDGE_JSON_MODE": "0",
            },
        ):
            self.assertFalse(rg.load_judge_config().json_mode)


class GradeCriterionRecovery(unittest.TestCase):
    def setUp(self):
        self.config = rg.JudgeConfig(
            api_key="k",
            model_id="m",
            base_url="https://example.invalid/v1",
            concurrency=1,
            max_attempts=3,
            timeout_seconds=1.0,
            backoff_base_seconds=0.01,
            send_images=False,
            json_mode=False,
        )

    def test_preambled_reply_no_longer_exhausts_the_retry_budget(self):
        item = rg.RubricItem(criterion="c", points=1)
        preambled = f"Looking at the criterion, I need to check...\n\n```json\n{VERDICT}\n```"
        with mock.patch.object(
            rg, "_post_judge_request", return_value=(preambled, "stop")
        ):
            verdict = rg.grade_criterion(self.config, "convo", item, 1, [])
        self.assertEqual(verdict["criterion_satisfied"], True)

    def test_missing_finish_reason_is_treated_as_complete(self):
        item = rg.RubricItem(criterion="c", points=1)
        with mock.patch.object(rg, "_post_judge_request", return_value=(VERDICT, None)):
            verdict = rg.grade_criterion(self.config, "convo", item, 1, [])
        self.assertEqual(verdict["criterion_satisfied"], True)

    def test_truncated_reply_is_never_read_as_a_verdict(self):
        """A reply cut off at max_tokens that echoed the prompt's worked
        example (verdict true) must fail the attempt, not pass the criterion -
        neither via a balanced span nor via salvage."""
        item = rg.RubricItem(criterion="c", points=1)
        echoed = (
            'Like the example {"explanation": "obeyed", "criterion_satisfied": true}, '
            'I check whether "criterion_satisfied": true holds here. The student'
        )
        with mock.patch.object(
            rg, "_post_judge_request", return_value=(echoed, "length")
        ) as post:
            with self.assertRaises(rg.JudgeCallError) as ctx:
                rg.grade_criterion(self.config, "convo", item, 1, [])
        self.assertEqual(post.call_count, self.config.max_attempts)
        self.assertIn("truncated", str(ctx.exception))

    def test_unusable_reply_still_raises_rather_than_defaulting(self):
        item = rg.RubricItem(criterion="c", points=1)
        with mock.patch.object(
            rg, "_post_judge_request", return_value=("no json here", "stop")
        ):
            with self.assertRaises(rg.JudgeCallError):
                rg.grade_criterion(self.config, "convo", item, 1, [])


if __name__ == "__main__":
    unittest.main()
