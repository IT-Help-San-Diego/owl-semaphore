

# OWL SEMAPHORE — INTEGRITY MANIFEST

## Version 2.0.0

> The previous publication of this manifest was stamped v1.2.0. In v2.0.0 the manifest is extended to cover the new explanation document and CHANGELOG, the regenerated PDFs, and to replace `TO_BE_COMPUTED` placeholders for tracked specification files with their SHA-3-512 digests. Asset-record `TO_BE_COMPUTED` / `TO_BE_VERIFIED` markers for master / layer / export PNGs remain where measurement is still pending. The generated-hash block at the bottom of this file is overwritten by `scripts/update_manifest.py` from `RELEASE-HASHES.txt`; do not hand-edit it.

---

## 1. Purpose

This document defines the integrity regime for the Owl Semaphore repository.

Its purpose is to make the repository auditable, reproducible, and resistant to silent drift. No asset, specification, export, or derived file is to be treated as authoritative merely because it looks correct. Authority requires verification.

This manifest exists to record:

- file identity
- file role
- transform class
- transparency claims
- cryptographic hash values
- verification procedures
- failure conditions

---

## 2. Integrity Doctrine

The Owl Semaphore is a constrained epistemic system. Its visual and textual artifacts therefore require the same treatment as any other standards-bound technical asset.

The governing principle is simple:

> A file is not canonical because it appears correct. It is canonical because it verifies against the system’s declared invariants.

For this reason, integrity is evaluated along four axes:

1. structural correctness
2. transform correctness
3. transparency correctness
4. cryptographic identity

---

## 3. Integrity Scope

This manifest applies to the following categories of repository content:

### 3.1 Specification Documents

- `OWL-SEMAPHORE-SYSTEM.md`
- `OWL-1-NORMATIVE.md`
- `OWL-2-NON-NORMATIVE.md`
- `OWL-3-CRITICAL.md`
- `OWL-4-METACOGNITIVE.md`
- `README.md`
- `CITATION.cff`

### 3.2 Asset Files

All files under:

- `assets/masters/`
- `assets/layers/`
- `assets/exports/`

### 3.3 Validation and Publication Files

- `INTEGRITY-MANIFEST.md`
- `CHANGELOG.md`
- `OWL-SEMAPHORE-EXPLANATION.md`
- generated PDFs (`OWL-SEMAPHORE-SYSTEM.pdf`, `OWL-SEMAPHORE-EXPLANATION.pdf`, and `OWL-{1,2,3,4}-*.pdf`)
- `RELEASE-HASHES.txt`
- `.zenodo.json`
- `CITATION.cff`
- validation reports
- release notes
- DOI metadata outputs

---

## 4. Hash Standard

### 4.1 Algorithm

The canonical hash algorithm for this repository is:

**SHA-3-512**

### 4.2 Rationale

SHA-3-512 is used because it provides strong cryptographic identity checking and aligns with the project’s requirement for explicit, modern integrity controls.

### 4.3 Canonical Verification Command

```bash
openssl dgst -sha3-512 <filename>
```

### 4.4 Directory Verification Example

```bash
find . -type f \
  ! -path './.git/*' \
  ! -path './.DS_Store' \
  -exec openssl dgst -sha3-512 {} \;
```

---

## 5. Transparency Integrity Rules

For any file labeled or published as transparent, the following conditions must hold:

- image mode must support alpha
- corner alpha values must equal 0
- the composited badge center must be fully opaque where the design requires it
- transparency may not be simulated by placing an RGB image on a neutral background and calling it transparent

### 5.1 Canonical Transparency Conditions

For canonical transparent composite badge files:

- mode = RGBA
- corner alpha = 0
- center alpha = 255

### 5.2 Failure Condition

Any file that claims transparency while lacking actual alpha information fails integrity review.

---

## 6. Transform Integrity Rules

The Owl Semaphore is defined by the Klein four-group:

$$
V_4 = \{I, \sigma_v, C_2, \sigma_h\}
$$

Each owl state must verify against its correct transform class.

### 6.1 Canonical State Map

