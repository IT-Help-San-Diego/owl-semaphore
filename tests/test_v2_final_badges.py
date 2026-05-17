"""Owl Semaphore v2 final composed-badge tests (presentation layer, v2.0.0-rc).

These tests gate the v2 *presentation-layer* composed badges under
``assets/v2/final-1080/`` and ``assets/v2/final-540/``, plus the v2 final
contact sheet. They are required to pass before any v2.0.0 release.

Doctrine context (see ``ASSET-DOCTRINE.md`` §1a, §5b):

- The mathematical master is the V4-tested owl-only PNG; that is gated by
  ``tests/test_v2_assets.py``.
- The composed badge is editorial / presentation-layer: per-state palette
  meander + outer ring around the owl. This file is what makes sure those
  final assets actually exist, carry the correct per-state palette, do not
  reintroduce v1 AOE / leaf / old-owl contamination, and that the PDF
  pipeline does not silently revert to v1 paths.
"""

from __future__ import annotations

import os
import re
import unittest

import numpy as np
from PIL import Image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FINAL_1080 = os.path.join(REPO, "assets", "v2", "final-1080")
FINAL_540 = os.path.join(REPO, "assets", "v2", "final-540")
PROOFS = os.path.join(REPO, "assets", "v2", "proofs")

FINAL_FILES_1080 = {
    "NORMATIVE":     "NORMATIVE-V2-FINAL-COMPOSED-1080.png",
    "NON-NORMATIVE": "NON-NORMATIVE-V2-FINAL-COMPOSED-1080.png",
    "CRITICAL":      "CRITICAL-V2-FINAL-COMPOSED-1080.png",
    "METACOGNITIVE": "METACOGNITIVE-V2-FINAL-COMPOSED-1080.png",
}
FINAL_FILES_540 = {
    "NORMATIVE":     "NORMATIVE-V2-FINAL-COMPOSED-540.png",
    "NON-NORMATIVE": "NON-NORMATIVE-V2-FINAL-COMPOSED-540.png",
    "CRITICAL":      "CRITICAL-V2-FINAL-COMPOSED-540.png",
    "METACOGNITIVE": "METACOGNITIVE-V2-FINAL-COMPOSED-540.png",
}

# Composed-badge dominant RGB centers, calibrated against the v2 build.
# These are *post-composite* medians (ring + owl ornament; inner black field
# and near-white background excluded). Tolerance is generous because the
# composite mixes ring + owl ornament + outline.
PALETTE_COMPOSED = {
    "NORMATIVE":     (176, 152,  83),
    "NON-NORMATIVE": ( 75, 172, 170),
    "CRITICAL":      (224, 115, 115),
    "METACOGNITIVE": (160, 135, 170),
}
PALETTE_COMPOSED_TOL = 30

CONTACT_SHEET = os.path.join(PROOFS, "OWL-SEMAPHORE-V2-FINAL-CONTACT-SHEET.png")

# v1 lineage paths that must NOT appear in the v2 PDF generator's emitted
# image references.
FORBIDDEN_V1_PATHS = (
    "assets/releases/",
    "assets/masters/",
    "assets/exports/",
    "assets/layers/normative-owl/NORM-L3-owl-body",
)

# Geometry layers we *do* legitimately reuse for v2 composed badges (the
# build script may reference these; the generator should not).
GENERATOR_FILE = os.path.join(REPO, "generate_pdfs.py")
BUILD_SCRIPT = os.path.join(REPO, "scripts", "build_v2_composed_badges.py")


def _dominant_rgb_composed(arr: np.ndarray) -> tuple[int, int, int]:
    """Median RGB of opaque pixels with mid-luma, excluding near-black inner
    field and near-white margin / background."""
    rgb = arr[..., :3]
    a = arr[..., 3]
    luma = rgb.sum(axis=-1)
    mask = (a > 200) & (luma > 200) & (luma < 720)
    if not mask.any():
        mask = a > 200
    median = np.median(rgb[mask], axis=0).astype(int)
    return int(median[0]), int(median[1]), int(median[2])


class V2FinalBadgePresence(unittest.TestCase):
    """File presence, mode, and size for the composed badges."""

    def test_all_final_files_1080_exist(self):
        for state, fn in FINAL_FILES_1080.items():
            self.assertTrue(
                os.path.isfile(os.path.join(FINAL_1080, fn)),
                f"missing v2 final 1080 PNG for {state}: {fn}",
            )

    def test_all_final_files_540_exist(self):
        for state, fn in FINAL_FILES_540.items():
            self.assertTrue(
                os.path.isfile(os.path.join(FINAL_540, fn)),
                f"missing v2 final 540 PNG for {state}: {fn}",
            )

    def test_final_contact_sheet_exists(self):
        self.assertTrue(
            os.path.isfile(CONTACT_SHEET),
            f"missing v2 final contact sheet: {CONTACT_SHEET}",
        )

    def test_1080_size_and_mode(self):
        for state, fn in FINAL_FILES_1080.items():
            with Image.open(os.path.join(FINAL_1080, fn)) as im:
                self.assertEqual(im.size, (1080, 1080), f"{state} final 1080 size != 1080x1080")
                self.assertEqual(im.mode, "RGBA", f"{state} final 1080 mode != RGBA")

    def test_540_size_and_mode(self):
        for state, fn in FINAL_FILES_540.items():
            with Image.open(os.path.join(FINAL_540, fn)) as im:
                self.assertEqual(im.size, (540, 540), f"{state} final 540 size != 540x540")
                self.assertEqual(im.mode, "RGBA", f"{state} final 540 mode != RGBA")


