# S17 Report — Final Polish Pass

Date: 2026-08-26. **3 days remain to the E-values deadline as of this session.**

This session touched presentation only: em-dashes, title/abstract precision, caption
compression, diagram cleanup, and a final acceptance-oriented read. It added zero new claims
and removed zero existing claims. The four-boundary theorem, both proof directions, both
degenerate cases, the closed form, and every hedge in Limitations were confirmed intact and
untouched at the end of S16, and remain confirmed intact and untouched at the end of S17 (see
Sub-session G's diff-based check, below).

## Em-dash count: 0, confirmed four independent ways

- `tools/check_prose_hygiene.sh --pdf paper/main.pdf`: **0** in source body (comments
  stripped), **0** in the compiled PDF.
- Raw `grep` for the literal em-dash character (—, U+2014) across `paper/main.tex` and every
  `paper/sections/*.tex`, **including comment lines**: **0** matches.
- A separate Python/Perl UTF-8 codepoint scan of the same files: **0**.
- `pdftotext -layout` piped through a codepoint counter on the freshly rebuilt PDF: **0**
  (en-dashes, U+2013, correctly untouched at 23 — all numeric/page/year ranges).

This was true at Wave 0's baseline (before any S17 edits) and remained true after every
subsequent sub-session's changes, right through Sub-session F's final read.

## Title (final, unchanged from S16)

> Where the Admissible Radius Binds: a Correction and a Measured Boundary in Online Conformal
> Prediction

Sub-session B read this fresh against the full four-boundary result and kept it: "Binds"
locates the claim rather than asserting it, "a Measured Boundary" avoids overselling now that
both directions are proved, and "a Correction" avoids overclaiming while accurately naming
what the paper delivers to the record. The reasoning is recorded in a comment block in
`paper/main.tex` so it is not re-litigated by a future session.

## Abstract (final)

> A printed claim that the scorecaster breaks online conformal coverage meets its refutation
> by overlapping authors; this paper joins them and locates the edge of the set that
> refutation relies on. Conformal PID states long-run coverage for any bounded scorecaster; a
> corollary keeps it for predictable perturbations of the deployed threshold inside an
> admissible radius. The claim was acted on; the readout's placement and the corollary's
> derivation are credited by name. At the null scorecaster and the minimal admissible
> saturator that radius is *tight*. A legal dead band on the *completed* threshold exits that
> set at its radius; past it miscoverage is $1.000000$ against $\alpha = 0.1$: coverage fails
> outright, not merely its rate. The edge belongs to the saturator–scorecaster pair, not the
> readout; elsewhere the condition is sufficient only. Under the equally legal
> $\hat{q} \equiv +b/2$ the failing band covers, as measured; at $\hat{q} \equiv -b/2$ both it
> and partial adjustment at $w = 0.999$ miscover.

Four wording fixes, all made by Sub-session B, zero claims added or removed: "conceded" ->
"credited" (attribution, not admission of fault); a scope-precision fix ("that condition" ->
"that radius", and naming "the minimal admissible saturator" explicitly, since tightness at
the null scorecaster holds only paired with that saturator, not for every admissible
saturator — the same over-read a prior session's adversarial critic once caught in the title
itself); "leaves" -> "exits" (the former idiomatically reads as abandonment); and "covers" ->
"covers, as measured" (the $+b/2$ clause is a measurement against the specified adversary
only, not a proof over the legal class). Still exactly 12 typeset lines, the constraint every
candidate was budgeted against.

## Caption sentence counts (final): all five at or under the three-sentence ceiling

| Figure/Table | Before S17 | After S17 | Description-only |
|---|---|---|---|
| Figure 1 (placement diagram, body) | 3 | 3 (unchanged, already compliant) | yes |
| Table 1 (eleven arms, appendix) | 3 | 3 (unchanged, already compliant) | yes |
| Figure 2 (the cliff + symlog grid, appendix) | 6 | 3 | yes |
| Figure 3 (19 dead-band runs, appendix) | 5 | 3 | yes |
| Table 2 (boundary-stress configurations, appendix) | 5 | 3 | yes |

Every compression preserved content rather than deleting it: Figure 2's symlog-distortion
disclosure and its 0.95/1.05 minor-tick values both survive, re-punctuated into fewer
sentences. The one sentence actually cut (Figure 2's closing mirror-adversary cross-reference)
was not relocated because it duplicates, near-verbatim, a paragraph already in
`sections/forfeit.tex`'s body prose that itself points back at the figure. Sub-session F's
final read caught and fixed one residual grammar defect in Table 2's caption (a dangling
participle left by C's sentence-merge, with the definite article "the rows" having been
dropped in the merge) — a same-length, same-facts, same-hedge wording fix, re-verified against
the page budget immediately after.

## Figure 1 diagram: inspected at 500 DPI, nothing found

Sub-session D rendered the compiled page containing Figure 1 (the two-panel placement
schematic) at 500 DPI and inspected every box, arrow, junction, feedback-loop wire,
indicator-function label, dashed loop boundary, and panel title in both panels for overlap,
text-to-border crowding, and spacing inconsistency. The one asymmetry noticed (Panel A's wider
gap between two boxes) was cross-checked against the TikZ source and confirmed deliberate — it
lets the dashed loop-boundary line pass through cleanly. No edit was made; the finding is "no
regression, nothing to fix," stated explicitly with what was checked, not assumed from a clean
prior report. Figures 2 and 3 (matplotlib-generated, appendix) were inspected the same way for
axis/tick/legend legibility, with no regression found from this project's prior fixes (S6,
S10).

