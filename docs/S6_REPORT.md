# S6 report — figures, captions, the Introduction, and O65

**Session S6, 2026-08-21.** Working folder `~/Desktop/Turnover-Blind`, branch `main`.
Nine sub-sessions, ten commits. Build under `sglblindworkshop` (E-values), the option that
was already active and that this session did not change.

---

## 1. The figure redesign: which option, and why

**Option 1 was taken: the two-figure split.** Figure 2 keeps one setting; a new Figure 3
carries the five-setting comparison and lives in Appendix A.

The axis principle decides it. The five `(r_t, q̂)` settings are a **categorical** variable.
On one continuous pair of axes they can only be told apart by colour and marker, which is
exactly what produced four nested markers on a single coordinate cell. Given a categorical
axis — five rows — they cannot collide at all, by construction rather than by tuning marker
sizes. Option 2 caps a panel at three series, which halves the density but leaves the same
kind of picture.

The null scorecaster is the right single setting for Figure 2 on the paper's own terms: it
is the only one of the five with runs on **both sides** of its own `τ⋆`, so it is the only
one that can show a cliff rather than a one-sided consistency check. Figure 3 goes in
Appendix A because E-values excludes appendices from the 4-page ceiling, so the split costs
the body nothing.

### Two premises in the brief that did not survive measurement

**The brief's diagnosis of panel (a) was wrong.** It says panel (a) plotted τ "with visually
near-equal tick spacing despite the values not being evenly spaced". `make_figure1.py:238`
already set `axA.set_xscale("log")`. Measured: rendered tick positions matched true log
positions to **1.1e-16**, and the gap-by-gap distortion factor was **exactly 1.000 at all
six gaps**. Both adversarial passes independently confirmed this by fitting the axis from
tick bounding boxes to under 0.005 pt. Panel (a) had a density defect, not a scaling one.
The brief's description of panel (a) is an accurate description of **panel (b)**.

**A claim of my own also failed.** A bounding-box test said 16 of 19 markers fell inside the
legend rectangle. A pixel test — legend drawn versus hidden — returned **0 of 19**. The
legend sat in the empty band between the only two attainable miscoverage values. The bbox
reading was abandoned, and what the legend actually occluded was worse: **627 px of the
`τ⋆=1` rule and 651 px of the `τ⋆=2` rule**, the figure's own headline annotation.

### Before and after, measured on the rendered artefact

| measure | before (S5) | after (S6) |
|---|---|---|
| text or legend boxes within 1.6 pt | 3 pairs, plus `0.9`/`1` rendering as the single token `0.91` | **0** (22 boxes in Fig 2, 15 in Fig 3) |
| pixels of any `τ⋆` rule overwritten | 627 + 651 by the legend, 168 + 69 + 69 by annotation boxes | **0** |
| coordinate cells carrying >1 marker | 4 cells, holding 4, 4, 3 and 2 markers | **0** |
| series in the busiest panel | 5 | **1** |
| smallest tick label | 5.6 pt | **6.0 pt** |
| grey band explained in the caption | no | **yes** |
| located window `[1, 1.001]`, share of panel (b)'s axis | 10.000 % (categorical) | 7.370 % (symlog) |
| — against its true log-τ share of 0.0910 % | ×109.9 | **×81.0** |
| `τ ∈ [0.5, 0.9]`, share of the axis | 10.0 % | 10.303 % |
| — against its true log-τ share of 53.5 % | ×0.19 | **×0.19** |

**The last two rows are the honest part of this table and they were found by the critics,
not by me.** The rebuild fixed the inflation only partly and **reproduced the compression
almost exactly**. This is structural, not a tuning failure: the eleven widths are a
geometric ladder in the *offset* by construction, so any log-like axis in that offset spaces
them near-uniformly. What symlog actually buys over the index axis is **disclosure** — the
coordinate is named on the axis, in the caption and on every labelled tick, where the index
axis silently presented itself as an axis of τ values. That correction is now recorded in
the generator and, so it reaches a reader who never opens the source, in the caption.

`overlap_audit()` now runs inside the generator and **fails the build** on any two text or
legend boxes within 1.6 pt, in either figure. The pad is 1.6 pt precisely because
matplotlib's `Bbox.overlaps()` is a strict intersection test and passed the abutting
`0.9`/`1` pair that rendered as `0.91`. Both figure PDFs are byte-reproducible.

