# Claim ledger for `docs/PLAN_ORIGINAL.md`

The planning document mixes computed results, bare assertions, planned work and
findings inherited from an earlier automated sweep — often in adjacent sentences of
the same paragraph. Separating them is the purpose of this file.

**STATUS** — one of four.

| tag | meaning |
|---|---|
| `computed` | the plan presents it as the output of a computation it ran |
| `asserted` | stated as fact in prose, with no computation and no citation behind it |
| `planned` | future work: a thing to be built, proved or shown |
| `inherited` | carried over from the automated novelty sweep described in the plan's own "Dedicated novelty sweep" section, with no artefact from that sweep in the repository |

Note on `computed`: **no computation in this repository produced any of it.** The
simulator is absent (`audit/REPRO_C1.md`). `computed` therefore means "presented as
computed", never "verified as computed".

**LOAD-BEARING** — does the paper survive if this claim is false?

**EVIDENCE** — the specific artefact that supports it, or `none`.

---

## 1. The anomaly

| # | Claim | Status | Load-bearing | Evidence |
|---|---|---|---|---|
| A1 | Conformal Kelly (arXiv:2608.01494) reports that every tweak adapting the interval faster costs 0.7–5.3 points of annual growth | asserted | **yes** | Externally verified against the preprint's abstract. Solid. |
| A2 | Ryan reports this and *cannot explain it* | asserted | **yes** | **FALSE — checked and resolved.** Ryan explains it in his abstract ("the stability of the width matters more than its local sharpness") and again in his conclusion ("a scale estimator consumed by a nonlinear sizing map is charged for its own estimation variance"). The explanation is hedged, measured for one device only, and is **not** a turnover account. The paper's opening move must be rewritten; see `docs/FRAMING.md`. |
| A3 | "Nobody has explained it" | asserted | **yes** | **FALSE, and the obvious weakening is also false.** Ryan publishes an explanation in his own abstract and conclusion, so "no published explanation" fails too. The defensible statement is the specific one: Ryan proposes a hedged, unmeasured, non-turnover mechanism — estimation variance charged through a nonlinear sizing map, measured for one device and conjectured for the rest — and F7 tests it against a turnover account. See `docs/OUTSTANDING.md` (resolved) and `docs/FRAMING.md`. |
| A4 | Slow unweighted per-asset rolling quantiles beat ACI, DtACI and conformal PID in Ryan's experiments | asserted | **yes** | Externally corroborated. |
| A5 | This "runs directly against the adaptive-conformal literature's premise that faster adaptation is better under non-stationarity" | asserted | **yes** | **none, and false in the strong form.** Two of the plan's own citations say the opposite: Angelopoulos, Barber & Bates (ICML 2024) show *decaying* step sizes give per-timepoint coverage under stability, and Zaffran et al. (ICML 2022) prove ACI's efficiency degrades **linearly in γ**. The literature does not hold the premise this sentence attributes to it. See §7. |

## 2. The C1 experimental result

