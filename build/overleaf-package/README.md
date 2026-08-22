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

Nothing below was decided for you. These are the only three places anything in this package
still needs a human decision before it is ready to upload.

1. **Venue confirmation.** `main.tex`'s venue switch (just above the title block) currently has
   `sglblindworkshop` active — the E-values workshop option; `dblblindworkshop`, for the
   anonymised TS-LIMITS option, is commented out on the line directly below it. This project's
   own venue analysis in `docs/VENUE.md` in the main repository recommends **E-values**: it
   scores highest on fit and is the tighter of the two live options (a 4-page ceiling versus
   TS-LIMITS' 4–7), so the paper is written to satisfy the harder constraint either way. If you
   are not submitting to E-values, flip which of the two `\usepackage[...]{neurips_2026}` lines
   is active, and flip the matching `\workshoptitle{...}` line just below it, and rebuild — that
   is the only change the venue switch requires.

2. **The affiliation line.** `main.tex`'s author block currently reads `Independent
   Researcher`, a placeholder that lets the document build, not a decision. See
   `docs/OPEN_QUESTIONS.md` Q11 in the main repository for the exact question and why a longer
   string — one that wraps to two lines — would need the page count re-measured before it can go
   in: this document is at its page ceiling with no slack, so re-run the opened-page method
   after any change here (search the rebuilt PDF for "References" and check which page it lands
   on; do not just trust a page-count field).

3. **The repository URL.** The "Code and data" section near the end of `main.tex` (guarded so it
   only prints under the single-blind option) currently reads
   `https://[REPOSITORY LINK - INSERTED BY AUTHOR PRIOR TO SUBMISSION]` — an explicit,
   unmissable placeholder rather than a real link, by design (`docs/OPEN_QUESTIONS.md` Q12 in
   the main repository). Insert the real repository URL here before submission. It is
   deliberately not wrapped in `\url{}`, since `\url`'s fragile-catcode scanning can choke on
   `[`, `]`, and spaces, and a plain `\texttt{}` placeholder cannot be mistaken for a live (if
   broken) hyperlink if it is ever left in by accident — keep that convention if you edit this
   line by hand.

## The isolated compile result

This package was compiled from a fresh copy in genuine isolation — no path back to the
repository — twice this session, independently, and both runs agree: `pdflatex → bibtex →
pdflatex ×3` (four passes total; the paper's own header explains why three is not enough), **0
TeX errors, 0 undefined citations or references, 0 bibtex warnings, 0 overfull boxes, 3
underfull boxes** (pre-existing, in Table 3's narrow columns), **0 LaTeX warnings, 0 pdfendlink
warnings**.

Page count was read by the opened-page method — `pdfinfo` plus per-page `pdftotext -f <n> -l
<n>`, never a trusted field alone: **10 pages total. Body exactly 4 pages** (Introduction,
Setup, Section 3, Limitations); **References is the first content on page 5**, with the
appendices and the "Code and data" note on pages 7–10. The rendered text is byte-identical to
the repository's own current `paper/main.pdf`.

## The paper is submission-ready

**Pending exactly the three fields above, and nothing else.** No math, no figure content, and no
claim in this paper was touched to build this package — it is the current, verified state of
`paper/`, reassembled into a form Overleaf can build with no external dependency.

## Checklist for your own visual pass once it renders in Overleaf

Overleaf's own TeX Live version can still differ subtly from this local toolchain even when both
compile cleanly, so once it's rendered there:

- [ ] Page count is still 10, and References is still the first content on page 5 (search the
      PDF for "References" and check which page it lands on — do not just trust a page-count
      field, open the page).
- [ ] Figures 2 and 3 render at full text width, not stretched or clipped, and Figure 1 (the
      inline schematic) renders correctly — it is drawn by TikZ at compile time, not a static
      file, so it is the one figure genuinely worth checking Overleaf's TeX Live rendered right.
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