---

## 2. The captions, in full

### Table 1 — before

```latex
\caption{Placement~A: a one-scalar readout on the \emph{completed} threshold; one deterministic
adversary, one pass to $T = 10^6$. \emph{All eleven arms run are listed}, so no covering arm is
withheld; five exceed the bound at $T = 10^6$. Proposition~2's bound is $13.2061$ at $T = 2{\times}10^5$ and $14.8155$ at $T = 10^6$;
``ratio'' is $\max_t|E_t|$ over it, ``Sat.'' the fraction of rounds on which~(4) delivers its full $\pm b$.
Every figure is the \emph{primary} regime's, defined in Appendix~\ref{app:support}, which also
gives the $T = 10^4$ excursions and the fitted excursion law.}
```

### Table 1 — after (3 sentences; target 2–3)

```latex
\caption{Placement~A: a one-scalar readout on the \emph{completed} threshold, under one
deterministic adversary, on one pass to $T = 10^6$; all eleven arms run are listed.
Proposition~2's bound is $13.2061$ at $T = 2{\times}10^5$ and $14.8155$ at $T = 10^6$;
``ratio'' is $\max_t|E_t|$ over it, and ``Sat.'' the fraction of rounds on which~(4)
delivers its full $\pm b$. Every number is the \emph{primary} regime's, defined in
Appendix~\ref{app:support}, which also gives the $T = 10^4$ excursions and the fitted
excursion law.}
```

Cut: **"so no covering arm is withheld"** — a rebuttal, not a description; the fact it
defended survives as the caption's own first clause. Cut and **relocated**: "five exceed the
bound at `T = 10^6`" — a conclusion, and grepping first showed it existed in exactly one
place in the paper, so deleting it would have lost a fact. It now sits in the retention
paragraph where Table 1 is first discussed, and the count was independently recounted off
the table's own ratio column (4.25, 42.10, 3.58, 3.34, 60,747 exceed 1 — five).

### Figure 2 — before (7 sentences)

```latex
\caption{The dead-band coverage cliff, and the fact that its edge moves.
  \textbf{(a)} Realised miscoverage against dead-band width $\tau$ under five admissible
  $(r_t,\hat{q})$ pairs. Each pair's $\tau^{\star} = \sup_x r_t(x) + \sup_t \hat{q}_t - b/2$
  is marked in its own colour, dashed where it falls on the axis and arrowed where it does
  not: $1$ at the null scorecaster, $2$ at $\hat{q} \equiv +b/2$ and $7$ at a saturator of
  level $4b$ are dashed; $0$ at $\hat{q} \equiv -b/2$ and unbounded under
  \citeauthor{angelopoulos2023pid}'s tangent integrator are arrows. Three widths run under
  each pair, plus four wider bands at the null scorecaster. All $19$ dead-band runs
  land on the side of their own $\tau^{\star}$ that the law predicts, and the vertical
  dashes are the law's prediction, not four located edges: only the null scorecaster's
  edge has runs on both sides of $\tau^{\star}$. Appendix~\ref{app:support} gives the
  realised miscoverage at each covering setting.
  \textbf{(b)} An eleven-point grid at the null scorecaster \emph{locates} that edge
  between $\tau = 1.000$ and $1.001$, with no intermediate regime. Horizons: $T = 10^{6}$
  in (a) except the four widest bands ($\tau \ge 2$), run only to $T = 2{\times}10^{5}$;
  $T = 10^{5}$ in (b).}
```

### Figure 2 — after (4 sentences; target 3–4)

```latex
\caption{Realised miscoverage against dead-band width $\tau$ at the null scorecaster,
  $\hat{q} \equiv 0$ with a saturator of level $b$, where $\tau^{\star} = \sup_x r_t(x) +
  \sup_t \hat{q}_t - b/2$ is $1$. \textbf{(a)} The full sweep: filled markers run to
  $T = 10^{6}$ and the four widest bands, drawn open, to $T = 2{\times}10^{5}$; blue
  covers, orange forfeits, and the dashed rule is $\tau^{\star}$. \textbf{(b)} The same
  setting at $T = 10^{5}$ over eleven measured widths, placed by $\tau - \tau^{\star}$ on
  a symlog axis whose linear zone is $|\tau - \tau^{\star}| \le 10^{-3}$, which magnifies the
  neighbourhood of $\tau^{\star}$; unlabelled minor ticks mark $\tau = 0.95$ and $1.05$. The grey band spans the widest covering width to the
  narrowest failing one; Figure~\ref{fig:settings} gives the other four $(r_t,\hat{q})$
  settings.}
```

