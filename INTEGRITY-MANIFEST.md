

# OWL SEMAPHORE — INTEGRITY MANIFEST

## Version 2.0.0-rc (release candidate)

> v2.0.0-rc extends the integrity manifest scope to cover the v2 authoritative
> asset set under `assets/v2/` (the owl-only PNG lineage with the human-selected
> gold branch / olive heritage marker), the multi-page TIFF masters under
> `assets/v2/masters/`, and the new doctrine + provenance documents
> (`ASSET-DOCTRINE.md`, `PROVENANCE.md`). The generated-hash block at the bottom
> of this file is overwritten by `scripts/update_manifest.py` from
> `RELEASE-HASHES.txt`; do not hand-edit it.
>
> Earlier note (preserved for audit continuity): v1.3.0-rc extended this
> manifest to cover the explanation document, CHANGELOG, and regenerated PDFs,
> and replaced `TO_BE_COMPUTED` placeholders for tracked specification files
> with their SHA-3-512 digests.

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
- `ASSET-DOCTRINE.md` (new in v2.0.0-rc — normative asset doctrine)
- `PROVENANCE.md` (new in v2.0.0-rc — AI-assisted-cleanup / Pixelmator Pro disclosure)

### 3.2 Asset Files

All files under:

- `assets/v2/transparent-1080/` (v2 authoritative master PNGs)
- `assets/v2/transparent-540/` (v2 derived 540 PNGs)
- `assets/v2/masters/` (v2 multi-page TIFF masters)
- `assets/v2/proofs/` (v2 contact sheet + per-state palette proofs)
- `assets/v2/metrics/` (v2 gold-branch transform metrics)
- `assets/masters/` (v1.3 lineage; retained)
- `assets/layers/` (v1.3 lineage; retained)
- `assets/exports/` (v1.3 lineage; retained)

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

### 6.3 Scope of the State Algebra

The canonical state system is exactly the four V₄ transforms: NORMATIVE *I*, NON-NORMATIVE σᵥ, CRITICAL C₂, METACOGNITIVE σₕ. Any other operator (continuous rotation, scaling, shearing, etc.) is out of scope for state assignment and must not be treated as a fifth badge state.

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
  notes: Root system specification (v1.3.0-rc)

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
  notes: Normative state specification (v1.3.0-rc)

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
  notes: Non-normative state specification (v1.3.0-rc)

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
  notes: Critical state specification (v1.3.0-rc)

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
  notes: Metacognitive state specification (v1.3.0-rc) — phrasing refined to "The observer audits the frame"

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
  notes: Publication-facing repository overview (v1.3.0-rc)

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
  notes: Citation metadata (v1.3.0-rc); v1.3.0 version DOI placeholder is TBD_BY_ZENODO_ON_RELEASE
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

## Generated Hash Records (v2.0.0-rc)

The block below is regenerated by `scripts/update_manifest.py` from
`RELEASE-HASHES.txt`. Do not hand-edit between the markers.

