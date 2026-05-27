#!/usr/bin/env python3
"""
Generate publication-grade PDFs for the Owl Semaphore system (v2.0.0).

Produces, with one command, five PDFs:
  - OWL-SEMAPHORE-SYSTEM.pdf
  - OWL-SEMAPHORE-EXPLANATION.pdf
  - OWL-1-NORMATIVE.pdf
  - OWL-2-NON-NORMATIVE.pdf
  - OWL-3-CRITICAL.pdf
  - OWL-4-METACOGNITIVE.pdf

Each PDF carries:
  - Per-page owl header (badge thumbnail + state token in the running header)
  - Title page with badge image and banner tuple (state / transform / det / mapping / quote)
  - Contact-sheet header
  - Body content (rendered from the matching .md via pandoc -> typst)
  - Classification ledger back page
  - Footer with version, page numbers, repository URL, DOI
  - Embedded PDF metadata (Title, Author, Subject, Keywords, Producer/Creator) set via qpdf

Requires: pandoc (cli), typst (python package), qpdf (cli; optional but used to set
PDF metadata). Falls back gracefully if qpdf is missing.

Usage:  python3 generate_pdfs.py   (or: make pdfs)
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from typing import Optional

try:
    import typst  # type: ignore
except ImportError:  # pragma: no cover - handled at runtime
    typst = None  # type: ignore

REPO = os.path.dirname(os.path.abspath(__file__))

# ── Project-wide metadata (v2.0.0) ──────────────────────────────────────────

VERSION = "2.0.0"
RELEASE_LABEL = "v2.0.0"
AUTHOR = "Carey James Balboa"
ORCID = "0009-0000-5237-9065"
REPO_URL = "github.com/IT-Help-San-Diego/owl-semaphore"
CONCEPT_DOI = "10.5281/zenodo.19473697"
PUBLISHED_VERSION_DOI = "10.5281/zenodo.19474599"  # v1.2.0 (previous published)
VERSION_DOI = "10.5281/zenodo.20418539"  # v2.0.0 (minted)
LICENSE = "CC-BY-4.0"

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
        "state_token": "SYSTEM",
        "title": "Owl Semaphore",
        "subtitle_typst": "System Specification — A Finite Algebra of Epistemic States",
        "mathline": "T = I    det = +1    (x, y) -> (x, y)",
        "quote": '"This is the standard."',
        "standard_ref": "RFC 2119 MUST / SHALL",
        "contact_caption": "Owl Semaphore System — Master Proof",
        "pdf_subject": "Owl Semaphore System Specification (v2.0.0)",
    },
    {
        "md": "OWL-SEMAPHORE-EXPLANATION.md",
        "pdf": "OWL-SEMAPHORE-EXPLANATION.pdf",
        "badge": "assets/releases/540/META-composite-transparent-540.png",
        "contact_sheet": "assets/proofs/OWL-SEMAPHORE-MASTER-PROOF.png",
        "color": "#8C4191",
        "color_rgb": "rgb(140, 65, 145)",
        "label": "E X P L A N A T I O N",
        "state_token": "EXPLAIN",
        "title": "Owl Semaphore — Explanation",
        "subtitle_typst": "Informative Companion — Origin Story, Archetype Rationale, Accessibility",
        "mathline": "V4 = { I, sigma_v, C2, sigma_h }",
        "quote": '"Thinking examines its own frame."',
        "standard_ref": "Informative / Explanatory",
        "contact_caption": "Owl Semaphore System — Master Proof",
        "pdf_subject": "Owl Semaphore Explanation (informative companion, v2.0.0)",
    },
    {
        "md": "OWL-1-NORMATIVE.md",
        "pdf": "OWL-1-NORMATIVE.pdf",
        "badge": "assets/releases/540/NORM-composite-transparent-540.png",
        "contact_sheet": "assets/proofs/NORM-layer-proof-palette.png",
        "color": "#d4a853",
        "color_rgb": "rgb(212, 168, 83)",
        "label": "N O R M A T I V E",
        "state_token": "NORMATIVE",
        "title": "Owl Semaphore — Normative",
        "subtitle_typst": "OWL 1 / Identity State / Standard Specification",
        "mathline": "T = I    det = +1    (x, y) -> (x, y)",
        "quote": '"This is the standard."',
        "standard_ref": "RFC 2119 MUST / SHALL",
        "contact_caption": "Normative — Layer Proof Palette",
        "pdf_subject": "Owl Semaphore — Normative state specification (OWL 1 / I, v2.0.0)",
    },
    {
        "md": "OWL-2-NON-NORMATIVE.md",
        "pdf": "OWL-2-NON-NORMATIVE.pdf",
        "badge": "assets/releases/540/NONNORM-composite-transparent-540.png",
        "contact_sheet": "assets/proofs/NONNORM-layer-proof-palette.png",
        "color": "#316964",
        "color_rgb": "rgb(49, 105, 100)",
        "label": "N O N - N O R M A T I V E",
        "state_token": "NON-NORMATIVE",
        "title": "Owl Semaphore — Non-Normative",
        "subtitle_typst": "OWL 2 / Reflection State (sigma_v) / Standard Specification",
        "mathline": "T = sigma_v    det = -1    (x, y) -> (-x, y)",
        "quote": '"This reflects the standard."',
        "standard_ref": "Informative / Advisory (NOTE)",
        "contact_caption": "Non-Normative — Layer Proof Palette",
        "pdf_subject": "Owl Semaphore — Non-Normative state specification (OWL 2 / sigma_v, v2.0.0)",
    },
    {
        "md": "OWL-3-CRITICAL.md",
        "pdf": "OWL-3-CRITICAL.pdf",
        "badge": "assets/releases/540/CRIT-composite-transparent-540.png",
        "contact_sheet": "assets/proofs/CRIT-layer-proof-palette.png",
        "color": "#990f1e",
        "color_rgb": "rgb(153, 15, 30)",
        "label": "C R I T I C A L",
        "state_token": "CRITICAL",
        "title": "Owl Semaphore — Critical",
        "subtitle_typst": "OWL 3 / Inversion State (C2) / Standard Specification",
        "mathline": "T = C2    det = +1    (x, y) -> (-x, -y)",
        "quote": '"This inverts the standard."',
        "standard_ref": "RFC 2119 MUST NOT / SHALL NOT",
        "contact_caption": "Critical — Layer Proof Palette",
        "pdf_subject": "Owl Semaphore — Critical state specification (OWL 3 / C2, v2.0.0)",
    },
    {
        "md": "OWL-4-METACOGNITIVE.md",
        "pdf": "OWL-4-METACOGNITIVE.pdf",
        "badge": "assets/releases/540/META-composite-transparent-540.png",
        "contact_sheet": "assets/proofs/META-layer-proof-palette.png",
        "color": "#8C4191",
        "color_rgb": "rgb(140, 65, 145)",
        "label": "M E T A C O G N I T I V E",
        "state_token": "METACOGNITIVE",
        "title": "Owl Semaphore — Metacognitive",
        "subtitle_typst": "OWL 4 / Frame-Audit State (sigma_h) / Standard Specification",
        "mathline": "T = sigma_h    det = -1    (x, y) -> (x, -y)",
        "quote": '"The observer audits the frame."',
        "standard_ref": "Epistemic / Framework (META)",
        "contact_caption": "Metacognitive — Layer Proof Palette",
        "pdf_subject": "Owl Semaphore — Metacognitive state specification (OWL 4 / sigma_h, v2.0.0)",
    },
]


def _typst_str(s: str) -> str:
    """Escape a Python string for safe embedding inside Typst double-quoted strings."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


