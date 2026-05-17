![METACOGNITIVE — v2 final composed badge](assets/v2/final-540/METACOGNITIVE-V2-FINAL-COMPOSED-540.png)

# OWL SEMAPHORE — METACOGNITIVE STANDARD SPECIFICATION

## OWL 4 / METACOGNITIVE / Frame-Audit State (σₕ)

### Version 2.0.0-rc (release candidate; document subordinate to v2.0.0-rc)

---

## 1. Statement of Intent

This document defines the **METACOGNITIVE owl** as the frame-audit state within the Owl Semaphore system: the state in which thinking examines its own frame rather than its object.

This is not a philosophical overlay. It is a mathematically defined operator (σₕ ∈ V₄) whose action is applied to the evaluative frame of an observer rather than to the object of analysis.

The purpose of this state is to enable structured inspection of perception, interpretation, and the analytical process itself. In short: METACOGNITIVE marks **thinking about thinking** ([Flavell 1979 / metacognition review, PMC 11368986](https://pmc.ncbi.nlm.nih.gov/articles/PMC11368986/)).

> **Canonical phrasing.** Across this release the METACOGNITIVE state is described as **"The observer audits the frame"** in normative/scientific contexts and **"Thinking examines its own frame"** in explanatory/teaching contexts. Earlier wording — *"This audits the standard"* — is deprecated as of v1.3.0-rc because it failed to convey that the audit is directed at the observer's own evaluative frame (thinking about thinking), not at an external object.

---

## 2. System Context

The Owl Semaphore is defined by the Klein four-group (a finite subgroup of the orthogonal group O(2) isomorphic to V₄, equivalently the dihedral group D₂):

$$
V_4 = \{I, \sigma_v, C_2, \sigma_h\}
$$

The METACOGNITIVE owl corresponds to the horizontal reflection operator (the operator that flips the vertical coordinate, i.e. inverts up/down structure):

$$
\sigma_h : (x,y) \mapsto (x,-y)
$$

The σₕ assignment and the V₄ algebra are unchanged from v1.2.0. Only the explanatory and interpretive language is refined.

---

## 3. Ontological Role

### 3.1 Semantic Designation

METACOGNITIVE represents:

- **observer-audit**: the observer auditing its own evaluative frame
- **frame-audit**: examination of the frame through which a claim is being evaluated
- **thinking about thinking**: monitoring and regulation of one's own cognitive process
- **controlled frame inversion**: a structured, reversible inversion of the evaluative frame to interrupt automatic recognition

### 3.2 Interpretive Role

This state indicates that:

- the subject of analysis remains fixed
- the evaluative frame has been deliberately inverted
- the observer is auditing their own perceptual or analytical process

In one sentence: **the observer audits the frame.**

### 3.3 What It Does Not Mean

- not subject change (the object of analysis is unchanged)
- not alternative interpretation (that is NON-NORMATIVE)
- not adversarial inversion (that is CRITICAL)
- not a claim that metacognition eliminates bias; metacognitive prompts can surface and partially mitigate cognitive biases but do not remove them ([ICD 203 §B](https://www.dni.gov/files/documents/ICD/ICD-203.pdf))

It is **observer-level analysis**, not object-level modification.

---

## 4. Mathematical Definition

### 4.1 State Operator

$$
T_{\text{meta}} = \sigma_h
$$

### 4.2 Matrix Form

$$
\sigma_h =
\begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}
$$

### 4.3 Determinant

$$
\det(\sigma_h) = -1
$$

### 4.4 Properties

- orientation-reversing
- reflection class
- order 2 (σₕ ∘ σₕ = I)

### 4.5 Cayley-Table Position

Within V₄ the METACOGNITIVE element σₕ satisfies:

- σₕ ∘ σₕ = I
- σₕ ∘ σᵥ = C₂
- σₕ ∘ C₂ = σᵥ

This places METACOGNITIVE on the reflection axis orthogonal to NON-NORMATIVE within the group.

---

## 5. Physical Instantiation (Canonical Demonstration)

### 5.1 Operational Description

A concrete physical demonstration of the METACOGNITIVE state is:

1. Search a room in the upright position
2. Fail to detect the target
3. Bend over and view the same environment upside down (e.g., through the legs)

This implements σₕ on the observer's frame:

$$
(x,y) \mapsto (x,-y)
$$

### 5.2 Key Property

- the environment does not change
- the observer does not change as an agent
- the evaluative frame changes (its vertical axis is inverted)

### 5.3 Why It Works

The maneuver disrupts perceptual priors:

- gravity alignment
- lighting expectations
- pattern-recognition bias

This forces reconstruction instead of automatic recognition. The frame-audit is the point: thinking is forced to examine its own frame, not just the scene.

---

## 6. Coordinate System

Same as normative:

- canvas: 1080 × 1080
- center: (540, 540)

Transformation is applied relative to the center.

---

## 7. Canonical Orientation

### 7.1 Visual Definition

- upside down
- faces RIGHT

### 7.2 Transform Relationship

The METACOGNITIVE owl is derived from normative via horizontal reflection (σₕ), i.e. inversion of the vertical coordinate.

---

## 8. Asset Topology

Layer structure is identical:

- L1 — inner field
- L2 — meander ring
- L3 — owl body
- L4 — outer ring

### 8.1 Composite Definition

$$
N_{\text{meta}} = L_1 \oplus L_2 \oplus L_3 \oplus L_4
$$

---

## 9. Geometry

All geometric constraints are inherited from the normative standard.

No geometric transformation beyond σₕ is permitted.

---

## 10. Color Specification

### 10.1 Palette

- outer ring: #8C4191 (amethyst)
- owl: #8C4191 (amethyst)
- field: #1A1020 (deep violet-black)
- meander: unchanged (gold)

### 10.2 Color Doctrine

Amethyst is used to represent introspective clarity and cognitive distance from automatic perception.

### 10.3 Contrast Constraint

The owl must remain distinguishable from the field with sufficient luminance contrast, in line with WCAG 2.2 SC 1.4.11 (Non-text Contrast) ([WCAG 2.2](https://www.w3.org/TR/WCAG22/)).

### 10.4 Accessibility — Color Is Not the Only Carrier

From v1.3.0-rc onward (and unchanged in v2.0.0-rc) the system explicitly states that **color cannot be the only carrier of state identity**. The METACOGNITIVE state — like every state — must be perceptually recoverable from at least three independent visual channels:

1. **color** (amethyst / violet)
2. **orientation** (upside-down, right-facing)
3. **textual label and context** (the literal token `METACOGNITIVE` and the supporting math/quote tuple printed alongside the badge)

This triple-redundant encoding (color + orientation + label) is the project's mitigation for color vision deficiency (≈8% of males, ≈0.5% of females of Northern-European descent ([PMC global review, 12385717](https://pmc.ncbi.nlm.nih.gov/articles/PMC12385717/))) and for grayscale rendering. It satisfies the design intent of WCAG 2.2 SC 1.4.1 (Use of Color), which prohibits color from being the sole means of conveying information ([WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html)). Conformance is a design target; full empirical accessibility audit is a v1.4 objective.

The same accessibility rule applies to the CRITICAL state, whose red palette is intentionally low-contrast: redness alone never carries the CRITICAL identity — orientation (upside-down, left-facing) and the literal label `CRITICAL` are required.

---

## 11. Transparency and Alpha

Same as normative:

- RGBA required
- corner alpha = 0
- center alpha = 255

---

## 12. Provenance

### 12.1 Construction

Derived from normative by:

- horizontal reflection σₕ (vertical-axis inversion)
- controlled recoloring of field, owl, and outer ring

### 12.2 Transform Integrity

No additional transforms permitted.

---

## 13. Asset Invariants

### 13.1 Algebraic

- operator = σₕ
- determinant = -1

### 13.2 Visual

- inverted orientation
- right-facing

### 13.3 Structural

- geometry preserved
- meander unchanged

---

## 14. Integrity Regime

All assets must:

- pass SHA-3-512 verification
- be reproducible from layers

---

## 15. Interpretation Rules

### 15.1 Positive Rule

When present:

> **The observer audits the frame.**

The author or system has deliberately inverted the evaluative frame in order to inspect whether the process of perception, judgment, or analysis is itself filtering out something important. Thinking is examining its own frame.

### 15.2 Negative Rule

It does not imply alternative interpretation (NON-NORMATIVE) or adversarial critique (CRITICAL).

### 15.3 Deprecation Note

The earlier interpretive sentence *"This audits the standard"* is deprecated in v1.3.0-rc. It was insufficient because *"the standard"* read as an external object — the opposite of frame-audit. The canonical replacement is *"The observer audits the frame"* (normative voice) or *"Thinking examines its own frame"* (explanatory voice).

---

## 16. Non-Permitted Changes

- rotation
- horizontal reflection instead of vertical
- geometry alteration
- recoloring outside defined palette

---

## 17. Relationship to Other States

| State | Operator | Quote (v2.0.0-rc) |
| --- | --- | --- |
| NORMATIVE | I | "This is the standard." |
| NON-NORMATIVE | σᵥ | "This reflects the standard." |
| CRITICAL | C₂ | "This inverts the standard." |
| METACOGNITIVE | σₕ | **"The observer audits the frame."** |

---

## 18. Formal Definition

Let L₁–L₄ be the layer fields.

$$
N_{\text{meta}} = L_1 \oplus L_2 \oplus L_3 \oplus L_4
$$

with

$$
T = \sigma_h
$$

---

## 19. Closing Statement

The METACOGNITIVE owl is the mechanism by which the system inspects its own evaluative frame.

It ensures that analysis does not become trapped inside its own assumptions — that thinking can examine its own thinking before belief, challenge, or action.
