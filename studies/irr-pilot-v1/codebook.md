# Owl Semaphore — Rater Codebook (OS-IRR-PILOT-v1)

> **Amendment (2026-07-23, pre-data).** The decision tree and the METACOGNITIVE-vs-CRITICAL
> tie-breaker previously located CRITICAL at the object level, contradicting this codebook's
> own 2×2 table (which places CRITICAL at departs + frame, matching the system algebra:
> CRITICAL = C₂ = σᵥ∘σₕ). The locus axis (Q2) is now defined once — object vs. frame, where
> "frame" covers premises/method/assumptions, one's own or the ones the claim rests on — and
> the tree and tie-breakers follow the table. No data had been collected. Original wording
> is preserved in git history. See PROTOCOL.md Amendment log.

You will read short passages and assign **exactly one** of four states to each: the *kind of
epistemic move* the passage is making. You are NOT judging whether the passage is true, good,
or well-written. You are marking **what sort of thinking it is.**

If a passage genuinely does two things at once, pick the **dominant** move and tick the
**blend** box. Do not leave any passage unrated.

---

## The two questions that decide the state

Ask these in order. They are the system's two independent axes.

**Q1 — Stance toward the prevailing standard:** does the passage *uphold* the accepted
standard/framework, or *push against / depart from* it?

**Q2 — Locus of audit:** is attention on the **object** (the claim/thing being discussed),
or on a **frame** — the premises, method, or evaluative assumptions under which the claim
is judged (one's own frame, or the framework the claim rests on)?

| | Object-level (Q2 = object) | Frame-level (Q2 = frame) |
|---|---|---|
| **Upholds standard (Q1 = preserve)** | **NORMATIVE** | **METACOGNITIVE** |
| **Departs from standard (Q1 = reverse)** | **NON-NORMATIVE** | **CRITICAL** |

Within the frame column, Q1 is what separates the two cells: frame-level attention that
**upholds** the enterprise is self-audit (METACOGNITIVE — typically one's own method,
assumptions, limits); frame-level attention that **reverses** stance is adversarial
inversion of the premises (CRITICAL). This matches the system algebra, where CRITICAL is
the composition of the stance reflection and the locus reflection (C₂ = σᵥ∘σₕ).

---

## State definitions (operational)

### NORMATIVE — "This is the standard."
Asserts, applies, or relies on an accepted/validated standard, method, or established result,
*within* the accepted frame. Reports settled procedure or consensus.
- Cues: "as established," "per the standard," "it is well known," states a method as given.
- Test: Could this sit unremarked in a textbook or a spec? → NORMATIVE.

### NON-NORMATIVE — "This reflects the standard."
A *legitimate alternative or exploratory* reading that diverges from the accepted view but
stays inside the same framework and standards of rigor. Disagreement *within* the system;
unfinished exploration. NOT a rejection of the framework itself.
- Cues: "an alternative interpretation," "we instead propose," "one might also explore,"
  a hypothesis offered against current consensus but by accepted methods.
- Test: Does it offer a *different path* using the *same rules*? → NON-NORMATIVE.

### CRITICAL — "This inverts the standard."
Adversarial inversion: attacks, falsifies, stress-tests, or red-teams the *premises/framework*
themselves. Assumes the worst case; tries to break the thing. Inverts both the object claim
AND the assumptions behind it, while staying structured (not mere emotional dismissal).
- Cues: "this fails because," "suppose the assumption is false," "counterexample,"
  "attack surface," "what if the entire approach is wrong."
- Test: Is it trying to *demolish or invert* the claim/framework? → CRITICAL.

### METACOGNITIVE — "The observer audits the frame."
Turns attention onto the *evaluator's own* reasoning, method, or limits — thinking about the
thinking. Examines whether the frame/measure itself is adequate, names one's own assumptions,
biases, or scope. Upholds the enterprise but audits *how we are judging*.
- Cues: "our method may be limited by," "we assumed X, which could bias," "a limitation of
  this analysis," "reflecting on how we evaluated this," "the framework itself may not capture."
- Test: Is the passage examining *its own evaluative lens* rather than the object? → METACOGNITIVE.

---

## Decision tree (use when unsure)

1. Is the passage's attention on a **frame** — premises, method, or evaluative assumptions
   (its own or the ones the claim rests on) — rather than on the object-level claim itself?
   If NO → go to step 3.
2. Frame-level. Is the move **adversarial** — attacking, inverting, or trying to break the
   premises/framework? → **CRITICAL**. Or **upholding** — auditing its own method,
   assumptions, or limits to bound or strengthen the enterprise? → **METACOGNITIVE**. Stop.
3. Object-level. Is it **departing from / offering an alternative to** the accepted view, but
   by accepted methods? → **NON-NORMATIVE**. Stop.
4. Otherwise (it asserts/applies the accepted standard) → **NORMATIVE**.

## Tie-breakers (predeclared, to keep raters consistent)

- **CRITICAL vs NON-NORMATIVE:** does it want to *replace within the system* (NON-NORMATIVE)
  or *break/invert the system* (CRITICAL)? Intent to demolish → CRITICAL.
- **METACOGNITIVE vs CRITICAL:** both are frame-level; **stance** separates them. Auditing a
  frame to *bound or strengthen* it (typically one's own method or limits) → **METACOGNITIVE**.
  Attacking a frame to *break or invert* it (typically the premises the claim rests on)
  → **CRITICAL**.
- **NORMATIVE vs METACOGNITIVE:** plain assertion of standard (NORM) vs commentary on the
  adequacy of one's own method (META).

## Micro-examples (calibration flavor — NOT in the test corpus)

- "We follow the WCAG 2.2 AA success criteria for contrast." → **NORMATIVE**
- "Rather than the standard fixation model, we explore a saccade-driven account." → **NON-NORMATIVE**
- "If the independence assumption is dropped, the proof collapses entirely." → **CRITICAL**
- "A limitation: our coding scheme may itself bias which passages we noticed." → **METACOGNITIVE**