def preprocess_md(md_path: str) -> str:
    with open(md_path, "r") as f:
        text = f.read()

    lines = text.splitlines()

    # Strip a leading image line
    if lines and lines[0].startswith("!["):
        lines = lines[1:]

    text = "\n".join(lines).strip()
    # Convert \(...\) inline math to $...$
    text = re.sub(r"\\\((.+?)\\\)", r"$\1$", text)

    # Drop the top-of-document title block lines that we render via the template.
    new_lines = []
    skipped = 0
    for line in text.split("\n"):
        if skipped < 3 and (
            line.startswith("# OWL SEMAPHORE")
            or line.startswith("## OWL ")
            or line.startswith("### Version")
            or line.startswith("## Version")
        ):
            skipped += 1
            continue
        new_lines.append(line)
    text = "\n".join(new_lines).strip()
    text = re.sub(r"^---\s*\n", "", text)
    return text


def md_to_typst(md_text: str) -> str:
    result = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "typst", "--wrap=none"],
        input=md_text,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"pandoc error: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    body = result.stdout
    # Pandoc emits heading id labels like ``<my-section-id>`` after each heading.
    # Typst's label parser rejects characters that aren't valid label chars (dots,
    # unicode digits like ₄). We don't use those labels for anything in this
    # pipeline, so strip them entirely.
    body = re.sub(r"\s*<[^>\n]*>\s*$", "", body, flags=re.MULTILINE)
    return body


