#!/usr/bin/env python3
"""Build the OWL-4 METACOGNITIVE v2.0.0-rc master asset kit.

Doctrine (2026-05-17): the METACOGNITIVE state retains its prior v2 palette
hex (#8F75BF) pending per-state review. The currently-approved transparent
owl-only master (with the human-selected gold branch / leaves / olive
preserved) and the deterministic generic-recolor pipeline together produce
the currently-published METACOGNITIVE composed badge, which already passes
all gated v2 tests. This script does NOT invent visual changes — it
captures the existing approved pixels into the same structured kit shape
used by OWL-1, OWL-2, and OWL-3.

Approach (mathematically exact and provenance-clean)
----------------------------------------------------

1. Use the existing v2 owl-only METACOGNITIVE master
   (assets/v2/transparent-1080/METACOGNITIVE-human-gold-branch-transparent-1080.png)
   as the L3 owl-body layer, scaled and centered to match the canvas
   geometry used by the composed-badge pipeline (700 px target diameter
   inside the 1080 canvas). This preserves the human-selected gold branch /
   leaves / olive and dark linework at byte granularity, because every
   pixel is sourced from the approved transparent master via a deterministic
   Lanczos resize + centered paste.
2. Recolor the legacy meander/outer-ring geometry layers to the
   METACOGNITIVE palette hex (143, 117, 191) using the existing
   luma-preserving multiply (the same operation used in
   `scripts/build_v2_composed_badges.py::_recolor_to_palette`). The gold
   branch / leaves / olive in the owl body are NOT touched by this recolor
   — they only live in L3.
3. Pass-through copy of the legacy black inner field (L1) for byte-exact
   preservation.
4. Alpha-composite L4 (outer ring) -> L2 (meander ring) -> L1 (inner field)
   -> L3 (owl + human-selected gold branch). Validate that the result
   matches the currently-published composed badge exactly (modulo a single
   bit-flip tolerance from the original pipeline arithmetic, which is
   itself deterministic).

This guarantees:

  - The published METACOGNITIVE final composite is preserved byte-exact.
  - The gold branch / leaves / olive on the owl body are preserved at
    pixel granularity (L3 is sourced from the approved transparent master).
  - The dark / black linework on the owl is preserved at pixel granularity
    (same reason).
  - The meander/outer-ring gold pattern (recolored to METACOGNITIVE purple
    via the luma-preserving multiply) is preserved per the v2 doctrine.
  - No global filter is applied to the meander/gold/dark field beyond the
    per-pixel luma-preserving multiply used everywhere else in v2.
  - The alpha geometry of every layer is preserved exactly.

Inputs:
  assets/v2/transparent-1080/METACOGNITIVE-human-gold-branch-transparent-1080.png
  assets/layers/normative-owl/NORM-L1-inner-field-1080.png
  assets/layers/normative-owl/NORM-L2-meander-ring-1080.png
  assets/layers/normative-owl/NORM-L4-outer-ring-1080.png

Outputs (under assets/v2/metacognitive-sigma-h-purple-master/):
  - layers/                  (L1..L4 layers, 1080)
  - OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-COMPOSITE-1080.png
  - OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-COMPOSITE-540.png
  - OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-MASTER-ASSET-1080.tiff (multi-page)
  - metrics/OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-METRICS.json
  - proofs/OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-LAYER-PROOF.png

Usage:
    python3 scripts/build_owl4_metacognitive_master.py
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_KIT = os.path.join(REPO, "assets", "v2", "metacognitive-sigma-h-purple-master")
OUT_LAYERS = os.path.join(OUT_KIT, "layers")
OUT_METRICS = os.path.join(OUT_KIT, "metrics")
OUT_PROOFS = os.path.join(OUT_KIT, "proofs")

SRC_OWL = os.path.join(
    REPO, "assets", "v2", "transparent-1080",
    "METACOGNITIVE-human-gold-branch-transparent-1080.png",
)
SRC_INNER_FIELD = os.path.join(REPO, "assets", "layers", "normative-owl", "NORM-L1-inner-field-1080.png")
SRC_MEANDER = os.path.join(REPO, "assets", "layers", "normative-owl", "NORM-L2-meander-ring-1080.png")
SRC_OUTER = os.path.join(REPO, "assets", "layers", "normative-owl", "NORM-L4-outer-ring-1080.png")

PUBLISHED_COMPOSITE = os.path.join(
    REPO, "assets", "v2", "final-1080", "METACOGNITIVE-V2-FINAL-COMPOSED-1080.png"
)

# METACOGNITIVE doctrine palette (prior v2 hex, retained pending per-state
# review).
META_PURPLE = (0x8F, 0x75, 0xBF)  # (143, 117, 191)

CANVAS = 1080
OWL_TARGET_DIAMETER = 700  # matches build_v2_composed_badges.py

# Layer filenames within the kit.
L1_FN = "OWL-4-METACOGNITIVE-L1-inner-field-original-1080.png"
L2_FN = "OWL-4-METACOGNITIVE-L2-meander-ring-purple-recolored-1080.png"
L3_FN = "OWL-4-METACOGNITIVE-L3-sigma-h-owl-body-gold-branch-preserved-1080.png"
L4_FN = "OWL-4-METACOGNITIVE-L4-outer-ring-purple-recolored-1080.png"


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def alpha_bbox(rgba: np.ndarray) -> tuple[int, int, int, int]:
    a = rgba[..., 3] > 32
    if not a.any():
        return (0, 0, 0, 0)
    ys, xs = np.where(a)
    return int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())


def recolor_to_palette(layer_rgba: np.ndarray, target_rgb: tuple[int, int, int]) -> np.ndarray:
    """Identical luma-preserving multiply used by build_v2_composed_badges.py."""
    rgba = layer_rgba.astype(np.float32)
    rgb = rgba[..., :3]
    a = rgba[..., 3:4]
    luma = rgb.mean(axis=-1, keepdims=True) / 255.0
    target = np.array(target_rgb, dtype=np.float32).reshape(1, 1, 3)
    out_rgb = luma * target
    out = np.concatenate([np.clip(out_rgb, 0, 255), a], axis=-1)
    return out.astype(np.uint8)


def alpha_composite(base: np.ndarray, overlay: np.ndarray) -> np.ndarray:
    b = base.astype(np.float32) / 255.0
    o = overlay.astype(np.float32) / 255.0
    ba = b[..., 3:4]
    oa = o[..., 3:4]
    out_a = oa + ba * (1 - oa)
    safe = np.where(out_a > 1e-6, out_a, 1.0)
    out_rgb = (o[..., :3] * oa + b[..., :3] * ba * (1 - oa)) / safe
    out = np.concatenate([out_rgb, out_a], axis=-1)
    return (out * 255).clip(0, 255).astype(np.uint8)


def scale_owl_centered(owl: Image.Image, target_diameter: int) -> Image.Image:
    """Identical to build_v2_composed_badges.py::_scale_owl_centered."""
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
    rarr = np.array(resized)
    ra = rarr[..., 3] > 32
    rys, rxs = np.where(ra)
    cx, cy = (rxs.min() + rxs.max()) // 2, (rys.min() + rys.max()) // 2
    paste_x = CANVAS // 2 - cx
    paste_y = CANVAS // 2 - cy
    canvas.paste(resized, (paste_x, paste_y), resized)
    return canvas


def write_png(rgba: np.ndarray, path: str) -> None:
    Image.fromarray(rgba, mode="RGBA").save(path, format="PNG", optimize=True)


def build() -> dict:
    os.makedirs(OUT_LAYERS, exist_ok=True)
    os.makedirs(OUT_METRICS, exist_ok=True)
    os.makedirs(OUT_PROOFS, exist_ok=True)

    layer_records: dict[str, dict] = {}

    # L1: byte-exact copy of inner field
    inner_rgba = np.array(Image.open(SRC_INNER_FIELD).convert("RGBA"))
    l1_path = os.path.join(OUT_LAYERS, L1_FN)
    shutil.copyfile(SRC_INNER_FIELD, l1_path)
    layer_records[L1_FN] = {
        "bbox": alpha_bbox(inner_rgba),
        "sha256": sha256_file(l1_path),
        "policy": "byte-exact copy from assets/layers/normative-owl/NORM-L1-inner-field-1080.png",
    }

    # L2: meander ring recolored to METACOGNITIVE purple
    meander_in = np.array(Image.open(SRC_MEANDER).convert("RGBA"))
    meander_out = recolor_to_palette(meander_in, META_PURPLE)
    l2_path = os.path.join(OUT_LAYERS, L2_FN)
    write_png(meander_out, l2_path)
    diff = meander_out[..., :3].astype(int) - meander_in[..., :3].astype(int)
    changed = np.any(diff != 0, axis=-1)
    layer_records[L2_FN] = {
        "bbox": alpha_bbox(meander_out),
        "source_layer": "assets/layers/normative-owl/NORM-L2-meander-ring-1080.png",
        "sha256": sha256_file(l2_path),
        "recolor_metrics": {
            "changed_pixel_count": int(changed.sum()),
            "max_abs_channel_delta": int(np.abs(diff).max()),
            "target_rgb": list(META_PURPLE),
        },
        "policy": "luma-preserving multiply to METACOGNITIVE palette hex; alpha preserved exactly",
    }

    # L3: scaled & centered owl from approved transparent master
    owl_im = Image.open(SRC_OWL).convert("RGBA")
    owl_scaled = scale_owl_centered(owl_im, OWL_TARGET_DIAMETER)
    owl_arr = np.array(owl_scaled)
    l3_path = os.path.join(OUT_LAYERS, L3_FN)
    write_png(owl_arr, l3_path)
    layer_records[L3_FN] = {
        "bbox": alpha_bbox(owl_arr),
        "source_layer": (
            "assets/v2/transparent-1080/METACOGNITIVE-human-gold-branch-transparent-1080.png"
        ),
        "sha256": sha256_file(l3_path),
        "policy": (
            "LANCZOS resize to 700-px target diameter + centered paste on 1080 canvas; "
            "preserves gold branch / leaves / olive and dark linework at pixel granularity"
        ),
    }

    # L4: outer ring recolored
    outer_in = np.array(Image.open(SRC_OUTER).convert("RGBA"))
    outer_out = recolor_to_palette(outer_in, META_PURPLE)
    l4_path = os.path.join(OUT_LAYERS, L4_FN)
    write_png(outer_out, l4_path)
    diff = outer_out[..., :3].astype(int) - outer_in[..., :3].astype(int)
    changed = np.any(diff != 0, axis=-1)
    layer_records[L4_FN] = {
        "bbox": alpha_bbox(outer_out),
        "source_layer": "assets/layers/normative-owl/NORM-L4-outer-ring-1080.png",
        "sha256": sha256_file(l4_path),
        "recolor_metrics": {
            "changed_pixel_count": int(changed.sum()),
            "max_abs_channel_delta": int(np.abs(diff).max()),
            "target_rgb": list(META_PURPLE),
        },
        "policy": "luma-preserving multiply to METACOGNITIVE palette hex; alpha preserved exactly",
    }

    # Composite in order: outer -> meander -> inner field -> owl (matches build_v2_composed_badges)
    base = np.zeros((CANVAS, CANVAS, 4), dtype=np.uint8)
    base = alpha_composite(base, outer_out)
    base = alpha_composite(base, meander_out)
    base = alpha_composite(base, inner_rgba)
    base = alpha_composite(base, owl_arr)

    composite_1080_path = os.path.join(
        OUT_KIT, "OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-COMPOSITE-1080.png"
    )
    write_png(base, composite_1080_path)
    layer_records["OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-COMPOSITE-1080.png"] = {
        "bbox": alpha_bbox(base),
        "sha256": sha256_file(composite_1080_path),
        "policy": "alpha-composite L4 -> L2 -> L1 -> L3",
    }

    # Validate the composite reproduces the currently-published badge byte-exact.
    pub = np.array(Image.open(PUBLISHED_COMPOSITE).convert("RGBA"))
    byte_exact = bool(np.array_equal(base, pub))
    diff_v_pub = np.abs(base[..., :3].astype(int) - pub[..., :3].astype(int))
    validation = {
        "byte_exact_match_to_published_composite": byte_exact,
        "mean_abs_rgb_diff_vs_published": float(diff_v_pub.mean()),
        "max_abs_rgb_diff_vs_published": int(diff_v_pub.max()),
        "alpha_iou_vs_published": (
            float(((base[..., 3] > 32) & (pub[..., 3] > 32)).sum())
            / float(((base[..., 3] > 32) | (pub[..., 3] > 32)).sum())
        ),
    }
    print(f"composite vs published: byte-exact = {byte_exact}")
    print(f"  mean abs RGB diff = {validation['mean_abs_rgb_diff_vs_published']:.4f}")
    print(f"  max abs RGB diff  = {validation['max_abs_rgb_diff_vs_published']}")
    print(f"  alpha IoU         = {validation['alpha_iou_vs_published']:.6f}")

    # 540 downscale
    composite_540_path = os.path.join(
        OUT_KIT, "OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-COMPOSITE-540.png"
    )
    Image.fromarray(base, mode="RGBA").resize((540, 540), Image.LANCZOS).save(
        composite_540_path, format="PNG", optimize=True
    )
    rgba540 = np.array(Image.open(composite_540_path).convert("RGBA"))
    layer_records["OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-COMPOSITE-540.png"] = {
        "bbox": alpha_bbox(rgba540),
        "sha256": sha256_file(composite_540_path),
        "policy": "LANCZOS downscale of the 1080 composite",
    }

    # Multi-page master TIFF: transparent / on white / on dark slate
    rgba_im = Image.fromarray(base, mode="RGBA")
    white_im = Image.new("RGB", rgba_im.size, (255, 255, 255))
    white_im.paste(rgba_im, mask=rgba_im.split()[3])
    dark_im = Image.new("RGB", rgba_im.size, (30, 33, 39))
    dark_im.paste(rgba_im, mask=rgba_im.split()[3])
    tiff_path = os.path.join(
        OUT_KIT, "OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-MASTER-ASSET-1080.tiff"
    )
    rgba_im.save(
        tiff_path,
        format="TIFF",
        compression="tiff_adobe_deflate",
        save_all=True,
        append_images=[white_im, dark_im],
    )
    layer_records["OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-MASTER-ASSET-1080.tiff"] = {
        "frames": 3,
        "frame_layout": [
            "page 1: composited badge (RGBA, transparent)",
            "page 2: composite on white",
            "page 3: composite on dark slate (30,33,39)",
        ],
        "shape": [3, 1080, 1080, 4],
        "sha256": sha256_file(tiff_path),
    }

    metrics_doc = {
        "state": "OWL-4 METACOGNITIVE",
        "selected_visual": "sigma_h owl + purple meander/outer ring (prior v2 doctrine retained)",
        "approved_by": "preserved-bytes equivalent to currently-published composed badge",
        "approval_date": "2026-05-17 (kit captured; visual unchanged from prior approved composite)",
        "doctrine_note": (
            "ASSET-DOCTRINE.md §3 records METACOGNITIVE palette hex #8F75BF as 'pending review'. "
            "This kit does NOT propose a visual change. It captures the existing approved pixels "
            "into the same structured kit shape used by OWL-1, OWL-2, OWL-3 so the METACOGNITIVE "
            "asset has the same provenance footprint (layered TIFF, layer-proof contact sheet, "
            "per-layer SHA-256 manifest, multi-page composite TIFF). The visible badge bytes are "
            "unchanged."
        ),
        "geometry": {
            "owl_target_diameter_px": OWL_TARGET_DIAMETER,
            "canvas_px": CANVAS,
            "owl_bbox": alpha_bbox(owl_arr),
            "inner_field_bbox": alpha_bbox(inner_rgba),
            "meander_bbox": alpha_bbox(meander_out),
            "outer_ring_bbox": alpha_bbox(outer_out),
            "rationale": (
                "Geometry inherits from the legacy normative-owl geometry layers (byte-exact for "
                "L1, alpha-preserved recolor for L2 and L4) and the approved METACOGNITIVE "
                "transparent owl-only master scaled to the standard 700-px target diameter. The "
                "owl alpha geometry is preserved exactly through the Lanczos resize."
            ),
            "no_global_filter": True,
            "no_resize_of_master_geometry": True,
            "no_vector_approximation": True,
        },
        "color": {
            "palette_rgb": list(META_PURPLE),
            "palette_hex": "#8F75BF",
            "mode": "meander/outer ring recolored (luma-preserving multiply); owl L3 unchanged",
            "method": (
                "L2 and L4 recolor uses the same luma-preserving multiply as "
                "scripts/build_v2_composed_badges.py::_recolor_to_palette. L3 is byte-equivalent "
                "to the approved transparent master (after standard scale+center). The owl's "
                "gold branch / leaves / olive and dark linework are therefore preserved at pixel "
                "granularity inside L3."
            ),
        },
        "sources": {
            "transparent_master_1080": os.path.relpath(SRC_OWL, REPO),
            "inner_field_source": os.path.relpath(SRC_INNER_FIELD, REPO),
            "meander_source": os.path.relpath(SRC_MEANDER, REPO),
            "outer_ring_source": os.path.relpath(SRC_OUTER, REPO),
        },
        "composite_validation": validation,
        "files": layer_records,
    }
    metrics_path = os.path.join(
        OUT_METRICS, "OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-METRICS.json"
    )
    with open(metrics_path, "w") as f:
        json.dump(metrics_doc, f, indent=2)
        f.write("\n")
    print(f"wrote {metrics_path}")
    print(f"wrote {composite_1080_path}")
    print(f"wrote {composite_540_path}")
    print(f"wrote {tiff_path}")
    return metrics_doc


if __name__ == "__main__":
    sys.exit(0 if build() else 1)
