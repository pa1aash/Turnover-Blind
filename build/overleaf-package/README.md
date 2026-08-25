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
sections/                the six body/appendix .tex files (S15 sub-session D2 deleted
                          evalue.tex; see "Page count" below)
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

## Venue: TS-LIMITS, double-blind (S15 rebuild)

`main.tex`'s venue switch (just above the title block) currently has `dblblindworkshop` active
— the anonymised TS-LIMITS option — with `sglblindworkshop` (E-values) commented out directly
below it, and `\workshoptitle` set to TS-LIMITS' full verbatim name, "Generalization for Time
Series in Tight Settings: Latency, Inference, Memory, prIvacy and susTainability". This is a
change from the package's earlier state, which shipped with `sglblindworkshop`/E-values active
by default (see git history). S15 wave 0 (`research/S15/A-venue-verification.json`) confirms
TS-LIMITS is the live target: 4–7 pages including everything except references, no appendix
exclusion, deadline 2026-09-05 23:59 AoE. If you are not submitting to TS-LIMITS, flip which of
the two `\usepackage[...]{neurips_2026}` lines is active, flip the matching `\workshoptitle{...}`
line just below it, and rebuild.

## Two fields still yours to set

1. **The affiliation line.** `main.tex`'s author block currently reads `Independent
   Researcher`, a placeholder that lets the document build, not a decision. See
   `docs/OPEN_QUESTIONS.md` Q11 in the main repository. It does not print under
   `dblblindworkshop` (the style file substitutes its own four-line anonymous block), so it
   only matters if you switch to a non-anonymous venue option.

2. **The repository URL.** The "Code and data" section near the end of `main.tex` currently
   reads `https://[REPOSITORY LINK - INSERTED BY AUTHOR PRIOR TO SUBMISSION]` — an explicit,
   unmissable placeholder rather than a real link, by design (`docs/OPEN_QUESTIONS.md` Q12).
   **This section does not print at all under `dblblindworkshop`** (guarded by `\if@anonymous`),
   so it is moot for a TS-LIMITS submission as currently configured; insert the real URL only if
   you switch to a non-anonymous venue option.

## The isolated compile result (S15 sub-session H, 2026-08-25; content resynced by D2)

The `.tex` sources here were resynced by S15 sub-session D2 after its budget-closing cut, so
they match `paper/` exactly apart from the two relative-path rewrites that let this directory
compile standalone (`../audit/REFS_VERIFIED` to `REFS_VERIFIED`, `../figures/` to `figures/`).
D2 RE-RAN THE ISOLATED COMPILE against the post-cut sources, from a temp directory with no path
back to this repository: **9 pages, References p.7 through p.9 = 2.232 pages, counted content
6.768 pages, 0 TeX errors, 0 undefined citations or references, 0 overfull boxes, 0 underfull
boxes, 0 LaTeX warnings, 0 pdfendlink warnings, 0 bibtex warnings**, and the isolated build's
rendered text is byte-identical to `paper/main.pdf`. `/Author` reads `Anonymous Author(s)`, no
XMP block, and a raw byte-grep for the operator's name, email and `github.com` returns zero
matches. The narrative below is sub-session H's original record, kept for its detail.

This package was rebuilt fresh against the merged S15 content (sub-sessions B/C/D/E: venue
switch, identity sweep, body/appendix restructuring, prose de-compression) and compiled from a
fresh copy in genuine isolation — a temp directory with no path back to this repository — as an
independent second check of sub-session B's own identity-leak sweep: `pdflatex → bibtex →
pdflatex ×3` (four passes total; the paper's own header explains why three is not enough), **0
TeX errors, 0 undefined citations or references, 0 bibtex warnings, 0 overfull boxes, 0
underfull boxes, 0 LaTeX warnings, 0 pdfendlink warnings**. The
isolated build's rendered text is byte-identical to the repository's own current `paper/main.pdf`
(verified by extracting and diffing text from every page).

**Metadata check (`python3` + `pypdf`, `pdfinfo` not available on this machine):** `/Author`
reads `Anonymous Author(s)`, `/Title` is the paper title with no author names, `/Producer` and
`/Creator` are plain LaTeX/pdfTeX toolchain strings, no XMP metadata block is present. A raw
byte-grep of the compiled PDF for the operator's name and email returned zero matches. No
identity leak found — consistent with sub-session B's own check.

## Page count: inside the TS-LIMITS ceiling

**9 total pages. References starts on page 7 (36% down the page under `dblblindworkshop`, 28%
under `sglblindworkshop`) and runs through page 9, i.e. occupies 2.232 pages (dbl) / 2.251
pages (sgl). Counted content (everything except the bibliography) is 6.768 pages (dbl) / 6.749
pages (sgl) against TS-LIMITS' 7-page whole-document ceiling.** Both options are inside it.

This closed a 2.77-page gap, and it cost real content. S15 sub-session D2 deleted, on explicit
operator authorisation and on nothing else, (a) Appendix A's five prose paragraphs and (b) the
whole e-value appendix, `sections/evalue.tex`, whose load-bearing sentences and surviving
hedges moved into the body paragraph "The boundary read as a bet." in `sections/forfeit.tex`.
What that cut and what it kept, with the deleted text quoted in full, is
`research/S15/D2-budget-closure.json`. The bibliography lost exactly one entry as a
consequence (41 to 40): `podkopaev2024betting`, cited only in the deleted section.

## The paper is otherwise submission-ready

Pending the page-budget decision above and the two fields under "still yours to set", no math,
no figure content, and no claim in this paper was touched to build this package — it is the
current, verified state of `paper/`, reassembled into a form Overleaf can build with no external
dependency.

## Checklist for your own visual pass once it renders in Overleaf

Overleaf's own TeX Live version can still differ subtly from this local toolchain even when both
compile cleanly, so once it's rendered there:

- [ ] Page count is still 9, and References still starts on page 7 (search the PDF for
      "References" and check which page it lands on — do not just trust a page-count field,
      open the page).
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
- [ ] If you change the venue switch or the affiliation line, rebuild and re-check the page
      count and where References starts before assuming the change is free — this document
      clears its 7-page ceiling by about 0.23 pages, and the last page is nearly full, so a
      single extra line of body text can push it to a tenth page and a whole page over.
