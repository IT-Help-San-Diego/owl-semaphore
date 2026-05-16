#!/usr/bin/env python3
"""
Banner-tuple integrity check for Owl Semaphore generated PDFs (v1.3.0-rc).

Modelled on DNS Tool's banner-tuple approach: extract page-one text from
every generated PDF and verify that the embedded
   (state, transform, determinant, mapping, version, concept_doi, version_doi,
    last_published_doi, license)
tuple matches the value expected for that PDF.

The tuple is emitted by generate_pdfs.py inside a fixed-format block:

    BANNER TUPLE BEGIN
    state=...
    transform=...
    determinant=...
    mapping=...
    version=...
    concept_doi=...
    version_doi=...
    last_published_doi=...
    license=...
    BANNER TUPLE END

If any PDF is missing, malformed, or carries the wrong tuple, this script
exits non-zero and prints a per-PDF diff. Intended to be run from `make verify`.
"""

from __future__ import annotations

import os
import sys
from typing import Any, Dict, List, Tuple

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Canonical expectations per PDF.
# These deliberately duplicate the values in generate_pdfs.py so the test is
# independent of the renderer's internal constants.
EXPECTED: List[Dict[str, Any]] = [
    {
        "pdf": "OWL-SEMAPHORE-SYSTEM.pdf",
        "state": "NORMATIVE",
        "transform": "I",
        "determinant": "+1",
        "mapping": "(x, y) -> (x, y)",
    },
    {
        "pdf": "OWL-1-NORMATIVE.pdf",
        "state": "NORMATIVE",
        "transform": "I",
        "determinant": "+1",
        "mapping": "(x, y) -> (x, y)",
    },
    {
        "pdf": "OWL-2-NON-NORMATIVE.pdf",
        "state": "NON-NORMATIVE",
        "transform": "σv",
        "determinant": "-1",
        "mapping": "(x, y) -> (-x, y)",
    },
    {
        "pdf": "OWL-3-CRITICAL.pdf",
        "state": "CRITICAL",
        "transform": "C2",
        "determinant": "+1",
        "mapping": "(x, y) -> (-x, -y)",
    },
    {
        "pdf": "OWL-4-METACOGNITIVE.pdf",
        "state": "METACOGNITIVE",
        "transform": "σh",
        "determinant": "-1",
        "mapping": "(x, y) -> (x, -y)",
    },
    {
        "pdf": "OWL-SEMAPHORE-EXPLANATION.pdf",
        "state": "EXPLANATION",
        "transform": "I",
        "determinant": "+1",
        "mapping": "(x, y) -> (x, y)",
    },
]

EXPECTED_VERSION = "v1.3.0-rc"
EXPECTED_CONCEPT_DOI = "10.5281/zenodo.19473697"
EXPECTED_VERSION_DOI = "TBD_BY_ZENODO_ON_RELEASE"
EXPECTED_LAST_VERSION_DOI = "10.5281/zenodo.19474599"
EXPECTED_LICENSE = "CC BY 4.0"


def _normalize_mapping(s: str) -> str:
    """Normalise Unicode arrows/minus signs introduced by PDF rendering."""
    return (
        s.replace("→", "->")
        .replace("−", "-")
        .replace("­", "")
        .replace(" ", "")
    )


def extract_front_text(pdf_path: str, max_pages: int = 2) -> str:
    """Return text from the first N pages of a PDF.

    The banner-tuple block is emitted right after the title block on page 1,
    but with long subtitles the title block can push the tuple slightly past
    the page break. Reading the first two pages keeps the parser robust
    against that without losing the "front matter" semantics.
    """
    try:
        import pypdf  # type: ignore
    except ImportError:
        pypdf = None  # type: ignore
    try:
        from pdfminer.high_level import extract_text as pdfminer_extract  # type: ignore
    except ImportError:
        pdfminer_extract = None  # type: ignore
    try:
        import pdfplumber  # type: ignore
    except ImportError:
        pdfplumber = None  # type: ignore

    if pdfplumber is not None:
        with pdfplumber.open(pdf_path) as pdf:
            chunks = []
            for i in range(min(max_pages, len(pdf.pages))):
                t = pdf.pages[i].extract_text() or ""
                if t:
                    chunks.append(t)
            text = "\n".join(chunks)
            if text:
                return text

    if pypdf is not None:
        reader = pypdf.PdfReader(pdf_path)
        chunks = []
        for i in range(min(max_pages, len(reader.pages))):
            chunks.append(reader.pages[i].extract_text() or "")
        return "\n".join(chunks)

    if pdfminer_extract is not None:
        return pdfminer_extract(pdf_path, page_numbers=list(range(max_pages))) or ""

    raise RuntimeError(
        "No PDF text-extraction library available. "
        "Install one of: pypdf, pdfplumber, pdfminer.six."
    )


def parse_banner_tuple(text: str) -> Dict[str, str]:
    """Pull the BANNER TUPLE block out of page-1 text."""
    start_marker = "BANNER TUPLE BEGIN"
    end_marker = "BANNER TUPLE END"
    if start_marker not in text or end_marker not in text:
        return {}
    block = text.split(start_marker, 1)[1].split(end_marker, 1)[0]
    out: Dict[str, str] = {}
    for line in block.splitlines():
        line = line.strip()
        if not line or "=" not in line:
            continue
        k, _, v = line.partition("=")
        out[k.strip()] = v.strip()
    return out


def verify(pdf_meta: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Return (passed, list_of_failure_messages)."""
    pdf_path = os.path.join(REPO, pdf_meta["pdf"])
    failures: List[str] = []

    if not os.path.exists(pdf_path):
        return False, [f"missing PDF: {pdf_meta['pdf']}"]

    text = extract_front_text(pdf_path)
    tuple_data = parse_banner_tuple(text)

    if not tuple_data:
        return False, [f"{pdf_meta['pdf']}: BANNER TUPLE block not found on page 1"]

    def check(key: str, expected: str, normalize=lambda s: s) -> None:
        actual = tuple_data.get(key, "")
        if normalize(actual) != normalize(expected):
            failures.append(
                f"{pdf_meta['pdf']}: {key} mismatch — "
                f"expected {expected!r}, got {actual!r}"
            )

    check("state", pdf_meta["state"])
    check("transform", pdf_meta["transform"])
    check("determinant", pdf_meta["determinant"])
    check("mapping", pdf_meta["mapping"], normalize=_normalize_mapping)
    check("version", EXPECTED_VERSION)
    check("concept_doi", EXPECTED_CONCEPT_DOI)
    check("version_doi", EXPECTED_VERSION_DOI)
    check("last_published_doi", EXPECTED_LAST_VERSION_DOI)
    check("license", EXPECTED_LICENSE)

    return (not failures), failures


def main() -> int:
    print("Owl Semaphore — banner-tuple verification")
    print("=" * 60)

    all_ok = True
    for entry in EXPECTED:
        ok, failures = verify(entry)
        status = "OK  " if ok else "FAIL"
        print(f"  [{status}] {entry['pdf']}")
        for msg in failures:
            print(f"         {msg}")
        if not ok:
            all_ok = False

    print("=" * 60)
    if all_ok:
        print(f"All {len(EXPECTED)} PDFs carry the expected banner tuple.")
        return 0
    print("Banner-tuple verification FAILED.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
