# Coverage Is Turnover-Blind — scope, aim, novelty, references, claims, state, and the order the work should happen in

**The answer, first.** F7 is a four-page decision-theoretic workshop paper carrying one measurement claim and one method claim. Its *design* is established; its *evidence* is not. The simulator named as the source of the central table does not exist anywhere on the operator's machine — ten search commands, by filename, by content string, by the distinctive value `0.8993`, across every retained scratch directory and every retained session transcript, all negative [1]. Of 88 numbers catalogued in the planning document, **0 were reproduced from code and 12 are orphans**: asserted in prose, displayed in no table, derivable from nothing, corroborated by nothing [2]. Five load-bearing quantities — the zero-cost null, the 5 bps case, the claimed 1.0–4.4 point magnitude match, the 330× variance rise, the claimed 5–100× statistical power — have no displayed table behind any of them: **a 100% orphan rate in exactly the subset the paper leans on hardest** [2]. And the opening claim, that the anomaly F7 explains is unexplained [3], is contradicted by the abstract of the paper cited for the anomaly [4].

That half is bad, and it is not the whole picture. Three things here were produced by verification rather than assertion: a reference audit that resolved 22 citations on three independent checks and failed 7, one of them cited for the opposite of what it says [5]; independent prior-art verdicts of NARROW for both claims, each with a distinguishing sentence that survives contact with its nearest neighbour [6]; and a 45-entry bibliography built entirely from fetched canonical records [7]. Several of the project's positions came through every check unweakened (§6.B). Nothing below says the idea is bad. What it says is that the central experiment does not currently exist, that four of the five statements the paper leans on hardest have never been printed, and that the gap between established and asserted is wide evidentially and narrow in effort: roughly one week of simulator engineering, one email to another author, and one operator decision.

## 1. SCOPE — what the paper is and is not

### 1.A — The object, and the format that binds it

F7 targets the NeurIPS 2026 ML×OR workshop: **four pages of main body, unlimited references and unlimited supplement, no reproducibility checklist, non-anonymous authorship** — the last confirmed at source level, since the `sglblindworkshop` option sets `\@anonymousfalse` in the fetched `neurips_2026.sty` [8]. The deadline is 2026-09-01 11:59 UTC, read from OpenReview's own submission invitation rather than a call-for-papers page; the workshop meets 2026-12-12/13 [8].

Two claims sit inside that budget.

**C1 is a measurement claim.** An online conformal method emits a prediction interval each period and updates its own miscoverage target from realised coverage errors; the canonical instance is adaptive conformal inference (ACI), whose update is `α_{t+1} = α_t + γ(α − err_t)` for target miscoverage α, realised error indicator `err_t`, and adaptation rate (step size) γ [9]. Sweep γ across a grid. **Coverage** — the long-run fraction of periods in which the outcome falls inside the interval — is flat. The **turnover** of the position the interval sizes, the summed absolute period-to-period movement `Σ|Δq|` pushed through a position map, varies by an order of magnitude. Money follows turnover, because turnover is charged at a transaction-cost rate in basis points (bps; one bps is 0.01%) [10][2].

**C2 is a method claim.** A movement-penalised "dead-band" update — do nothing until the evidence has moved enough to pay for the trade — that bounds turnover while retaining a coverage property [10].

### 1.B — What the paper is not: six exclusions, each forced by evidence

1. **Not an impossibility result, coverage floor, or information-theoretic limit.** That ground is held by Vaze's minimax lower bounds of order `T^{2/3}V_T^{1/3}` under a variation budget [11] and by Srinivas's coverage–efficiency frontier [12]. Two sentences in the plan can be read that way and must be rewritten; four pages does not win a collision with a SODA result [6].
2. **Not a claim that moving estimates cause turnover.** That is 1993, in a figure captioned "Average turnover for different percentage changes in means, variances and co-variances" [13] — reproduced inside the very Kelly paper the plan cites and claims to have refuted [14].
3. **Not the first critique of the coverage-and-length metric pair.** Min et al. published exactly that move in January 2026, with a third metric already named *interval stability* [15]. F7's quantity is temporal path variation within one run; theirs is run-to-run irreproducibility of a randomised algorithm on one input. A real distinction — one that must now be stated rather than assumed [6].
4. **Not a new sizing map.** The object is the denominator of a fractional-Kelly position rule (bet size proportional to estimated edge over estimated variance, scaled by a fraction κ), not the rule itself [10].
5. **Not the first pairing of conformal calibration with a switching cost.** An applied wireless paper already formulates an explicit cost-aware "stay-or-switch" decision under online conformal Bayesian optimisation [16] — a paper this project's own query returned and then discarded on a one-line judgement about domain [6]. "The intersection is empty" must be retired. What remains unoccupied is narrower: a *coverage guarantee under a movement-penalised update*.
6. **Not a generic equity experiment.** The applied arm replicates one published configuration: 8 ETFs (exchange-traded funds), α = 0.25, a 500-day rolling quantile shrunk with λ = 0.3 toward an expanding anchor, κ = 0.15, gross exposure cap 2.0, one-day execution lag, 5 bps per unit turnover [4].

And, as written, **not a paper with an experiment**: every cell of the central table — 24 rows, six γ values × four quantities, of which 23 are numeric and one is the reference arm — and all seven named C1 claims are NOT-EMITTED — the audit's tag for a quantity that no run in the record ever produced [1].

### 1.C — The page budget as an allocation, with opportunity costs

Four pages is roughly 3,200–3,600 words with two displayed tables. The allocation below is the argument, not an illustration of it.

| Allocation | Pages | What it buys | Opportunity cost |
|---|---|---|---|
| Intro, anomaly, corrected framing, contributions | 0.75 | Engages the published explanation head-on instead of claiming none exists [4][3] | Half a page of related work |
| Setup: the ACI update, the sizing map, the cost model | 0.5 | Makes the mechanism legible to the operations-research half of the room [8] | The C2 algorithm box |
| **Table 1** — γ × {coverage, mean width, turnover, net growth}, plus the discriminator | 1.0 | The entire empirical claim and the answer to the nearest theorem, in one object [17] | A second synthetic study |
| Identification: zero-cost equivalence test; `Var(q)` at the level and `Var(Δq)` at the increment | 0.5 | Closes the sharpest objection to the falsified-variance result [10] | The cost-monotonicity plot |
| Real data: replication, per-device turnover decomposition | 0.75 | The only part this audience will treat as evidence about the world | C2's empirical arm |
| Related work: four distinguishing sentences | 0.4 | Zaffran, Min et al., the anomaly paper, the decision-induced-turnover paper [17][15][4][18] | Breadth; one clause per citation |
| Limitations | 0.1 | The multiple-comparisons and development-window caveats [4] | Nothing |

That sums to exactly four pages **with C2 absent**, and the arithmetic is the finding: there is no version of this paper in which C1 is properly evidenced and C2 is also in the body. Attempting both yields a compressed C1 whose identification argument is asserted rather than shown — precisely the failure the audit found in the planning document [2]. Everything displaced goes to the unlimited supplement, where space is free and each item is a reviewer answer rather than a reader argument: the free-choice register R1–R13 and the frozen configuration, the five required executable tests [19], the cost grid at five or more levels, the equivalence-test power calculation, time-at-clip and time-at-cap per arm, the dead-band asymmetry result, and the replication reconciliation [20].

### 1.D — The minimum viable paper, and the recommendation

**C1 as the paper; C2 demoted to the supplement.** The plan treats this as its STOP condition — the fallback if the empirical result disappoints [3]. On the evidence assembled it is the *recommended* shape, and the trigger should be the theorem's status rather than the experiment's outcome. Two independent technical investigations converged on the finding that the only surviving C2 construction inherits its coverage guarantee from ACI rather than proving anything new [10][6], which reduces the method to a forty-year-old no-trade band — a region of the state space in which the optimal policy is to do nothing [21][22] — applied to a conformal interval. Pages spent there buy less than the same pages spent making C1 unimpeachable. The one-line scope statement that follows: **F7 is a mechanism paper about how a tuning knob that coverage cannot see becomes money**, demonstrated on a synthetic decision process and confirmed on a published multi-asset configuration.

## 2. AIM — the one sentence a reviewer repeats back

**The repeatable form**, which is what the prompt's test actually asks for — nothing at
eighty words survives being repeated back:

> **Coverage cannot see the tuning knob that costs the money: across adaptation rates with
> identical coverage, the turnover of the decision varies nearly tenfold.**

**The same claim at the precision a referee will demand:**

> **Across the range of adaptation rates that all attain the nominal coverage target to within 0.001, the turnover the interval induces in the position it sizes varies by nearly an order of magnitude — so coverage, which together with interval length is all the online conformal literature prices that rate against, does not locate a point on the turnover–tracking trade-off at all, and for a decision with an incumbent state the price of that blindness is N points of annual net log growth.**

