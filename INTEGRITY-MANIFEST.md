

# OWL SEMAPHORE — INTEGRITY MANIFEST

## Version 1.3.0-rc (release candidate; Zenodo DOI to be minted on publication)

- **Concept DOI (all versions):** [10.5281/zenodo.19473697](https://doi.org/10.5281/zenodo.19473697)
- **Last published version DOI (v1.2.0):** [10.5281/zenodo.19474599](https://doi.org/10.5281/zenodo.19474599)
- **Version DOI (v1.3.0):** `TBD_BY_ZENODO_ON_RELEASE`
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

Hashes below are produced by `scripts/compute_hashes.py`; the same script also writes `RELEASE-HASHES.txt`. Regenerate with `make hashes`.

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
- `OWL-SEMAPHORE-EXPLANATION.md`
- `README.md`
- `CHANGELOG.md`
- `CITATION.cff`
- `.zenodo.json`

### 3.1.1 Generated Publication PDFs

- `OWL-SEMAPHORE-SYSTEM.pdf`
- `OWL-1-NORMATIVE.pdf`
- `OWL-2-NON-NORMATIVE.pdf`
- `OWL-3-CRITICAL.pdf`
- `OWL-4-METACOGNITIVE.pdf`
- `OWL-SEMAPHORE-EXPLANATION.pdf`

PDFs are regenerated deterministically from their Markdown sources by `generate_pdfs.py` (invoked via `make pdfs`). Their per-page running headers and embedded BANNER TUPLE block are verified by `scripts/verify_banner_tuple.py`; their document-info metadata (title, author, keywords, subject) is verified by `scripts/check_pdf_metadata.py`.

### 3.2 Asset Files

All files under:

- `assets/masters/`
- `assets/layers/`
- `assets/exports/`

### 3.3 Validation and Publication Files

- `INTEGRITY-MANIFEST.md`
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

### 11.1 Root Specifications (v1.3.0-rc)

```text
- path: OWL-SEMAPHORE-SYSTEM.md
  role: system specification
  state: system
  type: markdown
  transform_class: n/a
  sha3_512: 952471b0bc53491d410f246152fbfdeeca995fe143b5cdda7bf377a069a3dd96f57327173258fb6d729416b842c36134af215f552723ecf459dd65e0543532ef
  status: VERIFIED

- path: OWL-1-NORMATIVE.md
  role: state specification
  state: NORMATIVE
  type: markdown
  transform_class: I
  sha3_512: b63756cf8444ed3fce9dcf53eb143c61c8123138be63df002c5532bec6e522700a8ec5f0de62a919984f04947acc40b59bf613e909e4bdf4a83cd4ce37b3be75
  status: VERIFIED

- path: OWL-2-NON-NORMATIVE.md
  role: state specification
  state: NON-NORMATIVE
  type: markdown
  transform_class: σᵥ
  sha3_512: 75fc74c9d9b27222939126295728f12ed5d099ad8fefce62c7c899c0ce0929d2fab1f8421b14120566a3eeb71168c40a0358ec6e504e5cc4e25bc6e60b49d42a
  status: VERIFIED

- path: OWL-3-CRITICAL.md
  role: state specification
  state: CRITICAL
  type: markdown
  transform_class: C₂
  sha3_512: 8de3fbad7ee992f5c83166345bf780ac852863e4b46ae205d56f5dee89cf70641bd6e6eeb891bd511e4cfe1e044fa793e8d9688d0979ded21c226febc93143f8
  status: VERIFIED

- path: OWL-4-METACOGNITIVE.md
  role: state specification
  state: METACOGNITIVE
  type: markdown
  transform_class: σₕ
  sha3_512: c35524ca6a67621fb3f650b070c32a7c85618cb6f16b3a89e7dcf39900553e4a5f317816347c175852e554eff1f4951e7cff81dc4ce059bd20677b3dc3c4854f
  status: VERIFIED

- path: OWL-SEMAPHORE-EXPLANATION.md
  role: informative explanation
  state: system
  type: markdown
  transform_class: n/a
  sha3_512: 483af7e6a87be2684e84f0c875105404035f4025fa52bc42fcba63597125f67516fe532df0859859399d1bc49ce3c247ec30fa4ce6e32fe82e7193189ca4ce0d
  status: VERIFIED
  notes: Origin story, archetype rationale; companion to OWL-SEMAPHORE-SYSTEM.md

- path: README.md
  role: repository overview
  state: system
  type: markdown
  transform_class: n/a
  sha3_512: 38e7450165260c8c16472e7d8d4f7a3f04aac43c6dd2a5e13f97670e600fb3fcd6ff0197628525c80306c747ad3c569c45d3e2007359970995f962657a1e8ef3
  status: VERIFIED

- path: CHANGELOG.md
  role: change history
  state: system
  type: markdown
  transform_class: n/a
  sha3_512: b87b869395b56423c1b1f0ff1ad3911084b3c3a675da6a2327a06f970909b05331d98a50d64bfbebdc34ba81186527c7ecc6df709ce4f5864522fe8b0757313f
  status: VERIFIED
  notes: Records canonical sentence per release

- path: CITATION.cff
  role: citation metadata
  state: system
  type: yaml
  transform_class: n/a
  sha3_512: 9f957df7d14fd0ebd8c01e9d7a0e2939a749f7a5dfaca6c664e8cef2f22409f03ac84a71ec9f6b36683b06c8f6e673ac0bf6662eac4b0fe10c2aa7e280e8b236
  status: VERIFIED

- path: .zenodo.json
  role: Zenodo metadata
  state: system
  type: json
  transform_class: n/a
  sha3_512: 75e86dfa0acc13475017af9cc7caad5267253b0930109b7459cebbf1fa024db9e1a5caa5b42b9124b08ed165a85057329d8110869bbf828d5d00def996752163
  status: VERIFIED
  notes: version_doi field carries TBD_BY_ZENODO_ON_RELEASE placeholder
```

### 11.3 Generated Publication PDFs (v1.3.0-rc)

```text
- path: OWL-SEMAPHORE-SYSTEM.pdf
  role: system specification PDF
  state: NORMATIVE-header
  type: pdf
  transform_class: I
  sha3_512: d1d2df90d637437a36955be21c86ba8d7e48681a1bbc5837e71c5ba471dc1d05574f562a43dfe7aeca147035df866ecd16578f6abea9368834fc7325cd23df76
  status: VERIFIED

- path: OWL-1-NORMATIVE.pdf
  role: state specification PDF
  state: NORMATIVE
  type: pdf
  transform_class: I
  sha3_512: d3b9b5782ceeed4b886f39eaeb04ed16885a74d2d3ce863c0bf722af34f78f618681ace72fab763d7fc071424176d01d59978a91d64c3e65092c8cceba8758ef
  status: VERIFIED

- path: OWL-2-NON-NORMATIVE.pdf
  role: state specification PDF
  state: NON-NORMATIVE
  type: pdf
  transform_class: σᵥ
  sha3_512: 5f4fd5876478b4626f1c398ca310101cd3114d942e6688f1f3ac70230fee937ddfbd9ba3847186b894a0f94e67c92e4e3829c6ecea22036b5f16b604d686a370
  status: VERIFIED

- path: OWL-3-CRITICAL.pdf
  role: state specification PDF
  state: CRITICAL
  type: pdf
  transform_class: C₂
  sha3_512: 2dd2ab42fa36052811d6c5c666e82a071b428fc6f39a2a26be44afa28487a12b290971b18351319b934fd4f21e5a364b28d1904ad971fef3ad980517178f1e90
  status: VERIFIED

- path: OWL-4-METACOGNITIVE.pdf
  role: state specification PDF
  state: METACOGNITIVE
  type: pdf
  transform_class: σₕ
  sha3_512: e3571c35e69a4e5686080c6936acf2ac2947d40dc2789199d00c9413ca864c4cd7177739d4bbaae1604845bf9f06c201c939727e8c2e8a11baefc31708a7ddb0
  status: VERIFIED

- path: OWL-SEMAPHORE-EXPLANATION.pdf
  role: informative explanation PDF
  state: NORMATIVE-header
  type: pdf
  transform_class: I
  sha3_512: eeac6433058cefd2e5ef79c463a7080c5f382897a209b2912d70e588599a52b4ab21df09349844e422e41ac90d2efbf862378b21a71edb80fb8e135962f1316b
  status: VERIFIED
```

### 11.4 540 px Composite Release Set (unchanged from v1.2.0)

```text
- path: assets/releases/540/NORM-composite-dark-540.png
  state: NORMATIVE
  transform_class: I
  sha3_512: 732f52da5ec897c8c7c4812791c2a1751ccd208538aee5b5137bb75bea5de3c2f64f8eb4c5bbb01abfc190220072bc3f3833127cccdcc24b743f1757ee434eab
  status: LOCKED

- path: assets/releases/540/NORM-composite-transparent-540.png
  state: NORMATIVE
  transform_class: I
  sha3_512: 17d108ada201e1cbbc77c164c7faaeffb3a6b0c2616d673fffcc42b9141576366f5d59743610ef79917108e4f3e4d63c18f086e2e4946e9c16f55644ef7d8f9f
  status: LOCKED

- path: assets/releases/540/NORM-composite-white-540.png
  state: NORMATIVE
  transform_class: I
  sha3_512: c48fef712d44fa43d26a7af0fe2183b21326510268f00a5c2135a84aca6689f6c6891d98c45f1ef5a9533d611d09dd32324ae3064fcf6b4a1a27f10216510eb4
  status: LOCKED

- path: assets/releases/540/NONNORM-composite-dark-540.png
  state: NON-NORMATIVE
  transform_class: σᵥ
  sha3_512: 466d5ee8f2b7c5fc5f4a5bf1461f3681d0e422bf1e74c8334a303f1cb1f9d2b55600a0a2701b09cc8aefa3cd35093799f87843ceefee6e87b5a42db237da1a03
  status: LOCKED

- path: assets/releases/540/NONNORM-composite-transparent-540.png
  state: NON-NORMATIVE
  transform_class: σᵥ
  sha3_512: 13fc1dd4a25d084d694decb69853a3417025aec13cb10623542002612906b261c58fbaa261555188c4e6778bdbefe7e9b4b95602302725f513a1e4dac071a56f
  status: LOCKED

- path: assets/releases/540/NONNORM-composite-white-540.png
  state: NON-NORMATIVE
  transform_class: σᵥ
  sha3_512: f03159ab60b436337c8a55fbbdd5a4efeb43f2d33777ac2bb97c1e0af89b93e39afbb968e52da580e377042b868a893f108f9490ac72ae44f654e9bbf89fee8c
  status: LOCKED

- path: assets/releases/540/CRIT-composite-dark-540.png
  state: CRITICAL
  transform_class: C₂
  sha3_512: 4132b809d07e88d8b5d35c08bf91d696c30db7dd644fcbd92d6e9a9f8b88f2bfe799ad8353dbd8e5a35cf221b418220f39de48a750fbf61a1602361ffb37167b
  status: LOCKED

- path: assets/releases/540/CRIT-composite-transparent-540.png
  state: CRITICAL
  transform_class: C₂
  sha3_512: 096b413d00cb5ed376b190c8c71c264ef453175143d355fc710fb77768e85e080b23a712e084b1f62975a694f6e53fb7bd046c5777662c112213757ee9c0253e
  status: LOCKED

- path: assets/releases/540/CRIT-composite-white-540.png
  state: CRITICAL
  transform_class: C₂
  sha3_512: 86336e8e1e726013e820db4ae38f93d0b9dd39493ee745b4faa4b1bf79dd27a5ab1221179208ab8fef657a1123ed18a17d3f1e7ce82e4c25f7817c85ffbcef55
  status: LOCKED

- path: assets/releases/540/META-composite-dark-540.png
  state: METACOGNITIVE
  transform_class: σₕ
  sha3_512: 8b2e2bd0a7d2d7958a5e152c576e5f9ec4eff63483e40c4a7c48118b011a5750c80345c1b80f9cd8e0cf4b2b2e1c1199d062c3f873155e134de5bfb68f08bbc4
  status: LOCKED

- path: assets/releases/540/META-composite-transparent-540.png
  state: METACOGNITIVE
  transform_class: σₕ
  sha3_512: 140c7b67ca5c2d6e3cfcaa8faecaeb81517a1c47e447c888cf55b0d88d27b7f23cd932570b80309147101039866f3a7578e393d378ac8c5db8d3b2046deaf8e9
  status: LOCKED

- path: assets/releases/540/META-composite-white-540.png
  state: METACOGNITIVE
  transform_class: σₕ
  sha3_512: 0df765966512a4d48f50b1aefa029403c357924f01c3e2802e7930d82b6521028aa0a9a65ff721b7be59f6e11f1bd52a03b091eaa0715d4bc7d0aea04d46c10f
  status: LOCKED
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

It becomes canonical only by passing the constraints defined here. The hashes listed in §11.4 are the authoritative SHA-3-512 values for the 540 px composite release set; the duplicated ad-hoc block that previously trailed this file has been folded into §11.4 for v1.3.0-rc.
