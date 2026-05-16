#!/usr/bin/env python3
"""
PDF metadata check for Owl Semaphore generated PDFs (v1.3.0-rc).

Each generated PDF MUST carry document-info metadata:
  - title       (matches the document title)
  - author      (Carey James Balboa)
  - keywords    (contains "Owl Semaphore" + the state label)
  - subject     (or "/Description"; contains the version label)

This script extracts PDF metadata using pypdf and asserts the expected values.
Intended to be run from `make verify`.
"""

from __future__ import annotations

import os
import sys
from typing import Any, Dict, List

import pypdf

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXPECTED_AUTHOR = "Carey James Balboa"
EXPECTED_VERSION = "1.3.0-rc"

CHECKS: List[Dict[str, Any]] = [
    {
        "pdf": "OWL-SEMAPHORE-SYSTEM.pdf",
        "title_contains": "Owl Semaphore",
        "keywords_contains": ["Owl Semaphore"],
    },
    {
        "pdf": "OWL-1-NORMATIVE.pdf",
        "title_contains": "Normative",
        "keywords_contains": ["Owl Semaphore", "NORMATIVE"],
    },
    {
        "pdf": "OWL-2-NON-NORMATIVE.pdf",
        "title_contains": "Non-Normative",
        "keywords_contains": ["Owl Semaphore", "NON-NORMATIVE"],
    },
    {
        "pdf": "OWL-3-CRITICAL.pdf",
        "title_contains": "Critical",
        "keywords_contains": ["Owl Semaphore", "CRITICAL"],
    },
    {
        "pdf": "OWL-4-METACOGNITIVE.pdf",
        "title_contains": "Metacognitive",
        "keywords_contains": ["Owl Semaphore", "METACOGNITIVE"],
    },
    {
        "pdf": "OWL-SEMAPHORE-EXPLANATION.pdf",
        "title_contains": "Explanation",
        "keywords_contains": ["Owl Semaphore", "EXPLANATION"],
    },
]


def check_pdf(entry: Dict[str, Any]) -> List[str]:
    pdf_path = os.path.join(REPO, entry["pdf"])
    failures: List[str] = []

    if not os.path.exists(pdf_path):
        return [f"missing PDF: {entry['pdf']}"]

    reader = pypdf.PdfReader(pdf_path)
    meta = reader.metadata or {}

    def m(key: str) -> str:
        v = meta.get(key, "") or meta.get(f"/{key}", "")
        return str(v) if v is not None else ""

    title = m("/Title") or m("/title")
    author = m("/Author") or m("/author")
    keywords = m("/Keywords") or m("/keywords")
    subject = m("/Subject") or m("/subject") or m("/Description")

    if entry["title_contains"] not in title:
        failures.append(
            f"{entry['pdf']}: title must contain {entry['title_contains']!r}, got {title!r}"
        )
    if author and EXPECTED_AUTHOR not in author:
        failures.append(
            f"{entry['pdf']}: author should be {EXPECTED_AUTHOR!r}, got {author!r}"
        )
    if not author:
        failures.append(f"{entry['pdf']}: author metadata missing")
    for kw in entry["keywords_contains"]:
        if kw not in keywords:
            failures.append(
                f"{entry['pdf']}: keywords missing {kw!r}; got {keywords!r}"
            )
    if EXPECTED_VERSION not in subject and EXPECTED_VERSION not in keywords:
        failures.append(
            f"{entry['pdf']}: neither subject nor keywords mention version "
            f"{EXPECTED_VERSION!r}; subject={subject!r} keywords={keywords!r}"
        )

    return failures


def main() -> int:
    print("Owl Semaphore — PDF document-info metadata check")
    print("=" * 60)

    all_ok = True
    for entry in CHECKS:
        failures = check_pdf(entry)
        status = "OK  " if not failures else "FAIL"
        print(f"  [{status}] {entry['pdf']}")
        for f in failures:
            print(f"         {f}")
        if failures:
            all_ok = False

    print("=" * 60)
    if all_ok:
        print(f"All {len(CHECKS)} PDFs carry the expected document-info metadata.")
        return 0
    print("PDF metadata check FAILED.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
