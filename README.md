![Owl Semaphore Master Proof](assets/proofs/OWL-SEMAPHORE-MASTER-PROOF.png)

# OWL SEMAPHORE — SYSTEM SPECIFICATION
A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants.

## Version 1.3.0-rc (release candidate — not yet published to Zenodo)

[![DOI (last published, v1.2.0)](https://zenodo.org/badge/DOI/10.5281/zenodo.19474599.svg)](https://doi.org/10.5281/zenodo.19474599)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

- **Version DOI (v1.3.0):** `TBD_BY_ZENODO_ON_RELEASE` (will be minted when this release candidate is published to Zenodo)
- **Last published version DOI (v1.2.0):** [10.5281/zenodo.19474599](https://doi.org/10.5281/zenodo.19474599)
- **Concept DOI (all versions):** [10.5281/zenodo.19473697](https://doi.org/10.5281/zenodo.19473697)
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## Canonical wording stack

| Layer | Sentence |
| --- | --- |
| Formal | A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants. |
| Operational | A four-state visual system for marking how a claim, document, dataset, or finding should be evaluated before belief, challenge, or action. |
| Human | Four owls tell the reader what kind of thinking they are looking at: standard, exploration, inversion, or self-audit. |

See [`OWL-SEMAPHORE-EXPLANATION.md`](OWL-SEMAPHORE-EXPLANATION.md) for the origin story, archetype rationale, and why two states were not enough.

## Citation

If you use the Owl Semaphore Badge System, please cite the most recently published version DOI:

> Balboa, Carey James. *Owl Semaphore Badge System* (v1.2.0). Zenodo. https://doi.org/10.5281/zenodo.19474599

When v1.3.0 is published, replace with the new version DOI. Machine-readable citation metadata is available in [`CITATION.cff`](CITATION.cff).

---

## 1. Statement of Intent

This document defines the Owl Semaphore as a formal epistemic system grounded in mathematics, perception, and reproducible graphical structure.

This is not a taxonomy of labels. It is a closed algebra over epistemic states, mapped into a constrained visual system.

The objective is to create a system that is:

- mathematically coherent
- visually invariant
- epistemically meaningful
- operationally reproducible
- resistant to ambiguity and drift

---

## 2. Mathematical Foundation

### 2.1 Group Definition

The four visual states of the Owl Semaphore are modelled by the Klein four-group:

$$
V_4 = \{I, \sigma_v, C_2, \sigma_h\}
$$

The four transformations form a finite subgroup of the orthogonal group \(O(2)\) isomorphic to \(V_4\) (equivalently, the dihedral group \(D_2\)). \(V_4\) itself is finite; \(O(2)\) is a continuous Lie group, so the system uses \(V_4\) as a subgroup of \(O(2)\), not as \(O(2)\) itself. The explicit Cayley table for these elements is given in Section 2.3 and in `OWL-SEMAPHORE-SYSTEM.md` §2.

### 2.2 Elements

| State | Operator | Mapping | Determinant |
|------|--------|--------|------------|
| NORMATIVE | I | (x,y) → (x,y) | +1 |
| NON-NORMATIVE | σᵥ | (x,y) → (-x,y) | -1 |
| CRITICAL | C₂ | (x,y) → (-x,-y) | +1 |
| METACOGNITIVE | σₕ | (x,y) → (x,-y) | -1 |

### 2.3 Closure

The system is closed under composition:

σᵥ ∘ σₕ = C₂  
σᵥ ∘ C₂ = σₕ  
σₕ ∘ C₂ = σᵥ

Each element is its own inverse:

$$
g^2 = I
$$

### 2.4 Interpretation

This closure is not decorative. It enforces that all epistemic transitions remain inside a defined state space.

---

## 3. State vs Process

### 3.1 Discrete States

The four owls represent discrete epistemic states:

- identity
- reflection
- inversion
- frame inversion

### 3.2 Continuous Process

Not all operations belong to the state system.

### 3.3 The 31° Rotation

The measured ~31° rotation is not part of V₄.

- it is not closed
- repeated composition does not return to the set

It represents **process**, not state.

### 3.4 Principle

States classify position.  
Processes move between positions.

---

## 4. Epistemic Model

### 4.1 Core Structure

The system separates three levels:

1. object of analysis  
2. observer  
3. evaluative frame

### 4.2 State Mapping

| State | Meaning |
|------|--------|
| NORMATIVE | baseline framework |
| NON-NORMATIVE | reflected interpretation |
| CRITICAL | inverted assumptions |
| METACOGNITIVE | observer audit |

### 4.3 Critical Distinction

The system is only valid if these states are not conflated.

---

## 5. Physical Grounding

The system is grounded in observable behavior.

### 5.1 Canonical Example

The METACOGNITIVE state is physically instantiated by:

- searching a space normally
- failing to detect a target
- inverting the viewing frame

### 5.2 Interpretation

The object does not change.  
The observer does not change.  
The frame changes.

---

## 6. Visual System Mapping

### 6.1 Shared Geometry

All owls share:

- identical center
- identical radial structure
- identical meander ring

### 6.2 Transform Consistency

Each owl is derived from the normative form by a valid element of V₄.

No arbitrary transformations are permitted.

### 6.3 Invariants

- geometry is fixed  
- center is fixed  
- ring structure is fixed  

---

## 7. Color System

Each state is assigned a distinct color space region:

- gold → normative authority
- teal → analytical reflection
- red → adversarial inversion
- amethyst → introspective analysis

### 7.1 Constraint

Color is semantic, not decorative.

---

## 8. Integrity Model

All assets must satisfy:

- reproducibility from layers
- RGBA transparency correctness
- cryptographic verification (SHA-3-512)

### 8.1 Principle

An asset is not valid because it looks correct.  
It is valid because it verifies.

---

## 9. File and System Architecture

### 9.1 Structure

OWL-SEMAPHORE/
├── OWL-SEMAPHORE-SYSTEM.md
├── INTEGRITY-MANIFEST.md
├── OWL-1-NORMATIVE/
├── OWL-2-NON-NORMATIVE/
├── OWL-3-CRITICAL/
└── OWL-4-METACOGNITIVE/

### 9.2 Separation of Concerns

- system rules live here
- state rules live in owl-specific files

---

## 10. Interpretation Doctrine

### 10.1 The System Encodes Position, Not Truth

The Owl Semaphore does not assert correctness.

It encodes:

- how something is being evaluated
- not whether it is ultimately true

### 10.2 Misuse Condition

If the system is used to imply certainty rather than epistemic position, it is being used incorrectly.

---

## 11. Core Principle

This system is defined as:

A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants.

This sentence is the single canonical formal definition for the project. Earlier wording variants (recorded verbatim in [`CHANGELOG.md`](CHANGELOG.md)) are superseded as of v1.3.0-rc.

---

## 12. Closing Statement

The Owl Semaphore is designed to make reasoning visible.

It enforces structure where ambiguity would otherwise dominate, and it preserves interpretability across transformation, disagreement, and self-examination.

It is not decoration.

It is a constraint system for thought.
## Standards

- NORMATIVE (NORM)
- NON-NORMATIVE (NONNORM)
- CRITICAL (CRIT)
- METACOGNITIVE (META)

## Release Location

assets/releases/540/

## Current Release Set

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
  "sameAs": "https://doi.org/10.5281/zenodo.19473697",
  "programmingLanguage": "Not applicable",
  "author": {
    "@type": "Person",
    "name": "Carey James Balboa",
    "identifier": "https://orcid.org/0009-0000-5237-9065"
  },
  "description": "A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants. Provides four classification states (NORMATIVE, NON-NORMATIVE, CRITICAL, METACOGNITIVE) for marking how a claim, document, dataset, or finding should be evaluated.",
  "keywords": [
    "Owl Semaphore",
    "DNS Tool",
    "visual standard",
    "classification system",
    "documentation",
    "epistemology"
  ],
  "releaseNotes": "Reproducible, integrity-verified release of the Owl Semaphore badge system.",
  "isAccessibleForFree": true
}
</script>
