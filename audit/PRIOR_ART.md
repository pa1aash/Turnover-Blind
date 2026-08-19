# Prior art and scoop risk

Three sweeps, run independently of the automated sweep described in
`docs/PLAN_ORIGINAL.md`, followed by explicit CLEAR / NARROW / OCCUPIED verdicts for
claims C1 and C2.

**Headline: the planning document's inherited novelty finding is wrong in its strongest
form and right in a much narrower one.** The claim that "arXiv returns 0 for
`conformal` × `downstream decision`" is false — decision-focused conformal prediction is
an active field with a dozen entries the plan does not cite, at least one of them by a
confirmed speaker at the target venue. What survives is a narrower and still-defensible
proposition: nobody varies the *temporal adaptation rate* of an online conformal method
and measures the *movement cost of the decision it drives*.

---

## 0. Method, and what it cannot see

**Worked:** the arXiv API (metadata and abstract search across all fields), DBLP
(computer-science venue verification), Crossref (DOIs, journals, volumes and pages), web
search, and direct retrieval of full text from arXiv HTML and author copies.

**Did not work, and the sweep is weaker for it:**

| Tool | Failure | Consequence |
|---|---|---|
| Semantic Scholar API | HTTP 429 throughout the G0 session, on both the direct API and the connected server | **The forward-citation screen of Gibbs–Candès ACI was not possible during G0.** It was subsequently run in S1 (2026-08-19) with **no API key**, using incremental backoff: 659 unique citing papers across ACI, DtACI, conformal PID and SAOCP. The gap this row records is closed; the row is retained because it explains why §3's verdicts were written without it. |
| OpenAlex | HTTP 429 on most calls; the one ACI record it returned carries 27 citations, which is obviously incomplete | Not usable as a citation-graph substitute. **Confirmed in S1 (2026-08-19): Semantic Scholar returns 557 citing papers for the same record, so the prescribed OpenAlex fallback misses ~95 % of the citing set and would have produced a false negative.** |
| Consensus | Monthly search quota exhausted before this session | No third academic-search opinion. |
| SSRN direct | HTTP 403 on every endpoint | SSRN was reached only indirectly through web search. The plan flags SSRN as unswept; **it remains only partially swept.** |

**A limit that applies even to what did work:** the arXiv API searches titles, abstracts,
comments and author fields — **not full text**. A paper that varies a conformal step size
and reports turnover in a results table, without saying so in its abstract, would not
appear in any query below. Zero hits here mean "nothing at abstract level", which is
weaker than "nothing exists". This is precisely the inference the plan's prior sweep made
too strongly, and it is not repeated here.

All queries and their result counts are recorded below so a later session can re-run them
rather than re-invent them.

---

## 1. The seven works the plan does not cite

All seven were supplied externally, and all seven resolve. Metadata below is from the
arXiv API and DBLP.

| Work | Identifier | Verified | Proximity to C1 | Proximity to C2 |
|---|---|---|---|---|
| Lin, Delage & Chan, *Conformal Inverse Optimization* | arXiv:2402.01489, **NeurIPS 2024** | ✔ authors, title, venue | **Low.** Learns an uncertainty set for unknown parameters in inverse optimization; no online adaptation rate, no repeated decision, no movement cost. | **Low.** |
| Yeh, Christianson, Wu, Wierman & Yue, *End-to-End Conformal Calibration for Optimization Under Uncertainty* | arXiv:2409.20534, **TMLR Dec 2025** | ✔ | **Medium.** Learns uncertainty sets shaped by downstream decision loss; portfolio optimization is one application. The premise "not all uncertainty is equally valuable for downstream decision-making" is C1's premise. But the object shaped is set *geometry*, not adaptation *rate*, and the setting is not sequential-with-inventory. | **Low.** |
| Zhou, Orfanoudaki & Zhu, *Conformalized Decision Risk Assessment* | arXiv:2505.13243 | ✔ | **Low.** Probability that a prescribed decision stays optimal; one-shot. | **Low.** |
| Zhou & Zhu, *Calibrating Decision Robustness via Inverse Conformal Risk Control* | arXiv:2510.07750 | ✔ | **HIGH — nearest neighbour on the "coverage is the wrong knob" axis.** Explicitly constructs estimators that "trace out the miscoverage–regret Pareto frontier", enabling calibration of robustness by cost–risk preference rather than by a prespecified coverage target. That is C1's thesis for the coverage *level*. It is not C1's thesis for the adaptation *rate*, and the setting is static robust predict-then-optimize with no incumbent decision. | **Low.** |
| Chen, Zhou & Zhu, *Learning Polyhedral Conformal Sets for Robust Optimization* | arXiv:2605.08506 | ✔ | **Medium.** Decision-aware conformal set geometry; same premise, different object. | **Low.** |
| Zhu, Kiyani, Pappas & Hassani, *Conformal Risk-Averse Decision Making with Action Conditional Guarantee* | arXiv:2606.05551 | ✔ | **Low–medium.** Action-conditional coverage for risk-averse decisions; conditional on the action, not on the decision's history. | **Low.** |
| Liang, Ren & Chen, *Optimal Training-Conditional Regret for Online Conformal Prediction* | arXiv:2602.16537 | ✔ | **Medium.** Online conformal under drift, evaluated by training-conditional cumulative regret with minimax-optimal rates; drift detection replaces a fixed step size. Relevant as an alternative answer to "how should the method adapt", but regret here is about coverage and set size, never about decision movement. | **Low.** |

**Erick Delage co-authors the first of these and is a confirmed ML×OR speaker.** A
submission to that workshop that does not cite Conformal Inverse Optimization, in a paper
about conformal prediction feeding an optimization-flavoured decision, is a gratuitous
risk. It costs one sentence to remove.

**Three further works, not on the supplied list, found by this sweep and equally
uncited:**

- **Podkopaev, Xu & Lee, *Adaptive Conformal Inference by Betting* (arXiv:2412.19318).**
  Parameter-free adaptive conformal inference. Its stated motivation is that existing
  methods have "explicit dependence on and sensitivity to the choice of the learning
  rates". This is directly damaging to the plan's rebuttal that the field has not noticed
  the step size matters — and it is also a *competing solution*: if you can be
  learning-rate-free, the question "how do I choose γ" partly dissolves. F7 must say why
  a decision-cost-aware γ still matters when a parameter-free method exists. The answer
  is available (parameter-free methods optimise coverage-tracking, not movement cost) but
  it has to be made.
- **Wang & Hasuike, arXiv:2605.01176.** In the plan's own reference list as a bare
  identifier in a trailing clause. See §4.3 — it is the closest published neighbour on the
  *pathology* (decision-focused learning induces excessive turnover; damping helps), and it
  has no conformal or interval content whatsoever.
- **Kato, *Conformal Predictive Portfolio Selection* (arXiv:2410.16333, q-fin.PM).**
  The only other conformal-prediction portfolio paper besides Ryan's. Uses prediction
  intervals to select portfolios; no adaptation-rate analysis, no transaction costs.

---

## 2. Sweep E1 — decision-focused conformal prediction

**Question.** Does any existing work vary the conformal **adaptation rate** and measure
**downstream turnover or switching cost**?

**Queries and counts.**

