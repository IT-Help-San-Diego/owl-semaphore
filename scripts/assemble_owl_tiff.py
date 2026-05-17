#!/usr/bin/env python3
"""Assemble Owl Semaphore v2 master TIFFs.

Layered-TIFF reality check
--------------------------
Photoshop / Pixelmator Pro "layered TIFF" is not a TIFF feature. It is a
proprietary Adobe Image Resources block (TIFF tag 0x8649) carrying a serialised
PSD layer stack. The base TIFF spec only supports *multi-page* TIFFs — multiple
independent IFDs in one file — which Photoshop/Pixelmator open as separate
documents, not as a layer stack.

Pillow can write multi-page TIFFs (true TIFF feature). It cannot write
PSD-compatible layered TIFFs.

This script therefore produces, for each Owl Semaphore v2 state, a
multi-page TIFF whose pages are:

  page 1: the composited owl badge (RGBA, transparent background)
  page 2: the same badge on white
  page 3: the same badge on dark slate

The layer-stack TIFF intended for editorial work in Pixelmator Pro must be
assembled manually by importing the four v2 transparent PNGs (and optionally
the per-state proof-palette PNGs) into Pixelmator Pro and exporting from there.

Usage:
    python3 scripts/assemble_owl_tiff.py
"""
from __future__ import annotations

import os
import sys

from PIL import Image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V2_SRC = os.path.join(REPO, "assets", "v2", "transparent-1080")
V2_OUT = os.path.join(REPO, "assets", "v2", "masters")

STATES = [
    ("NORMATIVE",     "NORMATIVE-human-gold-branch-transparent-1080.png"),
    ("NON-NORMATIVE", "NON-NORMATIVE-human-gold-branch-transparent-1080.png"),
    ("CRITICAL",      "CRITICAL-human-gold-branch-transparent-1080.png"),
    ("METACOGNITIVE", "METACOGNITIVE-human-gold-branch-transparent-1080.png"),
]


def _on_background(rgba: Image.Image, bg: tuple[int, int, int]) -> Image.Image:
    canvas = Image.new("RGB", rgba.size, bg)
    canvas.paste(rgba, mask=rgba.split()[3])
    return canvas


def assemble_state(state: str, fname: str) -> str:
    src = os.path.join(V2_SRC, fname)
    rgba = Image.open(src).convert("RGBA")

    transparent_page = rgba
    white_page = _on_background(rgba, (255, 255, 255))
    dark_page = _on_background(rgba, (30, 33, 39))

    os.makedirs(V2_OUT, exist_ok=True)
    out = os.path.join(V2_OUT, f"{state}-V2-MASTER-1080.tiff")
    transparent_page.save(
        out,
        format="TIFF",
        compression="tiff_adobe_deflate",
        save_all=True,
        append_images=[white_page, dark_page],
    )
    return out


def main() -> int:
    print("Owl Semaphore v2 — assemble_owl_tiff.py")
    print("Mode: multi-page TIFF (true TIFF feature).")
    print("Layered (PSD-style) TIFFs require Pixelmator Pro / Photoshop import.")
    for state, fname in STATES:
        out = assemble_state(state, fname)
        size_mb = os.path.getsize(out) / (1024 * 1024)
        print(f"  OK  {out} ({size_mb:.1f} MB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
