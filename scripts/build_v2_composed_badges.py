#!/usr/bin/env python3
"""Build Owl Semaphore v2 final composed badge assets (presentation layer).

These composites are the *published visible badge*: a per-state palette ring +
meander surrounding the v2 owl-only authoritative master. They are explicitly
NOT mathematical masters — the owl-only transparent PNGs under
``assets/v2/transparent-{1080,540}/`` remain the V4-tested masters
(see ``ASSET-DOCTRINE.md`` §1 and §7).

Inputs
------
- ``assets/v2/transparent-1080/<STATE>-human-gold-branch-transparent-1080.png``
  the V4-tested owl-only master (owl + human-selected gold branch only).
- ``assets/layers/normative-owl/NORM-L1-inner-field-1080.png``
  the black inner field (reused legacy layer, geometry only).
- ``assets/layers/normative-owl/NORM-L2-meander-ring-1080.png``
  the gold meander/Greek-key ring (reused legacy layer, geometry only).
- ``assets/layers/normative-owl/NORM-L4-outer-ring-1080.png``
  the thin gold outer ring (reused legacy layer, geometry only).

The reused layers contribute *geometry and pattern* only. Their color is
recolored per state to the v2 palette doctrine (NORMATIVE #D8B760,
NON-NORMATIVE #2F8C8C, CRITICAL #C85B5B, METACOGNITIVE #8F75BF). The legacy
AOE letters, leaf overlay, and old owl body (L3) are NOT reused.

Outputs
-------
- ``assets/v2/final-1080/<STATE>-V2-FINAL-COMPOSED-1080.png``
- ``assets/v2/final-540/<STATE>-V2-FINAL-COMPOSED-540.png``
- ``assets/v2/proofs/OWL-SEMAPHORE-V2-FINAL-CONTACT-SHEET.png``

Usage
-----
    python3 scripts/build_v2_composed_badges.py
"""
from __future__ import annotations

import os
import sys
from typing import Optional

import numpy as np
from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V2_SRC = os.path.join(REPO, "assets", "v2", "transparent-1080")
LAYER_DIR = os.path.join(REPO, "assets", "layers", "normative-owl")
OUT_1080 = os.path.join(REPO, "assets", "v2", "final-1080")
OUT_540 = os.path.join(REPO, "assets", "v2", "final-540")
PROOF_DIR = os.path.join(REPO, "assets", "v2", "proofs")

# Per-state palette used to recolor the legacy meander/outer-ring geometry.
#
# NORMATIVE was updated on 2026-05-17 to reflect the human-approved OWL-1
# NORMATIVE D-geometry + B parchment-gold master. The prior #D8B760 is
# retained as a comment for provenance. The new hex below approximates the
# B parchment-gold tone observed in the approved composite, but the active
# NORMATIVE composite is sourced byte-exact from
# assets/v2/normative-D-B-gold-master/NORMATIVE-V2-D-B-GOLD-MASTER-COMPOSITE-*.png
# (see PINNED_NORMATIVE_COMPOSITE_* below). NON-NORMATIVE / CRITICAL /
# METACOGNITIVE are unchanged pending the next per-state review.
PALETTE = {
    "NORMATIVE":     (0xCB, 0xB1, 0x78),  # B parchment-gold (prior: 0xD8 0xB7 0x60)
    "NON-NORMATIVE": (0x2F, 0x8C, 0x8C),
    "CRITICAL":      (0xDA, 0x37, 0x41),  # B alert red balanced (218,55,65) - prior: 0xC8 0x5B 0x5B
    "METACOGNITIVE": (0x8F, 0x75, 0xBF),
}

# Approved D+B parchment-gold master overrides for NORMATIVE. The approval was
# byte-exact on the composites; we copy them in directly instead of relying on
# the generic recolor pipeline so the published NORMATIVE badge is identical
# to the asset reviewed and approved by the human author.
PINNED_NORMATIVE_COMPOSITE_1080 = os.path.join(
    REPO, "assets", "v2", "normative-D-B-gold-master",
    "NORMATIVE-V2-D-B-GOLD-MASTER-COMPOSITE-1080.png",
)
PINNED_NORMATIVE_COMPOSITE_540 = os.path.join(
    REPO, "assets", "v2", "normative-D-B-gold-master",
    "NORMATIVE-V2-D-B-GOLD-MASTER-COMPOSITE-540.png",
)

