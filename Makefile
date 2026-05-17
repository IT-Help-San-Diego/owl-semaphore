# Owl Semaphore — Makefile (v2.0.0-rc)
#
# Single entry point for regenerating PDFs and TIFFs, recomputing hashes,
# rewriting the integrity manifest section that depends on those hashes, and
# running tests.
#
# Targets:
#   make pdfs        regenerate all six PDFs from the .md sources (v2 assets)
#   make tiffs       assemble v2 multi-page master TIFFs from v2 PNGs
#   make hashes      recompute SHA-3-512 hashes for release assets + PDFs
#   make manifest    rewrite generated integrity-manifest blocks from hashes
#   make test        run banner-tuple PDF integrity test + v2 asset doctrine tests
#   make all         tiffs -> pdfs -> hashes -> manifest -> test
#   make clean       remove .typ intermediates and __pycache__

PYTHON ?= python3
REPO   := $(CURDIR)

.PHONY: all owl3-b-balanced owl4-meta-master badges pdfs tiffs hashes manifest test clean help

help:
	@echo "Owl Semaphore — make targets (v2.0.0-rc):"
	@echo "  make owl3-b-balanced  build OWL-3 CRITICAL B-geometry + B alert red balanced master + layer proof"
	@echo "  make owl4-meta-master build OWL-4 METACOGNITIVE sigma_h + purple master + layer proof"
	@echo "  make badges           build v2 final composed badges (1080/540) + contact sheet"
	@echo "  make pdfs             regenerate all six PDFs (v2 asset set)"
	@echo "  make tiffs            assemble v2 multi-page master TIFFs"
	@echo "  make hashes           recompute SHA-3-512 hashes -> RELEASE-HASHES.txt"
	@echo "  make manifest         rewrite integrity-manifest sections from hashes"
	@echo "  make test             run banner-tuple PDF integrity test + v2 asset doctrine tests"
	@echo "  make all              owl3-b-balanced -> owl4-meta-master -> badges -> tiffs -> pdfs -> hashes -> manifest -> test"
	@echo "  make clean            remove generated intermediates"

all: owl3-b-balanced owl4-meta-master badges tiffs pdfs hashes manifest test

owl3-b-balanced:
	$(PYTHON) $(REPO)/scripts/build_owl3_b_balanced_master.py
	$(PYTHON) $(REPO)/scripts/build_owl3_layer_proof.py

owl4-meta-master:
	$(PYTHON) $(REPO)/scripts/build_owl4_metacognitive_master.py
	$(PYTHON) $(REPO)/scripts/build_owl4_layer_proof.py

badges:
	$(PYTHON) $(REPO)/scripts/build_v2_composed_badges.py

pdfs:
	$(PYTHON) $(REPO)/generate_pdfs.py

tiffs:
	$(PYTHON) $(REPO)/scripts/assemble_owl_tiff.py

hashes:
	$(PYTHON) $(REPO)/scripts/compute_hashes.py

manifest:
	$(PYTHON) $(REPO)/scripts/update_manifest.py

test:
	$(PYTHON) -m unittest discover -s $(REPO)/tests -v

clean:
	rm -f $(REPO)/*.typ
	rm -rf $(REPO)/__pycache__ $(REPO)/tests/__pycache__ $(REPO)/scripts/__pycache__