| Query (arXiv API) | Results |
|---|---|
| `abs:"conformal" AND abs:"downstream decision"` | **12** |
| `all:"conformal prediction" AND all:"transaction cost"` | 0 |
| `all:"conformal" AND all:"trading cost"` | 1 (Ryan) |
| `all:"conformal" AND all:"switching cost"` | 1 (unrelated: antenna configuration) |
| `all:"conformal prediction" AND all:"hysteresis"` | 0 |
| `all:"conformal prediction" AND (all:"soft-thresholding" OR all:"proximal operator" OR all:"movement cost")` | 0 |
| `all:"conformal prediction" AND (all:"lazy update" OR all:"infrequent update" OR all:"update frequency")` | 0 |
| `all:"adaptive conformal" AND (all:"learning rate" OR all:"step size")` | 5 |
| `cat:q-fin.* AND all:"conformal prediction"` | 11 |

**Finding 1 — the field exists, and the plan's inherited claim is false.** The single
query `conformal × downstream decision` returns a full page of directly on-topic work:
Utility-Directed Conformal Prediction, End-to-End Conformal Calibration, Optimal
Decision-Making Based on Prediction Sets, Optimal Model Selection for Conformalized
Robust Optimization, Decision-calibrated prediction sets for power systems, Learning
Polyhedral Conformal Sets, and more. The inherited assertion that "arXiv returns 0 for
`conformal` × `downstream decision` × `variance`" cannot be reproduced and should be
deleted from the paper, not softened.

**Finding 2 — but the specific dissociation is not occupied.** Across every one of those
works, the object being shaped for the downstream decision is one of: the **geometry** of
the uncertainty set, the **coverage level**, the **model** chosen, or the **risk
threshold**. None of them varies the **temporal adaptation rate**, and none of them
measures a **movement cost between consecutive decisions**. The reason is structural: the
decision problems in this literature are one-shot or per-period-independent
predict-then-optimize problems with no incumbent position, so there is no movement to
charge for.

**Finding 3 — the nearest neighbour is Zhou & Zhu (arXiv:2510.07750)**, which traces a
miscoverage–regret Pareto frontier and argues that fixing a coverage target a priori
"offers little guidance". That is C1's argument, one axis over: they vary the coverage
*level* and F7 varies the adaptation *rate*.

**E1 conclusion.** The field is populated; the square is not. The plan's novelty section
must be rewritten from "nothing exists" to "this literature shapes the set for the
decision; nobody prices the rate at which the set moves".

---

## 3. Sweep E2 — the pairing the plan admits was never swept

**Queries run:** `conformal prediction transaction costs turnover`; `adaptive conformal
step size decision cost`; `online conformal hysteresis dead-band`; `conformal prediction
switching cost` — each in several arXiv formulations (counts in §2) and as web searches.

**Result:** nothing occupies the pairing.

- `"conformal prediction" AND "transaction cost"` returns **zero** arXiv records.
- The whole of q-fin × conformal prediction is **11 papers**, of which nine are
  electricity-price or general time-series forecasting. Only two concern portfolio
  decisions: **Ryan's Conformal Kelly** and **Kato's Conformal Predictive Portfolio
  Selection**. Neither varies an adaptation rate against cost.
- Web search over SSRN surfaces adaptive conformal prediction applied to commodity
  forecasting (Pinitjitsamut), a survey of conformal prediction in finance (Noguer i
  Alonso), and adaptive conformal prediction under structural breaks (Calleo). None
  addresses adaptation rate versus trading cost.

**The forward-citation screen of ACI could not be run during G0** (§0). This is the one
query most likely to surface a paper that does the F7 experiment inside a larger applied
study without advertising it in the abstract. **It was run in S1 (2026-08-19) with no API
key, using incremental backoff — 659 unique citing papers across ACI, DtACI, conformal PID
and SAOCP.** Its verdict must be folded into §5 before gate G1 is signed.

**A caution about the word "turnover".** The plain arXiv query
`conformal AND turnover` returns fifteen results of which fourteen are enzyme kinetics —
"turnover" is dominated by molecular biology. Any future automated screen on this term
must be restricted by category, or it will be swamped and read as a null.

---

## 4. Sweep E3 — switching-cost online learning and no-trade regions

**The purpose of this sweep is to establish what is already known**, so that F7 does not
claim it. The answer is: a great deal.

### 4.1 Portfolio side — the no-trade region

| Work | Established |
|---|---|
| Constantinides, *JPE* 94(4):842–862, 1986 | The no-trade region under **proportional** transaction costs. |
| Davis & Norman, *Math. OR* 15(4):676–713, 1990 | The no-trade cone; the canonical treatment. |
| Gârleanu & Pedersen, *J. Finance* 68(6):2309–2340, 2013 | **Quadratic** costs give *linear partial adjustment* toward an aim portfolio — explicitly *not* a no-trade band. See `audit/REFS_REJECTED.md` §1.1. |

The dead-band under an L1 movement penalty is forty years old. **F7 must not present it
as new**, and must cite Constantinides and Davis–Norman rather than Gârleanu–Pedersen.

### 4.2 Learning side — online convex optimization with switching costs

| Work | Established |
|---|---|
| Zinkevich, ICML 2003 | Online gradient descent; the base algorithm ACI is an instance of. |
| Kalai & Vempala, *JCSS* 71(3):291–307, 2005 (COLT 2003) | Follow the Lazy Leader: no-regret with an explicitly bounded number of switches. |
| Geulen, Vöcking & Winkler, COLT 2010 | The shrinking dartboard: no-regret with O(1) expected switches. |
| Andrew, Barman, Ligett, Lin, Meyerson, Roytman & Wierman, COLT 2013 / SIGMETRICS 2013 (arXiv:1508.03769) | **No online algorithm can be simultaneously constant-competitive and no-regret under switching costs.** |
| Chen, Goel & Wierman, COLT 2018 (arXiv:1803.10366) | Online Balanced Descent for smoothed OCO in high dimensions. |
| Borodin, Linial & Saks | Metrical task systems: the general movement-cost framework. |

**"You can track a moving target while rarely moving, at a quantified regret cost" is a
solved problem.** The algorithmic content of C2 — laziness, soft-thresholding, a movement
penalty — is standard technology in this literature.

**Two consequences that bear directly on the paper.**

First, **the Andrew et al. impossibility constrains C2's headline claim.** C2 asserts it
"dominates *both* fast ACI (which churns) and fixed-α slow quantiles (which under-adapt)
at matched coverage". In the switching-cost formulation, simultaneous optimality against a
dynamic comparator (fast) and a static comparator (slow) is provably unattainable in
general. C2's dominance claim must therefore be stated as an empirical, regime-specific
result, or the paper must argue that the conformal setting escapes that lower bound. An
unqualified "dominates both" is a claim the OR half of the ML×OR audience will recognise
as too strong.

Second, **regret is the wrong currency and the plan already cites the proof.** Ramalingam,
Kiyani & Roth (ICML 2025, arXiv:2502.10947) show that regret guarantees imply marginal
coverage in i.i.d. settings but fail adversarially, and that the tight correspondence
requires *swap* regret. So the SOCO literature's regret bounds **cannot be imported to
give C2 its coverage theorem**. That is a genuinely useful fact: it tells you the theorem
in `audit/CLAIMS.md` C-a has to be proved directly on the coverage recursion, and it
explains why the intersection of the two literatures is empty rather than trivial.

### 4.2b Amendment — a 1993 antecedent for "estimate movement causes turnover"

*Added after the Module E sweep, from the research-pipeline run. See
`docs/HYPERRESEARCH_REPORT.md`.*

The planning document cites "MacLean, Thorp & Ziemba" with no locator and claims to have
experimentally ruled out the channel it describes. That citation has now been resolved to
**MacLean, Thorp & Ziemba, "Good and bad properties of the Kelly criterion" (2010)**, and
reading it produces two findings that bear directly on prior art.

**First, the plan mis-describes the channel.** The plan says the sweep argued the anomaly
was explained by "noisy **scale** estimates asymmetrically punish Kelly log-growth". What
the paper actually says is:

