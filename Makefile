# Owl Semaphore — release reproducibility targets
#
# Single-command regeneration of all publication-grade PDFs for v1.3.0-rc.
# Per OWL-SEMAPHORE-EXPLANATION.md §3, reproducibility is a hard requirement
# for the data-scientist / serious-operator / hacker archetypes: no hidden
# hand-built artefacts.
#
# Targets:
#   make pdfs        regenerate every PDF from its Markdown source
#   make hashes      recompute SHA-3-512 over release-relevant files
#   make verify      banner-tuple + PDF metadata + canonical-wording checks
#   make test        pytest (== verify, run through pytest)
#   make clean       remove generated PDFs and intermediate .typ files
#   make all         pdfs + hashes + verify
#   make help        list targets

PYTHON ?= python3

PDFS = OWL-SEMAPHORE-SYSTEM.pdf \
       OWL-1-NORMATIVE.pdf \
       OWL-2-NON-NORMATIVE.pdf \
       OWL-3-CRITICAL.pdf \
       OWL-4-METACOGNITIVE.pdf \
       OWL-SEMAPHORE-EXPLANATION.pdf

.PHONY: all pdfs hashes verify test clean help

help:
	@echo "Owl Semaphore — Make targets"
	@echo "  make pdfs     regenerate every PDF from Markdown"
	@echo "  make hashes   recompute SHA-3-512 hashes (RELEASE-HASHES.txt + manifest)"
	@echo "  make verify   banner-tuple + PDF metadata + canonical-wording checks"
	@echo "  make test     pytest wrapper around verify"
	@echo "  make clean    remove generated PDFs and intermediate .typ files"
	@echo "  make all      pdfs + hashes + verify"

all: pdfs hashes verify

pdfs:
	$(PYTHON) generate_pdfs.py

hashes:
	$(PYTHON) scripts/compute_hashes.py

verify:
	$(PYTHON) scripts/verify_banner_tuple.py
	$(PYTHON) scripts/check_pdf_metadata.py

test:
	$(PYTHON) -m pytest tests/ -v

clean:
	rm -f $(PDFS)
	rm -f *.typ