def build_typst_document(doc: dict, body_typst: str) -> str:
    badge_path = doc["badge"]
    contact_path = doc["contact_sheet"]
    color = doc["color_rgb"]
    is_system = doc["md"] == "OWL-SEMAPHORE-SYSTEM.md"

    norm_badge = "assets/releases/540/NORM-composite-transparent-540.png"
    nonnorm_badge = "assets/releases/540/NONNORM-composite-transparent-540.png"
    crit_badge = "assets/releases/540/CRIT-composite-transparent-540.png"
    meta_badge = "assets/releases/540/META-composite-transparent-540.png"

    state_token = doc["state_token"]
    label_long = doc["label"]
    mathline = doc["mathline"]
    quote = doc["quote"]
    standard_ref = doc["standard_ref"]
    title = doc["title"]
    subtitle = doc["subtitle_typst"]
    contact_caption = doc["contact_caption"]

    # Stable banner-tuple line — every PDF page-1 must contain this exact string
    # so the banner-tuple test can verify it.
    banner_tuple = (
        f"BANNER-TUPLE :: STATE={state_token} :: TRANSFORM={mathline} :: "
        f"QUOTE={quote} :: VERSION={RELEASE_LABEL} :: CONCEPT-DOI={CONCEPT_DOI} :: "
        f"PUBLISHED-VERSION-DOI={PUBLISHED_VERSION_DOI} :: "
        f"VERSION-DOI={VERSION_DOI}"
    )

    return f'''// Owl Semaphore PDF — generated by generate_pdfs.py ({RELEASE_LABEL})
#set document(
  title: "{_typst_str(title)} ({RELEASE_LABEL})",
  author: "{_typst_str(AUTHOR)}",
  keywords: ("Owl Semaphore", "Klein four-group", "V4", "epistemic notation",
             "{state_token}", "DNS Tool", "accessibility", "metacognition"),
)

#let header-color = {color}
#let owl-badge = "{badge_path}"
#let state-token = "{_typst_str(state_token)}"

#set page(
  paper: "us-letter",
  margin: (top: 90pt, bottom: 72pt, left: 72pt, right: 72pt),
  header: context {{
    set text(8pt, fill: luma(110))
    grid(
      columns: (auto, 1fr, auto),
      align: (left + horizon, center + horizon, right + horizon),
      box(height: 24pt)[#image(owl-badge, height: 22pt)],
      [#text(weight: "bold", tracking: 2pt, fill: header-color)[#state-token] #h(8pt) #text(fill: luma(140))[Owl Semaphore · {RELEASE_LABEL}]],
      [#text(fill: luma(140))[{REPO_URL}]],
    )
    v(2pt)
    line(length: 100%, stroke: 0.5pt + luma(200))
  }},
  footer: context {{
    set text(8pt, fill: luma(140))
    grid(
      columns: (1fr, 1fr, 1fr),
      align: (left, center, right),
      [Owl Semaphore · {RELEASE_LABEL}],
      [#counter(page).display("1 of 1", both: true)],
      [DOI {CONCEPT_DOI} · CC-BY-4.0],
    )
  }},
)

#set text(font: "New Computer Modern", size: 11pt)
#set par(justify: true, leading: 0.65em)

#let horizontalrule = line(length: 100%, stroke: 0.5pt + luma(200))

#show heading.where(level: 1): it => {{
  v(18pt)
  line(length: 100%, stroke: 1.5pt + header-color)
  v(6pt)
  set text(size: 16pt, weight: "bold", fill: header-color)
  it.body
  v(3pt)
  line(length: 100%, stroke: 0.75pt + header-color)
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

#set table(
  stroke: 0.5pt + luma(180),
  inset: 6pt,
)

// =====================================================================
// TITLE PAGE  (banner-tuple line is on page 1 by construction)
// =====================================================================

#align(center)[
  #v(12pt)
  #image("{badge_path}", width: 140pt)
  #v(8pt)

  #text(size: 10pt, weight: "bold", fill: header-color, tracking: 3pt)[{label_long}]

  #v(4pt)
  #text(size: 9pt, fill: luma(80))[#raw("{_typst_str(mathline)}")]

  #v(2pt)
  #text(size: 9.5pt, style: "italic", fill: luma(80))[{_typst_str(quote)}]

  #text(size: 8.5pt, fill: luma(120))[{_typst_str(standard_ref)}]

  #v(16pt)
  #text(size: 28pt, weight: "bold")[{_typst_str(title)}]
  #v(4pt)
  #text(size: 12pt, fill: luma(80))[{subtitle}]
  #v(10pt)

  #text(size: 11pt, weight: "bold")[{AUTHOR}] \\
  #text(size: 10pt, fill: luma(80))[Independent DNS Security Researcher]

  #v(6pt)
  #text(size: 8.5pt, fill: luma(120))[
    ORCID {ORCID} #h(12pt) CONCEPT-DOI {CONCEPT_DOI} \\
    PUBLISHED-VERSION-DOI {PUBLISHED_VERSION_DOI} (v1.2.0) #h(12pt) VERSION-DOI {VERSION_DOI} \\
    SOURCE {REPO_URL} #h(12pt) VERSION {RELEASE_LABEL} · LICENSE {LICENSE}
  ]
  #v(8pt)

  // Banner-tuple (machine-readable, required for tests/test_banner_tuple.py)
  #text(size: 6.5pt, fill: luma(160), font: "Courier", tracking: 0pt)[
    #raw("{_typst_str(banner_tuple)}")
  ]
  #v(8pt)
]

#line(length: 100%, stroke: 1.5pt + header-color)

// =====================================================================
// CONTACT SHEET
// =====================================================================

#v(16pt)
#align(center)[
  #text(size: 9pt, weight: "bold", fill: luma(100), tracking: 1.5pt)[
    {_typst_str(contact_caption.upper())}
  ]
  #v(8pt)
  #image("{contact_path}", width: {"85%" if not is_system else "90%"})
]
#v(12pt)

// =====================================================================
// BODY CONTENT
// =====================================================================

{body_typst}

// =====================================================================
// CLASSIFICATION LEDGER (BACK PAGE)
// =====================================================================

#pagebreak()

#v(1fr)

#line(length: 100%, stroke: 1.5pt + header-color)
#v(12pt)

#align(center)[
  #text(size: 10pt, weight: "bold", fill: luma(80), tracking: 2pt)[
    OWL SEMAPHORE SYSTEM — CLASSIFICATION LEDGER ({RELEASE_LABEL})
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
    align(center, text(size: 7.5pt, fill: luma(100))[T = #sym.sigma#sub[v] #h(4pt) det = -1]),
    align(center, text(size: 7.5pt, fill: luma(100))[T = C#sub[2] #h(4pt) det = +1]),
    align(center, text(size: 7.5pt, fill: luma(100))[T = #sym.sigma#sub[h] #h(4pt) det = -1]),
    align(center, text(size: 7.5pt, fill: luma(100))[(x, y) -> (x, y)]),
    align(center, text(size: 7.5pt, fill: luma(100))[(x, y) -> (-x, y)]),
    align(center, text(size: 7.5pt, fill: luma(100))[(x, y) -> (-x, -y)]),
    align(center, text(size: 7.5pt, fill: luma(100))[(x, y) -> (x, -y)]),
    align(center, text(size: 7.5pt, style: "italic", fill: luma(100))["This is the standard."]),
    align(center, text(size: 7.5pt, style: "italic", fill: luma(100))["This reflects the standard."]),
    align(center, text(size: 7.5pt, style: "italic", fill: luma(100))["This inverts the standard."]),
    align(center, text(size: 7.5pt, style: "italic", fill: luma(100))["The observer audits the frame."]),
    align(center, text(size: 7pt, fill: luma(140))[RFC 2119 MUST / SHALL]),
    align(center, text(size: 7pt, fill: luma(140))[Informative / Advisory (NOTE)]),
    align(center, text(size: 7pt, fill: luma(140))[RFC 2119 MUST NOT / SHALL NOT]),
    align(center, text(size: 7pt, fill: luma(140))[Epistemic / Framework (META)]),
  )

  #v(16pt)
  #text(size: 7.5pt, style: "italic", fill: luma(120))[
    Accessibility: color is not the only carrier. State identity is recoverable from color #h(2pt) + #h(2pt) orientation #h(2pt) + #h(2pt) textual label (WCAG 2.2 SC 1.4.1).
  ]

  #v(12pt)
  #line(length: 60%, stroke: 0.5pt + luma(200))
  #v(8pt)
  #text(size: 8pt, fill: luma(140))[
    Owl Semaphore {RELEASE_LABEL} · {REPO_URL} \\
    Concept DOI {CONCEPT_DOI} · v1.2.0 DOI {PUBLISHED_VERSION_DOI} · v2.0.0 DOI {VERSION_DOI} \\
    (c) 2024-2026 IT Help San Diego Inc. · Licensed under {LICENSE}
  ]
]

#v(1fr)
'''