### Figure 3 — new (4 sentences; target 3–4)

```latex
\caption{All $19$ dead-band runs, at the five admissible $(r_t,\hat{q})$ settings:
  rows are settings ordered by $\tau^{\star}$, and the shared horizontal axis is $\tau$.
  Blue markers cover at $\approx \alpha$ and orange markers return $1.000000$; filled
  markers run to $T = 10^{6}$ and open markers to $T = 2{\times}10^{5}$. The rule on each
  row is that setting's $\tau^{\star} = \sup_x r_t(x) + \sup_t \hat{q}_t - b/2$, printed
  at the right, and the tinted band is $\tau \le \tau^{\star}$. Two rules fall off the
  axis and are drawn as arrows: $\tau^{\star} = 0$ at $\hat{q} \equiv -b/2$, and
  $\tau^{\star}$ unbounded under \citeauthor{angelopoulos2023pid}'s tangent integrator.}
```

Neither adversarial pass could find a sentence in any of the three that argues a conclusion,
restates a finding, or pre-empts an objection. One quoted its own result: *"No quote to
offer."*

---

## 3. The Introduction, in full

```latex
\section{Introduction}
\label{sec:intro}

A refereed paper states that a scorecaster breaks Conformal PID's coverage guarantee. A later
one, by the same first and last authors, proves in the same notation that a bounded
perturbation of the deployed threshold does not. The later cites the earlier, so this is ordinary
self-correction, and the joining is what this paper adds.

An online conformal method emits a threshold before each observation and moves it. Forecast
stability names, scores and prices that movement
\citep{tunc2013nervousness,godahewa2025stability,vanbelle2023deepstability,%
pritularga2024congruence,genov2026switching,vanbelle2026stabilizing}. Varying temporal structure at
fixed level came earlier, in forecast verification, matching predictive marginals on real producers
\citep{gneiting2007calibration,pinson2012scenarios,worsnop2018scenarios}. Coverage and mean length
under-describe a deployed interval \citep{min2026questioning,vaze2026simultaneous}. None of it is
claimed here.

\paragraph{The record carries a claim and its refutation; this paper joins them.} Conformal PID \citep{angelopoulos2023pid}
adds a \emph{scorecaster} $\hat{q}_{t+1}$ to a saturating error integrator, asking only that it
be predictable and lie in $[-b/2,b/2]$: ``any function of the past'' (Theorem~1). Such a readout
is already quantified over. The claim reads ``[s]ince using a scorecaster (D-part) in
C-PID breaks the theoretical coverage guarantee'' \citep{li2024neuralconformal}, stated and
acted on in its baselines paragraph, verbatim on refereed printed page $18443$. It is refuted
twice, with proof. \citet[Corollary~2]{li2025o2cp} add an arbitrary predictable $d_t$ with
$|d_t| \le \mu_t(b/2-|\hat{q}_t|)$ to the deployed threshold, note that the result ``has exactly
the CPID error-integration form'', and conclude $|E_T| = o(T)$. The same generic-slot argument
carries AcMCP's long-run coverage \citep{wang2026acmcp}. Four surfaces were queried on 20 August
2026 for both identifiers and ``scorecaster''. They are arXiv full text, arXiv abstracts,
OpenReview, and the six works Semantic Scholar records citing
\mbox{\citet{li2024neuralconformal}}. None returns both the claim and the corollary.
\citet{hu2026distinformed} still call scorecaster choice ``arbitrary'' and lacking ``principled
guidance'' while asserting valid coverage: model selection, not validity. \textbf{We claim
neither the placement nor the derivation.}

\paragraph{Where that refutation stops, the condition is tight.} Corollary~2 is a \emph{retention} result, silent
outside its radius, and the question it leaves is whether that radius is sharp.
Section~\ref{sec:forfeit} exhibits a legal perturbation leaving it: the $L_1$ dead-band family
characterised here on the \emph{completed} threshold, whose edge is the corollary's radius at
the null scorecaster. Past it coverage goes, not only the rate: the published sufficient
condition is necessary there. Section~\ref{sec:related} sets both claims beside four
vocabularies for the same movement.
```

