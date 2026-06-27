#!/usr/bin/env python3
"""
analyze_irr.py — Inter-rater reliability for the Owl Semaphore IRR pilot.

Pure Python standard library. No installs. Run:
    python3 analyze_irr.py ratings.csv

Computes (all pre-registered in PROTOCOL.md §8):
  - Fleiss' kappa (primary), with 95% CI via bootstrap over passages
  - Krippendorff's alpha (nominal) as robustness check
  - Per-category one-vs-rest Fleiss' kappa
  - Pairwise confusion matrix (which states get mixed up)
  - Secondary Fleiss' kappa excluding passages flagged "blend" by >= 2 raters

Input CSV schema (fully crossed: every passage rated by every rater):
    passage_id,rater_id,state,blend_flag

Exit status is informational only; never edits data.
"""
import csv
import sys
import random
from collections import defaultdict, Counter

STATES = ["NORMATIVE", "NON-NORMATIVE", "CRITICAL", "METACOGNITIVE"]
STATE_IDX = {s: i for i, s in enumerate(STATES)}
LANDIS_KOCH = [
    (0.81, "almost perfect"), (0.61, "substantial"), (0.41, "moderate"),
    (0.21, "fair"), (0.0, "slight"), (-1.0, "poor / worse than chance"),
]


def interpret(k):
    for thr, label in LANDIS_KOCH:
        if k >= thr:
            return label
    return "poor"


def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            state = r["state"].strip().upper()
            if state not in STATE_IDX:
                raise ValueError(f"Unknown state {state!r} for {r['passage_id']}/{r['rater_id']}")
            rows.append((r["passage_id"].strip(), r["rater_id"].strip(),
                         state, int(r.get("blend_flag", "0") or 0)))
    return rows


def build_table(rows, passage_subset=None):
    """Return list of per-passage category-count vectors [n_NORM, n_NONNORM, n_CRIT, n_META]."""
    by_passage = defaultdict(Counter)
    for pid, rid, state, _ in rows:
        if passage_subset is not None and pid not in passage_subset:
            continue
        by_passage[pid][state] += 1
    table = []
    for pid in sorted(by_passage):
        counts = [by_passage[pid][s] for s in STATES]
        table.append(counts)
    return table


def fleiss_kappa(table):
    """Fleiss' kappa. table: list of [counts per category] per item. Assumes equal raters/item."""
    N = len(table)
    if N == 0:
        return float("nan")
    n = sum(table[0])  # raters per item (fully crossed => constant)
    if n <= 1:
        return float("nan")
    # P_i: agreement per item
    P = []
    for row in table:
        s = sum(c * c for c in row)
        P.append((s - n) / (n * (n - 1)))
    Pbar = sum(P) / N
    # p_j: marginal proportion per category
    totals = [0] * len(STATES)
    for row in table:
        for j, c in enumerate(row):
            totals[j] += c
    grand = N * n
    pj = [t / grand for t in totals]
    Pe = sum(p * p for p in pj)
    if abs(1 - Pe) < 1e-12:
        return float("nan")
    return (Pbar - Pe) / (1 - Pe)


def fleiss_one_vs_rest(table, cat_idx):
    """Collapse to binary (target category vs all others), then Fleiss' kappa."""
    bin_table = []
    for row in table:
        target = row[cat_idx]
        other = sum(row) - target
        bin_table.append([target, other])
    # reuse fleiss with 2 categories
    N = len(bin_table)
    n = sum(bin_table[0])
    if n <= 1 or N == 0:
        return float("nan")
    P = [((r[0]**2 + r[1]**2) - n) / (n * (n - 1)) for r in bin_table]
    Pbar = sum(P) / N
    grand = N * n
    p0 = sum(r[0] for r in bin_table) / grand
    p1 = 1 - p0
    Pe = p0*p0 + p1*p1
    return float("nan") if abs(1 - Pe) < 1e-12 else (Pbar - Pe) / (1 - Pe)


def krippendorff_alpha_nominal(rows, passage_subset=None):
    """Nominal Krippendorff's alpha via coincidence matrix."""
    by_passage = defaultdict(list)
    for pid, rid, state, _ in rows:
        if passage_subset is not None and pid not in passage_subset:
            continue
        by_passage[pid].append(state)
    # coincidence matrix
    coinc = defaultdict(float)
    n_total = 0.0
    for pid, vals in by_passage.items():
        m = len(vals)
        if m < 2:
            continue
        for a in range(m):
            for b in range(m):
                if a == b:
                    continue
                coinc[(vals[a], vals[b])] += 1.0 / (m - 1)
        n_total += m
    if n_total == 0:
        return float("nan")
    # observed disagreement
    n_c = {s: sum(coinc[(s, t)] for t in STATES) for s in STATES}
    Do = sum(coinc[(c, k)] for c in STATES for k in STATES if c != k)
    De_num = sum(n_c[c] * n_c[k] for c in STATES for k in STATES if c != k)
    if n_total <= 1:
        return float("nan")
    De = De_num / (n_total - 1)
    return float("nan") if De == 0 else 1 - (Do / De)


