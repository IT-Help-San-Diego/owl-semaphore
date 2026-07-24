# Owl Semaphore — Inter-Rater Reliability Pilot Study (PROTOCOL)

**Study ID:** OS-IRR-PILOT-v1
**Status:** DRAFT — committed to the repository for review; pre-registration not frozen (no data collected).
**Addresses:** Reviewer Gap 2 (Empirical Validation). Target: move the empirical claim
from "design hypothesis" (system spec §12A.2) to a feasibility-grade measurement.

> **Correction (2026-07-23).** The status line above originally read "DRAFT — local-only,
> **not committed, not pushed**. Review before use." That was inaccurate: this file has been
> committed and public since commit `52b2ba8` (2026-06-26). The line is amended rather than
> the file withdrawn — a dated correction preserves provenance better than deletion, and the
> original wording remains in git history. No study data had been collected as of this
> correction, so the pre-registered thresholds and methods (§2, §8) are unchanged and remain
> fixed in advance of data collection.

> **Scope discipline.** This study tests ONE thing: *can independent raters, given only
> the spec and a codebook, assign the same one of the four states to the same passage
> more reliably than chance?* It does **not** test whether the states are "correct,"
> whether the system is useful, or whether it is superior to alternatives. Those are
> separate studies. Keeping this pilot narrow is what makes it achievable and credible.

---

## 1. Research question & hypotheses

**RQ.** When independent raters classify text passages into the four Owl Semaphore states
{NORMATIVE, NON-NORMATIVE, CRITICAL, METACOGNITIVE} using only the published spec plus a
short codebook, is their agreement reliably above chance?

- **H0 (null):** Agreement is no better than chance. Population Fleiss' κ ≤ 0.
- **H1:** Agreement is at least *moderate*. Population Fleiss' κ ≥ 0.41 (Landis & Koch).

This is a **pre-registration draft**: thresholds and methods below are set in advance of
data collection and are **frozen at the moment data collection begins** (§7 step 0 records
the freezing commit hash). No data has been collected as of the latest amendment (see the
Amendment log at the end of this file). (Pre-registration is the verification-principle
move — it prevents choosing the favorable statistic after seeing results.)

## 2. Pre-registered success criteria

A **PASS** (feasibility demonstrated, justifies a larger study) requires BOTH:

1. **Fleiss' κ point estimate ≥ 0.41** (at least "moderate"), AND
2. **lower bound of the 95% bootstrap CI > 0.21** (credibly above chance — the true κ is
   credibly at least "fair"; 0.21 is the Landis & Koch slight/fair boundary).

- κ ≥ 0.61 (substantial) is the **aspirational** result.
- **CONDITIONAL** — either **0.21 ≤ κ point estimate < 0.41**, or **κ ≥ 0.41 with a CI lower
  bound ≤ 0.21**: the codebook needs revision (see §8 confusion analysis) and a re-run, not
  a larger study.
- **FAIL** — **κ point estimate < 0.21**: the state definitions are not operationally
  separable as written. This is an honest, publishable negative result and a direct signal
  to revise §4.2 of the spec.
- **UNDEFINED** — κ is not computable (degenerate marginals, e.g. every rating in a single
  category): inspect the data. An undefined κ is not a FAIL.

The bands partition the outcome space: every computable (κ, CI) result maps to exactly one
verdict, and the mapping is what `analyze_irr.py` implements.

Reviewer 2 explicitly accepted κ = 0.4–0.6 as sufficient for a *pilot* to demonstrate
feasibility — so the bar above is calibrated to the review, not invented.

## 3. Design

- **Fully-crossed (every rater codes every passage).** This lets us use Fleiss' κ cleanly
  and compute a per-passage agreement profile.
- **Forced single-state choice** is the primary task: each rater assigns exactly one of the
  four states to each passage (the "primary epistemic move").
