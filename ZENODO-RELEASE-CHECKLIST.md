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

- [ ] Zenodo account connected to GitHub
- [ ] repository enabled in Zenodo
- [ ] GitHub release created
- [ ] Zenodo ingestion confirmed
- [ ] concept DOI recorded
- [ ] version DOI recorded
- [ ] DOI added back into:
  - [ ] `README.md`
  - [ ] `CITATION.cff`
  - [ ] release notes

## 8. Post-Release

- [ ] archive exact release assets
- [ ] verify DOI landing page
- [ ] verify metadata rendering
- [ ] update DNS Tool references to cite Owl Semaphore
- [ ] update any other published docs that reference the Owl system