r"""ScreenSpot-Pro scorer (lane-1 external_scoring), GUI grounding.

Source benchmark: likaixin/ScreenSpot-Pro (MIT). Official grader:
github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding (eval_screenspot_pro.py +
models/gpt4x.py). The model is shown a high-res screenshot + an instruction and
must output the bounding box of the target UI element as normalised coords
`[[x0,y0,x1,y1]]` (0-1). Correctness = the predicted CLICK POINT (the bbox
midpoint, or a directly-emitted point) falls inside the ground-truth bbox.

Contract (scoring_runner.py): ll_run_tests(response_data) -> float.
  model text  = response_data["parsed_result" | "result"]
  gt bbox     = response_data["prompt"]["metadata"]["normalized_bbox"]  ([x0,y0,x1,y1], 0-1)
  img_size    = response_data["prompt"]["metadata"]["img_size"]         ([W,H] pixels)

We read the NORMALISED ground-truth bbox straight from prompt metadata, so the
scorer needs neither the image nor any pip dependency (stdlib `re` + arithmetic).

----------------------------------------------------------------------------
EXTRACTION (faithful to the official models/gpt4x.py regexes)
  point regex : r"\[\[(\d+\.\d+|\d+),(\d+\.\d+|\d+)\]\]"
  bbox  regex : r"\[\[(\d+\.\d+|\d+),(\d+\.\d+|\d+),(\d+\.\d+|\d+),(\d+\.\d+|\d+)\]\]"
The official model parser tries a direct point first; if absent but a bbox is
present, it uses the bbox midpoint  [(x0+x2)/2, (y0+y2)/2]  as the click point.
We mirror that order. A 4-number bracket also matches the 2-number point regex
on its first two numbers, so we MUST test the bbox (4-number) pattern first and
only fall back to the bare point pattern, otherwise "[[a,b,c,d]]" would be
mis-read as the point (a,b). No match anywhere -> 0.0 (wrong_format).

----------------------------------------------------------------------------
PIXEL-vs-NORMALISED ROBUSTNESS DEVIATION  (deliberate, documented)
The STRICT official harness assumes the model emits NORMALISED coords (0-1) and
compares them directly against the normalised gt bbox. Real-world VLMs very
often emit PIXEL coords instead (e.g. [[1774,1586,2113,1618]]). Under the strict
harness those score 0 purely on a unit mismatch, not on grounding ability.

Our deviation: after extracting the click point, if ANY of its coordinates is
> 1.0 we treat the point as PIXELS and divide by the embedded img_size
([W,H]) to normalise it before the in-bbox test. Points already in [0,1] are
used as-is (identical to the strict harness for compliant models). A reviewer
should note this is a superset of the official behaviour: it never changes the
verdict for a model that follows the normalised-coords instruction, and only
rescues otherwise-correct pixel-space predictions.
"""
from __future__ import annotations

import json
import re
import signal
from typing import Any

# Official ScreenSpot-Pro regexes (models/gpt4x.py). 4-number (bbox) tried first.
_BBOX_RE = re.compile(
    r"\[\[(\d+\.\d+|\d+),(\d+\.\d+|\d+),(\d+\.\d+|\d+),(\d+\.\d+|\d+)\]\]"
)
_POINT_RE = re.compile(r"\[\[(\d+\.\d+|\d+),(\d+\.\d+|\d+)\]\]")

GRADE_TIMEOUT_SECONDS = 15  # well under the harness's 30s/prompt wall


class _GradeTimeout(Exception):
    pass


def _on_alarm(signum: int, frame: Any) -> None:  # noqa: ANN401
    raise _GradeTimeout()


def _extract_click_point(text: str) -> tuple[float, float] | None:
    """Return the predicted click point (raw, un-normalised) or None.

    Mirrors the official parser: a 4-number bbox -> midpoint; else a bare
    2-number point used directly. Bbox is matched FIRST because a bbox literal
    also satisfies the 2-number point regex.
    """
    m = _BBOX_RE.search(text)
    if m:
        x0, y0, x1, y1 = (float(g) for g in m.groups())
        return (x0 + x1) / 2.0, (y0 + y1) / 2.0
    m = _POINT_RE.search(text)
    if m:
        return float(m.group(1)), float(m.group(2))
    return None


def _normalize_truth(metadata: dict[str, Any]) -> list[float] | None:
    """Pull the normalised gt bbox [x0,y0,x1,y1] (0-1) from prompt metadata.

    Accepts either a list or a JSON-string (the builder stores a list, but be
    tolerant). Returns None if absent/malformed.
    """
    nb = metadata.get("normalized_bbox")
    if isinstance(nb, str):
        try:
            nb = json.loads(nb)
        except (ValueError, TypeError):
            return None
    if not isinstance(nb, (list, tuple)) or len(nb) != 4:
        return None
    try:
        return [float(v) for v in nb]
    except (ValueError, TypeError):
        return None


def _grade(model_text: str, metadata: dict[str, Any]) -> float:
    pt = _extract_click_point(model_text)
    if pt is None:
        print("No parsable point/bbox in model output; wrong_format -> 0.0")
        return 0.0

    gt = _normalize_truth(metadata)
    if gt is None:
        print("No usable normalized_bbox in prompt metadata; scoring 0.0")
        return 0.0

    px, py = pt
    # Robustness deviation: pixel coords (> 1.0) -> divide by img_size to normalise.
    if px > 1.0 or py > 1.0:
        img_size = metadata.get("img_size")
        if (
            not isinstance(img_size, (list, tuple))
            or len(img_size) != 2
            or not all(isinstance(v, (int, float)) and v > 0 for v in img_size)
        ):
            print("Pixel-space point but no usable img_size to normalise; scoring 0.0")
            return 0.0
        w, h = float(img_size[0]), float(img_size[1])
        px, py = px / w, py / h

    x0, y0, x1, y1 = gt
    # gt bbox is xyxy with x0<=x1, y0<=y1 (builder guarantees this).
    hit = (x0 <= px <= x1) and (y0 <= py <= y1)
    return 1.0 if hit else 0.0


def ll_run_tests(response_data: dict[str, Any]) -> float:  # noqa: N802
    """Entry point for the LayerLens external-scoring harness.

    1.0 if the model's predicted click point lands inside the ground-truth
    UI-element bounding box, else 0.0.
    """
    try:
        # or-chain: a None/empty parsed_result falls through to result.
        model_text = (
            response_data.get("parsed_result") or response_data.get("result") or ""
        )
        prompt = response_data.get("prompt", {}) or {}
        metadata = prompt.get("metadata", {}) or {}

        old_handler = signal.signal(signal.SIGALRM, _on_alarm)
        signal.alarm(GRADE_TIMEOUT_SECONDS)
        try:
            return _grade(str(model_text), metadata)
        finally:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, old_handler)

    except _GradeTimeout:
        print(f"Grading exceeded {GRADE_TIMEOUT_SECONDS}s; scoring 0.0")
        return 0.0
    except Exception as exc:  # noqa: BLE001
        print(f"Scorer error: {exc}")
        return 0.0
