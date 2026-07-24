"""Forbidden-token / transient-marker scan for canonical release-facing files.

Owl Semaphore v2.0.2+ (current release v3.0.1) treats source files, generated PDFs, and machine-readable
metadata as final, archival artifacts. The repository convention is that no
transient cleanup tokens appear in those artifacts: no draft DOI markers, no
"to be computed" / "to be measured" / "to be verified" sentinels, no Wikipedia
URLs, no work-in-progress wording.

This test enforces that convention. It scans:

  - The canonical release-facing markdown / metadata files at the repo root
    (README, CITATION.cff, .zenodo.json, INTEGRITY-MANIFEST, the OWL specs,
    the explanation, the Zenodo release checklist, the Makefile).
  - The current-release block of CHANGELOG.md, delimited by the HTML markers
    ``<!-- BEGIN v3.0.1 RELEASE BLOCK -->`` and ``<!-- END v3.0.1 RELEASE
    BLOCK -->``. Historical entries for older releases live outside that
    block and are intentionally preserved verbatim.
  - The full text of every generated PDF in the release set, as extracted by
    ``pdftotext -layout``.

For each scanned region, the test fails on any case-insensitive occurrence of
the forbidden token set. The token set is the project's running list of
transient cleanup markers and external-link policy violations; extend it as
new markers are introduced and retired.

PDF scans are skipped (not failed) for any PDF that is not present on disk so
that ``make test`` remains usable in a clean checkout before ``make pdfs`` has
been run.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Tokens that must not appear in canonical release-facing files or PDFs.
# Matching is case-insensitive and substring-based; multi-word tokens are
# matched as substrings on the lowercased text so internal whitespace is
# treated literally.
#
# Note (v2.0.2): the word "draft" is intentionally NOT a forbidden token
# any more, because the reserve-DOI-first release workflow legitimately
# refers to "Zenodo new-version drafts" in process documentation
# (`ZENODO-RELEASE-CHECKLIST.md`, `RELEASE-PROCESS.md`). The durable
# transient-marker list below stays tightly focused on cleanup markers
# (TBD, placeholder, pending, not yet minted, temporary, to_be_*, the
# back-fill family) and the no-Wikipedia external-link rule.
FORBIDDEN_TOKENS = (
    "TBD",
    "placeholder",
    "pending",
    "not yet minted",
    "temporary",
    "Wikipedia",
    "TO_BE_COMPUTED",
    "TO_BE_VERIFIED",
    "TO_BE_MEASURED",
    "back-fill",
    "backfill",
)

# Canonical release-facing files at the repo root. CHANGELOG.md is handled
# separately (only its current-release block is scanned).
RELEASE_FACING_FILES = (
    "README.md",
    "CITATION.cff",
    ".zenodo.json",
    "INTEGRITY-MANIFEST.md",
    "ZENODO-RELEASE-CHECKLIST.md",
    "OWL-SEMAPHORE-SYSTEM.md",
    "OWL-SEMAPHORE-EXPLANATION.md",
    "OWL-1-NORMATIVE.md",
    "OWL-2-NON-NORMATIVE.md",
    "OWL-3-CRITICAL.md",
    "OWL-4-METACOGNITIVE.md",
    "Makefile",
)

CHANGELOG_PATH = "CHANGELOG.md"
CHANGELOG_BEGIN_MARKER = "<!-- BEGIN v3.0.1 RELEASE BLOCK -->"
CHANGELOG_END_MARKER = "<!-- END v3.0.1 RELEASE BLOCK -->"

PDF_FILES = (
    "OWL-SEMAPHORE-SYSTEM.pdf",
    "OWL-SEMAPHORE-EXPLANATION.pdf",
    "OWL-1-NORMATIVE.pdf",
    "OWL-2-NON-NORMATIVE.pdf",
    "OWL-3-CRITICAL.pdf",
    "OWL-4-METACOGNITIVE.pdf",
)


def _scan_text(text: str, source_label: str) -> list[str]:
    """Return a list of human-readable hit descriptions for forbidden tokens."""
    hits: list[str] = []
    lower = text.lower()
    for token in FORBIDDEN_TOKENS:
        needle = token.lower()
        if needle in lower:
            # Build a small context excerpt for the first occurrence so the
            # failure message points the reader at the right place.
            idx = lower.find(needle)
            start = max(0, idx - 40)
            end = min(len(text), idx + len(token) + 40)
            excerpt = text[start:end].replace("\n", " ⏎ ")
            hits.append(f"{source_label}: forbidden token {token!r} -> ...{excerpt}...")
    return hits


def _extract_pdf_text(pdf_path: str) -> str:
    if not shutil.which("pdftotext"):
        raise unittest.SkipTest("pdftotext not available in this environment")
    out = subprocess.run(
        ["pdftotext", "-layout", pdf_path, "-"],
        capture_output=True,
        text=True,
        check=False,
    )
    if out.returncode != 0:
        raise AssertionError(f"pdftotext failed for {pdf_path}: {out.stderr}")
    return out.stdout


def _read_changelog_current_block() -> str:
    path = os.path.join(REPO, CHANGELOG_PATH)
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if CHANGELOG_BEGIN_MARKER not in text or CHANGELOG_END_MARKER not in text:
        raise AssertionError(
            f"{CHANGELOG_PATH} is missing the v3.0.1 release-block markers "
            f"{CHANGELOG_BEGIN_MARKER!r} and {CHANGELOG_END_MARKER!r}"
        )
    begin = text.index(CHANGELOG_BEGIN_MARKER) + len(CHANGELOG_BEGIN_MARKER)
    end = text.index(CHANGELOG_END_MARKER)
    return text[begin:end]


class ForbiddenTokenTest(unittest.TestCase):
    """Verify that transient cleanup markers do not appear in release-facing files."""

    def test_release_facing_files_have_no_forbidden_tokens(self):
        all_hits: list[str] = []
        for rel in RELEASE_FACING_FILES:
            path = os.path.join(REPO, rel)
            if not os.path.exists(path):
                continue
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
            all_hits.extend(_scan_text(text, rel))
        self.assertEqual(all_hits, [], "\n".join(all_hits) or "no hits")

    def test_changelog_current_release_block_has_no_forbidden_tokens(self):
        block = _read_changelog_current_block()
        hits = _scan_text(block, f"{CHANGELOG_PATH} (v3.0.1 block)")
        self.assertEqual(hits, [], "\n".join(hits) or "no hits")

    def test_canonical_pdfs_have_no_forbidden_tokens(self):
        all_hits: list[str] = []
        any_scanned = False
        for pdf_name in PDF_FILES:
            pdf_path = os.path.join(REPO, pdf_name)
            if not os.path.exists(pdf_path):
                continue
            text = _extract_pdf_text(pdf_path)
            any_scanned = True
            all_hits.extend(_scan_text(text, pdf_name))
        if not any_scanned:
            self.skipTest("no PDFs present yet (run `make pdfs`)")
        self.assertEqual(all_hits, [], "\n".join(all_hits) or "no hits")

    def test_no_transient_canonical_output_filenames(self):
        """Canonical generated output filenames must not carry rc/prep/draft/temp markers."""
        forbidden_filename_markers = ("rc-", "rc_", "prep-", "prep_", "draft-", "draft_", "temp-", "temp_", "tmp-", "tmp_")
        offenders: list[str] = []
        for pdf_name in PDF_FILES:
            lowered = pdf_name.lower()
            for marker in forbidden_filename_markers:
                if marker in lowered:
                    offenders.append(f"{pdf_name} contains canonical-filename marker {marker!r}")
        # Also check any *.pdf at the repo root in case future PDFs land here.
        for entry in os.listdir(REPO):
            if entry.lower().endswith(".pdf"):
                lowered = entry.lower()
                for marker in forbidden_filename_markers:
                    if marker in lowered:
                        offenders.append(f"{entry} contains canonical-filename marker {marker!r}")
        self.assertEqual(offenders, [], "\n".join(offenders) or "no offenders")


if __name__ == "__main__":
    unittest.main()
