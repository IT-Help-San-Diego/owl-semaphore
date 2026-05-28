

# OWL SEMAPHORE — INTEGRITY MANIFEST

## Version 2.0.1

> Stamped v2.0.1 for the corrective patch release. The structure is unchanged from v2.0.0: tracked specification files carry SHA-3-512 digests; the explanation document, CHANGELOG, regenerated PDFs, and assets are covered. Asset-record `TO_BE_COMPUTED` / `TO_BE_VERIFIED` markers for master / layer / export PNGs remain where measurement is still pending. The generated-hash block at the bottom of this file is overwritten by `scripts/update_manifest.py` from `RELEASE-HASHES.txt`; do not hand-edit it. The hand-edited `sha3_512:` values under §11.1 will be recomputed and replaced as part of `make hashes` + `make manifest` for v2.0.1 (the markdown content of the spec files changes only in version stamps where applicable).

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
  sha3_512: 6ad12fa6764a00e084871587a9eb8e44bf8a82b9476e5ee568d12ad080e01aadba209a4679657ce9ca6863019e79da15108ca4516db55c0b83ed448e0f04c99a
  status: WORKING
  notes: Root system specification (v2.0.1)

- path: OWL-1-NORMATIVE.md
  role: state specification
  state: NORMATIVE
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: I
  sha3_512: e6e4f4080013a7d39a5c18e1ef8a652f445f942033caed55a1e6ba27aea9cd460ca93c53b76ef959c6abd83f7c3476f67c42a971f5b8d00668e4e74ffaedb26b
  status: WORKING
  notes: Normative state specification (v2.0.1)

- path: OWL-2-NON-NORMATIVE.md
  role: state specification
  state: NON-NORMATIVE
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: σᵥ
  sha3_512: 7bbd6be9cbedfeee729cc4315da9c119f583f5bf7917cedaca305c99516344d6b08851eb62449331b76c3192ebb5e5522ccd53a165e17b5993bc757ec66d6d04
  status: WORKING
  notes: Non-normative state specification (v2.0.1)

- path: OWL-3-CRITICAL.md
  role: state specification
  state: CRITICAL
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: C₂
  sha3_512: 6ae4dee406c5036ac6f09abbf0027dbf08fc530e1ca472e66b3a18efc98cb5a3999984bc41d6a2c43645c42838a1a05c3238f1dd2b098a07a3242a37f1c7681b
  status: WORKING
  notes: Critical state specification (v2.0.1)

- path: OWL-4-METACOGNITIVE.md
  role: state specification
  state: METACOGNITIVE
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: σₕ
  sha3_512: f9a3b89a8186fc8021812365929ea95160b6ebb42bcc516e099022fb27b710ee23455a144693a3674dcd5898b5e43030e7adbbab5e90d4badccbd45ff7780877
  status: WORKING
  notes: Metacognitive state specification (v2.0.1) — phrasing "The observer audits the frame" carried over from v2.0.0

- path: README.md
  role: repository overview
  state: system
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: n/a
  sha3_512: e95475ffc9dd155ae6cf1cb1e1d01192c40007499560547589569a4ccd88bec81bedabcb2bb3825d05be017a7afb8bd4532f2dfc1de685bc5b7c42db1e5e8d13
  status: WORKING
  notes: Publication-facing repository overview (v2.0.1)

- path: CITATION.cff
  role: citation metadata
  state: system
  type: yaml
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: n/a
  sha3_512: a77849fbcc7e2efc098324fa2daf6b7a13f7393dc906c01a2e3dd186f2e361659c055c76f6cef289748c1559b3e5239d996969f0266d2a3f83858c4f98a6f49f
  status: WORKING
  notes: Citation metadata (v2.0.1); v2.0.1 version DOI 10.5281/zenodo.20419874; v2.0.0 version DOI 10.5281/zenodo.20418539 retained as previously published
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

