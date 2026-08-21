# Overleaf submission package — Turnover-Blind

This package is a self-contained copy of the paper, "Where the Admissible Radius Binds: a
Correction and a Measured Boundary in Online Conformal Prediction." It has no dependency on
anything outside this directory: no build-time Python, no reference to the rest of the git
repository, no absolute paths.

## What's in it

```
main.tex                 the whole document (preamble, title, \input's the sections below)
neurips_2026.sty         the venue's own template file, used verbatim as fetched
sections/                the six body/appendix .tex files
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

## Three fields that are still yours to set

These are exactly the three items this session's report names as still open. Nothing below
was decided for you.

1. **Venue confirmation.** `main.tex` line 151 currently has `sglblindworkshop` active (the
   E-values workshop option; `dblblindworkshop`, for the anonymised TS-LIMITS option, is
   commented out on the line below it). `docs/OPEN_QUESTIONS.md` Q3 in the main repository has
   the full venue-vs-deadline analysis. If you are not submitting to E-values, flip which of
   the two `\usepackage[...]{neurips_2026}` lines is active and rebuild — that is the only
   change the venue switch requires.

2. **The affiliation line.** `main.tex`'s author block currently reads `Independent
   Researcher`, a placeholder that lets the document build, not a decision. See
   `docs/OPEN_QUESTIONS.md` Q11 for the exact question and why a longer string (one that wraps
   to two lines) would need the page count re-measured before it can go in — this document is
   at its page ceiling with no slack, so re-run the opened-page method after any change here.

3. **The repo-URL identity decision.** The unnumbered "Code and data" section near the end of
   `main.tex` (guarded so it only prints under the single-blind option) currently reads
   `https://github.com/pa1aash/Turnover-Blind` — the operator's own GitHub handle. This was
   surfaced, not decided, in `docs/OPEN_QUESTIONS.md` Q12: accept the URL as is, replace it
   with a de-identified mirror or an anonymized link service, or remove the statement. Whatever
   you choose, this line is the only place it needs to change.

## Checklist for your own visual pass once it renders in Overleaf

This was compiled locally with `pdflatex` + `bibtex`, four `pdflatex` passes, and tested in
full isolation (copied to an empty directory with nothing else present, compiled from there):
0 TeX errors, 0 undefined citations or references, 0 overfull boxes, 2 underfull hboxes
(pre-existing, in a table's ragged-fill column), 0 bibtex warnings, 8 pages total, body exactly
4 pages (References is the first thing on page 5). Overleaf's own TeX Live version can still
differ subtly from this local toolchain even when both compile cleanly, so once it's rendered
there:

- [ ] Page count is still 8, and References is still the first content on page 5 (search the
      PDF for "References" and check which page it lands on — do not just trust a page-count
      field, open the page).
- [ ] Figure 2 and Figure 3 render at full text width, not stretched or clipped.
- [ ] No citation renders as `[?]` or similar (Overleaf's bibtex/biblatex engine choice can
      differ from a local default — this project uses `plainnat` via `natbib`, both standard
      and bundled in every TeX Live install, but confirm the compiler setting is pdfLaTeX, not
      XeLaTeX or LuaLaTeX, since `fontenc`'s `T1` option assumes pdfLaTeX's font handling).
- [ ] Font substitution: `microtype` and the venue's own font choice (loaded automatically by
      `neurips_2026.sty`) can render with very slightly different spacing under a different TeX
      Live release. This will not change the page count in a way that matters, but is worth a
      glance.
- [ ] If you change the venue switch (item 1 above) or the affiliation line (item 2), rebuild
      and re-check the page count and offset before assuming the change is free — this
      document has zero page-budget slack under the active E-values option.