Four drafts were written and measured, not one presented as inevitable. Draft A opened
concrete and kept two retitled `\paragraph` heads; draft B opened on the thesis and dropped
the heads entirely for continuous prose. A's opening won because the brief asks for the
concrete facts in sentences 1–2 and B slipped them to 2–3; A's heads survived because S4
wave 1 installed them so a referee reading only the abstract and the heads counts exactly
two claims. Draft C, the synthesis, was then read back and found to have introduced a fault
of its own — it folded the Conformal PID definition inside the scope of "None of it is
claimed here", i.e. disowned the method the paper builds on. Draft D moved it back.

**A correction to the brief, which would have been an error to follow.** C1 says to open on
the fact that "neither cites the other". They **do** cite each other — this project's own
established finding is that the halves share a bibliography. Writing it would have put a
false statement in the paper's first paragraph. The true hook is stronger: the correction is
in the record and is nowhere *stated* as a correction, which is what the four-surface check
measures.

Nothing was dropped: **16 of 16 distinct citation keys survive**, verified independently by
both adversarial passes. Page 18443, the 20 August 2026 date, the four-surface list, the
six-citer count, every quotation, Theorem 1, Corollary 2 and the bolded concession are all
present in the compiled PDF. A residual S5 recorded but could not afford is now closed:
"prices it", whose antecedent was wrong, is now "prices that movement".

---

## 4. O65 — resolved, branch D1

**The repository is public**, verified headless with no browser:
`curl -s https://api.github.com/repos/pa1aash/Turnover-Blind` → HTTP 200, `"private": false`,
`"visibility": "public"`, `"default_branch": "main"`. The printed URL was re-checked live: 200.

The statement is an unnumbered `\section*{Code and data}` after the bibliography, guarded by
`\if@anonymous`:

> The simulator, its frozen configuration, the `results/` files behind every figure and
> table, the generators that read them, and this project's audit trail across sessions are
> at `https://github.com/pa1aash/Turnover-Blind`.

**The placement is not the brief's default, and the reason is measured.** The default — a
paragraph immediately after Limitations — was built first and rebuilt twice shorter. It does
not fit: the body is exactly full at offset 0, the statement is 2 typeset lines, and all
three versions spilled onto page 5. The only ways to buy those lines were to cut
claim-bearing prose or to shrink Figure 2 past what its readability check certifies, and
trading a claim for a metadata statement is the wrong way round. The chosen position is the
other convention the brief names, is free of E-values' count, and keeps a heading in the PDF
outline. Under TS-LIMITS (4–7 body pages) it moves back into the body for free, and
`main.tex` says so at the block.

---

## 5. The two numeric spot-checks

Neither re-ran the simulator. Both read `results/forfeit-20260820T063045Z-83747c45.json`
directly. R3a and R3b are untouched in substance.

### E1 — confirmed exactly

The four horizons were taken from the run's own `config.horizons`, not assumed from the
paper: `[10000, 100000, 200000, 1000000]`. 11 arms × 4 horizons = 44.

Comparing `exact_threshold_tie` against the primary `adversarial` regime **bit for bit** on
Table 1's five reported quantities: **44 of 44 identical**. The mirror claim holds too —
`exact_threshold_strict` matches on **0 of 44** and moves all 44 — and both named strict
figures reproduce.

One thing recorded so a recount is not misread: widened to all **nine** recorded fields the
count is **43**, not 44. The single difference is `frac_adversary_clipped` on
`(running_mean, T = 10^6)`, 0.899994 against 0.899990 — a field Table 1 does not report.
Both critics reached this independently. The sentence's noun was tightened as a result: it
now reads "reproduces every quantity Table 1 reports: 44 of 44 arm-horizon cells identical",
because Table 1 has 66 printed cells and shows two of the four horizons, so "every cell of
Table 1" was not the set being counted.

### E2 — failed as printed, and the paper was corrected in the same wave

"Across the arms the excursion fits `max_t|E_t| ≈ max{0.5 h(T)+0.9, 0.63/(1−w)}`" is **not
true across the arms.**

