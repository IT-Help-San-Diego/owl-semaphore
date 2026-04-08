# Owl Semaphore

A finite algebra of epistemic states mapped into a constrained visual system.

## Overview

The Owl Semaphore is a formal epistemic notation system built from the Klein four-group:

$$
V_4 = \{I, \sigma_v, C_2, \sigma_h\}
$$

It defines four discrete states:

- **NORMATIVE** — identity
- **NON-NORMATIVE** — reflection
- **CRITICAL** — inversion
- **METACOGNITIVE** — frame inversion

This is not a branding exercise or a decorative badge library. It is a mathematically constrained system for representing epistemic position through invariant visual structure.

## Core Principle

The Owl Semaphore encodes **epistemic position**, not truth value.

It does not claim that a marked statement is correct. It specifies how that statement is being evaluated.

## Mathematical Foundation

The system is defined as the Klein four-group:

$$
V_4 = \{I, \sigma_v, C_2, \sigma_h\}
$$

with mappings:

| State | Operator | Mapping | Determinant |
|------|----------|---------|-------------|
| NORMATIVE | \(I\) | \((x,y)\mapsto(x,y)\) | +1 |
| NON-NORMATIVE | \(\sigma_v\) | \((x,y)\mapsto(-x,y)\) | -1 |
| CRITICAL | \(C_2\) | \((x,y)\mapsto(-x,-y)\) | +1 |
| METACOGNITIVE | \(\sigma_h\) | \((x,y)\mapsto(x,-y)\) | -1 |

The system is closed under composition. Each element is its own inverse.

## State vs Process

The four owls are **states**.

The measured ~31° rotation is **not** one of the four states. It is not an element of \(V_4\), is not closed under repeated composition, and is therefore treated as a **process operator** rather than a badge state.

In this framework:

- **states classify position**
- **processes move between positions**

## Repository Structure

```text
owl-semaphore/
├── OWL-SEMAPHORE-SYSTEM.md
├── OWL-1-NORMATIVE.md
├── OWL-2-NON-NORMATIVE.md
├── OWL-3-CRITICAL.md
├── OWL-4-METACOGNITIVE.md
├── INTEGRITY-MANIFEST.md
├── CITATION.cff
├── LICENSE
├── README.md
├── assets/
│   ├── masters/
│   ├── layers/
│   └── exports/