def _set_pdf_metadata(pdf_path: str, doc: dict) -> None:
    """Use qpdf to embed Title/Author/Subject/Keywords/Creator/Producer into the PDF.

    Falls back silently if qpdf is missing or fails.
    """
    qpdf = shutil.which("qpdf")
    if not qpdf:
        return

    keywords = ", ".join([
        "Owl Semaphore",
        "Klein four-group",
        "V4",
        "epistemic notation",
        doc["state_token"],
        "DNS Tool",
        "accessibility",
        "metacognition",
        RELEASE_LABEL,
    ])
    subject = doc["pdf_subject"]
    title = f'{doc["title"]} ({RELEASE_LABEL})'

    # qpdf can rewrite the docinfo dict via --qdf+ JSON; the most portable
    # approach is to use --replace-input with a simple metadata overlay.
    # We use qpdf's --override-content-encryption-key-length / --linearize?
    # Simplest reliable path: qpdf has no direct CLI for docinfo, so use a
    # short python pdf re-writer via pikepdf if present; else skip.
    try:
        import pikepdf  # type: ignore
    except Exception:
        pikepdf = None  # type: ignore

    if pikepdf is None:
        return

    try:
        with pikepdf.open(pdf_path, allow_overwriting_input=True) as pdf:
            with pdf.open_metadata(set_pikepdf_as_editor=False) as meta:
                meta["dc:title"] = title
                meta["dc:creator"] = [AUTHOR]
                meta["dc:description"] = subject
                meta["pdf:Keywords"] = keywords
                meta["dc:subject"] = keywords.split(", ")
                meta["xmp:CreatorTool"] = f"owl-semaphore/generate_pdfs.py {RELEASE_LABEL}"
            pdf.docinfo["/Title"] = title
            pdf.docinfo["/Author"] = AUTHOR
            pdf.docinfo["/Subject"] = subject
            pdf.docinfo["/Keywords"] = keywords
            pdf.docinfo["/Creator"] = f"owl-semaphore/generate_pdfs.py {RELEASE_LABEL}"
            pdf.docinfo["/Producer"] = "typst (via python-typst) + pikepdf"
            pdf.save()
    except Exception as exc:  # pragma: no cover
        print(f"  ! pikepdf metadata embed failed for {pdf_path}: {exc}", file=sys.stderr)


