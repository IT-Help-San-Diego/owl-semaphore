#!/usr/bin/env python3
"""Build the OWL-4 METACOGNITIVE layer-proof PNG (3x2 contact sheet) and
mirror it as the v2 proofs/META-v2-layer-proof-palette.png.

Outputs:
    assets/v2/metacognitive-sigma-h-purple-master/proofs/
        OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-LAYER-PROOF.png
    assets/v2/proofs/META-v2-layer-proof-palette.png  (byte-exact copy)
"""

from __future__ import annotations

import os
import shutil

from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KIT = os.path.join(REPO, "assets", "v2", "metacognitive-sigma-h-purple-master")
LAYER_DIR = os.path.join(KIT, "layers")
COMPOSITE = os.path.join(KIT, "OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-COMPOSITE-1080.png")
OUT_KIT = os.path.join(KIT, "proofs", "OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-LAYER-PROOF.png")
OUT_FINAL = os.path.join(REPO, "assets", "v2", "proofs", "META-v2-layer-proof-palette.png")

TILES = [
    ("OWL-4-METACOGNITIVE-L1-inner-field-original-1080.png",
     ("L1  inner field", "byte-exact copy")),
    ("OWL-4-METACOGNITIVE-L2-meander-ring-purple-recolored-1080.png",
     ("L2  meander ring", "purple recolor  ·  luma-preserving")),
    ("OWL-4-METACOGNITIVE-L3-sigma-h-owl-body-gold-branch-preserved-1080.png",
     ("L3  METACOGNITIVE owl", "sigma_h  ·  gold preserved")),
    ("OWL-4-METACOGNITIVE-L4-outer-ring-purple-recolored-1080.png",
     ("L4  outer ring", "purple recolor  ·  luma-preserving")),
    (None,
     ("FINAL COMPOSITE", "sigma_h owl + purple ring")),
    (None,  # blank placeholder
     ("", "")),
]

COLS = 3
ROWS = 2
TILE = 380
CAPTION_H = 64
PAD = 30
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
    im.thumbnail((TILE, TILE), Image.LANCZOS)
    return im


def build() -> None:
    os.makedirs(os.path.dirname(OUT_KIT), exist_ok=True)
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

        # Blank cell support: no image, no caption — leave background BG.
        if fname is None and not line1 and not line2:
            continue

        src = COMPOSITE if fname is None else os.path.join(LAYER_DIR, fname)
        im = _load(src)
        ix = x0 + PAD + (TILE - im.width) // 2
        iy = y0 + PAD + (TILE - im.height) // 2
        bg_tile = Image.new("RGBA", im.size, BG + (255,))
        bg_tile.alpha_composite(im)
        canvas.paste(bg_tile.convert("RGB"), (ix, iy))

        text_y = y0 + PAD + TILE + 6
        max_w = TILE
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
