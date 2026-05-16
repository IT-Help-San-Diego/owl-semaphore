#!/usr/bin/env python3
"""
Generate publication-grade PDFs for the Owl Semaphore system (v1.3.0-rc).

Pipeline (Typst, kept for v1.3.0 per the release-candidate plan):
  Markdown source --pandoc--> Typst markup --typst--> PDF

Each PDF includes:
  - Title-page badge, label, math line, canonical quote, RFC reference
  - A machine-parseable banner-tuple block ("BANNER TUPLE … END") so
    scripts/verify_banner_tuple.py can read state/transform/det/mapping/
    version/DOI directly out of the rendered PDF
  - Per-page running header with the state's owl + label + version
  - Contact-sheet / layer-proof palette
  - Full classification ledger on the back page
  - PDF document-info metadata (title, author, subject, keywords)
  - Footer with v1.3.0-rc, repo URL, page numbers, license, concept DOI

Requires: pandoc on PATH, and the `typst` Python package
           (pip install typst) which embeds the Typst compiler.
Usage:   python3 generate_pdfs.py
"""

import os
import re
import subprocess
import sys

import typst

REPO = os.path.dirname(os.path.abspath(__file__))

# ── Project-wide constants ────────────────────────────────────────────────

VERSION = "1.3.0-rc"
VERSION_LABEL = "v1.3.0-rc"
CONCEPT_DOI = "10.5281/zenodo.19473697"
LAST_VERSION_DOI = "10.5281/zenodo.19474599"
VERSION_DOI = "TBD_BY_ZENODO_ON_RELEASE"
LICENSE = "CC BY 4.0"
REPO_URL = "github.com/IT-Help-San-Diego/owl-semaphore"
AUTHOR = "Carey James Balboa"
ORCID = "0009-0000-5237-9065"
CANONICAL_SENTENCE = (
    "A finite algebra over epistemic states, implemented as a reproducible "
    "visual notation system with enforced invariants."
)

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
        "label_compact": "NORMATIVE",
        "title": "Owl Semaphore",
        "subtitle_typst": "System Specification — A Finite Algebra of Epistemic States",
        "transform_text": "I",
        "det_text": "+1",
        "mapping_text": "(x, y) → (x, y)",
        "mathline": "T = I    det = +1    (x, y) → (x, y)",
        "quote": '"This is the standard."',
        "standard_ref": "RFC 2119 MUST / SHALL",
        "contact_caption": "Owl Semaphore System — Master Proof",
        "keywords": "Owl Semaphore, finite algebra, Klein four-group, V4, epistemic notation, visual standard, classification, DNS Tool",
        "subject": "System specification for the Owl Semaphore visual epistemic notation system.",
    },
    {
        "md": "OWL-1-NORMATIVE.md",
        "pdf": "OWL-1-NORMATIVE.pdf",
        "badge": "assets/releases/540/NORM-composite-transparent-540.png",
        "contact_sheet": "assets/proofs/NORM-layer-proof-palette.png",
        "color": "#d4a853",
        "color_rgb": "rgb(212, 168, 83)",
        "label": "N O R M A T I V E",
        "label_compact": "NORMATIVE",
        "title": "Owl Semaphore — Normative",
        "subtitle_typst": "OWL 1 / Identity State / Standard Specification",
        "transform_text": "I",
        "det_text": "+1",
        "mapping_text": "(x, y) → (x, y)",
        "mathline": "T = I    det = +1    (x, y) → (x, y)",
        "quote": '"This is the standard."',
        "standard_ref": "RFC 2119 MUST / SHALL",
        "contact_caption": "Normative — Layer Proof Palette",
        "keywords": "Owl Semaphore, normative, identity state, V4, RFC 2119, classification, DNS Tool",
        "subject": "OWL 1 NORMATIVE — identity state specification of the Owl Semaphore.",
    },
    {
        "md": "OWL-2-NON-NORMATIVE.md",
        "pdf": "OWL-2-NON-NORMATIVE.pdf",
        "badge": "assets/releases/540/NONNORM-composite-transparent-540.png",
        "contact_sheet": "assets/proofs/NONNORM-layer-proof-palette.png",
        "color": "#316964",
        "color_rgb": "rgb(49, 105, 100)",
        "label": "N O N - N O R M A T I V E",
        "label_compact": "NON-NORMATIVE",
        "title": "Owl Semaphore — Non-Normative",
        "subtitle_typst": "OWL 2 / Reflection State (σ#sub[v]) / Standard Specification",
        "transform_text": "σv",
        "det_text": "-1",
        "mapping_text": "(x, y) → (-x, y)",
        "mathline": "T = σᵥ    det = −1    (x, y) → (−x, y)",
        "quote": '"This reflects the standard."',
        "standard_ref": "Informative / Advisory (NOTE)",
        "contact_caption": "Non-Normative — Layer Proof Palette",
        "keywords": "Owl Semaphore, non-normative, reflection state, V4, informative, classification, DNS Tool",
        "subject": "OWL 2 NON-NORMATIVE — reflection state specification of the Owl Semaphore.",
    },
    {
        "md": "OWL-3-CRITICAL.md",
        "pdf": "OWL-3-CRITICAL.pdf",
        "badge": "assets/releases/540/CRIT-composite-transparent-540.png",
        "contact_sheet": "assets/proofs/CRIT-layer-proof-palette.png",
        "color": "#990f1e",
        "color_rgb": "rgb(153, 15, 30)",
        "label": "C R I T I C A L",
        "label_compact": "CRITICAL",
        "title": "Owl Semaphore — Critical",
        "subtitle_typst": "OWL 3 / Inversion State (C#sub[2]) / Standard Specification",
        "transform_text": "C2",
        "det_text": "+1",
        "mapping_text": "(x, y) → (-x, -y)",
        "mathline": "T = C₂    det = +1    (x, y) → (−x, −y)",
        "quote": '"This inverts the standard."',
        "standard_ref": "RFC 2119 MUST NOT / SHALL NOT",
        "contact_caption": "Critical — Layer Proof Palette",
        "keywords": "Owl Semaphore, critical, inversion state, V4, RFC 2119, classification, DNS Tool",
        "subject": "OWL 3 CRITICAL — inversion state specification of the Owl Semaphore.",
    },
    {
        "md": "OWL-4-METACOGNITIVE.md",
        "pdf": "OWL-4-METACOGNITIVE.pdf",
        "badge": "assets/releases/540/META-composite-transparent-540.png",
        "contact_sheet": "assets/proofs/META-layer-proof-palette.png",
        "color": "#8C4191",
        "color_rgb": "rgb(140, 65, 145)",
        "label": "M E T A C O G N I T I V E",
        "label_compact": "METACOGNITIVE",
        "title": "Owl Semaphore — Metacognitive",
        "subtitle_typst": "OWL 4 / Frame-Inversion State (σ#sub[h]) / Standard Specification",
        "transform_text": "σh",
        "det_text": "-1",
        "mapping_text": "(x, y) → (x, -y)",
        "mathline": "T = σₕ    det = −1    (x, y) → (x, −y)",
        "quote": '"This audits the standard."',
        "standard_ref": "Epistemic / Framework (META)",
        "contact_caption": "Metacognitive — Layer Proof Palette",
        "keywords": "Owl Semaphore, metacognitive, frame-inversion, V4, ICD 203, classification, DNS Tool",
        "subject": "OWL 4 METACOGNITIVE — frame-inversion state specification of the Owl Semaphore.",
    },
    {
        "md": "OWL-SEMAPHORE-EXPLANATION.md",
        "pdf": "OWL-SEMAPHORE-EXPLANATION.pdf",
        "badge": "assets/releases/540/NORM-composite-transparent-540.png",
        "contact_sheet": "assets/proofs/OWL-SEMAPHORE-MASTER-PROOF.png",
        "color": "#d4a853",
        "color_rgb": "rgb(212, 168, 83)",
        "label": "E X P L A N A T I O N",
        "label_compact": "EXPLANATION",
        "title": "Owl Semaphore — Explanation",
        "subtitle_typst": "Origin story, archetype rationale, why two states were not enough",
        "transform_text": "I",
        "det_text": "+1",
        "mapping_text": "(x, y) → (x, y)",
        "mathline": "Informative companion to OWL-SEMAPHORE-SYSTEM",
        "quote": '"Four owls tell the reader what kind of thinking they are looking at."',
        "standard_ref": "Informative (this entire document)",
        "contact_caption": "Owl Semaphore — Four-State Master Proof",
        "keywords": "Owl Semaphore, explanation, origin story, archetype, DNS Tool, RFC 2119, V4, WCAG, ICD 203, seL4",
        "subject": "Informative companion to the Owl Semaphore system specification: origin story and design rationale.",
    },
]