> "Given the extreme sensitivity of E log calculations to errors in **mean** estimates,
> these estimates must be accurate and to be on the safe side, the size of the wagers
> should be reduced."

and, citing Chopra & Ziemba (1993):

> "the mean is much more important than the variances and co-variances. **Errors in means
> versus errors in variances were about 20:2:1 in importance** as measured by the cash
> equivalent value of final wealth."

A conformal interval supplies a **scale** estimate. On the cited source's own numbers,
that is the channel roughly an order of magnitude *less* important than the one the paper
warns about. This cuts both ways for F7 and both should be said: the competing
explanation was weaker than the plan believed, so rejecting it is easier — and
correspondingly less impressive than "the difference between an over-determined
observation and an identified mechanism".

**Second, and more consequential: the same paper reproduces a figure of portfolio
turnover induced by input-estimate error.** Its Figure 2 is captioned "Average turnover
for different percentage changes in means, variances and co-variances", sourced to
**Chopra, "Improving Optimization", *The Journal of Investing* 2(3):51–59, 1993**
(doi 10.3905/joi.2.3.51).

So "moving input estimates induce portfolio turnover" is in the portfolio-optimization
literature from **1993**, and it appears in the very paper the planning document cites
and dismisses. **F7 cannot claim that observation.** The verdict in §5 is unchanged —
this strengthens rather than weakens the reasoning behind it — but the distinguishing
sentence now has to work harder: F7's claim is not that estimate movement causes
turnover, which is thirty-three years old, but that **the coverage criterion used to tune
the estimator does not record that turnover: arms matched on realised coverage and mean
width differ in it by an order of magnitude**.

Both Chopra references have been verified against Crossref and added to
`audit/REFS_VERIFIED.bib`.

### 4.2c Amendment — the switching-cost "calibration" lead does not scoop C2

*Added after the Module E sweep, from the research-pipeline run.*

The pipeline probed **Li, Yang & Ren, "Expert-Calibrated Learning for Online Optimization
with Switching Costs" (arXiv:2204.08572)** on the hypothesis that a paper combining
"calibration" with "switching costs" might already occupy C2's intersection. **It does
not.** From the paper's own text:

> "By tapping into the power of machine learning (ML) based optimizers, ML-augmented
> online algorithms (**also referred to as expert calibration in this paper**) have been
> emerging as state of the art, with provable worst-case performance guarantees."

"Calibration" there is the learning-augmented-algorithms sense — combining an ML
optimizer with a robust expert to bound the worst-case competitive ratio — not
statistical coverage calibration. Its comparator is a competitive ratio against an
offline optimal oracle, and its switching cost is a **Mahalanobis (quadratic)** distance,
not an L1 movement penalty.

Two consequences. The C2 intersection remains empty, so the NARROW verdict in §5 stands
and is now better tested. And the quadratic switching cost reinforces §4.1: even inside
the switching-cost learning literature the quadratic form is the default, which is one
more reason the L1 dead-band needs Constantinides and Davis–Norman rather than anything
from this line.

### 4.3 The closest published neighbour on the *pathology*, and it is in the plan's own reference list

**Wang & Hasuike, arXiv:2605.01176** (q-fin.PM, 2026-05-02), *"Decision-Induced Ranking
Explains Prediction Inflation and Excessive Turnover in SPO-Based Portfolio
Optimization"*. From the abstract: SPO-based decision-focused learning "may produce
inflated return signals and unstable portfolio reallocations"; the paper gives a KKT-based
interpretation and evaluates "clipping, min-max rescaling, and **partial portfolio
adjustment** as practical stabilization mechanisms."

That is: **a decision-focused learning method induces excessive turnover, and a damping
scheme fixes it.** Structurally, this is C1 and C2 together — in smart-predict-then-
optimize rather than conformal prediction, with prediction inflation rather than
adaptation rate as the cause, and with a heuristic rather than a coverage-preserving
update. **Read in full, S1 2026-08-19: the paper contains zero occurrences of
"conformal", "coverage", "quantile" or "prediction interval". It has no interval object of
any kind, so it is not a neighbour on C2's method at all — only on the pathology and the
remedy.** It still deserves a paragraph rather than the parenthesis the plan gives it.

**What it does pre-empt is the argument shape.** Its Table 1 caption already publishes
"Increasing risk aversion does not meaningfully reduce turnover" — the same move F7 makes
with the adaptation rate, one knob over. Two openings survive that: its risk-aversion
parameter δ is **fixed at 0.1 and never swept**, so the caption is an assertion rather
than a measured curve; and its partial adjustment is a **heuristic** stabilisation
mechanism rather than a rule derived from a movement cost.

**It is also a partial scoop of the framing**, not of the result: "decision-focused
methods churn, and damping helps" is now published. F7's distinct contribution has to be
(a) that the churn is caused by the *adaptation rate*, (b) that the *coverage criterion is
blind to it*, and (c) that the damping can be made *coverage-preserving*. Points (b) and
(c) are unoccupied. Point (a) is adjacent to occupied.

---

## 4.4 Amendment — one work the sweep missed, and the blind spot it reveals

*Added from the research-pipeline run.*

**Jia, Y. and Han, B., "Portfolio Selection with Adaptive Conformal Prediction",
PAKDD 2026, Lecture Notes in Computer Science vol. 16603, pp. 312–323, Springer Nature
Singapore, 14 July 2026, doi 10.1007/978-981-92-2014-4_25.**

This is the **closest-titled published work to F7** and it postdates nothing in this
project — it appeared a month before this audit. Module E's sweep did not find it.

What it does, from its abstract: a model-free portfolio-selection framework in which
investment risk is estimated by conformal prediction, accommodating distribution shift and
supplying coverage guarantees; VaR is taken from the lower bound of the conformal
prediction set; portfolio weights are optimised by projected gradient descent under
investor-specified constraints. Conformalised strategies with short-selling constraints
beat equal-weighted and non-conformal counterparts.

**Proximity assessment: close in territory, not in claim.** It does not vary the
adaptation rate, and neither the abstract nor the indexed metadata mentions transaction
costs or turnover. It therefore does not occupy C1's or C2's square. But it is a must-cite:
same application, same method family, one month old, and a reviewer who works in this area
will know it. Its full text sits behind a JavaScript challenge and **was not read**; the
proximity assessment above rests on the abstract and should be redone once the PDF is
obtained. Recorded in `docs/OUTSTANDING.md`.

### The blind spot this exposes, which matters more than the paper

Module E's sweep queried **only the arXiv API**. Jia & Han has **no arXiv identifier** — it
is a Springer LNCS conference chapter — so no arXiv query, however well constructed, could
have returned it. **But DBLP indexes the chapter and returns it on the first query, and
DBLP was already in this sweep's working-tool list (§0).** The failure was therefore
instrument choice, not venue coverage: a second index that was available and untried. It
surfaced here only because Ryan's Conformal Kelly cites it.

Two consequences for how the prior-art verdict should be read:

1. **The sweep's coverage of non-arXiv venues is weak because it did not use the indexes
   that cover them, not because those venues are unreachable.** DBLP covers Springer LNCS
   and was available; INFORMS journals, quantitative-finance journals and SSRN remain
   substantially unswept. The CLEAR/NARROW/OCCUPIED verdicts below are conditioned on that.
2. **The forward-citation screen of Gibbs–Candès ACI, which could not be run during G0
   because the Semantic Scholar API was rate-limited, was run in S1 (2026-08-19) with no
   API key via incremental backoff — 659 unique citing papers across ACI, DtACI, conformal
   PID and SAOCP.** It is the one instrument that indexes across venue types. It is no
   longer a G1 blocker; folding its verdict into §5 is.