# Approved Math-Mirror Center-Scale-97 + Seam-17 + Five-Over master overrides
# for NON-NORMATIVE. Same byte-exact-pin rationale as NORMATIVE: the user
# visually approved the COMPOSITE-1080.png and COMPOSITE-540.png as the
# published presentation-layer badge for OWL-2; we copy them in directly
# instead of relying on the generic recolor pipeline.
PINNED_NONNORMATIVE_COMPOSITE_1080 = os.path.join(
    REPO, "assets", "v2", "nonnormative-math97-five-over-master",
    "OWL-2-NON-NORMATIVE-MATH97-FIVE-OVER-COMPOSITE-1080.png",
)
PINNED_NONNORMATIVE_COMPOSITE_540 = os.path.join(
    REPO, "assets", "v2", "nonnormative-math97-five-over-master",
    "OWL-2-NON-NORMATIVE-MATH97-FIVE-OVER-COMPOSITE-540.png",
)

# Approved B-geometry + B alert red balanced master overrides for CRITICAL.
# Same byte-exact-pin rationale as NORMATIVE / NON-NORMATIVE: the user
# (Carey James Balboa) approved the COMPOSITE-1080.png and COMPOSITE-540.png
# as the published OWL-3 CRITICAL badge after a controlled six-candidate red
# perception study. The composite is body + rings recolored to RGB(218,55,65),
# preserving the gold branch / leaves / olive and dark/black linework
# exactly. See assets/v2/critical-b-geometry-e-ring-b-balanced-master/
# SOURCE-README.md for the provenance package. The prior salmon-rings-only
# kit is preserved under -superseded for provenance.
PINNED_CRITICAL_COMPOSITE_1080 = os.path.join(
    REPO, "assets", "v2", "critical-b-geometry-e-ring-b-balanced-master",
    "OWL-3-CRITICAL-B-GEOMETRY-B-BALANCED-COMPOSITE-1080.png",
)
PINNED_CRITICAL_COMPOSITE_540 = os.path.join(
    REPO, "assets", "v2", "critical-b-geometry-e-ring-b-balanced-master",
    "OWL-3-CRITICAL-B-GEOMETRY-B-BALANCED-COMPOSITE-540.png",
)

OWL_FILES = {
    "NORMATIVE":     "NORMATIVE-human-gold-branch-transparent-1080.png",
    "NON-NORMATIVE": "NON-NORMATIVE-human-gold-branch-transparent-1080.png",
    "CRITICAL":      "CRITICAL-human-gold-branch-transparent-1080.png",
    "METACOGNITIVE": "METACOGNITIVE-human-gold-branch-transparent-1080.png",
}

INNER_FIELD = os.path.join(LAYER_DIR, "NORM-L1-inner-field-1080.png")
MEANDER_RING = os.path.join(LAYER_DIR, "NORM-L2-meander-ring-1080.png")
OUTER_RING = os.path.join(LAYER_DIR, "NORM-L4-outer-ring-1080.png")

OWL_TARGET_DIAMETER = 700  # owl bbox target inside the 800-px inner field
CANVAS = 1080


def _recolor_to_palette(layer_rgba: np.ndarray, target_rgb: tuple[int, int, int]) -> np.ndarray:
    """Recolor a legacy gold layer to ``target_rgb`` while preserving luma and alpha.

    The legacy meander/outer ring is rendered in gold over a near-black outline.
    We map opaque pixels to ``target_rgb`` weighted by their per-pixel luma
    (preserving the gold-on-black ornament pattern), and pass alpha through.
    """
    rgba = layer_rgba.astype(np.float32)
    rgb = rgba[..., :3]
    a = rgba[..., 3:4]
    luma = rgb.mean(axis=-1, keepdims=True) / 255.0  # 0..1
    target = np.array(target_rgb, dtype=np.float32).reshape(1, 1, 3)
    out_rgb = luma * target  # bright gold becomes bright palette; near-black stays near-black
    out = np.concatenate([np.clip(out_rgb, 0, 255), a], axis=-1)
    return out.astype(np.uint8)