| # | Claim | Status | Load-bearing | Evidence |
|---|---|---|---|---|
| B1 | `scratchpad/confloor5.py` computes the C1 table | computed | **yes** | **none — the file does not exist.** `audit/REPRO_C1.md` §1. |
| B2 | Coverage is pinned at 0.90 for every γ ≥ 0.005 | computed | **yes** | The plan's own table, unverified. Internally consistent. |
| B3 | Net growth swings 4.4 points across the γ grid | computed | **yes** | Derivable from the same table. Unverified. |
| B4 | That swing is 13.7 standard errors | computed | **yes** | Derivable. Unverified. |
| B5 | At 0 bps the effect vanishes; all paired diffs within 1 SE | computed | **yes** | **none — no 0 bps table appears anywhere.** This is the identification argument for the whole paper. |
| B6 | At 5 bps the effect is intermediate | computed | no | **none — no 5 bps table appears anywhere.** |
| B7 | The effect is monotone in the cost rate | computed | **yes** | Asserted over three cost levels, one of which is tabulated. Three points is a thin basis for monotonicity regardless. |
| B8 | "The channel is unambiguously transaction cost" | asserted | **yes** | Rests entirely on B5–B7. "Unambiguously" is not earned by a three-point cost grid with two untabulated points. |
| B9 | The simulation gives 1.0–4.4 points, a quantitative match to Ryan's 0.7–5.3 | computed | **yes** | The plan's own table gives 0.02–4.37, not 1.0–4.4. See §5, C-c. |
| B10 | The quantitative match is "the strongest evidence this file contains" | asserted | no | Self-assessment. If C-c is right, the strongest evidence is the coverage-versus-turnover dissociation, not the magnitude match. |
| B11 | At 0 bps, Var(Δq) rises 330× across the γ sweep while net growth stays flat within 1 SE | computed | **yes** | **none — no variance table appears anywhere.** |
| B12 | Therefore the variance channel does not transmit; only the turnover channel does | asserted | **yes** | Rests entirely on B11. See §5, C-d. |
| B13 | The paired-CRN design cut the standard error by roughly 5× | asserted | no | none. No unpaired standard errors are reported anywhere for comparison. |
| B14 | γ = 0 (no adaptation) is statistically indistinguishable from the best arm at every cost level | computed | **yes** | Tabulated only at 15 bps (+0.0002 ± 0.0003, 0.67 SE). "At every cost level" extends to two untabulated cost levels. |
| B15 | The design resolves its own question by 5–100× | asserted | **yes** | **Overstated.** The table's own effect/SE ratios are 0.67×, 2.5×, 5.4×, 9.7×, 13.7×. Maximum 13.7×; two of five comparisons below the stated 5× floor. Marked "**Confirmed**" in the plan. |
| B16 | The core experiment runs in ~90 seconds, CPU-only | asserted | no | none. |
| B17 | "The central experiment is already done"; remaining effort 2 weeks | asserted | **yes** | **Contradicted.** See `audit/REPRO_C1.md` F-B2-1. |
| B18 | Adding the dead-band arm is ~15 lines | asserted | no | An estimate of an edit to a file that does not exist. |

## 3. Primary claim C1

| # | Claim | Status | Load-bearing | Evidence |
|---|---|---|---|---|
| C1a | For **any** online conformal method, the adaptation rate is first-order in downstream turnover and zeroth-order in coverage | planned | **yes** | One simulation, of one method, on one data-generating process, at one coverage level. The universal quantifier is not supported and is not needed; the claim is worth making for the class of methods actually tested. |
| C1b | Therefore no coverage-based criterion — marginal, conditional or adaptive — can select the adaptation rate for a decision that pays for turnover | planned | **yes** | The paper's thesis. Note it is a *negative* claim about a class of criteria, so a demonstration on one method cannot establish it; it needs either an argument that coverage is invariant to the relevant perturbation, or explicit restriction to the tested class. See §7 on DtACI, which selects the step size online *by a coverage-based criterion* and is therefore the sharpest test case. |
| C1c | Formalise the turnover-versus-tracking-error frontier | planned | **yes** | Nothing exists yet. |
| C1d | The coverage-optimal point sits at the wrong end of that frontier | planned | **yes** | Nothing exists yet. Note the plan's own table does not identify a coverage-*optimal* γ — coverage is flat over γ ≥ 0.005, which means coverage does not have an interior optimum to sit at the wrong end of. The claim needs restating as "coverage does not locate a point on the measured turnover–tracking-error curve at all", which is stronger, is what the table shows, and avoids the word "frontier" (see `audit/PRIOR_ART.md` §6, Risk 2). |

## 4. Secondary claim C2 — the method

