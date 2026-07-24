#!/usr/bin/env python3
"""Compute SHA-3-512 hashes for tracked release artifacts (v3.0.0).

Writes RELEASE-HASHES.txt at the repository root, formatted compatibly with
``openssl dgst -sha3-512`` output, covering:

  - all PNGs under assets/releases/540/
  - all six generated specification PDFs (when present)
  - the markdown specifications and README and CHANGELOG and EXPLANATION

The output is deterministic (sorted by path) so the hashes file diffs cleanly.
"""

from __future__ import annotations

import hashlib
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def sha3_512(path: str) -> str:
    h = hashlib.sha3_512()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def collect_targets() -> list[str]:
    targets: list[str] = []

    releases_dir = os.path.join(REPO, "assets", "releases", "540")
    if os.path.isdir(releases_dir):
        for name in sorted(os.listdir(releases_dir)):
            if name.endswith(".png"):
                targets.append(os.path.join("assets", "releases", "540", name))

    for name in (
        "OWL-SEMAPHORE-SYSTEM.pdf",
        "OWL-SEMAPHORE-EXPLANATION.pdf",
        "OWL-1-NORMATIVE.pdf",
        "OWL-2-NON-NORMATIVE.pdf",
        "OWL-3-CRITICAL.pdf",
        "OWL-4-METACOGNITIVE.pdf",
    ):
        if os.path.isfile(os.path.join(REPO, name)):
            targets.append(name)

    for name in (
        "README.md",
        "CHANGELOG.md",
        "OWL-SEMAPHORE-SYSTEM.md",
        "OWL-SEMAPHORE-EXPLANATION.md",
        "OWL-1-NORMATIVE.md",
        "OWL-2-NON-NORMATIVE.md",
        "OWL-3-CRITICAL.md",
        "OWL-4-METACOGNITIVE.md",
        "INTEGRITY-MANIFEST.md",
        "CITATION.cff",
        ".zenodo.json",
    ):
        if os.path.isfile(os.path.join(REPO, name)):
            targets.append(name)

    return targets


def main() -> int:
    targets = collect_targets()
    lines = []
    for rel in targets:
        full = os.path.join(REPO, rel)
        digest = sha3_512(full)
        lines.append(f"SHA3-512({rel})= {digest}")

    out_path = os.path.join(REPO, "RELEASE-HASHES.txt")
    with open(out_path, "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Wrote {out_path} ({len(lines)} entries)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
