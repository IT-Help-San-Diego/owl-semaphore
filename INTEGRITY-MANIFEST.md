

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
  notes: Citation metadata (v2.0.0); v2.0.0 version DOI placeholder is TBD_BY_ZENODO_ON_RELEASE
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
OWL-SEMAPHORE-SYSTEM.pdf: aea9b03567bc38ff8feed2654c63ddbb91e6d3d42b32a4c48c513091b10d23e7f9cc46b4a2dc256e8cfcfeddfee444fb678276d133c0c9ecc24dff7d9c8cc42b
OWL-SEMAPHORE-EXPLANATION.pdf: 31d3fcdde52eff88c1368257752465a9ab9887fa2b3d6a41412e0567dfe11c35da4fbf7c8ae442bcc4513d02405e12b7092c397dcc7afc7e925c0360c611b2bf
OWL-1-NORMATIVE.pdf: 3a0a6e07692d0cb7dc54a7baad07fe0eed7d376534e2e7ffed5f0dde6375305d14704775c1e772b19c2abfca254d747b96b0f7a1e516d0ff3bcf89feaadaa026
OWL-2-NON-NORMATIVE.pdf: 37bacfdbb437d10f759de9fec7112853ffb7b2ce894572218ad80eae4cad1b633a06c07bcc8471e695e43c55871afa71aacfd43c1f2eeecea14e6e2b446c4448
OWL-3-CRITICAL.pdf: a5d9c9e16926edea2649d44b8501f9f98e63e788f9934c496adf5565cbf9ffe07492dc10b1541d23dfd4bc94464b3d2cf42f31bce0dcf885ca97ed0300fd3c6a
OWL-4-METACOGNITIVE.pdf: 5ac63c17ee8f92aa93f7587ee2c61d26834aa4de6c0fc68eec66966364147fc8c0aba5b16badf7efe4e8021e122a4c628c8b958a90d9d0197b08b285be86bd7b
README.md: b690554b80b61b3c5c78397f0bc517804576b2b6b1a53577d5a7497cbc6766d2f93388eb112750e07aa11e63ddda84e14f95ef60a10c2c0135a98b1b96ea165e
CHANGELOG.md: e5d3d6b601dc2a3750a4d880b6f5d548e07e719378b370404768d465356e20573799ca9cd123fe12678f852aa8ef3463bb6efca5dc69549bab2c0c19f9b32653
OWL-SEMAPHORE-SYSTEM.md: f78b69999932b6410a26deb7abea4baa6dc0a330240d7adb3f7dec7e3ed74bd28dc8e48bc8fb4faea67edab3bf50564cd9ad10b81e54819bb0a6851b5cc3c751
OWL-SEMAPHORE-EXPLANATION.md: 86c3cc779bd3d907c49cc974a349e653f96b3001df9fe08d60487a5e0b7b4c03c1b2b8a910a0bd84ad0d2d0d85cd082260cd6b1abcb33bd6726b7408cab9c642
OWL-1-NORMATIVE.md: 0a894da03254879096bcc960cf87a328683b78939212e03656a449c21906062eed3549627344e964222813c8e667e7d0f384998cf7fce5d3115d190c99f9dfdc
OWL-2-NON-NORMATIVE.md: 5a9febe50a2fd6de5b5e17191cf8392e5ee8adcba42b478468ba739ae4f7c0b5d9fce8904dd323761b3f0dccd175b553ef583db73a20c34149f8eeb936932058
OWL-3-CRITICAL.md: a17efb26668581ef4deac8ec9458eb4947822b6604d33f25bf0887cf62b34cc10a1b1ed2e266ef6c8a823642e60619f673e8dc5ec7b8715968cf545f32b3a3a1
OWL-4-METACOGNITIVE.md: 8d81182931cde841f9633d669cc9a4caa2923ae381212349e9962c2bda88b46cd915996bd6b0f22066871b248b91aec0a5d1e7f1a60e1a9e9d95d7c134f34aa2
INTEGRITY-MANIFEST.md: 7f3cff27d9280f584232f760d2c14735d0c1be920514855b439d57d822c18066d57b5fb0306bfe4d4d8f881f51f934fb5ff56fd9da9c83499771cf1313fdfe47
CITATION.cff: 2eed4ae60c08ef9529b952966f1511b9fd893af3b612371844a6611d98ef6a2ea570e1d72e5323243ec458575d016c1b442c4626b6473014af2ef26723887105
.zenodo.json: 04058aa2b188e2327ec4cac457b2af5d2f0d4acccd0847c7d3ad644b804d8226e4f78c371f74ce6c2e54f90adb85b0d5d47ced781262591ab3fc81788e5d8ae9
```

<!-- END GENERATED HASHES -->