| # | Claim | Status | Load-bearing | Evidence |
|---|---|---|---|---|
| C2a | Add a cost-aware dead-band / hysteresis to the ACI update | planned | **yes** | Not implemented. |
| C2b | Choosing Δα to minimise `coverage-deviation-penalty + λ·cost·\|Δf(q)\|` gives an update that is "optimally sluggish rather than heuristically slow" | planned | **yes** | Not derived. "Optimal" is with respect to a one-step objective that is *not* the paper's actual objective (long-run net growth); a myopic per-round optimum is not an optimal policy under path dependence. See C-b. |
| C2c | The L1 movement penalty yields a soft-threshold / dead-band update in closed form | planned | no | The convex-analysis content is standard and correct: the proximal operator of the L1 norm is soft-thresholding. This part is safe. |
| C2d | This is "exactly as in the Gârleanu–Pedersen dynamic-trading solution" | asserted | **yes** | **False.** Gârleanu & Pedersen (2013) assume *quadratic* trading costs and derive linear partial adjustment toward an aim portfolio; they explicitly distinguish their solution from proportional-cost strategies "which exhibit periods of no trading". See `audit/REFS_REJECTED.md`. |
| C2e | C2 dominates both fast ACI and fixed-α slow quantiles at matched coverage | planned | **yes** | The empirical bet of the paper. Untested. The plan's own STOP condition concedes it may fail. |
| C2f | Coverage theorem: the dead-band delays but does not prevent adaptation, so long-run coverage is preserved while turnover is bounded | planned | **yes** | Stated as "the theorem to state". See §5, C-a. |
| C2g | "Conformal Kelly found slow beats fast; the correct answer is neither, and the dead-band is why" | planned | no | Rhetorical framing contingent on C2e. |

## 5. Experimental protocol and preflight

| # | Claim | Status | Load-bearing | Evidence |
|---|---|---|---|---|
| P1 | Seven-baseline comparison including fixed-α, ACI, DtACI, conformal PID, SAOCP and Conformal Decision Theory | planned | **yes** | None implemented. Note DtACI and SAOCP both already adapt the step size online; see §7. |
| P2 | Report net growth, coverage and turnover jointly | planned | **yes** | Correct and is the paper's actual contribution to practice. |
| P3 | Common random numbers across methods, ≥60 paths, paired differences with SEs | planned | no | Sound design. The 60-path count is calibrated to the largest effect, not the smallest one the paper wants to claim; see B15. |
| P4 | The interval must use only trailing data (no leakage) | planned | no | A requirement, not a result. Needs an executable assertion; see `audit/RECONSTRUCTION_SPEC.md` §3. |
| P5 | STOP condition: if the dead-band does not beat both baselines on real data, report the C1 dissociation alone | planned | no | Good practice. Worth keeping and worth writing into `docs/GATES.md`, which is done. |
| P6 | The applied arm uses free daily equity/ETF series | planned | no | Superseded by the operator's decision that the applied arm is specifically a replication of Ryan's configuration. |

## 6. Threat responses

| # | Claim | Status | Load-bearing | Evidence |
|---|---|---|---|---|
| T1 | "This is just transaction costs, obviously" is answerable because the field demonstrably did not account for it | asserted | **yes** | **Partly false.** The field is visibly aware that the step size matters and has produced at least three responses to it: DtACI aggregates over a set of step sizes online, Angelopoulos–Barber–Bates decay the step size, and Podkopaev, Xu & Lee (arXiv:2412.19318) build a parameter-free adaptive conformal method whose stated motivation is "explicit dependence on and sensitivity to the choice of the learning rates". What the field has not done is price the step size in **decision movement cost**. That narrower statement is true and defensible; the broad one is not. |
| T2 | CDT's trading experiment is explicitly zero-cost on synthetic GBM, so the turnover-penalised case is its stated gap | inherited | **yes** | **VERIFIED.** Lekeufack et al. (ICRA 2024), §V-C: "We model the agent as able to either buy or short-sell the stock, **with no trading cost**"; "We simulate stock returns using a **geometric Brownian motion**." Upgrade this from inherited to verified. See §7 for a caveat about CDT's decision space. |
| T3 | CDT's guarantee is risk control (average loss ≤ ε), not a turnover bound | asserted | no | Consistent with the paper. Correct. |
| T4 | Path-dependence breaks the regret analysis; the bounded-memory/lag assumption must be stated | asserted | **yes** | The concern is real and correctly identified. It is also *already a field*, which the plan does not mention. See §5, C-b. |
| T5 | The falsified variance hypothesis "shows the mechanism was not a given" | asserted | **yes** | Rests on B11/B12. See §5, C-d. |

## 7. Prior art and novelty

