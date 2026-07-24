# Owl Semaphore — Inter-Rater Reliability Pilot (`irr-pilot-v1`)

This directory is a **self-contained feasibility study with a pre-registration protocol**
(thresholds set in advance of data collection; the pre-registration freezes at
data-collection start — PROTOCOL §7 step 0), answering the single empirical question the
peer review says is missing:

> *Can independent raters, given only the spec + codebook, assign the same one of the four
> Owl Semaphore states to the same passage more reliably than chance?*

It does **not** claim the states are "correct" or "useful" — only whether they are
*operationally separable*. That narrow scope is what makes it credible and achievable.

## Files

| File | What it is |
|---|---|
| `PROTOCOL.md` | Pre-registered design, success thresholds, analysis plan, validity threats |
| `codebook.md` | Operational decision rules + tie-breakers the raters use |
| `analyze_irr.py` | Analysis: Fleiss' κ (+bootstrap CI), Krippendorff's α, per-state κ, confusion matrix, verdict |
| `test_analyze_irr.py` | Regression tests (perfect=1.0, monotonicity, chance≈0, CI in bounds) |
| `ratings.example.csv` | 5-passage toy input showing the schema |
| `corpus/manifest.csv` | (you create) source provenance + hashes for the 60 real passages |
| `ratings.csv` | (you create) the real merged ratings |
| `RESULTS.md` | (you create after the run) verbatim output + interpretation |

## Quick start (verify it works in 10 seconds)

```bash
cd studies/irr-pilot-v1
python3 test_analyze_irr.py          # all regression tests should pass
python3 analyze_irr.py ratings.example.csv   # see the full output shape
```

## How to actually run the pilot

1. **Build the corpus** (PROTOCOL §4): 60 contemporary passages, ~15 per state, sources
   logged in `corpus/manifest.csv` with URL/DOI + SHA-256. Compiler's intended labels are
   the *sampling frame only* — never shown to raters, never treated as a gold standard.
2. **Recruit ≥ 3 raters** who did not write the spec. Run the 10-passage calibration set
   (separate from the 60), review the key, one discussion round.
3. **Code independently** — silent, no discussion, randomized order per rater.
4. **Merge** each rater's CSV into `ratings.csv` (schema: `passage_id,rater_id,state,blend_flag`).
5. `python3 analyze_irr.py ratings.csv` → paste output verbatim into `RESULTS.md`.
   **Do not edit data after seeing the result.**

## Pre-registered verdict (set in advance; frozen at data-collection start)

| Outcome | Meaning |
|---|---|
| **PASS** | κ ≥ 0.41 AND 95% CI lower bound > 0.21 → feasibility shown; justifies larger study |
| **CONDITIONAL** | 0.21 ≤ κ < 0.41, or κ ≥ 0.41 with CI floor ≤ 0.21 → revise codebook (use confusion matrix), re-run |
| **FAIL** | κ < 0.21 → states not separable as written; honest negative; revise SYSTEM spec §4.2 |
| **UNDEFINED** | κ not computable (degenerate marginals) → inspect data; not a FAIL |

## Validation status of the tooling

`analyze_irr.py` was checked on synthetic data at three known agreement levels before
release. Point estimates land where they should (κ ≈ 0.79 / 0.47 / 0.06 for high/moderate/
chance), Krippendorff's α tracks κ within 0.01, and the confusion matrix correctly counts
pairwise disagreements. Note the synthetic generator draws rater errors **uniformly** over
the four states, so all six state-pairs confuse equally in expectation — synthetic runs
verify the bookkeeping, not the confusability prediction. The pre-registered prediction
(PROTOCOL §8: NON-NORMATIVE↔CRITICAL and NORMATIVE↔METACOGNITIVE confuse most, because they
differ only on the locus axis) can only be tested with real rater data.
A bootstrap-resampling bug (duplicate passages merging and inflating κ above 1) was found
and fixed; `test_analyze_irr.py` guards against its return. The script also enforces the
fully-crossed schema (duplicate or missing ratings fail loudly rather than yielding a
silently wrong κ).

## Scope honesty

A PASS does not validate the *choice* of these four states, nor that they beat a Likert scale
or GRADE — those are separate studies (system spec §12A.2 already says so). This pilot proves
the categories aren't mush. That is the specific brick the review says is missing.
