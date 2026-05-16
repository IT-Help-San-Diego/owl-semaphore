# Changelog

All notable changes to the Owl Semaphore Badge System are recorded here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Each release records the **canonical formal sentence** in effect for that version. Drift between the canonical sentence and the README, system specification, citation metadata, and generated PDFs is a release blocker.

---

## [1.3.0-rc] — 2026-05-16 — Release candidate (unpublished)

**Canonical sentence (Formal):**
> A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants.

**Canonical sentence (Operational):**
> A four-state visual system for marking how a claim, document, dataset, or finding should be evaluated before belief, challenge, or action.

**Canonical sentence (Human):**
> Four owls tell the reader what kind of thinking they are looking at: standard, exploration, inversion, or self-audit.

**Status:** release candidate. Not published to Zenodo. No release tag created. New version DOI to be minted by Zenodo when this candidate is published; until then the placeholder `TBD_BY_ZENODO_ON_RELEASE` stands in the metadata.

### Added

- `OWL-SEMAPHORE-EXPLANATION.md` — origin story (DNS Tool's attempt to honor multiple expert cultures), archetype rationale (hackers, OSINT/intelligence analysts, DNS engineers, RFC/standards readers, data scientists, serious operators, public readers), why two states (normative / non-normative) were not enough, why four states map to V₄, and why the owl.
- `CHANGELOG.md` (this file).
- `Makefile` with a single `make pdfs` target that regenerates every PDF deterministically from Markdown sources.
- `scripts/build_pdfs.sh` thin wrapper invoking `generate_pdfs.py`.
- `scripts/verify_banner_tuple.py` — banner-tuple test extracting `(state, transform, determinant, mapping, version, DOI)` from the first page of every generated PDF and asserting expected values per state.
- `scripts/check_pdf_metadata.py` — verifies that each generated PDF carries the expected title, author, subject, and keyword metadata.
- `scripts/compute_hashes.py` — recomputes SHA-3-512 hashes for `RELEASE-HASHES.txt` and the integrity manifest.
- `tests/test_banner_tuple.py` — pytest wrapper around `verify_banner_tuple.py` plus a canonical-wording consistency test.
- Per-page running owl headers on every generated PDF (small badge + state label) — previously only the title page carried a badge.
- PDF document-info metadata (title, author, keywords, subject) is now set explicitly by Typst.
- Citations section in `OWL-SEMAPHORE-SYSTEM.md` covering RFC 2119/8174, ISO/IEC Directives Part 2, V₄, O(2), Bertin, Moody, WCAG 2.2, Section 508, CVD prevalence, ICD 203, seL4.
- Explicit Cayley table in `OWL-SEMAPHORE-SYSTEM.md` §2.3 establishing all four group axioms before claiming \(V_4\) structure.
- RFC 2119 / BCP 14 boilerplate (informative section) clarifying that uppercase keywords apply only where they appear in ALL CAPS and only for interoperability requirements.

### Changed

- Canonical formal sentence reconciled across `README.md`, `OWL-SEMAPHORE-SYSTEM.md`, JSON-LD block, and PDF footers. The earlier variant *"…mapped into a visual system with strict invariants"* (Core Principle) and the masthead *"…implemented as a reproducible visual system with enforced invariants"* are superseded by the single canonical form above.
- Group-theory claims softened from "is a finite subgroup of \(O(2)\)" to "form a finite subgroup of \(O(2)\) isomorphic to \(V_4\) (equivalently \(D_2\))" — \(V_4\) is a proper subgroup of \(O(2)\), not \(O(2)\) itself.
- All four state specifications (`OWL-1-NORMATIVE.md`, `OWL-2-NON-NORMATIVE.md`, `OWL-3-CRITICAL.md`, `OWL-4-METACOGNITIVE.md`) and `OWL-SEMAPHORE-SYSTEM.md` updated from stale `Version 1.0 Draft` / `Version 1.0` stamps to `Version 1.3.0-rc` and given an explicit DOI block (concept DOI, last-published version DOI, TBD next version DOI).
- `CITATION.cff` and `.zenodo.json` updated to `v1.3.0-rc` and to reference the new canonical formal description. The version DOI fields point to the **last-published** v1.2.0 DOI until Zenodo mints a new one.
- README JSON-LD `version` → `1.3.0-rc`, `description` → canonical formal sentence, `sameAs` → concept DOI (stable across versions).
- `generate_pdfs.py` now emits per-page owl headers, sets PDF document-info metadata, references `v1.3.0-rc` in the footer, and additionally generates the new explanation PDF.

### Fixed

- README, system spec, state specs, JSON-LD, and PDF footers no longer disagree on the canonical sentence.
- `Version 1.0` / `Version 1.0 Draft` masthead stamps on the four state-spec documents and `OWL-SEMAPHORE-SYSTEM.md` no longer contradict the v1.2.0 / v1.3.0 release metadata.
- `INTEGRITY-MANIFEST.md` `TO_BE_COMPUTED` hash placeholders for the markdown specifications, README, CITATION.cff, .zenodo.json, CHANGELOG.md, EXPLANATION.md, and generated PDFs are replaced with computed SHA-3-512 values (refreshed by `scripts/compute_hashes.py`).
- `RELEASE-HASHES.txt` extended to cover all v1.3.0-rc release-relevant files, not only the 540 px PNG composites.

### Non-goals (unchanged)

- The \(V_4\) algebra, state assignments, transform assignments, determinants, color assignments, and canonical geometry are unchanged.
- The license remains CC BY 4.0.
- This release candidate is **not** published to Zenodo and does **not** create a release tag.

---

## [1.2.0] — 2026-04-07 — Last published Zenodo release

**Canonical sentence (in effect at the time of that release):**
> A finite algebra over epistemic states, implemented as a reproducible visual system with enforced invariants.

(That sentence is retained verbatim here for provenance. v1.3.0-rc replaces "visual system" with "visual notation system"; see the v1.3.0-rc entry above.)

### Published artefacts

- Concept DOI: `10.5281/zenodo.19473697`
- Version DOI (v1.2.0): `10.5281/zenodo.19474599`
- License: CC BY 4.0
- Bundle: `IT-Help-San-Diego/owl-semaphore-v1.2.0.zip` on Zenodo
- 540 px composite PNGs (NORM, NONNORM, CRIT, META) with SHA-3-512 hashes recorded in `RELEASE-HASHES.txt`.

### Known drift addressed in v1.3.0-rc

- Two different canonical sentence variants present in the repository (masthead vs. Core Principle).
- Four state specification documents still labelled `Version 1.0 Draft`.
- `OWL-SEMAPHORE-SYSTEM.md` still labelled `Version 1.0`.
- `INTEGRITY-MANIFEST.md` entries marked `sha3_512: TO_BE_COMPUTED`.
- No `CHANGELOG.md`.
- No explanation document.
- No per-page owl headers in generated PDFs.
- No single-command PDF regeneration target.

---

## [1.0.0] — Initial concept release

**Canonical sentence (in effect at the time of that release):**
> The Owl Semaphore is a four-standard publication-grade badge system for classifying DNS Tool documentation into normative, non-normative, critical, and metacognitive material.

(Recorded here for provenance. Subsequent releases moved the project from "badge system" framing to "finite algebra / visual notation system" framing; see v1.2.0 and v1.3.0-rc.)
