

# OWL SEMAPHORE — INTEGRITY MANIFEST

## Version 3.0.1

> Stamped v3.0.1 for the PATCH-level errata release (the §4A.1 locus-axis clarifying sentence) and the switch of PDF generation to the parity-proven `owl-semaphore-press` package. The integrity regime is unchanged from v2.0.2: tracked specification files carry SHA-3-512 digests; the explanation document, CHANGELOG, regenerated PDFs, and assets are covered. The asset-record markers under §11.2 for master / layer / export PNGs are carried forward unchanged from the v2.0.2 manifest; the canonical asset set under `assets/` is unchanged for v3.0.1 (this release alters specification text, metadata, and the rendering toolchain, not artwork). All hash values in this file derive from a single generated source: `scripts/compute_hashes.py` writes `RELEASE-HASHES.txt`, and `scripts/update_manifest.py` rewrites both the generated-hash block at the bottom of this file and the `sha3_512:` values in the §11.1 records from it. Do not hand-edit either; run `make hashes` + `make manifest` after any change to a tracked file.

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
  sha3_512: 049e3b8219042cf50b6a367b59b02aa24a1194ad4141330a4daa1db3693d62b903edf4a5f2d1336947cc6f13e301a04e9110a6722ff4fa1998ffd225f5b17c2c
  status: WORKING
  notes: Root system specification (v3.0.1)

- path: OWL-1-NORMATIVE.md
  role: state specification
  state: NORMATIVE
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: I
  sha3_512: ded3c57d4e1bbb477fecab536aa326554c8d7434686d44b7e653ce1323d94aa5ea45faa25bbcd510cd7601654538cdecc0d278ede74032eea5891a7b66d58d15
  status: WORKING
  notes: Normative state specification (v3.0.1)

- path: OWL-2-NON-NORMATIVE.md
  role: state specification
  state: NON-NORMATIVE
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: σᵥ
  sha3_512: 368e1dead57d3611cbec8b55f89e09d8b228c8720e3f1afaeaadb5c3d038244a9115a75a281b0007f04285a01d4b852f3c86597653ba11d497f60efaeec2ca19
  status: WORKING
  notes: Non-normative state specification (v3.0.1)

- path: OWL-3-CRITICAL.md
  role: state specification
  state: CRITICAL
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: C₂
  sha3_512: 7b6292ed5523dc18a0ddfb3ab87d06ab084e115fbfc9d7fbdef5c956efecb8c816ab09c493d835dbde981b2aedf74db9ca42f4004729a9e13d5dab340c73c2f2
  status: WORKING
  notes: Critical state specification (v3.0.1)

- path: OWL-4-METACOGNITIVE.md
  role: state specification
  state: METACOGNITIVE
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: σₕ
  sha3_512: 7afbe4a316159048711cbd353cac788694369edbb3fbe99bd2708f8266f771f33249dacd30e3fa16f31d5189a5c849b25e4d621fae93e833153c1a6a97231bb5
  status: WORKING
  notes: Metacognitive state specification (v3.0.1) — phrasing "The observer audits the frame" carried over from v2.0.0

- path: README.md
  role: repository overview
  state: system
  type: markdown
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: n/a
  sha3_512: f27a5115828b39a8dd0289bd77962ac312196cf84d136f1750410c282b1fb88624e535b4cccdd01e26ad837e76d937722c3f289eb395a6f40beb12baeac8baec
  status: WORKING
  notes: Publication-facing repository overview (v3.0.1)

- path: CITATION.cff
  role: citation metadata
  state: system
  type: yaml
  dimensions: n/a
  mode: text
  alpha_status: n/a
  transform_class: n/a
  sha3_512: 8acce586a17fa45d7a6a5297ed7e16bb6eaf53c6cf21eae57e3458cf9425bb1aebf1ba13bc0d1e006b7346eeb3386d7d671c6c6ffe7edaf357118b1898d3e792
  status: WORKING
  notes: Citation metadata (v3.0.1); cites the v3.0.1 version-specific DOI 10.5281/zenodo.21524422 (reserved on Zenodo) as the citing DOI; concept DOI 10.5281/zenodo.19473697 (all-versions; resolves to latest published version) retained as the cross-version citation target; v3.0.0 version DOI 10.5281/zenodo.20468727 retained as previous published; v2.0.2 version DOI 10.5281/zenodo.20433053, v2.0.1 version DOI 10.5281/zenodo.20419874, and v2.0.0 version DOI 10.5281/zenodo.20418539 retained as earlier published
