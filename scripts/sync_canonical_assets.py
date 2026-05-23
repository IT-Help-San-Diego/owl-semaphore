#!/usr/bin/env python3
"""Sync repo-tracked OWL Semaphore assets from the four frozen canonical
gold-master folders.

This is the single source-of-truth handoff between the visual-asset workspace
(``/home/user/workspace/owl_canonical_standardization/canonical``) and this
repository's tracked artefacts. Running it is idempotent: it re-derives every
asset under ``assets/`` that the PDF pipeline references from the canonical
masters, then leaves filenames identical so ``generate_pdfs.py`` does not need
to know which OWL revision is in play.

Canonical inputs (frozen by Carey):

  - owl-1-normative-gold-master      -> NORM
  - owl-2-non-normative-gold-master  -> NONNORM
  - owl-3-critical-gold-master       -> CRIT
  - owl-4-metacognitive-gold-master  -> META

Derived outputs:

  assets/releases/540/{KEY}-composite-transparent-540.png  (Lanczos downscale)
  assets/releases/540/{KEY}-composite-dark-540.png         (over #0D1117)
  assets/releases/540/{KEY}-composite-white-540.png        (over #FFFFFF)
  assets/masters/{KEY}-MASTER-1080.tiff                    (canonical TIFF copy)
  assets/masters/{KEY}-proof-transparent-1080.png          (canonical composite)
  assets/exports/{KEY}-MASTER-1080.tiff                    (mirror)
  assets/exports/{KEY}-proof-transparent-1080.png          (mirror)
  assets/proofs/{KEY}-proof-transparent-1080.png           (mirror)
  assets/proofs/{KEY}-layer-proof-palette.png              (canonical layer proof)
  assets/proofs/OWL-SEMAPHORE-MASTER-PROOF.png             (2x2 montage)
  assets/exports/{KEY}-layer-proof-palette.png             (mirror)
  assets/layers/{layer_dir}/                               (canonical layer kit)

The script writes ``assets/CANONICAL-PROVENANCE.json`` recording the source
SHA-256 of every input file so the integrity story is auditable.

Usage:  python3 scripts/sync_canonical_assets.py
        python3 scripts/sync_canonical_assets.py --check    (dry-run, report diffs)
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import shutil
import sys
from pathlib import Path

from PIL import Image

REPO = Path(__file__).resolve().parents[1]
CANONICAL_ROOT = Path(
    os.environ.get(
        "OWL_CANONICAL_ROOT",
        "/home/user/workspace/owl_canonical_standardization/canonical",
    )
)

# state-key -> (canonical-folder, layer-subdir-in-repo, layer-renames)
STATES = {
    "NORM": {
        "folder": "owl-1-normative-gold-master",
        "doc_key": "OWL-1-NORMATIVE",
        "layer_dir": "normative-owl",
        "layer_renames": {
            "OWL-1-NORMATIVE-L1-canonical-inner-field-dark-preserved-1080.png": "NORM-L1-inner-field-1080.png",
            "OWL-1-NORMATIVE-L2-canonical-meander-ring-gold-preserved-1080.png": "NORM-L2-meander-ring-1080.png",
            "OWL-1-NORMATIVE-L3-canonical-owl-gold-parchment-B-preserved-1080.png": "NORM-L3-owl-body-1080.png",
            "OWL-1-NORMATIVE-L4-canonical-outer-ring-gold-preserved-1080.png": "NORM-L4-outer-ring-1080.png",
        },
    },
    "NONNORM": {
        "folder": "owl-2-non-normative-gold-master",
        "doc_key": "OWL-2-NON-NORMATIVE",
        "layer_dir": "nonnormative-owl",
        "layer_renames": {
            "OWL-2-NON-NORMATIVE-L0-canonical-inner-field-underpaint-17-1080.png": "NONNORM-L0-inner-field-underpaint-1080.png",
            "OWL-2-NON-NORMATIVE-L1-canonical-inner-ring-teal-outward-17-1080.png": "NONNORM-L1-inner-field-1080.png",
            "OWL-2-NON-NORMATIVE-L2-canonical-meander-ring-gold-preserved-1080.png": "NONNORM-L2-meander-ring-1080.png",
            "OWL-2-NON-NORMATIVE-L2_5-canonical-inner-meander-black-edge-5-over-1080.png": "NONNORM-L1.5-inner-ring-1080.png",
            "OWL-2-NON-NORMATIVE-L3-canonical-owl-teal-gold-branch-math97-preserved-1080.png": "NONNORM-L3-owl-body-1080.png",
            "OWL-2-NON-NORMATIVE-L4-canonical-outer-ring-teal-preserved-1080.png": "NONNORM-L4-outer-ring-1080.png",
        },
    },
    "CRIT": {
        "folder": "owl-3-critical-gold-master",
        "doc_key": "OWL-3-CRITICAL",
        "layer_dir": "critical-owl",
        "layer_renames": {
            "OWL-3-CRITICAL-L0-canonical-inner-field-deep-oxblood-371218-1080.png": "CRIT-L1-inner-field-1080.png",
            "OWL-3-CRITICAL-L1-canonical-inner-ring-alert-red-preserved-1080.png": "CRIT-L1.5-inner-ring-1080.png",
            "OWL-3-CRITICAL-L2-canonical-meander-ring-gold-preserved-1080.png": "CRIT-L2-meander-ring-1080.png",
            "OWL-3-CRITICAL-L3-canonical-owl-critical-gold-branch-preserved-1080.png": "CRIT-L3-owl-body-1080.png",
            "OWL-3-CRITICAL-L4-canonical-outer-ring-alert-red-preserved-1080.png": "CRIT-L4-outer-ring-1080.png",
        },
    },
    "META": {
        "folder": "owl-4-metacognitive-gold-master",
        "doc_key": "OWL-4-METACOGNITIVE",
        "layer_dir": "metacognitive-owl",
        "layer_renames": {
            "OWL-4-METACOGNITIVE-L1-canonical-inner-field-mid-tan-black-786042-1080.png": "META-L1-inner-field-1080.png",
            "OWL-4-METACOGNITIVE-L1_5-canonical-inner-ring-purple-preserved-1080.png": "META-L1.5-inner-ring-1080.png",
            "OWL-4-METACOGNITIVE-L2-canonical-meander-ring-gold-preserved-1080.png": "META-L2-meander-ring-1080.png",
            "OWL-4-METACOGNITIVE-L3-canonical-owl-purple-gold-branch-88pct-preserved-1080.png": "META-L3-owl-body-1080.png",
            "OWL-4-METACOGNITIVE-L4-canonical-outer-ring-purple-preserved-1080.png": "META-L4-outer-ring-1080.png",
        },
    },
}

DARK_BG = (13, 17, 23, 255)   # GitHub dark canvas
WHITE_BG = (255, 255, 255, 255)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def composite_over(transparent: Image.Image, bg: tuple[int, int, int, int]) -> Image.Image:
    background = Image.new("RGBA", transparent.size, bg)
    background.alpha_composite(transparent.convert("RGBA"))
    return background.convert("RGB")


def downscale(img: Image.Image, side: int) -> Image.Image:
    return img.convert("RGBA").resize((side, side), Image.LANCZOS)


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def copy_file(src: Path, dst: Path, provenance: dict, role: str, key: str) -> None:
    ensure_dir(dst.parent)
    shutil.copyfile(src, dst)
    rel = str(dst.relative_to(REPO))
    provenance.setdefault(key, {}).setdefault(role, []).append({
        "source": str(src),
        "source_sha256": sha256(src),
        "destination": rel,
    })


def sync_state(key: str, spec: dict, provenance: dict, *, check_only: bool) -> list[str]:
    diffs: list[str] = []
    folder = CANONICAL_ROOT / spec["folder"]
    if not folder.is_dir():
        raise SystemExit(f"Canonical folder missing: {folder}")

    composite_src = folder / f"{spec['doc_key']}-CANONICAL-COMPOSITE-1080.png"
    tiff_src = folder / f"{spec['doc_key']}-CANONICAL-MASTER-ASSET-1080.tiff"
    layer_proof_src = folder / "proofs" / f"{spec['doc_key']}-CANONICAL-LAYER-PROOF.png"

    if not composite_src.is_file():
        raise SystemExit(f"Missing canonical composite: {composite_src}")
    if not tiff_src.is_file():
        raise SystemExit(f"Missing canonical TIFF: {tiff_src}")
    if not layer_proof_src.is_file():
        raise SystemExit(f"Missing canonical layer proof: {layer_proof_src}")

    img1080 = Image.open(composite_src).convert("RGBA")

    targets: list[tuple[Path, Image.Image | Path, str]] = []
    targets.append((REPO / "assets" / "masters" / f"{key}-MASTER-1080.tiff", tiff_src, "master_tiff"))
    targets.append((REPO / "assets" / "exports" / f"{key}-MASTER-1080.tiff", tiff_src, "master_tiff_export"))
    targets.append((REPO / "assets" / "masters" / f"{key}-proof-transparent-1080.png", composite_src, "composite_transparent_master"))
    targets.append((REPO / "assets" / "exports" / f"{key}-proof-transparent-1080.png", composite_src, "composite_transparent_export"))
    targets.append((REPO / "assets" / "proofs" / f"{key}-proof-transparent-1080.png", composite_src, "composite_transparent_proof"))
    targets.append((REPO / "assets" / "proofs" / f"{key}-layer-proof-palette.png", layer_proof_src, "layer_proof_palette"))
    targets.append((REPO / "assets" / "exports" / f"{key}-layer-proof-palette.png", layer_proof_src, "layer_proof_palette_export"))

    img540_transparent = downscale(img1080, 540)
    img540_dark = composite_over(img540_transparent, DARK_BG)
    img540_white = composite_over(img540_transparent, WHITE_BG)

    derived: list[tuple[Path, Image.Image, str]] = [
        (REPO / "assets" / "releases" / "540" / f"{key}-composite-transparent-540.png", img540_transparent, "release_540_transparent"),
        (REPO / "assets" / "releases" / "540" / f"{key}-composite-dark-540.png", img540_dark, "release_540_dark"),
        (REPO / "assets" / "releases" / "540" / f"{key}-composite-white-540.png", img540_white, "release_540_white"),
    ]

    if check_only:
        for dst, src_or_img, _role in targets:
            if not dst.exists():
                diffs.append(f"missing: {dst.relative_to(REPO)}")
        for dst, _img, _role in derived:
            if not dst.exists():
                diffs.append(f"missing: {dst.relative_to(REPO)}")
        return diffs

    for dst, src, role in targets:
        copy_file(src, dst, provenance, role, key)

    for dst, img, role in derived:
        ensure_dir(dst.parent)
        img.save(dst, "PNG", optimize=True)
        provenance.setdefault(key, {}).setdefault(role, []).append({
            "source": str(composite_src),
            "source_sha256": sha256(composite_src),
            "destination": str(dst.relative_to(REPO)),
            "transform": "Lanczos 1080->540" + (
                "" if role.endswith("transparent") else
                (" + composite over #0D1117FF" if role.endswith("dark") else " + composite over #FFFFFFFF")
            ),
        })

    layer_src_dir = folder / "layers"
    layer_dst_dir = REPO / "assets" / "layers" / spec["layer_dir"]
    ensure_dir(layer_dst_dir)
    for existing in layer_dst_dir.iterdir():
        if existing.is_file():
            existing.unlink()
    for src_name, dst_name in spec["layer_renames"].items():
        src = layer_src_dir / src_name
        if not src.is_file():
            raise SystemExit(f"Missing canonical layer: {src}")
        dst = layer_dst_dir / dst_name
        copy_file(src, dst, provenance, "layer", key)

    return diffs


def build_master_proof(provenance: dict) -> None:
    """2x2 montage of the four canonical 1080 composites over white."""
    tile = 1080
    pad = 60
    cap_h = 110
    cols, rows = 2, 2
    canvas_w = pad + cols * tile + (cols - 1) * pad + pad
    canvas_h = pad + rows * (tile + cap_h) + (rows - 1) * pad + pad
    canvas = Image.new("RGB", (canvas_w, canvas_h), (255, 255, 255))

    order = ["NORM", "NONNORM", "CRIT", "META"]
    sources = []
    for idx, key in enumerate(order):
        spec = STATES[key]
        comp = CANONICAL_ROOT / spec["folder"] / f"{spec['doc_key']}-CANONICAL-COMPOSITE-1080.png"
        sources.append(comp)
        col, row = idx % cols, idx // cols
        x = pad + col * (tile + pad)
        y = pad + row * (tile + cap_h + pad)
        tile_img = composite_over(Image.open(comp).convert("RGBA"), (255, 255, 255, 255))
        canvas.paste(tile_img, (x, y))

    out = REPO / "assets" / "proofs" / "OWL-SEMAPHORE-MASTER-PROOF.png"
    ensure_dir(out.parent)
    canvas.save(out, "PNG", optimize=True)
    provenance["MASTER_PROOF_MONTAGE"] = {
        "destination": str(out.relative_to(REPO)),
        "sources": [
            {"path": str(p), "source_sha256": sha256(p)} for p in sources
        ],
        "layout": "2x2 (NORM, NONNORM / CRIT, META) over white, 1080px tiles",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="report missing outputs but make no changes")
    args = parser.parse_args()

    provenance: dict = {
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "canonical_root": str(CANONICAL_ROOT),
        "script": "scripts/sync_canonical_assets.py",
    }

    all_diffs: list[str] = []
    for key, spec in STATES.items():
        diffs = sync_state(key, spec, provenance, check_only=args.check)
        all_diffs.extend(diffs)

    if args.check:
        if all_diffs:
            print("Canonical sync drift detected:")
            for line in all_diffs:
                print(f"  {line}")
            return 1
        print("Canonical sync: no drift detected.")
        return 0

    build_master_proof(provenance)

    prov_path = REPO / "assets" / "CANONICAL-PROVENANCE.json"
    with prov_path.open("w") as f:
        json.dump(provenance, f, indent=2, sort_keys=True)
    print(f"Wrote {prov_path.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
