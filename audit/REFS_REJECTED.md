# Reference audit — failures

Every reference in `docs/PLAN_ORIGINAL.md` was resolved against a record fetched from a
canonical source. Three checks were applied **separately** to each:

- **(i) resolution** — does the identifier, or the author/title/venue triple, resolve to
  a real work?
- **(ii) metadata** — are the authors, title, venue and year correct **as the planning
  document states them**?
- **(iii) attribution** — does the work actually contain the claim the planning document
  attributes to it?

Failures of (iii) are reported first and at length. A real paper cited for something it
does not say is worse than a fabricated citation: a fabricated citation is caught by any
reader who looks it up, whereas a misattributed one survives until a reviewer who knows
the paper reads the sentence.

**arXiv:2608.01494 (Ryan, Conformal Kelly) was not re-verified** — its existence and
abstract content were established externally and passed forward as given.

Corrected entries for everything below are in `audit/REFS_VERIFIED.bib`. A work
appearing here is not necessarily a bad work; the rejection is of the planning
document's citation or use of it.

---

## Summary

| | count |
|---|---|
| Distinct reference entries in the planning document | 22 |
| Entries failing at least one check | **7** |

Failures by check. **These columns sum to more than 7 because one entry fails two checks:**
MacLean–Thorp–Ziemba is both unresolvable as cited (check (i)) and missing its year and
title (check (ii)), and is counted once in the total above.

| Check failed | count |
|---|---|
| (iii) attribution — substantive | 1 (Gârleanu–Pedersen) |
| (iii) attribution — qualified | 1 (Vaze) |
| (ii) metadata | 4 (conformal PID year; conformal risk control author order and missing year; Schmitt method name; MacLean–Thorp–Ziemba missing year and title) |
| (i) unresolvable as cited | 1 (MacLean–Thorp–Ziemba, **also counted under (ii)**) |
| list hygiene — duplicate entry | 1 (arXiv:2502.10947) |
| Entries passing all three checks | 15 |
| **Failure rate** | **7 / 22 = 31.8 %** |

One further entry is flagged as a **caution** rather than a failure (DtACI, §4.1).

---

## 1. Attribution failures — check (iii)

### 1.1 Gârleanu & Pedersen (2013) is not the source of the dead-band form — **SUBSTANTIVE FAILURE**

**What the planning document says.** Twice, and both times load-bearing for C2:

> "yielding a soft-threshold/dead-band update in closed form for a proportional cost
> (the L1 penalty gives shrinkage-to-no-trade, **exactly as in the Gârleanu–Pedersen
> dynamic-trading solution**)"

> "**Gârleanu & Pedersen (2013)** — turnover-penalised dynamic trading, **the source of
> the dead-band form**"

**What the paper says.** Gârleanu, N. and Pedersen, L. H., "Dynamic Trading with
Predictable Returns and Transaction Costs", *The Journal of Finance* 68(6):2309–2340,
2013, doi 10.1111/jofi.12080. Retrieved from the author's copy at
`pages.stern.nyu.edu/~lpederse/papers/DynamicTrading.pdf`.

From the abstract:

> "The optimal strategy is characterized by two principles: (1) **aim in front of the
> target** and (2) **trade partially towards the current aim**. […] the optimal updated
> portfolio is a **linear combination** of the existing portfolio and an 'aim
> portfolio'."

From the related-work discussion, in a sentence written specifically to draw this
distinction:

> "Our trade-toward-the-aim strategy is **qualitatively different from the optimal
> strategy with proportional or fixed transaction costs, which exhibits periods of no
> trading**. Our strategy mimics a trader who is continuously 'floating' limit orders
> close to the mid-quote."

On the cost model:

> "Like Heaton and Lucas (1996) and Grinold (2006), we also rely on **quadratic trading
> costs**."

And Proposition 2 ("Trade Partially Toward the Aim") gives
`x_t = x_{t−1} + Λ⁻¹A_xx (aim_t − x_{t−1})`, a linear update with trading rate `a/λ < 1`.

