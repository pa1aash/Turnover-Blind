# Overleaf submission package — Turnover-Blind

This package is a self-contained copy of the paper, "Where the Admissible Radius Binds: a
Correction and a Measured Boundary in Online Conformal Prediction." It has no dependency on
anything outside this directory: no build-time Python, no reference to the rest of the git
repository, no absolute paths.

## What's in it

```
main.tex                 the whole document (preamble, title, \input's the sections below)
neurips_2026.sty         the venue's own template file, used verbatim as fetched
PROVENANCE.md            neurips_2026.sty's fetch record (source URL, date, SHA-256)
sections/                the six body/appendix .tex files (evalue.tex was deleted in S15;
                          its surviving content is folded into forfeit.tex and, as of S16,
                          partly relocated to a new appendix section, app:evalue)
checklist.tex            the completed NeurIPS Paper Checklist (S18 sub-session C; required
                          unconditionally by the template regardless of track, per S18
                          sub-session A's primary-source verification -- \input by main.tex
                          after references/appendix, per the template's own placement rule)
figures/                 two already-generated, static PDF figures (no regeneration needed)
REFS_VERIFIED.bib        the fully resolved bibliography
```

Nothing else is included on purpose. `research/`, `results/`, `src/`, and this project's audit
trail stay in the git repository — they are not part of what gets uploaded.

## How to get this into Overleaf

Either works:
- **Zip and import.** Zip the contents of this directory (not the directory itself — the zip's
  top level should contain `main.tex` directly) and use Overleaf's "New Project → Upload
  Project."
- **Push to a linked Overleaf git repo**, if your Overleaf account has that enabled: add the
  Overleaf project's git URL as a remote and push this directory's contents to it.

Overleaf should auto-detect `main.tex` as the main document. If it doesn't, set it explicitly
in the project's menu.

## Venue: E-values, single-blind (S16 rebuild)

`main.tex`'s venue switch (just above the title block) has `sglblindworkshop` active — the
non-anonymous E-values option — with `dblblindworkshop` (TS-LIMITS) commented out directly
below it, and `\workshoptitle` set to "E-values: From Statistics to ML". This reverses S15's
switch to TS-LIMITS/double-blind (see git history: S16 sub-sessions B and E). S16 wave 0
(`research/S16/A-venue-reconfirmation.json`) re-confirmed E-values fresh on 2026-08-26 — a
byte-identical page fetch to S4's 2026-08-20 record: short papers up to 4 pages excluding
references and optional appendices, single-blind, deadline 2026-08-29 23:59 AoE. (The CFP text
itself does not mention a checklist; see the correction directly below -- the template's own
requirement applies regardless.)
If you are not submitting to E-values, flip which of the two `\usepackage[...]{neurips_2026}`
lines is active, flip the matching `\workshoptitle{...}` line just below it, and rebuild.

**Checklist correction (S18 sub-session A, 2026-08-27):** the CFP text itself is silent on
"checklist" one way or the other; earlier sessions read that silence as a waiver. That was
wrong. The template's own `checklist.tex` states unconditionally, with no track-scoping
`\if` anywhere in it, "The papers not including the checklist will be desk rejected," and
`neurips_2026.tex` `\input`s it with no conditional wrapper, in the same master document
shared by all seven tracks. A checklist is required regardless of venue silence, and this
package includes one, completed honestly (`checklist.tex`, S18 sub-session C).

## Two fields still yours to set

1. **The affiliation line.** `main.tex`'s author block currently reads `Independent
   Researcher`, a placeholder that lets the document build, not a decision. See
   `docs/OPEN_QUESTIONS.md` Q11 in the main repository. It prints as-is under
   `sglblindworkshop` (the active option), so it is live now, not merely latent.

2. **The repository URL.** The "Code and data" section near the end of `main.tex` currently
   reads `https://[REPOSITORY LINK - INSERTED BY AUTHOR PRIOR TO SUBMISSION]` — an explicit,
   unmissable placeholder rather than a real link, by design (`docs/OPEN_QUESTIONS.md` Q12).
   **This section prints under `sglblindworkshop`** (guarded by `\if@anonymous`, which is false
   under the active option), so the placeholder is visible in the current build; insert the real
   URL before submission.

## The isolated compile result (S19 Wave 6, 2026-08-27; package rebuilt fresh)

This package was rebuilt fresh, from scratch, against the current content (S19: an exhaustive
16-category prose audit across the whole manuscript, 60 fixes applied to abstract, introduction,
setup, forfeit, limitations, appendix and related-work prose — 2 later surgically reverted for
the page budget, 58 stand) — every stale `sections/*.tex`, `main.tex`, and `checklist.tex` was
deleted/copied fresh from `paper/`, with the same two relative-path rewrites prior sessions
established (`../audit/REFS_VERIFIED` to `REFS_VERIFIED`, and the two `../figures/` in
`sections/appendix.tex` to `figures/`).

