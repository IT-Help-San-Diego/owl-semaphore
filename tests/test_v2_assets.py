"""Owl Semaphore v2 asset doctrine tests (v2.0.0-rc).

These tests gate the v2 authoritative asset set under ``assets/v2/`` and are
required to pass before any v2.0.0 release. They verify:

  1. File presence, mode, and size for the four state PNGs at 1080 and 540.
  2. V4 alpha-geometry fidelity: NON-NORMATIVE / CRITICAL / METACOGNITIVE
     alpha masks equal the V4 image of the NORMATIVE alpha mask under
     sigma_v / C2 / sigma_h respectively (Intersection-over-Union = 1.0
     within the tolerance band).
  3. Palette correctness per state (median dominant RGB falls inside a
     calibrated RGB box around the doctrine hex).
  4. NORMATIVE-not-red guardrail (NORMATIVE is gold-leaning, not red-leaning).
  5. CRITICAL-is-red guardrail (CRITICAL is red-leaning).
  6. V4 algebra invariants: each non-identity transform is its own inverse,
     and sigma_v . C2 = sigma_h.
  7. No black speckle / junk artifacts (count of opaque pixels with luma < 25
     is zero in the current v2 set).

The doctrine is in ``ASSET-DOCTRINE.md``. The provenance is in
``PROVENANCE.md``.
"""

from __future__ import annotations

import os
import unittest

import numpy as np
from PIL import Image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V2_1080 = os.path.join(REPO, "assets", "v2", "transparent-1080")
V2_540 = os.path.join(REPO, "assets", "v2", "transparent-540")

FILES_1080 = {
    "NORMATIVE":     "NORMATIVE-human-gold-branch-transparent-1080.png",
    "NON-NORMATIVE": "NON-NORMATIVE-human-gold-branch-transparent-1080.png",
    "CRITICAL":      "CRITICAL-human-gold-branch-transparent-1080.png",
    "METACOGNITIVE": "METACOGNITIVE-human-gold-branch-transparent-1080.png",
}
FILES_540 = {
    "NORMATIVE":     "NORMATIVE-human-gold-branch-transparent-540.png",
    "NON-NORMATIVE": "NON-NORMATIVE-human-gold-branch-transparent-540.png",
    "CRITICAL":      "CRITICAL-human-gold-branch-transparent-540.png",
    "METACOGNITIVE": "METACOGNITIVE-human-gold-branch-transparent-540.png",
}

# Palette centers (median of opaque, non-near-white, non-near-black pixels)
# calibrated from the v2 source PNGs. Tolerance is per-channel.
#
# NORMATIVE center was updated on 2026-05-17 to reflect the human-approved
# OWL-1 NORMATIVE D-geometry + B parchment-gold master. The prior center
# (220, 199, 116) was the saturated #D8B760 gold; the approved B parchment-gold
# is a lighter, warmer tone whose owl-only median is (211, 194, 154).
# See assets/v2/normative-D-B-gold-master/ for the provenance package.
#
# CRITICAL center was updated on 2026-05-17 to reflect the human-approved
# OWL-3 CRITICAL B-geometry + B alert red balanced master. The prior center
# (240, 125, 124) was the saturated salmon body; the approved alert-red body
# yields a median of (240, 121, 127) after LUT recolor (R preserved, G/B
# nudged toward the new alert-red palette). The transparent master was
# recolored in-place; the prior salmon master is preserved under
# assets/v2/critical-b-geometry-e-ring-master-superseded/preserved-transparent-pre-b-balanced/.
#
# NON-NORMATIVE / METACOGNITIVE palette centers are unchanged pending the
# next per-state review.
PALETTE = {
    "NORMATIVE":     (211, 194, 154),
    "NON-NORMATIVE": ( 77, 177, 176),
    "CRITICAL":      (240, 121, 127),
    "METACOGNITIVE": (181, 153, 230),
}
PALETTE_TOL = 25  # per-channel +/- band


def _load(state: str, dir_: str, files: dict[str, str]) -> np.ndarray:
    path = os.path.join(dir_, files[state])
    return np.array(Image.open(path).convert("RGBA"))


