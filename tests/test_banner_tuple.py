"""Banner-tuple PDF integrity test (v2.0.2).

Each generated PDF in the Owl Semaphore release embeds a single-line
``BANNER-TUPLE :: ...`` string on its title page that names the state, the
operator/transform, the determinant, the coordinate mapping, the canonical
quote, the version, the v2.0.2 reserved version-specific DOI, the concept
DOI (all-versions), and the previous-published version DOI (v2.0.1). The
v2.0.2 version-specific DOI is reserved on Zenodo before the release and
embedded directly into the PDFs that Zenodo archives, so the version DOI
inside the PDF exactly matches the DOI Zenodo publishes for the release.

This test extracts page-one text from each PDF via ``pdftotext -layout`` and
verifies that the banner tuple is present and that every expected field is
correct. It is the project's defense against silent PDF drift: if someone
regenerates a PDF from a stale or doctored source, this test fails.

The test is skipped (not failed) for any PDF that is not present on disk so
that ``make test`` can run usefully before ``make pdfs`` has been executed in
clean checkouts. It fails hard for any PDF that *is* present but whose tuple
disagrees with the expected values.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VERSION = "v2.0.2"
VERSION_DOI = "10.5281/zenodo.20433053"  # v2.0.2 reserved version-specific DOI
CONCEPT_DOI = "10.5281/zenodo.19473697"
PREVIOUS_VERSION_DOI = "10.5281/zenodo.20419874"  # v2.0.1 (previous published)

# (state, transform substring, det sign, mapping substring, quote, pdf filename)
EXPECTED = [
    (
        "SYSTEM",
        "T = I",
        "+1",
        "(x, y) -> (x, y)",
        '"This is the standard."',
        "OWL-SEMAPHORE-SYSTEM.pdf",
    ),
    (
        "EXPLAIN",
        "V4 = { I, sigma_v, C2, sigma_h }",
        None,
        None,
        '"Thinking examines its own frame."',
        "OWL-SEMAPHORE-EXPLANATION.pdf",
    ),
    (
        "NORMATIVE",
        "T = I",
        "+1",
        "(x, y) -> (x, y)",
        '"This is the standard."',
        "OWL-1-NORMATIVE.pdf",
    ),
    (
        "NON-NORMATIVE",
        "T = sigma_v",
        "-1",
        "(x, y) -> (-x, y)",
        '"This reflects the standard."',
        "OWL-2-NON-NORMATIVE.pdf",
    ),
    (
        "CRITICAL",
        "T = C2",
        "+1",
        "(x, y) -> (-x, -y)",
        '"This inverts the standard."',
        "OWL-3-CRITICAL.pdf",
    ),
    (
        "METACOGNITIVE",
        "T = sigma_h",
        "-1",
        "(x, y) -> (x, -y)",
        '"The observer audits the frame."',
        "OWL-4-METACOGNITIVE.pdf",
    ),
]


def _extract_page1_text(pdf_path: str) -> str:
    if not shutil.which("pdftotext"):
        raise unittest.SkipTest("pdftotext not available in this environment")
    out = subprocess.run(
        ["pdftotext", "-layout", "-f", "1", "-l", "1", pdf_path, "-"],
        capture_output=True,
        text=True,
        check=False,
    )
    if out.returncode != 0:
        raise AssertionError(f"pdftotext failed for {pdf_path}: {out.stderr}")
    return out.stdout


def _normalize(text: str) -> str:
    """Collapse soft-wrapped pdftotext output to a single search-friendly string.

    pdftotext can break the small Courier banner-tuple line in the middle of a
    token at a hyphen (e.g. ``CONCEPT-\\n  DOI``) or at a slash (e.g.
    ``10.5281/\\n  zenodo.19473697``). We undo both by stripping whitespace that
    follows a hyphen or slash, then collapsing any remaining whitespace to
    single spaces.
    """
    rejoined = re.sub(r"([-/])\s+", r"\1", text)
    return re.sub(r"\s+", " ", rejoined)


class BannerTupleTest(unittest.TestCase):
    """Verify each generated PDF's page-one banner tuple."""

    def _assert_pdf(self, state, transform, det, mapping, quote, pdf_name):
        pdf_path = os.path.join(REPO, pdf_name)
        if not os.path.exists(pdf_path):
            self.skipTest(f"{pdf_name} not generated yet (run `make pdfs`)")
        raw = _extract_page1_text(pdf_path)
        text = _normalize(raw)

        for needle, message in (
            ("BANNER-TUPLE", f"{pdf_name} page 1 is missing the BANNER-TUPLE marker"),
            (f"STATE={state}", f"{pdf_name} banner tuple does not report STATE={state}"),
            (_normalize(transform), f"{pdf_name} banner tuple does not report transform {transform}"),
            (_normalize(quote), f"{pdf_name} banner tuple does not contain canonical quote {quote}"),
            (f"VERSION={VERSION}", f"{pdf_name} banner tuple does not report VERSION={VERSION}"),
            (f"VERSION-DOI={VERSION_DOI}", f"{pdf_name} banner tuple does not report VERSION-DOI={VERSION_DOI} (v2.0.2 reserved)"),
            (f"CONCEPT-DOI={CONCEPT_DOI}", f"{pdf_name} banner tuple does not report CONCEPT-DOI={CONCEPT_DOI}"),
            (f"PREVIOUS-VERSION-DOI={PREVIOUS_VERSION_DOI}", f"{pdf_name} banner tuple does not report PREVIOUS-VERSION-DOI={PREVIOUS_VERSION_DOI} (v2.0.1)"),
        ):
            self.assertIn(needle, text, message)
        if det is not None:
            self.assertIn(
                f"det = {det}",
                text,
                f"{pdf_name} banner tuple does not report det = {det}",
            )
        if mapping is not None:
            self.assertIn(
                _normalize(mapping),
                text,
                f"{pdf_name} banner tuple does not report mapping {mapping}",
            )

    def test_deprecated_quote_absent_from_meta_ledger(self):
        """The deprecated METACOGNITIVE wording 'This audits the standard.' must
        not appear in the METACOGNITIVE PDF or the system PDF in v2.0.2."""
        for pdf_name in ("OWL-4-METACOGNITIVE.pdf", "OWL-SEMAPHORE-SYSTEM.pdf"):
            pdf_path = os.path.join(REPO, pdf_name)
            if not os.path.exists(pdf_path):
                continue
            if not shutil.which("pdftotext"):
                self.skipTest("pdftotext not available in this environment")
            out = subprocess.run(
                ["pdftotext", "-layout", pdf_path, "-"],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotIn(
                "This audits the standard.",
                out.stdout,
                f"{pdf_name} still contains deprecated wording 'This audits the standard.'",
            )


def _add_per_pdf_tests():
    for state, transform, det, mapping, quote, pdf_name in EXPECTED:
        def _make(state=state, transform=transform, det=det, mapping=mapping, quote=quote, pdf_name=pdf_name):
            def test(self):
                self._assert_pdf(state, transform, det, mapping, quote, pdf_name)
            test.__name__ = f"test_banner_tuple_{pdf_name.replace('.', '_').replace('-', '_')}"
            return test
        t = _make()
        setattr(BannerTupleTest, t.__name__, t)


_add_per_pdf_tests()


if __name__ == "__main__":
    unittest.main()
