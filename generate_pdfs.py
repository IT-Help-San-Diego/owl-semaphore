#!/usr/bin/env python3
"""
Generate publication-grade PDFs for the Owl Semaphore system.

Converts each OWL specification .md file into a styled PDF with:
  - Badge image header
  - Contact sheet / layer proof palette
  - Proper math rendering
  - Classification ledger (back page)
  - Styled headers, footers, and horizontal rules

Requires: pandoc, typst (both available via Homebrew)
Usage:   python3 generate_pdfs.py
"""

import os
import re
import subprocess
import sys
import base64

REPO = os.path.dirname(os.path.abspath(__file__))

# ── Document metadata ──────────────────────────────────────────────────────

DOCS = [
    {
        "md": "OWL-SEMAPHORE-SYSTEM.md",
        "pdf": "OWL-SEMAPHORE-SYSTEM.pdf",
        "badge": "assets/releases/540/NORM-composite-transparent-540.png",
        "contact_sheet": "assets/proofs/OWL-SEMAPHORE-MASTER-PROOF.png",
        "color": "#d4a853",
        "color_rgb": "rgb(212, 168, 83)",
        "label": "N O R M A T I V E",
        "title": "Owl Semaphore",
        "subtitle_typst": "System Specification — A Finite Algebra of Epistemic States",
        "mathline": "T = I    det = +1    (x, y) → (x, y)",
        "quote": '"This is the standard."',
        "standard_ref": "RFC 2119 MUST / SHALL",
        "contact_caption": "Owl Semaphore System — Master Proof",
    },
    {
        "md": "OWL-1-NORMATIVE.md",
        "pdf": "OWL-1-NORMATIVE.pdf",
        "badge": "assets/releases/540/NORM-composite-transparent-540.png",
        "contact_sheet": "assets/proofs/NORM-layer-proof-palette.png",
        "color": "#d4a853",
        "color_rgb": "rgb(212, 168, 83)",
        "label": "N O R M A T I V E",
        "title": "Owl Semaphore — Normative",
        "subtitle_typst": "OWL 1 / Identity State / Standard Specification",
        "mathline": "T = I    det = +1    (x, y) → (x, y)",
        "quote": '"This is the standard."',
        "standard_ref": "RFC 2119 MUST / SHALL",
        "contact_caption": "Normative — Layer Proof Palette",
    },
    {
        "md": "OWL-2-NON-NORMATIVE.md",
        "pdf": "OWL-2-NON-NORMATIVE.pdf",
        "badge": "assets/releases/540/NONNORM-composite-transparent-540.png",
        "contact_sheet": "assets/proofs/NONNORM-layer-proof-palette.png",
        "color": "#316964",
        "color_rgb": "rgb(49, 105, 100)",
        "label": "N O N - N O R M A T I V E",
        "title": "Owl Semaphore — Non-Normative",
        "subtitle_typst": "OWL 2 / Reflection State (σ#sub[v]) / Standard Specification",
        "mathline": "T = σᵥ    det = −1    (x, y) → (−x, y)",
        "quote": '"This reflects the standard."',
        "standard_ref": "Informative / Advisory (NOTE)",
        "contact_caption": "Non-Normative — Layer Proof Palette",
    },
    {
        "md": "OWL-3-CRITICAL.md",
        "pdf": "OWL-3-CRITICAL.pdf",
        "badge": "assets/releases/540/CRIT-composite-transparent-540.png",
        "contact_sheet": "assets/proofs/CRIT-layer-proof-palette.png",
        "color": "#990f1e",
        "color_rgb": "rgb(153, 15, 30)",
        "label": "C R I T I C A L",
        "title": "Owl Semaphore — Critical",
        "subtitle_typst": "OWL 3 / Inversion State (C#sub[2]) / Standard Specification",
        "mathline": "T = C₂    det = +1    (x, y) → (−x, −y)",
        "quote": '"This inverts the standard."',
        "standard_ref": "RFC 2119 MUST NOT / SHALL NOT",
        "contact_caption": "Critical — Layer Proof Palette",
    },
    {
        "md": "OWL-4-METACOGNITIVE.md",
        "pdf": "OWL-4-METACOGNITIVE.pdf",
        "badge": "assets/releases/540/META-composite-transparent-540.png",
        "contact_sheet": "assets/proofs/META-layer-proof-palette.png",
        "color": "#8C4191",
        "color_rgb": "rgb(140, 65, 145)",
        "label": "M E T A C O G N I T I V E",
        "title": "Owl Semaphore — Metacognitive",
        "subtitle_typst": "OWL 4 / Frame-Inversion State (σ#sub[h]) / Standard Specification",
        "mathline": "T = σₕ    det = −1    (x, y) → (x, −y)",
        "quote": '"This audits the standard."',
        "standard_ref": "Epistemic / Framework (META)",
        "contact_caption": "Metacognitive — Layer Proof Palette",
    },
]


