#!/usr/bin/env bash
# Thin wrapper for the Owl Semaphore PDF build (v1.3.0-rc).
# Equivalent to `make pdfs`; kept for environments without GNU make.
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
cd "$HERE"
python3 generate_pdfs.py "$@"
