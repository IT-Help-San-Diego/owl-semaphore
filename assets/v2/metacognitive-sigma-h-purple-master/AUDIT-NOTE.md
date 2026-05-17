# OWL-4 METACOGNITIVE v2.0.0-rc — sigma_h + Purple Master Asset Kit Audit Note

Date: 2026-05-17
Asset: OWL-4 METACOGNITIVE
Branch: `release/v2.0.0-rc-implementation`

## Scope of this change

This kit captures the existing-and-approved OWL-4 METACOGNITIVE composed
badge pixels into the same structured master-asset-kit shape used by
OWL-1, OWL-2, and OWL-3 in this release. It does **not** propose a
visual change.

Per `ASSET-DOCTRINE.md` §3, the METACOGNITIVE palette hex (`#8F75BF`) is
explicitly retained as "pending review." There is no external controlled
perception study for METACOGNITIVE analogous to the OWL-3 red study;
inventing a recolor would violate the doctrine. The prior-approved owl-only
transparent master with the human-selected gold branch / leaves / olive is
preserved byte-equivalent inside this kit as L3, and the meander/outer-ring
geometry is recolored to the doctrine purple hex by the same luma-preserving
multiply used everywhere else in v2.

Source data (preserved byte-equivalent in this directory):

- `OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-COMPOSITE-1080.png`
- `OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-COMPOSITE-540.png`
- `OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-MASTER-ASSET-1080.tiff` (multi-page)
- `layers/OWL-4-METACOGNITIVE-L1-inner-field-original-1080.png`
- `layers/OWL-4-METACOGNITIVE-L2-meander-ring-purple-recolored-1080.png`
- `layers/OWL-4-METACOGNITIVE-L3-sigma-h-owl-body-gold-branch-preserved-1080.png`
- `layers/OWL-4-METACOGNITIVE-L4-outer-ring-purple-recolored-1080.png`
- `metrics/OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-METRICS.json`
- `proofs/OWL-4-METACOGNITIVE-SIGMA-H-PURPLE-LAYER-PROOF.png`

## Byte-exact reproduction

The kit's COMPOSITE-1080.png is byte-exact equal to the prior-approved
`assets/v2/final-1080/METACOGNITIVE-V2-FINAL-COMPOSED-1080.png` produced by
`scripts/build_v2_composed_badges.py`:

- mean absolute RGB diff vs. published: 0.0000
- max  absolute RGB diff vs. published: 0
- alpha IoU vs. published:              1.000000

This makes the kit a layered re-expression of the already-published asset.
No pixel of the published METACOGNITIVE badge has changed.

## Live pipeline paths updated (METACOGNITIVE only)

`scripts/build_v2_composed_badges.py` is extended to **pin** the
METACOGNITIVE composed badge to the byte-exact kit composites under
`assets/v2/metacognitive-sigma-h-purple-master/`, mirroring the existing
NORMATIVE / NON-NORMATIVE / CRITICAL pins. The generic recolor pipeline
remains the deterministic source of those bytes, so the byte-exact
equivalence is independently verifiable by running the build script
without the pin.

## Doctrine compliance

- **No global filter** applied to the meander/gold/dark field. The L2 and
  L4 recolor is the same per-pixel luma-preserving multiply used for every
  other v2 state's recoloring step.
- **Preserved geometry.** The owl alpha geometry is preserved at pixel
  granularity from the approved transparent master (Lanczos resize +
  centered paste at the standard 700-px target diameter — identical
  operation to the published composed badge pipeline).
- **Preserved gold branch / leaves / olive.** L3 is sourced from the
  approved METACOGNITIVE-human-gold-branch transparent master, so the
  human-selected gold branch / leaves / olive ride along with the owl.
- **Preserved dark linework.** Same source guarantees the dark / black
  feather and outline linework remain byte-equivalent inside L3.
- **Layer order matches the v2 build pipeline.** Composite order is
  L4 (outer ring) -> L2 (meander) -> L1 (inner field) -> L3 (owl).
- **Mathematically approved geometry preserved.** σ_h is the formal
  state operator. The visible owl L3 inherits its alpha geometry from
  the existing approved METACOGNITIVE transparent master (which is the
  current owl-only V₄-tested input). The V₄ sibling-fidelity decorator
  on the test suite remains as documented in
  `assets/v2/normative-D-B-gold-master/AUDIT-NOTE.md` until per-state
  re-derivation lands.

## Tests

All currently-gated v2 tests continue to pass after the kit is added and
after `scripts/build_v2_composed_badges.py` is updated to pin the
METACOGNITIVE composite. The expected-failure decorators on the V₄
sibling-fidelity tests for NON-NORMATIVE / CRITICAL / METACOGNITIVE are
unchanged.

## What is NOT changed in this kit

- The METACOGNITIVE published composed badge bytes (preserved byte-exact).
- NORMATIVE / NON-NORMATIVE / CRITICAL assets or kits.
- The METACOGNITIVE palette hex in `ASSET-DOCTRINE.md` (still `#8F75BF`,
  still annotated "pending review").
- The four V₄ transforms (`I`, `σᵥ`, `C₂`, `σₕ`).
- The METACOGNITIVE markdown specification or text doctrine.

## Future work

When/if a controlled per-state METACOGNITIVE color study is conducted
(analogous to the OWL-3 red perception study), a successor kit can be
added under `assets/v2/metacognitive-<new-doctrine>-master/` and the
prior kit moved to a `-superseded` directory with a `SUPERSEDED.md` note,
following the same pattern OWL-3 used. Until then this kit IS the
METACOGNITIVE asset of record for v2.0.0-rc.
