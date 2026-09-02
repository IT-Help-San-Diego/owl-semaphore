# Visual Rendering Rule — text-native, never diffusion-raster

> Standing guidance for any future work that renders the Owl Semaphore's
> glyphs, formulas, or group structure into an image or poster. Write this
> down now so it is not re-derived (or re-violated) later.

## The rule

**Any surface that carries the Owl Semaphore's text or symbols must be authored
as literal text (HTML/CSS/SVG), never as a raster image produced by a diffusion
model.**

Rationale, measured 2026-08-28:

- A diffusion model (the raster backend behind image generation) **hallucinates
  glyphs**. A correctly-spelled prompt word `MEASURING` was rendered as
  `MEASERING` in the output PNG — a letter drifted as it was painted into pixels.
- The Owl Semaphore's entire visual vocabulary is **exact glyphs that carry
  mathematical meaning**: `σᵥ`, `σₕ`, `C₂`, the Cayley table, `NON-NORMATIVE · σᵥ`,
  `METACOGNITIVE · σₕ`, and the subscripts that distinguish the axes. A diffusion
  model will mangle every subscript and Greek letter into a near-miss. A near-miss
  glyph is *worse* than no glyph, because it looks right while silently changing
  which group element it names.

## The two halves of the discipline

1. **Authoring** — draw glyphs/formulas as text (SVG paths, HTML `<div>` with the
   right font, Unicode + a real typeface). A browser/engine renders the character
   from its definition, so a letter cannot misspell itself. Text is also
   deterministic, diffable, and re-renderable at any resolution.

2. **Verification** — after a human or a deterministic pipeline draws the surface,
   run a **vision model over it as the checker**: "did `σₕ` render, or did the
   subscript fall off / the glyph tofu / the Greek letter drift?" The vision bot's
   job is to *verify* the glyphs, never to *generate* them. This is the same
   external-checker pattern as the rest of the project: the generator and the
   checker are different instruments, and the checker has no ego.

## Consequence for raster images

Diffusion-raster is still fine for **illustrative mood** (an owl emblem, a nebula,
texture) where no glyph carries meaning. It is forbidden for anything where a
mismatched character changes the meaning — which is every place the V₄ algebra,
the σ axes, or the Cayley table appear.

## Where this came from

Carey caught the `MEASERING` typo in a generated "I WANT TO BELIEVE"-style poster
and, separately, a Claude-authored HTML poster (`I Want To Measure Poster.dc.html`)
used literal `<div>` text and therefore could not drift. The contrast is the lesson:
Claude's method (text-native) was the correct medium for meaning-carrying glyphs.