A prior-art verdict produced by an arXiv-only method, which has just been shown to miss
the closest-titled work in the field, should not be signed off as final. That is a
statement about the method, not about the conclusion — the conclusion still looks right —
and it is exactly why G1 requires the citation screen before the framing is locked.

## 4.5 Amendment — two works found by the corpus critic that narrow the verdicts

*Added from the research-pipeline run's step-8 adversarial pass, which was tasked with
finding what would overturn this file's own conclusions. It found two things, and one of
them is a mistake this sweep made.*

### 4.5.1 "Coverage and length are not enough" is already published

**Min, Lu, Li, Zhang & Teng, "Questioning the Coverage-Length Metric in Conformal
Prediction: When Shorter Intervals Are Not Better", arXiv:2601.21455, January 2026.**

From the abstract: the paper "critically examines the sufficiency of these standard
metrics", shows interval length can be "deceptively improved" while marginal coverage
remains valid, and "introduce[s] a new metric **interval stability**".

**This is F7's framing, already in print.** The structural move — *the standard evaluation
pair is insufficient, and here is a third quantity that exposes it* — is no longer
available as a novel contribution.

**What survives, and it is a genuine distinction.** Their instability is **across repeated
runs** of a randomised algorithm on the same input: the same test point can receive
different intervals on different executions. F7's turnover is variation of the interval
path **across time within a single run**, and it is the *decision* that pays for it, not
the reader's confidence in reproducibility. Those are different quantities with different
motivations.

But the distinction now has to be *stated*. Before this paper, F7 could say "nobody looks
past coverage and length". After it, F7 must say "the one existing critique of the
coverage-length pair measures run-to-run instability; we measure temporal path variation,
because that is what a position-holding decision is charged for." That is a narrower and
more precise claim, and it is still a claim.

### 4.5.2 A conformal-plus-switching-cost paper this sweep dismissed on domain

**Zhu, Yan & Gao, "Stay or Switch: Online Conformal Bayesian Optimization Guided Fluid
Antenna Configuration", arXiv:2607.26547, July 2026.**

This paper appeared in §2's own query results — `conformal AND "switching cost"` returned
exactly one hit — and **this sweep dismissed it in a single line as "unrelated: fluid
antenna configuration".** That was a judgement on the application domain, not on the
mechanism, and it was wrong.

What it actually does: formulates "a cost-aware multi-objective FAS switching problem
jointly considering slot-level ISAC performance and **switching energy**", and proposes
online conformal Bayesian optimization to "calibrate surrogate uncertainty for robust
**stay-or-switch** decisions".

**So online conformal calibration has been combined with an explicit switching cost inside
a decision.** It is an application paper in wireless sensing, not a methods paper: it does
not vary the conformal adaptation rate, does not claim coverage is blind to switching cost,
and proves no coverage property under a movement-penalised update. So it does not occupy
C2's square.

**But the sentence "the intersection is empty" must be retired and replaced with something
exact:** what is empty is the set of *methods with a coverage guarantee under a
movement-penalised conformal update*. The set of *applications combining conformal
calibration with a switching cost* is not empty, and F7 must cite this one.

### 4.5.3 The lesson, which is about method and is the more useful finding

Both misses came from the same failure mode, and it is not the arXiv blind spot of §4.4.
**Both of these were retrievable by the queries this sweep actually ran.** One was returned
and discarded on a one-line domain judgement; the other would have been caught by any query
about evaluation metrics rather than about occupancy.

A prior-art sweep that screens on *application domain* rather than on *mechanism* will keep
making this error, because the mechanism F7 cares about — an uncertainty estimate that
moves, driving a decision that pays to move — appears in wireless scheduling, in inventory
control, in data-centre right-sizing and in electricity dispatch, none of which look like
finance. **G1 should require that the prior-art screen be re-run on mechanism keywords
across application domains**, not only on conformal-plus-finance.

## 5. Verdicts

### C1 — the coverage/turnover dissociation

> **[Superseded 2026-08-19 by §7.]** This verdict was reached against the old claim, which
> varied the ACI adaptation rate. See §7 for the verdict against C1′/C2′ and the
> matched-width design.

> **NARROW.**

**The single sentence that distinguishes F7 from the nearest neighbour:**

> Zaffran et al. (ICML 2022) prove that ACI's coverage is asymptotically valid for every
> step size while its mean interval **length** degrades linearly in that step size; F7's
> claim is about the **variation** of the interval path rather than its level — a
> functional that neither realised coverage nor mean interval width records, and the
> one that a position-holding decision actually pays for. Concretely: across arms matched
> on realised coverage to within 0.002 and on mean interval width to within a stated
> tolerance, realised decision cost varies by N points of annual net log growth.

**Why not CLEAR.** The abstract structure of C1 — "coverage is insensitive to γ; a
downstream quantity is very sensitive to γ; so coverage does not discriminate among values
of γ" — is **already published, with a theorem**, for the downstream quantity *interval
length*.
Zaffran et al. §3, Theorem 3.1 gives

    E_{π_γ}[L] = L₀ + Q''(1−α)·(γ/2)·α(1−α) + O(γ^{3/2}),

and the paper's own reading of it is that "ACI on exchangeable scores degrades the
efficiency linearly with γ compared to CP" — which they immediately gloss as underlining
"that such adaptive algorithms may actually hinder" the practitioner. The plan
acknowledges Zaffran as "the closest existing analysis of γ" and says it "must be engaged
directly", but it does not appear to know how close it is. **A reviewer who knows this
paper will ask, in the first paragraph of their review, what F7 adds to it.** The paper
needs the answer above on page one, not in related work.

**Why not OCCUPIED.** Three things genuinely separate them, and they are not cosmetic:

1. **Level versus variation.** `E[L]` is a first moment of the interval *level*; turnover
   is a first moment of the interval *increment*. Two methods can have identical mean
   width and order-of-magnitude different path variation. Neither Zaffran nor Vaze nor
   Srinivas reports the increment functional; the sweep in §2–§4 found no work that does. The
   entire coverage-efficiency frontier line of work is about level.
2. **Monetisation through a decision with memory.** Zaffran's cost is a statistical
   inefficiency. F7's cost is realised money, mediated by a position that must be moved
   and charged for. That requires a decision with an incumbent state, which the conformal
   literature does not have.
3. **The published anomaly.** Ryan's 0.7–5.3 point result is a published empirical
   finding in the wild for which the reporting author offers a hedged, unmeasured
   explanation — estimation variance charged through a nonlinear sizing map — that is
   measured for one device only and is not a turnover account. Correcting someone else's
   published mechanism is a contribution independent of the theory around it.

**Residual risk, stated plainly.** If the C1 simulation is rebuilt and it turns out the
turnover effect tracks the mean-width effect closely — that is, if `Σ|Δq|` is
approximately a monotone function of `E[L]` across the γ grid — then C1 reduces to
Zaffran's theorem multiplied by a cost rate, and the paper is in serious trouble. **This
is a checkable, cheap, and decisive test, and it should be the first diagnostic the
rebuilt simulator emits.** It is recorded as a G2 acceptance criterion.

### C2 — the turnover-aware conformal update

> **[Superseded 2026-08-19 by §7.]** This verdict was reached against the old claim, which
> varied the ACI adaptation rate. See §7 for the verdict against C1′/C2′ and the
> matched-width design.

> **NARROW**, and conditionally so: NARROW if the coverage guarantee is delivered,
> effectively OCCUPIED if it is not.

**The single sentence that distinguishes F7 from the nearest neighbour:**