| State | Operator | Required Orientation |
|------|----------|----------------------|
| NORMATIVE | I | upright, right-facing |
| NON-NORMATIVE | σᵥ | upright, left-facing |
| CRITICAL | C₂ | upside down, left-facing |
| METACOGNITIVE | σₕ | upside down, right-facing |

### 6.2 Failure Condition

Any file whose rendered orientation does not match its assigned operator fails integrity review.

### 6.3 State vs Process

The measured ~31° rotation does not belong to the canonical state system and must not be treated as a fifth badge state.

It is a process operator, not an integrity-valid state assignment.

---

## 7. Geometry Integrity Rules

All four states must preserve the shared geometric architecture of the system.

### 7.1 Shared Invariants

The following must remain invariant across all canonical owl states:

- common image center
- common outer ring geometry
- common meander ring geometry
- common annular structure
- common layer model

### 7.2 Failure Conditions

A file fails geometry integrity if any of the following occur:

- off-center placement
- scaling drift
- ring thickness drift
- meander deformation
- arbitrary translation
- undocumented cropping that changes the canonical structure

---

## 8. State-Specific Integrity Conditions

### 8.1 NORMATIVE

Must satisfy:

- identity transform only
- upright orientation
- right-facing owl
- normative gold / near-black palette
- no reflection
- no rotation

### 8.2 NON-NORMATIVE

Must satisfy:

- exact horizontal reflection relative to normative
- upright orientation
- left-facing owl
- teal / cool gray palette
- no 180° rotation

### 8.3 CRITICAL

Must satisfy:

- exact 180° rotation relative to normative
- upside-down orientation
- left-facing owl
- red / warm red palette
- clipping rule preserved if applied in the canonical asset set

### 8.4 METACOGNITIVE

Must satisfy:

- exact vertical reflection relative to normative
- upside-down orientation
- right-facing owl
- amethyst / deep violet-black palette
- meander preserved

---

## 9. Specification Document Integrity

The repository’s specification files are part of the canonical system and therefore require structural integrity checking.

### 9.1 Minimum Conditions

Each specification document must preserve:

- complete heading hierarchy
- non-truncated lists
- mathematically correct operator assignments
- non-conflated epistemic roles
- consistent terminology across the full repository

### 9.2 Failure Conditions

A specification document fails integrity if it contains:

- broken section structure
- truncated checklists
- inconsistent operator mapping
- state/process conflation
- conflicting color doctrine
- conflicting geometry claims

---

## 10. Canonical File Record Format

The canonical per-file record format for this manifest is:

```text
- path:
- role:
- state:
- type:
- dimensions:
- mode:
- alpha_status:
- transform_class:
- sha3_512:
- status:
- notes:
```

### 10.1 Status Values

Permitted values:

- `LOCKED`
- `VERIFIED`
- `WORKING`
- `SUPERSEDED`

---

## 11. Initial Record Sections

Populate the following sections as files are finalized.

### 11.1 Root Specifications