| | cells | median rel. error | worst |
|---|---|---|---|
| control + four partial-adjustment arms | 20 | **1.01 %** | 5.66 % (`w = 0.9`, `T = 10^5`) |
| the other six arms | 24 | **52.5 %** | 100.0 % (failing dead band) |

Every one of the 24 missed cells excurses **further** than predicted, so the formula is not
even a conservative bound off-family. Worst case is the failing dead band, where
`|E_t| = (1−α)t` is linear in `T`: 900,000 measured against 7.808 predicted. The formula's
own `w` exists only for the partial-adjustment family, which is the structural tell that the
fit was always scoped to it.

The text now names the five arms it holds on, says plainly that it does not extend to the
other six, and — after an adversarial pass showed the failure is structural rather than
noise — names `w = 0.9` as the loosest case, the one arm whose two branches of the maximum
cross inside the horizon range. An adversarial recomputation found the paper now **under**-claims:
all 20 residuals are ≤ 0, so on those five arms the law is a strict upper envelope, not a
two-sided fit. That was left alone; strengthening a claim was outside the wave's remit.

---

## 6. Build, verified by the opened-page method

Recipe: `pdflatex`, `bibtex`, then **three** more `pdflatex` passes — four total, artefacts
deleted first. The fourth pass is new this session: `\clearpage` in the appendix made the
three-pass build emit "Label(s) may have changed". Measured before changing the recipe —
pass 4's `.aux` is byte-identical to pass 3's and the two PDFs' rendered text is identical,
so the three-pass output was already correct and the warning was page bookkeeping.

| counter | E-values (`sglblindworkshop`) | TS-LIMITS (`dblblindworkshop`) |
|---|---|---|
| TeX errors | 0 | 0 |
| undefined citations / references | 0 / 0 | 0 / 0 |
| overfull boxes | 0 | 0 |
| underfull hboxes | 2 | 2 |
| LaTeX warnings | 0 | 0 |
| `pdfendlink` warnings | 0 | 0 |
| bibtex warnings | 0 | 0 |
| `main.aux` bytes | 14,201 | 14,201 |
| pages | 8 | 8 |

**Page count by the opened-page method** (`pdfinfo` for the count, per-page `pdftotext` for
where the body actually ends):

| page | first content |
|---|---|
| 1 | title |
| 2 | Figure 1, Section 2 |
| 3 | Table 1, Figure 2, Section 3 |
| 4 | body |
| **5** | **References** |
| 6 | references, then "Code and data" |
| 7 | A — Supporting measurements |
| 8 | B — The four vocabularies |

**Body-end offset 0.** The body is exactly 4 pages. 8 pages is not an overrun: pages went
7 → 8 because the appendix grew and `\clearpage` now starts appendix B on its own page, and
E-values excludes references and optional appendices. **The offset is the test, not the
count.**

A stale record was corrected rather than left: `main.tex` had said the double-blind build
"runs 2 lines onto p.5" and told later sessions not to fix it. After the Introduction rewrite
and the Figure 2 height reduction **both options are offset 0** — the two builds share an
offset for the first time since S4 wave 2.

`tools/audit_paper_numbers.py`: 409 body tokens, 237 excluded as structural, 5 derived, 144
sourced, 21 config labels, 2 weak tier-2, **0 unsourced**.

---

## 7. The double-blind metadata check

This is the specific defect S5's critic found, and a broad rewrite plus a **new repository
URL** are exactly what could reintroduce it. Re-run, with a control so a zero cannot be a
broken test:

| probe | `dblblindworkshop` | `sglblindworkshop` (control) |
|---|---|---|
| `pdfinfo` Author | **Anonymous Author(s)** | Palaash Gang |
| "Palaash" in `pdfinfo` | **0** | 1 |
| "Palaash" in page text | **0** | 2 |
| "github.com" in page text | **0** | 1 |
| inflated FlateDecode object streams | **none** | Gang, Turnover, github, pa1aash, palaashgang |

The control fires on every probe, so the zeros are measurements. An adversarial pass
inflated **every** compressed object stream — which `strings` cannot see, and which is why
the original leak went unnoticed — and found the author's name in none of them.
**No regression.** The `\if@anonymous` guard on the new availability section works.

---

## 8. The critics

Three passes: one instruction critic and two adversarial (the second launched read-only when
the first stopped reporting; the first then returned as well, so both are acted on).

