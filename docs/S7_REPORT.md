# S7 report — close the remaining defects, verify once more, package for Overleaf

**Session S7, 2026-08-21.** Working folder `~/Desktop/Turnover-Blind`, branch `main`. Six
sub-sessions (Wave 0 preflight plus A–G), five commits — Wave 0 and sub-session E produced no
trackable change (their artefacts live under gitignored `research/`, and neither critic pass
found anything to patch), so there was nothing to commit at those two points.

---

## Read this first: the repo-URL identity question

**This is not resolved. It is surfaced, in full, as `docs/OPEN_QUESTIONS.md` Q12:**

> **Q12 — The availability statement's repo URL carries your GitHub handle: accept it, or
> change it? (added S7, 2026-08-21)**
>
> **The question.** The availability statement's repo URL contains the operator's GitHub
> handle. It is guarded out of the double-blind build. Confirm this is acceptable for the
> single-blind submission, or provide an alternative (a de-identified mirror, an anonymized
> link service, or removal of the statement).
>
> **The concrete text, as it now reads in `paper/main.tex`** (an unnumbered
> `\section*{Code and data}` after the bibliography, printed only when the active template
> is single-blind):
>
> > The simulator, its frozen configuration, the `results/` files behind every figure and
> > table, the generators that read them, and this project's audit trail across sessions are
> > at `https://github.com/pa1aash/Turnover-Blind`.
>
> **Why this is here rather than decided.** Session S6 introduced this text in a session
> whose own brief froze author identity, and its own report flagged the tension without
> resolving it: new author-identifying text (the handle `pa1aash`), added under an identity
> freeze, guarded correctly out of the anonymous build but not decided as acceptable for the
> one build that does print. Session S7 re-verified the guard independently — a fresh
> `dblblindworkshop` build, checked by decompressing every compressed object stream with
> `qpdf --qdf --object-streams=disable` (not just `strings`, which the object-stream leak
> that S5's critic found would evade) and grepping the result: **0 occurrences** of
> `Palaash`, `pa1aash`, or `github` anywhere in the double-blind build, against **5** in the
> same check run on the single-blind control. `pdfinfo` also reads `Author: Anonymous
> Author(s)` under `dblblindworkshop`. The guard holds. **Whether the handle should print
> at all in the build that does ship is a different question, and it is the operator's, not
> the session's.**
>
> **Answer one of:**
> - (a) The current URL is acceptable for the single-blind submission — keep it as is; or
> - (b) Replace it with a de-identified mirror or anonymized link service — name which; or
> - (c) Remove the availability statement entirely for this submission.
>
> **Why it matters more than it looks.** This is the last remaining piece of author identity
> in the paper that has not been given an explicit operator answer — venue, affiliation, and
> author name/email all already have one (Q3, Q11, and the author block itself). Answering
> this closes that list.

---

## 1. The tau-star forward reference — fixed

Section 2 (`paper/sections/setup.tex`) used `$\tau^{\star}$` with no antecedent; the symbol's
first formal definition sits in Section 3 (`paper/sections/forfeit.tex:250`). Fixed by option
(ii): rewrote Section 2's sentence to use the noun "the radius" — which the very next clause
in the same sentence already relies on ("What is tight is the radius, not a form") — instead
of the symbol, deferring `$\tau^{\star}$` itself entirely to Section 3.

Swept every other named term this paper introduces (Proposition 2, Corollary 2, admissible
radius/set, Placement A/B, the travel functional) for the same use-before-definition defect.
All clean — each is stated or defined at its own first use, most inside the figure caption or
citation sentence that introduces it.

**Page count after the fix: 8 pages, body-end offset 0** (References is the first content on
page 5), verified by the opened-page method (`pdfinfo` for the count, `pdftotext -layout`
per page for content) both before and after the edit — unchanged from S6's baseline. 0 TeX
errors, 0 undefined citations or references.

## 2. The symlog decision — B1, keep the figure, strengthen the caption

S6 disclosed but did not resolve a ×81 magnification of the region near `$\tau^{\star}$` in
Figure 2 panel (b)'s symlog axis, and established the distortion is structural (the eleven
grid widths form a near-geometric ladder in the offset, so any log-like axis spaces them
near-uniformly) — not a tuning failure.

**Chosen: B1**, not B2. Reasoning, stated in the terms the brief asked for: B2 (replace the
panel with a table) would need page budget this document does not have to spare, and would
require re-verifying a new set of numbers' provenance as a table instead of a plotted point —
more surface area to re-check, eight days from the deadline, after S6 already spent a full
sub-session plus two critic passes on this exact panel. The figure's generator
(`src/make_figure1.py`) carries no in-figure textual annotation about the magnification — the
disclosure lives entirely in the caption — so B1 cost one clause, needed no figure rebuild,
and touched nothing S6 had already verified. Added: "visual spacing here is not proportional
to true distance in `$\tau$`" as a direct, unmissable sentence. Page count and offset
unchanged (8 pages, offset 0).

