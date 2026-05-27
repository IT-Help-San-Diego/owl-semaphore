# Changelog — Owl Semaphore Badge System

All notable changes to this project are documented in this file.

The format roughly follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project's versioning aligns with semantic-versioning intent for a specification (MAJOR = algebra change; MINOR = additive content/metadata; PATCH = errata).

Each release entry records the **canonical formal sentence used in that release** so the conceptual evolution of the system is auditable.

---

## [v2.0.1] — corrective patch release (Zenodo DOI pending; no tag in this PR)

> v2.0.1 is a corrective patch release on top of v2.0.0. It fixes a story-table overflow in `OWL-SEMAPHORE-EXPLANATION.pdf` (PR #9) and stamps PDFs, source metadata, and tests as v2.0.1. The V₄ algebra, the σₕ assignment to METACOGNITIVE, the canonical formal sentence, the accessibility rule, and the asset set are unchanged from v2.0.0.

**Canonical formal sentence (this release, unchanged from v2.0.0):**
> *A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants.*

**Canonical operational sentence (unchanged):** *A four-state visual system for marking how a claim, document, dataset, or finding should be evaluated before belief, challenge, or action.*

**Canonical human sentence (unchanged):** *Four owls tell the reader what kind of thinking they are looking at: standard, exploration, inversion, or self-audit.*

**Version DOI:** `TBD_BY_ZENODO_ON_V2_0_1_RELEASE` — to be minted by Zenodo on release.
**Concept DOI:** [10.5281/zenodo.19473697](https://doi.org/10.5281/zenodo.19473697)
**Previously published v2.0.0 version DOI:** [10.5281/zenodo.20418539](https://doi.org/10.5281/zenodo.20418539)
**Earlier published v1.2.0 version DOI:** [10.5281/zenodo.19474599](https://doi.org/10.5281/zenodo.19474599) (retained for citation continuity)

### Fixed

- Story-table overflow in `OWL-SEMAPHORE-EXPLANATION.pdf` (merged as PR #9, commit `e77ba40`). The four front-loaded narrative stories now render within the page box without horizontal/vertical overflow.

### Changed

- Version stamps updated from `v2.0.0` to `v2.0.1` in `generate_pdfs.py` (`VERSION`, `RELEASE_LABEL`, `pdf_subject` strings, citation header, ledger footer, page-one banner-tuple `VERSION=` field), `tests/test_banner_tuple.py` (`VERSION`, `VERSION_DOI` placeholder), `README.md` (masthead, sentence stack heading, four-states heading, citation, JSON-LD block), `CITATION.cff`, `.zenodo.json`, `OWL-SEMAPHORE-EXPLANATION.md` masthead, `ZENODO-RELEASE-CHECKLIST.md`, and `INTEGRITY-MANIFEST.md`.
- DOI family roles in metadata:
  - Concept DOI `10.5281/zenodo.19473697` — unchanged.
  - **v2.0.0 DOI `10.5281/zenodo.20418539`** — now recorded as the *previous published* version DOI (was the *current* version DOI in v2.0.0 metadata).
  - **v1.2.0 DOI `10.5281/zenodo.19474599`** — retained as an *earlier published* version DOI for citation continuity (was the *previous* in v2.0.0 metadata).
  - **v2.0.1 DOI** — placeholder `TBD_BY_ZENODO_ON_V2_0_1_RELEASE` (will be minted by Zenodo on release).
- Regenerated all six PDFs via `make pdfs`; refreshed `RELEASE-HASHES.txt` and the generated section of `INTEGRITY-MANIFEST.md` via `make hashes && make manifest`.

### Non-goals (explicit, v2.0.1)

- V₄ algebra: unchanged.
- σₕ ↔ METACOGNITIVE assignment: unchanged.
- License (CC BY 4.0): unchanged.
- Visual identity / state assignments / transform assignments: unchanged.
- Canonical formal/operational/human sentences: unchanged.
- Accessibility rule: unchanged.
- Asset set under `assets/`: unchanged.
- This PR does not perform the Zenodo upload, `git tag`, or GitHub release for v2.0.1; those steps happen separately. The v2.0.0 tag, the v2.0.0 GitHub Release, and the minted v2.0.0 DOI are not modified.

---

## [v2.0.0] — final label (Zenodo DOI placeholder; no tag in this PR)

> Internally, work on this entry began under the label `v1.3.0-rc`. That label was superseded by the final `v2.0.0` identity prior to publication; all visible labels in PDFs, README, citation metadata, and the generated manifest now read `v2.0.0`. Historical references to `v1.3.0-rc` are preserved only in the CHANGELOG narrative below where they are part of the audit trail.

**Canonical formal sentence (this release):**
> *A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants.*

**Canonical operational sentence:** *A four-state visual system for marking how a claim, document, dataset, or finding should be evaluated before belief, challenge, or action.*

**Canonical human sentence:** *Four owls tell the reader what kind of thinking they are looking at: standard, exploration, inversion, or self-audit.*

**Version DOI:** [10.5281/zenodo.20418539](https://doi.org/10.5281/zenodo.20418539) — minted by Zenodo on release from immutable tag/main SHA `a8c147783827c40dd063b5249557eb6ffbea8a4d`.
**Concept DOI:** [10.5281/zenodo.19473697](https://doi.org/10.5281/zenodo.19473697)

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
- Concept-DOI badge and minted v2.0.0 version DOI (`10.5281/zenodo.20418539`) in README, CITATION.cff, and `.zenodo.json`.

### Changed

- **METACOGNITIVE wording reconciled.** The earlier interpretive line *"This audits the standard"* is deprecated. The v2.0.0 canonical phrasing is **"The observer audits the frame"** (normative voice) and **"Thinking examines its own frame"** (explanatory voice). The σₕ assignment, V₄ algebra, and asset rules are unchanged. The change is in §1, §3, §4.2, §15 of `OWL-4-METACOGNITIVE.md`, §4.2 and §11 of `OWL-SEMAPHORE-SYSTEM.md`, the README state table, and the four-state ledger printed on every PDF.
- **Canonical formal sentence reconciled.** Two earlier forms existed: *"implemented as a reproducible visual system with enforced invariants"* (former README masthead) and *"mapped into a visual system with strict invariants"* (former §11 of the system spec). They are unified to *"implemented as a reproducible visual notation system with enforced invariants."* The word **notation** is the substantive addition; it tracks the DNS Tool description of the system as a "visual epistemic notation system" and the cognitive-science distinction between a notation and arbitrary artwork.
- **Version drift fixed.** All four state specs (`OWL-1` through `OWL-4`) previously labeled themselves "Version 1.0 Draft" while the package metadata said v1.2.0. Each state spec is now stamped as a v2.0.0 subordinate document. The system spec is stamped v2.0.0 directly.
- **O(2) language softened** in §2 of the system spec and §2 of OWL-1-NORMATIVE: the four transforms form a *finite subgroup of O(2) isomorphic to V₄ (equivalently the dihedral group D₂)*, not O(2) itself.
- `generate_pdfs.py` extended: per-page header, embedded PDF metadata, citation footer, v2.0.0 version string in footer and ledger, METACOGNITIVE ledger quote updated.
- `INTEGRITY-MANIFEST.md` populated: `TO_BE_COMPUTED` placeholders for tracked specification files replaced with actual SHA-3-512 hashes computed from the current branch; integrity records now also cover the generated PDFs and the new explanation document and CHANGELOG.
- `RELEASE-HASHES.txt` extended to include SHA-3-512 hashes for the generated PDFs in addition to the 540 px release assets.
- `CITATION.cff` and `.zenodo.json` carry the minted v2.0.0 version DOI (`10.5281/zenodo.20418539`), with the v1.2.0 DOI retained as the previous-version identifier for citation continuity.

### Removed / Deprecated

- The interpretive sentence *"This audits the standard"* is removed from normative contexts (system spec, METACOGNITIVE spec, PDF four-state ledger). It is referenced only as a deprecated alias in `OWL-4-METACOGNITIVE.md` §15.3 and in this changelog.
- The `TO_BE_COMPUTED` placeholders in `INTEGRITY-MANIFEST.md` §11.1 for tracked specification files are removed; asset records under §11.2 retain `TO_BE_VERIFIED` / `TO_BE_COMPUTED` markers where asset measurement is still pending in this release candidate.

### Non-goals (explicit, v2.0.0)

- V₄ algebra: unchanged.
- σₕ ↔ METACOGNITIVE assignment: unchanged.
- License (CC BY 4.0): unchanged.
- Visual identity / state assignments / transform assignments: unchanged.
- This PR does not perform the Zenodo upload, `git tag`, or GitHub release for v2.0.0; those steps happen separately.

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

- v1.2.0 carried two slightly different canonical sentences in two different files; v2.0.0 reconciles them.
- The METACOGNITIVE interpretive line in v1.2.0 was *"This audits the standard,"* which v2.0.0 deprecates.
- Generated PDFs were committed but were not produced from a single-command reproducible pipeline.
- Specification documents in `OWL-1` through `OWL-4` carried "Version 1.0 Draft" labels even though the package was v1.2.0.

---

## [v1.0.0] — original publication

**Canonical formal sentence (this release):**
> *A finite algebra over epistemic states, mapped into a visual system with strict invariants.*

### Notes

- Initial four-state V₄ release with NORMATIVE, NON-NORMATIVE, CRITICAL, METACOGNITIVE states and CC BY 4.0 licensing. (Historical record reconstructed from in-repo specifications.)
