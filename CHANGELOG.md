# Changelog — Owl Semaphore Badge System

All notable changes to this project are documented in this file.

The format roughly follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project's versioning aligns with semantic-versioning intent for a specification (MAJOR = algebra change; MINOR = additive content/metadata; PATCH = errata).

Each release entry records the **canonical formal sentence used in that release** so the conceptual evolution of the system is auditable.

---

<!-- BEGIN v3.0.0 RELEASE BLOCK -->

## [v3.0.0] — structural and scientific remediation release

> v3.0.0 is a **structural and scientific** remediation release on top of v2.0.2 — **not a visual redesign.** **No change** to the V₄ algebra, the four canonical state-operator tuples, the σₕ assignment to METACOGNITIVE, the canonical formal sentence, the accessibility rule, the color/orientation semantics, or the approved asset set (NORMATIVE I/+1/(x,y)→(x,y); NON-NORMATIVE σᵥ/−1/(x,y)→(−x,y); CRITICAL C₂/+1/(x,y)→(−x,−y); METACOGNITIVE σₕ/−1/(x,y)→(x,−y)). The MAJOR version bump reflects the addition of normative justification and limitations sections that materially expand the specification's argument surface, not a break in the algebra.

**Canonical formal sentence (this release, unchanged from v2.0.0):**
> *A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants.*

**Canonical operational sentence (unchanged):** *A four-state visual system for marking how a claim, document, dataset, or finding should be evaluated before belief, challenge, or action.*

**Canonical human sentence (unchanged):** *Four owls tell the reader what kind of thinking they are looking at: standard, exploration, inversion, or self-audit.*