## 3. The critics — nothing to patch

Two independent agents ran in parallel, each with no access to the other's findings or to
this session's own JSON reports, each rebuilding the PDF from clean and re-deriving every
claim itself rather than trusting a written report.

**E1 (adversarial)** confirmed: Section 2's prose is genuinely clean of `$\tau^{\star}$`;
Figure 2's caption is honest about what the generator's symlog axis actually does (its stated
linear zone, `$|\tau-\tau^\star|\le10^{-3}$`, matches `src/make_figure1.py`'s `LINTHRESH`
exactly); the double-blind guard holds (0 hits in an inflated `dblblindworkshop` build, 5 in
the `sglblindworkshop` control); and five randomly spot-checked numbers all traced exactly to
`results/forfeit-20260820T063045Z-83747c45.json`. One nuance was raised and explicitly judged
not a defect: Figure 2 floats to the top of page 3, ahead of the Section 3 header text on
that same page, and its own caption uses `$\tau^{\star}$` — but the caption is self-contained
(it states the formula inline), so no undefined symbol reaches a reader, and this
float-ordering property predates S7 entirely.

**E2 (instruction)** checked all six items from the brief — Q12 surfaced exactly as
specified and not silently resolved; venue/affiliation/author/email untouched; every
sub-session committed separately; the tau-star fix verified by rendered order, not a diff;
B's decision explicitly justified with real reasoning; no frozen-field violation anywhere —
and returned PASS on all six.

**Disposition: no patches applied.** Both critic passes are recorded in full in
`research/S7/patch-log.json`.

## 4. The package

`build/overleaf-package/` — `main.tex`, `neurips_2026.sty` (SHA-256 verified against the
provenance record in `docs/PROVENANCE.md`, byte-identical to the version fetched from the
venue), the six section files (with their two `\includegraphics` paths flattened to a local
`figures/`), both already-generated figure PDFs, and the fully resolved `REFS_VERIFIED.bib`
(path likewise flattened, no dependency on `audit/` by path). No `research/`, `results/`,
`src/`, or audit trail included. `paper/checklist.tex` and `paper/neurips_2026.tex` were also
left out — neither is `\input` by `main.tex`, and `docs/VENUE.md`/`docs/PROVENANCE.md`
already established that the E-values/ML×OR venue requires no checklist, a decision this
session did not reopen.

**Test-compiled in genuine isolation**: copied only the package's contents to an empty `/tmp`
directory with no path back into this repository, then `pdflatex` × 1, `bibtex`, `pdflatex`
× 3. Result: 0 TeX errors, 0 undefined citations or references, 0 bibtex warnings, 2
underfull hboxes (pre-existing, unchanged), 8 pages, offset 0 — and the rendered text is
byte-identical to the repository's own `paper/main.pdf`. No absolute paths anywhere in the
packaged `.tex` sources; every package used (`natbib`, `lineno`, `geometry`, `environ`,
`graphicx`, `tikz` with the `positioning` library only, and the usual `inputenc`/`fontenc`/
`hyperref`/`amsmath` set) is bundled in any standard TeX Live install, so nothing here is
flagged as environment-dependent.

`build/overleaf-package/README.md` exists and states plainly: what's in the package, how to
get it into Overleaf (zip-and-import or a linked git push), and the **three fields still the
operator's to set** — venue confirmation, the affiliation line (`Independent Researcher`,
currently a placeholder), and this session's own repo-URL identity question (Q12) — each
named with its exact current value and what changing it requires. It also gives a short
render-time checklist for the operator's own visual pass, since Overleaf's TeX Live version
can differ subtly from this session's local toolchain even when both compile without error.

`build/overleaf-package.zip` was built and its file list verified to match the assembled
directory exactly: nothing extra, nothing missing.

## 5. Frozen fields — one sentence each

**Venue was not touched.** `docs/OPEN_QUESTIONS.md`'s Q3 content is untouched; only Q12 was
appended at the file's end.

**Affiliation was not touched.** `paper/main.tex` has a byte-for-byte zero diff against the
commit this session started from (`git diff 7b0e091 HEAD -- paper/main.tex` returns nothing),
so `Independent Researcher` is exactly as this session found it.

**Author name and email were not touched.** Same zero-diff check covers `\paperauthor` and
the email line — both untouched.

## Is it ready?

**Yes, with the same three open fields as before, now consolidated in one place.** The two
claims are unchanged, both builds are clean at offset 0, the double-blind variant leaks
nothing (independently re-verified, not assumed), every spot-checked number traces to
`results/`, and the Overleaf package compiles cleanly in genuine isolation. Nothing else needs
attention from this session's own work. Once venue, affiliation, and the repo-URL identity
question are set — the exact three fields `build/overleaf-package/README.md` names — the
package is ready to upload and submit.

**The E-values deadline is 2026-08-29 23:59 AoE. As of this session's date, 2026-08-21, that
is 8 days.**

Nothing was submitted.
