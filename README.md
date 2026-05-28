![Owl Semaphore Master Proof](assets/proofs/OWL-SEMAPHORE-MASTER-PROOF.png)

# OWL SEMAPHORE — SYSTEM SPECIFICATION
A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants.

## Version 2.0.2

> **Version notice.** v2.0.2 is an editorial science/citation remediation release on top of v2.0.1. It restricts the Gödel reference to a structural analogy; qualifies clinical language (ego-dystonic, aporia); reframes Newton/Einstein as a limiting-case relation; aligns the metacognition / ICD 203 framing as a functional parallel; adopts canonical RFC 2119 / RFC 8174 / BCP 14 boilerplate; names Bertin's six retinal variables explicitly; qualifies CVD prevalence as Northern-European descent; removes any metaphysical overclaim from the core framing; and preserves the EXPLANATION story-table overflow fix from v2.0.1. **It does not change the V₄ algebra, the σₕ assignment for METACOGNITIVE, the canonical formal sentence, the accessibility rule, the asset set, or the canonical math tuples.** The archived source snapshot cites the stable concept DOI [10.5281/zenodo.19473697](https://doi.org/10.5281/zenodo.19473697), which resolves to the latest published version; the v2.0.2 version-specific DOI is minted by Zenodo on release and recorded in the GitHub release notes.

