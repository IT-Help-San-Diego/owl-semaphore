# Changelog — Owl Semaphore Badge System

All notable changes to this project are documented in this file.

The format roughly follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project's versioning aligns with semantic-versioning intent for a specification (MAJOR = algebra change; MINOR = additive content/metadata; PATCH = errata).

Each release entry records the **canonical formal sentence used in that release** so the conceptual evolution of the system is auditable.

---

## [Unreleased — v2.0.0-rc] — major release candidate (no Zenodo DOI minted, no tag)

### 2026-05-17 — OWL-2 title-page hyphenation fix

- `OWL-2-NON-NORMATIVE.pdf` page 1 previously wrapped its big title as
  *"Owl Semaphore — Non-Norma- / tive"* — Typst's hyphenation broke the
  state name mid-word at 28 pt bold on US-letter.
- Fix in `generate_pdfs.py::build_typst_document()` — surgical, OWL-2 only:
  - Compute a typeset-only title variant by replacing the ASCII hyphen in
    `"Non-Normative"` with U+2011 (non-breaking hyphen). The state name
    is now atomic to the line breaker; the title wraps cleanly at the
    em-dash word boundary instead of breaking inside the state name.
  - Detect this case by `"‑" in title_typeset` (only OWL-2 ever has it);
    when set, wrap the big-title `#text` in `#par(justify: false)` so the
    two-line title is centered rather than justified edge-to-edge. Also
    set `hyphenate: false` as belt-and-suspenders.
  - When the typeset title contains no U+2011 (the other five PDFs), the
    code path is byte-identical to the pre-fix version: a single
    `#text(size: 28pt, weight: "bold")[…]` with no surrounding wrappers.
    OWL-1, OWL-3, OWL-4, OWL-SEMAPHORE-SYSTEM, and OWL-SEMAPHORE-EXPLANATION
    titles are unchanged in layout (verified via pdftotext diff).
- PDF docinfo `/Title` remains `"Owl Semaphore — Non-Normative (v2.0.0-rc)"`
  with the ASCII hyphen (searchable / copyable). Only the *visible* big
  title on the title page renders the U+2011 non-breaking hyphen — visually
  indistinguishable.
- All six PDFs regenerated. Tests pass (32 ran, 29 ok, 3 expected failures
  unchanged). Hashes/manifest regenerated.

### 2026-05-17 — OWL-2 NON-NORMATIVE promoted to Math-Mirror Center-Scale-97 + Seam-17 + Five-Over

- **OWL-2 NON-NORMATIVE master asset** promoted to the human-approved
  Math-Mirror Center-Scale-97 + Seam-17 + Five-Over master. User
  approval was the one-word "Pass!" on the Five-Over candidate after
  Math-Mirror Center-Scale-97 and Seam-17 refinement. The composite asset
  is byte-exact (SHA-256 `a0e995ec…`) with the user-passed proof at
  `/home/user/workspace/owl2_inner_meander_edge_refinement/OWL-2-C_touch_edge_black_5_over.png`
  (diff bbox: `None`).
- Source package preserved under
  `assets/v2/nonnormative-math97-five-over-master/` (TIFF + 6 layers +
  composites + metrics + 2 proofs + SOURCE-README + SOURCE-AUDIT-NOTE
  + AUDIT-NOTE).
- Live paths updated (NON-NORMATIVE only):
  `assets/v2/transparent-{1080,540}/NON-NORMATIVE-…png`,
  `assets/v2/final-{1080,540}/NON-NORMATIVE-V2-FINAL-COMPOSED-…png`,
  `assets/v2/proofs/NONNORM-v2-layer-proof-palette.png` (regenerated 6-up
  showing L0..L4 + L2.5 of the approved kit).
- `scripts/build_v2_composed_badges.py` now pins NON-NORMATIVE to the
  approved composite byte-exact (mirrors the existing NORMATIVE pin).