Four properties make this the right sentence, and each is load-bearing.

**It is a measurement, not a quantifier.** "No coverage-based criterion — marginal, conditional or adaptive — *can* select the adaptation rate" is the grammar of an impossibility theorem, will be read as one, and then loses next to Vaze and Srinivas [11][12][6]. It is also refuted by an algorithm in the paper's own baseline list: DtACI selects the step size online by aggregating over a candidate set, using a coverage-based criterion [23][10]. Either the claim is restricted to the tested class, or a reviewer stops at that sentence. The measurement form is unassailable because it is a measurement.

**It names coverage and turnover as the two columns, with money arriving last.** The growth column of the plan's table is reproduced to within about 5% of the effect size by `−c × Δturnover` (§6.D), and a referee will do that subtraction in thirty seconds. Leading with the 4.4-point swing hands the reader the exact objection the plan itself names as most likely to kill the paper [3][2]. Money is the unit in which the blindness is priced, not the finding.

**"Does not locate a point" beats "sits at the wrong end".** The plan says the coverage-optimal point sits at the wrong end of the frontier — but coverage runs 0.8993, 0.8998, 0.8999, 0.8999, 0.9000 across the five arms with γ ≥ 0.005 [10][2]; the sixth, γ = 0, is the only arm that misses, at 0.8926 [1]. Over the pinned range it is flat — and the one arm that does miss is the one with no adaptation at all. There is no coverage-optimal point to sit at the wrong end of, and **flatness is the finding**. The word *frontier* should also go: a formalised coverage–efficiency frontier is Srinivas's object, and borrowing the term invites a comparison F7 cannot win [12].

**`N` stays a placeholder.** In the plan's unreproduced table `N = 4.37` points at 15 bps, or 4.39 against the γ = 0 reference [2]. That number is internally consistent, arithmetically exact against the displayed growth column, and produced by no code that exists [1]. Until the reproduction gate is passed, the sentence is written with the number blank [20].

## 3. NOVELTY — verdicts and distinguishing sentences

### 3.A — The two verdicts

| Claim | Verdict | Nearest neighbour | What would flip it |
|---|---|---|---|
| C1 — coverage/turnover dissociation | **NARROW** [6] | Zaffran et al., ICML 2022, Theorem 3.1 [17] | A rebuild showing `Σ|Δq|` carries no information about net growth once mean interval length is conditioned on |
| C2 — turnover-aware conformal update | **NARROW only in a branch nobody knows how to reach** [6] | No-trade regions [21][22]; the switching-cost online-learning line (§3.D); decision-induced turnover in predict-then-optimise [18] | Delivering the coverage theorem for the suppressed-update branch — or abandoning it, which reduces C2 to a standard no-trade band on a conformal interval |

Neither verdict is CLEAR. C1 is NARROW outright. **C2's verdict has two legs and both must be carried: NARROW if the coverage guarantee is delivered, effectively OCCUPIED if it is not** [6] — and since §3.D finds no available proof route for the suppressed-update branch, **the OCCUPIED leg is the live one on present evidence**. Both verdicts are in any case provisional on an instrument with a demonstrated blind spot (§3.F).

### 3.B — C1's distinguishing sentence, and the four antecedents that narrow it

> Zaffran et al. prove that ACI's coverage is asymptotically valid for **every** step size while its mean interval **length** degrades linearly in that step size — Theorem 3.1 gives `E[L] = L₀ + Q''(1−α)·(γ/2)·α(1−α) + O(γ^{3/2})`, glossed by the authors as "ACI on exchangeable scores degrades the efficiency linearly with γ compared to CP" [17]; F7's object is the **variation of the interval path**, `Σ|Δq_t|`, which no coverage criterion and no efficiency criterion measures, and which a position-holding decision is charged for [6].

That sentence belongs on page one, not in related work. A reviewer who knows Theorem 3.1 will ask what F7 adds in the first paragraph of their review.

Four antecedents narrow the claim, and each must be conceded in print. **Zaffran** owns the abstract structure — coverage insensitive to γ, a downstream quantity very sensitive to γ, therefore coverage cannot tune γ — already published *with a theorem*, for interval length [17]. **Min et al.** own the framing move, seven months old, with the third metric already named [15]. **Chopra (1993)** owns "moving estimates cause turnover", thirty-three years old [13][14]. **Zhu, Yan & Gao** own the composition of conformal calibration with an explicit switching cost inside a decision [16]. What survives all four is precise: nobody has measured the temporal path variation of an online conformal interval, and nobody has priced it in the movement cost of the decision it drives.

The monetisation channel is also structurally unavailable to the nearest literature, and that deserves a sentence in the paper. Decision-focused conformal work shapes set *geometry* [24][25] or the coverage *level* [26]; its decision problems are one-shot or per-period-independent, so there is no incumbent position to move and nothing to charge for movement. Stating the reason the field has not found this is stronger than stating that it has not.

### 3.C — The load-bearing assumption, and the discriminator that actually discriminates

C1 survives Zaffran only because turnover is a **variation** functional while `E[L]` is a **level** functional. Two methods can share a mean width and differ by an order of magnitude in path variation. The distinction is real in principle. **It has never been measured in this project, and it is the paper's load-bearing assumption.**

The project's stated discriminator — "is turnover monotone in mean interval width across the γ grid?" — is too weak. On the plan's own table:

| γ | Coverage | Annual turnover | Excess over γ = 0.005 | Excess ÷ Δγ |
|---|---|---|---|---|
| 0.005 | 0.8993 | 3.4 | — | — |
| 0.020 | 0.8998 | 4.4 | 1.0 | 67 |
| 0.050 | 0.8999 | 6.9 | 3.5 | 78 |
| 0.150 | 0.8999 | 15.8 | 12.4 | 86 |
| 0.400 | 0.9000 | 31.0 | 27.6 | 70 |

**Turnover is already approximately affine in γ** — the same functional form Zaffran proves for mean length, whose excess is also first order in γ [17][2]. A monotonicity check therefore discriminates nothing, because both functionals are monotone and both are first order. It will come back positive and *look like* C1 collapsing into Zaffran's theorem multiplied by a cost rate.