**S19 touched presentation only.** No mathematical claim, hypothesis, proof, hedge, or verified
number changed. The four-boundary theorem, both proof directions, the closed form, both
degenerate cases, every Limitations hedge's claim/strength/scope, the S18 checklist content, and
S18's corrected martingale passage were all independently re-verified byte-identical to the
pre-S19 state after every wave. **Two possible substantive (non-prose) issues were surfaced as a
byproduct of the audit and require your own mathematical review before any action** — see
`docs/S19_REPORT.md` for both, stated in full; this package does not attempt to resolve either.

Compiled from a copy in genuine isolation — this package's own directory, with no other reference
to the rest of the repository: `pdflatex → bibtex → pdflatex ×2` (four passes total). **0 TeX
errors, 0 undefined citations or references.** The isolated build's rendered text is
**SHA-256-identical** to the repository's own current `paper/main.pdf` (verified by extracting
text from every page with `pdftotext` and comparing checksums directly, not just a `diff` exit
code).

**Metadata check (`pdfinfo`):** `/Author` reads `Palaash Gang` — correct and expected under the
active `sglblindworkshop` (single-blind) option, which is not an identity leak here the way it
would be under a double-blind option. Page-1 rendered text confirms the visible author block:
"Palaash Gang / Independent Researcher / palaashgang@gmail.com".

## Page count: inside the E-values 4-page body ceiling

**17 total pages. Body is exactly 4 pages** (verified by the opened-page method, not a
page-count estimate: page 4 ends with the closing Limitations-adjacent sentence, page 5 opens
with the literal word "References" as its first line). E-values' call is "Short papers up to 4
pages, excluding references and optional appendices" — the body is what's measured against that
ceiling, and it meets it exactly.

**A real page-budget regression was caught and fixed this session, not silently absorbed.**
Two of S19's applied abstract fixes (both net length additions) pushed 2 lines of pre-existing
body prose onto page 5, ahead of References. Both had been independently flagged by two
different fix sub-sessions during their own isolated checks, not discovered late. Fixed
surgically per this session's own escalation rule: reverted the two responsible fixes one at a
time, rebuilding and re-measuring after each (the first revert alone was insufficient; the
second restored the clean break) — no other fix, in the body or otherwise, was touched. Full
record: `research/checkpoints/S19-K-integration.md`.

## The paper is otherwise submission-ready

Pending the page-budget decision above and the two fields under "still yours to set", no math,
no figure content, and no claim in this paper was touched to build this package — it is the
current, verified state of `paper/`, reassembled into a form Overleaf can build with no external
dependency.

## Checklist for your own visual pass once it renders in Overleaf

Overleaf's own TeX Live version can still differ subtly from this local toolchain even when both
compile cleanly, so once it's rendered there:

- [ ] Page count is still 17, and References still starts on page 5, as the first thing on that
      page (search the PDF for "References" and check which page it lands on and whether
      anything precedes it there — do not just trust a page-count field, open the page).
- [ ] The completed NeurIPS Paper Checklist renders after References/appendices (search for
      "NeurIPS Paper Checklist"), with no `\answerTODO`/`\justificationTODO` red `[TODO]` markers
      left anywhere in it.
- [ ] Figures 2 and 3 (`figure1_boundary.pdf`, `figure3_settings.pdf`) render at full text
      width, not stretched or clipped, and Figure 1 (the inline schematic) renders correctly —
      it is drawn by TikZ at compile time, not a static file, so it is the one figure genuinely
      worth checking Overleaf's TeX Live rendered right.
- [ ] No citation renders as `[?]` or similar (Overleaf's bibtex/biblatex engine choice can
      differ from a local default — this project uses `plainnat` via `natbib`, both standard
      and bundled in every TeX Live install, but confirm the compiler setting is pdfLaTeX, not
      XeLaTeX or LuaLaTeX, since `fontenc`'s `T1` option assumes pdfLaTeX's font handling).
- [ ] Font substitution: `microtype` and the venue's own font choice (loaded automatically by
      `neurips_2026.sty`) can render with very slightly different spacing under a different TeX
      Live release. This will not change the page count in a way that matters, but is worth a
      glance.
- [ ] If you change the venue switch, the affiliation line, or any body prose, rebuild and
      re-check the page count and where References starts before assuming the change is free —
      **the body meets E-values' 4-page ceiling exactly, with zero lines of headroom.** This
      project's repeated experience across sessions is that the page-break mechanism is
      quantised: one extra typeset line of body text does not cost "part of a page", it pushes
      the References heading (and, in earlier states of this document, floats behind it) onto
      an entirely new page. Treat the budget as zero lines of headroom, not a fractional margin.
