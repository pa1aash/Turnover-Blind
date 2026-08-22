# S8 report — verify and repair the mechanical and factual layer

**Session S8, 2026-08-22.** Working folder `~/Desktop/Turnover-Blind`, branch `main`. Wave 0
preflight plus five sub-sessions (A–E) plus a critic wave (F), seven commits total
(`4352ad9`, `98fa967`, `d90a1ef`, `943ee0a`, `582dd86` — sub-session A made no code change and
committed nothing, documented below).

---

## 1. The footer/template question — resolved, definitively, after three sessions

S4 flagged it. S6 was assigned it. S7 left it open. **It is not a defect.**

`paper/neurips_2026.sty`'s footer text is gated by `\if@neuripsfinal`, set only by the
separate `final` package option — not by `sglblindworkshop` or any track option. Without
`final`, the `\else` branch prints the generic "Submitted to ... Do not distribute." string
and also hides acknowledgements and turns on `\linenumbers`: this is the standard NeurIPS
submission-vs-camera-ready switch, universal across the NeurIPS-family template, and it is
correct that it is still off. `sglblindworkshop` is doing its actual job correctly (it clears
`\if@anonymous` and wires `\@trackname`/`\workshoptitle`); it was never wired to the footer at
all, so there was nothing to fix. Independently confirmed by the E-values workshop's own
fetched author-kit page (`research/S8/records/e-values-workshop-index.html`), which instructs
only `sglblindworkshop` and says nothing about `final`, and by the S8 adversarial critic's own
independent re-read of the .sty source plus a live re-fetch of the same page. The exact
invocation that *would* produce the workshop-track footer, for the record — `\usepackage[sglblindworkshop,final]{neurips_2026}` — should only be applied once the paper is
accepted; applying it now would prematurely strip the line numbers reviewers use.

## 2. Corollary 2 anchor — version history re-verified from arXiv, restated self-contained

The adversarial review's concern (a suspicious title change across versions, an unconfirmable
Corollary 2 in v3) does **not hold up** against the primary source, verified independently
twice — once by sub-session B, once again by the S8 adversarial critic, from two separate
fetches:

| Version | Date | Title |
|---|---|---|
| v1 | 2025-08-18 | Adaptive Conformal Prediction Intervals Over Trajectory Ensembles |
| v2 | 2026-06-08 | Optimization-based Online Conformal Prediction for Multi-step Forecasting |
| v3 | 2026-08-07 | Optimization-based Online Conformal Prediction for Multi-step Forecasting |

The title change is a real, ordinary revision arXiv itself serves — not evidence of anything
irregular. v3 fetches cleanly (both fetches md5-identical to the `research/S3` copy saved in
an earlier session, confirming that record was faithful) and **does** contain a numbered
"Corollary 2 (CPID admissible set)" whose hypotheses and conclusion match, two phrases
verbatim, what this paper attributes to it. The reviewer's own "could not fetch v3" is most
likely explained by a tooling trap this session hit and recorded: `grep Corollary` on the
saved `.txt` returns nothing because grep classifies the file as binary — `grep -a` is
required.

The bibliography pin (`li2025o2cp`, arXiv:2508.13362v3) is unchanged — it was already correct.
What changed: **the corollary's content is now restated inline**, self-contained, at its first
substantive mention in `paper/sections/intro.tex` — the mechanism (a legal predictable
adjustment keeps the scorecaster inside CPID's own radius, so CPID's bound applies unchanged),
not just a citation to an external, still-revising document. The critic independently verified
this restatement's accuracy against the fetched v3 text and found it correct.

## 3. Four citations checked

| Citation | Status |
|---|---|
| `li2025o2cp` (Corollary 2 anchor) | Already cited; pin verified correct at v3; restatement added |
| `gibbs2021aci` (Gibbs & Candès, ACI) | Bib entry pre-existed but was uncited; **now cited** in Setup beside Conformal PID's recursion |
| `gibbs2024dtaci` (DtACI) | Bib entry pre-existed but was uncited; **now cited** alongside ACI |
| `angelopoulos2021gentle` (conformal-prediction survey) | Did not exist; **created and cited** — arXiv:2107.07511v6, verified via arXiv API, DBLP, and Crossref; cited in the Introduction |

## 4. Seed/determinism contradiction — disambiguated everywhere

The paper described its primary evaluation harness (Table 1, Figure 2, Figure 3) as running
under "one deterministic adversary" while separately mentioning "one seed" a few sentences
later with nothing marking these as two different procedures. Fixed at both ends:
`paper/sections/appendix.tex`'s primary-regime paragraph now states explicitly that harness
"consumes no randomness and needs no seed"; `paper/sections/limitations.tex` now names the
actual seed and sample size for the one place randomness is used at all — the i.i.d.-scores
robustness check, seed **20260820**, $T = 10^6$ — traced to `src/forfeit.py`'s
`Config.seed` and cross-checked against the matching `"seed": 20260820` field and
`0.249376` miscoverage row in `results/forfeit-20260820T063045Z-83747c45.json`. Every other
`seed`/`deterministic`/`stochastic`/`i.i.d.` mention in `paper/sections/*.tex` was checked;
none needed changes.

## 5. Stale-date sentence — fixed

The Introduction's "Four surfaces were queried on 20 August 2026..." sentence has been
rewritten to stand on its methodological merit (what was searched, how thoroughly, the
negative result) without leaning on the calendar date as evidence of currency. The date is
gone from the live text entirely; every citation key and quoted phrase in the passage
survives unchanged.

## 6. Final page count — verified by the opened-page method

