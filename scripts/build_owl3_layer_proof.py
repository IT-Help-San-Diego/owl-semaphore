#!/usr/bin/env python3
"""Rebuild the OWL-3 CRITICAL layer-proof PNG with shorter, non-truncating
captions. Approved composite/TIFF/layer pixels are not modified — only the
proof PNG (a descriptive 3x2 contact sheet of the existing layers) is
re-rasterized so its captions fit the tile width.

Outputs:
    assets/v2/critical-b-geometry-e-ring-master/proofs/
        OWL-3-CRITICAL-B-GEOMETRY-E-RING-LAYER-PROOF.png
    assets/v2/proofs/CRIT-v2-layer-proof-palette.png  (byte-exact copy)
"""

from __future__ import annotations

import os
import shutil

from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KIT = os.path.join(REPO, "assets", "v2", "critical-b-geometry-e-ring-master")
LAYER_DIR = os.path.join(KIT, "layers")
COMPOSITE = os.path.join(KIT, "OWL-3-CRITICAL-B-GEOMETRY-E-RING-COMPOSITE-1080.png")
OUT_KIT = os.path.join(KIT, "proofs", "OWL-3-CRITICAL-B-GEOMETRY-E-RING-LAYER-PROOF.png")
OUT_FINAL = os.path.join(REPO, "assets", "v2", "proofs", "CRIT-v2-layer-proof-palette.png")

# (file, two-line caption). Captions are intentionally short so each line
# fits well inside a tile at the available font size.
TILES = [
    ("OWL-3-CRITICAL-L0-inner-field-critical-original-1080.png",
     ("L0  inner field", "critical original")),
    ("OWL-3-CRITICAL-L1-inner-red-ring-matched-to-OWL2-halfway-salmon-1080.png",
     ("L1  inner red ring", "OWL-2 geometry  ·  halfway salmon")),
    ("OWL-3-CRITICAL-L2-meander-ring-critical-original-1080.png",
     ("L2  meander ring", "critical original")),
    ("OWL-3-CRITICAL-L3-critical-human-gold-branch-B-geometry-1080.png",
     ("L3  CRITICAL owl", "human gold branch  ·  B geometry")),
    ("OWL-3-CRITICAL-L4-outer-critical-ring-halfway-salmon-1080.png",
     ("L4  outer ring", "halfway salmon")),
    (None,  # composite uses COMPOSITE
     ("FINAL COMPOSITE", "B geometry + E ring")),
]

COLS = 3
ROWS = 2
TILE = 380         # tile image area (px)
CAPTION_H = 64     # vertical room for the two caption lines per tile
PAD = 30           # tile padding (gives at least 60 px of gutter between
                   # adjacent caption strings so they never butt together)
BG = (245, 245, 245)


def _font(size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def _load(path: str) -> Image.Image:
    im = Image.open(path).convert("RGBA")
    # Down-sample 1080 to the tile area, preserving the per-layer alpha so
    # transparent layers (rings/owl) read against the BG just like the
    # source kit proof does.
    im.thumbnail((TILE, TILE), Image.LANCZOS)
    return im


def build() -> None:
    cell_w = TILE + 2 * PAD
    cell_h = TILE + CAPTION_H + 2 * PAD
    canvas_w = cell_w * COLS
    canvas_h = cell_h * ROWS
    canvas = Image.new("RGB", (canvas_w, canvas_h), BG)
    draw = ImageDraw.Draw(canvas)

    font_top = _font(18)
    font_sub = _font(15)

    for idx, (fname, (line1, line2)) in enumerate(TILES):
        col = idx % COLS
        row = idx // COLS
        x0 = col * cell_w
        y0 = row * cell_h

        src = COMPOSITE if fname is None else os.path.join(LAYER_DIR, fname)
        im = _load(src)
        # Center the layer within the tile (in case thumbnail didn't fill
        # exactly TILExTILE).
        ix = x0 + PAD + (TILE - im.width) // 2
        iy = y0 + PAD + (TILE - im.height) // 2
        # Flatten alpha onto the proof background — this matches how the
        # source kit proof renders transparent layers.
        bg_tile = Image.new("RGBA", im.size, BG + (255,))
        bg_tile.alpha_composite(im)
        canvas.paste(bg_tile.convert("RGB"), (ix, iy))

        # Two-line caption, centered under the tile. If the rendered text
        # is wider than the tile, shrink the font until it fits — proofs
        # must never spill into a neighboring tile or get clipped.
        text_y = y0 + PAD + TILE + 6
        max_w = TILE  # strict: caption never reaches the gutter
        for line, base_font in ((line1, font_top), (line2, font_sub)):
            font = base_font
            size = base_font.size
            while draw.textlength(line, font=font) > max_w and size > 9:
                size -= 1
                font = _font(size)
            w = draw.textlength(line, font=font)
            draw.text(
                ((x0 + cell_w - w) / 2, text_y),
                line, fill=(40, 40, 40), font=font,
            )
            text_y += font.size + 4

    canvas.save(OUT_KIT, "PNG", optimize=True)
    shutil.copyfile(OUT_KIT, OUT_FINAL)
    print(f"wrote {OUT_KIT} ({canvas.size})")
    print(f"wrote {OUT_FINAL}")


if __name__ == "__main__":
    build()