```

### 11.2 Asset Records

Finalized asset records are added here, one entry per asset, using the canonical record format defined in §10. Each entry records the concrete measurements (`dimensions`, `mode`, `alpha_status`, `transform_class`) and the SHA-3-512 digest of the asset file, with a one-line `notes` field describing the asset's role in the release. Entries are added as assets are frozen and hashed; the v3.0.1 release does not introduce new asset entries because the asset set under `assets/` is unchanged from v2.0.2.

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

## Generated Hash Records (v3.0.1)

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
OWL-SEMAPHORE-SYSTEM.pdf: 683f4f99ac4a3b303b0893b5f09f05ce95e0ee00c5a2206293d730b9ee481663c175a78295a2b61ed1d4e591d16182b7fd284a77b9711dcbffc3add67be1d67e
OWL-SEMAPHORE-EXPLANATION.pdf: d46dd8bb5d285efe08c5a9ee457b2a22411b730a3ede0a08c15e23353e5d2fa5a133b1e6719329e47fdb76008461b1db47ec7c18f9394efb8210aae3f59765e1
OWL-1-NORMATIVE.pdf: 3ad2899d46427bbabb23b3bd95309641e7b27fe65c621858aecb86dcf8e2b227103d34226c3d2435b35e7175897f8296cd6831baba190c04150c2e4e506585ba
OWL-2-NON-NORMATIVE.pdf: 85337aaf06b20f159ddc33de4fce460eda1d8a35d13cfebe9e35677bfa0439731dfdba38acb4c5bb0f9d780c27b4cdc8042341a1a1d792e2188a0314c74ee2aa
OWL-3-CRITICAL.pdf: d30f283bbe7ad57e9ca84a7c8bfc02c35f56f958e0f12fdcbf21594d904d5ab0ddec29fd2ca063096af95f02ccf1d960f100f5f4cfd816b9a7030847dbf85a50
OWL-4-METACOGNITIVE.pdf: 18add5baba13ed385f0bfa4c29886b5a9f4108435ea40b3ce23f4976374d7031cddc06446225204332526cfbb61eb1f576db58503e5d4dedbf1872839d899b5d
README.md: f27a5115828b39a8dd0289bd77962ac312196cf84d136f1750410c282b1fb88624e535b4cccdd01e26ad837e76d937722c3f289eb395a6f40beb12baeac8baec
CHANGELOG.md: 1718bf5aa3a950817763855ad23687bfa8a2c2c4b0b2479ec49f1b6228c1ab6f3043e79cf170780290066648750982771624064425a059b3a9dfc307be094d5d
OWL-SEMAPHORE-SYSTEM.md: 049e3b8219042cf50b6a367b59b02aa24a1194ad4141330a4daa1db3693d62b903edf4a5f2d1336947cc6f13e301a04e9110a6722ff4fa1998ffd225f5b17c2c
OWL-SEMAPHORE-EXPLANATION.md: 12642806e7476bd2815a610f3fd54768be279146eabf562df138c4011c2698be6c4d3b08a8d69d7ae11757950e259d00a59817785a1914c538ff5e4985af4c48
OWL-1-NORMATIVE.md: ded3c57d4e1bbb477fecab536aa326554c8d7434686d44b7e653ce1323d94aa5ea45faa25bbcd510cd7601654538cdecc0d278ede74032eea5891a7b66d58d15
OWL-2-NON-NORMATIVE.md: 368e1dead57d3611cbec8b55f89e09d8b228c8720e3f1afaeaadb5c3d038244a9115a75a281b0007f04285a01d4b852f3c86597653ba11d497f60efaeec2ca19
OWL-3-CRITICAL.md: 7b6292ed5523dc18a0ddfb3ab87d06ab084e115fbfc9d7fbdef5c956efecb8c816ab09c493d835dbde981b2aedf74db9ca42f4004729a9e13d5dab340c73c2f2
OWL-4-METACOGNITIVE.md: 7afbe4a316159048711cbd353cac788694369edbb3fbe99bd2708f8266f771f33249dacd30e3fa16f31d5189a5c849b25e4d621fae93e833153c1a6a97231bb5
INTEGRITY-MANIFEST.md: 55918395df7689686aa29b3223cac7f9f08bd6c321c44fe0cbe965d5655dce9b642e55aa0cd595f0bbb9894d72d0f49c63fa1c633ff388960851e71e3d4c359b
CITATION.cff: 8acce586a17fa45d7a6a5297ed7e16bb6eaf53c6cf21eae57e3458cf9425bb1aebf1ba13bc0d1e006b7346eeb3386d7d671c6c6ffe7edaf357118b1898d3e792
.zenodo.json: e10220009081242f6fc626117c5ae26133b57f77304eeed41f2dad433ba82c520728b3516331701baaea4299a8bab37efadb687d2f49db9d687298df0400ceb2
```

<!-- END GENERATED HASHES -->
