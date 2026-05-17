#!/usr/bin/env python3
"""Compute SHA-3-512 hashes for tracked release artifacts (v2.0.0-rc).

Writes RELEASE-HASHES.txt at the repository root, formatted compatibly with
``openssl dgst -sha3-512`` output, covering:

  - all PNGs under assets/releases/540/ (v1.3 lineage; retained)
  - all PNGs under assets/v2/transparent-1080/ and assets/v2/transparent-540/
  - all TIFFs under assets/v2/masters/
  - all PNGs under assets/v2/proofs/
  - all five generated specification PDFs (when present)
  - the markdown specifications and README and CHANGELOG and EXPLANATION,
    plus the v2 doctrine and provenance files

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

    for sub in (
        os.path.join("assets", "v2", "transparent-1080"),
        os.path.join("assets", "v2", "transparent-540"),
        os.path.join("assets", "v2", "final-1080"),
        os.path.join("assets", "v2", "final-540"),
        os.path.join("assets", "v2", "masters"),
        os.path.join("assets", "v2", "proofs"),
        os.path.join("assets", "v2", "normative-D-B-gold-master"),
        os.path.join("assets", "v2", "normative-D-B-gold-master", "layers"),
        os.path.join("assets", "v2", "normative-D-B-gold-master", "proofs"),
        os.path.join("assets", "v2", "nonnormative-math97-five-over-master"),
        os.path.join("assets", "v2", "nonnormative-math97-five-over-master", "layers"),
        os.path.join("assets", "v2", "nonnormative-math97-five-over-master", "proofs"),
        os.path.join("assets", "v2", "nonnormative-math97-five-over-master", "metrics"),
    ):
        d = os.path.join(REPO, sub)
        if os.path.isdir(d):
            for name in sorted(os.listdir(d)):
                if name.lower().endswith((".png", ".tiff", ".tif", ".json")):
                    targets.append(os.path.join(sub, name))

    metrics = os.path.join("assets", "v2", "metrics")
    md = os.path.join(REPO, metrics)
    if os.path.isdir(md):
        for name in sorted(os.listdir(md)):
            if name.endswith(".json"):
                targets.append(os.path.join(metrics, name))

    norm_master_root = os.path.join("assets", "v2", "normative-D-B-gold-master")
    for name in ("SOURCE-README.md", "AUDIT-NOTE.md"):
        rel = os.path.join(norm_master_root, name)
        if os.path.isfile(os.path.join(REPO, rel)):
            targets.append(rel)

    nn_master_root = os.path.join("assets", "v2", "nonnormative-math97-five-over-master")
    for name in ("SOURCE-README.md", "SOURCE-AUDIT-NOTE.md", "AUDIT-NOTE.md"):
        rel = os.path.join(nn_master_root, name)
        if os.path.isfile(os.path.join(REPO, rel)):
            targets.append(rel)

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
        "ASSET-DOCTRINE.md",
        "PROVENANCE.md",
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
