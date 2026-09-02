![Owl Semaphore Master Proof](assets/proofs/OWL-SEMAPHORE-MASTER-PROOF.png)

# OWL SEMAPHORE — SYSTEM SPECIFICATION
A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants.

## Version 3.0.1

> **Version notice.** v3.0.1 is a **PATCH-level errata and toolchain release** on top of v3.0.0. It inserts one clarifying sentence into System §4A.1 defining the locus-of-audit axis's frame pole (one's own frame, audited at METACOGNITIVE, or the framework a claim rests on, inverted at CRITICAL) so the specification and the IRR study instruments define the axis identically, switches PDF generation to the parity-proven [`owl-semaphore-press`](https://github.com/IT-Help-San-Diego/owl-semaphore-press) package, and folds in the repository-side additions and post-publication documentation corrections accumulated since the v3.0.0 tag (see [`CHANGELOG.md`](CHANGELOG.md)). **It does not change the V₄ algebra, the four canonical state-operator tuples, the σₕ assignment for METACOGNITIVE, the canonical formal sentence, the accessibility rule, the color/orientation semantics, or the approved asset set.** The v3.0.1 version-specific DOI [10.5281/zenodo.21524422](https://doi.org/10.5281/zenodo.21524422) is reserved on Zenodo and embedded as the citing DOI throughout the v3.0.1 source, PDFs, and metadata; the concept DOI [10.5281/zenodo.19473697](https://doi.org/10.5281/zenodo.19473697) is the all-versions DOI that resolves to the latest published version.

[![Version DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21524422.svg)](https://doi.org/10.5281/zenodo.21524422)
[![Concept DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19473697.svg)](https://doi.org/10.5281/zenodo.19473697)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

- **Version DOI (v3.0.1):** [10.5281/zenodo.21524422](https://doi.org/10.5281/zenodo.21524422) — the version-specific DOI for this release; the citing DOI embedded in the v3.0.1 source, PDFs, and metadata
- **Concept DOI (all versions):** [10.5281/zenodo.19473697](https://doi.org/10.5281/zenodo.19473697) — resolves to the latest published version
- **Previous version DOI (v3.0.0):** [10.5281/zenodo.20468727](https://doi.org/10.5281/zenodo.20468727)
- **Earlier version DOI (v2.0.2):** [10.5281/zenodo.20433053](https://doi.org/10.5281/zenodo.20433053)
- **Earlier version DOI (v2.0.1):** [10.5281/zenodo.20419874](https://doi.org/10.5281/zenodo.20419874)
- **Earlier version DOI (v2.0.0):** [10.5281/zenodo.20418539](https://doi.org/10.5281/zenodo.20418539)
- **Earlier version DOI (v1.2.0):** [10.5281/zenodo.19474599](https://doi.org/10.5281/zenodo.19474599)
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## Canonical Sentence Stack (v3.0.1)

| Layer | Sentence | Use |
| --- | --- | --- |
| Formal | *A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants.* | README, system spec, citation abstract |
| Operational | *A four-state visual system for marking how a claim, document, dataset, or finding should be evaluated before belief, challenge, or action.* | Explanation doc, public overview |
| Human | *Four owls tell the reader what kind of thinking they are looking at: standard, exploration, inversion, or self-audit.* | Story sections, teaching material |

See [`CHANGELOG.md`](CHANGELOG.md) for the per-version canonical sentence history.

## The Four States (v3.0.1)

| State | Operator | Determinant | Quote (normative) | Standards register |
| --- | --- | --- | --- | --- |
| NORMATIVE | I | +1 | *"This is the standard."* | RFC 2119 MUST / SHALL |
| NON-NORMATIVE | σᵥ | −1 | *"This reflects the standard."* | Informative / Advisory (NOTE) |
| CRITICAL | C₂ | +1 | *"This inverts the standard."* | RFC 2119 MUST NOT / SHALL NOT |
| METACOGNITIVE | σₕ | −1 | **"The observer audits the frame."** | Epistemic / Framework (META) |

The METACOGNITIVE phrasing was refined in v2.0.0 and is unchanged through v3.0.1. The earlier line *"This audits the standard"* is deprecated because it failed to express *thinking examining its own frame*. See [`OWL-4-METACOGNITIVE.md`](OWL-4-METACOGNITIVE.md) §1 and [`OWL-SEMAPHORE-EXPLANATION.md`](OWL-SEMAPHORE-EXPLANATION.md) for the warmer explanatory variant *"Thinking examines its own frame."*

## Accessibility — Color Is Not the Only Carrier

Every state's identity is recoverable from three redundant channels: **color + orientation + textual label/context**. This is the project's mitigation for color vision deficiency (~8% of males, ~0.5% of females of Northern-European descent) and grayscale rendering, in line with [WCAG 2.2 SC 1.4.1 (Use of Color)](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html). The CRITICAL state's intentionally low red-on-red contrast is the most acute test of the rule; red alone never carries CRITICAL identity. See [`OWL-SEMAPHORE-SYSTEM.md`](OWL-SEMAPHORE-SYSTEM.md) §7.2.

## Citation

If you use the Owl Semaphore Badge System, cite the v3.0.1 version-specific DOI for this exact release, or the concept DOI for cross-version citation (it resolves to the latest published version):

> Balboa, Carey James. *Owl Semaphore Badge System* (v3.0.1). Zenodo. https://doi.org/10.5281/zenodo.21524422
>
> Concept DOI (all versions): https://doi.org/10.5281/zenodo.19473697
>
> Previously published versions:
>
> - Balboa, Carey James. *Owl Semaphore Badge System* (v3.0.0). Zenodo. https://doi.org/10.5281/zenodo.20468727
> - Balboa, Carey James. *Owl Semaphore Badge System* (v2.0.2). Zenodo. https://doi.org/10.5281/zenodo.20433053
> - Balboa, Carey James. *Owl Semaphore Badge System* (v2.0.1). Zenodo. https://doi.org/10.5281/zenodo.20419874
> - Balboa, Carey James. *Owl Semaphore Badge System* (v2.0.0). Zenodo. https://doi.org/10.5281/zenodo.20418539

The version-specific DOI [10.5281/zenodo.21524422](https://doi.org/10.5281/zenodo.21524422) is the citing DOI embedded in the v3.0.1 source, PDFs, and metadata. The concept DOI [10.5281/zenodo.19473697](https://doi.org/10.5281/zenodo.19473697) is the all-versions DOI for cross-version citation and resolves to the latest published version. Machine-readable citation metadata is in [`CITATION.cff`](CITATION.cff).

## Reproducing the PDFs

All six PDFs (system spec + four state specs + explanation) regenerate from the markdown sources with a single command:

```bash
make pdfs
# or, equivalently:
python3 generate_pdfs.py
```

`make pdfs` produces page-one banner-tuple-bearing PDFs with embedded PDF metadata (Title, Author, Subject, Keywords, Producer, Version), a contact-sheet header, a classification ledger back page, and per-page owl headers. As of v3.0.1 the pipeline drives the parity-proven [`owl-semaphore-press`](https://github.com/IT-Help-San-Diego/owl-semaphore-press) package (pandoc → Typst → PDF); install it pinned, with `pandoc` on PATH:

```bash
pip install "owl-semaphore-press[render] @ git+https://github.com/IT-Help-San-Diego/owl-semaphore-press@0.1.1"
```

See [`Makefile`](Makefile) for additional targets:

- `make hashes` — recompute SHA-3-512 hashes for committed PDFs and release assets
- `make manifest` — rewrite `INTEGRITY-MANIFEST.md` integrity records from current hashes
- `make test` — run the integrity test suite (`tests/`) plus the study toolkit regression tests
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

## Citation Package Structure (Zotero / Zenodo attachments)

For reference managers (Zotero) and the Zenodo record, the canonical
citation package is **fourteen attachments**: six readable PDFs plus eight
canonical image assets (four composite previews + four layered master TIFFs).
Suggested display names are given so the package reads cleanly in a library:

**Six readable PDFs** (the human- and machine-readable specifications):

| File | Suggested display name |
| --- | --- |
| `OWL-SEMAPHORE-SYSTEM.pdf` | Owl Semaphore — System Specification |
| `OWL-SEMAPHORE-EXPLANATION.pdf` | Owl Semaphore — Explanation |
| `OWL-1-NORMATIVE.pdf` | Owl Semaphore — 1 NORMATIVE |
| `OWL-2-NON-NORMATIVE.pdf` | Owl Semaphore — 2 NON-NORMATIVE |
| `OWL-3-CRITICAL.pdf` | Owl Semaphore — 3 CRITICAL |
| `OWL-4-METACOGNITIVE.pdf` | Owl Semaphore — 4 METACOGNITIVE |

**Four canonical composite previews** (transparent PNG, 540 px — render
correctly in any image viewer and are the at-a-glance state previews):

| File | Suggested display name |
| --- | --- |
| `assets/releases/540/NORM-composite-transparent-540.png` | Owl Semaphore — NORMATIVE preview |
| `assets/releases/540/NONNORM-composite-transparent-540.png` | Owl Semaphore — NON-NORMATIVE preview |
| `assets/releases/540/CRIT-composite-transparent-540.png` | Owl Semaphore — CRITICAL preview |
| `assets/releases/540/META-composite-transparent-540.png` | Owl Semaphore — METACOGNITIVE preview |

**Four canonical LAYERED master assets** (multi-layer TIFF, 1080 px — the
authoritative editable masters that carry the full layer model):

| File | Suggested display name |
| --- | --- |
| `assets/masters/NORM-MASTER-1080.tiff` | Owl Semaphore — NORMATIVE master (layered) |
| `assets/masters/NONNORM-MASTER-1080.tiff` | Owl Semaphore — NON-NORMATIVE master (layered) |
| `assets/masters/CRIT-MASTER-1080.tiff` | Owl Semaphore — CRITICAL master (layered) |
| `assets/masters/META-MASTER-1080.tiff` | Owl Semaphore — METACOGNITIVE master (layered) |

> **Note on the layered master TIFFs.** The four `*-MASTER-1080.tiff` files
> are **layered** masters. Some quick-look / thumbnail viewers flatten only
> the first layer and may therefore preview these files as black, empty, or
> incomplete. This is a viewer limitation, not a defect in the file — the
> full composite is present in the layers and renders correctly in a
> layer-aware editor (e.g. GIMP, Photoshop, Affinity). The transparent
> composite previews above are provided for at-a-glance viewing precisely so
> that no one has to open a layered master just to see a state.

## Related Resources

- Public home: https://owlsemaphore.systems
- Repository: https://github.com/IT-Help-San-Diego/owl-semaphore
- Version DOI: https://doi.org/10.5281/zenodo.21524422
- Concept DOI: https://doi.org/10.5281/zenodo.19473697
- Bridge page: https://dnstool.it-help.tech/owl-semaphore
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
  "version": "3.0.1",
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "codeRepository": "https://github.com/IT-Help-San-Diego/owl-semaphore",
  "datePublished": "2026-04-07",
  "dateModified": "2026-07-23",
  "identifier": [
    "https://doi.org/10.5281/zenodo.21524422",
    "https://doi.org/10.5281/zenodo.20468727",
    "https://doi.org/10.5281/zenodo.19473697",
    "https://doi.org/10.5281/zenodo.20433053",
    "https://doi.org/10.5281/zenodo.20419874",
    "https://doi.org/10.5281/zenodo.20418539",
    "https://doi.org/10.5281/zenodo.19474599"
  ],
  "sameAs": "https://doi.org/10.5281/zenodo.21524422",
  "programmingLanguage": "Not applicable",
  "author": {
    "@type": "Person",
    "name": "Carey James Balboa",
    "identifier": "https://orcid.org/0009-0000-5237-9065"
  },
  "description": "A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants. Four-state classification (NORMATIVE, NON-NORMATIVE, CRITICAL, METACOGNITIVE) for DNS Tool documentation and related research artifacts. v3.0.0 is a structural and scientific remediation release on top of v2.0.2 that adds a normative Formal Justification for the V4 structure, a normative Limitations and Scope Boundaries section, an Exclusion Argument with use-boundary/ethics guidance, and per-state bridge and limitations paragraphs, with no change to the V4 algebra, the canonical state-operator tuples, the canonical formal sentence, the accessibility rule, or the asset set. The v3.0.0 version-specific DOI 10.5281/zenodo.20468727 (published on Zenodo) is the citing DOI embedded in the v3.0.0 source, PDFs, and metadata. The concept DOI 10.5281/zenodo.19473697 is the all-versions DOI that resolves to the latest published version. Previous published version DOI (v2.0.2): 10.5281/zenodo.20433053.",
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
  "releaseNotes": "v3.0.1 — PATCH-level errata and toolchain release on top of v3.0.0. Inserts one clarifying sentence into System §4A.1 defining the locus-of-audit axis's frame pole (one's own frame, audited at METACOGNITIVE, or the framework a claim rests on, inverted at CRITICAL), so the specification and the IRR study instruments define the axis identically. Switches PDF generation to the parity-proven owl-semaphore-press package (byte-identical Typst-source parity with the legacy generator). Folds in the IRR pilot study toolkit, repository governance documentation, and post-publication documentation corrections accumulated since the v3.0.0 tag. The V4 algebra, the four canonical state-operator tuples, the σh assignment to METACOGNITIVE, the canonical formal sentence, the accessibility rule, the color/orientation semantics, and the asset set are unchanged from v3.0.0.",
  "isAccessibleForFree": true
}
</script>
