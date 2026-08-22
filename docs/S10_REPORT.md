# S10 report — the e-value bridge, verification, and the page-budget close

**Session S10, 2026-08-22.** Working folder `~/Desktop/Turnover-Blind`, branch `main`. Wave 0
preflight, three parallel sub-sessions (A/B/C), one serial compression sub-session (D), an
independent verification pass, two mandatory parallel critics (F1/F2), and a patch wave closing
their findings. Eight commits total this session (`5a8019e`, `4aedacf`, `14cefb9`, `39d5914`,
`1fb4cef`, in that causal order — the first two landed in the reverse order their sub-sessions
were assigned, for reasons explained below), none pushed yet.

---

## The paper is within the 4-page body limit

**Yes, exactly.** The body — Introduction, Setup, Section 3 ("the boundary law"), Limitations —
occupies pages 1–4 precisely; `References` is the literal first line of page 5, offset 0. Verified
three independent times this session, by the opened-page method (`pdftotext -f <n> -l <n>
-layout`, never a trusted LaTeX page-total field): once by sub-session D after its final
compression stage, once by the adversarial critic F1 building from a separate scratch copy under
both venue options (`sglblindworkshop` and `dblblindworkshop`), and once more by this report's own
author after the patch wave's fixes. All three agree. Total document length is 10 pages: body
1–4, references 5–7, Code-and-data note + Appendix A measurements 7–9, Appendix B (Table 3) and
Appendix C (Related Work, including the e-value bridge) on page 10. Zero TeX errors, zero
undefined references or citations, zero overfull boxes, both `check_hygiene.sh` and
`check_prose_hygiene.sh` passing at the current commit.

There is no slack: the body is *exactly* 4 pages, not comfortably under it. Anything added now
without an equivalent relocation elsewhere will spill onto page 5.

---

## The e-value bridge paragraph, in full, with its claimed level of connection

> **The accumulator, read as a bet.** A Skeptic who each round pays $\alpha$ for the payoff
> $\mathrm{err}_t$ has cumulative net gain exactly $E_t$, so this paper's accumulator is a
> game-theoretic capital process at unit stake [Shafer & Vovk, 2019; Ramdas et al., 2023]. It is
> not an e-value and not an e-process: it is signed, and Proposition 2 bounds it pathwise by
> feedback rather than under a null by Ville's inequality [Vovk & Wang, 2021]. What is formal is
> the standard transform. Under the null that $\mathrm{err}_t \mid \mathcal{F}_{t-1}$ is
> Bernoulli($\alpha$), $M_t = \prod_{i\le t}(1+\lambda(\mathrm{err}_i-\alpha))$ is a test
> martingale for each $\lambda \in [-1/(1-\alpha),1/\alpha]$, with $\log M_t = \lambda E_t +
> O(\lambda^2 t)$. Section 3's boundary is stated in $|E_T|$ and proved in both directions, so it
> transfers as a dichotomy rather than as a measured rate: inside the window $|E_T| \le c\,h(T)+1$
> and $M_T \to 0$ exponentially at every $\lambda \neq 0$; past it $|E_T|$ is linear in $T$ and
> some fixed $\lambda$ grows $M_T$ exponentially, so an anytime-valid test of the deployed
> intervals' calibration rejects at any fixed level within $O(1)$ rounds. Betting enters online
> conformal inference elsewhere as an optimiser rather than as evidence [Podkopaev et al., 2024].
> We construct no e-value here and claim none.

**Level of connection claimed:** a *structural correspondence that becomes formal only after the
standard exponential transform* — explicitly **not** a claim that $E_t$ is itself an e-value or
e-process. The paragraph states three things and denies a fourth: (1) the capital-process
identity is exact, no probability measure needed; (2) $E_t$ is **explicitly denied** to be an
e-value/e-process, in print, in the paragraph's second sentence, because it is signed and unbound
below with no null attached; (3) under the Bernoulli($\alpha$) null, $E_t$ is the first-order log
of a genuine test martingale, which is the one fully formal fact; and — the reason this is
stateable at all — S9's two-sided proof means the paper's own boundary transfers as a growth-rate
dichotomy (exponential decay vs. exponential growth of $M_T$) rather than a single measured point,
which a pre-S9 version of the paper could not have supported. This paragraph currently lives in
**Appendix C** (relocated there by sub-session D's compression, verified byte-identical apart from
a documentation comment by both D's own diff and the adversarial critic F1's independent
comment-stripped diff), with the intro's roadmap sentence in the body pointing to it: "Appendix C
sets both claims beside four vocabularies for the same movement, and reads $E_t$ as a
game-theoretic capital process." Three new citations were added, all fetched and read in full
(Crossref/Project Euclid metadata, arXiv PDFs read for definitions), plus one existing,
previously-uncited key now cited for contrast.

