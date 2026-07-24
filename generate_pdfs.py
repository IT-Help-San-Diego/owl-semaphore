#!/usr/bin/env python3
"""
Generate publication-grade PDFs for the Owl Semaphore system (v3.0.1).

Produces, with one command, six PDFs:
  - OWL-SEMAPHORE-SYSTEM.pdf
  - OWL-SEMAPHORE-EXPLANATION.pdf
  - OWL-1-NORMATIVE.pdf
  - OWL-2-NON-NORMATIVE.pdf
  - OWL-3-CRITICAL.pdf
  - OWL-4-METACOGNITIVE.pdf

As of v3.0.1 this script is a thin driver over the `owl-semaphore-press`
package (https://github.com/IT-Help-San-Diego/owl-semaphore-press), which
carries the codified Owl Semaphore design language extracted from this
repository's legacy v3.0.0 generator. The extraction is parity-proven: the
package's test suite includes a byte-identical Typst-source comparison
against the legacy generator, so the switch does not restyle any artifact.
This repository remains the normative source of the design language; the
package is the rendering instrument, and its identity + version are stamped
into every PDF's Creator metadata as provenance.

Each PDF carries:
  - Per-page owl header (badge thumbnail + state token in the running header)
  - Title page with badge image and banner tuple (state / transform / det / mapping / quote)
  - Contact-sheet header
  - Body content (rendered from the matching .md via pandoc -> typst)
  - Classification ledger back page
  - Footer with version, page numbers, repository URL, DOI
  - Embedded PDF metadata (Title, Author, Subject, Keywords, Producer/Creator)

Requires: pandoc (cli) and the pinned press package with its render extra:

    pip install "owl-semaphore-press[render] @ git+https://github.com/IT-Help-San-Diego/owl-semaphore-press@0.1.0"

(The render extra pulls the `typst` and `pikepdf` Python packages. Pin the
press version: a styling change in the package must never silently restyle
an already-released artifact.)

Usage:  python3 generate_pdfs.py   (or: make pdfs)
"""

from __future__ import annotations

import os
import sys

try:
    from owl_semaphore_press import (
        OWL_SEMAPHORE_DOCS,
        PressConfig,
        RenderError,
        render_pdf,
    )
    from owl_semaphore_press import __version__ as PRESS_VERSION
except ImportError:
    print(
        "ERROR: the 'owl-semaphore-press' package is not installed.\n"
        "Run: pip install \"owl-semaphore-press[render] @ "
        "git+https://github.com/IT-Help-San-Diego/owl-semaphore-press@0.1.0\"",
        file=sys.stderr,
    )
    sys.exit(1)

REPO = os.path.dirname(os.path.abspath(__file__))

# ── Project-wide metadata (v3.0.1) ──────────────────────────────────────────
#
# DOI strategy for the v3.0.1 release. v3.0.1 is a PATCH-level errata release
# (the §4A.1 locus-axis clarifying sentence) that also switches PDF
# generation to the parity-proven owl-semaphore-press package. Per
# RELEASE-PROCESS.md the v3.0.1 version-specific DOI is reserved on a Zenodo
# new-version draft of the concept record before the release-prep PR is
# finalized, embedded here as the citing DOI so it appears inside every PDF
# banner tuple, footer, and metadata file.
#
# Earlier published version DOIs (v3.0.0, v2.0.2, v2.0.1, v2.0.0, v1.2.0)
# remain recorded as historical entries for citation continuity.

VERSION = "3.0.1"
RELEASE_LABEL = "v3.0.1"
AUTHOR = "Carey James Balboa"
ORCID = "0009-0000-5237-9065"
REPO_URL = "github.com/IT-Help-San-Diego/owl-semaphore"
CONCEPT_DOI = "10.5281/zenodo.19473697"  # all-versions concept DOI (resolves to latest)
VERSION_DOI = "10.5281/zenodo.21524422"  # v3.0.1 version-specific DOI (reserved on Zenodo)
CITING_DOI = VERSION_DOI
PREVIOUS_VERSION_DOI = "10.5281/zenodo.20468727"  # v3.0.0 (previous published)
PRIOR_V202_DOI = "10.5281/zenodo.20433053"  # v2.0.2 (earlier published)
PRIOR_V201_DOI = "10.5281/zenodo.20419874"  # v2.0.1 (earlier published)
PRIOR_V200_DOI = "10.5281/zenodo.20418539"  # v2.0.0 (earlier published)
PRIOR_V120_DOI = "10.5281/zenodo.19474599"  # v1.2.0 (earlier published)
LICENSE = "CC-BY-4.0"


def build_config() -> PressConfig:
    """The v3.0.1 release identity, interpolated into every rendered PDF."""
    return PressConfig(
        release_label=RELEASE_LABEL,
        author=AUTHOR,
        orcid=ORCID,
        repo_url=REPO_URL,
        license=LICENSE,
        version_doi=VERSION_DOI,
        concept_doi=CONCEPT_DOI,
        previous_version=("v3.0.0", PREVIOUS_VERSION_DOI),
        prior_versions=(
            ("v2.0.2", PRIOR_V202_DOI),
            ("v2.0.1", PRIOR_V201_DOI),
            ("v2.0.0", PRIOR_V200_DOI),
            ("v1.2.0", PRIOR_V120_DOI),
        ),
    )


# The six canonical document specs ship with the press package so the
# migration cannot silently drop per-document rules the legacy generator
# hard-coded (e.g. the SYSTEM contact sheet's 90% width). The package pins
# its subject strings to the release it was extracted at (v3.0.0); re-stamp
# them with the current release label.
DOCS = [
    {**doc, "pdf_subject": doc["pdf_subject"].replace("v3.0.0", RELEASE_LABEL)}
    for doc in OWL_SEMAPHORE_DOCS
]


def main() -> None:
    if not VERSION_DOI:
        print(
            "ERROR: VERSION_DOI is unset. Reserve the v3.0.1 version DOI on a "
            "Zenodo new-version draft of the concept record (owl-press zenodo "
            "new-version <deposition-id>) and set VERSION_DOI above before "
            "generating release PDFs. See RELEASE-PROCESS.md §1.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Owl Semaphore PDF Generator ({RELEASE_LABEL})")
    print(f"Renderer: owl-semaphore-press {PRESS_VERSION}")
    print("=" * 60)

    cfg = build_config()
    success = 0
    for doc in DOCS:
        print(f"\n[{doc['state_token']}] {doc['title']}")
        print(f"  Rendering {doc['md']} -> {doc['pdf']}...")
        try:
            pdf_path = render_pdf(doc, repo_root=REPO, cfg=cfg)
        except RenderError as exc:
            print(f"  ERROR: {exc}", file=sys.stderr)
            continue
        size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
        print(f"  OK  {doc['pdf']} ({size_mb:.1f} MB)")
        success += 1

    print(f"\n{'=' * 60}")
    print(f"Generated {success}/{len(DOCS)} PDFs")

    if success < len(DOCS):
        sys.exit(1)


if __name__ == "__main__":
    main()