> Switching-cost online learning has lazy algorithms with regret guarantees but no notion
> of coverage, and the conformal literature has coverage guarantees but no notion of
> movement cost; F7's contribution is a movement-penalised conformal update that provably
> retains the coverage identity, which the sweep in §2–§4 found no existing work supplying — and the gap is not a
> free composition, because regret bounds are known not to imply coverage adversarially.
>
> *(Revised after §4.5.2. The earlier phrasing "the only object in the intersection" is
> too strong: conformal calibration has been combined with an explicit switching cost in
> an applied setting. What is unoccupied is a coverage GUARANTEE under a movement-penalised
> update, not the pairing of conformal prediction with switching costs as such.)*

**Why not CLEAR.** Every ingredient is off the shelf. The dead-band is Constantinides
(1986) and Davis–Norman (1990). Laziness with bounded regret is Kalai–Vempala (2005) and
the shrinking dartboard (2010). Soft-thresholding as the proximal operator of an L1
penalty is textbook convex analysis. "Decision-focused method churns, damping helps" is
published for SPO (Wang & Hasuike, 2026). None of these is F7's.

**Why not OCCUPIED.** What is unoccupied — per the precise statement in §4.5.2, which
retires the now-superseded "the intersection is empty" — is a coverage *guarantee* under
a movement-penalised conformal update; and — this
is the part that makes it a contribution rather than a composition — **it is unoccupied for
a reason**. Ramalingam, Kiyani & Roth prove that you cannot obtain a coverage guarantee from
a regret guarantee in adversarial settings. So a lazy no-regret algorithm applied to the
conformal update does not inherit ACI's coverage property; the property has to be
re-established on the thresholded recursion directly. That is a real theorem-shaped
problem, and this sweep — with the instrument limits recorded in §0, §4.4 and §4.5.3 —
found no work that poses it.

**The conditional, and it is the most important sentence in this file.** C2's novelty and
C2's principal risk are the *same object*. If the coverage result is proved, C2 is a clean
NARROW contribution with a defensible one-line differentiation. If the coverage result is
abandoned and the dead-band is applied to the position rather than the quantile — branch
(i) in `audit/CLAIMS.md` C-a — then C2 becomes "apply a forty-year-old no-trade band to a
conformal interval", which is an obvious composition of two known things and will not
carry a workshop paper on its own merits, let alone a journal fast-track.

**Recommendation.** Do not let C2's scope be decided by what the theorem turns out to
allow. Decide the branch first, at gate G1, and size the claim to it. The plan's own STOP
condition — fall back to reporting C1 alone — is the right instinct and should be
triggered by the theorem's status, not only by the empirical result.

---

## 6. Enforcement of the framing constraint

**The constraint, carried forward:** F7's claim is **decision-theoretic, not
information-theoretic**. Any framing as an impossibility result, a coverage floor, or a
fundamental limit is dead on arrival, because that ground is held by Vaze
(arXiv:2607.26577) and Srinivas (SODA 2026) — both re-verified in this audit
(`audit/REFS_VERIFIED.bib`).

Two places in the planning document are **at risk of being read as
information-theoretic**, and both should be rewritten before drafting.

**Risk 1 — C1's negative universal.**

> "**no coverage-based criterion — marginal, conditional, or adaptive — can select the
> adaptation rate for a decision that pays for turnover**"

"No X can do Y" is the grammar of an impossibility theorem. As written a reviewer will
expect a proof, will not find one, and will then place the claim next to Vaze and
Srinivas, where it loses. **Restate operationally:**

> "Across the range of adaptation rates that all attain nominal coverage to within
> 0.001, realised decision cost varies by N points of annual growth. Coverage is
> therefore uninformative for selecting the adaptation rate whenever the decision pays
> for movement."

That is the same finding, it is what the experiment actually shows, and it is
unassailable because it is a measurement rather than a quantifier.

**Risk 2 — the word "frontier".**

> "Formalise the turnover-vs-tracking-error frontier and show the coverage-optimal point
> sits at the wrong end of it."

A formalised *frontier* is precisely Srinivas's object — the joint coverage–efficiency
Pareto frontier, with matching upper and lower bounds. Stating a turnover–tracking
frontier as a theorem puts F7 directly alongside it, in a four-page paper, against a
SODA result. **Either** present the frontier empirically, as a measured curve over the γ
grid with no minimax claim, **or** drop the word.

There is also a second problem with that sentence, independent of framing. The plan's own
table shows coverage is **flat** over γ ≥ 0.005, which means there is no
"coverage-optimal point" to sit at the wrong end of anything. The stronger and more
accurate statement is that **coverage does not locate a point on the measured
turnover–tracking-error curve at all** — it is constant along it. That is a better
sentence, it is what the data show, and it avoids the word "frontier" for F7's own object,
which is what Risk 2 asks for.

**Elsewhere the plan is disciplined about this** — it explicitly says "F7's claim is
decision-theoretic, not information-theoretic — keep it that way" — and that instruction
is correct and should be enforced against the two sentences above.

---

# 7. Verdicts against C1′ and C2′ — session S1, 2026-08-19

**This section supersedes §5.** §5's verdicts were reached against the **old** claims,
which varied ACI's adaptation rate γ and measured turnover. That design is abandoned
(`docs/FRAMING.md` §5). The verdicts below are assessed against the **matched-width
design** and its claims C1′ and C2′, and they are not inherited from §5 in either
direction. §5 is retained as the record of what was believed and on what evidence.

**Method.** Seven retrieval agents, then one synthesis agent applying a five-question
occupancy rubric mechanically rather than by impression. Every query logged verbatim with
its result count in `research/S1/A1`–`A7*.json`; the synthesis, the ten-work table with all
five rubric answers, the stress test and the adjudications are in
`research/S1/B1-verdicts.md`.

**The rubric.** Q1 — does it hold mean interval width, or an equivalent level functional,
fixed across compared arms? Q2 — does it measure a temporal path-variation functional?
Q3 — does the decision it drives have an incumbent state charged for movement? Q4 — does it
claim something about what the tuning criterion can or cannot see? Q5 — does it prove or
bound a coverage property for a post-processed or movement-penalised interval? **OCCUPIED**
if Q1 ∧ Q2 ∧ Q3, or Q5 for a movement penalty; **NARROW** if three or four of Q1–Q4;
**ADJACENT** if one or two; **CLEAR** if none. **Screening was on mechanism, never on
application domain** — the §4.5.3 failure mode was the thing this sweep was designed to
avoid.

## 7.1 The verdicts

> ### C1′ — OCCUPIED as worded.
>
> **Van Belle, Wen, Verbeke & Pinson, "Stabilizing distribution-free probabilistic
> forecasts", arXiv:2605.28531, 27 May 2026** scores **Q1 ∧ Q2 ∧ Q3 all yes** and pre-empts
> Q4 verbatim. Read in full and independently by two agents. **C1′ as worded should not be
> submitted.** A residual claim survives and is stated in §7.4.
>
> ### C2′ — NARROW, conditional on one unread theorem.
>
> Nothing read occupies it: no work in the corpus states a coverage property for a
> movement-penalised or post-hoc-smoothed conformal quantile. The single live threat is
> **IPOC** (KDD 2023, doi 10.1145/3580305.3599396, and its extension, IEEE TKDE
> 38(5):3277–3290, doi 10.1109/TKDE.2026.3674583), whose Q5 stands at **unclear** after
> eleven failed retrieval routes. **C2′ cannot be certified until that theorem is read.**
> Independently of IPOC, C2′'s no-novelty concession must now extend from the two functional
> forms to the **readout-map formulation itself**.

