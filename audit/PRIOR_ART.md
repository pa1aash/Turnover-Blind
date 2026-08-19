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
| Semantic Scholar API | HTTP 429 throughout the session, on both the direct API and the connected server | **No forward-citation screen of Gibbs–Candès ACI was possible.** This is the single biggest gap in this sweep and it is exactly the screen the plan's prior sweep claims to have run over 100 titles. |
| OpenAlex | HTTP 429 on most calls; the one ACI record it returned carries 27 citations, which is obviously incomplete | Not usable as a citation-graph substitute. |
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
  identifier in a trailing clause. See §4 — it is the closest published neighbour to C2.
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

**The forward-citation screen of ACI could not be run** (§0). This is the one query most
likely to surface a paper that does the F7 experiment inside a larger applied study
without advertising it in the abstract. **It must be run before gate G1 is signed**, from
a machine with a Semantic Scholar API key. Recorded in `docs/OUTSTANDING.md`.

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

### 4.3 The closest published neighbour to C2, and it is in the plan's own reference list

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
update. It is the single most important comparison in the paper and the plan gives it a
parenthesis.

**It is also a partial scoop of the framing**, not of the result: "decision-focused
methods churn, and damping helps" is now published. F7's distinct contribution has to be
(a) that the churn is caused by the *adaptation rate*, (b) that the *coverage criterion is
blind to it*, and (c) that the damping can be made *coverage-preserving*. Points (b) and
(c) are unoccupied. Point (a) is adjacent to occupied.

---

## 5. Verdicts

### C1 — the coverage/turnover dissociation

> **NARROW.**

**The single sentence that distinguishes F7 from the nearest neighbour:**

> Zaffran et al. (ICML 2022) prove that ACI's coverage is asymptotically valid for every
> step size while its mean interval **length** degrades linearly in that step size; F7's
> claim is about the **variation** of the interval path rather than its level — a
> functional that no coverage-based and no efficiency-based criterion measures, and the
> one that a position-holding decision actually pays for.

**Why not CLEAR.** The abstract structure of C1 — "coverage is insensitive to γ; a
downstream quantity is very sensitive to γ; therefore coverage cannot tune γ" — is
**already published, with a theorem**, for the downstream quantity *interval length*.
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
   width and order-of-magnitude different path variation. Nothing in the conformal
   literature — Zaffran, Vaze, Srinivas included — measures the increment functional. The
   entire coverage-efficiency frontier line of work is about level.
2. **Monetisation through a decision with memory.** Zaffran's cost is a statistical
   inefficiency. F7's cost is realised money, mediated by a position that must be moved
   and charged for. That requires a decision with an incumbent state, which the conformal
   literature does not have.
3. **The published anomaly.** Ryan's 0.7–5.3 point result is an unexplained empirical
   finding in the wild, and no explanation exists for it. Explaining someone else's
   anomaly is a contribution independent of the theory around it.

**Residual risk, stated plainly.** If the C1 simulation is rebuilt and it turns out the
turnover effect tracks the mean-width effect closely — that is, if `Σ|Δq|` is
approximately a monotone function of `E[L]` across the γ grid — then C1 reduces to
Zaffran's theorem multiplied by a cost rate, and the paper is in serious trouble. **This
is a checkable, cheap, and decisive test, and it should be the first diagnostic the
rebuilt simulator emits.** It is recorded as a G2 acceptance criterion.

### C2 — the turnover-aware conformal update

> **NARROW**, and conditionally so: NARROW if the coverage guarantee is delivered,
> effectively OCCUPIED if it is not.

**The single sentence that distinguishes F7 from the nearest neighbour:**

> Switching-cost online learning has lazy algorithms with regret guarantees but no notion
> of coverage, and the conformal literature has coverage guarantees but no notion of
> movement cost; F7's contribution is the only object in the intersection — a
> movement-penalised conformal update that provably retains the coverage identity — and
> the intersection is not a free composition, because regret bounds are known not to
> imply coverage adversarially.

**Why not CLEAR.** Every ingredient is off the shelf. The dead-band is Constantinides
(1986) and Davis–Norman (1990). Laziness with bounded regret is Kalai–Vempala (2005) and
the shrinking dartboard (2010). Soft-thresholding as the proximal operator of an L1
penalty is textbook convex analysis. "Decision-focused method churns, damping helps" is
published for SPO (Wang & Hasuike, 2026). None of these is F7's.

**Why not OCCUPIED.** The intersection is genuinely empty, in both directions, and — this
is the part that makes it a contribution rather than a composition — **it is empty for a
reason**. Ramalingam, Kiyani & Roth prove that you cannot obtain a coverage guarantee from
a regret guarantee in adversarial settings. So a lazy no-regret algorithm applied to the
conformal update does not inherit ACI's coverage property; the property has to be
re-established on the thresholded recursion directly. That is a real theorem-shaped
problem, and nobody has solved it because nobody has posed it.

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
accurate statement is that **coverage does not locate a point on the frontier at all** —
it is constant along it. That is a better sentence and it is what the data show.

**Elsewhere the plan is disciplined about this** — it explicitly says "F7's claim is
decision-theoretic, not information-theoretic — keep it that way" — and that instruction
is correct and should be enforced against the two sentences above.