**Verdict.** The claim is not merely unsupported; it is the exact statement the cited
paper writes a sentence to deny. Gârleanu–Pedersen assume quadratic costs, and quadratic
costs are precisely what produce a smooth partial adjustment *instead of* a no-trade
band. Their strategy trades **every period**. There is no dead-band anywhere in it.

**Probable origin of the error.** The paper's Assumption 1 reads "Transaction costs are
proportional to the amount of risk, Λ = λΣ". The word *proportional* there describes the
cost **matrix** being proportional to the return covariance matrix — it does not mean the
cost is proportional to trade size. Reading that line out of context turns a quadratic
cost into a linear one and a partial adjustment into a band.

**Correct citations, both verified and added to the bib.**

- Constantinides, G. M., "Capital Market Equilibrium with Transaction Costs", *Journal of
  Political Economy* 94(4):842–862, 1986, doi 10.1086/261410 — the no-trade region under
  proportional costs.
- Davis, M. H. A. and Norman, A. R., "Portfolio Selection with Transaction Costs",
  *Mathematics of Operations Research* 15(4):676–713, 1990, doi 10.1287/moor.15.4.676 —
  the no-trade cone.

The soft-threshold form itself needs no finance citation at all: the proximal operator of
the L1 norm is soft-thresholding, which is standard convex analysis.

