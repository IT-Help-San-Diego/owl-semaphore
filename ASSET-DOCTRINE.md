# Owl Semaphore — Asset Doctrine (v2.0.0-rc)

This document is the normative asset doctrine for Owl Semaphore v2.0.0. It supersedes any earlier
asset-direction notes carried as ad-hoc text in the release candidate package. The doctrine itself
was approved by the human author on 2026-05-16 (`/home/user/workspace/owl_authoritative_candidate_v1_3/README.md`,
referenced internally as the v2.0.0 authoritative asset candidate; the v1.3 name on that staging folder
is a historical artifact and is not a target release).

## 1. The owl is the visual master

- The authoritative source is the owl-only clean PNG lineage.
- The full Athena medallion, AOE letters, and surrounding coin decoration are **not** part of the
  mathematical master and are not reintroduced into v2 assets.
- Anything that decorates around the owl is editorial, not algebraic. It does not enter the V₄
  transform input.

### 1a. Mathematical master vs. presentation-layer composed badge

The v2 asset set has two layers, kept strictly separate:

| Layer | Files | Role | Tested by |
| --- | --- | --- | --- |
| **Mathematical master** (algebraic) | `assets/v2/transparent-{1080,540}/<STATE>-human-gold-branch-transparent-{1080,540}.png` | Owl body + human-selected gold branch only. Transparent. V₄-tested source. | `tests/test_v2_assets.py` (V4 fidelity, palette, no speckle) |
| **Presentation-layer composed badge** | `assets/v2/final-{1080,540}/<STATE>-V2-FINAL-COMPOSED-{1080,540}.png` | Final published visible badge: per-state palette meander + outer ring around the owl. | `tests/test_v2_final_badges.py` (presence, palette correctness, no AOE/leaf, no obsolete v1 paths) |

Rules:

- The composed badge is built from the mathematical master plus reused legacy *geometry* layers
  (`assets/layers/normative-owl/NORM-L1-inner-field-1080.png`, `NORM-L2-meander-ring-1080.png`,
  `NORM-L4-outer-ring-1080.png`) recolored to the v2 palette. The legacy `NORM-L3-owl-body-1080.png`
  layer (old owl body), the AOE letters, and the leaf overlay are **NOT** reused. They are
  obsolete v1 contamination and must not appear in any v2 final composite.
- The composed badge is editorial / presentation-layer. It is NOT an input to the V₄ transform and
  is NOT part of the algebraic master. The V₄ algebra still holds on the owl-only master.
- PDFs use the composed badge on title pages, the back-page classification ledger, and the
  contact-sheet section (the published visible badge). They also include the owl-only master
  proof inline so the algebraic source remains visible alongside the editorial composite.
- Both layers must agree on palette: the composed badge ring/meander must use the same
  doctrine hex as the owl body of its state. Test `test_composed_palette_matches_doctrine`
  enforces this against `assets/v2/final-1080/`.

### 1b. Composed-badge build pipeline

The composed badges are produced by `scripts/build_v2_composed_badges.py`. The pipeline is:

1. Open the legacy inner-field, meander, and outer-ring geometry layers.
2. Recolor meander and outer-ring to the per-state palette hex (luma-preserving multiply).
3. Open the v2 owl-only master for the target state, rescale so its bounding box fits the inner
   black field, paste centered.
4. Alpha-composite outer-ring → meander → inner field → owl.
5. Write 1080×1080 PNG; downscale to 540×540 for the small badge.
6. Write the four-up contact sheet `assets/v2/proofs/OWL-SEMAPHORE-V2-FINAL-CONTACT-SHEET.png`.

The script is deterministic given the same inputs. Running `make all` regenerates composites,
recomputes hashes, rewrites the integrity manifest, and runs both test suites.

## 2. Gold branch / olive heritage marker

- The human-selected gold branch / olive element is treated as part of the source owl form
  **before** the V₄ transforms are applied.
- Because it is part of the input to the transform, it is transformed by the same V₄ operation as
  the owl. Its position in the NON-NORMATIVE / CRITICAL / METACOGNITIVE states is therefore
  determined by σᵥ / C₂ / σₕ acting on the NORMATIVE source.
- The branch is **not** a fixed decorative overlay. A fixed overlay would break the algebraic
  relationship between states (the branch would not move with the owl, so the V₄ relations would
  hold for the owl but not for the composite).
- The transform metrics (crop bounding box, resize, master offset, branch-mask bounding box) are
  recorded in `assets/v2/metrics/human_gold_branch_metrics.json`.

## 3. Palette (normative)