**Citing DOI for the v3.0.0 source snapshot:** [10.5281/zenodo.19473697](https://doi.org/10.5281/zenodo.19473697) — the concept (all-versions) DOI, which resolves to the latest published version. The v3.0.0 version-specific DOI is reserved on Zenodo as a single controlled release step (see `RELEASE-PROCESS.md`); the concept DOI is the citing DOI embedded in source, PDFs, and metadata until that reservation is performed, so no transient DOI markers appear anywhere in the corpus.
**Concept DOI (all versions):** [10.5281/zenodo.19473697](https://doi.org/10.5281/zenodo.19473697) — resolves to the latest published version.
**Previous published version DOI (v2.0.2):** [10.5281/zenodo.20433053](https://doi.org/10.5281/zenodo.20433053)
**Earlier published version DOI (v2.0.1):** [10.5281/zenodo.20419874](https://doi.org/10.5281/zenodo.20419874)
**Earlier published version DOI (v2.0.0):** [10.5281/zenodo.20418539](https://doi.org/10.5281/zenodo.20418539)
**Earlier published version DOI (v1.2.0):** [10.5281/zenodo.19474599](https://doi.org/10.5281/zenodo.19474599)

### Added (normative)

- **Formal Justification for V₄ Structure** — new §4A in `OWL-SEMAPHORE-SYSTEM.md`, placed after the operator and epistemic definitions (§2–§4) and before the application examples (§5). It argues why there are exactly four states (two independent binary distinctions — orientation of stance and locus of audit — closed under composition force the fourth state; three states are not closed; six or eight add redundant generators with no distinct referent); why the Klein four-group rather than the cyclic group C₄ (every state move is its own inverse, g² = I) or a non-abelian group (the two distinctions commute); and why an operator algebra rather than a continuous scale (the frame-audit axis is orthogonal to a confidence dial and a scale has no closure check) or a flat label taxonomy (which asserts rather than checks structure). Includes a comparison table of V₄ against binary, three-label, C₄, D₃/S₃, D₄, continuous-scale, and flat-taxonomy alternatives on parsimony, compositionality, constraint-verifiability, transition-modeling, and empirical-tractability.
- **Limitations and Scope Boundaries** — new §12A in `OWL-SEMAPHORE-SYSTEM.md`, before the Closing Statement: the four states are deliberately coarse (a classifier of stance, not a confidence measure); the epistemic partition has no empirical validation yet (no inter-rater reliability or user study); and the iconography, palette, and orientation conventions are culturally situated and depend on a learned key, with misreading risk highest where a badge is seen without its label.
- **Why Four States: The Exclusion Argument** — new §1C in `OWL-SEMAPHORE-EXPLANATION.md`, after "What the Owl Semaphore is" and the front-loaded stories, before §2: a plain-language companion to System §4A (why not a binary, why not three states — closure forces the fourth, why not six/eight, why not a continuous scale), plus a new §1C.1 use-boundary / ethics subsection (states are epistemic-stance labels not authority labels; NON-NORMATIVE and CRITICAL must not be used to suppress dissent; whoever classifies is accountable and the classification is always contestable).
- **Per-state bridge paragraphs** — each of `OWL-1-NORMATIVE.md`, `OWL-2-NON-NORMATIVE.md`, `OWL-3-CRITICAL.md`, and `OWL-4-METACOGNITIVE.md` now carries a bold **Bridge — from the story to the operator** paragraph immediately after its §1A story, connecting the narrative to the formal operator mapping: NORMATIVE → identity I, operational baseline, domain-bounded not permanently true; NON-NORMATIVE → σᵥ vertical-axis reflection, alternative orientation preserving the vertical reference while reversing lateral stance, legitimate exploration not failure; CRITICAL → C₂ full inversion (both axes), proof turned against the current stance, falsification/show-stopper/crisis with no psychiatric overclaim; METACOGNITIVE → σₕ horizontal reflection, frame/instrument audit, observer changes relation to the evidence, Gödel illustrative only.
- **Per-state limitations notes** — each of the four owl specifications now carries a concise **Limitations and Scope** section near its end, stating the state's specific misuse risks and cross-referencing System §12A and Explanation §1C.1.

### Changed (editorial)

- Version stamps advanced to v3.0.0 across `OWL-SEMAPHORE-SYSTEM.md`, `OWL-SEMAPHORE-EXPLANATION.md`, the four owl specifications, `README.md`, `CITATION.cff`, `.zenodo.json`, `INTEGRITY-MANIFEST.md`, the Makefile, the hash/manifest scripts, and the banner-tuple / forbidden-token tests. The deprecation history of *"This audits the standard"* (deprecated since v2.0.0) is preserved and now reads "carried through v3.0.0."

### DOI strategy (this release)

- The **concept DOI `10.5281/zenodo.19473697`** (all versions; resolves to latest) is the citing DOI embedded in the v3.0.0 source snapshot, PDFs, and metadata. No invented or transient version DOI is used.
- The **v3.0.0 version-specific DOI is reserved on Zenodo as a single controlled release step** documented in `RELEASE-PROCESS.md` and `ZENODO-RELEASE-CHECKLIST.md`. When that reservation is performed, the operator sets `VERSION_DOI` in `generate_pdfs.py` (and the matching constant in `tests/test_banner_tuple.py`) to the reserved value and re-runs `make pdfs hashes manifest test` as one controlled step.
- DOI family roles in metadata as of v3.0.0:
  - Concept DOI `10.5281/zenodo.19473697` — all-versions / citing DOI for the v3.0.0 source snapshot.
  - **v2.0.2 DOI `10.5281/zenodo.20433053`** — recorded as the *previous published* version DOI.
  - **v2.0.1 DOI `10.5281/zenodo.20419874`** — recorded as an *earlier published* version DOI.
  - **v2.0.0 DOI `10.5281/zenodo.20418539`** — recorded as an *earlier published* version DOI.
  - **v1.2.0 DOI `10.5281/zenodo.19474599`** — retained as an *earlier published* version DOI for citation continuity.

### Verification

- `make pdfs` regenerates all six PDFs from the edited sources at the v3.0.0 stamp.
- `make hashes` and `make manifest` re-stamp `RELEASE-HASHES.txt` and `INTEGRITY-MANIFEST.md` for v3.0.0.
- `make test` passes — the four canonical math tuples are unchanged: NORMATIVE I/+1/(x,y)→(x,y); NON-NORMATIVE σᵥ/−1/(x,y)→(−x,y); CRITICAL C₂/+1/(x,y)→(−x,−y); METACOGNITIVE σₕ/−1/(x,y)→(x,−y). The banner-tuple and forbidden-token tests are updated to the v3.0.0 stamp and DOI roles and pass against the v3.0.0 corpus.

### Non-goals (explicit, v3.0.0)

- V₄ algebra: unchanged.
- σₕ ↔ METACOGNITIVE assignment: unchanged.
- License (CC BY 4.0): unchanged.
- Visual identity / state assignments / transform assignments / approved asset set: unchanged.
- Canonical formal / operational / human sentences: unchanged.
- Accessibility rule (triple-redundant encoding): unchanged.
- Canonical math tuples in tests and PDFs: unchanged.
- This PR does not perform the Zenodo upload, `git tag`, or GitHub release for v3.0.0; those steps happen separately. Existing tags, GitHub releases, and minted DOIs for prior versions are not modified.

<!-- END v3.0.0 RELEASE BLOCK -->

---

<!-- BEGIN v2.0.2 RELEASE BLOCK -->

## [v2.0.2] — editorial science/citation remediation release

> v2.0.2 is an editorial science/citation remediation release on top of v2.0.1. **No change** to the V₄ algebra, the σₕ assignment to METACOGNITIVE, the canonical formal sentence, the accessibility rule, the asset set, or the canonical math tuples (NORMATIVE I/+1/(x,y)→(x,y); NON-NORMATIVE σᵥ/−1/(x,y)→(−x,y); CRITICAL C₂/+1/(x,y)→(−x,−y); METACOGNITIVE σₕ/−1/(x,y)→(x,−y)).

**Canonical formal sentence (this release, unchanged from v2.0.0):**
> *A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants.*

**Canonical operational sentence (unchanged):** *A four-state visual system for marking how a claim, document, dataset, or finding should be evaluated before belief, challenge, or action.*

**Canonical human sentence (unchanged):** *Four owls tell the reader what kind of thinking they are looking at: standard, exploration, inversion, or self-audit.*

**Citing DOI for v2.0.2 (version-specific):** [10.5281/zenodo.20433053](https://doi.org/10.5281/zenodo.20433053) — reserved on Zenodo before release and embedded directly in source, PDFs, and metadata so the exact version DOI appears inside every published artifact.
**Concept DOI (all versions):** [10.5281/zenodo.19473697](https://doi.org/10.5281/zenodo.19473697) — resolves to the latest published version.
**Previous published version DOI (v2.0.1):** [10.5281/zenodo.20419874](https://doi.org/10.5281/zenodo.20419874)
**Earlier published version DOI (v2.0.0):** [10.5281/zenodo.20418539](https://doi.org/10.5281/zenodo.20418539)
**Earlier published version DOI (v1.2.0):** [10.5281/zenodo.19474599](https://doi.org/10.5281/zenodo.19474599)

### Changed (editorial; no normative algebra changes)

- **RFC 2119 / RFC 8174 / BCP 14 boilerplate.** Reworded the keyword-use paragraph in `OWL-SEMAPHORE-SYSTEM.md` to use the canonical "when, and only when, they appear in all capitals, as shown here" form citing both RFC 2119 and RFC 8174 / BCP 14. The companion line in `OWL-SEMAPHORE-EXPLANATION.md` was aligned with the same phrasing.
- **V₄ / O(2) / SO(2) distinction.** Existing language already named V₄ as a *finite subgroup of O(2)* (equivalently D₂); the audit confirmed that reflections are included so the subgroup sits in O(2), **not** in the rotation-only SO(2). The text is preserved; no change required.
- **Metacognition and ICD 203.** In `OWL-4-METACOGNITIVE.md` §3.3 and `OWL-SEMAPHORE-EXPLANATION.md` §6, explicitly noted that ICD 203 does **not** use the word *metacognition* but functionally parallels metacognitive self-monitoring by requiring methods that reveal and mitigate the impact of assumptions and cognitive biases. Flavell 1979 (via PMC 11368986) retained as the metacognition reference.
- **Bertin / visual variables.** In `OWL-SEMAPHORE-EXPLANATION.md` §5, replaced "retinal variables" inline with "visual variables" and added an explicit note that Bertin identified **six** retinal variables (size, value, texture, color, orientation, shape) in addition to the two planar position dimensions; motion/dynamics was added by later literature, not by Bertin.
- **CVD prevalence.** Re-verified that all surviving prevalence numbers (~8% male / ~0.5% female) are qualified as **Northern-European descent**, with "rates vary by population." This was already the case in the v2.0.1 corpus; no further changes were required.
- **Aporia.** In `OWL-3-CRITICAL.md` §1A and `OWL-SEMAPHORE-EXPLANATION.md` §8, *aporia* is now qualified as **Platonic / productive-perplexity** and explicitly **not equivalent** to CRITICAL.
- **Through-the-legs / child illustration.** In `OWL-1-NORMATIVE.md` §20, `OWL-4-METACOGNITIVE.md` §5, and `OWL-SEMAPHORE-EXPLANATION.md`, marked the maneuver as a **heuristic illustration of perceptual frame disruption**, not formal psychophysical evidence and not rigorous support for epistemic auditing.
- **Gödel.** In `OWL-4-METACOGNITIVE.md` §1A and `OWL-SEMAPHORE-EXPLANATION.md`, restricted Gödel's incompleteness theorems to a **structural analogy only**, with an explicit statement that they do not ground or prove anything about metacognitive psychology or color ontology and are not offered as validation.
- **Ego-dystonic.** In `OWL-3-CRITICAL.md` §1A and `OWL-SEMAPHORE-EXPLANATION.md`, replaced *ego-dystonic* as the primary label with safer language (**frame-discrepant finding**, **state incongruence**, **dissonant signal**), and where the term is retained, noted that it is a clinical descriptor — not a current formal diagnostic category — and **not equivalent to CRITICAL**.
- **Newton / Einstein.** In `OWL-1-NORMATIVE.md` §1A and `OWL-SEMAPHORE-EXPLANATION.md` §1B, rephrased so general relativity **extends and contains** Newtonian mechanics as a limiting case rather than simply replacing or falsifying it; explicitly defined *normative* as "operationally validated within a stated domain and scope," not "true everywhere."
- **Core framing.** In `OWL-SEMAPHORE-EXPLANATION.md` §1A and `OWL-SEMAPHORE-SYSTEM.md` §1.0, removed the "must align with the human spirit / 2,500 years of accumulated understanding" framing and reframed the project as a visual notation whose design target is **compatibility** with established mathematics, accessibility practice, and carefully bounded analogies from epistemology and cognitive science — not a theory of everything and not a claim over the whole of human knowledge.

### DOI strategy (this release)

- The v2.0.2 version-specific DOI `10.5281/zenodo.20433053` is **reserved on Zenodo before release** and embedded directly into source files, PDFs, and metadata. The exact version DOI therefore appears inside every published artifact that Zenodo archives. No transient DOI markers appear in source, PDFs, or tests; the source snapshot is final on its own terms.
- The **concept DOI `10.5281/zenodo.19473697`** is preserved as the all-versions DOI for cross-version citation; it resolves to the latest published version on Zenodo.
- DOI family roles in metadata as of v2.0.2:
  - **v2.0.2 DOI `10.5281/zenodo.20433053`** — version-specific citing DOI for v2.0.2 (reserved on Zenodo before release; embedded in source and PDFs).
  - Concept DOI `10.5281/zenodo.19473697` — unchanged (resolves to latest version).
  - **v2.0.1 DOI `10.5281/zenodo.20419874`** — recorded as the *previous published* version DOI.
  - **v2.0.0 DOI `10.5281/zenodo.20418539`** — recorded as an *earlier published* version DOI.
  - **v1.2.0 DOI `10.5281/zenodo.19474599`** — retained as an *earlier published* version DOI for citation continuity.
- The repository convention (`RELEASE-PROCESS.md`, `ZENODO-RELEASE-CHECKLIST.md`) documents the reserve-DOI-first workflow: create a Zenodo new-version draft for the concept record, reserve the version DOI, embed it in source/PDFs/metadata, merge the release-prep PR, create the tag and GitHub Release, upload the exact release files to the same Zenodo draft, and publish the draft. The manual workflow does not auto-publish a separate Zenodo record via GitHub auto-ingest, so there is exactly one Zenodo record per release.

### Verification

- `make pdfs` regenerates all six PDFs from the edited sources at the new v2.0.2 stamp.
- `make hashes` and `make manifest` re-stamp `RELEASE-HASHES.txt` and `INTEGRITY-MANIFEST.md` for v2.0.2.
- `make test` passes — the four canonical math tuples are unchanged: NORMATIVE I/+1/(x,y)→(x,y); NON-NORMATIVE σᵥ/−1/(x,y)→(−x,y); CRITICAL C₂/+1/(x,y)→(−x,−y); METACOGNITIVE σₕ/−1/(x,y)→(x,−y).
- A new test (`tests/test_forbidden_tokens.py`) scans canonical release-facing files and generated PDFs for transient cleanup markers and external-link policy violations; it passes for the v2.0.2 corpus.

### Non-goals (explicit, v2.0.2)

- V₄ algebra: unchanged.
- σₕ ↔ METACOGNITIVE assignment: unchanged.
- License (CC BY 4.0): unchanged.
- Visual identity / state assignments / transform assignments: unchanged.
- Canonical formal/operational/human sentences: unchanged.
- Accessibility rule: unchanged.
- Asset set under `assets/`: unchanged.
- Canonical math tuples in tests and PDFs: unchanged.
- This PR does not perform the Zenodo upload, `git tag`, or GitHub release for v2.0.2; those steps happen separately. The v2.0.0 and v2.0.1 tags, their GitHub releases, and their minted DOIs are not modified.

<!-- END v2.0.2 RELEASE BLOCK -->

---

## [v2.0.1] — corrective patch release

> v2.0.1 is a corrective patch release on top of v2.0.0. It fixes a story-table overflow in `OWL-SEMAPHORE-EXPLANATION.pdf` (PR #9) and stamps PDFs, source metadata, and tests as v2.0.1. The V₄ algebra, the σₕ assignment to METACOGNITIVE, the canonical formal sentence, the accessibility rule, and the asset set are unchanged from v2.0.0.

**Canonical formal sentence (this release, unchanged from v2.0.0):**
> *A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants.*

**Canonical operational sentence (unchanged):** *A four-state visual system for marking how a claim, document, dataset, or finding should be evaluated before belief, challenge, or action.*

**Canonical human sentence (unchanged):** *Four owls tell the reader what kind of thinking they are looking at: standard, exploration, inversion, or self-audit.*

**Version DOI:** [10.5281/zenodo.20419874](https://doi.org/10.5281/zenodo.20419874)
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
  - **v2.0.1 DOI `10.5281/zenodo.20419874`** — minted by Zenodo for the v2.0.1 release (back-filled in this PR).
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