def preprocess_md(md_path):
    """Read markdown, strip front image, convert \\(...\\) to $...$."""
    with open(md_path, "r") as f:
        lines = f.readlines()

    # Strip leading image line
    if lines and lines[0].startswith("!["):
        lines = lines[1:]

    text = "".join(lines).strip()

    # Convert \(...\) inline math to $...$
    text = re.sub(r"\\\((.+?)\\\)", r"$\1$", text)

    # Strip the top-level heading and subtitle (we handle those in template)
    # Remove lines starting with # (h1) and ## that are title/version lines
    new_lines = []
    skip_count = 0
    for line in text.split("\n"):
        if skip_count < 3 and (
            line.startswith("# OWL SEMAPHORE")
            or line.startswith("## OWL ")
            or line.startswith("### Version")
            or line.startswith("## Version")
        ):
            skip_count += 1
            continue
        new_lines.append(line)

    text = "\n".join(new_lines).strip()
    # Remove leading --- if present (separator after removed title)
    text = re.sub(r"^---\s*\n", "", text)

    return text


def md_to_typst(md_text):
    """Convert markdown to Typst markup via pandoc."""
    result = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "typst", "--wrap=none"],
        input=md_text,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"pandoc error: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    return result.stdout


def build_typst_document(doc, body_typst):
    """Build complete Typst source with header, styling, contact sheet, and ledger."""

    badge_path = doc["badge"]
    contact_path = doc["contact_sheet"]
    color = doc["color_rgb"]
    is_system = doc["md"] == "OWL-SEMAPHORE-SYSTEM.md"

    # Badge paths for classification ledger (relative to repo root)
    norm_badge = "assets/releases/540/NORM-composite-transparent-540.png"
    nonnorm_badge = "assets/releases/540/NONNORM-composite-transparent-540.png"
    crit_badge = "assets/releases/540/CRIT-composite-transparent-540.png"
    meta_badge = "assets/releases/540/META-composite-transparent-540.png"

    return f'''// Owl Semaphore PDF — generated by generate_pdfs.py
#set page(
  paper: "us-letter",
  margin: (top: 72pt, bottom: 72pt, left: 72pt, right: 72pt),
  footer: context {{
    set text(8pt, fill: luma(140))
    grid(
      columns: (1fr, 1fr, 1fr),
      align: (left, center, right),
      [Owl Semaphore · v1.0],
      [#counter(page).display("1 of 1", both: true)],
      [github.com/IT-Help-San-Diego/owl-semaphore],
    )
  }},
)

#set text(font: "New Computer Modern", size: 11pt)
#set par(justify: true, leading: 0.65em)

// Pandoc compatibility
#let horizontalrule = line(length: 100%, stroke: 0.5pt + luma(200))

// Heading styles
#show heading.where(level: 1): it => {{
  v(18pt)
  line(length: 100%, stroke: 1.5pt + {color})
  v(6pt)
  set text(size: 16pt, weight: "bold", fill: {color})
  it.body
  v(3pt)
  line(length: 100%, stroke: 0.75pt + {color})
  v(10pt)
}}

#show heading.where(level: 2): it => {{
  v(10pt)
  set text(size: 13pt, weight: "bold")
  it.body
  v(6pt)
}}

#show heading.where(level: 3): it => {{
  v(8pt)
  set text(size: 11pt, weight: "bold")
  it.body
  v(4pt)
}}

// Code blocks
#show raw.where(block: true): it => {{
  set text(size: 9pt)
  block(
    fill: luma(245),
    inset: 10pt,
    radius: 3pt,
    width: 100%,
    it,
  )
}}

// Tables
#set table(
  stroke: 0.5pt + luma(180),
  inset: 6pt,
)

// ════════════════════════════════════════════════════════════════════════════
// TITLE PAGE
// ════════════════════════════════════════════════════════════════════════════

#align(center)[
  #v(24pt)
  #image("{badge_path}", width: 140pt)
  #v(8pt)

  #text(size: 10pt, weight: "bold", fill: {color}, tracking: 3pt)[{doc["label"]}]

  #v(4pt)
  #text(size: 9pt, fill: luma(80))[#raw("{doc["mathline"]}")]

  #v(2pt)
  #text(size: 9.5pt, style: "italic", fill: luma(80))[{doc["quote"]}]

  #text(size: 8.5pt, fill: luma(120))[{doc["standard_ref"]}]

  #v(16pt)
  #text(size: 28pt, weight: "bold")[{doc["title"]}]
  #v(4pt)
  #text(size: 12pt, fill: luma(80))[{doc["subtitle_typst"]}]
  #v(10pt)

  #text(size: 11pt, weight: "bold")[Carey James Balboa] \\
  #text(size: 10pt, fill: luma(80))[Independent DNS Security Researcher]

  #v(6pt)
  #text(size: 8.5pt, fill: luma(120))[
    ORCID 0009-0000-5237-9065 #h(12pt) DOI 10.5281/zenodo.19473698 \\
    SOURCE github.com/IT-Help-San-Diego/owl-semaphore #h(12pt) VERSION 1.0 · LICENSE CC-BY-4.0
  ]
  #v(12pt)
]

#line(length: 100%, stroke: 1.5pt + {color})

// ════════════════════════════════════════════════════════════════════════════
// CONTACT SHEET
// ════════════════════════════════════════════════════════════════════════════

#v(16pt)
#align(center)[
  #text(size: 9pt, weight: "bold", fill: luma(100), tracking: 1.5pt)[
    {doc["contact_caption"].upper()}
  ]
  #v(8pt)
  #image("{contact_path}", width: {"85%" if not is_system else "90%"})
]
#v(12pt)

// ════════════════════════════════════════════════════════════════════════════
// BODY CONTENT
// ════════════════════════════════════════════════════════════════════════════

{body_typst}

// ════════════════════════════════════════════════════════════════════════════
// CLASSIFICATION LEDGER (BACK PAGE)
// ════════════════════════════════════════════════════════════════════════════

#pagebreak()

#v(1fr)

#line(length: 100%, stroke: 1.5pt + {color})
#v(12pt)

#align(center)[
  #text(size: 10pt, weight: "bold", fill: luma(80), tracking: 2pt)[
    OWL SEMAPHORE SYSTEM — CLASSIFICATION LEDGER
  ]
  #v(16pt)

  #grid(
    columns: (1fr, 1fr, 1fr, 1fr),
    gutter: 12pt,
    // Row 1: badges
    align(center, image("{norm_badge}", width: 80pt)),
    align(center, image("{nonnorm_badge}", width: 80pt)),
    align(center, image("{crit_badge}", width: 80pt)),
    align(center, image("{meta_badge}", width: 80pt)),
    // Row 2: labels
    align(center, text(size: 8pt, weight: "bold", tracking: 1.5pt)[NORMATIVE]),
    align(center, text(size: 8pt, weight: "bold", tracking: 1.5pt)[NON-NORMATIVE]),
    align(center, text(size: 8pt, weight: "bold", tracking: 1.5pt)[CRITICAL]),
    align(center, text(size: 8pt, weight: "bold", tracking: 1.5pt)[METACOGNITIVE]),
    // Row 3: operator + det
    align(center, text(size: 7.5pt, fill: luma(100))[T = I #h(4pt) det = +1]),
    align(center, text(size: 7.5pt, fill: luma(100))[T = σ#sub[v] #h(4pt) det = −1]),
    align(center, text(size: 7.5pt, fill: luma(100))[T = C#sub[2] #h(4pt) det = +1]),
    align(center, text(size: 7.5pt, fill: luma(100))[T = σ#sub[h] #h(4pt) det = −1]),
    // Row 4: mapping
    align(center, text(size: 7.5pt, fill: luma(100))[(x, y) → (x, y)]),
    align(center, text(size: 7.5pt, fill: luma(100))[(x, y) → (−x, y)]),
    align(center, text(size: 7.5pt, fill: luma(100))[(x, y) → (−x, −y)]),
    align(center, text(size: 7.5pt, fill: luma(100))[(x, y) → (x, −y)]),
    // Row 5: quotes
    align(center, text(size: 7.5pt, style: "italic", fill: luma(100))["This is the standard."]),
    align(center, text(size: 7.5pt, style: "italic", fill: luma(100))["This reflects the standard."]),
    align(center, text(size: 7.5pt, style: "italic", fill: luma(100))["This inverts the standard."]),
    align(center, text(size: 7.5pt, style: "italic", fill: luma(100))["This audits the standard."]),
    // Row 6: standard ref
    align(center, text(size: 7pt, fill: luma(140))[RFC 2119 MUST / SHALL]),
    align(center, text(size: 7pt, fill: luma(140))[Informative / Advisory (NOTE)]),
    align(center, text(size: 7pt, fill: luma(140))[RFC 2119 MUST NOT / SHALL NOT]),
    align(center, text(size: 7pt, fill: luma(140))[Epistemic / Framework (META)]),
  )

  #v(20pt)
  #line(length: 60%, stroke: 0.5pt + luma(200))
  #v(8pt)
  #text(size: 8pt, fill: luma(140))[
    Owl Semaphore v1.0 · github.com/IT-Help-San-Diego/owl-semaphore · DOI: 10.5281/zenodo.19473698 \\
    © 2024–2026 IT Help San Diego Inc. · Licensed under CC-BY-4.0
  ]
]

#v(1fr)
'''