| # | Claim | Status | Load-bearing | Evidence |
|---|---|---|---|---|
| N1 | Prior-art verdict: NARROW | inherited | **yes** | Re-derived independently in `audit/PRIOR_ART.md`. |
| N2 | "Nothing exists on how variance in adaptive conformal interval widths propagates into downstream decision loss" | inherited | **yes** | **Partly false.** Decision-focused conformal prediction is an active field with at least a dozen entries the plan does not cite. The narrower proposition — that no work varies the *temporal adaptation rate* and measures *decision movement cost* — survives. `audit/PRIOR_ART.md` E1. |
| N3 | arXiv returns 0 results for `conformal` × `downstream decision` × `variance` | inherited | **yes** | **False.** A single arXiv API query on `conformal` × `downstream decision` returns a full page of on-topic results. `audit/PRIOR_ART.md` E1. |
| N4 | arXiv returns 0 results for `prediction interval` × `Kelly` | inherited | no | Approximately true at abstract level (Conformal Kelly is the only hit), but a zero-hit count from an unrecorded query with no stated field scope is not evidence of absence, and this is the second time the same method produced a false negative. |
| N5 | Do not frame F7 as an impossibility result or coverage floor; that ground is held by Vaze (Theorem 7) and Srinivas | inherited | **yes** | **VERIFIED, with one correction.** See `audit/REFS_VERIFIED.bib` and `audit/REFS_REJECTED.md`: Vaze's Theorem 7 is titled "Minimax lower bound" and gives the rate T^{2/3}V_T^{1/3}, but the tight statement is on *dynamic regret in threshold space*; the coverage-side bound carries an f_min factor that the author's own Remark 11 flags as not tight. The framing constraint stands regardless and should be obeyed. |
| N6 | The MacLean–Thorp–Ziemba estimation-error channel is the competing explanation, and it is ruled out | inherited + asserted | **yes** | The plan gives no year and no identifier for this reference — the only load-bearing citation in the document with no locator. The ruling-out rests on B11. See C-d. |
| N7 | Zaffran et al. (ICML 2022) is the closest existing analysis of γ and must be engaged directly | asserted | **yes** | **Verified and materially understated.** See C-e and `audit/PRIOR_ART.md`. |
| N8 | Angelopoulos, Barber & Bates is an existing partial account of slow-beats-fast that F7 must be distinguished from | asserted | **yes** | Verified. Their mechanism is statistical (quantile estimation under stability); F7's is economic (movement cost). The distinction is real and should be stated in one sentence in the paper. |

---

# 5. The five items requiring individual treatment

## C-a. C2's coverage theorem

**The plan's statement.** "Prove coverage is retained: the dead-band delays but does
not prevent adaptation, so long-run coverage is preserved while turnover is bounded —
this is the theorem to state."

**Status: `planned`, written in the grammar of a result.** The sentence contains its
own proof sketch ("delays but does not prevent"), which is where the difficulty is
hidden rather than addressed.

### Why the standard argument does not carry over

ACI's coverage guarantee is not statistical. It is a telescoping identity on a bounded
recursion. From `α_{t+1} = α_t + γ(α − err_t)`, summing over t gives

    α_{T+1} − α_1 = γ · Σ_t (α − err_t),

so the realised miscoverage frequency is `(1/T)Σ err_t = α − (α_{T+1} − α_1)/(γT)`,
and the deviation from nominal is bounded by whatever bounds `α_t`. It holds for
adversarial sequences, needs no exchangeability, and needs no assumption on the data.
It is also **exactly what a dead-band breaks.** With a dead-band the update is

    α_{t+1} = α_t + S_τ( γ(α − err_t) )

for a soft-threshold `S_τ`, and the sum no longer telescopes: the residual is the
accumulated *suppressed* increment, which nothing in the construction bounds. Long-run
coverage is not preserved for free; it has to be re-established.

### The asymmetry the plan does not address, and it points the wrong way

With `err_t ∈ {0,1}` and `α = 0.10`, the ACI increment takes exactly two values:
`+0.1γ` when the interval covers, and `−0.9γ` when it misses. A symmetric dead-band of
width `τ` therefore does **not** treat the two symmetrically. For any `τ` in
`(0.1γ, 0.9γ)` it annihilates every covered-step increment and passes every
miscovered-step increment untouched. `α_t` then drifts monotonically downward, the
interval widens without bound, and the method **systematically over-covers**.

