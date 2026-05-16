#!/usr/bin/env python3
"""
Compute SHA-3-512 hashes for all release-relevant files of the Owl Semaphore
v1.3.0-rc release candidate, and emit:
  - RELEASE-HASHES.txt    (flat list, openssl-dgst-style lines)
  - hashes also accessible via the manifest-augment routine (printed to stdout
    as YAML-style records suitable for pasting into INTEGRITY-MANIFEST.md).

Per `INTEGRITY-MANIFEST.md` the canonical algorithm is SHA-3-512.
"""

from __future__ import annotations

import hashlib
import os
import sys
from typing import List, Tuple

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Order matters here only for readability of the generated files.
RELEASE_FILES: List[str] = [
    # Specification documents
    "OWL-SEMAPHORE-SYSTEM.md",
    "OWL-1-NORMATIVE.md",
    "OWL-2-NON-NORMATIVE.md",
    "OWL-3-CRITICAL.md",
    "OWL-4-METACOGNITIVE.md",
    "OWL-SEMAPHORE-EXPLANATION.md",
    "README.md",
    "CHANGELOG.md",
    "CITATION.cff",
    ".zenodo.json",
    "INTEGRITY-MANIFEST.md",
    # Generated PDFs
    "OWL-SEMAPHORE-SYSTEM.pdf",
    "OWL-1-NORMATIVE.pdf",
    "OWL-2-NON-NORMATIVE.pdf",
    "OWL-3-CRITICAL.pdf",
    "OWL-4-METACOGNITIVE.pdf",
    "OWL-SEMAPHORE-EXPLANATION.pdf",
    # 540 px composite PNG release set
    "assets/releases/540/NORM-composite-dark-540.png",
    "assets/releases/540/NORM-composite-transparent-540.png",
    "assets/releases/540/NORM-composite-white-540.png",
    "assets/releases/540/NONNORM-composite-dark-540.png",
    "assets/releases/540/NONNORM-composite-transparent-540.png",
    "assets/releases/540/NONNORM-composite-white-540.png",
    "assets/releases/540/CRIT-composite-dark-540.png",
    "assets/releases/540/CRIT-composite-transparent-540.png",
    "assets/releases/540/CRIT-composite-white-540.png",
    "assets/releases/540/META-composite-dark-540.png",
    "assets/releases/540/META-composite-transparent-540.png",
    "assets/releases/540/META-composite-white-540.png",
]


def sha3_512(path: str) -> str:
    h = hashlib.sha3_512()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def collect() -> List[Tuple[str, str]]:
    results: List[Tuple[str, str]] = []
    for rel in RELEASE_FILES:
        abs_path = os.path.join(REPO, rel)
        if not os.path.exists(abs_path):
            results.append((rel, "MISSING"))
            continue
        try:
            results.append((rel, sha3_512(abs_path)))
        except OSError as exc:
            results.append((rel, f"ERROR:{exc}"))
    return results


def write_release_hashes(results: List[Tuple[str, str]]) -> str:
    out_path = os.path.join(REPO, "RELEASE-HASHES.txt")
    header = (
        "# Owl Semaphore — RELEASE-HASHES.txt\n"
        "# Algorithm: SHA-3-512\n"
        "# Version: v1.3.0-rc (release candidate; not yet published to Zenodo)\n"
        "# Regenerate with: make hashes\n"
        "#\n"
    )
    body_lines = []
    for rel, digest in results:
        if digest == "MISSING" or digest.startswith("ERROR:"):
            body_lines.append(f"# {digest}: {rel}")
        else:
            body_lines.append(f"SHA3-512({rel})= {digest}")
    with open(out_path, "w") as f:
        f.write(header + "\n".join(body_lines) + "\n")
    return out_path


def main() -> int:
    results = collect()
    out_path = write_release_hashes(results)
    print(f"Wrote {out_path}")
    print("=" * 60)
    n_missing = sum(1 for _, d in results if d == "MISSING")
    n_error = sum(1 for _, d in results if d.startswith("ERROR:"))
    n_ok = sum(1 for _, d in results if d not in ("MISSING",) and not d.startswith("ERROR:"))
    print(f"Hashed: {n_ok}    Missing: {n_missing}    Errors: {n_error}")
    if n_missing > 0:
        for rel, d in results:
            if d == "MISSING":
                print(f"  MISSING: {rel}")
    if n_error > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