---

## The numeric audit's outcome

**PASS. The hard escalation rule was never triggered.** Sub-session B traced all thirteen rows of
Table 2 (which turned out to live in `forfeit.tex`, not `appendix.tex` as the preflight's locator
guess had it — B corrected this and recorded the true location), the tangent-integrator excursion
triple (15.10 / 14.8155 / 15.8530), the level-4b excursion (623.70 → 120.60, distinct from the
tangent-integrator's separate 623.70 → 20.10), and the mirror-adversary figures (0.09992–0.09997,
the 10,000/100,000 $\max_t|E_t|$ values) to their exact source in
`results/boundary-stress-20260822T103716Z-cd208b98.json` and the companion `forfeit-*` result
files, with every derived column (printed $\tau^\star$, proved window) independently re-derived by
hand from equation (2) and matched. The adversarial critic F1 then independently re-traced **all
thirteen rows** itself (more than the five its brief required) from the current paper text,
re-deriving the same arithmetic from `src/boundary_stress.py`'s parameters rather than trusting
B's report, and reached the same PASS verdict. Nothing in this session ever required the
escalation-and-stop path.

---

## What moved to the appendices under Sub-session D, and D0's protected list

D0 recorded, verbatim, before any edit: the four-boundary definition (equation 2); the
failure-direction proof sketch over the whole admissible class, unrestricted; the
retention-direction proof sketch keyed to $\Lambda^\pm$ rather than $A^\pm$; the sharp iff on the
five-settings' sub-class plus its symmetric one-line form; both degenerate cases (unbounded
saturator, $\hat q \equiv -b/2$); and the open-band disclosure in Limitations, stated as future
work. **All six items survive verbatim in substance in the main body** — confirmed independently
three times this session: by D's own text-search verification immediately after compressing, by
the adversarial critic F1 reading the compressed paper from scratch and quoting the surviving
text back (including the specific protecting clause "Nothing here asks $\hat q$ to be constant,
asks the extremes to be attained anywhere, or asks $A^\pm_t$ to be finite"), and by this report's
author confirming `git diff 022a945 HEAD -- paper/sections/limitations.tex` is **empty** — the
Limitations section was not reworded at all this session, let alone softened.

What actually moved, across D's seven compression stages plus two further moves in the patch
wave: Section 4 ("Where this sits," now carrying both the e-value bridge and Table 3's relocated
cell content) moved whole to Appendix C; Table 2 (13 rows) moved to Appendix A; Table 1 (the
original eleven-arm table) moved to the head of Appendix A; Figure 2 moved to Appendix A; a
"what survives of the measurement" paragraph and two Table-1-detail sentences moved to Appendix
A's own paragraphs; and, in the patch wave, a $\tau=1.9$ illustration was relocated beside the
Table 2 row it reads and a duplicated mirror-boundary derivation was compressed. Every move was a
**relocation**, never a deletion — sub-session D's own loss audit (rebuilding HEAD from `git
archive` and token-diffing the whole rendered PDF) found exactly one class of removed token: the
eleven mirror-adversary widths, reprinted to the digit in the body when they were already listed
individually in Appendix A — a de-duplication, not a loss, with the underlying claim ($\tau^{\star-}
= 1$, closed on the failing side) kept in the body with a pointer.

**One caveat, found by F1 and closed by the patch wave, not by D:** D's own loss audit measured
the whole document, so it was structurally blind to whether the *body specifically* stayed
self-supporting after a relocation — a body→appendix move is invisible to a whole-PDF diff. It
missed two real problems (detailed below), which the adversarial critic F1 caught and the patch
wave fixed. This is exactly why the plan requires a critic pass after a compression wave, not
just the compressing session's own self-check.

---

## The two problems the compression caused, and how they were closed

**High severity — an abstract/body contradiction.** The abstract states "under the equally legal
$\hat q \equiv +b/2$ the failing band covers." After D's stage-6/7 relocations, the body's only
remaining sentence about that setting read "(2) permits no width at all... the unsmoothed control
included" with no reconciling clause — the sentence explaining *which* adversary that referred to
had moved to the appendix, leaving what reads as a flat contradiction to anyone who only reads the
body. **Fixed**: the sentence in `forfeit.tex` now reads "...permits no width at all *against the
mirror adversary*, the unsmoothed control included, though $\tau = 1.5$ covers there *against the
specified one*" — restoring the reconciliation at a cost of nine words, independently re-verified
against equation (2) ($\tau^{\star+}=2$, $\tau^{\star-}=0$ at that setting) by both the patch wave
and this report.

**High severity — self-containment.** After every relocation, the 4-page body contained zero
data tables and zero data figures — only the Figure 1 schematic — meaning the abstract's own
headline number (miscoverage 1.000000, $|E_T|$ 60,747× Proposition 2's bound at $\tau=1.5$) lived
only past the References, violating this project's own self-containment gate (`docs/GATES.md`
G7.7). **Fixed** by inlining the headline figures as prose at the point the tightness paragraph
already discusses that setting — "$\tau = 0.9$ covers at $0.100012$, $\tau = 1.5$ returns
$1.000000$ with $\max_t|E_t| = 900{,}000$, $60{,}747$ times Proposition 2's bound at $T=10^6$" —
rather than reintroducing a table, which was costed and found to not fit the remaining budget.
The four body lines this cost, plus three medium-severity cross-reference fixes (a now-false
"Table 1 and the paragraph above" pointer, corrected; three missing appendix pointers, added),
were paid for by tightening wording and dropping one contentless signpost sentence — the same
class of move D used throughout, never by touching protected content. The body remeasured at
exactly 4 pages afterward, confirmed independently by this report's own rebuild.

Two lower-severity items were explicitly **not** fixed, with reasons on record in
`research/S10/patch-log.json`: a third missing appendix pointer sits inside the byte-identical,
protected Limitations text and was left alone rather than risk that guarantee; and moving the
e-value content or the whole of "Related Work" back into the body were judged venue/strategy
calls costing roughly 0.6 pages with no budget available without cutting protected content —
flagged, not decided.

---

## The remaining Table 3 and Figure 1 fixes

**Table 3** (the four-vocabularies table, Appendix B): every cell reduced from a full prose
paragraph to one or two lines plus citations; nothing dropped — the elaboration that no longer fit
each cell (the tightness claim, the verification-control detail, the switching-cost trade-off) was
worked into the surrounding Section 4 prose instead, and all seven citation keys preserved.

**Figure 1** (the readout-placement schematic): edge labels, panel titles, and two inline
sub-labels were found below the venue style file's 8pt floor (at 7pt) and bumped to
`\footnotesize`, verified by rendering the compiled page to PNG before and after, not by assuming
the source font size was sufficient; a legend swatch was added distinguishing the grey readout
element in the figure itself, not only in the caption; and the caption was confirmed
description-only (it already was). Figures 2 and 3's captions were independently swept and found
already description-only and already unambiguous about $\tau^\star$ (a failure boundary) versus
$\sigma$ (a retention boundary) — no changes were needed there, and none were made for their own
sake.

---

## Is S9's mathematical result still fully and honestly represented?

**Yes, plainly and without hedging — but only because the adversarial critic caught what the
compressing session's own self-check could not, and the patch wave then closed it.** The
compression itself never touched a single line of the protected mathematical content: the
four-boundary definition, both complete proof directions, both degenerate cases, and the
Limitations open-band disclosure are byte-identical or textually unchanged from before this
session's compression began, confirmed by diff, not by trusting any sub-session's self-report. The
compression *did* cause two real, if narrow, defects — an apparent internal contradiction and a
self-containment gap — as a side effect of moving supporting material for page budget. Both were
found by a critic specifically tasked with re-deriving the mathematics rather than trusting prior
reports, and both are now closed, verified independently a third time by this report. Nothing
about S9's open band was reopened, re-attempted, or softened: it reads today exactly as S9 left
it.

---

## Process note: the one commit-attribution wrinkle

Sub-sessions A and C ran concurrently in the same working directory (not git-worktree-isolated)
and both edited `paper/sections/related.tex`. As a result, C's commit (`4aedacf`) ended up
carrying A's e-value paragraph as well as its own changes — its message doesn't mention this — and
A's own commit (`5a8019e`) ended up containing only its `.bib` additions, since `related.tex` was
already staged by C by the time A committed. This was caught and self-reported by A immediately,
confirmed independently by this report's author before F2 ran, and confirmed a third time by F2's
own instruction-compliance check: no content was lost or duplicated (`related.tex` at HEAD has
the paragraph exactly once, and the paper compiles and reads correctly), only the commit
boundary is misattributed. It was not corrected by rewriting history, since both commits are
factually accurate about what changed in the tree even if one's message undersells its own diff.
Future waves that mutate overlapping files concurrently should use worktree isolation or run
serially instead — noted for any following session.

---

Committed (`5a8019e`, `4aedacf`, `14cefb9`, `39d5914`, `1fb4cef`, plus this report) and pushed, per
this session's own closing instruction. Venue, affiliation, and author identity were not touched
by any sub-session this session; verified by diff against `022a945` (this session's starting
point) as part of the instruction critic's own check.

**7 days remain before the E-values submission deadline** (2026-08-29 AoE, as of this session's
date, 2026-08-22).