This is a concrete, cheap, falsifiable prediction that should be checked on day one of
C2 work, because it determines whether the naive form of the method is viable at all.
It also means the plan's phrase "delays but does not prevent adaptation" is false for
the naive construction: the dead-band does not delay adaptation symmetrically, it
deletes one direction of it.

### The fork the plan does not acknowledge

Everything depends on **which object the dead-band acts on**, and the plan is
inconsistent about this. Its §Method item 3 puts the penalty inside the choice of
`Δα_t` — the dead-band acts on the quantile update. Its C2 summary says "move the
interval only when accumulated coverage evidence exceeds the cost of moving the
position it implies" — also the interval. But "the cost of moving the position" is a
property of the decision map, not of the interval.

**Branch (i) — dead-band on the decision map.** Run ACI untouched; apply the
threshold between `q_t` and the traded position, so the position moves only when the
implied position change is large enough to be worth paying for. Then:
- coverage is *identical to ACI's*, and the theorem is immediate and trivial;
- turnover is bounded by construction;
- and the method is, in substance, "do not rebalance on small signal changes" — a
  standard no-trade band from portfolio practice, applied to a conformal interval. It
  is defensible and it will work, but it is a **contribution to practice, not a
  theorem**, and a reviewer will say so.

**Branch (ii) — dead-band on the quantile update.** The interval itself becomes lazy.
Then coverage is genuinely at risk, the theorem is genuinely hard, and the asymmetry
above bites. This is where the novelty is, and it is unproved.

The plan gets the credit of branch (ii) while implicitly relying on the tractability of
branch (i). **Choosing between them is the single most consequential open decision in
the project** and is recorded in `docs/OPEN_QUESTIONS.md`.

### What a proof on branch (ii) would actually require

1. A construction that **accumulates rather than discards** the suppressed evidence —
   an integrator with anti-windup, so that the telescoping sum is preserved up to a
   bounded residual term. "Delays but does not prevent" is only true if the suppressed
   increment is *stored*, and storing it is a design choice that must appear in the
   algorithm, not an emergent property of thresholding.
2. A bound on the accumulated deviation of the form
   `|(1/T)Σ err_t − α| ≤ (B + Σ_t |suppressed_t|) / (γT)`, together with a bound on
   `Σ_t |suppressed_t|` that does not itself grow linearly in T. This second part is
   the whole problem: a dead-band that binds a constant fraction of rounds gives a
   suppressed sum that is Θ(T), and the bound is vacuous.
3. A resolution of the asymmetry — almost certainly an asymmetric threshold, with
   `τ_+ / τ_-` in the ratio `α / (1−α)`.
4. An explicit statement of what "turnover is bounded" means. Bounded by a constant?
   By `o(T)`? Against what benchmark? The plan does not say, and the answer determines
   whether the theorem is interesting.

### Why an asserted theorem will not survive review

The programme committee includes people who work directly on conformal prediction and
on decision-focused learning. The telescoping argument above is the first thing such a
reader will reconstruct, and the first question will be "what happens to the sum when
the update is thresholded?" A paper that states the coverage claim without answering
that question fails at the first reviewer.

### The honest empirical fallback

If the theorem cannot be proved in time — and four pages is not much room for it — the
defensible substitute is **an a-posteriori certificate rather than an a-priori
theorem**:

> The dead-band update satisfies `|(1/T)Σ err_t − α| ≤ (B + S_T)/(γT)` where
> `S_T = Σ_t |suppressed_t|` is computable from the run. We report `S_T` for every
> experiment; across all tested regimes it grows sublinearly, giving realised
> miscoverage within X of nominal.

This is honest, it is checkable by a reader, it is genuinely informative about when the
method is safe, and it does not claim a theorem the paper does not have. It also
degrades gracefully: if `S_T` turns out to grow linearly in some regime, that is a
finding about when the method must not be used, which is publishable in itself.

**Recommendation.** Do not attempt to state an unproved coverage theorem. Either prove
the branch-(i) statement (easy, honest, modest) and present the branch-(ii)
construction as empirical, or commit to branch (ii) and treat the theorem as the
project's main technical risk with its own gate. This is reflected in G3 of
`docs/GATES.md`.