| State | Hex | Token in code |
| --- | --- | --- |
| NORMATIVE | `#D8B760` | `PALETTE_NORMATIVE` |
| NON-NORMATIVE | `#2F8C8C` | `PALETTE_NONNORMATIVE` |
| CRITICAL | `#C85B5B` | `PALETTE_CRITICAL` |
| METACOGNITIVE | `#8F75BF` | `PALETTE_METACOGNITIVE` |

Hard rules:

- **CRITICAL red is reserved for CRITICAL.** It MUST NOT be used as the dominant body color of any
  other state.
- **NORMATIVE must never be red.** NORMATIVE is gold. If NORMATIVE appears red at any size, that is a
  regression and the asset is rejected.
- Per-state hue check tolerance is set per-channel in `tests/test_v2_assets.py` and is calibrated
  to the median dominant-RGB sampling of the v2 source PNGs.

## 4. Group-theoretic scope (no overclaim)

- The four transforms form a **finite subgroup of O(2) isomorphic to V₄ (≅ D₂)**.
- The system is not O(2). There is no 31-degree tilt as active doctrine. There is no formal-
  verification claim — invariants are tested by `tests/`, not proved by a proof assistant.
- The geometric transforms applied to the owl + branch composite are exactly:

| State | T | det T | (x, y) ↦ |
| --- | --- | --- | --- |
| NORMATIVE | I | +1 | (x, y) |
| NON-NORMATIVE | σᵥ | −1 | (−x, y) |
| CRITICAL | C₂ | +1 | (−x, −y) |
| METACOGNITIVE | σₕ | −1 | (x, −y) |

## 5. Verification requirements (gated by tests)

### 5a. Mathematical master (owl-only)

`tests/test_v2_assets.py` verifies, against `assets/v2/transparent-1080/`:

1. **File presence** for all four state PNGs at 1080 and 540.
2. **Mode** is RGBA and **size** is 1080×1080 and 540×540 respectively.
3. **V₄ alpha-geometry fidelity:** the alpha mask of each non-NORMATIVE state equals the alpha mask
   of its V₄ image of NORMATIVE under the corresponding transform (Intersection-over-Union = 1.0
   within a single-pixel tolerance band).
4. **Palette correctness per state:** the median opaque non-outline RGB falls inside a calibrated
   ΔE-like RGB box around the doctrine hex.
5. **NORMATIVE-not-red:** the NORMATIVE median dominant RGB has R ≤ G + 40 (it is gold-leaning, not
   red-leaning). The CRITICAL median dominant RGB has R > G + 30 (it is red-leaning). These two
   tests together enforce that NORMATIVE and CRITICAL cannot be swapped.
6. **No black speckle / junk:** count of opaque pixels with luma < 25 outside the owl outline is
   below a hard threshold (zero for the current v2 set).
7. **V₄ algebra invariant:** σᵥ ∘ σᵥ = I, C₂ ∘ C₂ = I, σₕ ∘ σₕ = I, σᵥ ∘ C₂ = σₕ — checked by
   composing the transforms on the NORMATIVE alpha mask.

### 5b. Presentation-layer composed badges

`tests/test_v2_final_badges.py` verifies, against `assets/v2/final-1080/` and
`assets/v2/final-540/`:

1. **File presence** for all four state composed PNGs at 1080 and 540, plus the four-up final
   contact sheet at `assets/v2/proofs/OWL-SEMAPHORE-V2-FINAL-CONTACT-SHEET.png`.
2. **Mode RGBA, size 1080×1080 and 540×540** for the per-state composed badges.
3. **Palette correctness per state:** the dominant non-black, non-near-white RGB falls inside a
   calibrated RGB box around the state's doctrine hex. NORMATIVE remains gold-leaning; CRITICAL
   remains red-leaning.
4. **No obsolete v1 paths referenced in generated PDFs:** the PDF generator must not emit any
   image reference into `assets/releases/`, `assets/masters/`, or `assets/exports/` paths
   (those are v1 lineage). The current `generate_pdfs.py` is greppable text and is checked.
5. **No AOE / no leaf contamination:** the composed badge must not contain the legacy AOE
   letter cluster or the standalone leaf overlay outside the owl body. This is checked
   structurally (forbidden geometry layers are not used) and by checksum (composed badges
   are produced only by `scripts/build_v2_composed_badges.py`, which never references those
   layers).

## 6. Disclosure (cross-reference)

AI-assisted raster cleanup and V₄ transform generation were used. Final branch / olive selection was
performed manually by Carey James Balboa in Pixelmator Pro and mapped through a reproducible script.
See [`PROVENANCE.md`](PROVENANCE.md) for the full disclosure.