[![Concept DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19473697.svg)](https://doi.org/10.5281/zenodo.19473697)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

- **Citing DOI for v2.0.2 (concept, all versions):** [10.5281/zenodo.19473697](https://doi.org/10.5281/zenodo.19473697) — resolves to the latest published version
- **Previous version DOI (v2.0.1):** [10.5281/zenodo.20419874](https://doi.org/10.5281/zenodo.20419874)
- **Earlier version DOI (v2.0.0):** [10.5281/zenodo.20418539](https://doi.org/10.5281/zenodo.20418539)
- **Earlier version DOI (v1.2.0):** [10.5281/zenodo.19474599](https://doi.org/10.5281/zenodo.19474599)
- **v2.0.2 version-specific DOI:** minted by Zenodo on release; recorded in the GitHub release notes
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## Canonical Sentence Stack (v2.0.2)

| Layer | Sentence | Use |
| --- | --- | --- |
| Formal | *A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants.* | README, system spec, citation abstract |
| Operational | *A four-state visual system for marking how a claim, document, dataset, or finding should be evaluated before belief, challenge, or action.* | Explanation doc, public overview |
| Human | *Four owls tell the reader what kind of thinking they are looking at: standard, exploration, inversion, or self-audit.* | Story sections, teaching material |

See [`CHANGELOG.md`](CHANGELOG.md) for the per-version canonical sentence history.

## The Four States (v2.0.2)

| State | Operator | Determinant | Quote (normative) | Standards register |
| --- | --- | --- | --- | --- |
| NORMATIVE | I | +1 | *"This is the standard."* | RFC 2119 MUST / SHALL |
| NON-NORMATIVE | σᵥ | −1 | *"This reflects the standard."* | Informative / Advisory (NOTE) |
| CRITICAL | C₂ | +1 | *"This inverts the standard."* | RFC 2119 MUST NOT / SHALL NOT |
| METACOGNITIVE | σₕ | −1 | **"The observer audits the frame."** | Epistemic / Framework (META) |

The METACOGNITIVE phrasing was refined in v2.0.0 and is unchanged through v2.0.2. The earlier line *"This audits the standard"* is deprecated because it failed to express *thinking examining its own frame*. See [`OWL-4-METACOGNITIVE.md`](OWL-4-METACOGNITIVE.md) §1 and [`OWL-SEMAPHORE-EXPLANATION.md`](OWL-SEMAPHORE-EXPLANATION.md) for the warmer explanatory variant *"Thinking examines its own frame."*

## Accessibility — Color Is Not the Only Carrier

Every state's identity is recoverable from three redundant channels: **color + orientation + textual label/context**. This is the project's mitigation for color vision deficiency (~8% of males, ~0.5% of females of Northern-European descent) and grayscale rendering, in line with [WCAG 2.2 SC 1.4.1 (Use of Color)](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html). The CRITICAL state's intentionally low red-on-red contrast is the most acute test of the rule; red alone never carries CRITICAL identity. See [`OWL-SEMAPHORE-SYSTEM.md`](OWL-SEMAPHORE-SYSTEM.md) §7.2.

## Citation

If you use the Owl Semaphore Badge System, please cite the concept DOI (which resolves to the latest published version):

> Balboa, Carey James. *Owl Semaphore Badge System* (v2.0.2). Zenodo. https://doi.org/10.5281/zenodo.19473697
>
> Previously published versions:
>
> - Balboa, Carey James. *Owl Semaphore Badge System* (v2.0.1). Zenodo. https://doi.org/10.5281/zenodo.20419874
> - Balboa, Carey James. *Owl Semaphore Badge System* (v2.0.0). Zenodo. https://doi.org/10.5281/zenodo.20418539

The v2.0.2 version-specific DOI is minted by Zenodo on release and recorded in the GitHub release notes. The concept DOI [10.5281/zenodo.19473697](https://doi.org/10.5281/zenodo.19473697) is the recommended citing DOI for v2.0.2 and resolves to the latest version. Machine-readable citation metadata is in [`CITATION.cff`](CITATION.cff).

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
├── OWL-SEMAPHORE-EXPLANATION.md       (added in v2.0.0)
├── OWL-1-NORMATIVE.md
├── OWL-2-NON-NORMATIVE.md
├── OWL-3-CRITICAL.md
├── OWL-4-METACOGNITIVE.md
├── INTEGRITY-MANIFEST.md
├── RELEASE-HASHES.txt
├── CITATION.cff
├── .zenodo.json
├── Makefile                            (added in v2.0.0)
├── generate_pdfs.py
├── tests/
│   └── test_banner_tuple.py            (added in v2.0.0)
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
  "version": "2.0.2",
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "codeRepository": "https://github.com/IT-Help-San-Diego/owl-semaphore",
  "datePublished": "2026-04-07",
  "dateModified": "2026-05-28",
  "identifier": [
    "https://doi.org/10.5281/zenodo.19473697",
    "https://doi.org/10.5281/zenodo.20419874",
    "https://doi.org/10.5281/zenodo.20418539",
    "https://doi.org/10.5281/zenodo.19474599"
  ],
  "sameAs": "https://doi.org/10.5281/zenodo.19473697",
  "programmingLanguage": "Not applicable",
  "author": {
    "@type": "Person",
    "name": "Carey James Balboa",
    "identifier": "https://orcid.org/0009-0000-5237-9065"
  },
  "description": "A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants. Four-state classification (NORMATIVE, NON-NORMATIVE, CRITICAL, METACOGNITIVE) for DNS Tool documentation and related research artifacts. v2.0.2 is an editorial science/citation remediation release on top of v2.0.1. The source snapshot cites the concept DOI 10.5281/zenodo.19473697 (resolves to the latest published version); the v2.0.2 version-specific DOI is minted by Zenodo on release and recorded in the GitHub release notes. Previous published version DOI (v2.0.1): 10.5281/zenodo.20419874.",
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
  "releaseNotes": "v2.0.2 — editorial science/citation remediation release on top of v2.0.1. Restricts the Gödel reference to a structural analogy; qualifies clinical language (ego-dystonic, aporia); reframes Newton/Einstein as a limiting-case relation; aligns the metacognition / ICD 203 framing as a functional parallel; adopts canonical RFC 2119 / RFC 8174 / BCP 14 boilerplate; names Bertin's six retinal variables explicitly; qualifies CVD prevalence as Northern-European descent; removes metaphysical overclaim from the core framing; preserves the EXPLANATION story-table overflow fix from v2.0.1. V4 algebra, σh assignment to METACOGNITIVE, canonical formal sentence, accessibility rule, asset set, and canonical math tuples are unchanged from v2.0.1.",
  "isAccessibleForFree": true
}
</script>