## C-b. Path dependence is online convex optimization with switching costs

**The plan's statement.** "Real and must be handled: the turnover-penalised loss
depends on the incumbent position, so per-round loss is not a fixed function of α_t.
State the bounded-memory/lag assumption explicitly — this is a genuine quantifier-order
trap, not a formality."

The diagnosis is correct. The response — "state the assumption" — is not adequate,
because the problem the plan has just described **already has a name and a fifteen-year
literature**, and the plan does not mention it anywhere.

### What the problem is

Once the per-round loss is

    ℓ_t(α_t) + c · | f(q(α_t)) − f(q(α_{t−1})) |,

this is **Smoothed Online Convex Optimization (SOCO)**, also called online convex
optimization with switching costs: a hitting cost plus a movement cost in the decision
space. It is not a variant of ACI analysis. It is a different problem with its own
algorithms, its own lower bounds and its own impossibility results.

### What that literature already establishes

| Result | Bearing on C2 |
|---|---|
| Kalai & Vempala, *Efficient algorithms for online decision problems* (JCSS 2005; COLT 2003) — Follow the Lazy Leader | No-regret with an explicitly bounded number of switches. The "be lazy without losing much" technology predates F7 by twenty years. |
| Geulen, Vöcking & Winkler (COLT 2010) — the shrinking dartboard | No-regret with **O(1)** expected switches per unit of weight movement. The strongest form of "you can adapt and almost never move". |
| Andrew et al., *A Tale of Two Metrics: Simultaneous Bounds on Competitiveness and Regret* (arXiv:1508.03769) | **No online algorithm can be simultaneously constant-competitive and no-regret under switching costs.** This is a direct constraint on C2's "dominates *both* fast ACI and slow fixed-α" claim: in the SOCO formulation, simultaneous optimality against both a dynamic and a static comparator is provably impossible. C2's dominance claim must therefore be empirical and regime-specific, or it must be shown that the conformal setting escapes this lower bound. |
| Chen, Goel & Wierman, *Online Balanced Descent* (arXiv:1803.10366), and the smoothed-OCO line generally | Established algorithms for exactly the objective C2 proposes to minimise. If C2's update is not compared to one of these, a reviewer from the OR side will ask why. |
| Borodin, Linial & Saks — metrical task systems | The general framework; movement cost as a metric. |
| Constantinides (1986, JPE); Davis & Norman (1990, Math. OR) | The no-trade region under **proportional** costs — the actual source of the dead-band form, and the correct citation in place of Gârleanu–Pedersen. |

### How much of C2's analysis is already covered

**The regret side: essentially all of it.** That one can track a moving target while
paying bounded movement cost, at a quantified regret penalty, is known. C2 should not
claim novelty for the algorithmic idea of laziness, for the soft-threshold form, or for
the observation that movement is costly.

**The coverage side: none of it.** SOCO has no notion of coverage. Its guarantees are
regret and competitive ratio against a comparator, and those are the wrong currency —
which is not a guess, because one of the plan's own citations proves it. Ramalingam,
Kiyani & Roth (ICML 2025, arXiv:2502.10947) show that standard regret guarantees imply
marginal coverage in i.i.d. settings but **fail as soon as the environment is
adversarial or conditional coverage is asked for**, and that the tight correspondence
requires *swap* regret. So importing a SOCO regret bound will not deliver C2's coverage
theorem, and the plan cites the very paper that says so without using it.

### The consequence for how C2 should be positioned

The honest structure is:

> Take a switching-cost-bounded online scheme from the SOCO literature. Show that,
> applied to the conformal quantile update, it retains the ACI coverage identity.

That is a well-posed problem, it is novel in the precise sense `audit/PRIOR_ART.md` §4.5.2
fixes — what is unoccupied is a coverage *guarantee* under a movement-penalised conformal
update, not the pairing of conformal prediction with switching costs as such — and it makes
the related-work section a strength rather than an exposure.
The framing "we invent a dead-band" is neither novel nor necessary; the framing "we
show a known lazy scheme is coverage-safe" is both.

