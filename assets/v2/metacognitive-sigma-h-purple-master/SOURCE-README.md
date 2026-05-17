# OWL-4 METACOGNITIVE sigma_h + Purple Master Asset Kit

This kit captures the v2.0.0-rc OWL-4 METACOGNITIVE asset into the same
structured master-asset-kit shape used by OWL-1, OWL-2, and OWL-3.

## Decision

Per `ASSET-DOCTRINE.md` §3, the METACOGNITIVE palette hex `#8F75BF`
("pending review") is retained for v2.0.0-rc. The existing approved
METACOGNITIVE transparent owl-only master (human-selected gold branch /
leaves / olive, preserved at pixel granularity) is the source of L3.
Meander and outer ring are recolored from the legacy normative-owl
geometry to the METACOGNITIVE palette by the same luma-preserving multiply
used for every other v2 state's recoloring.

The resulting composite is byte-exact equal to the prior-published
METACOGNITIVE composed badge — this kit is a layered re-expression of an
already-approved visible asset, not a new recolor proposal. See
`AUDIT-NOTE.md` for the full provenance reasoning.

## Layer names

1. `L1-inner-field` — byte-exact copy of the legacy normative-owl inner
   field. No color change.
2. `L2-meander-ring` — meander/Greek-key ring recolored to the
   METACOGNITIVE palette via luma-preserving multiply. Alpha preserved
   exactly.
3. `L3-sigma-h-owl-body-gold-branch-preserved` — the approved
   METACOGNITIVE-human-gold-branch transparent master, scaled (Lanczos)
   to the v2 standard 700-px target diameter and pasted centered on a
   1080×1080 canvas. The owl's gold branch / leaves / olive and dark /
   black linework are preserved at pixel granularity through this
   geometry-only operation.
4. `L4-outer-ring` — outer ring recolored to METACOGNITIVE palette
   (same per-pixel luma-preserving multiply as L2).
5. `COMPOSITE-preview` — alpha-composite of L4 -> L2 -> L1 -> L3.

## TIFF note

`OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-MASTER-ASSET-1080.tiff` is a 3-page
TIFF: page 1 is the transparent RGBA composite, page 2 is the same
composite on white, page 3 is on dark slate (30,33,39). It is not a
proprietary Pixelmator/Photoshop editable-layer TIFF — the per-layer
PNG files in `layers/` are the editable layer set.

## Color management

The kit remains in sRGB. No CMYK conversion has been applied.

## Files

- `OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-COMPOSITE-1080.png` — final composite (1080).
- `OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-COMPOSITE-540.png` — final composite (540).
- `OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-MASTER-ASSET-1080.tiff` — multi-page master.
- `layers/OWL-4-METACOGNITIVE-L1-inner-field-original-1080.png`
- `layers/OWL-4-METACOGNITIVE-L2-meander-ring-purple-recolored-1080.png`
- `layers/OWL-4-METACOGNITIVE-L3-sigma-h-owl-body-gold-branch-preserved-1080.png`
- `layers/OWL-4-METACOGNITIVE-L4-outer-ring-purple-recolored-1080.png`
- `metrics/OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-METRICS.json` — per-layer SHA-256s and validation.
- `proofs/OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-LAYER-PROOF.png` — 3×2 layer contact sheet.

## How to rebuild

```
python3 scripts/build_owl4_metacognitive_master.py
python3 scripts/build_owl4_layer_proof.py
make all  # rebuilds composed badges, PDFs, hashes, manifest, tests
```