def generate_pdf(doc):
    """Generate a single PDF from its doc spec."""
    md_path = os.path.join(REPO, doc["md"])
    pdf_path = os.path.join(REPO, doc["pdf"])

    print(f"  Reading {doc['md']}...")
    md_text = preprocess_md(md_path)

    print(f"  Converting to Typst...")
    body_typst = md_to_typst(md_text)

    print(f"  Building document...")
    typst_source = build_typst_document(doc, body_typst)

    typ_path = os.path.join(REPO, doc["pdf"].replace(".pdf", ".typ"))
    with open(typ_path, "w") as f:
        f.write(typst_source)

    print(f"  Compiling {doc['pdf']}...")
    result = subprocess.run(
        ["typst", "compile", typ_path, pdf_path],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"  ERROR compiling {doc['pdf']}:\n{result.stderr}", file=sys.stderr)
        return False

    # Clean up .typ intermediate
    os.remove(typ_path)

    size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
    print(f"  ✓ {doc['pdf']} ({size_mb:.1f} MB)")
    return True


def main():
    print("Owl Semaphore PDF Generator")
    print("=" * 50)

    success = 0
    for doc in DOCS:
        print(f"\n[{doc['label'].replace(' ', '')}] {doc['title']}")
        if generate_pdf(doc):
            success += 1

    print(f"\n{'=' * 50}")
    print(f"Generated {success}/{len(DOCS)} PDFs")

    if success < len(DOCS):
        sys.exit(1)


if __name__ == "__main__":
    main()
