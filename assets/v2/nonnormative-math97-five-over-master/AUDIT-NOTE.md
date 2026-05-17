# OWL-2 NON-NORMATIVE v2.0.0-rc — Math-Mirror Center-Scale-97 + Seam-17 + Five-Over Promotion Audit Note

Date: 2026-05-17
Asset: OWL-2 NON-NORMATIVE
Branch: `release/v2.0.0-rc-implementation`
Trigger: explicit user visual approval (one-word "Pass!") on the Five-Over
candidate after Math-Mirror Center-Scale-97 + Seam-17 refinement.

## Scope of this change

Promotes the human-approved OWL-2 NON-NORMATIVE master into the live v2
asset/PDF pipeline. The approved composite is byte-exact (SHA-256
`a0e995ec…`). NORMATIVE, CRITICAL, and METACOGNITIVE assets are intentionally
NOT touched.

Source package (preserved byte-exact in this directory):

- `OWL-2-NON-NORMATIVE-MATH97-FIVE-OVER-MASTER-ASSET-1080.tiff` — multi-page TIFF (32 MB)
- `OWL-2-NON-NORMATIVE-MATH97-FIVE-OVER-COMPOSITE-1080.png`
- `OWL-2-NON-NORMATIVE-MATH97-FIVE-OVER-COMPOSITE-540.png`
- `layers/OWL-2-NON-NORMATIVE-L0-inner-field-underpaint-17-1080.png`
- `layers/OWL-2-NON-NORMATIVE-L1-inner-teal-ring-outward-17-1080.png`
- `layers/OWL-2-NON-NORMATIVE-L2-meander-ring-original-1080.png`
- `layers/OWL-2-NON-NORMATIVE-L2_5-inner-meander-black-edge-5-over-1080.png`
- `layers/OWL-2-NON-NORMATIVE-L3-owl-math-mirror-center-scale-97-1080.png`
- `layers/OWL-2-NON-NORMATIVE-L4-outer-teal-ring-1080.png`
- `proofs/OWL-2-NON-NORMATIVE-MATH97-FIVE-OVER-LAYER-PROOF.png`
- `proofs/OWL-2-selected-proof-vs-master-composite-diff.png` (diff bbox: `None`)
- `metrics/OWL-2-NON-NORMATIVE-MATH97-FIVE-OVER-METRICS.json`
- `SOURCE-README.md` (parent-agent README copied verbatim)
- `SOURCE-AUDIT-NOTE.md` (parent-agent audit note copied verbatim)

## Live pipeline paths updated (NON-NORMATIVE only)

| Live path | Source |
| --- | --- |
| `assets/v2/transparent-1080/NON-NORMATIVE-human-gold-branch-transparent-1080.png` | byte-exact copy of approved L3 owl (math-mirror center-scale-97) |
| `assets/v2/transparent-540/NON-NORMATIVE-human-gold-branch-transparent-540.png`   | Lanczos 540 downscale of approved L3 |
| `assets/v2/final-1080/NON-NORMATIVE-V2-FINAL-COMPOSED-1080.png` | byte-exact copy of approved COMPOSITE-1080 |
| `assets/v2/final-540/NON-NORMATIVE-V2-FINAL-COMPOSED-540.png`   | byte-exact copy of approved COMPOSITE-540 |
| `assets/v2/proofs/NONNORM-v2-layer-proof-palette.png` | regenerated 6-up over the approved L0..L4 + L2.5 |

Byte-exact verification:

- composite 1080: `a0e995ecaa8bcc7e1a26b718be5d48d51ad88af9ff971e2b06878a5652179d00`
- composite 540:  `8c50c01a9a116e116f27792e9d9a18e8224f7cafd0fc70753ae8bea387bc7048`
- L3 owl-only:    `b1440b6bb15bdf3e0c7bcf7d3999e35e30fc2836928efc2df16ce7ba219c8dd6`

