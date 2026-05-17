# OWL-3 CRITICAL B-Geometry + B Alert Red Balanced Master Asset Kit

This kit promotes the OWL-3 CRITICAL candidate to the human-approved
**B "alert red balanced"** standard following a controlled six-candidate
perception study (see [`metrics/OWL-3-CRITICAL-B-GEOMETRY-B-BALANCED-METRICS.json`](metrics/OWL-3-CRITICAL-B-GEOMETRY-B-BALANCED-METRICS.json)).

## What changed vs. the superseded kit

| Aspect | Superseded kit (E halfway-salmon, rings only) | This kit (B alert red balanced, body + rings) |
| --- | --- | --- |
| Red RGB | `(226, 92, 96)` | `(218, 55, 65)` |
| Recolor scope | Rings only (L1, L4) | Body + rings (L1, L3, L4) |
| Geometry | B (correct CRITICAL source, OWL-2-matched inner ring) | **Same** — preserved exactly |
| Gold branch / leaves / olive | Preserved | **Preserved** (pixel-granular, via LUT identity) |
| Dark / black linework | Preserved | **Preserved** (pixel-granular, via LUT identity) |
| Inner field (L0) | Original dark | **Byte-exact copy** |
| Meander ring (L2) | Original gold | **Byte-exact copy** |

## Provenance chain

The recolor is derived from `OWL-3-RED-STUDY-B.png`, the study-approved
final composite under `/home/user/workspace/owl3_critical_red_perception_study/`.
The recolor is implemented as a per-pixel LUT (256³ → 3) built from paired
pixels of the superseded salmon composite and the study B composite. The
LUT is identity for unobserved source triples, so any pixel the study left
unchanged is preserved at byte granularity in this kit.

The final composite from this kit matches the study B composite to within
0.074 mean per-channel absolute difference (max 48 on a few rare
anti-aliased edge pixels), with alpha geometry identical (IoU = 1.0).

## Doctrine compliance

- **No global filter applied** — colors are derived per-pixel from the LUT,
  not from a sweep across the whole image.
- **No vector approximation** — every layer is the raster preserved from
  the prior approved B-geometry kit.
- **No stale flattened assets** — `assets/exports/`, `assets/releases/`,
  and `assets/masters/` are not touched.
- **CRITICAL source preserved** — L3 is derived from the previously
  approved `CRITICAL-human-gold-branch-transparent-1080.png` source via
  the same human-gold-branch chain, then color-mapped only.
- **Old kit preserved** — the superseded salmon kit is kept under
  `assets/v2/critical-b-geometry-e-ring-master-superseded/` with its
  hashes, audit note, and a `SUPERSEDED.md` explaining the supersession.

## Files

- `layers/OWL-3-CRITICAL-L0-inner-field-critical-original-1080.png` — byte-exact copy.
- `layers/OWL-3-CRITICAL-L1-inner-red-ring-B-alert-red-balanced-1080.png` — LUT-recolored.
- `layers/OWL-3-CRITICAL-L2-meander-ring-critical-original-1080.png` — byte-exact copy.
- `layers/OWL-3-CRITICAL-L3-B-balanced-owl-body-gold-branch-preserved-1080.png` — LUT-recolored.
- `layers/OWL-3-CRITICAL-L4-outer-ring-B-alert-red-balanced-1080.png` — LUT-recolored.
- `OWL-3-CRITICAL-B-GEOMETRY-B-BALANCED-COMPOSITE-1080.png` — final composite (1080).
- `OWL-3-CRITICAL-B-GEOMETRY-B-BALANCED-COMPOSITE-540.png` — final composite (540).
- `OWL-3-CRITICAL-B-GEOMETRY-B-BALANCED-MASTER-ASSET-1080.tiff` — multi-page master (transparent / on white / on dark slate).
- `metrics/OWL-3-CRITICAL-B-GEOMETRY-B-BALANCED-METRICS.json` — per-layer SHA-256s, bboxes, and recolor metrics.
- `proofs/OWL-3-CRITICAL-B-GEOMETRY-B-BALANCED-LAYER-PROOF.png` — 3×2 contact sheet (rebuilt via `scripts/build_owl3_layer_proof.py`).

## How to rebuild

```
python3 scripts/build_owl3_b_balanced_master.py
python3 scripts/build_owl3_layer_proof.py
make all  # rebuilds composed badges, PDFs, hashes, manifest, tests
```