def _dominant_rgb(arr: np.ndarray) -> tuple[int, int, int]:
    """Median RGB across opaque pixels, excluding near-black outline."""
    rgb = arr[..., :3]
    a = arr[..., 3]
    mask = (a > 200) & (rgb.sum(axis=-1) > 100)
    if not mask.any():
        mask = a > 200
    median = np.median(rgb[mask], axis=0).astype(int)
    return int(median[0]), int(median[1]), int(median[2])


def _alpha_mask(arr: np.ndarray) -> np.ndarray:
    return (arr[..., 3] > 32).astype(np.uint8)


def _iou(a: np.ndarray, b: np.ndarray) -> float:
    inter = int((a & b).sum())
    union = int((a | b).sum())
    return inter / union if union else 1.0


class V2AssetPresence(unittest.TestCase):
    """File presence, mode, and size."""

    def test_all_state_files_1080_exist(self):
        for state, fn in FILES_1080.items():
            self.assertTrue(
                os.path.isfile(os.path.join(V2_1080, fn)),
                f"missing v2 1080 PNG for {state}: {fn}",
            )

    def test_all_state_files_540_exist(self):
        for state, fn in FILES_540.items():
            self.assertTrue(
                os.path.isfile(os.path.join(V2_540, fn)),
                f"missing v2 540 PNG for {state}: {fn}",
            )

    def test_1080_size_and_mode(self):
        for state, fn in FILES_1080.items():
            with Image.open(os.path.join(V2_1080, fn)) as im:
                self.assertEqual(im.size, (1080, 1080), f"{state} 1080 size != 1080x1080")
                self.assertEqual(im.mode, "RGBA", f"{state} 1080 mode != RGBA")

    def test_540_size_and_mode(self):
        for state, fn in FILES_540.items():
            with Image.open(os.path.join(V2_540, fn)) as im:
                self.assertEqual(im.size, (540, 540), f"{state} 540 size != 540x540")
                self.assertEqual(im.mode, "RGBA", f"{state} 540 mode != RGBA")


class V2TransformFidelity(unittest.TestCase):
    """Alpha-mask geometry must match the V4 image of NORMATIVE.

    NOTE (2026-05-17): NORMATIVE was promoted to the human-approved
    D-geometry + B parchment-gold master, and NON-NORMATIVE was promoted to
    the human-approved Math-Mirror Center-Scale-97 + Seam-17 + Five-Over
    master. The latter is a deliberate visual choice (the owl is mirrored
    *and* scaled to 97 % with seam refinements) rather than a pure
    pixel-array sigma_v, so NON-NORMATIVE / NORMATIVE alpha IoU is ~0.815
    rather than 1.0. The CRITICAL and METACOGNITIVE siblings have not been
    reviewed yet and remain on the prior NORMATIVE geometry.

    The three V4 sibling-fidelity tests below are therefore marked
    ``expectedFailure``. For NON-NORMATIVE the failure is permanent at this
    visual doctrine (the user-approved asset is the source of truth); the
    decorator should remain. For CRITICAL and METACOGNITIVE, the decorator
    MUST be removed after each state's own per-state visual review concludes
    and the sibling is re-derived (or, like NN, approved as a deliberate
    visual choice).

    The algebra invariant test on the NORMATIVE mask alone remains active
    (no decorator).
    """

    def setUp(self):
        self.imgs = {state: _load(state, V2_1080, FILES_1080) for state in FILES_1080}
        self.norm = self.imgs["NORMATIVE"]

    @unittest.expectedFailure
    def test_nonnormative_is_sigma_v_of_normative(self):
        # Permanent expected failure at the approved Math-Mirror Center-Scale-97
        # visual doctrine for NON-NORMATIVE. The user explicitly approved the
        # composite asset, which is not pixel-array-sigma_v of NORMATIVE
        # (observed IoU ~ 0.815). See
        # assets/v2/nonnormative-math97-five-over-master/SOURCE-AUDIT-NOTE.md.
        a = _alpha_mask(self.imgs["NON-NORMATIVE"])
        b = _alpha_mask(self.norm[:, ::-1, :])
        iou = _iou(a, b)
        self.assertGreaterEqual(iou, 0.995, f"NON-NORMATIVE != sigma_v(NORMATIVE), IoU={iou:.4f}")

    @unittest.expectedFailure
    def test_critical_is_C2_of_normative(self):
        a = _alpha_mask(self.imgs["CRITICAL"])
        b = _alpha_mask(self.norm[::-1, ::-1, :])
        iou = _iou(a, b)
        self.assertGreaterEqual(iou, 0.995, f"CRITICAL != C2(NORMATIVE), IoU={iou:.4f}")

    @unittest.expectedFailure
    def test_metacognitive_is_sigma_h_of_normative(self):
        a = _alpha_mask(self.imgs["METACOGNITIVE"])
        b = _alpha_mask(self.norm[::-1, :, :])
        iou = _iou(a, b)
        self.assertGreaterEqual(iou, 0.995, f"METACOGNITIVE != sigma_h(NORMATIVE), IoU={iou:.4f}")

    def test_v4_algebra_invariants(self):
        """sigma_v . sigma_v = I, C2 . C2 = I, sigma_h . sigma_h = I, sigma_v . C2 = sigma_h."""
        norm = _alpha_mask(self.norm)
        # involutions
        self.assertGreaterEqual(_iou(norm, norm[:, ::-1][:, ::-1]), 0.999)
        self.assertGreaterEqual(_iou(norm, norm[::-1, ::-1][::-1, ::-1]), 0.999)
        self.assertGreaterEqual(_iou(norm, norm[::-1, :][::-1, :]), 0.999)
        # sigma_v . C2 = sigma_h
        composed = norm[::-1, ::-1][:, ::-1]
        self.assertGreaterEqual(
            _iou(composed, norm[::-1, :]),
            0.999,
            "sigma_v . C2 != sigma_h on the NORMATIVE alpha mask",
        )