**8 pages total. Body ends cleanly on page 4; References begins as the first content on page
5. Zero body-text lines spill.** This was not true at the start of the session — Wave 0's
preflight found the closing sentence of Limitations spilling two lines onto the References
page, a pre-existing defect (present at HEAD before any S8 edit). Sub-sessions C and D's
concurrent edits to the same region left the net spill unchanged (D's compressions recovered
what C's disambiguation text added); sub-session E closed the remaining gap by retightening
C's own seed-disambiguation sentence — trimming detail already stated in `appendix.tex`
without cutting the disambiguation itself — and re-verified the boundary directly via
`pdftotext -layout -f 4/5 -l 4/5`, not by trusting `pdfinfo`'s total. The S8 adversarial critic
independently rebuilt from source and confirmed the same boundary on their own copy, byte-for-
byte matching the committed `paper/main.pdf`.

---

## Critics — findings and disposition

Both critics ran independently in parallel against commit `943ee0a`, per the brief.

**Instruction critic (compliance): FULL COMPLIANCE.** All 10 checked items passed — separate
commits per sub-session (with A's documented zero-commit exception), frozen fields untouched,
Q12 closed via placeholder, all four citations live-cited, seed language consistent, stale
date fixed, page count clean by the opened-page method, no gate recorded as signed, no
question beyond Q12 touched, no R3a/R3b/figures/experiments scope creep.

**Adversarial critic: the mechanical/factual layer is solid.** Every load-bearing technical
claim this session made — the footer gate mechanism, the arXiv version history, the Corollary
2 restatement's mathematical accuracy, the seed's traceability to real code and data, the page
boundary, the URL scrub — survived independent re-derivation from primary sources, not just a
re-read of prior sub-sessions' self-reports. Five findings surfaced, all applied or explicitly
dispositioned in `research/S8/patch-log.json`:

1. **Fixed** — a record-only date misread in `research/S8/A-footer.json` (gitignored, not
   paper-facing): the real E-values submission deadline is **2026-08-29 AoE**, not
   2026-09-29 (that date is notification of acceptance). Corrected in the working record.
2. **Fixed** — `paper/sections/setup.tex`'s new ACI/DtACI clause had two referent problems (a
   locative "where" implying the opposite relationship, and a pronoun — "their iteration (5)"
   — newly ambiguous between Gibbs & Candès and Angelopoulos et al.). Rewritten with an
   explicit "generalizing" relation and an explicit "Angelopoulos et al.'s iteration (5)".
3. **Fixed** — `paper/sections/related.tex`'s own explanatory comment (not the paper's live
   prose) claimed more survived a compression than actually did. Corrected the comment to
   match the live text; the live prose itself was found defensible as-is and left untouched.
4. **Not applied, flagged for a future session** — `docs/GATES.md` G7.7's recorded
   `dblblindworkshop` page-count measurement is stale (records 5 pages/offset 2; a fresh
   build gives 8 pages/offset 0). This predates S8 and is not an S8 regression.
   `docs/GATES.md` is out of scope for this session's brief and carries its own sign-off and
   claim-drift conventions this session was not positioned to touch mid-critic-response.
5. **Not applied, judged not worth the risk** — a minor, critic-flagged-as-defensible
   attribution nuance in the Corollary 2 restatement (a bound stated as the corollary's
   conclusion technically sits in its proof) and a comment-only imprecision about how the
   seed disambiguation is carried across sentences. The critic's own language called both
   "defensible"/"adequate," not defects; reopening either risked introducing a new error for
   no verified gain.

## What was not reached this session

Only the one item above — `docs/GATES.md` G7.7's stale dblblindworkshop measurement. Nothing
else from this session's brief was left incomplete.

---

## Frozen fields and Q12, confirmed

**Venue, affiliation, and author name/email remain completely untouched** — `git diff
fe3a04a..HEAD -- paper/main.tex` touches only the guarded `\section*{Code and data}` block and
the `setup.tex`/`related.tex` prose fixed above; no line matching the author block, venue
option, or affiliation was changed anywhere in this session's seven commits.

**Q12 is closed via an explicit placeholder, not a real link** — the operator will host the
reproducibility package and insert the real URL himself; `paper/main.tex`'s availability
statement now prints `https://[REPOSITORY LINK - INSERTED BY AUTHOR PRIOR TO SUBMISSION]`
(styled in `\texttt{}`, not `\url{}`, so it cannot be mistaken for a live or broken hyperlink
if left in by accident), and `docs/OPEN_QUESTIONS.md` Q12 is recorded resolved with full
reasoning. Verified in the compiled PDF: zero occurrences of the real repository URL, and the
placeholder correctly present.

---

## Verdict: is the mechanical/factual layer clean enough for S9?

**Yes.** Both critics — one hunting independently from primary sources for anything wrong,
one checking compliance item by item against the brief — returned clean verdicts, and the
handful of real findings from the adversarial pass were paper-facing prose bugs (a locative
"where," an ambiguous pronoun, a stale explanatory comment) that are now fixed and re-verified
by a full rebuild: 0 TeX errors, 0 undefined citations/references, 0 bibtex warnings, page
boundary unchanged and clean, both hygiene gates passing. The paper's central anchor citation
is now independently version-verified twice over and self-contained rather than resting on
trust in an external document. S9's proof work has a stable, verified foundation to build
against.

---

Committed and pushed. Nothing was submitted.

**7 days remain before the E-values submission deadline** (2026-08-29 AoE, as of this
session's date, 2026-08-22) — this figure was itself corrected during this session (see
Critics, finding 1): an earlier working note had misread the deadline as 2026-09-29, which is
actually the notification-of-acceptance date, not the submission deadline.