**This also supplies the missing citations.** The plan's reference list contains
Zinkevich (2003) and nothing else from this literature. A four-page paper that proposes
an online algorithm with a movement penalty and cites no switching-cost work will read,
to an ML×OR audience specifically, as unaware of its own field.

## C-c. The "quantitative match" claim

**The plan's statement.** "Conformal Kelly reports 0.7–5.3 points; this simulation
gives 1.0–4.4 points across the γ range. An independently derived quantitative match to
someone else's unexplained empirical finding is the strongest evidence this file
contains."

**Verdict: "quantitative match" is not defensible.** Three separate problems, in
increasing order of severity.

**1. The stated range is not the plan's own range.** The paired differences in the C1
table are 0.02, 0.10, 0.43, 1.84 and 4.37 points. No comparison yields 1.0. The
interval "1.0–4.4" is not derivable from the table it claims to summarise
(`audit/NUMBERS.md` row 54).

**2. The configurations differ on every axis that matters.**

| | Ryan (Conformal Kelly) | F7 simulation |
|---|---|---|
| Coverage level | 75 % interval | 90 % target |
| Data | real series, 2016–2021 development window | synthetic regime-switching path |
| Universe | multi-asset, per-asset quantiles | single scalar process |
| What varies | the *identity of the method* (rolling quantile vs ACI vs DtACI vs PID) | a single scalar γ within one method |
| Estimator | unweighted per-asset rolling empirical quantiles | `ŝ_t · z(α_t)` |
| Frictions | trading costs and leverage caps | proportional cost, cap unspecified |

The coverage difference alone is disqualifying for a *quantitative* claim: 75 % and
90 % intervals have different quantile curvature, so the map from α-jitter to
width-jitter differs by a factor the plan never computes.

**3. Overlapping ranges are a weak statistic in any case.** Two intervals overlapping
is not quantitative agreement. It would be satisfied by a wide class of unrelated
mechanisms, and a referee will note that the F7 range is partly a choice — it is set by
where the γ grid was truncated. Extend the grid and the range extends with it.

**The honest claim.** "Same sign, same order of magnitude, and the same monotone
direction: a mechanism-level simulation reproduces the reported anomaly at a comparable
magnitude under a different configuration."

**The much better claim, which is available.** The operator has already decided that
the applied arm is a *replication of Ryan's configuration* rather than a generic equity
experiment. That converts rhetoric into a real test: run the F7 mechanism at Ryan's
75 % level, on Ryan's window, with Ryan's estimator family and cost model, and predict
Ryan's per-method growth costs **before** looking at them. A prediction that lands is
worth incomparably more than two overlapping ranges, and it is the strongest single
thing this project could produce. It should be stated as a pre-registered prediction in
the G2 protocol freeze.

## C-d. The falsified variance hypothesis

**The plan's statement.** The first explanation considered was that log-utility is
variance-averse and coverage is variance-blind, so quantile jitter would hurt growth
directly. It is reported false: at zero cost, `Var(Δq)` rises 330× across the γ sweep
while net growth stays flat within 1 SE.

**This is genuinely an asset.** Recording a falsified hypothesis is good practice, it
pre-empts the obvious reviewer counter-explanation, and it is the difference between an
over-determined observation and an identified mechanism. Keep it.

**But the evidence is weaker than the plan claims, in four distinct ways, and a
competent reviewer will find at least two of them.**

**1. There is no table.** The 330× and the "flat within 1 SE" are both prose assertions
with no displayed numbers at any cost level (`audit/NUMBERS.md` row 55). This is the
single load-bearing statistic for the paper's identification argument.

**2. "Flat within 1 SE" is a failure to reject, presented as a refutation.** Absence of
evidence is being reported as evidence of absence, with no power statement. The
question a reviewer will ask is: *what size of variance-channel effect would this design
have detected?* At the reported SEs, the 0 bps design excludes effects of roughly
0.0006–0.006 in annual log growth depending on the arm — which is to say it excludes a
large variance effect and says nothing about a moderate one. **The fix is cheap:**
report an equivalence test (two one-sided tests) with an explicit equivalence margin,
so the claim becomes "we exclude a variance-channel effect larger than δ", with δ
stated.