- `OWL-2-NON-NORMATIVE.md`:
  - Inserted new `## 1. Da Vinci's Wings` with the user-approved
    interpretive story (mirror, Leonardo da Vinci's wing studies, Wright
    Brothers 400 years later, non-normative work as the engine of progress).
    Frames itself as orientation, not proof.
  - Renumbered all subsequent sections by +1 (old 1..18 → 2..19) and
    bumped every nested `### N.M` subsection parent number by +1 for
    coherence (same fix pattern as OWL-1).
  - Rewrote §8 Asset Topology to reflect the L0/L1/L2/L2.5/L3/L4 layer
    structure of the approved kit.
  - Rewrote §10 Color Specification with the approved observed dominant
    RGB (77, 177, 176) ≈ `#4DB1B0`.
  - Rewrote §12 Provenance to point at the kit and honestly describe the
    Math-Mirror Center-Scale-97 construction (not a pure pixel-array σᵥ;
    the visual master adds the 97 % re-scale and seam refinements while
    the formal state operator remains σᵥ).
- `tests/test_v2_assets.py::V2TransformFidelity` docstring updated to
  explain that `test_nonnormative_is_sigma_v_of_normative` is
  **permanently** expected-failure at this visual doctrine (IoU ~ 0.815
  due to the 97 % re-scale). CRITICAL and METACOGNITIVE V4 tests remain
  pending per-state reviews.
- `tests/test_v2_final_badges.py::PALETTE_COMPOSED["NON-NORMATIVE"]`
  updated from `(75, 172, 170)` to `(172, 175, 101)` — the test-method
  composed-dominant on the approved kit. The kit preserves the original
  gold meander, so the luma-band-restricted median is gold-leaning;
  this is the approved visual, not a regression.
- `ASSET-DOCTRINE.md` §3 palette table extended with an "approved-master
  observed RGB" column and a note that CRITICAL / METACOGNITIVE remain
  pending review.
- `scripts/compute_hashes.py` extended to cover the new NN master kit
  directory (TIFF, layers, proofs, metrics, READMEs, AUDIT-NOTE).
- All six PDFs regenerated. `OWL-2-NON-NORMATIVE.pdf` rendered at 9 pages,
  ~2.4 MB, with full embedded docinfo. The running page-corner marker is
  the full NON-NORMATIVE composed medallion (verified via `pdfimages`).
- `RELEASE-HASHES.txt` + `INTEGRITY-MANIFEST.md` regenerated.

### 2026-05-17 — PDF byline broadened to "Independent Researcher"

- The visible title-page byline in `generate_pdfs.py` was changed from
  *"Independent DNS Security Researcher"* to the broader, more accurate
  *"Independent Researcher"*. The Owl Semaphore is not exclusively a DNS
  artifact; the prior label under-described its scope.
- All other identity / provenance / licensing metadata on the title page
  is unchanged: name `Carey James Balboa`, `ORCID 0009-0000-5237-9065`,
  `CONCEPT-DOI 10.5281/zenodo.19473697`, `PUBLISHED-VERSION-DOI
  10.5281/zenodo.19474599`, `RC-VERSION-DOI TBD_BY_ZENODO_ON_RELEASE`,
  `SOURCE github.com/IT-Help-San-Diego/owl-semaphore`, `VERSION v2.0.0-rc`,
  `LICENSE CC-BY-4.0`.
- The "DNS Tool" keyword in PDF docinfo and pikepdf metadata stays — it
  describes the upstream project context, not an author credential, and
  the system genuinely grew out of DNS Tool.
- All six PDFs regenerated. pdftotext: old byline "Independent DNS Security
  Researcher" appears 0 times in every PDF; new byline "Independent
  Researcher" appears once per PDF (the title page).

### 2026-05-17 — Page-header marker switched to per-state composed badge

- `generate_pdfs.py` now uses each document's `final_badge` (the full per-state
  composed medallion at 540 px) as the small running page-corner marker in
  the Typst page header, instead of the prior owl-only transparent thumbnail.
  Resolved paths per document:
  - `OWL-1-NORMATIVE.pdf`               → `assets/v2/final-540/NORMATIVE-V2-FINAL-COMPOSED-540.png`
  - `OWL-2-NON-NORMATIVE.pdf`           → `assets/v2/final-540/NON-NORMATIVE-V2-FINAL-COMPOSED-540.png`
  - `OWL-3-CRITICAL.pdf`                → `assets/v2/final-540/CRITICAL-V2-FINAL-COMPOSED-540.png`
  - `OWL-4-METACOGNITIVE.pdf`           → `assets/v2/final-540/METACOGNITIVE-V2-FINAL-COMPOSED-540.png`
  - `OWL-SEMAPHORE-SYSTEM.pdf`          → `assets/v2/final-540/NORMATIVE-V2-FINAL-COMPOSED-540.png`
  - `OWL-SEMAPHORE-EXPLANATION.pdf`     → `assets/v2/final-540/METACOGNITIVE-V2-FINAL-COMPOSED-540.png`
