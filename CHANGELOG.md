# Changelog — Owl Semaphore Badge System

All notable changes to this project are documented in this file.

The format roughly follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project's versioning aligns with semantic-versioning intent for a specification (MAJOR = algebra change; MINOR = additive content/metadata; PATCH = errata).

Each release entry records the **canonical formal sentence used in that release** so the conceptual evolution of the system is auditable.

---

## [Unreleased — v2.0.0-rc] — major release candidate (no Zenodo DOI minted, no tag)

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
  system is not O(2). No 31-degree tilt is reintroduced. No formal-verification claim is added.

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