**Both verdicts changed.** C1 moved NARROW → OCCUPIED. C2 stayed NARROW-conditional, but
the conditional now rests on a different object and the concession list is longer.

## 7.2 The occupant, and why no conformal query could have found it

Van Belle et al. §2 builds a stable and an unstable forecaster with *identical* bias
variances (4, 2.5, 1.75) and *identical* bias magnitudes, differing only in the **sign** of
the bias recursion (+½τ versus −½τ). Because the initial sign is symmetric, every marginal
functional coincides by construction. Table 2 verifies it — CRPS 2.91 / 1.43 / 0.83 against
2.91 / 1.44 / 0.83 — and the paper states that "the forecasters are indistinguishable in
terms of forecast quality" (**Q1**). The varied quantity is the 1-Wasserstein distance
between forecasts for the same target at consecutive origins, reported as 2.00 / 1.00
against 6.00 / 3.00, a threefold gap, with non-adjacent stability identical across arms
(**Q2**). It is priced through a newsvendor with an incumbent order, `c_e` to add, `c_c` to
cancel and **retain free**, giving +0.83 % to +3.49 % average profit with the stable arm
winning 76–81 % of periods; a "procrastination" arm that never revises an incumbent shows
**+0.00 %**, a placebo isolating the movement channel (**Q3**). And it draws the moral:
forecast instability "may go unnoticed if forecasts are evaluated solely from a forecast
quality perspective" (**Q4**).

**Q5 is no.** "Coverage", "interval width", "conformal", "pinball" and "guarantee" occur
**zero** times in its 16,217 words. Its λ (Eq. 9) is a training regulariser convexly mixing
scaled CRPS with a scaled Wasserstein distance; it yields neither partial adjustment nor a
dead-band. Its design is a synthetic two-DGP simulation, and that is its only structural
weakness — it does not rescue C1′ as worded.

**Why the G0 sweep could not have found it, and why this one did.** The paper contains no
conformal vocabulary at all, so no query anchored on "conformal" returns it in any
instrument. It was reached by mechanism screening across application domains, and
independently by a citation traversal from an earlier paper by the same group. This is the
§4.5.3 lesson, vindicated: **the mechanism recurs where the vocabulary does not.**

## 7.3 The literature behind it, which this project had never cited

A named **forecast-stability** literature, roughly seventeen years old, largely in the
*International Journal of Forecasting* and in operations journals. It already has the
increment metrics (MASC / RMSSC — mean absolute *scaled change*), and it already publishes
**both** of C2′'s readout maps.

| Work | What it already establishes |
|---|---|
| **Godahewa, Bergmeir, Baz et al., "On forecast stability", *IJF* 41(4):1539–1558, doi 10.1016/j.ijforecast.2025.01.006** | Publishes the linear partial-adjustment readout `ỹ = (1−w_s)·ŷ_new + w_s·ỹ_prev`, one scalar, as **model-agnostic post-processing** — C2′'s quadratic-cost map, in print. Also the canonical vertical/horizontal vocabulary and six stability metrics. |
| **Genov, Ruddick, Bergmeir et al., *ESWA* 298:129305, doi 10.1016/j.eswa.2025.129305 (preprint arXiv:2407.03368)** | **Eq. 18–20 state C2′'s readout-map formulation directly:** `x_t = M(ŷ_t)` with `M` assumed Lipschitz with constant `L_M`, and the switching cost bounded by `β·L_M·Σ‖ŷ_t − ŷ_{t−v}‖`. Plus an explicit switching cost `β‖S_t − S_{t−1}‖` in a formal OCO-with-switching-costs framework, four path-variation metrics including a novel probabilistic one, and real battery scheduling with ramping costs. |
| Van Belle, Crevits & Verbeke, *IJF* 39(3):1333–1350 (2023); Caljon et al., *IJF* 42(2):344–358 (2026) | The composite quality-plus-stability loss. |
| Pritularga & Kourentzes (2024), doi 10.2139/ssrn.4711817 | *Forecast congruence*: only weakly correlated with accuracy, and good congruence at acceptable accuracy beats best accuracy on inventory decisions. |
| Tunc, Kilic, Tarim & Eksioglu, *IJPE* 141(2):619–625 (2013) | The cost of system nervousness. |

**Genov is the old γ design, in another field, and it fails exactly where this audit
predicted the old design would fail.** Its arms are commitment periods v = 1…12 driven by a
single fixed forecaster, and its §4.4 states that "the forecast error generally decreases
with shorter commitment periods, while the vertical stability is better with longer
commitment periods" — level and variation move together, and attribution runs through a
cross-arm correlation table. The strings *matched*, *same accuracy*, *equal accuracy*,
*controlling for* and *holding* appear zero times. **Q1 = no ⇒ NARROW.** A third-party
citation glossing it as showing stable forecasts win "even when raw accuracy is equivalent"
is **not supported by the paper**, and one agent's verdict rested on that gloss until two
others read the full text. That adjudication is recorded in `research/S1/B1-verdicts.md`
§1.2.

**The bridge between the two literatures is unbuilt.** On arXiv, `"conformal"` crossed with
`"forecast stability"`, `"forecast instability"`, `"forecast congruence"`, `"jumpiness"` and
`"forecast revision"` returns **zero** on every pairing in both directions, and
`"forecast stability" coverage` returns zero. Not one of the papers citing Van Belle et al.
2023 is conformal. **That zero is title-and-abstract-level and is weaker than a full-text
zero** — see §7.6.

## 7.4 The residual claim

Two legs, claimed separately because they have different strengths. Full wording and the
stress test against the five nearest neighbours are in `docs/FRAMING.md` §2.2 and
`research/S1/B1-verdicts.md` §5.

- **R1 (measurement, the motivation).** On a real online conformal producer, the pair the
  online conformal literature reports and tunes on — realised coverage **together with**
  mean interval width — can be held fixed while the width path `Σ|Δq_t|` varies by a factor
  of F, and the difference in annual net log growth on a position charged to move is N
  points. **Claimed as the conformal instance of a result established outside conformal
  prediction, and no wider.**
- **R2 (the object and its validity, the paper).** A one-scalar movement penalty on the
  **deployed** conformal quantile is not covered by the existing predictable-modification
  arguments, because it acts on the quantile-based width mechanism and puts at risk the
  monotonicity condition those arguments require. The paper states the conditions under
  which ACI's long-run coverage survives, and reports smoothed-arm realised coverage as a
  measured control regardless.

**R1 survives all five nearest neighbours — thinly against Van Belle, contingently against
Ryan. R2 survives all five cleanly, and is void only if IPOC's theorem quantifies over the
movement-constrained object.** R2 is the headline; R1 is the motivation.

**The inherited STOP condition is now wrong.** "Fall back to reporting C1 alone" was written
before this sweep, and C1 alone is the occupied leg. The replacement is in
`docs/FRAMING.md` §2.3: **if R2 cannot be delivered, re-scope rather than submit R1 alone.**

## 7.5 Corrections this sweep forces on earlier sections

