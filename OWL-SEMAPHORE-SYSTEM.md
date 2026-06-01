![Owl Semaphore Master Proof](assets/proofs/OWL-SEMAPHORE-MASTER-PROOF.png)

# OWL SEMAPHORE — SYSTEM SPECIFICATION
A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants.
## Version 3.0.0

---

## 1. Statement of Intent

This document defines the Owl Semaphore as a formal epistemic system grounded in mathematics, perception, and reproducible graphical structure.

This is not a taxonomy of labels. It is a closed algebra over epistemic states, mapped into a constrained visual notation system.

The objective is a system that is:

- mathematically coherent
- visually invariant
- epistemically meaningful
- operationally reproducible
- resistant to ambiguity and drift

### 1.0 Core Framing (informative preamble)

> The semaphore is a visual notation. Its design target is *compatibility* with established mathematics, accessibility practice, and carefully bounded analogies from epistemology and cognitive science — not a theory of everything, and not a claim over the whole of human knowledge.

This preamble is informative. It states the project's external-compatibility criterion: the four states are a notation system for moves that several mature fields already make — peer review separates normative from non-normative; CVEs flag critical; methodology audits are metacognitive — not a novel taxonomy. Where the notation contradicts a careful practitioner's existing terminology in psychiatry, philosophy, statistics, computer science, or accessibility, the notation is wrong, not the field. The four front-loaded stories in the state specifications (*The Proven Ground*, *Da Vinci's Wings*, *The Manhattan Moment*, *The Observer's Mirror*) are the human-intuition bridge to the V₄ algebra defined in §2 below; see [`OWL-SEMAPHORE-EXPLANATION.md`](OWL-SEMAPHORE-EXPLANATION.md) §1B for the ordered reading guide and §13 for the closing bridge.

### 1.1 Canonical Sentence Stack (v3.0.0)

The project uses a three-layer canonical sentence stack so that the same concept can be expressed at the level of mathematics, operation, and human story without drifting between documents:

| Layer | Canonical sentence | Use |
| --- | --- | --- |
| Formal | *A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants.* | README, system spec, Zenodo deposit metadata, citation abstract |
| Operational | *A four-state visual system for marking how a claim, document, dataset, or finding should be evaluated before belief, challenge, or action.* | Explanation document, public overview, DNS Tool bridge |
| Human | *Four owls tell the reader what kind of thinking they are looking at: standard, exploration, inversion, or self-audit.* | Story sections, teaching material |

Earlier inconsistent forms — *"mapped into a visual system with strict invariants"* (former §11) and *"implemented as a reproducible visual system with enforced invariants"* (former README masthead) — were reconciled in v2.0.0 onto the canonical formal sentence above, and that reconciliation is unchanged through v3.0.0.

---

## 2. Mathematical Foundation

### 2.1 Group Definition

The Owl Semaphore's discrete state space is modeled as the Klein four-group:

$$
V_4 = \{I, \sigma_v, C_2, \sigma_h\}
$$