def preprocess_md(md_path):
    """Read markdown, strip front image, convert \\(...\\) inline math to $...$.

    Also strip the top-level heading and version line — they're rendered
    from the template's title block, not the body.
    """
    with open(md_path, "r") as f:
        lines = f.readlines()

    # Strip leading image line
    if lines and lines[0].startswith("!["):
        lines = lines[1:]

    text = "".join(lines).strip()

    # Convert \(...\) inline math to $...$ for pandoc->typst.
    text = re.sub(r"\\\((.+?)\\\)", r"$\1$", text)

    new_lines = []
    skip_count = 0
    for line in text.split("\n"):
        if skip_count < 4 and (
            line.startswith("# OWL SEMAPHORE")
            or line.startswith("# OWL-SEMAPHORE-EXPLANATION")
            or line.startswith("## OWL ")
            or line.startswith("## Version")
            or line.startswith("### Version")
        ):
            skip_count += 1
            continue
        new_lines.append(line)

    text = "\n".join(new_lines).strip()
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


def typst_escape(s):
    """Escape a string for safe interpolation inside a Typst string literal."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


def build_typst_document(doc, body_typst):
    """Build complete Typst source with header, styling, contact sheet, and ledger."""

    badge_path = doc["badge"]
    contact_path = doc["contact_sheet"]
    color = doc["color_rgb"]
    is_system = doc["md"] == "OWL-SEMAPHORE-SYSTEM.md"

    # Per-state badge paths used in the classification ledger.
    norm_badge = "assets/releases/540/NORM-composite-transparent-540.png"
    nonnorm_badge = "assets/releases/540/NONNORM-composite-transparent-540.png"
    crit_badge = "assets/releases/540/CRIT-composite-transparent-540.png"
    meta_badge = "assets/releases/540/META-composite-transparent-540.png"

    # PDF document-info metadata.
    pdf_title = typst_escape(doc["title"])
    pdf_keywords = typst_escape(doc["keywords"])
    pdf_subject = typst_escape(doc["subject"])
    pdf_author = typst_escape(AUTHOR)

    # Banner tuple — a fixed-format machine-parseable block on page 1 that
    # tests/test_banner_tuple.py reads back out of the rendered PDF.
    banner_block = (
        f"BANNER TUPLE BEGIN\\n"
        f"state={doc['label_compact']}\\n"
        f"transform={doc['transform_text']}\\n"
        f"determinant={doc['det_text']}\\n"
        f"mapping={doc['mapping_text']}\\n"
        f"version={VERSION_LABEL}\\n"
        f"concept_doi={CONCEPT_DOI}\\n"
        f"version_doi={VERSION_DOI}\\n"
        f"last_published_doi={LAST_VERSION_DOI}\\n"
        f"license={LICENSE}\\n"
        f"BANNER TUPLE END"
    )

    return f'''// Owl Semaphore PDF — generated by generate_pdfs.py
#set document(
  title: "{pdf_title}",
  author: "{pdf_author}",
  keywords: ("Owl Semaphore", "{doc['label_compact']}", "V4", "Klein four-group", "epistemic notation", "DNS Tool"),
  description: "{pdf_subject} Version {VERSION_LABEL}. Concept DOI {CONCEPT_DOI}. License {LICENSE}.",
)

#set page(
  paper: "us-letter",
  margin: (top: 96pt, bottom: 72pt, left: 72pt, right: 72pt),
  header: context {{
    // Per-page running owl header (suppressed on the title page).
    let p = counter(page).get().first()
    if p > 1 [
      #set text(8pt, fill: luma(110))
      #grid(
        columns: (auto, 1fr, auto),
        align: (left + horizon, center + horizon, right + horizon),
        [#image("{badge_path}", height: 20pt)],
        [
          #text(weight: "bold", tracking: 2pt)[{doc["label_compact"]}]
          #h(8pt)
          T = #raw("{doc["transform_text"]}")
          #h(6pt)
          det = #raw("{doc["det_text"]}")
          #h(6pt)
          #raw("{doc["mapping_text"]}")
        ],
        [Owl Semaphore · {VERSION_LABEL}],
      )
      #v(2pt)
      #line(length: 100%, stroke: 0.4pt + {color})
    ]
  }},
  footer: context {{
    set text(8pt, fill: luma(140))
    grid(
      columns: (1fr, 1fr, 1fr),
      align: (left, center, right),
      [Owl Semaphore · {VERSION_LABEL} · CC BY 4.0],
      [#counter(page).display("1 of 1", both: true)],
      [{REPO_URL} · concept DOI {CONCEPT_DOI}],
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
  #v(12pt)
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

  #text(size: 11pt, weight: "bold")[{AUTHOR}] \\
  #text(size: 10pt, fill: luma(80))[Independent DNS Security Researcher]

  #v(6pt)
  #text(size: 8.5pt, fill: luma(120))[
    ORCID {ORCID} #h(12pt) Concept DOI {CONCEPT_DOI} \\
    Last published version DOI {LAST_VERSION_DOI} #h(12pt) v1.3.0 version DOI {VERSION_DOI} \\
    SOURCE {REPO_URL} #h(12pt) VERSION {VERSION_LABEL} · LICENSE {LICENSE}
  ]
  #v(6pt)
  #text(size: 8pt, fill: luma(100), style: "italic")[
    Canonical: {CANONICAL_SENTENCE}
  ]
  #v(12pt)
]

#line(length: 100%, stroke: 1.5pt + {color})

// ── Banner tuple (machine-parseable; used by scripts/verify_banner_tuple.py) ─

#v(10pt)
#block(
  fill: luma(248),
  inset: 8pt,
  radius: 2pt,
  width: 100%,
  text(size: 7.5pt, font: "DejaVu Sans Mono", fill: luma(70))[#raw("{banner_block}")],
)
#v(8pt)

// ════════════════════════════════════════════════════════════════════════════
// CONTACT SHEET
// ════════════════════════════════════════════════════════════════════════════

#v(12pt)
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
    align(center, image("{norm_badge}", width: 80pt)),
    align(center, image("{nonnorm_badge}", width: 80pt)),
    align(center, image("{crit_badge}", width: 80pt)),
    align(center, image("{meta_badge}", width: 80pt)),
    align(center, text(size: 8pt, weight: "bold", tracking: 1.5pt)[NORMATIVE]),
    align(center, text(size: 8pt, weight: "bold", tracking: 1.5pt)[NON-NORMATIVE]),
    align(center, text(size: 8pt, weight: "bold", tracking: 1.5pt)[CRITICAL]),
    align(center, text(size: 8pt, weight: "bold", tracking: 1.5pt)[METACOGNITIVE]),
    align(center, text(size: 7.5pt, fill: luma(100))[T = I #h(4pt) det = +1]),
    align(center, text(size: 7.5pt, fill: luma(100))[T = σ#sub[v] #h(4pt) det = −1]),
    align(center, text(size: 7.5pt, fill: luma(100))[T = C#sub[2] #h(4pt) det = +1]),
    align(center, text(size: 7.5pt, fill: luma(100))[T = σ#sub[h] #h(4pt) det = −1]),
    align(center, text(size: 7.5pt, fill: luma(100))[(x, y) → (x, y)]),
    align(center, text(size: 7.5pt, fill: luma(100))[(x, y) → (−x, y)]),
    align(center, text(size: 7.5pt, fill: luma(100))[(x, y) → (−x, −y)]),
    align(center, text(size: 7.5pt, fill: luma(100))[(x, y) → (x, −y)]),
    align(center, text(size: 7.5pt, style: "italic", fill: luma(100))["This is the standard."]),
    align(center, text(size: 7.5pt, style: "italic", fill: luma(100))["This reflects the standard."]),
    align(center, text(size: 7.5pt, style: "italic", fill: luma(100))["This inverts the standard."]),
    align(center, text(size: 7.5pt, style: "italic", fill: luma(100))["This audits the standard."]),
    align(center, text(size: 7pt, fill: luma(140))[RFC 2119 MUST / SHALL]),
    align(center, text(size: 7pt, fill: luma(140))[Informative / Advisory (NOTE)]),
    align(center, text(size: 7pt, fill: luma(140))[RFC 2119 MUST NOT / SHALL NOT]),
    align(center, text(size: 7pt, fill: luma(140))[Epistemic / Framework (META)]),
  )

  #v(20pt)
  #line(length: 60%, stroke: 0.5pt + luma(200))
  #v(8pt)
  #text(size: 8pt, fill: luma(140))[
    Owl Semaphore {VERSION_LABEL} · {REPO_URL} · concept DOI {CONCEPT_DOI} \\
    Last published version DOI {LAST_VERSION_DOI} · v1.3.0 version DOI {VERSION_DOI} \\
    © 2024–2026 IT Help San Diego Inc. · Licensed under {LICENSE}
  ]
]

#v(1fr)
'''


def generate_pdf(doc):
    """Generate a single PDF from its doc spec."""
    md_path = os.path.join(REPO, doc["md"])
    pdf_path = os.path.join(REPO, doc["pdf"])

    if not os.path.exists(md_path):
        print(f"  SKIP missing source: {doc['md']}", file=sys.stderr)
        return False

    print(f"  Reading {doc['md']}...")
    md_text = preprocess_md(md_path)

    print(f"  Converting to Typst...")
    body_typst = md_to_typst(md_text)

    print(f"  Building Typst source...")
    typst_source = build_typst_document(doc, body_typst)

    typ_path = os.path.join(REPO, doc["pdf"].replace(".pdf", ".typ"))
    with open(typ_path, "w") as f:
        f.write(typst_source)

    print(f"  Compiling {doc['pdf']}...")
    try:
        typst.compile(typ_path, output=pdf_path, root=REPO)
    except Exception as exc:
        print(f"  ERROR compiling {doc['pdf']}: {exc}", file=sys.stderr)
        return False
    finally:
        # Keep .typ on error for debugging; only delete on success.
        if os.path.exists(pdf_path):
            try:
                os.remove(typ_path)
            except OSError:
                pass

    size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
    print(f"  OK {doc['pdf']} ({size_mb:.1f} MB)")
    return True


def main():
    print("Owl Semaphore PDF Generator")
    print(f"Version: {VERSION_LABEL}")
    print("=" * 60)

    success = 0
    for doc in DOCS:
        print(f"\n[{doc['label_compact']}] {doc['title']}")
        if generate_pdf(doc):
            success += 1

    print(f"\n{'=' * 60}")
    print(f"Generated {success}/{len(DOCS)} PDFs")

    if success < len(DOCS):
        sys.exit(1)


if __name__ == "__main__":
    main()