- The owl-only master remains the algebraic source and continues to be shown
  inline in the *Owl-Only Mathematical Master — V4-Tested Source* proof block
  under the contact sheet, per `ASSET-DOCTRINE.md §1a`.
- `ASSET-DOCTRINE.md §1a` updated to record that the running page-corner
  marker is now the composed medallion.
- No state assets were modified; only the running-header image path changed.
  Each PDF still uses *its own* per-state badge.
- Visual evidence: `pdfimages -p -f 1 -l 1` extracted the page-1 header image
  from each regenerated PDF and confirmed it is byte-equivalent to the
  corresponding `assets/v2/final-540/<STATE>-V2-FINAL-COMPOSED-540.png`
  (identical dominant RGB and identical ~0.49 dark-opaque ratio, vs the
  owl-only master's 0.00 dark-opaque ratio).
- 31°/lean/tilt scrub re-checked across all six active PDFs: 0 matches each.

### 2026-05-17 — OWL-1-NORMATIVE: fix subsection numbering after §1 insertion

- QA after the *Proven Ground* §1 insertion caught that `### N.M` subsection
  headings still carried the pre-insertion parent number (e.g. *4. Ontological
  Role* was followed by *3.1 Semantic Designation*).
- Renumbered all 60 `###` subsection headings in `OWL-1-NORMATIVE.md` by +1 on
  the parent: §4 → 4.1/4.2/4.3, §5 → 5.1..5.5, §7 → 7.1..7.5, §8 → 8.1/8.2,
  §9 → 9.1/9.2/9.3, §10 → 10.1..10.4, §11 → 11.1..11.4, §12 → 12.1..12.3,
  §13 → 13.1..13.3, §14 → 14.1..14.4, §15 → 15.1..15.5, §16 → 16.1..16.5,
  §17 → 17.1..17.3, §18 → 18.1..18.3, §21 → 21.1..21.8.
- Audited the body for stray decimal cross-references that might still cite
  the old numbering; only non-section decimals remain (e.g. the 8.69:1
  contrast ratio).
- Regenerated `OWL-1-NORMATIVE.pdf`; pdftotext confirms every parent N is
  followed by N.1, N.2, … with no parent/child mismatches.
- 31°/lean/tilt scrub re-checked across all six active PDFs: 0 matches each.

### 2026-05-17 — OWL-1 NORMATIVE reader-facing story moved to top of doc

- Added a new `## 1. The Proven Ground` at the top of `OWL-1-NORMATIVE.md` so
  the plain-English NORMATIVE example (upright, feet planted, (x, y) ↦ (x, y);
  Newton's laws as a 200-year normative ground) appears immediately after the
  title page and visual proof pages, before the formal `Statement of Intent`
  and `System Context`.
- Renumbered all subsequent sections by +1 (old 1 → 2, …, old 23 → 24).
  Total sections now 24. No internal cross-references depended on the prior
  numbering, so renaming is purely additive at the head.
- The new section explicitly frames itself as **orientation, not proof**, and
  points readers to the now-§5 *Mathematical Definition* for the formal
  identity-transform statement. The state-line at the top of the new section
  is the canonical `T = I, det = +1, (x, y) ↦ (x, y)` so the formal object
  remains visible alongside the story.
- No 31°/lean/tilt language was reintroduced. No non-NORMATIVE / CRITICAL /
  METACOGNITIVE source was modified by this revision (those PDFs were merely
  rebuilt by the unified `generate_pdfs.py` run).

### 2026-05-17 — Removed obsolete 31°/lean/tilt content from active scientific docs

- Removed `## 21. Forward-Looking Rule for the 31° Lean` from
  `OWL-1-NORMATIVE.md`; renumbered subsequent sections (22→21, 23→22, 24→23).
- Removed `### 3.3 The 31° Rotation` (and the now-redundant `### 3.2 Continuous
  Process` lead-in) from `OWL-SEMAPHORE-SYSTEM.md`; section 3.4 Principle is
  renumbered to 3.2 and rephrased to enumerate the four V₄ transforms only.
- Replaced `INTEGRITY-MANIFEST.md` §6.3 *State vs Process* with §6.3 *Scope of
  the State Algebra* — the state algebra is exactly the four V₄ transforms
  (I, σᵥ, C₂, σₕ); any other operator is out of scope for state assignment.
- Trimmed 31°/lean/tilt mentions from active doctrine language in `README.md`,
  `ASSET-DOCTRINE.md` §4, `ZENODO-RELEASE-CHECKLIST.md` §2, and
  `.zenodo.json` description.
- Quarantined the history into `PROVENANCE.md` §7 *Historical-only: the v1-era
  ~31° rotation note*. This is the single place in the repo where the
  historical removal is recorded, for full audit-trail traceability. It is
  not active doctrine and is not cited by any active publication.
- Regenerated all six PDFs. `pdftotext` audit on the new PDFs reports zero
  occurrences of `31°`, `31 deg`, `tilt`, or `lean` in active scientific
  documents; the only `180° rotation` references are legitimate (C₂).

### 2026-05-17 — NORMATIVE promoted to D-geometry + B parchment-gold

- **OWL-1 NORMATIVE master asset** promoted to the human-approved
  D-geometry + B parchment-gold master. Approval is byte-exact on the
  composites; the source package is preserved under
  `assets/v2/normative-D-B-gold-master/` (TIFF + L1..L4 + composites +
  metrics + wing-line proof + `SOURCE-README.md` + `AUDIT-NOTE.md`).
- Live paths updated (NORMATIVE only):
  `assets/v2/transparent-1080/NORMATIVE-...-1080.png`,
  `assets/v2/transparent-540/NORMATIVE-...-540.png`,
  `assets/v2/final-1080/NORMATIVE-V2-FINAL-COMPOSED-1080.png`,
  `assets/v2/final-540/NORMATIVE-V2-FINAL-COMPOSED-540.png`,
  `assets/v2/proofs/NORM-v2-layer-proof-palette.png`.
- `scripts/build_v2_composed_badges.py` now pins NORMATIVE to the approved
  composite byte-exact and updates the NORMATIVE doctrine hex to a B
  parchment-gold tone (`#CBB178`); other states unchanged.
- `tests/test_v2_assets.py` and `tests/test_v2_final_badges.py` palette
  centers updated for NORMATIVE only (other states unchanged).
- Three V4 sibling-fidelity tests
  (`test_nonnormative_is_sigma_v_of_normative`,
  `test_critical_is_C2_of_normative`,
  `test_metacognitive_is_sigma_h_of_normative`) are now marked
  `@unittest.expectedFailure` because the sibling masters have not yet
  been re-derived from the new NORMATIVE under V4. These decorators MUST
  be removed before v2.0.0 final release, once each sibling has its own
  per-state human review.
- All six PDFs regenerated by `generate_pdfs.py`. `OWL-1-NORMATIVE.pdf`
  rendered at 18 pages, ~2.5 MB, with full embedded docinfo.
- `RELEASE-HASHES.txt` and `INTEGRITY-MANIFEST.md` regenerated (71 entries,
  up from 61).

**Canonical formal sentence (this release):**
> *A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants.*

**Canonical operational sentence:** *A four-state visual system for marking how a claim, document, dataset, or finding should be evaluated before belief, challenge, or action.*

**Canonical human sentence:** *Four owls tell the reader what kind of thinking they are looking at: standard, exploration, inversion, or self-audit.*

**Version DOI:** `TBD_BY_ZENODO_ON_RELEASE` — Zenodo has not minted the v2.0.0 version DOI; this branch is a release candidate.

**Why MAJOR:** the authoritative artifact set is replaced. The owl-only PNG lineage becomes the
visual master; the full Athena medallion / AOE letters / surrounding decoration is not part of the
v2 mathematical master. The human-selected gold branch / olive heritage marker is part of the
source owl form **before** the V₄ transforms, so it transforms with the owl rather than being a
fixed decorative overlay. The V₄ algebra and the σₕ assignment for METACOGNITIVE are unchanged
from v1.3.0-rc.

### Added

- `assets/v2/transparent-1080/` and `assets/v2/transparent-540/` — the authoritative owl-only PNGs
  with the human-selected gold branch, named `{STATE}-human-gold-branch-transparent-{1080|540}.png`.
- `assets/v2/masters/` — multi-page TIFF masters for each state (transparent / on white / on dark
  pages), produced by `scripts/assemble_owl_tiff.py`.
- `assets/v2/proofs/OWL-SEMAPHORE-V2-MASTER-PROOF.png` — v2 contact sheet across the four states.
- `assets/v2/proofs/{NORM,NONNORM,CRIT,META}-v2-layer-proof-palette.png` — per-state proof-palette
  composites used by the per-state PDFs.
- `assets/v2/metrics/human_gold_branch_metrics.json` — gold-branch selection metrics carried over
  from the v2 authoritative asset candidate package.
- `ASSET-DOCTRINE.md` — normative asset doctrine for v2 (owl-only master, gold branch before V₄,
  palette rules, NORMATIVE-not-red guardrail, verification gates).
- `PROVENANCE.md` — AI-assisted-cleanup / Pixelmator Pro provenance disclosure, layered-TIFF
  feasibility statement, what is and is not claimed.
- `scripts/assemble_owl_tiff.py` — multi-page TIFF assembler.
- `tests/test_v2_assets.py` — V₄ alpha-geometry fidelity, palette correctness per state,
  NORMATIVE-not-red guardrail, CRITICAL-is-red guardrail, V₄ algebra invariants, black-speckle /
  junk-pixel check.
- `make tiffs` Makefile target to regenerate v2 multi-page TIFFs.
- `assets/v2/final-1080/` and `assets/v2/final-540/` — final composed badge assets (presentation
  layer): per-state palette meander + outer ring around the v2 owl-only master. These are the
  *published visible badge*. The mathematical master remains the owl-only transparent PNG.
- `assets/v2/proofs/OWL-SEMAPHORE-V2-FINAL-CONTACT-SHEET.png` — four-up contact sheet of the
  final composed badges, intended for editorial visual review.
- `scripts/build_v2_composed_badges.py` — deterministic composed-badge build pipeline. Reuses
  legacy geometry layers (`NORM-L1-inner-field`, `NORM-L2-meander-ring`, `NORM-L4-outer-ring`)
  recolored to the v2 palette, around the v2 owl-only master. Does NOT reuse the legacy
  `NORM-L3-owl-body` layer or the AOE letters or the leaf overlay.
- `tests/test_v2_final_badges.py` — final-badge presence, mode/size, per-state composed-palette
  correctness, structural sanity (inner black field present, ring reaches the canvas edge),
  guardrail that `generate_pdfs.py` does not silently revert to v1 lineage paths
  (`assets/releases/`, `assets/masters/`, `assets/exports/`).
- `make badges` Makefile target to regenerate the v2 final composed badges and contact sheet.

### Changed

- README masthead updated to point at the v2 master proof and to describe v2.0.0-rc as a major
  release with the owl-only doctrine.
- `generate_pdfs.py` switched to consume v2 badges and v2 proof-palette images from `assets/v2/`.
  Title pages and the back-page classification ledger now use the **final composed badges**
  (`assets/v2/final-540/<STATE>-V2-FINAL-COMPOSED-540.png`) as the published visible badge.
  The header thumbnail and an inline "owl-only mathematical master proof" panel continue to
  show the owl-only transparent master so the algebraic source remains visible alongside the
  presentation composite.
- Per-state spec mastheads (`OWL-1` through `OWL-4`) now reference the v2 final composed badge
  as the leading image, replacing the v1 `assets/proofs/<STATE>-layer-proof-palette.png` image.
- Active document version stamps in the v2 spec docs updated from "Version 1.3.0-rc" to
  "Version 2.0.0-rc"; canonical-sentence-stack section header retitled to "v2.0.0-rc".
  Historical "deprecated as of v1.3.0-rc" notes are retained (they record when the deprecation
  happened) and the "carried forward in v2.0.0-rc" continuity is now explicit.
- Banner-tuple test target updated to `v2.0.0-rc` (state quotes and transforms unchanged).
- `INTEGRITY-MANIFEST.md` scope extended to cover the v2 asset directory, the multi-page TIFF
  masters, and the new doctrine + provenance markdown files.
- Schema.org JSON-LD in README updated to v2.0.0-rc release notes.

### Not changed

- V₄ algebra: unchanged.
- σₕ ↔ METACOGNITIVE assignment: unchanged.
- METACOGNITIVE phrasing: unchanged from v1.3.0-rc (*"The observer audits the frame"* /
  *"Thinking examines its own frame"*).
- Group-theoretic scope language: still **finite subgroup of O(2) isomorphic to V₄ (≅ D₂)**; the
  system is not O(2). The state algebra is exactly the four V₄ transforms (*I*, σᵥ, C₂, σₕ); no
  other operator is reintroduced. No formal-verification claim is added.

### Non-goals (explicit, v2.0.0-rc)

- No Zenodo upload, no `git tag`, no PR merge for v2.0.0 from this branch.
- No new DOI is minted in this branch. The v2.0.0 version DOI placeholder is `TBD_BY_ZENODO_ON_RELEASE`.
- No PSD-compatible layered TIFF is generated by code; producing one requires Pixelmator Pro /
  Photoshop import. See [`PROVENANCE.md`](PROVENANCE.md) §4.

---

## [Unreleased — v1.3.0-rc] — release candidate (no Zenodo DOI minted, no tag)

**Canonical formal sentence (this release):**
> *A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants.*

**Canonical operational sentence:** *A four-state visual system for marking how a claim, document, dataset, or finding should be evaluated before belief, challenge, or action.*

**Canonical human sentence:** *Four owls tell the reader what kind of thinking they are looking at: standard, exploration, inversion, or self-audit.*

**Version DOI:** `TBD_BY_ZENODO_ON_RELEASE` — Zenodo has not minted the v1.3.0 version DOI; this branch is a release candidate.

### Added

- `OWL-SEMAPHORE-EXPLANATION.md` — informative companion document with the DNS Tool origin story, archetype audience rationale, the "why four states, not two" argument, the V₄ rationale, the METACOGNITIVE-language refinement, the accessibility rule, and bridges to DNS Tool and Zenodo.
- `CHANGELOG.md` — this file. Per-release record of the canonical sentence and the changes that produced it.
- `Makefile` — single-command pipeline. Targets: `pdfs`, `hashes`, `manifest`, `test`, `clean`, `all`.
- `tests/test_banner_tuple.py` — integrity test that extracts page-one text from every generated PDF and verifies the expected state name, transform symbol, determinant, coordinate mapping, version string, and DOI family.
- Per-page owl header on generated PDFs (badge + state token in the running header) so the state identity is recoverable on every printed page, not just the title page.
- Embedded PDF metadata (Title, Author, Subject, Keywords, Producer/Creator) on every generated PDF.
- Citations for external scientific claims in the system spec and the explanation doc: RFC 2119/8174 (normative-keyword discipline), Klein four-group / O(2), Bertin / Peirce / Moody (semiotics and visual notation), WCAG 2.2 SC 1.4.1 + Section 508 §302.3 + PMC 12385717 (CVD prevalence and accessibility), ICD 203 (analytic tradecraft), seL4 (formal verification scope discipline).
- Cayley table for V₄ in `OWL-SEMAPHORE-SYSTEM.md` §2.3 — making the group structure verifiable rather than asserted.
- Accessibility rule **(normative)**: state identity must be triple-redundant through color **+ orientation + textual label/context**. Color cannot be the only carrier. Applies in particular to the CRITICAL (red-on-red) state and is restated for each state spec.
- DNS Tool bridge links from README and from the explanation doc to the Owl Semaphore, confidence, corpus, and publications pages.
- Concept-DOI badge / explicit `TBD_BY_ZENODO_ON_RELEASE` placeholder for the v1.3.0 version DOI in README, CITATION.cff, and `.zenodo.json`.

### Changed

- **METACOGNITIVE wording reconciled.** The earlier interpretive line *"This audits the standard"* is deprecated. The v1.3.0-rc canonical phrasing is **"The observer audits the frame"** (normative voice) and **"Thinking examines its own frame"** (explanatory voice). The σₕ assignment, V₄ algebra, and asset rules are unchanged. The change is in §1, §3, §4.2, §15 of `OWL-4-METACOGNITIVE.md`, §4.2 and §11 of `OWL-SEMAPHORE-SYSTEM.md`, the README state table, and the four-state ledger printed on every PDF.
- **Canonical formal sentence reconciled.** Two earlier forms existed: *"implemented as a reproducible visual system with enforced invariants"* (former README masthead) and *"mapped into a visual system with strict invariants"* (former §11 of the system spec). They are unified to *"implemented as a reproducible visual notation system with enforced invariants."* The word **notation** is the substantive addition; it tracks the DNS Tool description of the system as a "visual epistemic notation system" and the cognitive-science distinction between a notation and arbitrary artwork.
- **Version drift fixed.** All four state specs (`OWL-1` through `OWL-4`) previously labeled themselves "Version 1.0 Draft" while the package metadata said v1.2.0. Each state spec is now stamped as a v1.3.0-rc release-candidate subordinate document. The system spec is stamped v1.3.0-rc directly.
- **O(2) language softened** in §2 of the system spec and §2 of OWL-1-NORMATIVE: the four transforms form a *finite subgroup of O(2) isomorphic to V₄ (equivalently the dihedral group D₂)*, not O(2) itself.
- `generate_pdfs.py` extended: per-page header, embedded PDF metadata, citation footer, v1.3.0-rc version string in footer and ledger, METACOGNITIVE ledger quote updated.
- `INTEGRITY-MANIFEST.md` populated: `TO_BE_COMPUTED` placeholders for tracked specification files replaced with actual SHA-3-512 hashes computed from the current branch; integrity records now also cover the generated PDFs and the new explanation document and CHANGELOG.
- `RELEASE-HASHES.txt` extended to include SHA-3-512 hashes for the generated PDFs in addition to the 540 px release assets.
- `CITATION.cff` and `.zenodo.json` carry an unreleased-version banner pointing at `TBD_BY_ZENODO_ON_RELEASE` for v1.3.0, with the currently published v1.2.0 DOI retained for citation continuity.

### Removed / Deprecated

- The interpretive sentence *"This audits the standard"* is removed from normative contexts (system spec, METACOGNITIVE spec, PDF four-state ledger). It is referenced only as a deprecated alias in `OWL-4-METACOGNITIVE.md` §15.3 and in this changelog.
- The `TO_BE_COMPUTED` placeholders in `INTEGRITY-MANIFEST.md` §11.1 for tracked specification files are removed; asset records under §11.2 retain `TO_BE_VERIFIED` / `TO_BE_COMPUTED` markers where asset measurement is still pending in this release candidate.

### Non-goals (explicit, v1.3.0-rc)

- V₄ algebra: unchanged.
- σₕ ↔ METACOGNITIVE assignment: unchanged.
- License (CC BY 4.0): unchanged.
- Visual identity / state assignments / transform assignments: unchanged.
- No Zenodo upload, no `git tag`, no PR merge for v1.3.0 from this branch.

---

## [v1.2.0] — published on Zenodo

**Canonical formal sentence (this release, README masthead):**
> *A finite algebra over epistemic states, implemented as a reproducible visual system with enforced invariants.*

**Canonical formal sentence (this release, system-spec §11 — note the drift relative to the masthead):**
> *A finite algebra over epistemic states, mapped into a visual system with strict invariants.*

**Version DOI:** [10.5281/zenodo.19474599](https://doi.org/10.5281/zenodo.19474599)
**Concept DOI:** [10.5281/zenodo.19473697](https://doi.org/10.5281/zenodo.19473697)
**Date:** 2026-04-07.

### Notes

- v1.2.0 carried two slightly different canonical sentences in two different files; v1.3.0-rc reconciles them.
- The METACOGNITIVE interpretive line in v1.2.0 was *"This audits the standard,"* which v1.3.0-rc deprecates.
- Generated PDFs were committed but were not produced from a single-command reproducible pipeline.
- Specification documents in `OWL-1` through `OWL-4` carried "Version 1.0 Draft" labels even though the package was v1.2.0.

---

## [v1.0.0] — original publication

**Canonical formal sentence (this release):**
> *A finite algebra over epistemic states, mapped into a visual system with strict invariants.*

### Notes

- Initial four-state V₄ release with NORMATIVE, NON-NORMATIVE, CRITICAL, METACOGNITIVE states and CC BY 4.0 licensing. (Historical record reconstructed from in-repo specifications.)