This is a finite subgroup of the orthogonal group \(O(2)\) isomorphic to V₄ (equivalently the dihedral group D₂); it is not O(2) itself ([Vierergruppe, Wolfram MathWorld](https://mathworld.wolfram.com/Vierergruppe.html); [nLab, Klein four-group](https://ncatlab.org/nlab/show/Klein+four-group); [Knill, Harvard Math 22b, Unit 8: The orthogonal group](https://people.math.harvard.edu/~knill/teaching/math22b2019/handouts/lecture08.pdf)).

### 2.2 Elements

| State | Operator | Mapping | Determinant |
|------|--------|--------|------------|
| NORMATIVE | I | (x,y) → (x,y) | +1 |
| NON-NORMATIVE | σᵥ | (x,y) → (-x,y) | -1 |
| CRITICAL | C₂ | (x,y) → (-x,-y) | +1 |
| METACOGNITIVE | σₕ | (x,y) → (x,-y) | -1 |

The σₕ assignment to METACOGNITIVE is unchanged from v1.2.0. The interpretive wording was refined in v2.0.0 (see §4) and is unchanged through v3.0.0.

### 2.3 Closure (Cayley Table)

The system is closed under composition. The Cayley table is:

| ∘ | I | σᵥ | C₂ | σₕ |
| --- | --- | --- | --- | --- |
| **I** | I | σᵥ | C₂ | σₕ |
| **σᵥ** | σᵥ | I | σₕ | C₂ |
| **C₂** | C₂ | σₕ | I | σᵥ |
| **σₕ** | σₕ | C₂ | σᵥ | I |

Each element is its own inverse: \(g^2 = I\) for all \(g \in V_4\). The four group axioms (closure, associativity, identity, inverses) hold by the table above.

### 2.4 Interpretation

This closure is not decorative. It enforces that all epistemic transitions remain inside a defined state space. Group structure guarantees algebraic closure; it does not by itself guarantee security or behavioral correctness without further proof.

---

## 3. State vs Process

### 3.1 Discrete States

The four owls represent discrete epistemic states:

- identity (NORMATIVE)
- reflection (NON-NORMATIVE)
- inversion (CRITICAL)
- frame-audit (METACOGNITIVE)

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

### 4.2 State Mapping (Normative Phrasing — v3.0.0)

| State | Quote (scientific / normative) | Meaning |
|------|--------|--------|
| NORMATIVE | *"This is the standard."* | baseline framework |
| NON-NORMATIVE | *"This reflects the standard."* | reflected interpretation |
| CRITICAL | *"This inverts the standard."* | inverted assumptions |
| METACOGNITIVE | *"The observer audits the frame."* | observer audits its own evaluative frame — thinking about thinking |

> **Note on the METACOGNITIVE phrasing.** The earlier line *"This audits the standard"* is deprecated as of v2.0.0 and remains deprecated through v3.0.0. The audit at METACOGNITIVE is directed at the **observer's own evaluative frame**, not at the standard as an external object. The explanatory variant — *"Thinking examines its own frame"* — appears in the warmer-voiced [OWL-SEMAPHORE-EXPLANATION.md](OWL-SEMAPHORE-EXPLANATION.md). This refinement aligns the language with the cognitive-science meaning of metacognition: monitoring and regulation of one's own cognitive process ([metacognitive reflection review, PMC 11368986](https://pmc.ncbi.nlm.nih.gov/articles/PMC11368986/)).

### 4.3 Critical Distinction

The system is only valid if these states are not conflated.

---

## 4A. Formal Justification for V₄ Structure (normative)

The choice of V₄ as the carrier algebra is not aesthetic. This section states *why* the state space has exactly four elements, why those elements form the Klein four-group rather than another group of similar size, and why an operator algebra is the right modeling tool rather than a continuous scale or a flat list of labels. It is placed after the operator and epistemic definitions (§2–§4) and before the application examples (§5 onward) so that the algebra is justified before it is exercised.

### 4A.1 Why four states — not two, three, six, or eight

The four states are forced by composing two independent binary epistemic distinctions, then closing the result under composition.

- **Distinction 1 — orientation of stance toward the standard (preserve vs. reverse lateral stance).** A claim can be read in agreement with the prevailing standard, or laterally reflected against it. This is the σᵥ axis.
- **Distinction 2 — locus of audit (object vs. frame).** Evaluation can be directed at the object under analysis, or turned back onto the observer's own evaluative frame. This is the σₕ axis.

These two reflections are independent (they act on orthogonal axes), and each is an involution. The smallest set closed under their composition is exactly:

$$
\{\, I,\ \sigma_v,\ \sigma_h,\ \sigma_v\sigma_h = C_2 \,\}
$$

- **Not two states.** A single binary (e.g. "normative vs. critical") cannot represent the frame-audit move at all; it collapses Distinction 2. Two states under-fit the phenomena the notation must mark.
- **Not three states.** Any three of the four are not closed: composing the two non-identity reflections produces the fourth element (σᵥ ∘ σₕ = C₂). A three-state system is therefore algebraically incomplete — closure *forces* the fourth state into existence. This is the central structural fact of the system.
- **Not six or eight states.** Adding states beyond the four (e.g. moving to D₃/S₃ of order 6, or D₄ of order 8) introduces generators with no distinct epistemic referent. The extra elements are redundant relabelings of the same two underlying binary distinctions; they fail parsimony without adding representational power.

Four is therefore the unique closed answer to two independent binary epistemic distinctions: not fewer (incomplete), not more (redundant).

### 4A.2 Why V₄ — not C₄, and not a non-abelian group

Two groups of order four exist: the cyclic group C₄ and the Klein four-group V₄. The notation requires V₄.

- **Against C₄.** C₄ has a generator of order 4, meaning one of its elements is *not* self-inverse — applying it twice does not return to start. Epistemically, every state move in this system is its own undo: reflecting a stance twice returns the original stance; auditing a frame and auditing it back returns the original reading. This involutive property (g² = I for all g) holds in V₄ and fails in C₄. C₄ would impose a directional 4-cycle on states that have no such ordering.
- **Against non-abelian groups.** The two distinctions commute: reflecting stance then auditing frame yields the same state as auditing frame then reflecting stance. Order independence is an empirical property of the epistemic moves being modeled, and it is exactly the abelian condition. The smallest non-abelian group (S₃, order 6) would encode a path-dependence the phenomena do not exhibit, and it is already excluded by §4A.1 on cardinality grounds.

V₄ is the unique group that is order 4, abelian, and fully involutive — matching all three observed properties of the epistemic moves.

### 4A.3 Why an operator algebra — not a continuous scale or a flat label set

- **Against a continuous scale.** A scalar "confidence" or "normativity" dial cannot represent the frame-audit move, which is orthogonal to the object-level stance rather than further along it. Continuous scales also admit no notion of closure: there is no guarantee that operations on them stay inside a defined space, and no algebraic check that a transition is legitimate.
- **Against a flat list of labels.** A taxonomy of four unrelated labels would carry the same four names but none of the structure: it could not say that CRITICAL *is* the composition of the two reflections, could not guarantee that composing states yields another defined state, and could not be verified for closure. The operator algebra makes the relationships between states *checkable* (the Cayley table, §2.3) rather than asserted.

### 4A.4 Comparison table

The table below compares V₄ against the main alternatives on the properties that matter for a verifiable epistemic notation. "Compositionality" means states can be composed and the result is a defined state; "constraint-verifiability" means closure and legality can be checked mechanically; "transition-modeling" means moves between states are first-class; "empirical-tractability" means the structure makes testable commitments.

| Model | Parsimony | Compositionality | Constraint-verifiability | Transition-modeling | Empirical-tractability |
| --- | --- | --- | --- | --- | --- |
| **V₄ (this system)** | exactly 4 — minimal closed set | yes — closed under ∘ | yes — Cayley table + involution | yes — operators *are* transitions | yes — commits to closure, involution, commutativity |
| Binary (2 labels) | over-parsimonious — collapses frame audit | n/a | trivial but under-fitting | no | weak — too coarse to test |
| Three labels (no closure) | misleadingly small | no — not closed | fails (closure forces 4th) | partial | incoherent (algebraically incomplete) |
| C₄ (order 4) | 4, but wrong structure | yes | yes, but imposes false 4-cycle | yes, but directional | makes false ordering commitment |
| D₃/S₃ (order 6) or D₄ (order 8) | redundant generators | yes | yes | yes | over-fits; extra states lack referents |
| Continuous scale | one dial | no algebraic composition | no closure notion | as scalar motion only | hard to falsify; can't encode frame axis |
| Flat label taxonomy | 4 names | no | no | no | asserts rather than checks structure |

The justification is therefore convergent: cardinality, group structure, and modeling-tool choice each independently select V₄, and they agree.

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
The observer does not change as an agent.
The frame changes.

In short: the observer audits the frame.

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

## 7. Color System and Accessibility

Each state is assigned a distinct color space region:

- gold → normative authority
- teal → analytical reflection
- red → adversarial inversion
- amethyst → introspective frame-audit

### 7.1 Constraint

Color is semantic, not decorative.

### 7.2 Accessibility — Triple-Redundant Encoding (v3.0.0, normative)

**Color is not the only carrier.** State identity must remain recoverable when color is removed (grayscale rendering, color vision deficiency, or low-vision contexts). Every state in the Owl Semaphore is therefore encoded through at least three independent channels:

1. **color** (the palette assigned in §7)
2. **orientation** (the V₄ transform applied to the canonical owl: upright/inverted × right/left-facing)
3. **textual label and context** (the literal state token — `NORMATIVE`, `NON-NORMATIVE`, `CRITICAL`, `METACOGNITIVE` — and the math/quote tuple printed alongside the badge)

This satisfies the design intent of **WCAG 2.2 SC 1.4.1 (Use of Color, Level A)**, which prohibits color from being the only visual means of conveying information ([W3C](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html)), and aligns with Section 508 §302.3 ([Section 508.gov](https://www.section508.gov/create/making-color-usage-accessible/)). The CRITICAL state's intentionally low red-on-red contrast is the most acute test of this rule: redness alone never carries CRITICAL identity — orientation (upside-down, left-facing) and the literal label `CRITICAL` are required.

Red-green color vision deficiency affects approximately 8% of males and 0.5% of females of Northern European descent; rates vary by population ([PMC global CVD review, 12385717](https://pmc.ncbi.nlm.nih.gov/articles/PMC12385717/)).

Full WCAG 2.2 Level AA empirical conformance testing (automated checks, CVD simulation, user testing) is scoped to a future release; v3.0.0 carries forward the design rule and its compliance intent established in v2.0.0.

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
├── OWL-SEMAPHORE-EXPLANATION.md
├── INTEGRITY-MANIFEST.md
├── CHANGELOG.md
├── OWL-1-NORMATIVE.md
├── OWL-2-NON-NORMATIVE.md
├── OWL-3-CRITICAL.md
└── OWL-4-METACOGNITIVE.md

### 9.2 Separation of Concerns

- system rules live in the system spec
- state rules live in the four owl-specific files
- origin story and audience rationale live in the explanation document
- canonical sentence history lives in `CHANGELOG.md`

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

## 11. Core Principle (Reconciled, v3.0.0)

This system is defined as:

> **A finite algebra over epistemic states, implemented as a reproducible visual notation system with enforced invariants.**

This sentence is the single formal canonical definition for v3.0.0, unchanged from v2.0.0. It supersedes both *"implemented as a reproducible visual system with enforced invariants"* and *"mapped into a visual system with strict invariants"*. See [CHANGELOG.md](CHANGELOG.md) for the per-version canonical-sentence history.

---

## 12. Normative-Language Discipline

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 ([RFC 2119](https://www.rfc-editor.org/rfc/rfc2119); [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174)) **when, and only when, they appear in all capitals, as shown here**. Lowercase forms ("must", "should", "may") carry ordinary English meanings.

Sections labeled "(normative)" form part of the canonical specification; sections labeled "(informative)" or "(explanatory)" provide context only and do not extend the algebra.

---

## 12A. Limitations and Scope Boundaries (normative)

The Owl Semaphore makes specific, bounded claims. This section states what the system does *not* claim, so that the algebra (§2, §4A) is not over-read.

### 12A.1 Four states are deliberately coarse

The four-state algebra is a low-resolution notation by design. It marks *which kind of epistemic move* a reader is looking at — standard, exploration, inversion, self-audit — not the degree, confidence, or correctness of that move. Many real evaluations carry finer gradations (partial agreement, mixed evidence, staged revision) that the four states intentionally compress. The coarseness is the source of the system's parsimony and verifiability (§4A), but it means the notation is a classifier of stance, never a substitute for the underlying argument. Where a task needs continuous confidence, the semaphore should sit *alongside* such a measure, not replace it.

### 12A.2 No empirical validation yet

The algebraic claims (closure, involution, commutativity) are proven (§2.3). The *epistemic* claim — that these four states usefully and reliably partition how practitioners evaluate real claims — has not been empirically tested. There is no inter-rater reliability study, no user study, and no corpus annotation demonstrating that independent annotators assign the same state to the same artifact. The full WCAG 2.2 Level AA conformance testing noted in §7.2 is likewise future work. Until such studies exist, the system's epistemic utility is a design hypothesis supported by analogy to mature practice (peer review, CVE severity, methodology audit), not a validated empirical result.

### 12A.3 Cultural specificity and semantic-interpretation risk

The owl iconography, the gold/teal/red/amethyst palette, and the upright/inverted/left/right orientation conventions are culturally situated choices. Owls do not carry uniform connotations across cultures; color associations (red as adversarial, gold as authoritative) are not universal; and reading order assumptions (left/right stance) reflect particular conventions. The semantic mapping from a visual badge to an epistemic state therefore depends on a learned key (§4.2, §7) and is not self-evident to an untrained viewer. Misreading risk is highest where the badge is encountered without its label or context — which is precisely why triple-redundant encoding (§7.2) requires the literal state token, never color or orientation alone. The system encodes position, not truth (§10); a badge asserts how something is being evaluated, and even that assertion is only legible through the shared notation.

---

## 13. Closing Statement

The Owl Semaphore is designed to make reasoning visible.

It enforces structure where ambiguity would otherwise dominate, and it preserves interpretability across transformation, disagreement, and self-examination.

It is not decoration.

It is a constraint system for thought.