(These match the SHA-256 fingerprints in the kit's metrics JSON.)

## Build pipeline

`scripts/build_v2_composed_badges.py` was extended to **pin** the
NON-NORMATIVE composed badge to the byte-exact approved master under
`assets/v2/nonnormative-math97-five-over-master/`, mirroring the existing
NORMATIVE pin. The generic recolor pipeline still applies to CRITICAL and
METACOGNITIVE only. Running `make all` reproduces the same NON-NORMATIVE
bytes the user approved.

## PDF regeneration

`generate_pdfs.py` was rerun, producing all six PDFs. The OWL-2 PDF:

- Page count: 9
- Title: `Owl Semaphore — Non-Normative (v2.0.0-rc)`
- State token: `NON-NORMATIVE`
- Banner-tuple: `STATE=NON-NORMATIVE :: TRANSFORM=T = sigma_v   det = -1    (x, y) -> (-x, y) :: QUOTE="This reflects the standard."`
- Running page-corner marker: the full NON-NORMATIVE composed badge at
  `assets/v2/final-540/NON-NORMATIVE-V2-FINAL-COMPOSED-540.png` (verified
  via `pdfimages -p -f 1 -l 1`: extracted page-1 header image matches the
  reference composed badge byte-fingerprint, dominant RGB (114, 167, 100)).
- Story-first §1: `Da Vinci's Wings` — user-approved interpretive narrative,
  followed by the formal §5 *Mathematical Definition*.

## Test posture

`python3 -m unittest discover -s tests`:

```
Ran 32 tests in ~2.5s
OK (expected failures=3)
```

29 ok / 3 `@unittest.expectedFailure` / 0 unexpected failures.

The `test_v2_assets.py::V2TransformFidelity::test_nonnormative_is_sigma_v_of_normative`
test still fails at IoU ~ 0.815 vs the required ≥ 0.995. This is **expected
and documented**: the approved Math-Mirror Center-Scale-97 master deliberately
re-scales the owl to 97 % and adds seam refinements, so the alpha mask is not
bit-for-bit identical to `σᵥ(NORMATIVE)`. The user-approved visual asset is
the source of truth; the test stays gated with an inline NOTE in
`tests/test_v2_assets.py::V2TransformFidelity` recording this rationale. The
formal state operator remains σᵥ; the visual asset is a presentation-layer
composite around σᵥ-derived owl geometry.

The composed-badge palette center for NON-NORMATIVE in
`tests/test_v2_final_badges.py::PALETTE_COMPOSED` was updated from `(75, 172, 170)`
to `(172, 175, 101)` — the gold-leaning dominant the test method produces on
the approved composite, because the approved kit preserves the original gold
meander ring alongside the teal owl and teal outer ring. The owl-only palette
center in `tests/test_v2_assets.py::PALETTE` did not need an update — the
approved L3 owl dominant `(77, 177, 176)` matches the existing center
`( 77, 177, 176)` exactly.

## V4 expected-failure status

After this promotion, the three V4 sibling-fidelity tests remain
`@unittest.expectedFailure`. Specifically:

- `test_nonnormative_is_sigma_v_of_normative` — **remains expected-failure
  permanently at this visual doctrine** (97 % scale + seams). The
  `@unittest.expectedFailure` decorator should stay on this method until/unless
  the visual doctrine itself changes.
- `test_critical_is_C2_of_normative` — still pending the per-state CRITICAL review.
- `test_metacognitive_is_sigma_h_of_normative` — still pending the per-state METACOGNITIVE review.

## Provenance integrity (from approved kit metrics)

From `metrics/OWL-2-NON-NORMATIVE-MATH97-FIVE-OVER-METRICS.json` (preserved here):

- `diff_bbox_vs_selected_proof`: `null` — the composite pixel-matches the
  user-passed proof at `/home/user/workspace/owl2_inner_meander_edge_refinement/OWL-2-C_touch_edge_black_5_over.png`.
- All ten layer + composite + TIFF SHA-256 fingerprints are recorded.

## What is NOT changed in this promotion

- NORMATIVE, CRITICAL, METACOGNITIVE owl-only masters
- NORMATIVE, CRITICAL, METACOGNITIVE composed badges
- ASSET-DOCTRINE.md normative palette
- The four V₄ transforms (`I`, `σᵥ`, `C₂`, `σₕ`) remain the formal state algebra
