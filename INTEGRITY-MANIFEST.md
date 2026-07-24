

# OWL SEMAPHORE — INTEGRITY MANIFEST

## Version 3.0.0

> Stamped v3.0.0 for the structural and scientific remediation release. The integrity regime is unchanged from v2.0.2: tracked specification files carry SHA-3-512 digests; the explanation document, CHANGELOG, regenerated PDFs, and assets are covered. The asset-record markers under §11.2 for master / layer / export PNGs are carried forward unchanged from the v2.0.2 manifest; the canonical asset set under `assets/` is unchanged for v3.0.0 (this release alters specification text and metadata, not artwork). All hash values in this file derive from a single generated source: `scripts/compute_hashes.py` writes `RELEASE-HASHES.txt`, and `scripts/update_manifest.py` rewrites both the generated-hash block at the bottom of this file and the `sha3_512:` values in the §11.1 records from it. Do not hand-edit either; run `make hashes` + `make manifest` after any change to a tracked file.

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

The `sha3_512:` values in the records below are rewritten by `scripts/update_manifest.py` from `RELEASE-HASHES.txt` (single source of truth); do not hand-edit them.

```text
- path: OWL-SEMAPHORE-SYSTEM.md
  role: system specification
  state: system
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: n/a
  sha3_512: 027ebc1c0073d183cd532ba0665e6abf9053ffc3f6d00b8cbb1223d78250bd670dd162716a3192ea2bce84768fddb7dea3a6e5d0925cc6cd53dc2fcf4f7a6bd2
  status: WORKING
  notes: Root system specification (v3.0.0)

- path: OWL-1-NORMATIVE.md
  role: state specification
  state: NORMATIVE
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: I
  sha3_512: 2436367ff85abfc83a95520f5e511bafb70f5157a852f1bfdd07b318d6b561bfeee98a70faa45bb7cb6b95bb4e7b6ac218b6f628aefef7af297f254539e0585c
  status: WORKING
  notes: Normative state specification (v3.0.0)

- path: OWL-2-NON-NORMATIVE.md
  role: state specification
  state: NON-NORMATIVE
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: σᵥ
  sha3_512: 1cd4199c888ae2866a83c53191542ffff5a4ecb64807c854d304245cc61475f9b653c9d9b161f23d63445a09e4b79ab5139dd8603d6781d5311f110e641f8a62
  status: WORKING
  notes: Non-normative state specification (v3.0.0)

- path: OWL-3-CRITICAL.md
  role: state specification
  state: CRITICAL
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: C₂
  sha3_512: 48eb3b3520fa38241ca20afe5af480841fa18f9bdbf3dc95a16d32e0aad208b7a565ae53f3d96b91f7a8aee92e736ccfbf34d9db4f8142e13ac959bad1b2bb71
  status: WORKING
  notes: Critical state specification (v3.0.0)

- path: OWL-4-METACOGNITIVE.md
  role: state specification
  state: METACOGNITIVE
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: σₕ
  sha3_512: 30dcfe35c1030cae25ee395d94911cae9357628b8de0e660eaaf951173d3120b87aea034ee1464b682f8bbb5ec5bc30db10b7d460e6bed8a81201c12e7e3f52f
  status: WORKING
  notes: Metacognitive state specification (v3.0.0) — phrasing "The observer audits the frame" carried over from v2.0.0

- path: README.md
  role: repository overview
  state: system
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: n/a
  sha3_512: b23fd7c82421c44f6ced85e6a611efbd5970f4bd0f2cf8196ad71a89e39c555d888f848f1a33d6f1a5545c9de38af7cf6e07c60f370da55b19cd0257ee9430f7
  status: WORKING
  notes: Publication-facing repository overview (v3.0.0)

- path: CITATION.cff
  role: citation metadata
  state: system
  type: yaml
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: n/a
  sha3_512: 9f354c41d7f80ec8bba8bebee8cd53c10d6937c8a9f4db8303298e9c3147ecc6a43e2214d122197ab389bcd085a4a0266d6e9dcc1aa86738871efaf1b7b61e62
  status: WORKING
  notes: Citation metadata (v3.0.0); cites the v3.0.0 version-specific DOI 10.5281/zenodo.20468727 (published on Zenodo 2026-05-31) as the citing DOI; concept DOI 10.5281/zenodo.19473697 (all-versions; resolves to latest published version) retained as the cross-version citation target; v2.0.2 version DOI 10.5281/zenodo.20433053 retained as previous published; v2.0.1 version DOI 10.5281/zenodo.20419874 and v2.0.0 version DOI 10.5281/zenodo.20418539 retained as earlier published
```

### 11.2 Asset Records