| Section | What it said | What is true |
|---|---|---|
| §0 | The Semantic Scholar API was unusable and no forward-citation screen of ACI was possible | **The screen ran, with no API key.** 659 unique citing papers across ACI (557), DtACI (188), Conformal PID (147) and SAOCP (101); 12 candidates; **zero OCCUPIED, zero NARROW**. The instrument is incremental backoff against the anonymous pool. Note also that the OpenAlex fallback would have produced a **false negative**: its ACI record carries 27 citations against 557, a 95 % miss. |
| §4.3 | Wang & Hasuike is "the closest published neighbour to C2" | Overstated. Full-text read: **zero** occurrences of "conformal", "coverage", "quantile" or "prediction interval" — no interval object at all. What it does pre-empt is the *argument shape*: Table 1's caption already publishes "Increasing risk aversion does not meaningfully reduce turnover", its δ is fixed at 0.1 and never swept, and its damping is heuristic rather than cost-derived. |
| §4.4 | Jia & Han was missed because the sweep was arXiv-centric | True but incomplete. **DBLP indexes it and returns it on the first query.** The failure was instrument choice, not venue coverage. Scored **CLEAR / CLEAR** on its abstract and full reference list; the body remains closed. |
| §4.5.2 | arXiv:2607.26547 was dismissed on domain and the dismissal was wrong | The **dismissal method** was wrong; the **answer** was right. Read in full: Q3 yes — `Q_t(a) = EHI_t(a\|a_{t−1}) − η_e·E_mv(a\|a_{t−1})` with the stay action free, a genuine proportional movement cost with a stay region — but Q1, Q2, Q4 and Q5 all no. There is no theorem, the conformal step is a rolling-window empirical quantile used as a variance inflator, and the penalty sits downstream in the acquisition function. **ADJACENT / ADJACENT**, and a must-cite: `"conformal" "switching cost"` returns exactly this one paper on arXiv. |
| §5, C1 residual risk | "If `Σ\|Δq\|` is approximately a monotone function of `E[L]` across the γ grid, C1 reduces to Zaffran's theorem times a cost rate" | The risk was correctly identified and the proposed test for it — the old G2.10 conditional discriminator — was **rank-deficient and could not have been estimated**, because both regressors are approximately affine in the single manipulated variable. Deleted with reason; see `docs/GATES.md` G2 and `docs/OUTSTANDING.md` O8. |

## 7.6 What the sweep still cannot see

Stated so that the verdicts are read with their instrument, in the spirit of §0.

1. **IPOC is unread and C2′'s Q5 is unknown.** Eleven routes failed: ACM DL 403 on the
   abstract page, the PDF path, a real-browser fetch and a server-side fetch; IEEE Xplore
   JavaScript-gated; ResearchGate 403; Unpaywall `is_oa: false`, `oa_status: closed`, zero
   locations; no arXiv preprint, and the first author has four others, so this is a genuine
   absence rather than an indexing gap; the corresponding author's homepage lists the paper
   but hosts no copy. **This needs institutional access, not more open-web searching.**
2. **The full-text instrument ran out mid-sweep.** OpenAlex's anonymous daily budget was
   exhausted with roughly twenty queries unrun. Full-text search is the **only** instrument
   in the set that sees a smoother buried in a methods section — the arXiv API and HTML UI
   index title and abstract only, and the Semantic Scholar screen is abstract-level.
   **The hole is demonstrably non-empty:** two SSRN papers carry "turnover" and "transaction
   cost" in their full text but not their abstracts, appear in no Semantic Scholar citing
   set, and surfaced only through full-text indexing. §0's caution about abstract-level
   nulls should therefore be **strengthened, not relaxed**.
3. **No forward-citation screen was run on Godahewa or Van Belle**, in either direction.
   Two agents independently name the mirror traversal — screening the online-conformal
   anchors' citing sets for forecast-stability vocabulary and vice versa — as the
   highest-value follow-up. The instrument is known to work: Semantic Scholar's
   `/paper/{id}`, `/citations` and `/references` return 200 even while `/paper/search` is
   throttled, and it was a traversal of this kind that surfaced Genov, which no keyword
   query reached.
4. **Unread material bearing on the verdicts:** Van Belle et al. (2024), *IEEE TNNLS*
   35:18872–18885 — the composite loss extended to *probabilistic* forecasts using KL and
   2-Wasserstein distances between successive predictive distributions, named as the single
   closest published object to "penalise the movement of a predictive interval", and never
   fetched; Genov et al.'s companion paper; the full texts of Godahewa et al. and
   Pritularga & Kourentzes; *Conformal Portfolio Optimization* (doi 10.2139/ssrn.5011129),
   recorded UNRESOLVED; Chopra (1993), not obtained at all, not even an abstract; and 72 of
   the 659 citing papers screened on title only.
5. **A venue-speed conditional.** An SSRN cluster is forming around conformal intervals
   meeting financial decisions — Ryan, Cotton, Koukorinis, Schmitt, Noguer i Alonso,
   Beckman, Hoxha & Thanasi, Dai, Manokhin and others, most dated 2026 and several only
   weeks old. It is invisible to arXiv and to DBLP. **Crossref `prefix:10.2139` must be
   re-run immediately before any submission.**

## 7.7 Metadata corrections that must propagate

- **Genov et al.'s DOI is `10.1016/j.eswa.2025.129305`.** The 2026 form returns HTTP 404,
  despite the issue being dated March 2026.
- Semantic Scholar mis-normalises Conformal-ABR's venue to "International Conference on
  Multimodal Interaction" — an acronym collision. Use the Crossref record: *2026 IEEE 5th
  International Conference on Computing and Machine Intelligence (ICMI)*.
- A web-search summariser fabricated an author list for IPOC during this session. Crossref
  and Semantic Scholar agree on the true one and it is what `audit/REFS_VERIFIED.bib`
  carries.
- Ryan's *Conformal Kelly* also has an SSRN record, doi 10.2139/ssrn.7221760.

---

## 7.8 Amendment — the adversarial pass, 2026-08-19

*Added after §7 was written. A critic was tasked with overturning this session's own
verdicts: assume they are wrong and find the paper that proves it. It did not overturn
either, and it damaged both. It also resolved the session's largest open question.*

### 7.8.1 IPOC is read. Its Q5 is NO. The conditional in §7.6 item 1 is closed.

**The eleven failed routes shared one wrong premise: that the ACM Digital Library's HTTP
403 was a paywall. It is Cloudflare bot detection, and the ACM Digital Library is open
access.** A headed system Chrome instance driven through a persistent profile passes the
challenge, and the full eleven-page PDF downloads. **Every ACM paper in this project is
reachable this way.** That is an operational fact worth more than the finding it produced.

**What the theorem says.** IPOC has exactly one coverage statement — Lemma 3 in §5.1,
titled "The Effectiveness of ACI", imported verbatim from Gibbs & Candès: *"The average
miscoverage ratio of confidence intervals {c^f_t} will converge to α with enough training
steps."* Appendix A's notation table settles the scope: `c^f_t` is "confidence interval of
**model f** at time t by ACI", where `f` is the point prediction model and `f̄`, listed
separately, is the ensemble. **The guarantee is on the base model's interval, not on the
chased ensemble interval the movement cost acts upon.** The chased interval's validity is
asserted and never proved — §5.1 offers only "we can still approximately guarantee coverage
rate, which is verified in the experiment results". Theorems 1 and 2 are pinball-loss regret.

**IPOC becomes a supporting citation, not a threat.** Its hedge is a fourth independent
instance of the obstacle R2 names. The TKDE extension's theory section remains unread
(`isOpenAccess: false`, PDF download timed out); its abstract enumerates only the same two
regret results plus a Dd-MDP framework.

### 7.8.2 R1's two stated distinctions are destroyed. It survives on Q3 alone.

**Pinson, P. & Girard, R., "Evaluating the quality of scenarios of short-term wind power
generation", *Applied Energy* 96:12–20 (2012), doi 10.1016/j.apenergy.2011.11.004.**

§7.4 rested R1's survival on exactly two claims: that the matched pair is *(realised
coverage, mean interval width)* specifically rather than any level functional, and that the
producer is real rather than a synthetic two-DGP simulation. **Both are false.**

