# Owl Semaphore — Validation Script Specification

## Purpose

Define a validator that checks Owl Semaphore assets for transform correctness, geometry preservation, alpha integrity, and cryptographic consistency.

## Scope

The validator must inspect:

- exported PNGs
- master TIFF files
- layer PNGs
- integrity manifest records

## Required Checks

### 1. File Presence
Confirm required files exist for all four states.

### 2. Image Properties
For each PNG/TIFF-derived raster target:

- width
- height
- mode
- alpha presence
- center pixel alpha
- corner pixel alpha

### 3. Orientation Validation
Expected orientations:

| State | Expected Orientation |
|------|----------------------|
| NORMATIVE | upright, faces right |
| NON-NORMATIVE | upright, faces left |
| CRITICAL | upside down, faces left |
| METACOGNITIVE | upside down, faces right |

### 4. Transform Validation
Using NORMATIVE as canonical source:

- NON-NORMATIVE must equal horizontal reflection of normative
- CRITICAL must equal 180° rotation of normative
- METACOGNITIVE must equal vertical reflection of normative

The validator should compare pixel outputs after transform normalization.

### 5. Geometry Validation
Confirm invariant geometry:

- shared center
- identical outer ring bounds
- identical meander ring bounds
- no scaling drift
- no translation drift

### 6. Layer Validation
Confirm layer count and roles:

- L1 inner field
- L2 meander ring
- L3 owl body
- L4 outer ring

### 7. State-Specific Rules

#### NORMATIVE
- no transform
- gold/black palette
- identity orientation

#### NON-NORMATIVE
- horizontal mirror only
- teal/cool gray palette

#### CRITICAL
- 180° rotation
- red palette
- clipping rule enforced if canonical asset set includes clipped owl variant

#### METACOGNITIVE
- vertical reflection
- amethyst/violet-black palette
- meander unchanged

### 8. Alpha Integrity
Confirm:

- RGBA mode where transparency is claimed
- corner alpha = 0
- center alpha = 255 for composite badges
- no fake transparency in RGB-only files labeled transparent

### 9. Hash Validation
Compute SHA-3-512 for all tracked files and compare against `INTEGRITY-MANIFEST.md`.

## Output

The validator should generate:

- pass/fail summary
- per-file report
- per-state report
- hash report
- transform mismatch report
- geometry mismatch report

## Recommended CLI

```bash
python validate_owl_semaphore.py --root .

--update-manifest
--strict
--json-report