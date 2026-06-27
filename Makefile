# Owl Semaphore — Makefile (v3.0.0)
#
# Single entry point for regenerating PDFs, recomputing hashes, rewriting the
# integrity manifest section that depends on those hashes, and running tests.
#
# Targets:
#   make sync-assets re-derive assets/ from the canonical gold-masters
#   make pdfs        regenerate all five PDFs from the .md sources
#   make hashes      recompute SHA-3-512 hashes for release assets + PDFs
#   make manifest    rewrite generated integrity-manifest blocks from hashes
#   make test        run integrity tests + study toolkit regression tests
#   make test-studies  run only the IRR study toolkit regression tests
#   make all         pdfs -> hashes -> manifest -> test
#   make clean       remove .typ intermediates and __pycache__

PYTHON ?= python3
REPO   := $(CURDIR)

.PHONY: all sync-assets pdfs hashes manifest test test-studies clean help

help:
	@echo "Owl Semaphore — make targets:"
	@echo "  make sync-assets  re-derive assets/ from canonical gold-masters"
	@echo "  make pdfs         regenerate all five PDFs"
	@echo "  make hashes       recompute SHA-3-512 hashes -> RELEASE-HASHES.txt"
	@echo "  make manifest     rewrite integrity-manifest sections from hashes"
	@echo "  make test         run integrity tests + study toolkit regression tests"
	@echo "  make test-studies run only the IRR study toolkit regression tests"
	@echo "  make all          pdfs -> hashes -> manifest -> test"
	@echo "  make clean        remove generated intermediates"

all: pdfs hashes manifest test

sync-assets:
	$(PYTHON) $(REPO)/scripts/sync_canonical_assets.py

pdfs:
	$(PYTHON) $(REPO)/generate_pdfs.py

hashes:
	$(PYTHON) $(REPO)/scripts/compute_hashes.py

manifest:
	$(PYTHON) $(REPO)/scripts/update_manifest.py

# Canonical test target: repo integrity suite, then study-toolkit regression tests.
# test-studies runs first as a prerequisite so a broken analysis script fails fast.
test: test-studies
	$(PYTHON) -m unittest discover -s $(REPO)/tests -v

# Study toolkit regression tests (pure stdlib; no external deps).
test-studies:
	$(PYTHON) $(REPO)/studies/irr-pilot-v1/test_analyze_irr.py

clean:
	rm -f $(REPO)/*.typ
	rm -rf $(REPO)/__pycache__ $(REPO)/tests/__pycache__ $(REPO)/scripts/__pycache__ $(REPO)/studies/irr-pilot-v1/__pycache__
