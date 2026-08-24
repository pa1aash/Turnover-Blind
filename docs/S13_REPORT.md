# S13 report — remaining review fixes, and the page-count compression that didn't arrive

**Session S13, 2026-08-24.** Working folder `~/Desktop/Turnover-Blind`, branch `main`. Wave 0
preflight, three parallel sub-sessions (A/B/C), one serial merge-and-fallback sub-session (D),
one serial package rebuild (E), two mandatory parallel critics (F1/F2), and a patch wave (F)
closing their findings. Eight commits this session (`1ddc357` through `214f99e`), not yet
pushed as of this report.

---

## The single most important fact: the body does not fit, and neither path closed it

**No.** The body still overflows E-values' 4-page limit. `4 Limitations` (18 rendered lines)
still spills whole from page 4 onto page 5, exactly as it did when this session started.

Neither authorized path closed the gap:

- **Byproduct compression (sub-sessions A, B, C) closed nothing.** Its net effect on the body
  page-4/5 boundary, measured directly by rebuilding and reading pages 4 and 5, is **zero**.
  Sub-session B's caption/table work (-2 typeset lines) and sub-session C's bibliography work
  (+4 lines) both landed entirely in appendix and reference material, which E-values excludes
  from the 4-page count. Sub-session A's prose fixes, once corrected for a mid-session
  regression (below), were net-neutral in the body.
- **The single authorized fallback (sub-session D, trimming the Introduction's prior-art
  paragraph) saved exactly 1 typeset line**, and that line did not move any part of Limitations
  onto page 4 — it was absorbed by page-break granularity. The paragraph is only 7 typeset lines
  total and cannot supply anything close to what's needed while preserving every citation, which
  this session was required to do.

**The exact remaining shortfall, measured precisely by the adversarial critic (F1) via a binary
search on inserted vertical space:** **202pt of body vertical space — approximately 19
typeset-line-equivalents at this document's 10.95pt baseline**, not simply "18 lines" (Limitations'
own line count understates the true requirement, because its section heading costs more vertical
space than one text line). This is also a cliff, not a ramp: any trim short of the full 202pt
leaves Limitations *split* across pages 4 and 5, which is strictly worse than the current clean
break. There is no partial credit available here.

**This is now an operator decision.** Two paths forward, neither decided by this session:
finding roughly 202pt of further authorized cuts elsewhere in the body (a scope this session was
not given), or switching to TS-LIMITS, which allows 4-7 body pages and comfortably fits the
paper's current length as-is. The venue switch itself is a two-line change in `paper/main.tex`
(swap which `\usepackage` line is active, and `\workshoptitle`) already documented there as
`[OPERATOR INPUT]` — untouched by this session.

---

## A mid-session regression, caught and corrected before it became the fallback trigger

Sub-session A's agent stalled (harness watchdog) partway through its work, after sub-session C
ran `git stash` on the shared working tree while A and B were both still editing it — sweeping
up their uncommitted edits. The orchestrator recovered A's work from the two resulting stashes
(both diffed against clean HEAD, confirmed disjoint, reassembled; both stashes left intact and
undropped for audit — `git stash list` still shows 2 entries).

The first rebuild of that recovered state showed the page boundary had gotten **worse**, not
better: Section 3 itself spilled 2 extra lines onto page 5, on top of Limitations' 18, because
several of A's stall-recovered edits were net word-*additions* to body text — violating A's own
brief, which required every fix to be net-neutral-or-shorter, but which A never got to enforce
before it stalled. Before treating the byproduct as exhausted, sub-session D completed that
tightening pass itself (reverting an inaccurate caption addition, shortening two wordy phrasings)
and re-measured: this restored the exact pre-session baseline. Only then did D conclude the
byproduct alone hadn't closed the gap and proceed to the authorized fallback.

The adversarial critic (F1) later found that this tightening pass had itself introduced two
attribution errors — see the patch wave below. Both were caught and fixed before this report.

---

## Every fix from A, B, C — with before/after

### A — prose precision (`research/S13/A-prose-precision.json`)

