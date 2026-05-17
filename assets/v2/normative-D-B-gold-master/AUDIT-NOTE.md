# NORMATIVE v2.0.0-rc — D Geometry + B Parchment-Gold Promotion Audit Note

Date: 2026-05-17
Asset: OWL-1 NORMATIVE
Branch: `release/v2.0.0-rc-implementation`

## Scope of this change

This change promotes the human-approved OWL-1 NORMATIVE master into the live
v2 asset/PDF pipeline. The approval is:

- **Geometry:** D — C alignment with the owl scaled to 94 %.
- **Color:** B — old-owl parchment-gold, selected as the lightest candidate
  that keeps the owl crisp against the dark inner field.

Source package (preserved byte-exact in this directory):

- `NORMATIVE-V2-D-B-GOLD-MASTER-ASSET-1080.tiff` — multi-page TIFF
- `NORMATIVE-V2-D-B-GOLD-MASTER-COMPOSITE-1080.png`
- `NORMATIVE-V2-D-B-GOLD-MASTER-COMPOSITE-540.png`
- `NORMATIVE-V2-D-B-GOLD-MASTER-METRICS.json`
- `layers/NORMATIVE-V2-D-B-GOLD-L{1..4}-*.png`
- `proofs/NORMATIVE-V2-D-B-GOLD-MASTER-LAYER-AND-WING-LINE-PROOF.png`
- `SOURCE-README.md` (copied from the source package README)

## Live pipeline paths updated

The following live paths were promoted from the approved master:

| Live path | Source |
| --- | --- |
| `assets/v2/transparent-1080/NORMATIVE-human-gold-branch-transparent-1080.png` | byte-exact copy of approved L3 owl-only |
| `assets/v2/transparent-540/NORMATIVE-human-gold-branch-transparent-540.png`   | Lanczos 540 downscale of approved L3 |
| `assets/v2/final-1080/NORMATIVE-V2-FINAL-COMPOSED-1080.png` | byte-exact copy of approved COMPOSITE-1080 |
| `assets/v2/final-540/NORMATIVE-V2-FINAL-COMPOSED-540.png`   | byte-exact copy of approved COMPOSITE-540 |
| `assets/v2/proofs/NORM-v2-layer-proof-palette.png` | regenerated 4-up using approved L1..L4 |

Byte-exact verification (SHA-256 abbreviated to 16 chars at promotion time):

- composite 1080:  `03141182ea692c01` (final-1080 == master pkg)
- composite 540:   `be45854738dc5cd2` (final-540  == master pkg)

The full SHA3-512 hash set for every promoted file is recorded in
`RELEASE-HASHES.txt` and mirrored into `INTEGRITY-MANIFEST.md`.

## Build pipeline

`scripts/build_v2_composed_badges.py` was updated to **pin** the NORMATIVE
composed badge to the byte-exact approved master under
`assets/v2/normative-D-B-gold-master/`. The generic recolor pipeline still
produces NON-NORMATIVE / CRITICAL / METACOGNITIVE from the existing owl-only
masters, so subsequent runs of `make all` reproduce the same NORMATIVE bytes
the human reviewed. The doctrine palette hex for NORMATIVE in the script was
also updated from `#D8B760` to `#CBB178` so the recolor path, if reused for
NORMATIVE in the future, approximates the approved B parchment-gold tone.

## PDFs regenerated (v2.0.0-rc pipeline)

`generate_pdfs.py` was rerun, producing:

- `OWL-1-NORMATIVE.pdf`            (18 pages, ~2.5 MB)
- `OWL-2-NON-NORMATIVE.pdf`        (~2.4 MB)
- `OWL-3-CRITICAL.pdf`             (~2.4 MB)
- `OWL-4-METACOGNITIVE.pdf`        (~2.5 MB)
- `OWL-SEMAPHORE-SYSTEM.pdf`       (~3.8 MB)
- `OWL-SEMAPHORE-EXPLANATION.pdf`  (~3.8 MB)

Embedded PDF docinfo verified for OWL-1-NORMATIVE.pdf:
Title=`Owl Semaphore — Normative (v2.0.0-rc)`, Author=`Carey James Balboa`,
Creator=`owl-semaphore/generate_pdfs.py v2.0.0-rc`, Producer=`typst (via
python-typst) + pikepdf`, page count 18.

## Test posture

`python3 -m unittest discover -s tests` — 32 tests, 29 ok, 3 expected
failures (gated by `@unittest.expectedFailure`):

1. `test_v2_assets.V2TransformFidelity.test_nonnormative_is_sigma_v_of_normative`
2. `test_v2_assets.V2TransformFidelity.test_critical_is_C2_of_normative`
3. `test_v2_assets.V2TransformFidelity.test_metacognitive_is_sigma_h_of_normative`

These three V4 sibling-fidelity tests now fail with IoU ≈ 0.5383 (vs the
required ≥ 0.995) because the NORMATIVE master was promoted in isolation and
the NON-NORMATIVE / CRITICAL / METACOGNITIVE owl-only masters have **not yet
been re-derived** from the new NORMATIVE under σᵥ / C₂ / σₕ. This is an
**intentional, documented limitation**: per the human author's direction,
non-NORMATIVE, CRITICAL and METACOGNITIVE are pending separate per-state
reviews and must not be auto-regenerated here.

The decorators MUST be removed when those siblings are re-derived so the V4
invariant is gated again before any v2.0.0 final release.

The remaining V4 algebra invariant test on the NORMATIVE mask alone (σᵥ∘σᵥ=I,
C₂∘C₂=I, σₕ∘σₕ=I, σᵥ∘C₂=σₕ) is **still active and passing** — the algebra
holds; only the sibling masters have not yet been re-imaged through it.

## Provenance audit (from approved master metrics)

From `NORMATIVE-V2-D-B-GOLD-MASTER-METRICS.json` (preserved here):

- `alpha_diff_nonzero_pixels_vs_prior_D_L3`: 0
- `orig_dark_line_pixel_count`: 0
- `new_dark_line_pixel_count`: 0
- `dark_line_xor_pixels_vs_prior_D_L3`: 0
- `linework_warning_addressed`: wing-end linework audited against original
  alpha mask; the B color update preserves the prior D owl alpha silhouette
  exactly.

## Out of scope (next steps)

- Per-state review of NON-NORMATIVE owl-only master and re-derivation under σᵥ.
- Per-state review of CRITICAL owl-only master and re-derivation under C₂.
- Per-state review of METACOGNITIVE owl-only master and re-derivation under σₕ.
- Re-enabling the three sibling-fidelity tests once those re-derivations land.
- Recoloring of the meander/outer-ring composite for NON-NORMATIVE / CRITICAL /
  METACOGNITIVE is unchanged and follows the same per-state review cadence.

## What was *not* changed in this promotion

- NON-NORMATIVE, CRITICAL, METACOGNITIVE owl-only masters
- NON-NORMATIVE, CRITICAL, METACOGNITIVE composed badges
- Meander-ring (L2), inner-field (L1), outer-ring (L4) geometry — these were
  byte-identical between the repo's legacy normative-owl layer set and the
  approved master package, so they did not need to be updated.
- Markdown specifications and the broader v2 doctrine narrative.