def bootstrap_ci(rows, stat_fn, B=10000, seed=42):
    """Bootstrap 95% CI by resampling PASSAGES with replacement."""
    rng = random.Random(seed)
    pids = sorted({pid for pid, *_ in rows})
    by_p = defaultdict(list)
    for row in rows:
        by_p[row[0]].append(row)
    ks = []
    for _ in range(B):
        sample_rows = []
        # Each draw gets a UNIQUE synthetic passage id so that drawing the same
        # passage twice yields two SEPARATE rows (preserving the per-item rater
        # count n). Keying by the original id would merge duplicates and inflate
        # n, producing impossible kappa > 1. (See PROTOCOL §8 / regression test.)
        for d in range(len(pids)):
            pid = rng.choice(pids)
            tag = f"__bs{d}__"
            for (opid, rid, state, bf) in by_p[pid]:
                sample_rows.append((tag, rid, state, bf))
        k = stat_fn(sample_rows)
        if k == k:  # not NaN
            ks.append(k)
    ks.sort()
    if not ks:
        return (float("nan"), float("nan"))
    lo = ks[int(0.025 * len(ks))]
    hi = ks[int(0.975 * len(ks)) - 1]
    return (lo, hi)


def confusion(rows, passage_subset=None):
    """Unordered pairwise disagreement counts between states across rater pairs."""
    by_passage = defaultdict(list)
    for pid, rid, state, _ in rows:
        if passage_subset is not None and pid not in passage_subset:
            continue
        by_passage[pid].append(state)
    pair = Counter()
    for vals in by_passage.values():
        m = len(vals)
        for a in range(m):
            for b in range(a + 1, m):
                if vals[a] != vals[b]:
                    key = tuple(sorted((vals[a], vals[b])))
                    pair[key] += 1
    return pair


def main():
    if len(sys.argv) != 2:
        print("usage: python3 analyze_irr.py ratings.csv", file=sys.stderr)
        sys.exit(2)
    rows = load(sys.argv[1])
    pids = sorted({r[0] for r in rows})
    rids = sorted({r[1] for r in rows})
    print("=" * 64)
    print("OWL SEMAPHORE — IRR PILOT ANALYSIS")
    print("=" * 64)
    print(f"passages: {len(pids)}   raters: {len(rids)}   observations: {len(rows)}")

    table = build_table(rows)
    k = fleiss_kappa(table)
    fk = lambda r: fleiss_kappa(build_table(r))
    lo, hi = bootstrap_ci(rows, fk)
    print("\n--- PRIMARY: Fleiss' kappa (all states, all raters) ---")
    print(f"  kappa = {k:.3f}  ({interpret(k)})")
    print(f"  95% bootstrap CI = [{lo:.3f}, {hi:.3f}]  (10,000 resamples over passages)")

    alpha = krippendorff_alpha_nominal(rows)
    print("\n--- ROBUSTNESS: Krippendorff's alpha (nominal) ---")
    print(f"  alpha = {alpha:.3f}")
    if k == k and alpha == alpha and abs(k - alpha) > 0.10:
        print("  ! kappa and alpha differ by > 0.10 — investigate before interpreting")

    print("\n--- PER-CATEGORY: one-vs-rest Fleiss' kappa ---")
    for i, s in enumerate(STATES):
        ck = fleiss_one_vs_rest(table, i)
        print(f"  {s:<16} kappa = {ck:.3f}  ({interpret(ck)})")

    print("\n--- CONFUSION: pairwise disagreements (rater-pair level) ---")
    conf = confusion(rows)
    if conf:
        for (a, b), c in conf.most_common():
            print(f"  {a:<14} <-> {b:<14} : {c}")
    else:
        print("  (no disagreements)")

    # Secondary: drop passages flagged blend by >= 2 raters
    blend = Counter()
    for pid, rid, state, bf in rows:
        if bf:
            blend[pid] += 1
    dropped = {pid for pid, c in blend.items() if c >= 2}
    if dropped:
        keep = {pid for pid in pids if pid not in dropped}
        t2 = build_table(rows, keep)
        k2 = fleiss_kappa(t2)
        kept_rows = [r for r in rows if r[0] in keep]
        # rows already pre-filtered to `keep`; the bootstrap retags ids, so the
        # stat fn must NOT re-filter (it would reject the synthetic ids).
        fk2 = lambda r: fleiss_kappa(build_table(r))
        lo2, hi2 = bootstrap_ci(kept_rows, fk2)
        print("\n--- SECONDARY: excluding {} blended passages ---".format(len(dropped)))
        print(f"  kappa = {k2:.3f}  ({interpret(k2)})   95% CI = [{lo2:.3f}, {hi2:.3f}]")
    else:
        print("\n--- SECONDARY: no passages flagged blend by >= 2 raters ---")

    # Pre-registered verdict
    print("\n" + "=" * 64)
    print("PRE-REGISTERED VERDICT (PROTOCOL.md §2)")
    print("=" * 64)
    if k == k and k >= 0.41 and lo > 0.21:
        print("  PASS — moderate+ agreement, CI clears the 0.21 floor.")
        print("  -> Feasibility demonstrated; justifies a larger study.")
    elif k == k and k >= 0.21:
        print("  CONDITIONAL — fair/moderate but CI does not clear 0.21,")
        print("  or point estimate < 0.41. Revise codebook (see confusion above) and re-run.")
    else:
        print("  FAIL — agreement at/below 'fair'. State definitions are not")
        print("  operationally separable as written. Honest negative result;")
        print("  revise SYSTEM spec §4.2 before any larger study.")
    print("=" * 64)


if __name__ == "__main__":
    main()