def _alpha_composite(base: np.ndarray, overlay: np.ndarray) -> np.ndarray:
    """Standard 'over' alpha composite of two HxWx4 uint8 arrays."""
    b = base.astype(np.float32) / 255.0
    o = overlay.astype(np.float32) / 255.0
    ba = b[..., 3:4]
    oa = o[..., 3:4]
    out_a = oa + ba * (1 - oa)
    safe = np.where(out_a > 1e-6, out_a, 1.0)
    out_rgb = (o[..., :3] * oa + b[..., :3] * ba * (1 - oa)) / safe
    out = np.concatenate([out_rgb, out_a], axis=-1)
    return (out * 255).clip(0, 255).astype(np.uint8)


def _scale_owl_centered(owl: Image.Image, target_diameter: int) -> Image.Image:
    """Resize the v2 owl so its bounding box fits ``target_diameter``, centered on CANVAS."""
    arr = np.array(owl)
    a = arr[..., 3] > 32
    ys, xs = np.where(a)
    if not len(xs):
        return owl
    bb_w = xs.max() - xs.min()
    bb_h = ys.max() - ys.min()
    longest = max(bb_w, bb_h)
    scale = target_diameter / longest
    new_size = (int(round(owl.size[0] * scale)), int(round(owl.size[1] * scale)))
    resized = owl.resize(new_size, Image.LANCZOS)
    canvas = Image.new("RGBA", (CANVAS, CANVAS), (0, 0, 0, 0))
    # compute paste offset so the *bbox* (not the full image) is centered on CANVAS/2
    rarr = np.array(resized)
    ra = rarr[..., 3] > 32
    rys, rxs = np.where(ra)
    cx, cy = (rxs.min() + rxs.max()) // 2, (rys.min() + rys.max()) // 2
    paste_x = CANVAS // 2 - cx
    paste_y = CANVAS // 2 - cy
    canvas.paste(resized, (paste_x, paste_y), resized)
    return canvas


def build_state_badge(state: str) -> Image.Image:
    target = PALETTE[state]

    inner = np.array(Image.open(INNER_FIELD).convert("RGBA"))
    meander = np.array(Image.open(MEANDER_RING).convert("RGBA"))
    outer = np.array(Image.open(OUTER_RING).convert("RGBA"))

    meander_tinted = _recolor_to_palette(meander, target)
    outer_tinted = _recolor_to_palette(outer, target)

    owl = Image.open(os.path.join(V2_SRC, OWL_FILES[state])).convert("RGBA")
    owl_scaled = np.array(_scale_owl_centered(owl, OWL_TARGET_DIAMETER))

    # composite: outer ring -> meander -> inner field -> owl
    base = np.zeros((CANVAS, CANVAS, 4), dtype=np.uint8)
    base = _alpha_composite(base, outer_tinted)
    base = _alpha_composite(base, meander_tinted)
    base = _alpha_composite(base, inner)
    base = _alpha_composite(base, owl_scaled)
    return Image.fromarray(base, mode="RGBA")


def _draw_label(canvas: Image.Image, text: str, anchor_xy: tuple[int, int]) -> None:
    draw = ImageDraw.Draw(canvas)
    font: Optional[ImageFont.ImageFont]
    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22
        )
    except Exception:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x = anchor_xy[0] - w // 2
    y = anchor_xy[1] - h // 2
    draw.text((x, y), text, fill=(40, 40, 40, 255), font=font)