The instruction critic returned **PASS on 10 of 12 items**, including every frozen-field
check, the axis principle, the caption targets, the drafting requirement, the O65 branch,
"no gate signed", and all Section 0 rules. It found one real cross-reference defect and
three thin spots, all fixed.

**Findings applied (13):** the symlog compression reproduction, recorded in generator and
caption; Figure 3's `τ⋆=0` arrow tail sitting inside a data marker; an unlabelled τ = 2.5
marker; a caption claiming "each tick carrying the τ it marks" against an 11-tick, 9-label
axis, with the two orphans unattributable and one of them a forfeit point; marker fill
meaning two different horizons under one legend; "every cell of Table 1" being the wrong
noun; "at every horizon" carrying no tolerance; "and cite it" weakened to "share a
bibliography"; a `\ref` supporting half its clause; the two `\paragraph` heads keeping their
slot and losing their function; plus two stale records of my own in `GATES.md` and `VENUE.md`.

**What held under attack**, which is signal in itself: all 66 Table 1 cells recomputed with 0
mismatches; both numeric claims verified independently by both passes; every axis fitted from
tick bounding boxes to under 0.005 pt; the declared symlog confirmed as the applied symlog
with `linthresh` exactly 1e-3 and all 11 marker centres within 0.4 pt; 16 of 16 citation keys
surviving; and no caption sentence that argues.

---

## 9. Frozen fields — one sentence each

**Venue was not touched.** `docs/OPEN_QUESTIONS.md` has a zero-byte diff across the whole
session, and both `\usepackage` venue lines and both `\workshoptitle` lines are byte-identical
to `b74825e` — verified by md5 by the instruction critic and independently by diff by me,
after the switch was flipped for double-blind testing and flipped back.

**Affiliation was not touched.** `main.tex` still reads `Independent Researcher`, byte-identical.

**Author name and email were not touched.** `\paperauthor` and the `\texttt` email line are
byte-identical.

One thing for your eye, which is within the letter of the freeze but worth seeing: sub-session
D introduced a new author-identifying string, the repository URL carrying your handle. It is
`\if@anonymous`-guarded and verified absent from the double-blind build.

---

## 10. Not reached, and what still needs a pass

- **`τ⋆` is first used in Section 2 and first defined in Section 3.** A pre-existing forward
  reference. The fix is an inline definition the exactly-full body has no room for, or a
  reordering outside this session's scope. Flagged, not hidden.
- **The symlog axis still magnifies the neighbourhood of `τ⋆` by ×81** against a true log-τ
  axis. The caption now warns the reader; the alternative fix — a second inset on a true
  log-τ axis — needs body lines the 4-page ceiling does not have. Revisit under TS-LIMITS.
- **The excursion law under-claims.** On its five arms it is a strict upper envelope, not a
  fit. Strengthening was outside sub-session E's remit.
- **Figure 1 still floats above the end of Section 1.** Pre-existing; S5 measured the
  alternatives worse.
- **Several Appendix A numbers were not independently recomputed by a critic**: 70.80, 120.60,
  11.20, 0.100010, 0.100001, 20.10, 0.249376. They were verified mechanically by
  `audit_paper_numbers.py` (0 unsourced) but not attribution-checked by hand this session.

## Is it ready?

**Close, but one thing is not done and it is not a prose problem.** Read once more by you,
the paper is submittable once venue and affiliation are set — the two claims are unchanged and
were verified, every printed number traces to `results/`, both builds are clean at offset 0,
and the double-blind variant leaks nothing.

**The one blocker is the push.** Until `main` is pushed, the availability statement is false:
the remote is still at S5's HEAD, so it holds neither Figure 3 nor the generator that made
either figure, and `figure1_boundary.pdf` there is the very figure this session condemned. A
referee clicking that link today sees an S5 tree. That is this sub-session's last action and
it is verified against the remote below.

**The E-values deadline is 2026-08-29 23:59 AoE. As of today, 2026-08-21, that is 8 days.**
The OpenReview form enforces `duedate` 2026-08-30 13:00 UTC, 61 minutes past the published
AoE time, in the safe direction. Plan to the published time.

Venue and affiliation remain `[OPERATOR INPUT]`, frozen exactly as this session found them.
Nothing was submitted.
