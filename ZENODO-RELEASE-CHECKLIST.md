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

> **DOI gate for v3.0.1 (reserved — publish steps remain).** The v3.0.1 version-specific DOI **`10.5281/zenodo.21524422`** was reserved on a Zenodo new-version draft of the concept record via `owl-press zenodo new-version` (draft `https://zenodo.org/deposit/21524422`) and embedded as the citing DOI everywhere — `generate_pdfs.py` (as of v3.0.1 a thin driver over the `owl-semaphore-press` package), the regenerated PDFs, `tests/test_banner_tuple.py`, and all metadata. After the release-prep PR merges and the `v3.0.1` tag is pushed, the released files are uploaded into that same draft (`owl-press zenodo upload 21524422 <files> --fresh` — the `--fresh` flag clears file inheritance from the v3.0.0 record) and the draft is published (`owl-press zenodo publish 21524422 --yes`), so the reserved DOI is the canonical and only Zenodo record for v3.0.1. See `RELEASE-PROCESS.md` §1 and §4.

> **DOI gate for v3.0.0 (complete — record published).** The v3.0.0 version-specific DOI **`10.5281/zenodo.20468727`** was reserved on a Zenodo new-version draft of the concept record and embedded as the citing DOI everywhere — `generate_pdfs.py`, the regenerated PDFs, `tests/test_banner_tuple.py`, and all metadata. The released files were uploaded to that draft and the record was **published on 2026-05-31**; the DOI resolves to the live v3.0.0 record. The concept DOI `10.5281/zenodo.19473697` (all-versions; resolves to the latest published version) is preserved as the durable cross-version citation target. Final release PDFs carry the v3.0.0 DOI — never a transient marker. See `RELEASE-PROCESS.md` §0 and §4.

- [x] Zenodo account connected to GitHub
- [x] repository enabled in Zenodo (and temporarily disabled before the GitHub Release for this release, then re-enabled afterwards, per `RELEASE-PROCESS.md` §4)
- [x] concept DOI recorded (all-versions DOI for cross-version citation): `10.5281/zenodo.19473697`
- [x] previously published version DOI recorded (v2.0.2): `10.5281/zenodo.20433053`
- [x] earlier published version DOI recorded (v2.0.1): `10.5281/zenodo.20419874`
- [x] earlier published version DOI recorded (v2.0.0): `10.5281/zenodo.20418539`
- [x] earlier published version DOI recorded (v1.2.0): `10.5281/zenodo.19474599`
- [x] v3.0.0 version-specific DOI reserved on Zenodo new-version draft: `10.5281/zenodo.20468727` (draft `https://zenodo.org/uploads/20468727`)
- [x] Reserved v3.0.0 DOI swapped into `generate_pdfs.py` + `tests/test_banner_tuple.py`, then `make pdfs hashes manifest test` re-run once
- [x] v3.0.0 version-specific DOI `10.5281/zenodo.20468727` embedded as the citing DOI in source/PDFs/metadata:
  - [x] `README.md`
  - [x] `CITATION.cff`
  - [x] `.zenodo.json`
  - [x] `CHANGELOG.md`
  - [x] `OWL-SEMAPHORE-EXPLANATION.md`
  - [x] `INTEGRITY-MANIFEST.md`
  - [x] `generate_pdfs.py` and regenerated PDF page-one banner tuples
  - [x] `tests/test_banner_tuple.py`
- [x] Files matching the merge commit uploaded to the Zenodo new-version record that holds the reserved DOI `10.5281/zenodo.20468727` (human step; see `RELEASE-PROCESS.md` §4)
- [x] Zenodo new-version record published from the Zenodo UI (human step) — published 2026-05-31
- [x] Zenodo "Versions" tab confirms exactly one v3.0.0 record with DOI `10.5281/zenodo.20468727` (verified via the Zenodo API, 2026-07-23)

## 8. Post-Release

- [ ] archive exact release assets
- [ ] verify DOI landing page
- [ ] verify metadata rendering
- [ ] update DNS Tool references to cite Owl Semaphore
- [ ] update any other published docs that reference the Owl system