```text
- path: OWL-SEMAPHORE-SYSTEM.md
  role: system specification
  state: system
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: n/a
  sha3_512: 798b524ff54461dad72eef3d10494485bf3eadfcaa7d8628754c870b3481696ca6ca6abac42b46b14cbd41cd7e32ec6e3350192a0d84b4959dd476edfa44832f
  status: WORKING
  notes: Root system specification (v2.0.0)

- path: OWL-1-NORMATIVE.md
  role: state specification
  state: NORMATIVE
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: I
  sha3_512: b67014fc3ed0df4645fed579ea77153ca056acd9f00bae5dcffbd5f2f77a5e96850b61a69aea80827da2509bc0465f52ad02cbe5cbaa58baa339ba67471ff16f
  status: WORKING
  notes: Normative state specification (v2.0.0)

- path: OWL-2-NON-NORMATIVE.md
  role: state specification
  state: NON-NORMATIVE
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: σᵥ
  sha3_512: 9b2bc691221ffda598caf3ab0819e47126f9542eae7c6df5867773484f3e050609a66e95fb215e7df58b40e23a747dcf833596a4ac80bd9cf1d822a3a3801678
  status: WORKING
  notes: Non-normative state specification (v2.0.0)

- path: OWL-3-CRITICAL.md
  role: state specification
  state: CRITICAL
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: C₂
  sha3_512: 177588a9116cd176d4b34e27b9b09b6af076e958188ab73e6144e144b77a387a140efd5025997109a49f8d4b3d1f5b8176a113020a8ececb6960e4ffc5ebe516
  status: WORKING
  notes: Critical state specification (v2.0.0)

- path: OWL-4-METACOGNITIVE.md
  role: state specification
  state: METACOGNITIVE
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: σₕ
  sha3_512: d90010f35968714b306747be0e78abf8fc4f0d6be599911c8848062001a7983bd1045b47daa465ea24f1380b59dbc99c0e8bb734395cabc52687a9c50172082d
  status: WORKING
  notes: Metacognitive state specification (v2.0.0) — phrasing refined to "The observer audits the frame"

- path: README.md
  role: repository overview
  state: system
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: n/a
  sha3_512: cd8ccbb5aa07774a2c0f4fdf40042f0e170c810e1e74373097ca8a10b72d53ba67b80b4bc4bda6c1fae56f678f7601c89334561a268c80ad455cb3884013edeb
  status: WORKING
  notes: Publication-facing repository overview (v2.0.0)

- path: CITATION.cff
  role: citation metadata
  state: system
  type: yaml
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: n/a
  sha3_512: 1e88d215c57611f13d3515a8214ca1dff442ed1b0cd6548a8af4d58900f347635e5d144ae3638becf2bfdbed580c5301187d33f24dac5b2859659a861b1d4d9a
  status: WORKING
  notes: Citation metadata (v2.0.0); v2.0.0 version DOI 10.5281/zenodo.20418539
```

### 11.2 Asset Records

Add finalized asset records here using the same format once the masters, layers, and exports are frozen and hashed.

```text
- path: assets/masters/...
  role: master asset
  state: ...
  type: image
  dimensions: TO_BE_MEASURED
  mode: TO_BE_MEASURED
  alpha_status: TO_BE_VERIFIED
  transform_class: TO_BE_VERIFIED
  sha3_512: TO_BE_COMPUTED
  status: WORKING
  notes: pending validation
```

---

## 12. Validation Procedure

### 12.1 Order of Operations

1. confirm required files exist
2. validate specification structure
3. validate image dimensions and modes
4. validate orientation and transform class
5. validate geometry invariants
6. validate alpha integrity
7. compute SHA-3-512 hashes
8. record values in this manifest
9. mark validated files as `VERIFIED` or `LOCKED`

### 12.2 Strict Release Rule

No file may be promoted to release status until all applicable integrity checks pass.

---

## 13. Release Integrity Policy

Before any tagged public release:

- all root documents must be complete
- all canonical assets must be validated
- all published hashes must be current
- `CITATION.cff` must reflect the release version
- Zenodo metadata must match repository state

---

## 14. Misuse and Drift Policy

This repository is especially vulnerable to silent semantic drift if assets are treated as design variants instead of constrained epistemic states.

The following are considered integrity violations even when they appear visually subtle:

- arbitrary recoloring
- transform substitution
- state/process conflation
- geometry drift
- silent asset replacement
- undocumented semantic reassignment

---

## 15. Closing Statement

The Owl Semaphore is not a decorative icon set. It is a formal system. Its files therefore require formal verification.

This manifest is the repository’s integrity backbone.

If a file cannot be verified, it does not become canonical by familiarity, convenience, or visual plausibility.

It becomes canonical only by passing the constraints defined here.
## METACOGNITIVE STANDARD (ADDED)

META-composite-white-540.png
SHA3-512: 0df765966512a4d48f50b1aefa029403c357924f01c3e2802e7930d82b6521028aa0a9a65ff721b7be59f6e11f1bd52a03b091eaa0715d4bc7d0aea04d46c10f

META-composite-dark-540.png
SHA3-512: 8b2e2bd0a7d2d7958a5e152c576e5f9ec4eff63483e40c4a7c48118b011a5750c80345c1b80f9cd8e0cf4b2b2e1c1199d062c3f873155e134de5bfb68f08bbc4