Finalized asset records are added here, one entry per asset, using the canonical record format defined in §10. Each entry records the concrete measurements (`dimensions`, `mode`, `alpha_status`, `transform_class`) and the SHA-3-512 digest of the asset file, with a one-line `notes` field describing the asset's role in the release. Entries are added as assets are frozen and hashed; the v3.0.0 release does not introduce new asset entries because the asset set under `assets/` is unchanged from v2.0.2.

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

<!-- BEGIN GENERATED HASHES -->

## Generated Hash Records (v3.0.0)

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
OWL-SEMAPHORE-SYSTEM.pdf: 6d56d81d8a3c3071c18e433074908e93b28962cae323e0d1dceed0a0fa4e5438de724e6288c84e26efe2104019949a6f70f39928c1fc0586f2104ad815e62960
OWL-SEMAPHORE-EXPLANATION.pdf: 4eec0d609d3577ffbee9a3fcb3009321ff6d8b4b6aa2a706193252b19a6725627391c36620f07e9e619110782eafebe3545b77736529b5fd2705e4533787c6f4
OWL-1-NORMATIVE.pdf: f6a04ebd61e4d0e965d75cbac0b9da9d342121e7f67603b671a6d788cdca169beb64f6883176e50e33287d1ac6674306d2dab4d459bd2a2a6b4fbf5f631b4168
OWL-2-NON-NORMATIVE.pdf: 8e266c03e5d2ef95693c164f01e9127a2f2ba84d8b3c2a66f169616a2dcb903df3b39c1dd4dd26c43daf5d210a3e06e9dba654c9d3f164a9cfd38ef92f32a359
OWL-3-CRITICAL.pdf: e1c76f485e0f11d44bb58605c2cdd7c1ff77307193742f9aed83c8541d83a2df588d7d7432826aa9699de82e4a3558c01dcdb0f98dfbdcd814300ff589b86cf0
OWL-4-METACOGNITIVE.pdf: f39b1cdb9111873429207cda6b64b1ad0a3feb5deea2d56f6f9fda31c0fdeed5b922ed1b30f22c9488bfd92721cee0ceb8d1a94e4653e8822471d008e34a0833
README.md: b23fd7c82421c44f6ced85e6a611efbd5970f4bd0f2cf8196ad71a89e39c555d888f848f1a33d6f1a5545c9de38af7cf6e07c60f370da55b19cd0257ee9430f7
CHANGELOG.md: 1f75e9842cedb30237900691f9c18cde174c116bd2d58a93cc0fabac904452373da7ca801435f63cf0ceb34806da6dbf2d09380e3d1692d1e9213839f87b8328
OWL-SEMAPHORE-SYSTEM.md: 027ebc1c0073d183cd532ba0665e6abf9053ffc3f6d00b8cbb1223d78250bd670dd162716a3192ea2bce84768fddb7dea3a6e5d0925cc6cd53dc2fcf4f7a6bd2
OWL-SEMAPHORE-EXPLANATION.md: dcb4dd90e8eb2541db980ffd93fe8f612b73fe2a5aff9b9adc4502106b1ade6cef80b66b94e05f3ffffa7ce9a32c7a1b457864e6397fd09351a5882264fdf829
OWL-1-NORMATIVE.md: 2436367ff85abfc83a95520f5e511bafb70f5157a852f1bfdd07b318d6b561bfeee98a70faa45bb7cb6b95bb4e7b6ac218b6f628aefef7af297f254539e0585c
OWL-2-NON-NORMATIVE.md: 1cd4199c888ae2866a83c53191542ffff5a4ecb64807c854d304245cc61475f9b653c9d9b161f23d63445a09e4b79ab5139dd8603d6781d5311f110e641f8a62
OWL-3-CRITICAL.md: 48eb3b3520fa38241ca20afe5af480841fa18f9bdbf3dc95a16d32e0aad208b7a565ae53f3d96b91f7a8aee92e736ccfbf34d9db4f8142e13ac959bad1b2bb71
OWL-4-METACOGNITIVE.md: 30dcfe35c1030cae25ee395d94911cae9357628b8de0e660eaaf951173d3120b87aea034ee1464b682f8bbb5ec5bc30db10b7d460e6bed8a81201c12e7e3f52f
INTEGRITY-MANIFEST.md: 45a27fa80bff938679dadc919d92c84b77bbb2b1683def014f132aceb8ab9885ee7ddd2822d8c88039132290f01a42d578639c6e2f35098304163ada82026249
CITATION.cff: 9f354c41d7f80ec8bba8bebee8cd53c10d6937c8a9f4db8303298e9c3147ecc6a43e2214d122197ab389bcd085a4a0266d6e9dcc1aa86738871efaf1b7b61e62
.zenodo.json: 7b4eb61dcb8dfa7e64f3784f4889450d4a00f7cb37a978038931c35f50a9d8b7b52630a44e4fc0c60fff5f313a02f3c2a518e573202844aa2a29e321107f0cf6
```

<!-- END GENERATED HASHES -->