| Item | Before | After (final, post-patch) |
|---|---|---|
| Abstract, readout antecedent | "placement and derivation are conceded by name" | "the readout's placement and the corollary's derivation are conceded by name" |
| Abstract, dead-band label | "A legal $L_1$ dead band" | "A legal dead band" (label dropped to avoid the forward reference, per A1's own shortest-fix instruction) |
| Abstract, aphorism | "Coverage goes, not only the rate." | "coverage fails outright, not merely its rate" |
| Intro, refutation/condition antecedents | "Where that refutation stops, the condition is tight." | "Where Corollary~2 stops, its radius condition is tight." |
| Intro, matching aphorism | "Past it coverage goes, not only the rate" | "Past it coverage fails outright, not merely its rate" |
| forfeit.tex, realised-supremum antecedent | "its realised supremum" | "the deployed value's realised supremum" |
| forfeit.tex, τ⋆− attribution | "And $\tau^{\star-}$ was missing entirely." | "And that printed rule omits $\tau^{\star-}$ entirely." |
| forfeit.tex, failure-criterion inference | conclusion stated before its evidence | evidence now precedes "so the failure criterion is..." |
| forfeit.tex, Table 1 caption | (attempted "primary regime (§setup's harness)" pointer) | reverted — the pointer was factually imprecise (setup.tex doesn't define "primary regime"; only Appendix A does) and cost body space for no real gain |

Three of the review's named aphorisms ("What is tight is the radius, not a form"; "And τ⋆− was
missing entirely"; "The edge is a theorem") were searched for against current text. The first two
were found and fixed (the first lived in `setup.tex`, outside where the session's own preflight
had looked, and A found it on a second pass — now "So the tight quantity is the radius, not
either form."). The third was not found verbatim or as an evident paraphrase anywhere in current
text; most likely already resolved in an earlier session under different wording. A4's "un-named
refereed paper" framing was confirmed absent from current text (zero grep hits for "un-named");
its trigger condition doesn't apply here.

**Net line delta on the body page-4/5 boundary: zero**, after the tightening pass described
above.

### B — caption and table compression (`research/S13/B-captions-tables.json`)

- **Table 4 (the four-vocabularies table, `tab:bridge`) — deleted**, flagged in the *original*
  adversarial review before session S8 and never fixed until now. Its content (all seven
  citations, all ten named works across four vocabularies) folded into a description-only
  paragraph in the same location. `setup.tex`'s count-based cross-reference and a live pointer in
  `related.tex` both repointed at the new location rather than left dangling.
- **Figure 1's caption** — a genuine, twice-flagged contradiction (S10, and the review before
  S12) between panel A's unconditional "the deployed sequence leaves that set" and the paper's
  own text ("the forfeit is a property of the smoothing strength, not Placement A") was fixed:
  now reads "nothing keeps the deployed sequence inside that set" — the true asymmetric fact,
  not the false unconditional one. Node-label legibility (≥8pt at compiled size) was checked by
  three independent methods and found already satisfied; no change needed.
- **Table 2 and Figures 2/3's captions** — confirmed already description-only from a prior S6
  rewrite; no manufactured edits.

**Net line delta: -2 typeset lines, entirely inside Appendix material** (excluded from the
4-page body count).

### C — reference completion and correction (`research/S13/C-references.json`, reconstructed —
see note below)

- **`gibbs2024dtaci`** (Gibbs & Candès, DtACI): added JMLR volume 25, number 162, pages 1-36.
- **`podkopaev2024betting`**: the review's claim of ICML 2024 was verified true (PMLR v235, pp.
  40886-40907); converted from an arXiv-only entry. A near-miss on the author name ("Dong Xu" per
  PMLR's own site metadata) was caught and correctly rejected — the camera-ready PDF and arXiv
  record both say "Darren Xu."
- **`dupuy2026relevance`**: the generic series name ("Communications in Computer and Information
  Science") was replaced with the specific proceedings title and CCIS volume 2830.
- **`angelopoulos2021gentle`**: the review's claim of a published Foundations and Trends in
  Machine Learning version was verified true (16(4):494-591, 2023) — a prior session (S8) had
  tried and failed to confirm this by a different search method; converted from arXiv-only.
- **`vaze2026simultaneous`** — **escalation trigger pulled.** The review's claim that this
  citation is a "convenience citation" not supported by its own abstract was checked directly
  against the abstract and found **false**: the abstract explicitly makes close to the exact
  claim it's cited for. A genuine, separate, already-resolved attribution problem with an
  *earlier, unrelated* use of the same citation (documented in `audit/REFS_REJECTED.md`) appears
  to be what the review was actually recalling. No change made; disputed and recorded.
- **C4**: the e-value section's four citations (Shafer & Vovk, Ramdas et al., Vovk & Wang,
  Podkopaev et al.) confirmed already present from S12. Three further candidate citations were
  checked and found already in the bibliography from a prior session but attached to no live,
  unsupported claim in the paper text — not added, to avoid decorative citations.

**Net line delta: +4 lines, entirely in References** (excluded from the 4-page body count).

*(Sub-session C's own JSON report was found unreadable during the critics' wave — 0 disk blocks
allocated against a nominal 13099-byte file size, every read attempt timing out, consistent with
the file having been evicted by an interrupted cloud-sync during this session's own earlier
connectivity failure. Reconstructed from C's completion report, preserved in the orchestrating
session's conversation history, and cross-verified against the adversarial critic's own
independent re-fetch of every claim above.)*

---

## The prior-art paragraph's citation count, before and after D4

**12 before, 12 after — identical multiset, nothing dropped.** Verified twice: once by the
orchestrator during the trim (each of the 12 keys individually grepped and counted), and once
independently by the adversarial critic (F1), who extracted every `\citep`/`\citet` key from the
pre-S13 version (`git show 90629fd:paper/sections/intro.tex`) and the current version and
confirmed an exact match: `angelopoulos2021gentle`, `tunc2013nervousness`,
`godahewa2025stability`, `vanbelle2023deepstability`, `pritularga2024congruence`,
`genov2026switching`, `vanbelle2026stabilizing`, `gneiting2007calibration`,
`pinson2012scenarios`, `worsnop2018scenarios`, `min2026questioning`, `vaze2026simultaneous`.

The trim itself: one sentence was genuinely shortened ("emits a threshold before each observation
and moves it" → "moves a threshold each round," -5 words, no attribution content). A second edit
was reverted during the patch wave after the adversarial critic found it had introduced a real
attribution error (misattributing "priced" to the forecast-verification literature, which the
paper reserves for forecast-stability) for a savings that never helped the page count anyway —
see below.

---

## The patch wave: what the critics found, and what changed

**F1 (adversarial, opus):** no HIGH findings. No protected content was touched, no citation was
dropped, no mathematical content changed, no claim was weakened. Three MEDIUM findings, all
introduced by this session's own editing, all fixed:

1. The abstract's tightened readout/derivation clause had drifted into attributing "derivation"
   to the readout, when the paper's own Appendix C attributes placement to the readout and
   derivation to Corollary 2 specifically. Fixed by restoring "the corollary's."
2. The prior-art paragraph's trim had dropped "Varying" and misattached "priced" to the wrong
   literature. Reverted to the original correct wording — F1 also confirmed this specific edit
   had saved exactly 1 line and moved zero lines of Limitations onto page 4, so nothing was lost
   toward the session's actual goal by reverting it.
3. Sub-session B's table-to-prose fold had merged two citations into one `\citep` cluster,
   causing natbib to attach a `§4.2` locator to the wrong work. Split back into two citations;
   verified the render is now correct.

F1 also independently re-measured the page boundary (confirming the 202pt/~19-line figure above,
more precise than this session's own earlier "18 lines" framing), independently re-verified five
of sub-session C's reference corrections against publisher records (all held), independently
rebuilt the Overleaf package in isolation (0 errors, text-identical to `paper/main.pdf`), and
confirmed every one of A's other prose fixes correctly disambiguates or explicitizes without
narrowing or strengthening any claim. Two LOW findings were fixed (a Candès middle-initial
inconsistency; a heading/paragraph wording repeat in Appendix B); two were left as-is with reasons
recorded (a source-formatting nit with zero rendered effect; a dropped `$L_1$` abstract label F1
itself judged defensible).

**F2 (instruction, sonnet):** full compliance across all six checklist items — one commit per
sub-session (including a transparently-documented recovery commit for A), frozen fields
untouched, the venue question left undecided, sub-session D's escalation logic correctly followed
(byproduct measured first, fallback applied only after, scope limited to the named paragraph,
honest reporting of the unclosed gap), no gate recorded as signed. One process note, not a
defect: D's tightening pass over A's recovered edits is real prose editing beyond pure
measurement, but a defensible reading of "resolve any overlap" and of completing A's own
interrupted net-neutral mandate rather than a second discretionary fallback — recorded here for
transparency rather than treated as a violation.

---

## The package's final state

`build/overleaf-package/` was stale going into this session — predating roughly sessions S8
through S13's worth of content (its `main.tex` still carried S5-era float-glue values, and
`sections/related.tex` was hundreds of lines out of sync with the current Appendix C). Rebuilt
fresh from the current repo state, then updated a second time after the patch wave to carry the
same attribution and locator fixes. Isolation-tested twice, in scratch directories with no path
back into the git working tree: **0 TeX errors, 0 undefined references or citations, 0 bibtex
warnings**, both times. Its rendered text is confirmed text-identical to `paper/main.pdf` by
direct diff (and, in F1's independent check, by md5 of the `pdftotext` output). It carries the
same unresolved page-4/5 gap this report describes — the package is a faithful mirror of the
paper's current state, not a place where the gap was hidden or worked around.

---

## Page budget aside: is the paper now free of every identified defect from both adversarial
reviews?

**Yes, as far as this session's scope reached.** Every item named in this session's brief was
addressed: the definitions-before-use items (A1), the ambiguous antecedents (A2), the aphorisms
(A3, two of three located and fixed, one not found in current text), the abstract's opening
framing (A4, confirmed moot), the four-vocabularies table (B1, deleted after being flagged since
before S8), the Figure 1 caption contradiction (B2, fixed after being flagged twice), the
remaining caption/table items (B3/B4, confirmed already clean), and all four reference items
(C1-C4, including one correctly-disputed review claim). The two critics' own passes surfaced
three further defects — but those were introduced *by this session's own edits*, not carried
over from either adversarial review, and all three were fixed before this report.

**One thing remains, and it is the page count itself** — not a defect in the prose, math, or
references, but the structural fact that the paper, at its current honest length, does not fit
E-values' 4-page ceiling. That is the operator decision named above.

---

## Days remaining before the E-values deadline

**5 days.** Today is 2026-08-24; the E-values deadline is 2026-08-29 23:59 AoE
(`docs/GATES.md`, `docs/OUTSTANDING.md` O20).