## Generated Hash Records (v2.0.1)

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
OWL-SEMAPHORE-SYSTEM.pdf: c7dbf213551ba660a8cbeef96bd0df7657512d2f2b87d8cc9862f1c08513f54fabf85585de7be32683136724fae1d766af8a043979c5ae459e3c493046fcf384
OWL-SEMAPHORE-EXPLANATION.pdf: 24c36b8c115497d85158c435cc812e74534c35f98859f85625e26cde83ed730bf769592e1824e917ca576125766f18763e88aa123168676be7f0a052b0e9fe9a
OWL-1-NORMATIVE.pdf: d07d342470a5f6aa3af5c1e0a07fa11f10ce473a54604c7d660fb47b3394b38b2e0355f29443b605efc188c3eb678882a39b730da796578c82d2681f2e289767
OWL-2-NON-NORMATIVE.pdf: 5472e118f384caf2526a784b1a3ef839d98e9fd6eb74081d1785ef87aa962c4db684c5608cc3a8697c75277a154196109cf3636f8072e2cda9ff6ea90974ced5
OWL-3-CRITICAL.pdf: 4fe30bf11f2708d449f322e8e41e487a6e1c11a85f637f4000d95880100d0e62ea04272353f9aaa93032dd9193d7522579624037b6716beff598ece21dee6bf6
OWL-4-METACOGNITIVE.pdf: f3a95421e4baad48b5a3ac0c39cfd219c66516ba2d42eb7c31007660c838c360cf3d8e712d5cbfcfb335b538b3dca7ae46cc96a526ec7f6ead0d17728e29bd44
README.md: b9865c2364d6db4dd0992b6af2bbf2c500c3f24460e4983dd1916e37721bf23a8f96521de87ca12abedaba49e60e42411d1a70e670b6724170f08a032730b7cb
CHANGELOG.md: 1ab6b1026ba1b69688ba98515e48b6bb31582f3ed921d674ef718aba9938818c4a504e1586b070967f9cb73d432bf1a55cdfc27175cca32ed80aa376cbfd371c
OWL-SEMAPHORE-SYSTEM.md: 3b5282e724d3dda12a48c586125c92dc331efe813c295eb35f8654c1fdd5252194210ccfef331ce2f81e11fffdad4502666223cf227a9337fd961e67011bd022
OWL-SEMAPHORE-EXPLANATION.md: c232d801ff157f4371915ab601bff50ee928264f3724f8306f80b206497aecf57b582ecbf87800a67bce312bc43517d533daf748e6ea8dd4faf0e5f9eb776ec7
OWL-1-NORMATIVE.md: 69c10d14c79591b0df5eb9e8536341521f9925468f5008823c9474381c084c870af37753a72d6ba55c75c4565b21bdf271e1a456ec84bd616ea595ec4a651064
OWL-2-NON-NORMATIVE.md: 7bbd6be9cbedfeee729cc4315da9c119f583f5bf7917cedaca305c99516344d6b08851eb62449331b76c3192ebb5e5522ccd53a165e17b5993bc757ec66d6d04
OWL-3-CRITICAL.md: 31df97d38a6772e5f862afdca36c8dee0019957c431fbf568b04dc7b12d11d4e0a472de02ba29cdbdf0ea960af3db3e97fda613e930041631f8bd56e443d0954
OWL-4-METACOGNITIVE.md: 4db324abf16ebe2a188c3b673cff7844d3d4d3cbffd2a1a0d1771ebf67d88a9e4f71d22f91eca6280fc83c6e78cab0518eecaed8d856e3bc490f43839c694a8f
INTEGRITY-MANIFEST.md: d0c98eb1a2011a9d682e0582f9f2bfafff77a50fc5dcc10404cf8336c57249a7edca1d9bfd12bf667ffc5a4ecd6b3c5b1e006ea0ea186d1d910fd19882cf7606
CITATION.cff: c6075ae3e19a52f6b876c4ffa20d84806ba9f0ca6e5a4b47bf65bd78ab94fbebf3f60bf6a734c725ddf97b19a04ab01d4dfbd90cdc756369793af3871d6d1149
.zenodo.json: f4c890fb9effaee7c0a872f02d46be0fda5804c7de310ffef114aeba97279bc511772f66508b533d34afdebfdc674c9751f9b9260d7d68fecca3b20d627402b1
```

<!-- END GENERATED HASHES -->
