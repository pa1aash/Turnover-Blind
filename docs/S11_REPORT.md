# S11 report — final packaging and final read-through

**Session S11, 2026-08-22.** Working folder `~/Desktop/Turnover-Blind`, branch `main`, remote
`git@github.com:pa1aash/Turnover-Blind.git`. Five sub-sessions (A–E). This session touched no
mathematics, no figures' content, and no claims: it rebuilds the Overleaf submission package
against the current paper and runs one last continuous proofread. Four commits so far this
session (`7042932`, `9f0bb4b`, `f1764b6`, plus this report's own commit), to be pushed at the
close of sub-session E.

---

## Sub-session A — the Overleaf package, rebuilt fresh

`build/overleaf-package/` was deleted and reassembled from the current `paper/`, not patched
from the stale S7 snapshot (which had a real repository URL, an eight-page build, and a
now-outdated section set). The old package directory and its `.zip` are both gone — one commit,
`7042932` — and no second copy was left behind.

The rebuilt package contains `main.tex`, `neurips_2026.sty`, all six `sections/*.tex` files, the
two matplotlib-rendered figure PDFs (`figure1_boundary.pdf` = Figure 2, `figure3_settings.pdf` =
Figure 3 — pre-rendered, since Overleaf will not run `src/make_figure1.py`), a fully resolved
`REFS_VERIFIED.bib`, and a new `PROVENANCE.md` carrying `neurips_2026.sty`'s fetch record (source
URL, retrieval date, SHA-256 of both the archive and the extracted file) so the package needs no
path back to `docs/PROVENANCE.md` to establish where its template file came from. Figure 1 (the
placement schematic) is inline TikZ, not a rendered asset, and needed no figure file at all.

Two path bugs were caught and fixed before the package would even compile: `\bibliography{}`
pointed at `../audit/REFS_VERIFIED`, which does not exist inside the package, and the two
`\includegraphics` calls in `sections/appendix.tex` pointed at `../figures/...`. Both are
artefacts of a subtlety worth recording for a future session — LaTeX resolves a relative path
inside an `\input`'d file against the *master* document's own directory, not the included file's
directory, so a path that is correct in `paper/` (one level below the repo root, where
`figures/` actually lives) is wrong once `main.tex` and `figures/` become siblings inside the
package. Fixed to `REFS_VERIFIED` and `figures/...` respectively, verified by a full local
build before committing.

## Sub-session B — isolated compile, verified genuinely standalone

