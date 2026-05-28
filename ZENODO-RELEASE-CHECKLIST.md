# Owl Semaphore — Zenodo Release Checklist

## 1. Repository Readiness

- [ ] Repository name is `owl-semaphore`
- [ ] Repository is public
- [ ] Root files present:
  - [ ] `OWL-SEMAPHORE-SYSTEM.md`
  - [ ] `OWL-1-NORMATIVE.md`
  - [ ] `OWL-2-NON-NORMATIVE.md`
  - [ ] `OWL-3-CRITICAL.md`
  - [ ] `OWL-4-METACOGNITIVE.md`
  - [ ] `OWL-SEMAPHORE-SYSTEM.pdf`
  - [ ] `OWL-1-NORMATIVE.pdf`
  - [ ] `OWL-2-NON-NORMATIVE.pdf`
  - [ ] `OWL-3-CRITICAL.pdf`
  - [ ] `OWL-4-METACOGNITIVE.pdf`
  - [ ] `INTEGRITY-MANIFEST.md`
  - [ ] `CITATION.cff`
  - [ ] `LICENSE`
  - [ ] `README.md`
- [ ] Asset directories present:
  - [ ] `assets/masters/`
  - [ ] `assets/layers/`
  - [ ] `assets/exports/`

## 2. Content Verification

- [ ] All four owl specifications are complete
- [ ] System specification is complete
- [ ] State vs process distinction is explicit
- [ ] 31° rotation is documented as process, not state
- [ ] Mathematical notation is internally consistent
- [ ] Terminology is consistent across all documents

## 3. Asset Verification

- [ ] NORMATIVE: upright, right-facing
- [ ] NON-NORMATIVE: upright, left-facing
- [ ] CRITICAL: upside down, left-facing
- [ ] METACOGNITIVE: upside down, right-facing
- [ ] Shared geometry preserved across all four
- [ ] Meander layer invariant preserved
- [ ] RGBA alpha integrity verified
- [ ] Hashes generated using SHA-3-512
- [ ] `INTEGRITY-MANIFEST.md` updated

## 4. Citation and Metadata

- [ ] `CITATION.cff` valid
- [ ] author metadata correct
- [ ] repository URL correct
- [ ] version correct
- [ ] release date correct
- [ ] abstract reflects actual scope
- [ ] keywords present

## 5. Licensing

- [ ] license chosen intentionally
- [ ] `LICENSE` file included
- [ ] license language is consistent with intended reuse model

## 6. GitHub Release Preparation

- [ ] Git tag created (example: `v1.0.0`)
- [ ] release title prepared
- [ ] release notes prepared
- [ ] release notes include:
  - [ ] first formal publication of Owl Semaphore
  - [ ] four-state V₄ structure
  - [ ] asset integrity and invariants
  - [ ] relationship to DNS Tool as implementation context

## 7. Zenodo Preparation

> **Convention (effective v2.0.2).** The archived source snapshot for each release cites the **stable concept DOI**, which Zenodo resolves to the latest published version. The version-specific DOI for the *current* release is recorded in the GitHub release notes after Zenodo mints it, and source files, PDFs, and tests are not edited after the release tag. This convention keeps each release's source snapshot final on its own terms and removes any source-side reapplication step. The full publication recipe — including the manual release workflow that creates the tag, publishes the GitHub release, and captures the minted version-specific DOI into the release notes — lives in `RELEASE-PROCESS.md`.

- [x] Zenodo account connected to GitHub
- [x] repository enabled in Zenodo
- [x] GitHub release created
- [x] Zenodo ingestion confirmed
- [x] concept DOI recorded (citing DOI for the source snapshot of every release): `10.5281/zenodo.19473697`
- [x] previous published version DOI recorded (v2.0.1): `10.5281/zenodo.20419874`
- [x] earlier published version DOI recorded (v2.0.0): `10.5281/zenodo.20418539`
- [x] earlier published version DOI recorded (v1.2.0): `10.5281/zenodo.19474599`
- [ ] v2.0.2 version-specific DOI: recorded in the GitHub release notes only after Zenodo mints it. Files that already cite the concept DOI as the source's citing DOI:
  - [x] `README.md`
  - [x] `CITATION.cff`
  - [x] `.zenodo.json`
  - [x] `CHANGELOG.md`
  - [x] `OWL-SEMAPHORE-EXPLANATION.md`
  - [x] `generate_pdfs.py` and regenerated PDF page-one banner tuples
  - [x] `tests/test_banner_tuple.py`

## 8. Post-Release

- [ ] archive exact release assets
- [ ] verify DOI landing page
- [ ] verify metadata rendering
- [ ] update DNS Tool references to cite Owl Semaphore
- [ ] update any other published docs that reference the Owl system