Paper arithmetic corroborates this before any code is written. The ACI increment structure gives an expected per-step quantile movement of order `Q'(1−α)·γ·2α(1−α)` [9], against Zaffran's mean-width excess of order `Q''(1−α)·γ·α(1−α)/2` [17]. Both are first order in γ; their ratio is governed by the curvature-to-slope ratio `Q''/Q'` of the score quantile function, which is distribution-dependent and measurable. This is a reading of two established results rather than a result in either, and it needs checking before it is relied on — but the design consequence holds regardless.

**The corrected discriminator: does `Σ|Δq|` carry information about net growth *conditional on* `E[L]` across the γ grid?** Regress net growth on mean interval length across the grid, then ask whether turnover adds explanatory power. If it does not, C1 reduces to a published theorem times a cost rate, and the honest move is to stop and re-scope rather than re-word. This is stricter than what is currently scoped, it is still cheap, and `docs/GATES.md` G2.10 and `docs/OUTSTANDING.md` O8 should both be corrected to the stricter form [20][27].

Two honest riders. The slopes are not constant — they rise from 67 to 86 and then fall to 70 — so the relation is affine only to within about 25%, and at five points with no error bars the departure is uninformative on its own. But the fall at γ = 0.400 is exactly what a clipping artefact would produce (§6.E): if `α_t` spends much of its time pinned at an implementation bound, turnover saturates. That is a conjecture worth a diagnostic, not a finding.

### 3.D — C2's distinguishing sentence, and the branch that carries the novelty

> Switching-cost online learning has lazy algorithms with regret guarantees and no notion of coverage [28][29][30][31]; online conformal prediction has coverage guarantees and no notion of movement cost; F7 would supply a movement-penalised conformal update that *provably retains the coverage identity* — and the gap is not a free composition, because external regret is known not to imply coverage adversarially, the tight correspondence requiring swap regret, a stronger notion evaluated action-by-action [32].

The novelty lives entirely in one branch. **Branch (i)** dead-bands the decision map: coverage is inherited from ACI unchanged, the method reduces to a no-trade band on a conformal interval [21][22], and the theorem is trivial. **Branch (ii)** dead-bands the quantile update itself: coverage is genuinely at risk, and this is where the contribution would be.

Branch (ii) is a theorem-shaped problem with no available proof route, and four facts close the obvious repairs [10]. ACI's guarantee is not statistical but a telescoping identity on a bounded recursion — summing the update gives `α_{T+1} − α_1 = γ Σ_t (α − err_t)` [9] — and a dead-band breaks the telescoping, because the residual becomes the accumulated *suppressed* increment and nothing bounds it. The general arbitrary-step-size bound requires `η_t > 0` strictly and diverges as any `η_t → 0`, so it excludes literal suppression by its own hypothesis rather than degrading gracefully [33]. Every known repair for non-every-round conformal updating requires the suppression to be **independent of the tracked error process** — an exogenous skip probability with importance weighting [34], a fixed deterministic round-robin [35] — and an evidence-triggered dead-band violates that by construction. And the regret route is closed twice over: external regret does not imply coverage adversarially [32], and the black-box reduction that looked like it might supply the theorem re-derives the same unconditional-update requirement under a second name.

The inverse construction is the one that works, and the literature already demonstrates it: conformal PID maintains `Σ_i(err_i − α)` unconditionally and passes it through a saturating nonlinearity, so every term enters the accumulator and only the readout saturates [36]. That is the mirror image of a dead-band, and it is analysable. **The surviving C2 therefore accumulates `α_t` unconditionally every round and dead-bands only the readout into the traded position.** One sub-question stays open and is the only technical novelty left standing: if the *reported interval* is built from the saturated readout `h(α_t)` rather than from `α_t`, coverage does not obviously transfer, because the saturation changes which threshold is tested against the score. Nobody has stated that question, let alone answered it. A one-sided bound by a monotonicity argument on `h` is a small, real, supplement-sized result — and a coverage guarantee stated for a quantile the reader never sees, attached to an interval that is not that quantile, is precisely the quantifier slip a conformal-literate reviewer catches.

### 3.E — The eight objections, adjudicated

| # | Objection | Verdict | Cost to answer |
|---|---|---|---|
| 1 | "This is just transaction costs, obviously" | **PARTLY LANDS** — fatal to the framing, not the finding | Reorder the columns; free |
| 2 | "This is Zaffran Theorem 3.1 with a different loss" | **PARTLY LANDS**, and is currently unanswerable | The conditional discriminator (§3.C); one day |
| 3 | "Questioning the coverage–length pair is already published" | **PARTLY LANDS** | One sentence of positioning; loss of a priority claim |
| 4 | "The field already knows the step size matters" | **LANDS** against the plan as written; **DOES NOT LAND** against the corrected claim | Drop the general claim, keep the specific one |
| 5 | "Andrew et al. Theorem 2 forbids your dominance claim" | **DOES NOT LAND** | The word "dominates" |
| 6 | "Your coverage theorem does not exist" | **LANDS** — this is what kills the paper today | Demotion to an a-posteriori certificate |
| 7 | "You say the anomaly is unexplained; the paper you cite explains it" | **LANDS**, and converts into an asset | Rewrite the opening; free, and an improvement |
| 8 | "Your anomaly is a development-window ranking from a ~200-configuration search" | **LANDS**, and is the cheapest to answer | One honest sentence |

Three need the reasoning spelled out, because the verdict does not carry it.

**Objection 4 is where the plan is simply wrong and the corrected claim is simply right.** "The field demonstrably did not account for" the step size's cost is cheaply falsified: step sizes are decayed with guarantees for arbitrary positive sequences [33]; DtACI aggregates over a set of them [23]; a parameter-free method exists whose stated motivation is "explicit dependence on and sensitivity to the choice of the learning rates" [37]; and a further line removes the rate entirely by recasting the update as a wealth process with the mixture chosen online, no learning-rate hyperparameter anywhere [38]. The narrow claim survives intact: **the field prices the rate against interval length and coverage tracking; nobody prices it against decision movement cost** [6]. The objection's second half must also be answered — if the rate can be eliminated, why tune it? — and the answer is available. Parameter-free methods optimise coverage-tracking without a rate, and nothing guarantees the rate they implicitly select is the one a costly decision wants. The parameter-free line's own concession, that a tuned rate can beat it at short horizons while such tuning cannot be validated online [38], is the opening: the tuning problem does not vanish, it becomes unobservable.

**Objection 5 does not land, and the precision here is the cheapest available signal that the paper knows its own literature.** Andrew et al. Theorem 2 is serious: for an arbitrary seminorm switching cost, no algorithm, deterministic or randomised, achieves sublinear regret and a constant competitive ratio — worst-case performance against an offline optimum — simultaneously; the result is robust to the α-unfair ratio, to static and dynamic comparators, and to lookahead, and holds even for linear costs and scalar actions [30]. But Theorem 7 gives an exception exactly where F7 sits: in strictly **one-dimensional** decision spaces, Randomly Biased Greedy attains sublinear regret with a competitive ratio that grows arbitrarily slowly. ACI's state `α_t` is one scalar. The impossibility does not forbid what F7 needs; it does forbid what F7 says. "Dominates both fast ACI and fixed-α slow quantiles at matched coverage" is unavailable; "sublinear regret with a slowly growing competitive ratio", or an explicitly regime-specific empirical result, is.

**Objection 6 lands, and the honest response is a good one.** Report the a-posteriori certificate `|(1/T)Σ err_t − α| ≤ (B + S_T)/(γT)` with the realised suppressed sum `S_T = Σ_t|suppressed_t|` printed per run [10]. It is reader-checkable, it degrades gracefully, and a regime in which `S_T` grows linearly is itself a publishable finding about when the method must not be used. The naive construction also has a failure mode a reviewer derives in two lines: with `err_t ∈ {0,1}` and α = 0.10 the increment is `+0.1γ` on a covered step and `−0.9γ` on a miss, so **any symmetric threshold in `(0.1γ, 0.9γ)` annihilates every covered-step increment and passes every miss**, producing monotone widening and systematic over-coverage. The plan's proof sketch — "delays but does not prevent adaptation" — is false for that construction. It deletes one direction of adaptation.

Objection 7 is developed in §5, where the replacement framing is stronger than what it replaces.

### 3.F — The caveat on the instrument

Both verdicts rest on a sweep with a demonstrated blind spot. This is a statement about method, not about conclusion. The sweep was **arXiv-centric and abstract-level**, and arXiv searches metadata rather than full text, so a zero-hit result means only "nothing at abstract level" [6]. It missed the closest-titled published work in the field — a PAKDD 2026 Springer chapter on portfolio selection with adaptive conformal prediction, one month old and carrying no arXiv identifier [39]. It returned and then discarded, on a one-line domain judgement, the one paper pairing conformal calibration with an explicit switching cost [16]. Both were retrievable by queries the sweep actually ran. And the **forward-citation screen of the foundational adaptive-conformal paper — the one instrument that indexes across venue types — was never run**, because the academic search API returned HTTP 429 throughout [6][9]. A verdict produced by a method demonstrated to miss the closest-titled work in its own field should not be signed as final. The conclusions still look right; the fix is a mechanism-keyword screen across application domains, and it is a gate blocker [27].

## 4. REFERENCES — the verified set only

**The rule is not negotiable: the bibliography is rebuilt from `audit/REFS_VERIFIED.bib` and nothing else.** Forty-five entries, 20 of them explicitly marked `[ADDED]` — the marker is under-applied, since the unmarked remainder is 25 against the planning document's 22 distinct entries, so the true added count is at least 23 and the file's own marking should be reconciled before the bibliography is rebuilt [7]. The entries were added, each constructed from a record fetched from the arXiv API, DBLP, Crossref or a publisher copy; nothing written from memory [7]. The planning document's list carried 22 distinct entries, of which **7 failed at least one of resolution, metadata and attribution — a 31.8% failure rate** [5]. One failure lands on a programme-committee member's own paper — *Conformal Risk Control*, cited with the author order reversed, and Lihua Lei is both an author and on the committee [5][8] — and a second, the Gârleanu–Pedersen attribution, is the one the venue analysis singles out as certain to be caught by this room in particular [8]. That is why this is not clerical.

| Failed entry | What is wrong | Repair |
|---|---|---|
| Gârleanu & Pedersen (2013) as "the source of the dead-band form" | Assumes **quadratic** costs and derives linear partial adjustment toward an aim portfolio; writes a sentence specifically distinguishing itself from proportional-cost strategies "which exhibit periods of no trading" [40][5] | Constantinides (1986) and Davis & Norman (1990) [21][22]; the soft-threshold form needs no finance citation, being the proximal operator of the L1 norm |
| "Bates, Angelopoulos et al., conformal risk control" | Author order reversed, no year, no venue — and Lihua Lei is both an author and on the programme committee [41][5][8] | Angelopoulos, Bates, Fisch, Lei, Schuster, ICLR 2024 |
| Conformal PID dated 2024 | Preprint July 2023; NeurIPS **2023** [36][5] | Redate |
| Vaze, "Theorem 7 … on cumulative miscoverage" | Theorem 7 exists, is titled "Minimax lower bound", and gives the right rate — but the tight statement is on dynamic regret in threshold space, the coverage-side bound carries an `f_min` factor, and the author's own Remark 11 is titled "The Q(T) lower bound is not stated tightly" [11][5] | Restate precisely; the framing constraint survives, the sentence stating it does not |
| "Schmitt, RWCP" | The method is RWC, and the entry has no stated reason for being in the list [42][5] | Fix or drop |
| "MacLean, Thorp & Ziemba", no locator | The only load-bearing citation with no year, title, identifier or venue — and the mechanism the plan claims to have tested and ruled out [5] | Resolved provisionally to the 2010 chapter [14]; the identification is the audit's inference, not the operator's confirmation [43] |
| arXiv:2502.10947 listed twice | Both descriptions accurate; a list assembled in passes and never read as a list [32][5] | Rebuild from the verified file |

**The substantive failure carries an interpretive point that exceeds the citation.** A quadratic movement penalty gives smooth partial adjustment and a differentiable update far easier to analyse than a thresholded one. Whether C2 penalises movement in L1 (a dead-band) or L2 (smooth partial adjustment) is therefore a live design question, and the wrong citation concealed it. A mis-citation that hides a design decision is more expensive than a wrong year.

**The unresolvable one changes an argument.** MacLean, Thorp & Ziemba warn about errors in the **mean**, not the scale: "Given the extreme sensitivity of E log calculations to errors in mean estimates, these estimates must be accurate"; and "Errors in means versus errors in variances were about 20:2:1 in importance as measured by the cash equivalent value of final wealth" [14][44]. A conformal interval supplies a *scale*. On the source's own numbers the competing channel is roughly an order of magnitude weaker than the plan assumed — so refuting it is easier, and correspondingly less impressive than "the difference between an over-determined observation and an identified mechanism". Both halves of that should be said.

**Because references are unlimited at this venue [8], there is no page cost to citing well — only a sentence cost to engaging.** The must-adds, ordered by how badly their absence reads in this room: Conformal Inverse Optimization, whose co-author is a confirmed speaker [24]; the entire switching-cost line, because a paper proposing a movement-penalised online algorithm that cites none of it reads as unaware of its field [28][29][30][31]; Min et al. and Zhu, Yan & Gao, both of which narrow the novelty claim [15][16]; the PAKDD chapter [39]; the decision-induced-turnover paper promoted from a bare identifier in a trailing clause to a paragraph, because "a decision-focused method churns and damping fixes it" is now published for smart predict-then-optimise, SPO — training a predictor against the decision loss it feeds rather than against prediction error [18][45]; the parameter-free line [37][38]; and Chopra (1993), the antecedent F7 cannot claim [13].

Two more deserve their own sentence, because they are the differentiation that **survived every check**, verified in the sources' own words. Conformal Decision Theory models an agent that can buy or short-sell "with no trading cost" on simulated geometric Brownian motion [46][6]; the nearest conformal portfolio paper assumes investors "can adjust their portfolio holdings without incurring additional transaction costs" [47]. That differentiation is safe in print.

**Still unread in full**, a live gap rather than a formality: the decision-induced-turnover paper, which the prior-art audit rates the single most important comparison for C2 while assessing it from an abstract [18][6]; the PAKDD chapter, behind a JavaScript challenge [39]; the KDD 2023 predict-then-optimise paper surfaced by a partial citation pull and never fetched [27]; and Chopra (1993), paywalled and known only as reproduced [13]. The anomaly preprint was passed forward rather than re-verified in the reference audit [5], though its anomaly text and cost tables were later read directly. **The reference set is in far better shape than the claim set, and it is not finished.**

## 5. CLAIMS — with the demotions that survive scrutiny

The plan mixes computed results, bare assertions, planned work and findings inherited from an unlogged sweep, often in adjacent sentences [10]. Below is the subset where demotion is forced by evidence, not by caution.

| Claim as written | Surviving form | Why |
|---|---|---|
| "Ryan reports this and cannot explain it. Nobody has explained it." | He proposes a hedged, unmeasured, non-turnover mechanism; F7 tests it against a turnover account | He explains it in his abstract and conclusion [4] |
| "No coverage-based criterion — marginal, conditional or adaptive — can select the rate" | "Across rates that all attain nominal coverage to within 0.001, realised decision cost varies by N points of annual growth" | A quantifier loses to Vaze and Srinivas, and to DtACI [11][12][23] |
| "For any online conformal method, the rate is first-order in turnover" | For the tested class only | Untested outside vanilla ACI; DtACI is the sharpest counter-case and must be run [10][23] |
| "The coverage-optimal point sits at the wrong end of the frontier" | Coverage is flat over γ ≥ 0.005, so coverage does not locate a point on the curve at all | Stronger, and what the data show [2] |
| "Formalise the frontier" | A measured curve with no minimax claim, or drop the word | A formalised frontier is Srinivas's object [12] |
| "Runs against the literature's premise that faster adaptation is better" | The field prices the rate against length and coverage tracking; nobody prices it against decision movement cost | False in the strong form [17][33][23][37][38] |
| "The channel is unambiguously transaction cost" | "Consistent with transaction cost; we exclude a variance-channel effect larger than δ", via an equivalence test — one whose null is that the difference exceeds a stated margin — at full Kelly as well as fractional | Rests on a three-point cost grid with two untabulated points [1][10] |
| "`Var(Δq)` rises 330×, so the variance channel is falsified" | Report `Var(q)` at the level alongside `Var(Δq)` at the increment | The plan may be falsifying a statistic the competing channel does not depend on [10] |
| "A quantitative match: 1.0–4.4 points against 0.7–5.3" | Same sign, same order of magnitude, same monotone direction, under a different configuration — better, delete and replace with a pre-registered prediction | Not derivable: the table's paired differences are 0.02, 0.10, 0.43, 1.84, 4.37 [2] |
| "Dead-band exactly as in the Gârleanu–Pedersen solution" | Delete; cite Constantinides and Davis–Norman | False [40][5][21][22] |
| "Dominates both fast ACI and fixed-α slow quantiles" | Sublinear regret with a slowly growing competitive ratio, via the one-dimensional exception; or an explicitly regime-specific empirical result | Theorem 2 forbids the strong form; Theorem 7 licenses the weak one [30] |
| "Prove coverage is retained — the dead-band delays but does not prevent adaptation" | Coverage inherited from ACI because `α_t` is never suppressed; or an a-posteriori certificate | The sketch is false for the naive construction [10] |
| "The design resolves its own question by 5–100×. **Confirmed**" | Delete; set the path count from the smallest difference the paper intends to claim | 0.67×, 2.5×, 5.4×, 9.7×, 13.7× on the plan's own table [2] |
| "arXiv returns 0 for conformal × downstream decision × variance" | Delete, not soften | A single query returns a page of on-topic work [6] |

Five of these need the reasoning spelled out.

**The opening reframe is an upgrade, not a retreat.** The published mechanism appears in the abstract — "when it sizes a position rather than describing a single forecast, the stability of the width matters more than its local sharpness" — and again in the conclusion: "a scale estimator consumed by a nonlinear sizing map is charged for its own estimation variance, so there is an interior optimum in adaptation speed, far slower than that literature recommends" [4]. "Nobody has explained it. I have" does not survive contact with that abstract. But the mechanism is hedged in its own words as "consistent with the results", measured directly for only one device — the holding-period-residual case, standard deviation of daily log-changes in `q` at 0.00391 for the fast setting against 0.00343 for the slow, autocorrelation 0.36 against 0.53 — and conjectured for the rest. The accounting is now settled from the source: seven devices are tabulated; the variance mechanism is attributed to the **first four** — "Every one of the first four devices makes the interval adapt faster, and every one loses, because the sizing map integrates the interval and so charges the variance of q" — while "the last three rows fail for a different reason", and "for the other devices the mechanism is conjectured, not measured" [4]. So **every device the mechanism is claimed for is conjectured, and the one device where it was measured is in the category the author says fails for a different reason.** The same passage carries a refinement F7 should adopt rather than rediscover: "what fails is fast adaptivity, not cross-sectional adaptivity ... It is the speed of the scale estimator that must be slow, not its cross-sectional content" [4]. And it is never connected to turnover, since the cost sweep at 0/5/10/20/50 bps runs only on the two aggregate headline configurations and is never decomposed per losing device [4]. So the turnover account is not scooped; only the priority claim is. **A specific falsifiable disagreement with a named mechanism beats an unfalsifiable universal negative one reviewer can puncture** — and it moves the falsified variance hypothesis from defensive aside to centrepiece.

**The power claim is materially overstated, and the design is still good.** The effect-to-standard-error ratios implied by the plan's own table are 0.67×, 2.5×, 5.4×, 9.7× and 13.7× [2]. Maximum 13.7×; no 100×; two of five below the stated 5× floor. That is a perfectly adequate design; it is not the design the preflight section marks "Confirmed". Operationally, γ = 0.020 is where a realistic practitioner sits and it is the unresolved comparison at 60 paths, so the path count must be set from the smallest γ difference the paper intends to claim, not the largest.

**Keep the falsified-variance finding, but not as stated.** Recording a refuted competing explanation is an asset [10]. The sharpest objection to it is not the missing table: **the plan measures `Var(Δq)`, the variance of the quantile's increment, while the Kelly overbetting channel is driven by the dispersion of the estimate's *level*, since overbetting arises from `E[μ/σ̂²] > μ/σ²` by Jensen's inequality** [10][14]. A 330× rise in increment-variance is compatible with a much smaller rise in level-variance, so the plan may be falsifying a channel it has not measured. Add that "flat within 1 SE" is a failure to reject presented as a refutation, with no power statement, and that the null is conditional on an unstated Kelly fraction — at κ = 0.15 the overbetting channel is nearly invisible [4]. The fixes are cheap and fully specified: report `Var(q)` alongside `Var(Δq)`, run two one-sided tests with a stated equivalence margin, and report the null at full Kelly as well.

**One claim should be added rather than demoted, and it is counter-evidence.** In the one place the published harness actually tests the turnover reflex — its Config A versus Config B comparison across the cost sweep — the 2.56-point growth gap at 0 bps becomes 2.61 points at 5 bps, so the turnover-attributable share is `0.0005/0.0261 ≈ 1.9%`: **98.1% of the effect is present at zero transaction cost** [4]. The sealed window reproduces the pattern (0 bps gap 0.014, 5 bps 0.015, turnover share ≈ 7%). The author's diagnosis is regime timing — "the timing is bad, and measurably so — trailing miscoverage peaks after a shock, during the rebound, so it sells the bottom" — neither variance-charging nor turnover cost [4]. The comparison sits on an orthogonal axis, a drawdown dial rather than adaptation speed, so it does **not** refute C1. But it is a published, quantified, in-domain demonstration that "activity correlates with growth loss, therefore transaction costs" is unreliable in this exact apparatus, and any reader of that paper will find it. Stating it and bounding it is far stronger than omitting it.

**The multiple-comparisons exposure costs one sentence and buys the objection.** The anomaly is a development-window result: the numbers came from an autonomous search over roughly 200 configurations, only the winning configuration was re-tested out of sample, and on the sealed window the calibration transferred (coverage 0.745 against 0.750) while growth fell to roughly 30% of its development value, below both passive bars [4]. F7 depends on the *relative ranking*, a weaker requirement than the absolute growth that failed, so the anomaly survives as an object worth explaining. One honest sentence pre-empts the objection entirely.

**One pattern matters more than any single item.** Of eight claims inherited from an unlogged sweep, one is false, two are materially overstated, one is unresolvable as cited, and two are verified [10]. A sweep with that error rate cannot carry a novelty section.

## 6. CURRENT STATE — done versus asserted

### 6.A — What is genuinely done, and it is not nothing

A complete file inventory, regenerable from a committed script [20]. A numeric trace of all 88 numbers with an explicit orphan count [2]. A claim ledger tagging every proposition `computed` / `asserted` / `planned` / `inherited`, with load-bearingness and evidence [10]. A 45-entry bibliography built from fetched canonical records, with a rejection log [7][5]. A prior-art sweep with logged queries and result counts, and four amendments generated by adversarial re-examination of its own conclusions [6]. Venue facts read from OpenReview's submission-invitation records, with the style file inspected at source [8]. Gates written *before* the work, with pre-written acceptance criteria and a standing rule that no automated session may record one as passed [20]. Three technical investigations that between them closed the C2 theorem question. A compute plan [48]. None of these is a research result; all of them are checkable. **The project now knows precisely what it does not have**, which is a real asset and rarer than it sounds.

### 6.B — What survived every check that was run

Five positions came through unweakened, and a reader who takes only the demotions away has read this report wrong.

- **The zero-cost differentiation from the two nearest conformal-portfolio precedents**, verified in the sources' own words [46][47].
- **The narrow form of the step-size claim**: the field prices γ against interval length and coverage tracking, and nobody prices it against decision movement cost [6].
- **The switching-cost impossibility does not forbid what F7 needs.** The one-dimensional exception covers ACI's scalar state exactly [30].
- **The venue choice is right on merit.** ML×OR is the only room that can evaluate both halves of the paper and the only one with a journal pathway [8]. It is also the room certain to catch every unfixed defect, which is an argument for arriving finished rather than for going elsewhere.
- **C1 itself.** Nothing in the audit suggests C1 is wrong. The internal arithmetic is consistent in all five comparisons, the growth column is coherent with an untabulated zero-cost null, and the implied per-path standard deviations are plausible [1].

### 6.C — What is asserted, quantified

| Object | Status | What would verify it | Cost |
|---|---|---|---|
| The simulator named as the source of the central table | **Does not exist here.** Ten searches negative; no scratch directory exists anywhere under the home directory [1] | Recovery from other hardware, or a rebuild | Operator answer, then ~1 week |
| All 23 C1 table cells; all 7 named C1 claims | **NOT-EMITTED**, every one. The only positive information is internal: the paired-difference column agrees with the growth column in all five comparisons [1] | A frozen-spec rebuild hitting the stated reproduction targets [19] | Days |
| The zero-cost null ("all diffs within 1 SE") | **Orphan.** No 0 bps table anywhere — and this is the paper's identification argument [2] | A displayed table plus an equivalence test with a stated margin [20] | Hours post-rebuild |
| The 5 bps intermediate case | **Orphan.** No 5 bps table anywhere [2] | A displayed table; monotonicity over ≥ 5 cost levels, not 3 [19] | Hours |
| The 330× rise in `Var(Δq)` | **Orphan.** No variance table anywhere; sole basis for the falsified-variance finding [2] | Both `Var(q)` and `Var(Δq)`, normalised and absolute [20] | Hours |
| "1.0–4.4 points" | **Orphan, lower bound not derivable.** The paired differences are 0.02, 0.10, 0.43, 1.84, 4.37; nothing yields 1.0 [2] | The run that produced 1.0, or deletion | Immediate |
| "5–100× power, Confirmed" | **Orphan and materially overstated** — 0.67× to 13.7× on the plan's own table [2] | Restatement; path count reset from the smallest claimed effect | Immediate |
| "~90 seconds"; "2 weeks remaining"; "~15 lines" | **Orphans**, all conditioned on a file that does not exist [2][1] | A rebuild plus a timing record | After rebuild |
| Prior-sweep hit counts ("100 titles"; two zero-hit claims) | **Orphans** inherited with no log, no output, no query record; one demonstrably false [2][6] | Logged queries committed to the audit directory | Hours |

**The tally, three ways** [2]: 0 of 88 reproduced from code (0.0%); 12 of 88 orphans (13.6%); and the cut that matters, **5 of 5 load-bearing quantities whose supporting table is not shown anywhere are orphans — 100%**. Four of those five are exactly the claims the plan calls its strongest evidence.

### 6.D — The identity finding, which cuts both ways

At 15 bps the growth difference predicted by turnover alone is `−0.0015 × (turnover_γ − turnover_0.005)`. Residuals against the plan's stated paired differences are −0.0001, +0.0004, +0.0009, +0.0002 and −0.0023, against effects up to 0.0437 [2] — in points, between −0.23 and +0.09 against an effect of 4.37. **Gross growth is flat across the γ grid to within about 5% of the effect size.**

*For* the plan: that is exactly what the untabulated zero-cost null asserts, so the table is coherent with a claim the document never displays — mild evidence the zero-cost run was really done [2]. *Against* it: the growth column carries essentially no information beyond the turnover column, and a reviewer will call "growth falls because turnover rises and turnover is charged" an accounting identity rather than a finding. **The result that is not an identity is that coverage does not constrain turnover.** This is the highest-value structural recommendation available and it costs nothing to adopt.

### 6.E — One risk that could make the headline an artefact

ACI's `α_t` is a random walk that leaves `[0,1]` unless constrained, and the plan states no clipping rule. At γ = 0.400 with α = 0.10, each step moves `α_t` by +0.04 when covered and −0.36 when missed, so a single miscoverage drives it negative and the arm may spend much of its time pinned at whatever bound the implementation imposes [19]. Interval width, position and turnover would then be governed by the clip rather than by the ACI dynamics — and **γ = 0.400 supplies the 4.4-point swing, the 13.7 standard errors and the turnover of 31.0.** If those are clip artefacts, the headline is an artefact. The diagnostic is one line: report time-at-clip per arm.

### 6.F — Gates, schedule and compute

G0 is `ready for review` and **not signed**; G1 through G6 are `not started`; no gate has been recorded as passed [20]. Reproducing and hardening C1 is the critical path, because nothing downstream can be evidenced without a simulator. The plan's self-assessment — "the central experiment is already done", "est. effort 2 weeks", "day-1: add the dead-band arm, it is ~15 lines" — is conditioned on a file that does not exist, so every schedule estimate downstream of it is unreliable [1][3]. The real day-one task is building a simulator against a specification with thirteen underdetermined choices, several of which change the answer [19].

Compute is not a constraint and should stay that way. The workload is a scalar recursion, and the full factorial the protocol implies is about 16,800 path-runs — single-digit hours single-threaded, minutes across a laptop's cores, zero spend [48]. This project is the exception to a GPU-default routing policy: branch-heavy scalar recursion with negligible arithmetic intensity leaves an accelerator idle. The only thing that could push it off a laptop is a bootstrap layer over the full grid, which wants a many-core CPU box.

### 6.G — The assessment

The audit cannot distinguish "run elsewhere and lost" from "never run" [1]. The consequence is identical either way, though the distinction changes how the operator should read the plan. What the audit does establish is that **no one can currently tell the difference between a real result and a self-consistent table**, and that four of the five statements the paper leans on hardest have never been printed. The right posture is neither "rebuild the code, the result is fine" nor "the result is fabricated": the project has a good design, a well-specified experiment, and zero evidence, and all three facts belong in the paper's own methods section.

## 7. FUTURE PIPELINE — ordered plan for session 2 onward

Ordered by what can end a branch soonest, not by what is most interesting. The first phase costs hours and can collapse everything below it.

### 7.A — Phase 0: hours, zero engineering, before anything is built

1. **Request the author's `results.tsv`.** Appendix A of the anomaly preprint offers it "available from the author on request", and the harness that produced the per-device growth table computed per-device turnover as a side effect, because the cost model is 5 bps × turnover applied uniformly [4][27]. **This is the cheapest high-value action available to the project**: one email that could settle the central variance-versus-turnover dispute on real multi-asset data without rebuilding anything. It carries long external latency and therefore goes first, not when convenient.
2. **Establish whether the original simulator exists on other hardware** [43]. Under recovery, most current uncertainty collapses at once; under loss, a rebuild becomes the critical path and every estimate is redone. These are different projects and the audit cannot distinguish them [1].
3. **Read the three unread must-cites in full** — the decision-induced-turnover paper, the PAKDD chapter, the KDD 2023 predict-then-optimise paper [18][39][27]. One command each, zero discovery cost, and the first currently carries a novelty assessment resting on an abstract [6].
4. **Decide the dead-band fork in one written paragraph** [20][43]. **This report does not decide it — the fork is operator question Q4 and is reserved there** [43]. What this run can say is that the evidence now points one way: two independent depth investigations found no proof route for the suppressed-update branch (§3.D), which leaves accumulating `α_t` unconditionally and dead-banding only the readout as the sole construction with a known analysis. Deciding after implementation begins wastes the implementation.
5. **Derive the analytic turnover-versus-width relation on paper** (§3.C). One hour, and it removes a trap the paper would otherwise walk into at review.
6. **Delete the four claims that need no experiment to fix**: the 1.0 lower bound, "5–100×", "nobody has explained it", and the Gârleanu–Pedersen attribution [2][5].

### 7.B — Phase 1, days 1–2: freeze before you build

Fix all thirteen underdetermined choices R1–R13 in a committed configuration whose timestamp precedes the first results record [19][20]. Rebuilding against a table you have already read is a fitting exercise; if parameters are tuned until the table appears, the agreement carries no evidential weight and **the gate has failed regardless of the numbers** [20].

**R1 is the highest-severity item and should be run both ways.** If the interval is `q_t = ŝ_t·z(α_t)` with a Gaussian `z`, it is not split conformal at all — split conformal calibrates on a held-out split and reads the interval off as an empirical quantile of held-out nonconformity scores, with no distributional assumption; and that empirical quantile, being a **step function** of `α_t`, already has a dead-band for free and may absorb part of the effect the paper attributes to γ [27][49]. A conformal-literate reviewer will catch this immediately.

### 7.C — Phase 2, days 3–6: the simulator and its three kill-shots

Build the module, then the five required tests before any number is believed — common-random-number bit-identity across arms, zero-cost invariance, the cost identity `gross − net = rate × turnover`, γ = 0 degeneracy, and a leakage check that perturbs `y_t` and confirms `q_t` is unchanged — and emit one never-overwritten JSON per run carrying the configuration, the commit hash, wall-clock time, library versions and **per-path raw quantities**, not only aggregates [19]. The absence of exactly this record is why the audit has nothing to check. Then, in this order:

1. **The conditional discriminator** (§3.C). If `Σ|Δq|` carries no information about net growth once mean interval length is conditioned on, C1 reduces to a published theorem times a cost rate. Better known in week one than at review.
2. **Time-at-α-clip per arm** (§6.E). A two-line diagnostic that can invalidate the paper's most-quoted number.
3. **The zero-cost arm as an equivalence test with a stated margin**, reporting `Var(q)` at the level and `Var(Δq)` at the increment side by side [20][10].

Then reset the path count from the γ = 0.020 comparison rather than the γ = 0.400 one [2], extend the cost grid to at least five levels before claiming monotonicity, and only then compare against the plan's table.

### 7.D — Phase 3, days 7–11: the real-data arm

Replicate the published configuration exactly, and **pre-register the prediction before looking at the per-device numbers** [20][4]. Handle the disclosed `z = 1.2816` versus `1.1503` inconsistency explicitly and both ways — silently correcting it makes the replication not a replication. Carry the development-window and multiple-comparisons qualifications into the paper (§5). If Phase 0's request lands, this phase shortens sharply and gains the one analysis the original author did not run: his cost sweep decomposed per losing device [27].

### 7.E — Phase 4, parallel and non-blocking, but before the framing locks

Run the forward-citation screen of the foundational adaptive-conformal paper from an environment with a working academic search key, and extend the sweep beyond arXiv to Springer, INFORMS, quantitative-finance journals and SSRN [27][20]. Re-run it on **mechanism** keywords across application domains rather than on conformal-plus-finance: a moving uncertainty estimate driving a decision that pays to move recurs in wireless scheduling, inventory control, data-centre right-sizing and electricity dispatch, and a domain-screened sweep will keep missing it, as it already has twice [16][39].

### 7.F — Phase 5: C2, deliberately small

Day one of C2 is the asymmetry test: implement the symmetric threshold, measure the predicted systematic over-coverage, then fix it with thresholds in roughly the ratio α : (1−α) [10]. Then the readout construction, then the open readout-interval coverage question (§3.D). Attempt the Online Balanced Descent potential-function template for the bound [31] — it converts "no known approach" into "a template to try". If it fails, demote deliberately to the a-posteriori certificate, and state any comparative claim compatibly with the one-dimensional exception [30]. All of it lives in the supplement, or in a second paper. The journal nomination should be planned as *Stochastic Systems*; the upgrade to *Mathematics of Operations Research* was conditional on a proved rather than asserted coverage theorem, and that condition will not now be met [8].

### 7.F-bis — Phase 6, days 12–14: the draft, in dependency order

Sub-question 8 asks for an ordered plan covering experimental **and** writing work, and the
writing has a dependency structure of its own. It is not a single block at the end.

| # | What is written | Unblocked by | Why here |
|---|---|---|---|
| 1 | Setup, the anomaly, and the **corrected opening framing** | **Nothing** — day 0 | It depends only on §5's reframe and on reading the anomaly paper, both of which are done. It is the one section writable before any experiment exists, and it is the section that currently contains a false claim. Write it first. |
| 2 | Related work: the four distinguishing sentences | Nothing — day 0 | Zaffran, Min et al., the anomaly paper, the decision-induced-turnover paper. Also gated on G1's citation screen for its final form, but draftable now. |
| 3 | Table 1 and the mechanism section | Phase 2 (the simulator) | The paper's centre. Nothing else in the body can be sized until Table 1 exists. |
| 4 | The identification subsection — zero-cost equivalence test, `Var(q)` and `Var(Δq)` | Phase 2 | Closes the sharpest objection to the falsified-variance result. |
| 5 | The real-data section | Phase 3 or 4 | Written against whichever of the replication or the requested per-device data lands first. |
| 6 | Limitations | Phase 3 | The development-window and multiple-comparisons caveats, which cost one paragraph and pre-empt a reviewer who reads the anomaly paper. |
| 7 | Supplement | Continuous | Everything displaced by the four-page budget: the frozen R1–R13 configuration, the five executable tests, the wider cost grid, the equivalence-test power calculation, time-at-clip and time-at-cap, the dead-band asymmetry result. Space is free here and each item is a reviewer answer. |

Items 1 and 2 are the argument that the writing does not wait for the experiment. They are
also the two sections where this audit found errors of fact rather than errors of evidence,
which makes them the cheapest quality gain available.

### 7.G — Gate mapping

| Phase | Gate | Blocking condition |
|---|---|---|
| 7.A item 3; 7.E | G1 — prior art | Forward-citation screen unrun; three must-cites unread [6][27] |
| 7.B; 7.C | G2 — reproduction | Frozen spec timestamped before first run; five tests passing; conditional discriminator reported [19][20] |
| 7.D | **G4** — Ryan-configuration replication complete | Pre-registered prediction recorded before comparison [20] |
| 7.F | **G3** — C2 implemented; theorem proved or claim demoted; journal nomination fixed | Fork decided; asymmetry test run; theorem or a-posteriori certificate [10] |
| 7.F-bis | **G5** — full draft at four pages, compliance checklist clear | Main body compiles to four pages in the unmodified style file; `\workshoptitle{}` set alongside `\title{}`; checklist walked line by line; bibliography rebuilt from the verified file only [8][7] |
| Submission | **G6** — submission | G0–G5 signed by the operator; journal nomination selected; deadline met without relying on the expiry buffer [20][8] |

Note that G3 and G4 are **not** in execution order: G4 (the replication) is reachable
before G3 (the method) because the replication depends only on the frozen simulator and
the published configuration, whereas the method depends on the fork decision. The gate
numbering follows `docs/GATES.md`; the phases follow dependency. Both orderings are
correct and they differ.

### 7.H — The calendar arithmetic, stated once

The deadline is 2026-09-01 11:59 UTC, with a 30-minute expiry buffer that is not usable time [8]. From 2026-08-19 that is thirteen days. Against it: Phase 0 is hours but carries external latency; Phases 1–2 are four to six working days of engineering; Phase 3 is three to five more, most of it data acquisition and reconciliation rather than compute [48]; writing four pages to the standard this audit demands is three days; and sign-off is required at three gates, which is human latency the schedule cannot compress [20]. That is ten to fourteen working days of effort with zero slack, against thirteen calendar days.

Three further facts belong in the operator's hand. The alternative venue with the best conformal room closes **two days earlier**, so switching venues does not buy time [8]. The later-closing venues buy four to five days at the cost of a materially worse room [8]. And the workshop is non-archival and has now run twice, so a one-cycle deferral costs a year of calendar and essentially nothing else, since the target journal accepts direct submissions independently of the workshop [8]. If the deadline is attempted, the only honest version that fits is **C1 on synthetic data alone** — discriminator and clip diagnostic reported, zero-cost arm as an equivalence test, no real-data arm, no C2, and the paper explicitly labelled a mechanism study. That is buildable in thirteen days. Its weakness is the missing real-data arm, which is the half an operations-research room weights most. The decision is the operator's, and this report does not make it.

### 7.I — The forward view, past this cycle

The most durable thing in this project is neither claim; it is the **reporting convention**. The parameter-free line is actively moving to eliminate the step size entirely [37][38], and if it succeeds, a paper whose contribution is "how to choose γ" has a short half-life. But a parameter-free method still has a realised interval path with a realised variation, and nothing in its guarantee bounds that variation — so a decision with an incumbent state still pays for it and still cannot see it in the reported numbers. Stated at the level of the mechanism rather than the application, F7 becomes a proposal about what online uncertainty quantification should *report*: coverage, length, **and path variation**. That framing survives every method change beneath it, and it is immune to "this is just transaction costs", because transaction cost becomes one instance rather than the claim.

The surrounding literature is converging on the same dissatisfaction from three independent directions — run-to-run interval instability [15], miscoverage–regret frontiers arguing that a prespecified coverage target offers little guidance [26], and decision-focused methods that visibly churn and need damping [18][45]. A four-page paper that measures the third quantity on a decision with memory, and shows the standard tuning criterion is invariant to it, plants a flag in a space three separate lines of work are approaching independently. That is worth more than the dead-band. The paper after this one ports the diagnostic to a non-financial domain — inventory reorder points, capacity right-sizing, electricity dispatch, robot policy switching [46] — converting a finance-flavoured curiosity into a general evaluation result and discharging the parameter-free objection in the same move. On present evidence that second paper is worth more than C2 ever was.

## Failures and gaps in this run

- **The forward-citation screen of the foundational adaptive-conformal paper was never run.** One academic search API returned HTTP 429 throughout, a second returned an obviously incomplete 27-citation record missing papers already known to exist, a third's quota was exhausted, and SSRN refused every direct request with HTTP 403 [6]. This is the largest single hole and the one instrument that indexes across venue types; every novelty verdict here is conditioned on it.
- **The prior-art sweep was arXiv-centric and abstract-level**, missed the PAKDD chapter entirely [39], and discarded a conformal-plus-switching-cost paper on a one-line domain judgement [16]. Both were retrievable by queries the sweep actually ran [6].
- **Four primary sources remain unread in full**: the decision-induced-turnover paper [18], the PAKDD chapter behind a JavaScript challenge [39], the KDD 2023 predict-then-optimise paper [27], and Chopra (1993), paywalled [13].
- **The cheapest available experiment was not attempted.** The author's per-device results file is offered on request and almost certainly carries the column that would discriminate the two competing mechanisms without any rebuild [4].
- **The analytic turnover-versus-width relation in §3.C is a reading of two established results, not a result in either** [17][9]. It needs checking before it is relied on, and is offered as a design input to the discriminator rather than as an established fact.
- **The 1.0 lower bound of "1.0–4.4 points" is still unexplained** and is not derivable from the plan's table [2]. It may come from an unshown run at a different cost level, or it may be an error; the audit cannot distinguish these.
- **The Config A/B counter-evidence is one analogical data point** on an orthogonal axis, generalised by argument rather than measurement. Confidence in the directional reading is moderate, against high confidence in the negative claim that the published tables cannot discriminate the channels [4].
- **The readout-interval coverage question is open.** Whether `1{S_t ≤ h(α_t)}` admits its own bound was flagged but not resolved, and no source read here answers it.
- **The source target for this run was deliberately reduced** to avoid re-deriving the reference audit and the prior-art sweep, both established inputs. This report therefore adds fewer new external sources than it otherwise would, by design.
- **One fetch defect reproduced and was routed around**: a non-arXiv PDF returned junk content and had to be sourced by another route. Two automated analysis passes failed mid-run on API errors and were re-run; both recovered, at a cost in session time. **Of four planned late-stage review passes, one was run.** The adversarial reading was discharged earlier — by the dedicated adversarial draft, which adjudicated eight named objections, and by the corpus critic, which was tasked specifically with finding sources that would overturn this report's conclusions and found three, two of which changed the verdicts. The one pass that was run, the instruction check, returned **twelve findings — two critical, six major, four minor — and all twelve were applied.** The two critical ones were a gate ladder that contradicted the gates file on three of six rows and silently erased the writing gate, and a novelty verdict that had dropped the OCCUPIED leg of its own two-legged conditional. One major finding was a scope violation: the report had closed an operator question it was required to leave open. **A report whose first serious check found two critical defects should be read as one that has had one check, not four.**
- **No experiment was run and no gate was advanced.** G0 remains `ready for review` pending explicit operator sign-off; everything after it is `not started` [20]. Three venue-compliance questions are unresolved — in-person presentation, reciprocal reviewing, and whether an arXiv preprint affects eligibility under the "previously published" language, the last of which interacts with the decision to keep the repository public [8][27]. Co-author management is untouched: the venue is non-anonymous and submission requires co-author approval, and no co-author has been contacted or named in the project record [43].
- **This report weights novelty and evidence heavily.** It does not score the project's engineering hygiene, gate discipline, or willingness to audit its own inherited claims — all unusually good, and none of which appears in a review.

## Sources

[1] `audit/REPRO_C1.md` — C1 reproduction attempt; ten filesystem search commands, all negative; every table cell NOT-EMITTED (repository, established input).
[2] `audit/NUMBERS.md` — numeric-claim trace across 88 numbers, with orphan counts, the cost-identity arithmetic and the power recomputation (repository, established input).
[3] `docs/PLAN_ORIGINAL.md` — the F7 planning document under audit (repository).
[4] Robert Jacob Ryan. "Conformal Kelly: Conformal Prediction Intervals as the Scale in Fractional Kelly Position Sizing." arXiv:2608.01494 (q-fin.PM), 2026. https://arxiv.org/abs/2608.01494
[5] `audit/REFS_REJECTED.md` — reference-audit failures across resolution, metadata and attribution checks (repository, established input).
[6] `audit/PRIOR_ART.md` — three independent prior-art sweeps with CLEAR / NARROW / OCCUPIED verdicts and four self-generated amendments (repository, established input).
[7] `audit/REFS_VERIFIED.bib` — 45 verified entries, 23 marked `[ADDED]`, each built from a fetched canonical record (repository, established input).
[8] `docs/VENUE.md` — six candidate venues scored against OpenReview submission-invitation records; ML×OR compliance checklist and style-file inspection (repository, established input).
[9] Isaac Gibbs, Emmanuel Candès. "Adaptive Conformal Inference Under Distribution Shift." *NeurIPS*, 2021. arXiv:2106.00170. https://arxiv.org/abs/2106.00170
[10] `audit/CLAIMS.md` — claim ledger tagging every proposition `computed` / `asserted` / `planned` / `inherited`, with load-bearingness and evidence (repository, established input).
[11] Rahul Vaze. "Simultaneous Coverage and Efficiency Guarantee in Online Conformal Prediction." arXiv:2607.26577, 2026. https://arxiv.org/abs/2607.26577
[12] Vaidehi Srinivas. "Online Conformal Prediction with Efficiency Guarantees." *SODA*, 2026. arXiv:2507.02496. https://arxiv.org/abs/2507.02496
[13] Vijay K. Chopra. "Improving Optimization." *The Journal of Investing* 2(3):51–59, 1993. doi:10.3905/joi.2.3.51
[14] Leonard C. MacLean, Edward O. Thorp, William T. Ziemba. "Good and Bad Properties of the Kelly Criterion." 2010; reprinted in *The Kelly Capital Growth Investment Criterion*, World Scientific, 2011. doi:10.1142/7598
[15] Yizhou Min, Yizhou Lu, Lanqi Li, Zhen Zhang, Jiaye Teng. "Questioning the Coverage-Length Metric in Conformal Prediction: When Shorter Intervals Are Not Better." arXiv:2601.21455, 2026. https://arxiv.org/abs/2601.21455
[16] Gangyong Zhu, Jia Yan, Shijian Gao. "Stay or Switch: Online Conformal Bayesian Optimization Guided Fluid Antenna Configuration." arXiv:2607.26547, 2026. https://arxiv.org/abs/2607.26547
[17] Margaux Zaffran, Olivier Féron, Yannig Goude, Julie Josse, Aymeric Dieuleveut. "Adaptive Conformal Predictions for Time Series." *ICML*, 2022. arXiv:2202.07282. https://arxiv.org/abs/2202.07282
[18] Yi Wang, Takashi Hasuike. "Decision-Induced Ranking Explains Prediction Inflation and Excessive Turnover in SPO-Based Portfolio Optimization." arXiv:2605.01176 (q-fin.PM), 2026. https://arxiv.org/abs/2605.01176
[19] `audit/RECONSTRUCTION_SPEC.md` — free-choice register R1–R13, implementation contract, five required tests and reproduction targets (repository).
[20] `docs/GATES.md` — stage gates G0–G6 with acceptance criteria written before the work (repository).
[21] George M. Constantinides. "Capital Market Equilibrium with Transaction Costs." *Journal of Political Economy* 94(4):842–862, 1986. doi:10.1086/261410
[22] M. H. A. Davis, A. R. Norman. "Portfolio Selection with Transaction Costs." *Mathematics of Operations Research* 15(4):676–713, 1990. doi:10.1287/moor.15.4.676
[23] Isaac Gibbs, Emmanuel Candès. "Conformal Inference for Online Prediction with Arbitrary Distribution Shifts." *JMLR*, 2024. arXiv:2208.08401. https://arxiv.org/abs/2208.08401
[24] Bo Lin, Erick Delage, Timothy C. Y. Chan. "Conformal Inverse Optimization." *NeurIPS*, 2024. arXiv:2402.01489. https://arxiv.org/abs/2402.01489
[25] Christopher Yeh, Nicolas Christianson, Alan Wu, Adam Wierman, Yisong Yue. "End-to-End Conformal Calibration for Optimization Under Uncertainty." *TMLR*, 2025. arXiv:2409.20534. https://arxiv.org/abs/2409.20534
[26] Wenbin Zhou, Shixiang Zhu. "Calibrating Decision Robustness via Inverse Conformal Risk Control." arXiv:2510.07750, 2025. https://arxiv.org/abs/2510.07750
[27] `docs/OUTSTANDING.md` — outstanding technical items O1–O21, ranked by blocking status (repository).
[28] Adam Kalai, Santosh Vempala. "Efficient Algorithms for Online Decision Problems." *JCSS* 71(3):291–307, 2005. doi:10.1016/j.jcss.2004.10.016
[29] Sascha Geulen, Berthold Vöcking, Melanie Winkler. "Regret Minimization for Online Buffering Problems Using the Weighted Majority Algorithm." *COLT*, 2010.
[30] Lachlan L. H. Andrew, Siddharth Barman, Katrina Ligett, Minghong Lin, Adam Meyerson, Alan Roytman, Adam Wierman. "A Tale of Two Metrics: Simultaneous Bounds on Competitiveness and Regret." *COLT*, 2013. arXiv:1508.03769. https://arxiv.org/abs/1508.03769
[31] Niangjun Chen, Gautam Goel, Adam Wierman. "Smoothed Online Convex Optimization in High Dimensions via Online Balanced Descent." *COLT*, 2018. arXiv:1803.10366. https://arxiv.org/abs/1803.10366
[32] Ramya Ramalingam, Shayan Kiyani, Aaron Roth. "The Relationship Between No-Regret Learning and Online Conformal Prediction." *ICML*, 2025. arXiv:2502.10947. https://arxiv.org/abs/2502.10947
[33] Anastasios N. Angelopoulos, Rina Foygel Barber, Stephen Bates. "Online Conformal Prediction with Decaying Step Sizes." *ICML*, 2024. arXiv:2402.01139. https://arxiv.org/abs/2402.01139
[34] "Mirror Online Conformal Prediction with Intermittent Feedback." arXiv:2503.10345, 2025. https://arxiv.org/abs/2503.10345
[35] "Staggered Integral Online Conformal Prediction for Safe Dynamics Adaptation with Multi-Step Coverage Guarantees." arXiv:2604.06058, 2026. https://arxiv.org/abs/2604.06058
[36] Anastasios N. Angelopoulos, Emmanuel J. Candès, Ryan J. Tibshirani. "Conformal PID Control for Time Series Prediction." *NeurIPS*, 2023. arXiv:2307.16895. https://arxiv.org/abs/2307.16895
[37] Aleksandr Podkopaev, Darren Xu, Kuang-Chih Lee. "Adaptive Conformal Inference by Betting." arXiv:2412.19318, 2024. https://arxiv.org/abs/2412.19318
[38] Bhawesh Bharti, Aniket Pal, Jonathan Tenegzi, Jeremias Sulam. "Parameter-Free and Group-Conditional Online Conformal Prediction." arXiv:2606.00419, 2026. https://arxiv.org/abs/2606.00419
[39] Yusen Jia, Bingyan Han. "Portfolio Selection with Adaptive Conformal Prediction." *PAKDD 2026*, LNCS 16603:312–323, Springer, 2026. doi:10.1007/978-981-92-2014-4_25
[40] Nicolae Gârleanu, Lasse Heje Pedersen. "Dynamic Trading with Predictable Returns and Transaction Costs." *The Journal of Finance* 68(6):2309–2340, 2013. doi:10.1111/jofi.12080
[41] Anastasios N. Angelopoulos, Stephen Bates, Adam Fisch, Lihua Lei, Tal Schuster. "Conformal Risk Control." *ICLR*, 2024. arXiv:2208.02814. https://arxiv.org/abs/2208.02814
[42] Marc Schmitt. "Taming Tail Risk in Financial Markets: Conformal Calibration for Nonstationary Portfolio VaR." arXiv:2602.03903 (q-fin.RM), 2026. https://arxiv.org/abs/2602.03903
[43] `docs/OPEN_QUESTIONS.md` — operator decisions Q1–Q8 the characterisation session declined to make on its own authority (repository).
[44] Vijay K. Chopra, William T. Ziemba. "The Effect of Errors in Means, Variances, and Covariances on Optimal Portfolio Choice." *The Journal of Portfolio Management* 19(2):6–11, 1993. doi:10.3905/jpm.1993.409440
[45] Adam N. Elmachtoub, Paul Grigas. "Smart 'Predict, then Optimize'." *Management Science* 68(1):9–26, 2022. doi:10.1287/mnsc.2020.3922
[46] Jordan Lekeufack, Anastasios N. Angelopoulos, Andrea Bajcsy, Michael I. Jordan, Jitendra Malik. "Conformal Decision Theory: Safe Autonomous Decisions from Imperfect Predictions." *ICRA*, 2024. arXiv:2310.05921. doi:10.1109/ICRA57147.2024.10610041
[47] Masahiro Kato. "Conformal Predictive Portfolio Selection." arXiv:2410.16333 (q-fin.PM), 2024. https://arxiv.org/abs/2410.16333
[48] `docs/COMPUTE.md` — compute plan; CPU-only, zero spend (repository).
[49] Vladimir Vovk, Alexander Gammerman, Glenn Shafer. *Algorithmic Learning in a Random World.* Springer, 2005 (2nd ed. 2022).