The package's contents (not the directory itself) were copied to a fresh `/tmp` directory with
no path back to the repository and compiled from there: `pdflatex → bibtex → pdflatex ×3` (four
passes, per the paper's own documented recipe — three leaves a stale `.aux`). Result: **0 TeX
errors, 0 undefined citations or references, 0 bibtex warnings, 0 overfull boxes, 3 underfull
boxes** (pre-existing, in Table 3's p-columns), **0 LaTeX warnings, 0 pdfendlink warnings**.

Page count was read by the opened-page method, not trusted from a field: `pdfinfo` reported 10
pages, and `pdftotext -f <n> -l <n>` on each page individually confirmed the body ends on page 4
with no "References" heading present, and "References" is the first line of content on page 5 —
offset 0. The isolated build's `pdftotext` output is byte-identical to the repository's own
`paper/main.pdf`, and `pdfinfo` metadata matches excluding build timestamps.

Nothing needed fixing, so this sub-session made no commit — the only trackable output is
`research/S11/B-isolation-test.json`, which is gitignored by design (`research/` is this
project's hyperresearch working vault, excluded repo-wide).

## Sub-session C — final continuous proofread

The whole paper was read front to back as one document — `main.tex` plus all six files under
`paper/sections/` — specifically checking the appendix reorganisation S9 and S10 left behind
(Table 1, Table 2, Figure 2, and the "What survives of the measurement" paragraph now live in
Appendix A; Table 3 in Appendix B; "Where this sits," formerly the body's Section 4, is now
Appendix C).

**Cross-references.** Every `\ref`/`\label` pair resolves under compile (0 undefined). Every
printed pointer that names an appendix, table, or figure by number was traced by hand against
what it now actually points to: the Introduction's "Appendix~\ref{sec:related} sets both claims
beside four vocabularies" prints as "Appendix C," which is exactly right; every hardcoded
"Table N" / "Figure N" / "Appendix X" string that survives in *printed* body text turned out to
be a citation locator into a different paper's own appendix or figure (e.g.
`\citet[Appendix~A]{dupuy2026relevance}`), never a stale self-reference — the paper's own
appendix and table numbers are never hardcoded, only reached through `\ref`.

**Placeholders.** No TODO/FIXME/XXX survives anywhere in `paper/`. The only bracketed
placeholders left are the three deliberately frozen `[OPERATOR INPUT]` fields (see below).

**Hygiene.** `tools/check_prose_hygiene.sh` passes clean across the full text: 0 em-dashes, 0
duplicate words, matching an independent check against the compiled PDF's own text.

**Tense and terminology.** Checked for drift across the restructured document: "scorecaster" is
lowercase everywhere; "readout" is one word everywhere, never "read-out"; "dead band" / "dead-band"
follows ordinary English compound-modifier hyphenation (hyphenated only when used as an
attributive adjective before a noun, e.g. "dead-band width"; unhyphenated as a standalone noun,
e.g. "a dead band pulls...") — consistent, not an error.

**Two comment-only fixes**, verified via `pdftotext` diff to change zero characters of printed
output: `main.tex`'s bibliography-provenance comment still quoted the S5 wave 6 count (92
entries, 31 keys cited, 34 bibitems); S10 sub-session A's e-value bridge citations moved that to
96/41/41, recounted and corrected here. And `appendix.tex`'s S10 sub-session D comment misquoted
its own edit to the Table 1 caption ("now reads 'defined in the paragraph below'" when the
caption actually reads "defined in this appendix") — corrected to quote it exactly. Both fixes
were mirrored into `build/overleaf-package/`'s copies. Commit `9f0bb4b`.

## Sub-session D — both critics, mandatory, in parallel

**D1 (adversarial, Opus)** — the last gate before submission — re-derived everything
independently rather than trusting A/B/C's own reports: a fresh isolated compile (same 4-pass
result as B: 0 errors, 0 undefined, 0 bibtex warnings, 0 overfull, 3 underfull), the opened-page
count walked page by page (10 pages, offset 0), and a three-way text-identity check across the
isolated build, a fresh from-scratch repo rebuild, and the committed `paper/main.pdf` — all
byte-identical. D1 re-read the whole paper once more and hand re-derived roughly thirty numeric
quantities against their printed source (e.g. `900,000 / 14.8155 = 60,747`; every row of Table
2's printed $\tau^\star$ and proved window against equation (2)) without finding a transcription
error. Confirmed no gate is recorded as signed (`docs/` untouched by S11 so far) and no frozen
field was touched.

**D2 (instruction, Sonnet)** checked this session's own brief item by item against the actual
repository state — package contents, the deleted S7 package and zip, self-contained `.bib`,
pre-rendered figures, `.sty` provenance, one commit per sub-session that produced a change,
frozen fields, and scope — and returned **full compliance**, no deviations.

**Findings, recorded in `research/S11/patch-log.json`:**

1. **Applied (LOW).** `sections/related.tex`'s S8-era comment said "see its Fig.~2 caption"
   referring to `sections/setup.tex`'s own figure, but that file's only figure (the placement
   schematic) is Figure 1, not Figure 2 — a stale comment sub-session C's own sweep missed.
   Corrected to "Fig.~1" in both `paper/` and the package mirror; comment-only, verified via
   `pdftotext` diff that printed output is unchanged.
2. **Not applied (LOW), recorded with reason.** Two printed pointers into the appendix
   (`sections/setup.tex`: "Table~\ref{tab:bridge}'s caption names ten"; `sections/limitations.tex`:
   "Table~\ref{tab:stress}'s power-of-two rows sit there") use the table as a grammatical
   possessive subject rather than the parenthetical "(App.~\ref{...})" locator style used
   elsewhere. Both are already-established, distinct sentence constructions in this paper —
   inserting a parenthetical between a `\ref` and its possessive `'s` would be a prose restructure
   past this session's no-claims scope, and the PDF is hyperlinked (`hyperref` + `hidelinks`), so
   either `\ref` takes a reader straight to the right appendix on click regardless of whether the
   locator is printed. Left as-is.

No HIGH or MEDIUM findings from either critic. Commit `f1764b6`.

---

## Frozen fields, confirmed unchanged across the whole session

`git diff f7f925a..HEAD -- paper/` (the commit immediately before S11 began) touches only the two
comment corrections listed under sub-session C, plus the one comment correction under D — never
a line of printed content. Current state, unchanged from before S11:

- Venue: `\usepackage[sglblindworkshop]{neurips_2026}` active, `\workshoptitle{E-values: From
  Statistics to ML}`
- Affiliation: `Independent Researcher` (placeholder, per `docs/OPEN_QUESTIONS.md` Q11)
- Author name/email: `Palaash Gang` / `palaashgang@gmail.com`
- Placeholder repository URL: `https://[REPOSITORY LINK - INSERTED BY AUTHOR PRIOR TO
  SUBMISSION]`

No gate in `docs/GATES.md` was touched or recorded as signed by this session; G1.7 (venue) still
stands as an explicit operator decision.

---

## Is the package ready?

**Yes, mechanically.** `build/overleaf-package/` is self-contained (no path to `research/`,
`results/`, `src/`, or `audit/`), compiles cleanly in genuine isolation (verified independently
twice this session, by B and again by D1), and its rendered output is byte-identical to the
repository's own current build: 10 pages total, body exactly 4 pages, References the first
content on page 5, offset 0, 0 TeX errors, 0 undefined references or citations, 0 bibtex
warnings.

**Pending exactly three fields, all deliberately left as operator decisions and none of them
touched by this or any prior session:** the venue (E-values is this project's own recommendation
— see `docs/VENUE.md`'s scoring), the affiliation line, and the real repository URL to replace
the placeholder. `build/overleaf-package/README.md` (written this sub-session, see below) states
where each one is and what changing it costs.

---

Committed (`7042932`, `9f0bb4b`, `f1764b6`, plus this report and the package README) and pushed,
per this session's own closing instruction.

**7 days remain before the E-values submission deadline** (2026-08-29 23:59 AoE, as of this
session's date, 2026-08-22).