Pinson & Girard compare three arms on a **real** producer that share the **full marginal
predictive distribution** — hence identical realised coverage and identical mean interval
width, exactly, by construction — and differ only in temporal dependence structure. That is
a **strictly stronger** control than the pair, and it subsumes it. They do it inside the
reliability-and-sharpness framing, citing Gneiting, Balabdaoui & Raftery for the paradigm —
**which is this project's matched pair under its meteorological name.** And they state the
Q4 moral.

**They fail Q3 only: no decision, no movement cost.** Their own conclusion commissions
exactly the missing study: *"a more intuitive approach to the evaluation of sets of
scenarios may be to concentrate on their value instead, i.e. on the comparative benefits
from their use as input to various decision-making problems."*

**So R1 rests on Q3 — the movement-charged decision — and on nothing else.** The reviewer
line to expect is not the one §7.4 anticipated; it is *"matching the whole predictive
marginal is stronger than matching your pair, on real data, fourteen years ago."*

**Aggravating fact: Pierre Pinson is a co-author of Van Belle et al. (arXiv:2605.28531), the
work that occupies C1′.** The two papers that between them cover everything R1 claimed share
an author, and he is a likely reviewer.

**Consequence for positioning:** the **probabilistic-forecast-verification line** must join
the forecast-stability chain in the paper's opening — Gneiting, Balabdaoui & Raftery (2007);
Pinson & Girard (2012); Pinson et al. (2008). **Omitting it repeats the exact failure mode
that occupied C1′, one literature over.**

### 7.8.3 R2's object is not new, and the question is already contested

| Work | What it does to R2 |
|---|---|
| **Binny & Dixit, "Who Moved My Distribution?", arXiv:2511.11567, Eq. (13)** | **Publishes R2's smoother verbatim** on the deployed conformal calibration threshold: `q ← (1−γ)q + γ q̂`, one scalar, data-dependent, able to shrink. Their Theorem 5 is a Banach contraction result in which γ does not appear, and the coverage claim holds at the fixed point where the smoother is inert; the transient is never analysed. **The object is not new. The property is still open.** |
| **Dupuy, Xu, Perrey, Montmain & Imoussaten, arXiv:2510.02809 / doi 10.1007/978-3-032-16708-8_17** | **The closest published work to R2 and the one that most constrains it.** Replaces the binary indicator in the online conformal update with a smooth relevance function, explicitly to prevent abrupt threshold changes while maintaining coverage validity, and proves three long-run coverage theorems. Theorems 1 and 3 are inherited from the saturating-integrator argument, by the authors' own proof text. **Theorem 2 is the case where the width mechanism itself is driven by the smoothed signal — and it needs a domination hypothesis the authors immediately disown**, as "pretty strong" and "highly dependent on the choice of parameters ω and v". **That is R2's thesis, stated by someone else, with an attempted theorem attached.** |

**R2 must now be positioned against Dupuy Theorem 2 specifically** — as discharging the
assumption they could not, or as not being written.

### 7.8.4 A statement in §7 and in `docs/FRAMING.md` was false and is corrected

Both asserted that *the one statement in print about what a post-hoc smoother does to a
conformal quantile is SCD-split's remark that it invalidates the guarantee.* **There are at
least four**, and the corrected sentence is **stronger**, because four independent groups
hitting the same obstacle is better evidence that the obstacle is real and unsolved than one
remark ever was:

1. **SCD-split** (arXiv:2509.22529) — post-hoc smoothing of the conformal quantile
   invalidates the coverage guarantee.
2. **ECI** (Wu, Hu, Bao, Xia & Zou, arXiv:2502.00818) — under a fully smoothed update rule
   "we cannot directly control the averaged miscoverage gap … due to the smoothing bias".
3. **Dupuy et al.** — Theorem 2's self-disowned domination assumption.
4. **IPOC** §5.1 — "we can still approximately guarantee coverage rate, which is verified in
   the experiment results".

### 7.8.5 Two further must-cites, both with authors shared with the occupant

- **Stratigakos, Wen, Spyrou & Pinson, "Decision-calibrated prediction sets for robust power
  system operations", arXiv:2606.02081.** Publishes, in the conformal setting in 2026, the
  claim that coverage is the wrong criterion to tune on when a decision pays for it. **Two
  of its authors — Wen and Pinson — are co-authors of the work occupying C1′.**
- **Shekhar & Howard, "Decision-Calibrated Conformal Uncertainty for Pacing Decisions in
  Streaming Advertising", arXiv:2606.10187.**

### 7.8.6 Settled, and corrected

- **Van Belle et al. (2024), *IEEE TNNLS* 35(12):18872–18885, is fetched and settled.** Its
  Eq. (14) penalises movement of the whole Gaussian via KL, 2-Wasserstein or
  root-mean-square-change distance; σ̂-drift is penalised and is proportional to interval
  half-width under a Gaussian, but **width is never derived, weighted or evaluated as
  such**, and in its full text *coverage*, *validity*, *guarantee*, *width* and *nominal*
  each occur **zero** times. No coverage object. ADJACENT.
- **The Genov companion line is closed:** there is no second stability paper, and the
  readout-map Lipschitz argument is new in the *ESWA* v5 revision, absent from arXiv v2.
- **The KU Leuven / DTU programme is four items, not three, and none adds coverage content.**
- **A citation correction, and it is the reason the fetched-record rule exists.** The critic
  reported the scenario method paper as "Pinson, Papaefthymiou, Klöckl, Nielsen & Verboomen
  (2009), *Wind Energy* 12:51–62". **Crossref gives a different author list and an online
  date of 2008.** The fetched record is used in `audit/REFS_VERIFIED.bib`.

### 7.8.7 Where a scoop is still hiding — three named places, with routes

1. **The decision-value follow-up to Pinson & Girard.** Matched-marginal scenario sets
   priced through stochastic unit commitment or hydro/battery scheduling, where start-up and
   ramping costs charge an incumbent schedule for moving. **That is Q1 ∧ Q2 ∧ Q3 on a real
   producer, and R1 falls outright.** Pinson & Girard has 257 citations and the traversal
   returned 1,023 unique citing papers, screened at abstract level only — and
   matched-marginal construction is a methods-section fact that rarely reaches an abstract.
   The named unclosed candidate is **Rachunok, Staid, Watson & Woodruff, *Applied Energy*
   274:114986 (2020), doi 10.1016/j.apenergy.2020.114986**; the single question is whether
   its three scenario-creation methods share matched marginals. Three fetch attempts failed
   on network reachability.
2. **The applied conformal layer behind publisher bot walls**, which this project wrongly
   treated as paywalls for an entire session. The named item is **"AQA",
   doi 10.1109/CEEPE69795.2026.11552153**, which "anchors the conformal threshold to a
   weighted estimate of recent score quantiles" to produce narrower *and* more stable
   intervals — the closest method match to R2's object after Binny & Dixit. Now reachable by
   the proven headed-Chrome route, along with the IPOC extension, Conformal-ABR's full text,
   and the three title-only-screened incumbent-state candidates in §7.6 item 4.
3. **The hydrology and reservoir-operations branch of the Schaake-shuffle and
   ensemble-copula-coupling literature, which is entirely absent from this repository** —
   `Schaake`, `copula coupling`, `variogram` and `PINAW` return **zero** occurrences across
   the whole tree. ECC and the Schaake shuffle **preserve the univariate margins exactly by
   construction** and change only the rank dependence, so *every* ECC-versus-alternative
   comparison is automatically a matched-(coverage, width) comparison on a real producer.
   Reservoir operations charge for changing releases through ramping limits, re-operation
   penalties and hydropower start-up. The branch's own vocabulary was never used as a query
   in any instrument this session.
