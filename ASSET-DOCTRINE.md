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

## 6. Disclosure (cross-reference)

AI-assisted raster cleanup and V₄ transform generation were used. Final branch / olive selection was
performed manually by Carey James Balboa in Pixelmator Pro and mapped through a reproducible script.
See [`PROVENANCE.md`](PROVENANCE.md) for the full disclosure.