**3. The falsification is conditional on the unspecified Kelly fraction.** The
MacLean–Thorp–Ziemba overbetting penalty is second-order in the position size. At
quarter-Kelly the penalty is roughly an order of magnitude smaller than at full Kelly,
so a null at small λ is close to uninformative. Since λ is not stated anywhere
(`audit/RECONSTRUCTION_SPEC.md` R6), a reviewer can say "you used a fractional Kelly
small enough that the overbetting channel could not appear" and the plan has no reply.
**The fix:** report the null at full Kelly as well, where the competing channel is
strongest, and state λ.

**4. The statistic may be the wrong one, and this is the sharpest available
objection.** The plan measures `Var(Δq)` — the variance of the *increment* of the
quantile. The estimation-error channel it claims to falsify is driven by the dispersion
of the *level* of the scale estimate around the truth: overbetting arises from
`E[μ/σ̂²] > μ/σ²` by Jensen, which depends on the spread of `σ̂`, not on how much `σ̂`
moves between consecutive periods. A γ sweep moves both, but they are different
quantities, and a 330× rise in increment-variance is compatible with a much smaller
rise in level-variance. **As stated, the plan may be falsifying a channel it has not
measured.**

**The fix:** report both `Var(q)` (level, relative to the oracle quantile) and
`Var(Δq)` (increment) across the γ grid at 0 bps, and show the growth null holds
against the level statistic. If it does, the falsification becomes robust and the
finding is strong. If it does not, the plan has found something more interesting than
it thought.

**What a reviewer could say against it, in one sentence:** "You have shown that
first-differences of the interval width do not affect zero-cost growth in your
parameterisation; you have not shown that the dispersion of the width estimate does
not, and the Kelly literature's claim is about the latter."

## C-e. Inherited-and-unverified claims

These are the highest-risk category in the document: assertions whose only support is
"a prior sweep found X", with no query log, no result list and no artefact in the
repository. Every one is tagged `inherited` above. Consolidated with this audit's
findings:

| Claim | Inherited status | Status after this audit |
|---|---|---|
| N3 — arXiv returns 0 for `conformal` × `downstream decision` × `variance` | asserted as fact, used to establish novelty | **FALSE.** A single query returns a page of on-topic work. `audit/PRIOR_ART.md` E1. |
| N2 — "nothing exists on how variance in adaptive conformal interval widths propagates into downstream decision loss" | the plan calls this the sweep independently identifying "this file's exact square as unoccupied" | **PARTLY FALSE.** The field exists and is active. The narrower square — adaptation *rate* versus decision *movement cost* — does appear unoccupied, but that is a different and much more modest claim than the one inherited. |
| N4 — arXiv returns 0 for `prediction interval` × `Kelly` | asserted | Approximately true at abstract level, but produced by the same unrecorded method that produced N3. Two zero-hit claims from one unlogged process, one of which is false, is not a basis for a novelty section. |
| N5 — Vaze and Srinivas occupy the impossibility/floor framing | asserted, used to impose a hard framing constraint | **VERIFIED**, with a precision correction on which quantity Vaze's tight bound covers. The constraint should be obeyed. |
| N6 — the MacLean–Thorp–Ziemba channel is the competing explanation | asserted, and refuted via B11 | **UNRESOLVABLE AS CITED** — no year, no identifier. Refutation depends on B11, which has no table. See C-d. |
| N1 — verdict NARROW | asserted | Re-derived independently in `audit/PRIOR_ART.md`; see the verdicts there. |
| T2 — CDT's trading experiment is zero-cost synthetic GBM | inherited, and the entire differentiation from CDT rests on it | **VERIFIED against the paper's own text.** This one holds. |
| "100 titles" forward-citation screen of ACI | asserted | No log, no output. The screen may or may not have happened; nothing in the repository shows it did. |

**The pattern matters more than any single item.** Of the eight inherited claims, one
is false, two are materially overstated, one is unresolvable as cited, and two are
verified. A sweep with that error rate cannot be the basis of a novelty section, and
the plan's own instruction to itself — "⚠️ Verify before committing" — was correct. Every
inherited claim should be either re-derived with a logged query or removed from the
paper.
