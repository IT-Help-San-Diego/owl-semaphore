"""
Pytest wrapper for the Owl Semaphore v1.3.0-rc release-candidate verification.

Two test groups:

1. test_banner_tuple_<state> — parameterised over every generated PDF.
   Loads scripts/verify_banner_tuple.py, extracts the BANNER TUPLE block from
   the rendered PDF, and asserts state/transform/det/mapping/version/DOI/license
   match expectations.

2. test_canonical_wording — asserts the canonical Formal sentence appears
   verbatim in README.md, OWL-SEMAPHORE-SYSTEM.md, CHANGELOG.md, and
   OWL-SEMAPHORE-EXPLANATION.md, and that no stale variant survives in
   committed markdown.

If the PDFs have not been generated yet (`make pdfs` hasn't run), the
banner-tuple tests are skipped with a clear message rather than failing —
this lets `pytest tests/` work in CI even before the build step.
"""

from __future__ import annotations

import importlib.util
import os
import sys

import pytest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load(name: str, relpath: str):
    spec = importlib.util.spec_from_file_location(name, os.path.join(REPO, relpath))
    assert spec and spec.loader, f"could not load {relpath}"
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


banner = _load("verify_banner_tuple_mod", "scripts/verify_banner_tuple.py")
metacheck = _load("check_pdf_metadata_mod", "scripts/check_pdf_metadata.py")

CANONICAL_SENTENCE = (
    "A finite algebra over epistemic states, implemented as a reproducible "
    "visual notation system with enforced invariants."
)

CANONICAL_WORDING_FILES = [
    "README.md",
    "OWL-SEMAPHORE-SYSTEM.md",
    "CHANGELOG.md",
    "OWL-SEMAPHORE-EXPLANATION.md",
]

# Drift sentinels: phrases that should no longer appear in v1.3.0-rc body text.
DRIFT_PHRASES_IN_BODY = [
    "mapped into a visual system with strict invariants",
]


@pytest.mark.parametrize("entry", banner.EXPECTED, ids=lambda e: e["pdf"])
def test_banner_tuple(entry):
    pdf_path = os.path.join(REPO, entry["pdf"])
    if not os.path.exists(pdf_path):
        pytest.skip(f"{entry['pdf']} not generated yet — run `make pdfs` first")
    ok, failures = banner.verify(entry)
    assert ok, "\n".join(failures)


@pytest.mark.parametrize("entry", metacheck.CHECKS, ids=lambda e: e["pdf"])
def test_pdf_metadata(entry):
    pdf_path = os.path.join(REPO, entry["pdf"])
    if not os.path.exists(pdf_path):
        pytest.skip(f"{entry['pdf']} not generated yet — run `make pdfs` first")
    failures = metacheck.check_pdf(entry)
    assert not failures, "\n".join(failures)


@pytest.mark.parametrize("relpath", CANONICAL_WORDING_FILES)
def test_canonical_sentence_present(relpath):
    with open(os.path.join(REPO, relpath), "r", encoding="utf-8") as f:
        content = f.read()
    assert CANONICAL_SENTENCE in content, (
        f"{relpath} does not contain the canonical Formal sentence verbatim."
    )


def test_no_stale_canonical_phrase_in_body():
    """Drift sentinel: the v1.2.0 Core Principle phrasing must not survive
    as a current canonical statement. It is allowed to appear in CHANGELOG.md
    as part of the historical record only."""
    offenders = []
    for fname in os.listdir(REPO):
        if not fname.endswith(".md"):
            continue
        if fname == "CHANGELOG.md":
            continue  # historical record may quote prior wording
        with open(os.path.join(REPO, fname), "r", encoding="utf-8") as f:
            content = f.read()
        for phrase in DRIFT_PHRASES_IN_BODY:
            if phrase in content:
                offenders.append((fname, phrase))
    assert not offenders, (
        "Stale canonical-sentence variants still present: " + repr(offenders)
    )


def test_version_drift_purged():
    """No state spec or system spec should still claim 'Version 1.0 Draft'."""
    specs = [
        "OWL-SEMAPHORE-SYSTEM.md",
        "OWL-1-NORMATIVE.md",
        "OWL-2-NON-NORMATIVE.md",
        "OWL-3-CRITICAL.md",
        "OWL-4-METACOGNITIVE.md",
    ]
    bad = []
    for s in specs:
        with open(os.path.join(REPO, s), "r", encoding="utf-8") as f:
            content = f.read()
        if "Version 1.0 Draft" in content:
            bad.append(s)
        if "## Version 1.0\n" in content:
            bad.append(s + " (## Version 1.0)")
    assert not bad, f"Stale Version-1.0 stamps survived in: {bad}"