def build_contact_sheet(badges_540: dict[str, Image.Image]) -> Image.Image:
    states = ["NORMATIVE", "NON-NORMATIVE", "CRITICAL", "METACOGNITIVE"]
    cell = 540
    label_h = 60
    margin = 24
    title_h = 90
    width = margin * 2 + cell * 4 + margin * 3
    height = title_h + cell + label_h + margin * 2
    sheet = Image.new("RGBA", (width, height), (255, 255, 255, 255))
    draw = ImageDraw.Draw(sheet)

    try:
        title_font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28
        )
        sub_font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16
        )
    except Exception:
        title_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()

    title = "Owl Semaphore v2.0.0-rc — Final Composed Badges (Presentation Layer)"
    sub = ("Owl-only V4-tested master + per-state palette meander/ring. "
           "Mathematical master remains the transparent owl-only PNG.")
    tw = draw.textbbox((0, 0), title, font=title_font)[2]
    sw = draw.textbbox((0, 0), sub, font=sub_font)[2]
    draw.text(((width - tw) // 2, 16), title, fill=(20, 20, 20, 255), font=title_font)
    draw.text(((width - sw) // 2, 54), sub, fill=(90, 90, 90, 255), font=sub_font)

    for i, state in enumerate(states):
        x = margin + i * (cell + margin)
        y = title_h
        sheet.alpha_composite(badges_540[state], (x, y))
        _draw_label(sheet, state, (x + cell // 2, y + cell + label_h // 2))

    return sheet


def main() -> int:
    os.makedirs(OUT_1080, exist_ok=True)
    os.makedirs(OUT_540, exist_ok=True)
    os.makedirs(PROOF_DIR, exist_ok=True)

    print("Owl Semaphore v2 — build_v2_composed_badges.py")
    badges_1080: dict[str, Image.Image] = {}
    badges_540: dict[str, Image.Image] = {}

    for state in ["NORMATIVE", "NON-NORMATIVE", "CRITICAL", "METACOGNITIVE"]:
        out1080 = os.path.join(OUT_1080, f"{state}-V2-FINAL-COMPOSED-1080.png")
        out540 = os.path.join(OUT_540, f"{state}-V2-FINAL-COMPOSED-540.png")

        pinned_1080: Optional[str] = None
        pinned_540: Optional[str] = None
        pin_label = ""
        if state == "NORMATIVE" and os.path.isfile(PINNED_NORMATIVE_COMPOSITE_1080):
            pinned_1080 = PINNED_NORMATIVE_COMPOSITE_1080
            pinned_540  = PINNED_NORMATIVE_COMPOSITE_540
            pin_label   = "approved D+B gold master"
        elif state == "NON-NORMATIVE" and os.path.isfile(PINNED_NONNORMATIVE_COMPOSITE_1080):
            pinned_1080 = PINNED_NONNORMATIVE_COMPOSITE_1080
            pinned_540  = PINNED_NONNORMATIVE_COMPOSITE_540
            pin_label   = "approved Math97 Five-Over master"
        elif state == "CRITICAL" and os.path.isfile(PINNED_CRITICAL_COMPOSITE_1080):
            pinned_1080 = PINNED_CRITICAL_COMPOSITE_1080
            pinned_540  = PINNED_CRITICAL_COMPOSITE_540
            pin_label   = "approved B-geometry + B alert red balanced master"

        if pinned_1080:
            # Use the human-approved composite byte-exact, bypassing the generic
            # recolor pipeline so the published badge is identical to the
            # reviewed master.
            badge = Image.open(pinned_1080).convert("RGBA")
            badges_1080[state] = badge
            badge.save(out1080, format="PNG")
            print(f"  OK  {out1080} (pinned to {pin_label}, "
                  f"{os.path.getsize(out1080) / 1024:.0f} KB)")

            if pinned_540 and os.path.isfile(pinned_540):
                badge_540 = Image.open(pinned_540).convert("RGBA")
            else:
                badge_540 = badge.resize((540, 540), Image.LANCZOS)
            badges_540[state] = badge_540
            badge_540.save(out540, format="PNG")
            print(f"  OK  {out540} (pinned to {pin_label}, "
                  f"{os.path.getsize(out540) / 1024:.0f} KB)")
            continue

        badge = build_state_badge(state)
        badges_1080[state] = badge

        badge.save(out1080, format="PNG")
        size_kb = os.path.getsize(out1080) / 1024
        print(f"  OK  {out1080} ({size_kb:.0f} KB)")

        badge_540 = badge.resize((540, 540), Image.LANCZOS)
        badges_540[state] = badge_540
        badge_540.save(out540, format="PNG")
        size_kb = os.path.getsize(out540) / 1024
        print(f"  OK  {out540} ({size_kb:.0f} KB)")

    sheet = build_contact_sheet(badges_540)
    sheet_path = os.path.join(PROOF_DIR, "OWL-SEMAPHORE-V2-FINAL-CONTACT-SHEET.png")
    sheet.convert("RGB").save(sheet_path, format="PNG")
    size_kb = os.path.getsize(sheet_path) / 1024
    print(f"  OK  {sheet_path} ({size_kb:.0f} KB)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