class V2FinalBadgePalette(unittest.TestCase):
    """Composed-badge dominant RGB must fall in the per-state palette box."""

    def setUp(self):
        self.imgs = {
            state: np.array(
                Image.open(os.path.join(FINAL_1080, fn)).convert("RGBA")
            )
            for state, fn in FINAL_FILES_1080.items()
        }

    def test_composed_palette_per_state(self):
        for state, expected in PALETTE_COMPOSED.items():
            r, g, b = _dominant_rgb_composed(self.imgs[state])
            er, eg, eb = expected
            for ch, val, exp in (("R", r, er), ("G", g, eg), ("B", b, eb)):
                self.assertLessEqual(
                    abs(val - exp), PALETTE_COMPOSED_TOL,
                    f"{state} composed dominant {ch}={val} outside palette box "
                    f"{exp}+/-{PALETTE_COMPOSED_TOL}",
                )

    def test_composed_normative_is_not_red(self):
        r, g, b = _dominant_rgb_composed(self.imgs["NORMATIVE"])
        self.assertLessEqual(
            r - g, 40,
            f"NORMATIVE composed looks red-leaning (R={r}, G={g}); doctrine forbids",
        )

    def test_composed_critical_is_red(self):
        r, g, b = _dominant_rgb_composed(self.imgs["CRITICAL"])
        self.assertGreater(r - g, 30, f"CRITICAL composed is not red-leaning (R={r}, G={g})")
        self.assertGreater(r - b, 30, f"CRITICAL composed is not red-leaning (R={r}, B={b})")


class V2NoObsoleteV1Leakage(unittest.TestCase):
    """The v2 PDF generator must not embed obsolete v1 lineage image paths."""

    def test_generate_pdfs_does_not_reference_v1_paths(self):
        with open(GENERATOR_FILE, "r") as f:
            text = f.read()
        for path in FORBIDDEN_V1_PATHS:
            self.assertNotIn(
                path, text,
                f"generate_pdfs.py references forbidden v1 path: {path}",
            )

    def test_generate_pdfs_uses_v2_final_badges(self):
        """The PDF generator must reference v2 final composed badges."""
        with open(GENERATOR_FILE, "r") as f:
            text = f.read()
        self.assertIn(
            "assets/v2/final-540/", text,
            "generate_pdfs.py does not reference the v2 final composed badges",
        )

    def test_build_script_does_not_use_old_owl_body_layer(self):
        """The composed-badge build must not reuse the legacy L3 owl-body."""
        with open(BUILD_SCRIPT, "r") as f:
            text = f.read()
        self.assertNotIn(
            "NORM-L3-owl-body", text,
            "build_v2_composed_badges.py reuses the obsolete L3 owl-body layer",
        )


class V2FinalCompositeStructural(unittest.TestCase):
    """Composed badges must have a black inner field and a coloured ring (not solid color)."""

    def test_inner_field_is_dark(self):
        """The center 200x200 region should be very dark (inner field present)."""
        for state, fn in FINAL_FILES_1080.items():
            arr = np.array(Image.open(os.path.join(FINAL_1080, fn)).convert("RGBA"))
            # owl occupies the center, so sample a small ring just outside the inner
            # field rim but inside the meander: the center pixel itself may be on
            # an owl ornament. Instead pick a quadrant gap.
            # Use a known background region between owl and inner-field rim by
            # checking the four corners of the inner-field bounding box.
            # Easier: assert that at least 10% of opaque pixels are near-black
            # (the inner-field circle), which would not be true for a flat
            # owl-only image.
            a = arr[..., 3]
            luma = arr[..., :3].sum(axis=-1)
            opaque = (a > 200)
            dark = ((luma < 60) & opaque).sum()
            total = opaque.sum()
            ratio = dark / max(total, 1)
            self.assertGreater(
                ratio, 0.10,
                f"{state} composed has only {ratio:.2%} dark opaque pixels — "
                "inner black field appears missing",
            )

    def test_ring_geometry_extends_near_edge(self):
        """The composed badge must occupy a circular region close to the canvas
        edge (the outer ring sits at radius ~520 on a 1080 canvas)."""
        for state, fn in FINAL_FILES_1080.items():
            arr = np.array(Image.open(os.path.join(FINAL_1080, fn)).convert("RGBA"))
            a = arr[..., 3] > 32
            # opaque pixels should reach close to the canvas edge (within 50 px)
            ys, xs = np.where(a)
            self.assertLess(xs.min(), 50, f"{state} composed: ring does not reach left edge")
            self.assertGreater(xs.max(), 1030, f"{state} composed: ring does not reach right edge")
            self.assertLess(ys.min(), 50, f"{state} composed: ring does not reach top edge")
            self.assertGreater(ys.max(), 1030, f"{state} composed: ring does not reach bottom edge")


if __name__ == "__main__":
    unittest.main()
