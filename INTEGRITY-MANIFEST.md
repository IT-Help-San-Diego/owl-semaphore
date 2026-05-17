

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
assets/v2/transparent-1080/NON-NORMATIVE-human-gold-branch-transparent-1080.png: 47e3118e5599758101b81a0b2d5db2ec2a9ff2da9469dcaaff9869e2d0a46b699f8782ccc0b616cfd0b8c8f27acd53325a6faa56cd77ac302d949aba08261bdf
assets/v2/transparent-1080/NORMATIVE-human-gold-branch-transparent-1080.png: de40ca9f40a8abd9774939e911b1899bcc31896a14f363c14e925fb7042d40f47a4859e965115df5346d793bca7e47674b5216f063d348f5a61f7662014a2c57
assets/v2/transparent-540/CRITICAL-human-gold-branch-transparent-540.png: 68710d0a665b6947544bbf42b5e3375122138dcd84ac31ea02f30a5c5e250f623b2049016b3eb278f3e4b8096d39209b859cb7b3fafcf407c8107f1dc95d1d84
assets/v2/transparent-540/METACOGNITIVE-human-gold-branch-transparent-540.png: 3ac6e3951f4d8f5dedc8bfe06ddcbdf35dacfe4b22c6e221a71667f829d907f0b622cf7d8bb75c7e48f307fb3071a0544cf59adbf2f6a62e6291ec60f495ce36
assets/v2/transparent-540/NON-NORMATIVE-human-gold-branch-transparent-540.png: 77e80a7d888cb2c2297b67ee8694f7cf4b89d93920bdc5b49efb09bd346b23f9bac5aa66fcea579b15f90a0a9dceaaaa266aaedca33b7a89d09737fa88f8ca4b
assets/v2/transparent-540/NORMATIVE-human-gold-branch-transparent-540.png: 4dd5ad5cac3b7f6368bcc59bb5f676c618a7f7cd4b9cea09bfe08feafab02aae9eab44ee97a7bdebbfd2d7c298495ac180caa8308ad5ef251794b5ee21b16892
assets/v2/final-1080/CRITICAL-V2-FINAL-COMPOSED-1080.png: 638ce02f386cb8c9c8f578037a88f64c482cc9048096922d7471aa27fb7aada96717010732495c1b91a9dcda266ba5212dddd34e86cb8ecffeaa5d9827c5d6f2
assets/v2/final-1080/METACOGNITIVE-V2-FINAL-COMPOSED-1080.png: fc5862c4f784b464aa7d1c8d84e3ded84e90b3fa2272436e18443c27708b8d90cb70513f2b88bf0075ed3b60f1384a50e548b711599ab9e5fd8bbe5aa8e70ae3
assets/v2/final-1080/NON-NORMATIVE-V2-FINAL-COMPOSED-1080.png: 1ca934c84231837ee21e0b4ac311e25b80fa8ed46d74a2bd313218d703ff3905a1c427bcc6282c4c10e5071832b1e52f0c9dcd2fdb97bb71eb910726e2b9e75d
assets/v2/final-1080/NORMATIVE-V2-FINAL-COMPOSED-1080.png: ff9e2fbf1d39b2474433bf943a333a22f900668dcdda037d46ffa953c1cf3ab26b43d2e1f0367f27aa67654d1cdeb89ea1452489de37015759116a0b9d641526
assets/v2/final-540/CRITICAL-V2-FINAL-COMPOSED-540.png: aad1bd2a51abcff85787ae2018d0c08525fb7db75e5957f072d98de799f82de51e447bc3a8355cd80c4b0f06442542505ab1acaa564cc95f0785e83e1ed1bbfc
assets/v2/final-540/METACOGNITIVE-V2-FINAL-COMPOSED-540.png: aeefcebcc139325b8d24c13a2f20c0ed4b1c9786f31fa75e6e8c7b02ae9e570e89b8c2119db5d0e23749c9c80aeda337686bbefcc53e1f9d3bbb5e4411bf861f
assets/v2/final-540/NON-NORMATIVE-V2-FINAL-COMPOSED-540.png: 07c1690277b625049bdd91895e4e1977565e6edf669028e218856b881ddd61f29600c1b9ef2ed2b611b9b4690469a1f4bb3072631805fb46ab9c03c1c5e4bff0
assets/v2/final-540/NORMATIVE-V2-FINAL-COMPOSED-540.png: 42cda5d977ed6741d454a981e63c95e2687f25474c5d79fda47bdaf894af64d97069770cad657da99cd965c292ad3a3965d70c63f8a27ae7206e9b1570471562
assets/v2/masters/CRITICAL-V2-MASTER-1080.tiff: e5d643ca46a04c57de10f8529d35f8885df2b06edf45ff009928190120350b7ea9c9fed9a4a967f953209581708671a1c05d7fd3b616ee3b3234e8d19b9dc113
assets/v2/masters/METACOGNITIVE-V2-MASTER-1080.tiff: 970a9528ade54f3d11977c3f82e125d21d985cafba3270fbc4698670e86db39653e825194867804de1a9ea352bf10ac67eb0b2c7a6358bdb240d9f049faaf14c
assets/v2/masters/NON-NORMATIVE-V2-MASTER-1080.tiff: d47b03a851ba3f0c003c691afbfeee7c682b8d19f90a70fe50551778dd1df6f265d9c2445c70b16bd5e109d2318bd3086acd72b8bb0658877a0cd0ba8ecf1901
assets/v2/masters/NORMATIVE-V2-MASTER-1080.tiff: 90a16c8860dcd10b29013d8a56ab450e13656b2ab4cfdfb7ebba006a95e212f173728f9705edd4031f579d30ccfb1786e3ab454ef1fe7fba92af8668726c0ec0
assets/v2/proofs/CRIT-v2-layer-proof-palette.png: 18d5ecc7afd5d4cdd0df1d09aab918225618513df0bc8abc90a24387ae779c495f4810d60f9ab5744cf4acf0a0b84a6202fca9e9a030cfd43a312bd60d193920
assets/v2/proofs/META-v2-layer-proof-palette.png: 00f7632b65ca483a40fcb93e4d49eb9d39b32dbb361f6ce8a7d5cb4ac04f79702bb34e65a34a9ed58ca2f6e1b593f15df2c377a46f081e6ca1abcc04b6f058c6
assets/v2/proofs/NONNORM-v2-layer-proof-palette.png: 9a4aa755badcc8a9d820b9750e02376f47b524e7c36bb49a5d378530fb7033b6c358d5a6fc23687ac2f23a2178286eda7bb0fe7b1ca1f286ce5793eb913769ab
assets/v2/proofs/NORM-v2-layer-proof-palette.png: 1db46b8c591f10c18355dde3959ff1dd2ab3d2fcd8f828311c5345e296c3806cb2949c9e3a10b6c6ba922d00441b6aa809981e788e3bf1c513d36be80e723b52
assets/v2/proofs/OWL-SEMAPHORE-V2-FINAL-CONTACT-SHEET.png: 2c0f1a56bdbf179c5ebcd9762af89e9835ae2621c8df87965906ad0e8f21d48ebfc67d1264204e2a3d8c11792ef5fb20dfb3105c52ae270aabafa31c8ee140f6
assets/v2/proofs/OWL-SEMAPHORE-V2-MASTER-PROOF.png: 2958612393b4b6ba534eed3d2527df971f14722063d588d91cf9d560584fdc0e6ca966ac13fb124323ebc0bc786366a7155f0c43afc4b600cd20f74f70fa71b5
assets/v2/proofs/human-gold-branch-contact-sheet.png: 142c3173247abfe3f302436ddd265a64e33e6180948c3eedeec0eb7d04559735d5b50fc0ba10b00152defec9163b9b5328656aa586befdb83ab0c5fccb92bfc3
assets/v2/proofs/human-gold-branch-mask-1080.png: 0714ab75960a296c53b0cf72b8ee80484a122ec88c17fdfaaae23f778dba021ea75141ef940aab7f7172fef50712222976435e49db1f1281e236d2bdf1df447b
assets/v2/proofs/human-gold-branch-mask-zoom.png: a4d6e19e4523992309ed96af9925829ba40120963ed0e1d48db314b4c6a5a458b8f58f74eaa2ee54631fb19b3de0a2161a767faa7102df4457a7147b7dae914e
assets/v2/metrics/human_gold_branch_metrics.json: 5f03af471430257db5dd51e46eb326304e4d18d8f9f39a39f64ff8ba39da40ee0940a43bcccfca768495b0b425fe759eeece2fc25bf5f4cc0353676af30be9c5
OWL-SEMAPHORE-SYSTEM.pdf: 1689df675c72e96dd0ead863736600e405120c22d5a69cbbbaf46b9b8f6721337a2066197e8b0703d634ce7acd5f32ca79cf8c6ec0debe1d0c01352b8c426471
OWL-SEMAPHORE-EXPLANATION.pdf: 8fdad4931a7d0dee6a524f9c1f07b20d65191b43881b7ef9c13c3db00ee06bb60f431c968dea105af2c9a9a173a0f11e1d864b8570361e917a14833eb27bdc6d
OWL-1-NORMATIVE.pdf: 69916719b2e7f636b555ebb5dbc733277c83df4367c62c41d3691609bede77a20411e25eff224a41135afc611fb266b4f5a3023efeb1190ba02f098d1834c265
OWL-2-NON-NORMATIVE.pdf: fbb9d1da890181c70835887b3def87127ed8511ebfdf0d94267707fb68e4cce93fadcf1c7d48877a1236a0ff69bcd22828555bbf01c186200eceaeb42604e24a
OWL-3-CRITICAL.pdf: 1c88a06d78d1b27ec7d95c5cda07360043b3f3fb8304d7c02ae1a324d6b9e22a86903efb6a8e82c5d2ecf2ce47b6d81cce2716acf7fb5473c9ef468e68acdd31
OWL-4-METACOGNITIVE.pdf: 3ada91b42a9a17a22cc5a4d2708b62b8acba9f77a535baf86e237ae0714086ea05a19efef488374d2d0b4611e6d77d8c05c801abd0bf5fe5cb42fef6cd940257
README.md: 70120547ecc914abc028d3cc0452a3a57e72667a32fc4e370ed8d12d90735248d53baef72a54f39fd4d35aa7c180a22c7bcef5f3d0f4fca806c856e5df86b8bc
CHANGELOG.md: 126670aae965170f0e59935721e43dbbd6f821589e7d10e39811641760b11b2f3599f8d283357b304d9cd0f30ec0cebbea916a5c96404cc6c923d98eabb39c30
ASSET-DOCTRINE.md: 74c458213cb595ceb87eeedd0247a8745e24606d9542b650f49eced59e364c8063c5e98b9a6ec76188a51adde8b5ebab9a0140f1c5a3d472cd05e04e8e89b223
PROVENANCE.md: 98fa6c035df5ab739a733d0f7791d72b7bcf70f84ef61962976ab5b4db3815aad00d33958c967aae72cfae28ffef1292f51b7ece0553635429e16cf7a2a99977
OWL-SEMAPHORE-SYSTEM.md: 84572df0b0bba0e95385875ff670e3d744a7e925b779e5baabea0679bc5482db0476ec630236204dfdbc441d4a8f29147d40aecb695429d58421b7cc2d00acee
OWL-SEMAPHORE-EXPLANATION.md: 6e84df27c4969bb492a869969f68e41e5426ce7028de7456acba8f86c8d1cfe1d11087e11a82207a530d7b754dc69e6f0f80aa6e9462f2fc953ac6d91c1f1ea9
OWL-1-NORMATIVE.md: 1934cd05a377dee1426bf1ad27906d51123e757271ff2f8ce1fbe4e0637fe28c5ec9388f791c94a723e020af4f350897e618cca5243ced25bcaf645891c5e203
OWL-2-NON-NORMATIVE.md: 068edf7b8c25d2847b3744f461ec928e45db85fc41b7ec7c65c9d1a75efe03589fc94163c6a6703e673edf593591bbb2caf02c12de44f1560d7a59cc6b94df25
OWL-3-CRITICAL.md: de91a0e03cbc2dba4cf429652b27ad51f1ce9ec77761c8fb57e6b5677c2301edfd484bdaa9892ebd0c7c8e6169c71fdc0954f7ae04ba92866b7e7eed9ff12a5b
OWL-4-METACOGNITIVE.md: f7c08e99d2695e7ae656731140fbc69e4f0b2a492ac6277a9ac1636687d3cfae6a84bd9b27c20983772c8f2b011136a8b37a4a858bc101cbe66c3d17d1b1f10f
INTEGRITY-MANIFEST.md: d67aab89ca35025be488bd217ca0c2b98ecee4d1e2604fe4288cc6fad03fad2ef216eda471264d924f63f7b14779f188cd51f87aed6a04cf72636bf3fc140c90
CITATION.cff: 954271af5e2771ccb8d53c98422263f1ee0b77598d9f6c11641ab7db86f1170a47070bef50d60d82b0e2c293060707f22439080acd05df5f1cba78439b6e0d7d
.zenodo.json: 4ae89e776b1913e7fcdbdc414e770f74da9519e30a662135cf79904c533c522f69066524402cc7893942855e82fc5d0f58dc7cee924d240008ae0c8ffbdeecba
```

<!-- END GENERATED HASHES -->