META-composite-transparent-540.png
SHA3-512: 140c7b67ca5c2d6e3cfcaa8faecaeb81517a1c47e447c888cf55b0d88d27b7f23cd932570b80309147101039866f3a7578e393d378ac8c5db8d3b2046deaf8e9

<!-- BEGIN GENERATED HASHES -->

## Generated Hash Records (v2.0.0)

The block below is regenerated by `scripts/update_manifest.py` from
`RELEASE-HASHES.txt`. Do not hand-edit between the markers.

```text
assets/releases/540/CRIT-composite-dark-540.png: e6ab81b30a7ea1dd0db79b851181d60bb3608524be57038079e144c6e9d2c9473b3e4c8fcd2974845292a5e8f978c147bec9767528af2ba58178e37ad275061c
assets/releases/540/CRIT-composite-transparent-540.png: da42dd3a690f97dae0f5fa316692d9a218b7f7540b72018cde9f5262dab2bae0eed9f6f4b9598fbbcac12d85e4d9502433806941d72434a611c41c4f349ad051
assets/releases/540/CRIT-composite-white-540.png: 9427afafd2d2a182a9a2d3fc34861182356caafd0f4b3d720160ddceb4bcf4243da7ba56183efee4971f8756cc4c1280272ee7614146f0b516949c40b706b57c
assets/releases/540/META-composite-dark-540.png: c8024e53b3f284ed37601c6099bd566593e0ba8d40c8381a00c2070843a53b5c36e5f007ad6b8c7467233ce3d07fd0a426169ced7feb8bd61cc53ec56f007450
assets/releases/540/META-composite-transparent-540.png: 59b66aba7a731b7b0618a3d6eb79134478f1837569679fa630433006c6c5fabd99a3a7cc18679ab73b77e6ece8a970930815879113e05ce1f94aa214d0a0d8dc
assets/releases/540/META-composite-white-540.png: 354e47230a19f4b2e3e8bcdc0dcc4b0f347c75d1f55748d3cf0adc1524c0014dafa908fbf0444b1f9a41b020a2694bdaad591835c83c690eeecef0845d883289
assets/releases/540/NONNORM-composite-dark-540.png: 232e079c78ffe7fe778a914930ec79192b53096c856c0d89ff092b11e278f77c3e9267e4e720abd82295d708f9ef0afcfeef7701c6bb78deeb1975deeddc8b1c
assets/releases/540/NONNORM-composite-transparent-540.png: fd5e0fbf3298393079d35c417f6ed3eaf8bf4e3ee5111c57e68a3e161764b502964bb66b0ddd0da5ec7a41a27deb01aa93032f1aee30fd5f4537d6a17331607f
assets/releases/540/NONNORM-composite-white-540.png: 7ef0e888ff009aff3fc0bbde3d7246cb659262ff5ee67e8fa2368561444e42c06bf951c24c9b5f0cf0314712c65de62283b65092b2ff8f05c7d31b45a1b8f2f1
assets/releases/540/NORM-composite-dark-540.png: 95b34b154ac026c966eb039041b3c83a1e3da4da8321d99c2c6ba885d7225a11a022a202993383cb99477db8b98f48e2bda1a833ff2b8ca882cb2108cea0ec11
assets/releases/540/NORM-composite-transparent-540.png: e7447d169d2980ae1cd1ecaf50e4cefddfc1798ed018e08a8b865f2bb12d32ed5a1114e54bfb79cd9bacb39589a65053c9b34c2e5e7b25df4d94fc9547c20587
assets/releases/540/NORM-composite-white-540.png: d2a24e049ae0fe0531fe19973a4ac6456291beb951565eab0dd61746b298a91bd8b5bc151983abb8a803b42af73d41bb7e26ac418fd921fdbacb12fa8ce212a5
OWL-SEMAPHORE-SYSTEM.pdf: fd11408d8a700d51df7ac691edc1fe9c09079178c43366fc2020e883839b8d6c46167ee1cca2d5631e1fdec9b318b8f3153a6b296e5690b38577202a1bc0039d
OWL-SEMAPHORE-EXPLANATION.pdf: 85c7703646f94d8b40460c5fa24006d770e676246ed830999d2e23f41cbdfd2498b00b918d1e12fb71cfe0cb8a9e4b1d0c56f5713c834e14ef25caf6fece2bfc
OWL-1-NORMATIVE.pdf: 070e75e7b2290d766f076f0007decae4b8d69c399079a6033563e5e8149893e983e732dfa03f2ab57684204b81c88e23bdd6f2abac8badd0a5323f8d6fb3e16d
OWL-2-NON-NORMATIVE.pdf: b5253cf62da0821dae86f500de8a42c95a9722b81f9d6fb4b7e92370ae96e76658cf764ce19967faaebba29a1be1bd4c5294e94e039bc8645b687a31248ea53c
OWL-3-CRITICAL.pdf: 0e821b80802a62b23edc7fb63edee46b86a4f561089f6af12915fd89ec22eda887736b98274216b56843a3861847b8c25721f7bb4cf3713e7be08b2dbecb5aa8
OWL-4-METACOGNITIVE.pdf: 0ac6ee3f3b965ad341fa184e982e57868e0d88462a8133a340273b2744d984de81b62ef33ea5554439d089e3b403fbf6a59dd3c70155dc2eb3b44fb6fc193694
README.md: 399b7cf59b1147b7ebd072d03b0835459cbbc8a3ce35fbc6be300678f97cdcf7dd6743694cbe9da8c15384d828bf6b29a2d264815e98702ccca2266f95f56bed
CHANGELOG.md: 682d73b8aa1160d0cf2d8e314986b43413fd118cb857e70c6a8be968f287563b20ed551f63b6d3aeb40538f87ff2310135bb6a8e25dea9d6fb35d9e897789c32
OWL-SEMAPHORE-SYSTEM.md: 822417a3c5c68b148e697024a5d31599b154df4f1d9961447c2b405563c8efb27991376595231b99846cdb422c899d561e888014ced2c3c23a56ce29556a5140
OWL-SEMAPHORE-EXPLANATION.md: dceda72445a9711302ee54824fbfd4bbee593459ecdb8d74e122b4d0fc48e543dbb3529bc3ee395c23dfe27d5112f3b5b54754c526300f1e9d116fe90e0c143e
OWL-1-NORMATIVE.md: 75015453b652112278808525012f8a3cd7c17ce3d2d7deb1190cd6d8c8fe9f90c5b72410b1d4a2a6f4b295d941049cdbcf28a9d31c058ad032ee162aa0c398bd
OWL-2-NON-NORMATIVE.md: 52d2f2a232c0adb2f2df1518296e59ac3da89a44be29de470c2a5608bab2072a32f6e8aea8744fc2f0227d1e8e4e0c1582043896afb4af9ed1299270d5f98a6f
OWL-3-CRITICAL.md: 6e5736ee4143168f7ee542302c6750cdb983e540be3b6a4998289242450525476aee9e42fd4f2b6cb337039710ed8d80f8d0c8ffc4d39de26dbd57d102a601c4
OWL-4-METACOGNITIVE.md: 11e6dff8d0c316bc7b65b5d060caf3d3684f8eb134f84e41e609381fafc4cb559246da8fb23f066637e58bfebfee94a464a1c503f11986374883e6628da12842
INTEGRITY-MANIFEST.md: 4ad2a72e92572548d4e66141ee724fbf874641e2ced1a86ef7100b22518b73bdfa8767f93cf64023b7a40af714c54b272344301f1a9dc17d0519d746d2f96b83
CITATION.cff: aa23db7ef3aecb26ac0ca23eb405eea5c9eb04889342df9cad2efb3921b2ee07fafe20dbd85c9d503f0dbfa42bcf860ed0c1f8f9c21cae961b13a0a56bbdde0f
.zenodo.json: ad103dbd63799be5393b3e21edbba6ed0707b1b947e78ca4862038f4c704175b78c1faa3fda7fa7072f22519eb0b4f022b32f507586ebca887ef5d00cae03d80
```

<!-- END GENERATED HASHES -->
