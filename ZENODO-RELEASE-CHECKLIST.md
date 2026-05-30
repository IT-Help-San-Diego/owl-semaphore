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

- [ ] Git tag created (example: `v3.0.0`)
- [ ] release title prepared
- [ ] release notes prepared
- [ ] release notes include:
  - [ ] reserved version-specific DOI for this release
  - [ ] concept DOI as the all-versions DOI
  - [ ] previously published version DOIs
  - [ ] four-state V₄ structure summary
  - [ ] relationship to DNS Tool as implementation context

## 7. Zenodo Preparation (canonical convention, v2.0.2 onward)

> **Convention (effective v2.0.2).** The release-specific version DOI is **reserved on Zenodo before the release** by creating a Zenodo new-version record for the concept DOI and capturing the reserved version DOI from that record. The reserved version DOI is then embedded directly into source files, PDFs, and metadata so the exact version DOI appears inside every published artifact. The same Zenodo new-version record is published from the Zenodo UI after the GitHub Release is created, so exactly one Zenodo record per release exists. The GitHub-Zenodo auto-ingest path is intentionally side-stepped for this release to avoid producing a duplicate Zenodo record with a different DOI. The full publication recipe lives in `RELEASE-PROCESS.md`.

> **DOI gate for v3.0.0 (single controlled step).** The v3.0.0 source snapshot does **not** invent a version DOI. The **concept DOI `10.5281/zenodo.19473697`** (all-versions; resolves to the latest published version) is the citing DOI embedded everywhere until the v3.0.0 version DOI is reserved. The reserve-and-swap is one controlled step: reserve the v3.0.0 DOI on a Zenodo new-version draft, set `VERSION_DOI` in `generate_pdfs.py` and `tests/test_banner_tuple.py` to the reserved value, then re-run `make pdfs hashes manifest test` once. Final release PDFs must carry a real DOI — the concept DOI before the swap, or the reserved v3.0.0 DOI after it — never a transient marker. See `RELEASE-PROCESS.md` §0.

- [x] Zenodo account connected to GitHub
- [x] repository enabled in Zenodo (and temporarily disabled before the GitHub Release for this release, then re-enabled afterwards, per `RELEASE-PROCESS.md` §4)
- [x] concept DOI recorded (all-versions DOI for cross-version citation): `10.5281/zenodo.19473697`
- [x] previously published version DOI recorded (v2.0.2): `10.5281/zenodo.20433053`
- [x] earlier published version DOI recorded (v2.0.1): `10.5281/zenodo.20419874`
- [x] earlier published version DOI recorded (v2.0.0): `10.5281/zenodo.20418539`
- [x] earlier published version DOI recorded (v1.2.0): `10.5281/zenodo.19474599`
- [x] v3.0.0 source snapshot cites the concept DOI `10.5281/zenodo.19473697` as the citing DOI (no invented version DOI)
- [x] Citing DOI embedded in source/PDFs/metadata:
  - [x] `README.md`
  - [x] `CITATION.cff`
  - [x] `.zenodo.json`
  - [x] `CHANGELOG.md`
  - [x] `OWL-SEMAPHORE-EXPLANATION.md`
  - [x] `INTEGRITY-MANIFEST.md`
  - [x] `generate_pdfs.py` and regenerated PDF page-one banner tuples
  - [x] `tests/test_banner_tuple.py`
- [ ] v3.0.0 version-specific DOI reserved on Zenodo new-version draft (DOI gate — human step; see `RELEASE-PROCESS.md` §0)
- [ ] Reserved v3.0.0 DOI swapped into `generate_pdfs.py` + `tests/test_banner_tuple.py`, then `make pdfs hashes manifest test` re-run once
- [ ] Files matching the merge commit uploaded to the Zenodo new-version record that holds the reserved DOI
- [ ] Zenodo new-version record published from the Zenodo UI
- [ ] Zenodo "Versions" tab confirms exactly one v3.0.0 record with the reserved DOI

## 8. Post-Release

- [ ] archive exact release assets
- [ ] verify DOI landing page
- [ ] verify metadata rendering
- [ ] update DNS Tool references to cite Owl Semaphore
- [ ] update any other published docs that reference the Owl system