def generate_pdf(doc: dict) -> bool:
    if typst is None:
        print(
            "  ERROR: the 'typst' Python package is not installed. "
            "Run: pip install typst",
            file=sys.stderr,
        )
        return False

    md_path = os.path.join(REPO, doc["md"])
    pdf_path = os.path.join(REPO, doc["pdf"])
    print(f"  Reading {doc['md']}...")
    md_text = preprocess_md(md_path)
    print("  Converting to Typst...")
    body_typst = md_to_typst(md_text)
    print("  Building document...")
    typst_source = build_typst_document(doc, body_typst)

    typ_path = os.path.join(REPO, doc["pdf"].replace(".pdf", ".typ"))
    with open(typ_path, "w") as f:
        f.write(typst_source)

    print(f"  Compiling {doc['pdf']}...")
    try:
        compiler = typst.Compiler(input=typ_path, root=REPO)
        compiler.compile(output=pdf_path)
    except Exception as exc:
        print(f"  ERROR compiling {doc['pdf']}: {exc}", file=sys.stderr)
        return False
    finally:
        try:
            os.remove(typ_path)
        except OSError:
            pass

    _set_pdf_metadata(pdf_path, doc)

    size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
    print(f"  OK  {doc['pdf']} ({size_mb:.1f} MB)")
    return True


def main() -> None:
    print(f"Owl Semaphore PDF Generator ({RELEASE_LABEL})")
    print("=" * 60)

    success = 0
    for doc in DOCS:
        print(f"\n[{doc['state_token']}] {doc['title']}")
        if generate_pdf(doc):
            success += 1

    print(f"\n{'=' * 60}")
    print(f"Generated {success}/{len(DOCS)} PDFs")

    if success < len(DOCS):
        sys.exit(1)


if __name__ == "__main__":
    main()