```text
assets/releases/540/CRIT-composite-dark-540.png: 4132b809d07e88d8b5d35c08bf91d696c30db7dd644fcbd92d6e9a9f8b88f2bfe799ad8353dbd8e5a35cf221b418220f39de48a750fbf61a1602361ffb37167b
assets/releases/540/CRIT-composite-transparent-540.png: 096b413d00cb5ed376b190c8c71c264ef453175143d355fc710fb77768e85e080b23a712e084b1f62975a694f6e53fb7bd046c5777662c112213757ee9c0253e
assets/releases/540/CRIT-composite-white-540.png: 86336e8e1e726013e820db4ae38f93d0b9dd39493ee745b4faa4b1bf79dd27a5ab1221179208ab8fef657a1123ed18a17d3f1e7ce82e4c25f7817c85ffbcef55
assets/releases/540/META-composite-dark-540.png: 8b2e2bd0a7d2d7958a5e152c576e5f9ec4eff63483e40c4a7c48118b011a5750c80345c1b80f9cd8e0cf4b2b2e1c1199d062c3f873155e134de5bfb68f08bbc4
assets/releases/540/META-composite-transparent-540.png: 140c7b67ca5c2d6e3cfcaa8faecaeb81517a1c47e447c888cf55b0d88d27b7f23cd932570b80309147101039866f3a7578e393d378ac8c5db8d3b2046deaf8e9
assets/releases/540/META-composite-white-540.png: 0df765966512a4d48f50b1aefa029403c357924f01c3e2802e7930d82b6521028aa0a9a65ff721b7be59f6e11f1bd52a03b091eaa0715d4bc7d0aea04d46c10f
assets/releases/540/NONNORM-composite-dark-540.png: 466d5ee8f2b7c5fc5f4a5bf1461f3681d0e422bf1e74c8334a303f1cb1f9d2b55600a0a2701b09cc8aefa3cd35093799f87843ceefee6e87b5a42db237da1a03
assets/releases/540/NONNORM-composite-transparent-540.png: 13fc1dd4a25d084d694decb69853a3417025aec13cb10623542002612906b261c58fbaa261555188c4e6778bdbefe7e9b4b95602302725f513a1e4dac071a56f
assets/releases/540/NONNORM-composite-white-540.png: f03159ab60b436337c8a55fbbdd5a4efeb43f2d33777ac2bb97c1e0af89b93e39afbb968e52da580e377042b868a893f108f9490ac72ae44f654e9bbf89fee8c
assets/releases/540/NORM-composite-dark-540.png: 732f52da5ec897c8c7c4812791c2a1751ccd208538aee5b5137bb75bea5de3c2f64f8eb4c5bbb01abfc190220072bc3f3833127cccdcc24b743f1757ee434eab
assets/releases/540/NORM-composite-transparent-540.png: 17d108ada201e1cbbc77c164c7faaeffb3a6b0c2616d673fffcc42b9141576366f5d59743610ef79917108e4f3e4d63c18f086e2e4946e9c16f55644ef7d8f9f
assets/releases/540/NORM-composite-white-540.png: c48fef712d44fa43d26a7af0fe2183b21326510268f00a5c2135a84aca6689f6c6891d98c45f1ef5a9533d611d09dd32324ae3064fcf6b4a1a27f10216510eb4
assets/v2/transparent-1080/CRITICAL-human-gold-branch-transparent-1080.png: 2dd4df4154a16f8813b8459e6f8a574f2ba4828a81a36b6d3071d3affda9c60eaa73de7143a11b84057796161fbafabbc76a87e2289a8b28580f383e21997b39
assets/v2/transparent-1080/METACOGNITIVE-human-gold-branch-transparent-1080.png: d3e9ba3b019b4f9d69462e3f174082a3412a9ca64b2636d57077351c0e020376922708c27bc74578781c9714915550c891a7862da7ba89a43a867e6ada7b375e
assets/v2/transparent-1080/NON-NORMATIVE-human-gold-branch-transparent-1080.png: ca5cd84c5d37222ac10e3407af4c1dc9803df7d8506c5537c0335e0a4bb6ea35796f3ad4492cafae47ed078f49426663d4251937b3420865634cb94e540207be
assets/v2/transparent-1080/NORMATIVE-human-gold-branch-transparent-1080.png: 8be00902745c676eac24fc5aa2b8a34762da66cfcd8d21b4ee785baf4d2facef22d79952b33d0e17d5309455bc05d8dfb97ddda5e2d689e0b4aa642b880e7b47
assets/v2/transparent-540/CRITICAL-human-gold-branch-transparent-540.png: 68710d0a665b6947544bbf42b5e3375122138dcd84ac31ea02f30a5c5e250f623b2049016b3eb278f3e4b8096d39209b859cb7b3fafcf407c8107f1dc95d1d84
assets/v2/transparent-540/METACOGNITIVE-human-gold-branch-transparent-540.png: 3ac6e3951f4d8f5dedc8bfe06ddcbdf35dacfe4b22c6e221a71667f829d907f0b622cf7d8bb75c7e48f307fb3071a0544cf59adbf2f6a62e6291ec60f495ce36
assets/v2/transparent-540/NON-NORMATIVE-human-gold-branch-transparent-540.png: 24f2c0c978925679260e50241c94b386acfed4ad946bfe47e3db6b38e6a0abc4d2c1b18b7229beb69d29531966976a860facbf507863bbfdffe3d259496ce4a8
assets/v2/transparent-540/NORMATIVE-human-gold-branch-transparent-540.png: 3933054e7ee0ffb566b6b4140f222b266727dc44189c48279fc87e17cd3f495619f52eba667744e50020caee454bef99b6a5f1e1e136a73b3ee17c3368622e5f
assets/v2/final-1080/CRITICAL-V2-FINAL-COMPOSED-1080.png: 638ce02f386cb8c9c8f578037a88f64c482cc9048096922d7471aa27fb7aada96717010732495c1b91a9dcda266ba5212dddd34e86cb8ecffeaa5d9827c5d6f2
assets/v2/final-1080/METACOGNITIVE-V2-FINAL-COMPOSED-1080.png: fc5862c4f784b464aa7d1c8d84e3ded84e90b3fa2272436e18443c27708b8d90cb70513f2b88bf0075ed3b60f1384a50e548b711599ab9e5fd8bbe5aa8e70ae3
assets/v2/final-1080/NON-NORMATIVE-V2-FINAL-COMPOSED-1080.png: 1f29081bbd70571e63e7caccd86e09b18d8ce861fb65ce755a67bcf01a8b25f945dc05823cda122592c7021fca63e617b741b0e2901e2b89a15162a74ee94bb1
assets/v2/final-1080/NORMATIVE-V2-FINAL-COMPOSED-1080.png: da2a70ad028e8eb372e1341a0290632ae4b12fbf720386a643bc81052073f26af54b3547c2a452b447001ef97baf520a779e9529c70fb6c89097185ef919d3d8
assets/v2/final-540/CRITICAL-V2-FINAL-COMPOSED-540.png: aad1bd2a51abcff85787ae2018d0c08525fb7db75e5957f072d98de799f82de51e447bc3a8355cd80c4b0f06442542505ab1acaa564cc95f0785e83e1ed1bbfc
assets/v2/final-540/METACOGNITIVE-V2-FINAL-COMPOSED-540.png: aeefcebcc139325b8d24c13a2f20c0ed4b1c9786f31fa75e6e8c7b02ae9e570e89b8c2119db5d0e23749c9c80aeda337686bbefcc53e1f9d3bbb5e4411bf861f
assets/v2/final-540/NON-NORMATIVE-V2-FINAL-COMPOSED-540.png: ad111af965c4071023e524ec198b12a30deb73298e00aa55c89b53e174af91305fd3f062a73eb129a1ddd97a09191aee7e30940c160cc963658d3bc7039cf231
assets/v2/final-540/NORMATIVE-V2-FINAL-COMPOSED-540.png: 9e87fb9014541635e15cef2dbf7c034eabd2ee01842985bbe7e457c7db8d291e52a0f6eab33c02e169a199213c9043a06acec4e01724a09117076c8b821a0b22
assets/v2/masters/CRITICAL-V2-MASTER-1080.tiff: e5d643ca46a04c57de10f8529d35f8885df2b06edf45ff009928190120350b7ea9c9fed9a4a967f953209581708671a1c05d7fd3b616ee3b3234e8d19b9dc113
assets/v2/masters/METACOGNITIVE-V2-MASTER-1080.tiff: 970a9528ade54f3d11977c3f82e125d21d985cafba3270fbc4698670e86db39653e825194867804de1a9ea352bf10ac67eb0b2c7a6358bdb240d9f049faaf14c
assets/v2/masters/NON-NORMATIVE-V2-MASTER-1080.tiff: d47b03a851ba3f0c003c691afbfeee7c682b8d19f90a70fe50551778dd1df6f265d9c2445c70b16bd5e109d2318bd3086acd72b8bb0658877a0cd0ba8ecf1901
assets/v2/masters/NORMATIVE-V2-MASTER-1080.tiff: 90a16c8860dcd10b29013d8a56ab450e13656b2ab4cfdfb7ebba006a95e212f173728f9705edd4031f579d30ccfb1786e3ab454ef1fe7fba92af8668726c0ec0
assets/v2/proofs/CRIT-v2-layer-proof-palette.png: 18d5ecc7afd5d4cdd0df1d09aab918225618513df0bc8abc90a24387ae779c495f4810d60f9ab5744cf4acf0a0b84a6202fca9e9a030cfd43a312bd60d193920
assets/v2/proofs/META-v2-layer-proof-palette.png: 00f7632b65ca483a40fcb93e4d49eb9d39b32dbb361f6ce8a7d5cb4ac04f79702bb34e65a34a9ed58ca2f6e1b593f15df2c377a46f081e6ca1abcc04b6f058c6
assets/v2/proofs/NONNORM-v2-layer-proof-palette.png: 3f1385cf3db75bdfec1f3d03db94199bd53b582526c4f0de5c6d0020848b951e3e51db13e9c80afc0412bf3875706829b91e7923d80dbeee9a0ca34cd1c573d3
assets/v2/proofs/NORM-v2-layer-proof-palette.png: e014d0fdecd30d41506f5ae180184a5730ac3729fa617c5bf6f08f523584a5b19ca31186fa4fbe4f466561f80edbd3ba1849505cb755c338856a5e6dac63fe7f
assets/v2/proofs/OWL-SEMAPHORE-V2-FINAL-CONTACT-SHEET.png: da2641abb3a3a49fb845dbc029f0c0eddc618bda3b2529f9eb2e9b586e8648939dd3de35ce77a0a0a3ca2d076dd6c308b277576b52018a07ad70d3745231b409
assets/v2/proofs/OWL-SEMAPHORE-V2-MASTER-PROOF.png: 2958612393b4b6ba534eed3d2527df971f14722063d588d91cf9d560584fdc0e6ca966ac13fb124323ebc0bc786366a7155f0c43afc4b600cd20f74f70fa71b5
assets/v2/proofs/human-gold-branch-contact-sheet.png: 142c3173247abfe3f302436ddd265a64e33e6180948c3eedeec0eb7d04559735d5b50fc0ba10b00152defec9163b9b5328656aa586befdb83ab0c5fccb92bfc3
assets/v2/proofs/human-gold-branch-mask-1080.png: 0714ab75960a296c53b0cf72b8ee80484a122ec88c17fdfaaae23f778dba021ea75141ef940aab7f7172fef50712222976435e49db1f1281e236d2bdf1df447b
assets/v2/proofs/human-gold-branch-mask-zoom.png: a4d6e19e4523992309ed96af9925829ba40120963ed0e1d48db314b4c6a5a458b8f58f74eaa2ee54631fb19b3de0a2161a767faa7102df4457a7147b7dae914e
assets/v2/normative-D-B-gold-master/NORMATIVE-V2-D-B-GOLD-MASTER-ASSET-1080.tiff: 1adb9e14016bc913e0fe1377a9cb0f44bc87ca9c9a5b3c67fde2a2158b438e525ffbcb368237111ebbece49f807e6b65192d1fb441e8a5a893ba205438cbd068
assets/v2/normative-D-B-gold-master/NORMATIVE-V2-D-B-GOLD-MASTER-COMPOSITE-1080.png: da2a70ad028e8eb372e1341a0290632ae4b12fbf720386a643bc81052073f26af54b3547c2a452b447001ef97baf520a779e9529c70fb6c89097185ef919d3d8
assets/v2/normative-D-B-gold-master/NORMATIVE-V2-D-B-GOLD-MASTER-COMPOSITE-540.png: 9e87fb9014541635e15cef2dbf7c034eabd2ee01842985bbe7e457c7db8d291e52a0f6eab33c02e169a199213c9043a06acec4e01724a09117076c8b821a0b22
assets/v2/normative-D-B-gold-master/NORMATIVE-V2-D-B-GOLD-MASTER-METRICS.json: 2683c210eb74b8d034024262c339f9b8ffcee7a2ced4f0f4ec642e047f0195d70c84889b1d56096959bb37217ab1612a63ebdaba00ed8d7c1c78959efa19ef4f
assets/v2/normative-D-B-gold-master/layers/NORMATIVE-V2-D-B-GOLD-L1-inner-field-1080.png: 5288d99dea892292a025d7d51518e5cd888b85b686846dc0b2ec5328c4629a78e12819ebfe0bbeb75f35b52d40f04800fc1313db7d31509ca176c2e0bf6cd408
assets/v2/normative-D-B-gold-master/layers/NORMATIVE-V2-D-B-GOLD-L2-meander-ring-1080.png: 40b54d0ecdd80bf3f5c2eeab2286798b1cf4424810b4f85e967cb5ba9b45f05b44ee05218e133711c1f4b4c2921089e0e9b3a5bbdf8f50da43ca733a4e242c3e
assets/v2/normative-D-B-gold-master/layers/NORMATIVE-V2-D-B-GOLD-L3-v2-approved-owl-D-geometry-B-parchment-gold-1080.png: 8be00902745c676eac24fc5aa2b8a34762da66cfcd8d21b4ee785baf4d2facef22d79952b33d0e17d5309455bc05d8dfb97ddda5e2d689e0b4aa642b880e7b47
assets/v2/normative-D-B-gold-master/layers/NORMATIVE-V2-D-B-GOLD-L4-outer-ring-1080.png: a587ec28a47321af93ba79971568cb303b8919252f72ddafcf961a5bb3ecadbb41d197ed5ac003952d131f75ad799942a7a1305db5b93f02e8aff9d3a51f8e27
assets/v2/normative-D-B-gold-master/proofs/NORMATIVE-V2-D-B-GOLD-MASTER-LAYER-AND-WING-LINE-PROOF.png: 30e0406e372520eabd88fff5454d373fa8006179a0dbbfd0434723f9700ca52d3b91e2af89ad545c55c5f25890213da677c22b489a5d88a1d253bf5c4132f7f4
assets/v2/nonnormative-math97-five-over-master/OWL-2-NON-NORMATIVE-MATH97-FIVE-OVER-COMPOSITE-1080.png: 1f29081bbd70571e63e7caccd86e09b18d8ce861fb65ce755a67bcf01a8b25f945dc05823cda122592c7021fca63e617b741b0e2901e2b89a15162a74ee94bb1
assets/v2/nonnormative-math97-five-over-master/OWL-2-NON-NORMATIVE-MATH97-FIVE-OVER-COMPOSITE-540.png: ad111af965c4071023e524ec198b12a30deb73298e00aa55c89b53e174af91305fd3f062a73eb129a1ddd97a09191aee7e30940c160cc963658d3bc7039cf231
assets/v2/nonnormative-math97-five-over-master/OWL-2-NON-NORMATIVE-MATH97-FIVE-OVER-MASTER-ASSET-1080.tiff: 539519f32503e53ca93507a0ae6925f161bd0d9af2f4726d1818d32f979606daebd572da07c3d1a1070338bed5a092b4a7a740a8a6b4534648fd6eda80abb972
assets/v2/nonnormative-math97-five-over-master/layers/OWL-2-NON-NORMATIVE-L0-inner-field-underpaint-17-1080.png: d22473f0434e1df58332309e4dcb77e5ef43a0744c8ab57abee7b5a4101eb72c738ff26590afc5fac7d1e8d12ae09a5e2fe31b97eb52a3727ee6edc843dec0df
assets/v2/nonnormative-math97-five-over-master/layers/OWL-2-NON-NORMATIVE-L1-inner-teal-ring-outward-17-1080.png: bf66d1e7e79af51ec3f7265be9d4e9642cb504aa384d4fdbc68b2472fc485cd76c59ae5585a84158eee45215eca83763b27b60044195af5025262ee1ccac6305
assets/v2/nonnormative-math97-five-over-master/layers/OWL-2-NON-NORMATIVE-L2-meander-ring-original-1080.png: 40b54d0ecdd80bf3f5c2eeab2286798b1cf4424810b4f85e967cb5ba9b45f05b44ee05218e133711c1f4b4c2921089e0e9b3a5bbdf8f50da43ca733a4e242c3e
assets/v2/nonnormative-math97-five-over-master/layers/OWL-2-NON-NORMATIVE-L2_5-inner-meander-black-edge-5-over-1080.png: 4f04e4aed1d01a43c9739b10a69cb65287b12c7867946c359481aea155069fac65751a82451ade615088a18be023e892ef3b7de10fcbf825022298376eea80aa
assets/v2/nonnormative-math97-five-over-master/layers/OWL-2-NON-NORMATIVE-L3-owl-math-mirror-center-scale-97-1080.png: ca5cd84c5d37222ac10e3407af4c1dc9803df7d8506c5537c0335e0a4bb6ea35796f3ad4492cafae47ed078f49426663d4251937b3420865634cb94e540207be
assets/v2/nonnormative-math97-five-over-master/layers/OWL-2-NON-NORMATIVE-L4-outer-teal-ring-1080.png: 21acd2be4a3c3d5b1a86db31ef0a279acadfb4085507f53b35d0ef6c8949f4037330954a947b81b177eee8972c6e2819a72cf9522fcda95a34bdf68f7eb9e4bc
assets/v2/nonnormative-math97-five-over-master/proofs/OWL-2-NON-NORMATIVE-MATH97-FIVE-OVER-LAYER-PROOF.png: 54c76144fc09d14d5e5a9ffb2ca66d298de33b4cef784030858c7c47d0e6d0aaf9a2ce8c5c664ce0dfefe795832808c4115a774d62c2bb693d177ca1350c3391
assets/v2/nonnormative-math97-five-over-master/proofs/OWL-2-selected-proof-vs-master-composite-diff.png: fdf1be1da9712d122f2640bb2468bc4c28a9366b3be97bc66afbf487bd503b5c9015d38390b60676a8a1eb3ea4ae9f8b676a1279791717773df5a396480b7bf9
assets/v2/nonnormative-math97-five-over-master/metrics/OWL-2-NON-NORMATIVE-MATH97-FIVE-OVER-METRICS.json: d29b4e5abc19f9920bef3ed089cf8b7493c2d649fc929506b1d1f473fdebcc52f9dbe1369d9114eb8ef690c9b49173a93cda40cbdf64bd54b6ba9765e6fadd81
assets/v2/metrics/human_gold_branch_metrics.json: 5f03af471430257db5dd51e46eb326304e4d18d8f9f39a39f64ff8ba39da40ee0940a43bcccfca768495b0b425fe759eeece2fc25bf5f4cc0353676af30be9c5
assets/v2/normative-D-B-gold-master/SOURCE-README.md: 0c3257acfcdb5d6caf23e6b04c2e9dd0ae9e347588295a44dd0d74c38ed2b3b09238e11581f28d37c090a415739580cf32971d18e06f11e333223741f878d09d
assets/v2/normative-D-B-gold-master/AUDIT-NOTE.md: b20d4d716d675b09a4e0958a7cadc5e0e7fc014b44c11d052c2ec38ff29001d2459e53e80d4512a3a35c2658ac0d09df17601070d68b2bdac424386263b83b48
assets/v2/nonnormative-math97-five-over-master/SOURCE-README.md: 244d6db8b313b7cf05616d9a5d05f3fe748db19d2d53e23b5e8de6f55c1c9d7e8a076cacda9f6022bb2aac3b3089a9a1092c6f7097cb2abccfceb488b0031707
assets/v2/nonnormative-math97-five-over-master/SOURCE-AUDIT-NOTE.md: 732c2f678e9dc14aaa2557ac75259039a031e8ccc27fd9f39e59e3b9a8baa3eb3df3a5b43ab2bd4b615d9f29fc042c8f94bc16db3577591108a0ec48ac37faf8
assets/v2/nonnormative-math97-five-over-master/AUDIT-NOTE.md: f89039256db4537ef635edabe733e0107a6d76d9f4422188131034056d649451a81a9d20cf37ca88932498b47ee62635649364c1b933e9dc7d4133c618a5905b
OWL-SEMAPHORE-SYSTEM.pdf: 4d0687720b575a5d1ee3fb9c669e9a59f395d01b2df08b3b04e80325cf4eb6216d15acfd073bca01ffbec21f4ab695d66035146f53df09bc8505be5a12438b25
OWL-SEMAPHORE-EXPLANATION.pdf: de82766d00850fb9fc09499b499b1166d79fe6c34dc8fd49e573af443a96d38c820e7a4bd4709dafd20cc35360ddd8a3df457e3f58dbab77e3a20444ccfd8c83
OWL-1-NORMATIVE.pdf: a278edd49248e9f9ca8d4fe2732b0b6d89e66ad2516c5599cb1460d8b8c66ece4147375161203707ddaabde2795bde9f99b860d2d0089620befc2350484afc1c
OWL-2-NON-NORMATIVE.pdf: fbda7e76ce5f62f0e67c2446afe79988e4c0302c1b82f405ee483ed781dd05a554e6c086e6b4015cbc969b9d689f5cac0ba2ca7ebc03991d9578c9ed34456ad1
OWL-3-CRITICAL.pdf: 0b7a65607182f08ca7685ffc3bd3ea0008bfe1405d0b3c1438efd19771eb31c36a85a13c752b75bd275d3c79a6ac6a0a3c4bcfc4c8d772d05460d954b0ec513b
OWL-4-METACOGNITIVE.pdf: 9a1858a974e668465ae0c98e9c8c9b6e7e17e654c52f9e657f8deb5da18f2b96f0363be5fba78154b9d7276c3979202483640681b5587406b62968f5699697f5
README.md: 55d038270bb9c76c4654ce664afd214fa1761b26405f0256c4fd6beacfe3fe113b9675fa65cf3b1b6b490ea1ef9654835099073256c28d4a2340996c2d338512
CHANGELOG.md: 131c9e33a8d0d9f6a2a61e7671cb09b525d1efc5140dc1a9c6ab874f1a7d7bf6b6118a0cd4ce39b40a1af36a2eb34e06ce6ca5aef6211766ab6eac56942514a2
ASSET-DOCTRINE.md: bedcfb3cdd9a5c8a12f82cca547d074abdc36f48163a63ca4b39b5d935da838f84fc88e6ba3162d013554df19c6e999a849cce26c90128716f6e0b6649767f51
PROVENANCE.md: c0be026a3a67bbb02c774378fe483e14b059bff020b234fe19cf36cc97b449267e25b68060ad2c1ccefa73ebcef25109ffbd32d3dc9a05b1b3458a053c032d52
OWL-SEMAPHORE-SYSTEM.md: 3be963b3d10dd87aa14981185ddf74650a3d802e7287ba7e173d5a5cc3977b498e59c27b2036040e5ce66f87249018917e4acf9a70b65f2bade83fb61ffcb72c
OWL-SEMAPHORE-EXPLANATION.md: 6e84df27c4969bb492a869969f68e41e5426ce7028de7456acba8f86c8d1cfe1d11087e11a82207a530d7b754dc69e6f0f80aa6e9462f2fc953ac6d91c1f1ea9
OWL-1-NORMATIVE.md: 12dca247ad3ef896e5c5c2f68b53414d0ea2c40b8413ac3ac5569ef0dc9c70e0243519fceb01701360ea7f2c68ce8a1e49d90b3c7648a223ec0f32df5011af94
OWL-2-NON-NORMATIVE.md: 683b5cd2557d420b1b361cf019f4197bd73e81ec23c288e7ad82195052b1ec2e783818d304f6c6900b709b8bfe645814922d2d4c97c43bb500ea117f2c316440
OWL-3-CRITICAL.md: de91a0e03cbc2dba4cf429652b27ad51f1ce9ec77761c8fb57e6b5677c2301edfd484bdaa9892ebd0c7c8e6169c71fdc0954f7ae04ba92866b7e7eed9ff12a5b
OWL-4-METACOGNITIVE.md: f7c08e99d2695e7ae656731140fbc69e4f0b2a492ac6277a9ac1636687d3cfae6a84bd9b27c20983772c8f2b011136a8b37a4a858bc101cbe66c3d17d1b1f10f
INTEGRITY-MANIFEST.md: cd0e4a5e644e26dff78b8d9a6114508e97da94dd462c9b0cd5e48f466da88b4103993abae2af17a36ab10c9409d3cc436693263f2767819f2779a90cee2cf27a
CITATION.cff: 954271af5e2771ccb8d53c98422263f1ee0b77598d9f6c11641ab7db86f1170a47070bef50d60d82b0e2c293060707f22439080acd05df5f1cba78439b6e0d7d
.zenodo.json: ccce68ce3f536b6e0aa485388b35684be0d882fb4307a21b1e4f386f81d1fb60ad48092ab4049d8aa33c25446b71a012a0812f91adfef8442d63b4bdfe2ec1c6
```

<!-- END GENERATED HASHES -->
