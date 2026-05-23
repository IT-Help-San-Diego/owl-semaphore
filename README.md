![Owl Semaphore Master Proof](assets/proofs/OWL-SEMAPHORE-MASTER-PROOF.png)

# OWL SEMAPHORE — SYSTEM SPECIFICATION
A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants.

## Version 1.3.0-rc (release candidate)

> **Release-candidate notice.** This branch is the v1.3.0 release candidate. It refines explanatory language, fixes version drift, adds an explanation document, repairs the reproducible PDF pipeline, and tightens accessibility wording. **It does not change the V₄ algebra or the σₕ assignment for METACOGNITIVE.** No Zenodo upload, no release tag, and no merge has occurred for v1.3.0. The currently published Zenodo record remains v1.2.0 (DOI [10.5281/zenodo.19474599](https://doi.org/10.5281/zenodo.19474599)). The version DOI for v1.3.0 is `TBD_BY_ZENODO_ON_RELEASE`.

[![Published Version DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19474599.svg)](https://doi.org/10.5281/zenodo.19474599)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

- **Currently published version DOI (v1.2.0):** [10.5281/zenodo.19474599](https://doi.org/10.5281/zenodo.19474599)
- **Concept DOI (all versions):** [10.5281/zenodo.19473697](https://doi.org/10.5281/zenodo.19473697)
- **Release-candidate version DOI (v1.3.0):** `TBD_BY_ZENODO_ON_RELEASE`
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## Canonical Sentence Stack (v1.3.0-rc)

| Layer | Sentence | Use |
| --- | --- | --- |
| Formal | *A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants.* | README, system spec, citation abstract |
| Operational | *A four-state visual system for marking how a claim, document, dataset, or finding should be evaluated before belief, challenge, or action.* | Explanation doc, public overview |
| Human | *Four owls tell the reader what kind of thinking they are looking at: standard, exploration, inversion, or self-audit.* | Story sections, teaching material |

See [`CHANGELOG.md`](CHANGELOG.md) for the per-version canonical sentence history.

## The Four States (v1.3.0-rc)

| State | Operator | Determinant | Quote (normative) | Standards register |
| --- | --- | --- | --- | --- |
| NORMATIVE | I | +1 | *"This is the standard."* | RFC 2119 MUST / SHALL |
| NON-NORMATIVE | σᵥ | −1 | *"This reflects the standard."* | Informative / Advisory (NOTE) |
| CRITICAL | C₂ | +1 | *"This inverts the standard."* | RFC 2119 MUST NOT / SHALL NOT |
| METACOGNITIVE | σₕ | −1 | **"The observer audits the frame."** | Epistemic / Framework (META) |

The METACOGNITIVE phrasing is refined in v1.3.0-rc. The earlier line *"This audits the standard"* is deprecated because it failed to express *thinking examining its own frame*. See [`OWL-4-METACOGNITIVE.md`](OWL-4-METACOGNITIVE.md) §1 and [`OWL-SEMAPHORE-EXPLANATION.md`](OWL-SEMAPHORE-EXPLANATION.md) for the warmer explanatory variant *"Thinking examines its own frame."*

## Accessibility — Color Is Not the Only Carrier

Every state's identity is recoverable from three redundant channels: **color + orientation + textual label/context**. This is the project's mitigation for color vision deficiency (~8% of males, ~0.5% of females of Northern-European descent) and grayscale rendering, in line with [WCAG 2.2 SC 1.4.1 (Use of Color)](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html). The CRITICAL state's intentionally low red-on-red contrast is the most acute test of the rule; red alone never carries CRITICAL identity. See [`OWL-SEMAPHORE-SYSTEM.md`](OWL-SEMAPHORE-SYSTEM.md) §7.2.

## Citation

If you use the Owl Semaphore Badge System, please cite the most recently published version DOI (currently v1.2.0):

> Balboa, Carey James. *Owl Semaphore Badge System* (v1.2.0). Zenodo. https://doi.org/10.5281/zenodo.19474599

After v1.3.0 is published on Zenodo, replace the version DOI with the minted v1.3.0 DOI (currently `TBD_BY_ZENODO_ON_RELEASE`). Machine-readable citation metadata is in [`CITATION.cff`](CITATION.cff).

## Reproducing the PDFs

All five PDFs (system spec + four state specs + explanation) regenerate from the markdown sources with a single command:

```bash
make pdfs
# or, equivalently:
python3 generate_pdfs.py
```

`make pdfs` produces page-one banner-tuple-bearing PDFs with embedded PDF metadata (Title, Author, Subject, Keywords, Producer, Version), a contact-sheet header, a classification ledger back page, and per-page owl headers. The pipeline uses pandoc → Typst (via the `typst` Python package). See [`Makefile`](Makefile) for additional targets:

- `make hashes` — recompute SHA-3-512 hashes for committed PDFs and release assets
- `make manifest` — rewrite `INTEGRITY-MANIFEST.md` integrity records from current hashes
- `make test` — run the banner-tuple integrity test (`tests/test_banner_tuple.py`)
- `make clean` — remove generated `.typ` intermediates

## Repository Layout

```
owl-semaphore/
├── README.md
├── CHANGELOG.md
├── OWL-SEMAPHORE-SYSTEM.md
├── OWL-SEMAPHORE-EXPLANATION.md       (new in v1.3.0-rc)
├── OWL-1-NORMATIVE.md
├── OWL-2-NON-NORMATIVE.md
├── OWL-3-CRITICAL.md
├── OWL-4-METACOGNITIVE.md
├── INTEGRITY-MANIFEST.md
├── RELEASE-HASHES.txt
├── CITATION.cff
├── .zenodo.json
├── Makefile                            (new in v1.3.0-rc)
├── generate_pdfs.py
├── tests/
│   └── test_banner_tuple.py            (new in v1.3.0-rc)
└── assets/
    ├── exports/
    ├── layers/
    ├── masters/
    ├── proofs/
    └── releases/
```

## Related Resources

- DNS Tool Owl Semaphore page: https://dnstool.it-help.tech/owl-semaphore
- DNS Tool confidence framework: https://dnstool.it-help.tech/confidence
- DNS Tool corpus (epistemic classification legend): https://dnstool.it-help.tech/corpus
- DNS Tool publications: https://dnstool.it-help.tech/publications

## Standards

- NORMATIVE (NORM)
- NON-NORMATIVE (NONNORM)
- CRITICAL (CRIT)
- METACOGNITIVE (META)

## Release Location

`assets/releases/540/`

## Current Release Set

```
CRIT-composite-dark-540.png
CRIT-composite-transparent-540.png
CRIT-composite-white-540.png
META-composite-dark-540.png
META-composite-transparent-540.png
META-composite-white-540.png
NONNORM-composite-dark-540.png
NONNORM-composite-transparent-540.png
NONNORM-composite-white-540.png
NORM-composite-dark-540.png
NORM-composite-transparent-540.png
NORM-composite-white-540.png
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareSourceCode",
  "name": "Owl Semaphore Badge System",
  "version": "1.3.0-rc",
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "codeRepository": "https://github.com/IT-Help-San-Diego/owl-semaphore",
  "datePublished": "2026-04-07",
  "dateModified": "2026-05-16",
  "identifier": [
    "https://doi.org/10.5281/zenodo.19474599",
    "https://doi.org/10.5281/zenodo.19473697"
  ],
  "sameAs": "https://doi.org/10.5281/zenodo.19474599",
  "programmingLanguage": "Not applicable",
  "author": {
    "@type": "Person",
    "name": "Carey James Balboa",
    "identifier": "https://orcid.org/0009-0000-5237-9065"
  },
  "description": "A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants. Four-state classification (NORMATIVE, NON-NORMATIVE, CRITICAL, METACOGNITIVE) for DNS Tool documentation and related research artifacts. v1.3.0-rc is a release candidate; the version DOI for v1.3.0 will be minted by Zenodo on release.",
  "keywords": [
    "Owl Semaphore",
    "DNS Tool",
    "visual epistemic notation",
    "Klein four-group",
    "V4",
    "classification system",
    "documentation",
    "epistemology",
    "metacognition",
    "accessibility"
  ],
  "releaseNotes": "v1.3.0-rc — release-candidate refinements: METACOGNITIVE phrasing reconciled to 'The observer audits the frame'; accessibility rule (color is not the only carrier) made normative; OWL-SEMAPHORE-EXPLANATION.md added; CHANGELOG.md added; Makefile-based one-command PDF regeneration with embedded PDF metadata and per-page owl headers; integrity manifest reconciled with computed SHA-3-512 hashes for markdown and generated PDFs; banner-tuple test added. V4 algebra and σh assignment are unchanged.",
  "isAccessibleForFree": true
}
</script>
