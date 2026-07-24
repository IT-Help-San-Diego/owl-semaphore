# Owl Semaphore — Release Process (v2.0.2 onward)

This document is the single authoritative recipe for publishing a new
Owl Semaphore release. It is written so that one merge of the release-prep
PR (e.g. PR #13 for v2.0.2) followed by a small, deterministic set of
human steps produces a clean, reproducible release in which the exact
reserved version-specific DOI appears inside every published artifact —
without any post-release source-side reapplication, without transient
markers in canonical source or PDFs, and without producing a duplicate
Zenodo record via GitHub auto-ingest.

> **v3.0.1 status (DOI reserved; upload + publish remain).** The v3.0.1
> version-specific DOI **`10.5281/zenodo.21524422`** was reserved on a
> Zenodo new-version draft of the concept record via
> `owl-press zenodo new-version` (draft URL:
> `https://zenodo.org/deposit/21524422`) and embedded as the citing DOI
> in `generate_pdfs.py` (as of v3.0.1 a thin driver over the
> `owl-semaphore-press` package), the PDFs, `CITATION.cff`,
> `.zenodo.json`, `README.md`, `OWL-SEMAPHORE-EXPLANATION.md`, the
> CHANGELOG release block, and the banner-tuple test. The §4 steps for
> v3.0.1 — tag at the merge commit, GitHub Release, upload the released
> files into draft 21524422 (`owl-press zenodo upload 21524422 <files>
> --fresh`), publish (`owl-press zenodo publish 21524422 --yes`), and
> verify exactly one Zenodo record — are performed after the
> release-prep PR merges.

> **v3.0.0 status (DOI published).** The v3.0.0 version-specific DOI
> **`10.5281/zenodo.20468727`** was reserved on a Zenodo new-version
> draft of the concept record, embedded as the citing DOI in
> `generate_pdfs.py`, the PDFs, `CITATION.cff`, `.zenodo.json`,
> `README.md`, and the CHANGELOG release block, and the Zenodo record
> was **published on 2026-05-31**
> (`https://doi.org/10.5281/zenodo.20468727`). The concept DOI
> `10.5281/zenodo.19473697` (all-versions; resolves to the latest
> published version) is preserved as the durable cross-version citation
> target. Both the reserve-and-swap controlled step (§0 below) and the
> upload + publish step (§4) are **complete** for v3.0.0; no DOI-related
> actions remain for this release.

---

## 0. v3.0.0 controlled DOI step (reserve + swap) — COMPLETE

This controlled step has been performed for v3.0.0. It is recorded here
for provenance:

1. On Zenodo, a *new-version* draft of the concept record (concept DOI
   `10.5281/zenodo.19473697`) was created and the v3.0.0 version DOI
   **`10.5281/zenodo.20468727`** was reserved. Draft URL:
   `https://zenodo.org/uploads/20468727`.
2. The reserved DOI was set as `VERSION_DOI` in `generate_pdfs.py` and as
   the matching constant in `tests/test_banner_tuple.py`.
3. `make pdfs hashes manifest test` was re-run once. The banner-tuple test
   asserts the reserved version DOI; the forbidden-token test passes
   because a real DOI is not a transient marker.
4. The tag + publish steps in §4 were subsequently completed: the
   released files were uploaded into the same Zenodo draft the DOI was
   reserved on, and that draft was published on 2026-05-31. The DOI now
   resolves to the live v3.0.0 record.

The process has three halves:

1. **Pre-source-side (Zenodo reserve DOI).** Before opening or finalizing
   the release-prep PR, create a Zenodo *new-version* draft for the
   concept record and reserve the version DOI. The reserved DOI is the
   value that gets embedded into source, PDFs, and metadata.
2. **Source-side (release-prep PR).** Bumps version stamps, embeds the
   reserved version-specific DOI in `generate_pdfs.py`, `CITATION.cff`,
   `.zenodo.json`, `README.md`, the `CHANGELOG.md` release block, all
   canonical `OWL-*.md` source, `INTEGRITY-MANIFEST.md`, and the
   banner-tuple test. Regenerates PDFs / hashes / manifest. The source
   snapshot for the release is final at merge.
3. **Tag + publish-side (manual, guard-railed).** Creates the annotated
   tag, the GitHub Release, and **uploads the exact released files into
   the same Zenodo draft that the reserved DOI was minted on**, then
   publishes that Zenodo draft. The repository's GitHub auto-ingest path
   to Zenodo is intentionally avoided for this release so that the
   reserved DOI is the canonical (and only) Zenodo record for the
   release.

No source files, PDFs, or tests are edited after the release tag.

---

## 1. DOI strategy (canonical, effective v2.0.2)

This is the convention every release follows from v2.0.2 onward.

- The **version-specific DOI** for the release is reserved on a Zenodo
  *new-version* draft of the concept record (concept DOI
  `10.5281/zenodo.19473697`) **before** the release-prep PR is finalized.
  The reserved DOI is embedded directly into source files, PDFs, and
  metadata: `generate_pdfs.py`, `CITATION.cff`, `.zenodo.json`,
  `README.md`, `CHANGELOG.md` (current release block),
  `OWL-SEMAPHORE-EXPLANATION.md`, `INTEGRITY-MANIFEST.md`, and the
  banner-tuple test. The exact version DOI therefore appears inside every
  PDF page-one banner tuple and footer, every metadata file, and every
  published artifact Zenodo archives.
- The **concept DOI `10.5281/zenodo.19473697`** is preserved as the
  *all-versions* DOI for cross-version citation. It is unchanged across
  releases and resolves to the latest published version.
- Previously published version DOIs (v2.0.1: `10.5281/zenodo.20419874`;
  v2.0.0: `10.5281/zenodo.20418539`; v1.2.0: `10.5281/zenodo.19474599`)
  remain recorded as historical "previous published version" entries in
  `CITATION.cff`, `.zenodo.json`, and the CHANGELOG. They are not rewritten
  when a new version is minted.
- For v2.0.2 specifically: the reserved version DOI is
  `10.5281/zenodo.20433053`, on Zenodo draft URL
  `https://zenodo.org/uploads/20433053`.

This convention eliminates the post-release source-side reapplication
cycle that earlier releases (v2.0.0, v2.0.1) required, because the
version DOI is known before the PDFs are generated.

---

## 2. Avoiding duplicate Zenodo records (GitHub auto-ingest)

This repository is connected to Zenodo via the GitHub ↔ Zenodo
integration. By default, publishing a GitHub Release triggers Zenodo to
auto-ingest the release and **mint a brand-new version DOI**, which is
*different* from the DOI reserved on the manual Zenodo draft. That would
produce two Zenodo records for the same release — one whose files match
what the source/PDFs cite (the reserved DOI), and one created by
auto-ingest with a different DOI. Citation integrity requires exactly one
Zenodo record per release.

The v2.0.2 release process therefore intentionally **does not** trigger
the GitHub auto-ingest path. The operator follows one of these mutually
exclusive paths:

### Path A (recommended for v2.0.2 — manual Zenodo draft is canonical)

The reserved Zenodo draft already has the version DOI minted on it. The
operator uploads the exact released files into the same draft and
publishes the draft from the Zenodo UI. The GitHub Release is still
created (so users can find the source and tag), but no auto-ingest is
allowed to fire toward Zenodo for this release. Practical ways to keep
auto-ingest from firing a second time include:

- Temporarily disabling the repository in the Zenodo *GitHub* settings
  panel before publishing the GitHub Release, and re-enabling it
  afterwards. (No tokens are needed for this; it is a UI toggle on the
  Zenodo side.)
- Or, if the repository must stay enabled, watching the Zenodo dashboard
  during step 5 of §4 and immediately discarding any unpublished
  duplicate Zenodo draft that the integration creates, before it can be
  published. Zenodo allows unpublished drafts to be discarded; published
  records cannot be deleted, so the operator must act before the
  duplicate is finalized.

Path A is the recommended path for v2.0.2 because the reserved DOI
`10.5281/zenodo.20433053` is already embedded in the released PDFs and
metadata. The release is only valid if the published Zenodo record uses
that exact DOI.

### Path B (future releases — switch fully to manual)

For future releases the project may choose to disable the GitHub ↔ Zenodo
auto-ingest integration entirely and rely on the manual draft + publish
flow described above. That path eliminates the duplicate-record race
condition by construction. Switching paths is a project policy decision
documented in this file; the source-side files do not change.

---

## 3. Source-side: the release-prep PR

Each release-prep PR (e.g. PR #13 for v2.0.2) does, in one pass:

- Reserve the version-specific DOI on a Zenodo *new-version* draft of the
  concept record **before** finalizing the PR. Record the draft URL and
  the reserved DOI in the PR description so reviewers can verify.
- Bump `VERSION` / `RELEASE_LABEL` in `generate_pdfs.py` and update
  `VERSION_DOI` to the reserved version DOI.
- Bump version stamps in `README.md`, `CITATION.cff`, `.zenodo.json`,
  `CHANGELOG.md`, `INTEGRITY-MANIFEST.md`, all six `OWL-*.md` sources,
  `OWL-SEMAPHORE-SYSTEM.md`, `OWL-SEMAPHORE-EXPLANATION.md`, the
  `Makefile`, `scripts/compute_hashes.py`, `scripts/update_manifest.py`,
  and `tests/test_banner_tuple.py`.
- Update DOI references in source to embed the reserved version DOI as
  the citing DOI, preserve the concept DOI as the all-versions DOI, and
  preserve the previously published version DOIs unchanged.
- Promote any `[Unreleased]` block of `CHANGELOG.md` into the new
  `[vX.Y.Z]` block, wrapped by the matching
  `<!-- BEGIN vX.Y.Z RELEASE BLOCK -->` / `<!-- END vX.Y.Z RELEASE BLOCK -->`
  markers. Update `tests/test_forbidden_tokens.py`'s
  `CHANGELOG_BEGIN_MARKER` / `CHANGELOG_END_MARKER` constants to match.
- Regenerate PDFs, hashes, and manifest:
  ```
  make pdfs
  make hashes
  make manifest
  make test
  ```
- Confirm `make test` passes — the banner-tuple test verifies every PDF
  carries the new version stamp, the reserved version DOI, the concept
  DOI, the previous version DOI, and the canonical math tuples; the
  forbidden-token test verifies no transient cleanup markers leaked into
  canonical release-facing files or PDFs.

When the prep PR merges, the `main` branch contains the final source
snapshot for the release, with the reserved version DOI baked into every
published artifact. No further source edits happen for this release.

---

## 4. Tag + publish-side: human steps (no auto-ingest)

The v2.0.2 release publish flow is intentionally a small set of explicit
human steps, not an automated workflow that publishes a GitHub Release
and lets Zenodo auto-ingest mint a second DOI.

After PR #13 is merged into `main`:

1. **Tag the release at the merge commit.**
   ```
   git fetch origin
   git checkout main
   git pull --ff-only origin main
   git tag -a v2.0.2 <MERGE_COMMIT_SHA> -m "Owl Semaphore v2.0.2"
   git push origin refs/tags/v2.0.2
   ```
   The `release-assets.yml` workflow fires on tag push and builds the
   canonical release bundle (`owl-semaphore-v2.0.2.zip`). The bundle
   contents are defined by `RELEASE-BUNDLE-MANIFEST.txt` at the repo
   root (single source of truth); the workflow reads that manifest and
   `tests/test_release_bundle.py` enforces in CI that every required
   release artifact is listed. That workflow only attaches assets to the
   GitHub Release it creates — it does not talk to Zenodo.
2. **Prepare the manual Zenodo draft for upload.** Open the Zenodo draft
   that has the reserved DOI minted on it (for v2.0.2:
   `https://zenodo.org/uploads/20433053`). Confirm the version field is
   `v2.0.2`, the DOI is `10.5281/zenodo.20433053`, and the metadata
   matches `.zenodo.json` from the merge commit.
3. **Avoid GitHub auto-ingest before creating the GitHub Release.** In
   the Zenodo *GitHub* settings panel, temporarily disable the
   `owl-semaphore` repository toggle. (Re-enable it after step 7 if
   future releases will continue to use the integration.) This step
   prevents the GitHub Release in step 4 from triggering a second
   Zenodo ingestion that would mint a different DOI.
4. **Create the GitHub Release at the tag.** Title it
   `Owl Semaphore v2.0.2`. Use the `[v2.0.2]` block of `CHANGELOG.md` as
   the release notes. The release notes already cite the reserved DOI
   `10.5281/zenodo.20433053`; no additional DOI line needs to be appended.
5. **Upload the exact released files to the Zenodo draft.** Use the
   `owl-semaphore-v2.0.2.zip` bundle produced by `release-assets.yml`
   (or, equivalently, the individual canonical PDFs / source markdown /
   LICENSE / manifest / hashes attached to the GitHub Release). The
   uploaded files must be byte-identical to the files at the tagged
   commit; do not regenerate them locally.
6. **Publish the Zenodo draft from the Zenodo UI.** Confirm the published
   Zenodo record has DOI `10.5281/zenodo.20433053` and that the files
   match the GitHub Release bundle.
7. **Verify there is exactly one Zenodo record for v2.0.2.** Open the
   concept record's "Versions" tab and confirm the v2.0.2 entry is the
   one with DOI `10.5281/zenodo.20433053`. If a duplicate draft was
   auto-created by GitHub-Zenodo, discard it (drafts can be deleted).
8. **Optional: re-enable the Zenodo GitHub integration** for future
   releases. The next release-prep PR's pre-source step will again
   reserve a DOI on a fresh Zenodo draft, and this procedure repeats.

---

## 5. Why no follow-up cleanup PR is required

Earlier releases (v2.0.0, v2.0.1) used a post-release source-side
reapplication PR after the Zenodo DOI was minted, to rewrite the
version-specific DOI into source files, PDFs, and metadata. v2.0.2
eliminates that step:

- The version-specific DOI is reserved on Zenodo **before** PDFs are
  generated, so it is embedded directly into source, PDFs, and metadata
  on the first pass.
- The forbidden-token test (`tests/test_forbidden_tokens.py`) enforces
  that no transient cleanup marker (`TBD`, `placeholder`,
  `not yet minted`, `temporary`, etc.) leaks into canonical
  release-facing files or PDFs. The current-release block of
  `CHANGELOG.md` is also scanned. Old releases' CHANGELOG entries are
  outside the scanned block and are preserved verbatim.

The forbidden-token test deliberately does not scan `.github/workflows/`
or process documentation (`RELEASE-PROCESS.md`,
`ZENODO-RELEASE-CHECKLIST.md`), because vocabulary used to *forbid* such
markers must remain usable in those files without leaking false positives.

---

## 6. Recommended human steps for v2.0.2

After PR #13 is merged to `main`, follow §4 step-by-step.

- The Zenodo draft URL for v2.0.2 is `https://zenodo.org/uploads/20433053`.
- The reserved v2.0.2 version DOI is `10.5281/zenodo.20433053`.
- The concept DOI is `10.5281/zenodo.19473697`.
- The previous-published version DOI (v2.0.1) is
  `10.5281/zenodo.20419874`.
- The earlier-published version DOIs (v2.0.0, v1.2.0) are
  `10.5281/zenodo.20418539` and `10.5281/zenodo.19474599`.

The v2.0.0 and v2.0.1 tags, their GitHub Releases, and their published
Zenodo DOIs are not modified by the v2.0.2 release.