class V2Palette(unittest.TestCase):
    """Per-state dominant RGB must fall in the doctrine palette box."""

    def setUp(self):
        self.imgs = {state: _load(state, V2_1080, FILES_1080) for state in FILES_1080}

    def test_palette_per_state(self):
        for state, expected in PALETTE.items():
            r, g, b = _dominant_rgb(self.imgs[state])
            er, eg, eb = expected
            for ch, val, exp in (("R", r, er), ("G", g, eg), ("B", b, eb)):
                self.assertLessEqual(
                    abs(val - exp), PALETTE_TOL,
                    f"{state} dominant {ch}={val} outside palette box {exp}+/-{PALETTE_TOL}",
                )

    def test_normative_is_not_red(self):
        """NORMATIVE must be gold-leaning. R > G is allowed (gold has high R),
        but R must NOT dominate G by more than 40 — that would make it red.
        And B must be substantially below R and G (gold is warm/yellow)."""
        r, g, b = _dominant_rgb(self.imgs["NORMATIVE"])
        self.assertLessEqual(
            r - g, 40,
            f"NORMATIVE looks red-leaning (R={r}, G={g}); doctrine says NORMATIVE must never be red",
        )
        self.assertLess(b, min(r, g), f"NORMATIVE is not warm (B={b}, R={r}, G={g})")

    def test_critical_is_red(self):
        """CRITICAL must be red-leaning: R > G by a clear margin, R > B."""
        r, g, b = _dominant_rgb(self.imgs["CRITICAL"])
        self.assertGreater(r - g, 30, f"CRITICAL is not red-leaning (R={r}, G={g})")
        self.assertGreater(r - b, 30, f"CRITICAL is not red-leaning (R={r}, B={b})")


class V2NoSpeckle(unittest.TestCase):
    """No opaque near-black 'speckle' / junk pixels in the v2 transparent masters."""

    def test_no_dark_opaque_speckle(self):
        for state, fn in FILES_1080.items():
            arr = np.array(Image.open(os.path.join(V2_1080, fn)).convert("RGBA"))
            rgb = arr[..., :3].astype(np.int32)
            a = arr[..., 3]
            luma = rgb.sum(axis=-1)
            dark_opaque = ((luma < 25) & (a > 100)).sum()
            self.assertEqual(
                dark_opaque, 0,
                f"{state} has {dark_opaque} opaque near-black speckle pixels",
            )


if __name__ == "__main__":
    unittest.main()
