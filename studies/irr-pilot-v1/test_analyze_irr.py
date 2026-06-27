#!/usr/bin/env python3
"""
test_analyze_irr.py — regression tests for analyze_irr.py
Run: python3 test_analyze_irr.py    (exit 0 = all pass)
Pure stdlib; no pytest needed.
"""
import random
import analyze_irr as A

STATES = A.STATES


def synth(n_pass, raters, agree, seed):
    rng = random.Random(seed)
    rows = []
    for i in range(n_pass):
        pid = f"P{i+1:03d}"
        truth = STATES[i % 4]
        for r in raters:
            s = truth if rng.random() < agree else rng.choice(STATES)
            rows.append((pid, r, s, 1 if rng.random() < 0.08 else 0))
    return rows


def approx(a, b, tol=0.06):
    return abs(a - b) <= tol


def main():
    raters = ["R1", "R2", "R3", "R4"]
    fails = []

    # 1. Perfect agreement -> kappa == 1.0
    perfect = [(f"P{i:03d}", r, STATES[i % 4], 0) for i in range(40) for r in raters]
    k = A.fleiss_kappa(A.build_table(perfect))
    if not approx(k, 1.0, 1e-6):
        fails.append(f"perfect agreement: kappa={k}, expected 1.0")

    # 2. Monotonicity: high > moderate > chance
    kh = A.fleiss_kappa(A.build_table(synth(60, raters, 0.90, 1)))
    km = A.fleiss_kappa(A.build_table(synth(60, raters, 0.62, 7)))
    kc = A.fleiss_kappa(A.build_table(synth(60, raters, 0.25, 3)))
    if not (kh > km > kc):
        fails.append(f"monotonicity broken: high={kh:.3f} mod={km:.3f} chance={kc:.3f}")

    # 3. Chance-level kappa near 0
    if not approx(kc, 0.0, 0.12):
        fails.append(f"chance kappa not near 0: {kc:.3f}")

    # 4. kappa and alpha agree within 0.05 (different chance-correction, same data)
    rows = synth(60, raters, 0.62, 7)
    ka = A.krippendorff_alpha_nominal(rows)
    km2 = A.fleiss_kappa(A.build_table(rows))
    if abs(ka - km2) > 0.05:
        fails.append(f"kappa/alpha diverge: kappa={km2:.3f} alpha={ka:.3f}")

    # 5. CRITICAL: bootstrap CI must stay in [-1, 1] (the bug we fixed)
    fk = lambda r: A.fleiss_kappa(A.build_table(r))
    lo, hi = A.bootstrap_ci(rows, fk, B=2000, seed=11)
    if not (-1.0 <= lo <= 1.0 and -1.0 <= hi <= 1.0):
        fails.append(f"bootstrap CI out of bounds: [{lo:.3f}, {hi:.3f}] (kappa must be <= 1)")
    if not (lo <= km2 <= hi):
        fails.append(f"point estimate {km2:.3f} not inside CI [{lo:.3f}, {hi:.3f}]")

    # 6. CI tighter for more passages (sanity: 120 passages narrower than 30)
    lo_s, hi_s = A.bootstrap_ci(synth(30, raters, 0.62, 5), fk, B=2000, seed=2)
    lo_l, hi_l = A.bootstrap_ci(synth(120, raters, 0.62, 5), fk, B=2000, seed=2)
    if (hi_l - lo_l) >= (hi_s - lo_s):
        fails.append("CI did not narrow with more passages")

    if fails:
        print("FAIL:")
        for f in fails:
            print("  -", f)
        raise SystemExit(1)
    print("All regression tests passed.")
    print(f"  perfect kappa=1.0  high={kh:.3f}  moderate={km:.3f}  chance={kc:.3f}")
    print(f"  bootstrap CI in bounds: [{lo:.3f}, {hi:.3f}]")


if __name__ == "__main__":
    main()