**Why this matters beyond the citation.** C2's method is specified as an L1 movement
penalty producing a dead-band. That is internally coherent and the mathematics is right.
But it means **C2 cannot claim Gârleanu–Pedersen as its antecedent**, and it also means
the plan has an unexamined design choice: a *quadratic* movement penalty would give
partial adjustment (G–P's actual solution), no dead-band, and — importantly — a smooth,
differentiable update that is far easier to analyse. Whether C2 should use L1 or L2 is a
real methodological question that the mis-citation has concealed. It is recorded in
`docs/OPEN_QUESTIONS.md`.

There is also an exposure risk. Gârleanu–Pedersen is one of the best-known papers in
this area and Pedersen is widely read in the ML×OR audience. A four-page paper asserting
that G–P is "the source of the dead-band form" will be caught.

### 1.2 Vaze, Theorem 7 — **QUALIFIED**: the theorem exists, but not on the quantity claimed

**What the planning document says.**

> "**Vaze, arXiv:2607.26577 (29 Jul 2026)**, whose Theorem 7 gives a matching minimax
> lower bound Ω(T^{2/3}·V_T^{1/3}) **on cumulative miscoverage** over all online
> algorithms"

**What the paper says.** Rahul Vaze, "Simultaneous Coverage and Efficiency Guarantee in
Online Conformal Prediction", arXiv:2607.26577v1, 2026-07-29. Retrieved as arXiv HTML.

Theorem 7 is indeed titled "Minimax lower bound" and reads, for Model II (nonstationary
stochastic scalar scores over the class `D(V_T)` of distributions with variation budget
at most `V_T`):

> `inf_A sup_{{F_t} ∈ D(V_T)} R(T) ≥ c₁ T^{2/3} V_T^{1/3}`,
> `inf_A sup_{{F_t} ∈ D(V_T)} Q(T) ≥ c₁ f_min T^{2/3} V_T^{1/3}`

where `R(T)` is **dynamic regret in threshold space** — an efficiency quantity — and
`Q(T) = Σ_t c_t(q_t)` is the cumulative coverage error.

**Where the plan's statement is off.** Three things.

1. The **tight** bound is on `R(T)`, the efficiency side. The coverage-side bound carries
   an extra `f_min` factor.
2. The paper's own **Remark 11** is titled "The `Q(T)` lower bound is not stated tightly"
   and says the coverage bound is obtained from the regret bound by a generic conversion
   that "is loose whenever `f_min ≪ 1`", conjecturing but not proving the clean rate. So
   "matching" is the author's conjecture for coverage, not the author's theorem.
3. The result is for **Model II**, the nonstationary *stochastic* model with a variation
   budget — not the adversarial Model I. The planning document's "over all online
   algorithms" is right about the `inf`, but silent about the restricted instance class.

**Verdict.** Not a fabrication and not a serious misreading — the rate, the theorem
number and the minimax character are all correct. But the sentence as written would be
challenged by anyone who has read the paper, and it is used to impose a hard constraint
on F7's framing, so it needs to be precise.

**The constraint itself survives intact and should be obeyed.** If anything the paper
strengthens it: Vaze's entire subject is *simultaneous* coverage and efficiency
guarantees against dynamic benchmarks, so a framing of F7 as "a coverage floor nobody
stated" would collide with it directly. F7's claim is decision-theoretic. It must stay
that way.

**Suggested replacement wording:** "Vaze (2026) proves minimax lower bounds of order
T^{2/3}V_T^{1/3} for online conformal prediction under a variation budget, tightly for
dynamic regret in threshold space and up to a density factor for cumulative coverage
error. We make no information-theoretic claim; our result is decision-theoretic."

---

## 2. Metadata failures — check (ii)

### 2.1 Conformal PID is NeurIPS **2023**, not 2024

The planning document writes "**Angelopoulos, Candès & Tibshirani, conformal PID
(2024)**". The preprint (arXiv:2307.16895) is dated 2023-07-31 and DBLP records the
venue as **NeurIPS 2023**. Corrected in the bib.

### 2.2 Conformal risk control — author order reversed, no year

The planning document writes "**Bates, Angelopoulos et al., conformal risk control**".
The canonical author order is **Angelopoulos**, Bates, Fisch, Lei, Schuster (arXiv:2208.02814;
DBLP records the venue as **ICLR 2024**). No year or venue is given in the planning
document at all. Corrected in the bib.

Worth noting in passing: **Lihua Lei is an author of this paper and sits on the ML×OR
programme committee.** A miscited author list on a committee member's own paper is an
avoidable and specifically costly error.

### 2.3 Schmitt — the method is RWC, not "RWCP"

The planning document writes "**Schmitt, RWCP (arXiv:2602.03903)**" with no title. The
identifier resolves to Marc Schmitt, "Taming Tail Risk in Financial Markets: Conformal
Calibration for Nonstationary Portfolio VaR", q-fin.RM, 2026-02-03. The method proposed
is **regime-weighted conformal calibration (RWC)**, with time-weighted calibration (TWC)
as a special case. "RWCP" does not appear. Minor, but it is a method name that does not
exist.

No claim is attributed to this work in the planning document, so check (iii) is vacuous.
That is itself worth flagging: the reference is in the list without a stated reason for
being there.

### 2.4 MacLean, Thorp & Ziemba — unresolvable as cited (also a check (i) failure)

The planning document writes "**MacLean, Thorp & Ziemba** — Kelly under estimation
error; cite as the mechanism you **tested and ruled out**". No year, no title, no
identifier, no venue.

These three authors have a large joint corpus. The most likely referent is the edited
volume *The Kelly Capital Growth Investment Criterion: Theory and Practice*, World
Scientific, 2011, doi 10.1142/7598, and within it most likely the chapter "Good and Bad
Properties of the Kelly Criterion" (doi 10.1142/9789814293501_0039). Both records were
fetched and both are real, but **the audit cannot determine which work the plan means**,
so check (iii) cannot be performed at all.

This is the only load-bearing citation in the document with no locator, and it is the
one the plan claims to have experimentally refuted. Refuting a source you have not
identified is not a defensible position in print. The operator must name the work; the
question is in `docs/OPEN_QUESTIONS.md`.

---

## 3. Duplication — check on list hygiene

**arXiv:2502.10947 appears twice in the reference list, under two different
descriptions:**

> "**Ramalingam, Kiyani & Roth (ICML 2025, arXiv:2502.10947)** — the regret↔coverage
> correspondence holds i.i.d. but fails adversarially (the tight version needs *swap*
> regret)"

and, eleven lines later in the same list:

> "Zinkevich (2003); **arXiv:2502.10947** (no-regret ↔ online conformal)"

Both descriptions are of the same paper, and — this is the point — **both descriptions
are accurate.** The abstract of "The Relationship between No-Regret Learning and Online
Conformal Prediction" says precisely that standard regret guarantees imply marginal
coverage in i.i.d. settings but fail under adversarial environments or group-conditional
coverage, and that the tight connection is with swap regret. So this is not a
mis-citation. It is a list that was assembled in at least two passes without being
deduplicated.

**What that signals.** The reference list was not read as a list before it was written
down. Combined with the two other structural defects in the same list — one entry with no
locator at all (§2.4), one entry with no stated reason for being there (§2.3), and two
entries given as bare arXiv identifiers with no authors or titles — the section reads as
accumulated rather than curated. For a four-page paper with unlimited references at a
venue whose committee works in this exact area, the reference list is a visible quality
signal and this one needs rebuilding from `audit/REFS_VERIFIED.bib`.

---

## 4. Cautions — not failures

### 4.1 DtACI, "2022"

"Gibbs & Candès (ACI 2021; **DtACI 2022**)". The DtACI paper, "Conformal Inference for
Online Prediction with Arbitrary Distribution Shifts" (arXiv:2208.08401), was posted in
2022 but published in the **Journal of Machine Learning Research in 2024**. Citing the
preprint year is legitimate; citing the journal is better. Not scored as a failure.

### 4.2 Zaffran et al., author order

The planning document's order — Zaffran, Féron, Goude, Josse, Dieuleveut — **matches the
published ICML 2022 record**. The arXiv v1 metadata lists a different order. The plan is
right and arXiv is the outlier. No action.

### 4.3 Entries cited as bare identifiers

`arXiv:2605.01176` is cited with the gloss "(decision-induced turnover in SPO)" and no
authors or title. The identifier resolves to Yi Wang and Takashi Hasuike,
"Decision-Induced Ranking Explains Prediction Inflation and Excessive Turnover in
SPO-Based Portfolio Optimization", q-fin.PM, 2026-05-02, and the gloss is accurate.

Flagged here for a different reason: **this is the nearest published neighbour to C2 in
the plan's own reference list, and it is cited as a bare identifier in a trailing
clause.** It studies excessive turnover induced by decision-focused learning and
evaluates *partial portfolio adjustment* as a stabilization mechanism — which is a
damping scheme for exactly the pathology C2 addresses, in SPO rather than conformal
prediction. It deserves a paragraph in related work, not a parenthesis. See
`audit/PRIOR_ART.md`.

---

## 5. Entries passing all three checks

Gibbs & Candès ACI (NeurIPS 2021) · Bhatnagar et al. SAOCP (ICML 2023) · Lekeufack et al.
CDT (ICRA 2024) · Zaffran et al. (ICML 2022) · Angelopoulos, Barber & Bates (ICML 2024) ·
Srinivas (SODA 2026) · Ramalingam, Kiyani & Roth (ICML 2025) · Vovk, Gammerman & Shafer
(Springer 2005) · Elmachtoub & Grigas (*Management Science* 2022) · Wang & Hasuike
(arXiv:2605.01176) · Zinkevich (ICML 2003) · Kelly (1956) · Rockafellar & Uryasev (2000) ·
Gibbs & Candès DtACI (with the §4.1 caution) · Ryan (passed forward, not re-verified).

Two of these deserve positive mention because the plan's attribution to them was checked
against the full text and **held**:

- **Lekeufack et al., CDT.** The plan's entire differentiation from CDT rests on its
  trading experiment being zero-cost and synthetic. Section V-C of the paper says exactly
  that, in the paper's own words. This claim is safe to make in print.
- **Zaffran et al.** The plan says this is "the closest existing analysis of γ and must
  be engaged directly." It is — and it is closer than the plan appears to realise. See
  `audit/PRIOR_ART.md`.