- **Optional blend flag:** a rater may additionally flag a passage as "blended / ambiguous."
  Primary analysis uses the forced choice; a **secondary** analysis excludes any passage
  flagged by ≥ 2 raters, to see how much disagreement is concentrated in genuinely mixed text.
  (This directly answers the reviewers' "edge case handling" concern.)

## 4. Materials (corpus)

- **Size:** 60 passages (above the reviewer-suggested ≥ 50 floor; see §6 for the rationale).
- **Length:** 1–4 sentences each, enough to carry an epistemic move, short enough to rate fast.
- **Provenance — contemporary, not historical** (reviewers rejected Newton/Leonardo as
  illustrations rather than tests). Draw from a mix:
  - peer-review reports / referee comments (rich in NON-NORMATIVE and CRITICAL),
  - methods & limitations sections of recent papers (METACOGNITIVE, NORMATIVE),
  - standards/specs and documentation (NORMATIVE),
  - red-team / security write-ups, adversarial analyses (CRITICAL).
- **Stratification:** the *compiler* (not a rater) targets a roughly balanced design —
  ~15 passages they believe exemplify each state — so the corpus can exercise all four.
  The compiler's labels are the sampling frame **only**; they are NOT a gold standard and
  are never shown to raters. (Using them as "truth" would beg the question.)
- **Source manifest:** every passage stored with source URL/DOI, retrieval date, and a
  SHA-256 of the exact text, in `corpus/manifest.csv`. (Matches the repo's integrity culture.)

## 5. Raters

- **n = 4** independent raters (3 minimum, 5 better). They must not have co-authored the spec.
- **Training/calibration:** each rater (a) reads `OWL-SEMAPHORE-SYSTEM.md` §2–§4 and the
  codebook, then (b) codes a **separate 10-passage calibration set** that *does* have an
  answer key, then (c) reviews the key and one round of discussion to align. Calibration
  passages are NOT in the 60-passage test corpus.
- **Independence:** after calibration, all 60 test passages are coded **alone, in silence,
  no discussion**, presented in a **randomized order per rater** (mitigates order/fatigue
  effects). Raters do not see each other's codes.

## 6. Sample-size rationale

For a nominal κ with 4 categories and 4 raters, 60 items yields a 95% CI half-width on κ of
roughly ±0.12–0.15 under moderate agreement (estimated by the bootstrap in `analyze_irr.py`,
not assumed). That is precise enough to place κ credibly above the chance/slight region
(CI lower bound > 0.21) when true agreement is moderate — which is all a feasibility pilot
must do. It is **not** precise enough to statistically separate "moderate" from "fair"
(that boundary is 0.41, and a moderate point estimate's CI will typically overlap the fair
band). We are not powering for a tight point estimate — we are powering to clear the
κ = 0.21 floor with the CONFIDENCE INTERVAL, not just the point estimate.

## 7. Procedure (run order)

0. **Freeze the pre-registration:** record the commit hash of the final pre-data
   `PROTOCOL.md` + `codebook.md` in `RESULTS.md`. No amendments after this point.
1. Compiler builds corpus + manifest; computes hashes; freezes the file (record its hash).
2. Raters complete calibration; record calibration agreement (sanity check only).
3. Raters code the 60 test passages independently (randomized order).
4. Collect one CSV per rater → merge into `ratings.csv` (schema in §9).
5. Run `analyze_irr.py ratings.csv`. Do not edit data after seeing output.
6. Record results verbatim into `RESULTS.md`, including the confusion matrix.

## 8. Analysis plan (fixed in advance)

- **Primary:** Fleiss' κ across all 4 raters × 60 passages, with a **95% CI from 10,000
  bootstrap resamples over passages.**
- **Robustness:** Krippendorff's α (nominal). Reported alongside; if Fleiss κ and
  Krippendorff α disagree by > 0.1, investigate before interpreting.
- **Per-category κ** (one-vs-rest) for each state — reveals *which* state is unreliable.
- **Confusion matrix** of rater-pair disagreements — reveals *which pairs* of states get
  confused. The prediction worth testing: NON-NORMATIVE↔CRITICAL and NORMATIVE↔METACOGNITIVE
  will confuse most — these are the two pairs that differ **only on the locus-of-audit axis
  (Q2)**, and the prediction is that Q2 is the harder judgment. They should confuse more than
  the stance-adjacent pairs (NORMATIVE↔NON-NORMATIVE, CRITICAL↔METACOGNITIVE, which differ
  only on Q1), and far more than the diagonal pairs (NORMATIVE↔CRITICAL,
  NON-NORMATIVE↔METACOGNITIVE, which differ on both axes).
- **Secondary:** re-run primary κ excluding passages flagged "blended" by ≥ 2 raters.

All computed by the included script — no hand calculation, no spreadsheet.

## 9. Data schema (`ratings.csv`)

```
passage_id,rater_id,state,blend_flag
P001,R1,NORMATIVE,0
P001,R2,METACOGNITIVE,0
P001,R3,NORMATIVE,1
...
```
- `state` ∈ {NORMATIVE, NON-NORMATIVE, CRITICAL, METACOGNITIVE}
- `blend_flag` ∈ {0,1}
- Every (passage_id, rater_id) pair appears exactly once (fully crossed).

## 10. Threats to validity & mitigations

| Threat | Mitigation |
|---|---|
| Raters infer the compiler's intended label from passage choice | Compiler labels never shown; order randomized; sources mixed |
| Order / fatigue effects | Per-rater randomized order; 60 items is ≤ ~45 min |
| One rater anchors others | Strictly independent, silent coding after calibration |
| "Agreement by chance" inflation | κ and α both correct for chance; CI must clear 0.21 |
| Genuinely mixed passages depress κ unfairly | Blend flag + secondary analysis excluding them |
| Investigator degrees of freedom (p-hacking) | Pre-registered thresholds & methods (§2, §8) |

## 11. Reproducibility & data management

- Directory `studies/irr-pilot-v1/` holds: this protocol, `codebook.md`, `analyze_irr.py`,
  `corpus/manifest.csv`, `ratings.csv`, `RESULTS.md`.
- Hash every input (corpus, ratings) with SHA-256; record in `RESULTS.md`.
- `analyze_irr.py` is pure Python stdlib — runs with system `python3`, no installs, so the
  result is reproducible by anyone with the repo.

## 12. Deliverables that satisfy the reviewer

1. This protocol (pre-registration). ✔ produced
2. Working, validated analysis script. ✔ produced (`analyze_irr.py`, tested on synthetic data)
3. A codebook with operational decision rules. ✔ produced (`codebook.md`)
4. After data collection: `RESULTS.md` with κ, α, CI, confusion matrix.

## 13. What a pilot can and cannot show (stated honestly)

A PASS shows the four states are **operationally distinguishable by trained raters** — it
does NOT show they are the *right* four, that they are *useful*, or that they beat a Likert
scale. Those remain future work (the spec already concedes this in §12A.2). A pilot's job is
narrow: prove the categories aren't mush. That is exactly the brick the review says is missing.

---

## Amendment log

All amendments below predate any data collection (none has occurred). Original wording is
preserved in git history; the pre-registration freezes at §7 step 0.

- **2026-07-23 — provenance:** status line corrected (see the note under the header).
- **2026-07-23 — §1/§7:** freeze mechanics made explicit (frozen at data-collection start,
  recorded by commit hash in `RESULTS.md`).
- **2026-07-23 — §2:** verdict bands restated as a true partition. Previously the
  CONDITIONAL clause "or a CI lower bound ≤ 0.21" carried no point-estimate qualifier, so
  every FAIL result also satisfied it, and κ values between the printed band edges (e.g.
  0.205) were unclassified. The restated bands match what `analyze_irr.py` has always
  implemented. An explicit UNDEFINED verdict was added for non-computable κ.
- **2026-07-23 — §2:** the CI-floor gloss "credibly above 'fair'" corrected to "credibly at
  least 'fair'" — 0.21 is the Landis & Koch slight/fair boundary, not the fair/moderate one.
- **2026-07-23 — §6:** precision claim corrected: the design separates at-least-fair from
  slight/chance; it does not statistically separate moderate from fair.
- **2026-07-23 — §8:** confusion-prediction rationale corrected. "Each pair shares one of
  the two binary axes" describes four of the six pairs, not the two named; the named pairs
  are the two that differ only on the locus axis, and the prediction is now stated as
  "locus is the harder judgment," which does single them out.
- **2026-07-23 — codebook:** the decision tree and the METACOGNITIVE-vs-CRITICAL tie-breaker
  previously located CRITICAL at the object level, contradicting the codebook's own 2×2
  table and the system algebra (CRITICAL = C₂ = σᵥ∘σₕ, the composition of the stance and
  locus reflections). The locus axis is now defined once and all instruments agree; see the
  amendment note in `codebook.md`.
