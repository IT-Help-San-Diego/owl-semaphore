# Owl Semaphore — Release Process (v2.0.2 onward)

This document is the single authoritative recipe for publishing a new
Owl Semaphore release. It is written so that one merge of the release-prep
PR (e.g. PR #13 for v2.0.2) followed by one run of the manual release
workflow produces a clean, reproducible release — without any follow-up
"back-fill" PR, without transient markers in canonical source or PDFs,
and with the matching Zenodo record citing the same documents that the
GitHub release publishes.

The process has two halves:

1. **Source-side** — handled by the release-prep PR. Bumps version stamps,
   regenerates PDFs/hashes/manifest, and lands the editorial changes for
   the release. The source snapshot for the release is final at merge.
2. **Tag + publish-side** — handled by the manual workflow in
   `.github/workflows/release.yml`. Creates the annotated tag, the GitHub
   release, triggers Zenodo ingestion (via the existing GitHub ↔ Zenodo
   integration), and once Zenodo has minted the version-specific DOI,
   records that DOI in the GitHub release notes only.

No source files, PDFs, or tests are edited after the release tag.

---

## 1. DOI strategy (canonical, effective v2.0.2)

This is the convention every release follows from v2.0.2 onward. It is
captured here so future maintainers do not re-derive it.

- The archived source snapshot for each release cites the **stable concept
  DOI** `10.5281/zenodo.19473697`. Zenodo resolves the concept DOI to the
  latest published version, so the source snapshot's citing DOI remains
  stable and correct across releases without rewriting.
- The **version-specific DOI** for the current release is minted by Zenodo
  when the GitHub release is published. That minted DOI is recorded in the
  GitHub release notes only — it is intentionally **not** baked into source
  files, PDFs, `CITATION.cff`, `.zenodo.json`, `INTEGRITY-MANIFEST.md`, or
  the test suite. This eliminates the post-release source-side reapplication
  cycle that earlier releases required.
- Previously published version DOIs (v2.0.1: `10.5281/zenodo.20419874`;
  v2.0.0: `10.5281/zenodo.20418539`; v1.2.0: `10.5281/zenodo.19474599`)
  remain recorded as historical "previous published version" entries in
  `CITATION.cff`, `.zenodo.json`, and the CHANGELOG. They are not rewritten
  when a new version is minted.
- If a *future* project (not Owl Semaphore) ever requires the version-specific
  DOI to appear inside the uploaded PDFs themselves, Zenodo supports
  reserving a DOI before upload. In that workflow the DOI is reserved on
  Zenodo first, written into the PDF source, the PDF is regenerated, and
  only then is the GitHub release published. Owl Semaphore does **not** use
  the reserve-DOI-first workflow because the concept-DOI strategy above
  removes the requirement that drove it.

---

## 2. Source-side: the release-prep PR

Each release-prep PR (e.g. PR #13 for v2.0.2) does, in one pass:

- Bump `VERSION` / `RELEASE_LABEL` in `generate_pdfs.py`.
- Bump version stamps in `README.md`, `CITATION.cff`, `.zenodo.json`,
  `CHANGELOG.md`, `INTEGRITY-MANIFEST.md`, all six `OWL-*.md` sources,
  `OWL-SEMAPHORE-SYSTEM.md`, `OWL-SEMAPHORE-EXPLANATION.md`, the
  `Makefile`, `scripts/compute_hashes.py`, `scripts/update_manifest.py`,
  and `tests/test_banner_tuple.py`.
- Update DOI references in source to point at the **concept DOI** and the
  prior published version DOI(s). Do **not** write the new release's
  version-specific DOI into source — it does not exist yet, and even after
  Zenodo mints it, source is not back-filled.
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
  carries the new version stamp and the canonical math tuples; the
  forbidden-token test verifies no transient cleanup markers leaked into
  canonical release-facing files or PDFs.

When the prep PR merges, the `main` branch contains the final source
snapshot for the release. No further source edits happen for this release.

---

## 3. Tag + publish-side: the manual release workflow

The manual workflow lives at `.github/workflows/release.yml` and is
dispatched by hand from the GitHub Actions tab (or via `gh workflow run`).

It takes two inputs:

- `version` — required, e.g. `v2.0.2`. Must start with `v` and must not
  already exist as a tag on the repository.
- `target_sha` — required, the merge-commit SHA on `main` to tag. Pinning
  the SHA explicitly prevents accidentally tagging a later commit if `main`
  advanced between merge and dispatch.

The workflow runs, in order:

1. **Checkout** the supplied `target_sha`.
2. **Guard: tag does not exist.** If the supplied `version` already exists
   as a tag, the workflow fails immediately.
3. **Guard: clean forbidden-token + banner-tuple tests on `target_sha`.**
   The workflow runs `make test` against the checked-out SHA. If any
   canonical release-facing file or PDF contains a transient cleanup
   marker, or any PDF banner tuple disagrees with the expected math
   tuples, the workflow fails before any tag, release, or upload happens.
4. **Create the annotated tag at `target_sha`** and push it to origin.
   The tag message is the release title.
5. **Build the release bundle.** Reuses the same file set as
   `release-assets.yml` for tag-triggered builds: every canonical `.md`,
   every PDF, `LICENSE`, `INTEGRITY-MANIFEST.md`, `RELEASE-HASHES.txt`,
   `VALIDATION-SCRIPT-SPEC.md`, and `assets/`. The bundle is zipped as
   `owl-semaphore-${version}.zip`.
6. **Create the GitHub Release** at the new tag. The release notes are
   assembled from the matching `<!-- BEGIN vX.Y.Z RELEASE BLOCK -->` /
   `<!-- END vX.Y.Z RELEASE BLOCK -->` section of `CHANGELOG.md`. The
   release is created as a normal, published release; it is not a
   pre-release and it is not a workflow holding area.
7. **Trigger Zenodo ingestion.** Publishing the GitHub release fires the
   existing GitHub ↔ Zenodo integration, which produces a new Zenodo
   record and mints a version-specific DOI for the release.
8. **Wait for Zenodo to mint the version-specific DOI.** The workflow
   polls the Zenodo public REST API for the concept record
   (`10.5281/zenodo.19473697`) until either a new version-specific DOI
   appears for the current `version` or a polling budget elapses. Polling
   uses only the public Zenodo API and requires no Zenodo token in the
   workflow.
9. **Record the minted DOI in the GitHub release notes.** When polling
   resolves, the workflow appends a single line to the existing release
   notes via the GitHub REST API using the default `GITHUB_TOKEN`:
   ```
   v2.0.2 version DOI: 10.5281/zenodo.<minted>
   ```
   No source file is edited. No new commit is made. No new tag is created.
10. **If polling did not resolve in budget**, the workflow exits non-fatal
    with a console note. The minted DOI can be added by hand to the release
    notes later — still without any source-side change.

---

## 4. Why no follow-up cleanup PR is required

Earlier releases (v2.0.0, v2.0.1) used a "back-fill" PR after the Zenodo
DOI was minted, to rewrite the version-specific DOI into source files,
PDFs, and metadata. v2.0.2 eliminates that step:

- The source's citing DOI is the **concept DOI**, which is stable across
  releases.
- The version-specific DOI lives in the GitHub release notes, where it can
  be appended by the workflow (or, as a fallback, by hand) without
  re-tagging, re-merging, or amending any source file.
- The forbidden-token test (`tests/test_forbidden_tokens.py`) enforces
  that no transient cleanup marker (`TBD`, `placeholder`,
  `not yet minted`, `temporary`, `back-fill`, etc.) leaks into canonical
  release-facing files or PDFs. The current-release block of
  `CHANGELOG.md` is also scanned. Old releases' CHANGELOG entries are
  outside the scanned block and are preserved verbatim.

The forbidden-token test deliberately does not scan `.github/workflows/`.
Action vocabulary such as the GitHub API's pre-release flag must remain
usable in workflow code without leaking false positives into source.
Whenever the workflow uses such vocabulary in passing, comments prefer
the neutral phrasing "staged" or "awaiting DOI" so the workflow's intent
is still readable.

---

## 5. Recommended human steps for v2.0.2

After PR #13 is merged to `main`:

1. From the GitHub Actions tab, run the **Release** workflow
   (`release.yml`) with:
   - `version`: `v2.0.2`
   - `target_sha`: the merge-commit SHA of PR #13 into `main`
2. Watch the workflow run. The early steps (guard checks, `make test` on
   the target SHA, tag creation, GitHub release creation) complete in
   under a few minutes. The Zenodo polling step then waits for the
   GitHub ↔ Zenodo integration to ingest the new release and mint the
   version-specific DOI.
3. When the workflow's Zenodo-polling step completes, confirm on the
   Zenodo dashboard that the v2.0.2 record was created and the
   version-specific DOI was minted, and confirm the GitHub release notes
   now end with a single `v2.0.2 version DOI: ...` line.
4. If polling timed out (Zenodo can take longer than the polling budget
   under load), copy the minted DOI from the Zenodo dashboard and append
   the same `v2.0.2 version DOI: 10.5281/zenodo.<minted>` line to the
   GitHub release notes by hand. Do **not** open a source-side back-fill
   PR; the source snapshot is final at the merge commit.
5. Verify:
   - The v2.0.2 Zenodo landing page resolves and renders correctly.
   - `CITATION.cff` cffinit-lints clean (it already cites the concept
     DOI).
   - The v2.0.0 and v2.0.1 tags, releases, and DOIs are untouched.

That is the entire v2.0.2 publication recipe.
