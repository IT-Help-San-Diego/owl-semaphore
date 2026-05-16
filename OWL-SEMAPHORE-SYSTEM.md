![Owl Semaphore Master Proof](assets/proofs/OWL-SEMAPHORE-MASTER-PROOF.png)

# OWL SEMAPHORE — SYSTEM SPECIFICATION
A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants.
## Version 1.3.0-rc (release candidate; Zenodo DOI to be minted on publication)

- **Concept DOI (all versions):** [10.5281/zenodo.19473697](https://doi.org/10.5281/zenodo.19473697)
- **Last published version DOI (v1.2.0):** [10.5281/zenodo.19474599](https://doi.org/10.5281/zenodo.19474599)
- **Version DOI (v1.3.0):** `TBD_BY_ZENODO_ON_RELEASE`
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

## 1. Statement of Intent

This document defines the Owl Semaphore as a formal epistemic notation system grounded in mathematics, perception, and reproducible graphical structure.

This is not a taxonomy of labels. It is a finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants.

The objective is to create a system that is:

- mathematically coherent
- visually invariant
- epistemically meaningful
- operationally reproducible
- resistant to ambiguity and drift

---

## 2. Mathematical Foundation

### 2.1 Group Definition

The four visual states are modelled by the Klein four-group:

$$
V_4 = \{I, \sigma_v, C_2, \sigma_h\}
$$

The four transformations form a finite subgroup of the orthogonal group \(O(2)\) isomorphic to \(V_4\) (equivalently, the dihedral group \(D_2\)). The group \(V_4\) is finite; \(O(2)\) is a continuous Lie group. The system embeds \(V_4\) inside \(O(2)\) — it does not claim that \(V_4\) is \(O(2)\) (see [Knill, Harvard, "The orthogonal group"](https://people.math.harvard.edu/~knill/teaching/math22b2019/handouts/lecture08.pdf); [Klein four-group, nLab](https://ncatlab.org/nlab/show/Klein+four-group)).

### 2.2 Elements

| State | Operator | Matrix | Mapping | Determinant |
|------|--------|--------|--------|------------|
| NORMATIVE | I | diag(1, 1) | (x,y) → (x,y) | +1 |
| NON-NORMATIVE | σᵥ | diag(-1, 1) | (x,y) → (-x,y) | -1 |
| CRITICAL | C₂ | diag(-1, -1) | (x,y) → (-x,-y) | +1 |
| METACOGNITIVE | σₕ | diag(1, -1) | (x,y) → (x,-y) | -1 |

### 2.3 Cayley Table (Closure Proof)

Composition \(g \circ h\), read as "row then column":

| ∘ | I | σᵥ | C₂ | σₕ |
|---|---|----|----|----|
| **I**  | I  | σᵥ | C₂ | σₕ |
| **σᵥ** | σᵥ | I  | σₕ | C₂ |
| **C₂** | C₂ | σₕ | I  | σᵥ |
| **σₕ** | σₕ | C₂ | σᵥ | I  |

The table establishes the four group axioms for this set under composition:

- **Closure** — every cell lies in {I, σᵥ, C₂, σₕ}.
- **Associativity** — inherited from matrix multiplication in \(O(2)\).
- **Identity** — \(I\) acts as the identity (top row, left column).
- **Inverses** — every diagonal entry is \(I\), so \(g \circ g = I\) and \(g^{-1} = g\).

This is the unique (up to isomorphism) abelian non-cyclic group of order 4 ([Klein four-group, Wikipedia](https://en.wikipedia.org/wiki/Klein_four-group)).

### 2.4 Closure Identities (informative)

Useful identities visible directly in the Cayley table:

σᵥ ∘ σₕ = C₂  
σᵥ ∘ C₂ = σₕ  
σₕ ∘ C₂ = σᵥ

Each element is its own inverse:

$$
g^2 = I \quad \text{for every } g \in V_4.
$$

### 2.5 Interpretation

The closure shown above is not decorative. It enforces that all epistemic transitions remain inside a defined state space. Group structure guarantees algebraic closure; it does not by itself guarantee security, correctness, or analytic validity of the content marked with these states.

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

This is the single canonical formal definition (see `CHANGELOG.md`).

---

## 12. Normative Register and Standards Labelling (informative)

This specification uses RFC 2119 / RFC 8174 BCP 14 normative keywords **only when** they appear in ALL CAPITALS and **only** for genuine interoperability requirements (asset transparency, hash verification, transform identity, state mapping). The mandated BCP 14 boilerplate applies:

> The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC 2119] [RFC 8174] when, and only when, they appear in all capitals, as shown here.

Lowercase "must", "should", "may" carry their normal English meanings and are not normative. Sections labelled `(informative)` are explanatory and place no interoperability requirement on implementations (per ISO/IEC Directives Part 2, §3 and Annex H).

---

## 13. Accessibility (informative)

The four states are encoded with redundant channels — color, orientation, label — so that the state identity remains perceptible to readers with color vision deficiency (approximately 8% of males and 0.5% of females of Northern European descent, per [PMC global CVD review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12385717/); rates vary by population) and in grayscale rendering. This satisfies the design intent of WCAG 2.2 SC 1.4.1 *Use of Color* (Level A) and Section 508 §302.3. The redundant-encoding approach follows Bertin's retinal variables (shape, value, orientation) and Moody's dual-coding principle.

This specification targets WCAG 2.2 Level AA conformance. "Targets" is the correct register: WCAG conformance requires empirical verification, not design intent alone.

---

## 14. Analytic Confidence (informative)

Where the Owl Semaphore is used inside analytic products, users adopting [ICD 203](https://www.dni.gov/files/documents/ICD/ICD-203.pdf) tradecraft should observe ICD 203's prohibition on combining a confidence statement and a likelihood statement in the same sentence. The Owl Semaphore is a state notation, not a confidence/likelihood scale: it marks how a claim is being evaluated, not how probable the claim is or how strong the supporting evidence is. ICD 203 is referenced as a discipline standard; it is not a binding external requirement on this notation.

---

## 15. Relation to Formal Verification (informative)

The Owl Semaphore borrows discipline — explicit invariants, bounded state space, machine-checkable transition rules — from formal-verification practice. The canonical reference here is seL4 ([Klein et al., SOSP 2009](https://trustworthy.systems/publications/nicta_full_text/1852.pdf); [seL4 whitepaper](https://sel4.systems/About/seL4-whitepaper.pdf)). The Owl Semaphore does not claim that this repository, its assets, or its specifications are formally verified in the seL4 sense. seL4 is cited as an aspirational discipline reference only.

---

## 16. Closing Statement

The Owl Semaphore is designed to make reasoning visible.

It enforces structure where ambiguity would otherwise dominate, and it preserves interpretability across transformation, disagreement, and self-examination.

It is not decoration.

It is a constraint system for thought.

---

## 17. Citations

- [RFC 2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels," BCP 14, RFC 2119, March 1997. https://www.rfc-editor.org/rfc/rfc2119
- [RFC 8174] Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words," BCP 14, RFC 8174, May 2017. https://www.rfc-editor.org/rfc/rfc8174
- [ISO/IEC Directives Part 2] Principles and rules for the structure and drafting of ISO and IEC documents. https://www.iso.org/sites/directives/current/part2/index.xhtml
- [Klein four-group, Wikipedia] https://en.wikipedia.org/wiki/Klein_four-group
- [Klein four-group, nLab] https://ncatlab.org/nlab/show/Klein+four-group
- [Knill 2019] "Unit 8: The orthogonal group," Harvard Math 22b notes. https://people.math.harvard.edu/~knill/teaching/math22b2019/handouts/lecture08.pdf
- [Bertin 1967/1983] *Semiology of Graphics*, ESRI Press 2011 edition.
- [Moody 2009] "A Scientific Approach to Designing Visual Notations in Requirements Engineering," RE 2009 Tutorial. http://csis.pace.edu/~ogotel/professional/RE09%20Tutorial%20-%20Designing%20Effective%20Visual%20Notations.pdf
- [WCAG 2.2] W3C Recommendation, October 2023. https://www.w3.org/TR/WCAG22/
- [Section 508] Making Color Usage Accessible. https://www.section508.gov/create/making-color-usage-accessible/
- [PMC CVD Global Review] https://pmc.ncbi.nlm.nih.gov/articles/PMC12385717/
- [ICD 203] ODNI, "Analytic Standards," January 2, 2015. https://www.dni.gov/files/documents/ICD/ICD-203.pdf
- [Klein et al. 2009] "seL4: Formal Verification of an OS Kernel," SOSP 2009. https://trustworthy.systems/publications/nicta_full_text/1852.pdf
- [seL4 Whitepaper] https://sel4.systems/About/seL4-whitepaper.pdf