## Final page count (opened-page method)

`pdfinfo paper/main.pdf` → **9 total pages**. Per-page `pdftotext -f N -l N -layout`
extraction confirms page 4 ends mid-body ("...what they rule out. Equation (3) is where the
reach meets the supremum...") and **page 5 opens literally with "References."** The body is
exactly 4 pages with a clean break, unchanged from the S16 baseline and re-verified fresh
after every sub-session in this session, including the final grammar fix in Sub-session F.

## Frozen content: confirmed unchanged, by diff, not by trust

Sub-session G checked this directly against S16's ending commit (`baf3613`) rather than
inheriting any sub-session's self-report:

- `git diff baf3613 HEAD -- paper/sections/forfeit.tex paper/sections/limitations.tex`:
  **empty** — byte-identical. The theorem statement, both proof directions, both degenerate
  cases, the closed form, and every hedge in Limitations are untouched.
- `paper/sections/intro.tex`, `setup.tex`, `related.tex`: also byte-identical to `baf3613`.
- `paper/main.tex`'s only delta is Sub-session B's abstract wording (above) plus its
  provenance comment block; `\papertitle`, `\paperauthor`, the `\if@anonymous` single-blind
  author-block conditional, the `\workshoptitle` macro, and the repository-URL placeholder are
  all outside that diff.
- `paper/sections/appendix.tex`'s only delta is Sub-session C's caption compression plus
  Sub-session F's one wording fix in Table 2's caption — no table data, no figure content, no
  numeric claim was touched.
- `docs/GATES.md` was not edited this session; no gate is recorded as signed (the file's own
  standing prohibition against exactly that was not overridden).

## Sub-session F's verdict on whether the paper presents as finished

Quoting F's own assessment: **"The paper reads as finished, not as triaged."** The argument
runs unbroken from the abstract through the four-boundary theorem, both proof directions, the
closed form and both degenerate edges, into a Limitations section written in the same voice.
F's aphorism sweep (checking specifically for conclusion-asserting sentences without
explanation, a pattern flagged repeatedly across S5, S6, and later sessions) came back empty
across fifteen candidate sentences — each has its explanation adjacent. A small number of
items were flagged as noticed-but-correctly-left-alone: the abstract's "credited by name" reads
slightly cold in isolation but is char-budgeted against a 12-line abstract that was itself just
precision-edited this session; the travel-number sentence in the body doesn't name its two
arms because doing so would add content to frozen text; Figure 1's panel order in the drawing
versus the caption's discussion order was checked and found consistent; and stale
non-rendering `\ref`-adjacent comments (referring to old table/appendix numbering from before a
prior relocation) don't affect anything, since every `\ref` resolves correctly against
`main.aux`.

## Overleaf package: final isolated-build result

`build/overleaf-package/` was rebuilt fresh against the fully merged and finally-read content
(Sub-session E's initial rebuild, refreshed again by Sub-session F after its one wording fix).
Confirmed in sync with `paper/` by direct diff (the only differences are the three expected
relative-path rewrites: two `../figures/` → `figures/`, one `../audit/REFS_VERIFIED` →
`REFS_VERIFIED`). `neurips_2026.sty`'s SHA-256 re-verified against `PROVENANCE.md`'s recorded
hash: exact match, no local modification. Tested in genuine isolation — copied to a directory
entirely outside this git tree, compiled independently (`pdflatex` → `bibtex` → `pdflatex` ×2):
**0 errors, 0 undefined references, 9 pages**, with rendered text confirmed **SHA-256-identical**
to the repository's own freshly rebuilt `paper/main.pdf`.

## Status

This paper is ready for the operator's own final read and submission to E-values, pending
only the affiliation line and the real repository URL, both of which remain the operator's to
set. **3 days remain to the E-values deadline as of 2026-08-26.**
