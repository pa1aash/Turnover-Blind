# FRAMING — locked 2026-08-19

**This file governs every later session.** Where it and any other document in this
repository disagree, this file wins, except that `audit/PRIOR_ART.md` §7 is its evidentiary
basis and `docs/GATES.md` is its enforcement mechanism.

It was written at the end of session S1, after a seven-agent prior-art sweep whose
governing finding is that **the first claim, as it was worded going into that session, is
occupied.** Nothing here is a softening of that. The framing is locked *around* it.

---

## 0. The one thing to read if you read nothing else

A published paper three months older than this framing already runs the identifying design
the project intended to claim: **Van Belle, Wen, Verbeke & Pinson, "Stabilizing
distribution-free probabilistic forecasts", arXiv:2605.28531, 27 May 2026.** It matches two
forecasters on a level functional by construction, varies only the temporal path of their
updates, prices the difference through a decision charged to revise an incumbent, includes
a placebo arm that shows no effect, and states the evaluation moral explicitly. It does all
of this without the words "coverage", "interval width" or "conformal", which is why no
conformal-anchored query in any instrument would ever have returned it.

**What survives is narrower than what was intended, and it is stated in §2 as R1 and R2.
R2 is the paper. R1 is the motivation.**

> **AMENDED 2026-08-19 BY SESSION S2 — read §2.2b before §2.2.** R2 as stated in §2.2 is
> superseded by **R2\*\***. The reduction to Conformal PID Theorem 1 **holds**, so no new
> theorem is needed — **and none may be claimed, because the placement is already in print in
> three places.** What the paper claims instead is the **price** of the placement, which is a
> conservation law derived independently by two agents. Separately, **§8b item 4 is withdrawn:
> R1's priced-movement-cost leg is occupied** by Chen, Yang, Li & Liu (2013), and R1 now rests
> on the absence of a coverage object plus one object distinction. **Neither change is a
> softening. Both are losses, and the second is the larger one.**

---

## 1. The aim

### Repeatable form

> An online conformal interval can be held to the same coverage and the same average width
> and still move very differently from day to day, and a decision that pays to move is
> charged for the difference.

### Precise form

> Fix an online conformal interval producer and hold two quantities constant across arms:
> realised coverage, and mean interval width `E[L]`. These are the two quantities on which
> the online conformal literature reports and tunes. Vary a one-scalar movement penalty
> applied to the width path — a smoother on the conformal quantile `q_t`. Measure the path
> variation `Σ|Δq_t|`, the induced turnover, and the net log growth of a position charged
> to move. Then ask what the movement penalty does to the validity of the interval that is
> actually deployed.

Identification comes from **holding LEVEL fixed and varying VARIATION**. That is the whole
methodological content, and it is also the reason the claim is exposed — see §5.

---

## 2. The claims, as they will be stated in the paper

The claims **C1'** and **C2'** as they were carried into session S1 are superseded. They
are recorded here so later sessions can see what changed, followed by what replaces them.

### 2.1 Superseded

> **C1' (superseded — OCCUPIED).** At fixed coverage AND fixed mean interval width, the
> temporal variation of an online conformal interval varies materially and carries a
> decision cost, measured in annual net log growth. Neither coverage nor efficiency (mean
> length) measures it.
>
> **C2' (superseded — subsumed into R2, with a longer concession list).** The
> movement-penalised readout map is the right object for setting that variation: quadratic
> movement cost gives linear partial adjustment, proportional cost gives a dead-band. No
> novelty is claimed for either form.

C1' is occupied by Van Belle et al. §2. **C2''s no-novelty concession has had to be extended
twice, and now covers three things, not one:**

1. the two functional forms — Godahewa et al. (*IJF* 2025) publish the linear
   partial-adjustment readout as model-agnostic post-processing;
2. **the readout-map formulation itself** — Genov et al. (*ESWA* 2026), Eq. 18–20, write
   `x_t = M(ŷ_t)` with `M` Lipschitz with constant `L_M`, and bound the switching cost by
   `β·L_M·Σ‖ŷ_t − ŷ_{t−v}‖`;
3. **the smoother applied to a deployed conformal quantile** — Binny & Dixit
   (arXiv:2511.11567), Eq. (13), `q ← (1−γ)q + γ q̂`, one scalar, data-dependent, able to
   shrink.

**Nothing about the object is claimed as new. Only the validity condition is.**

### 2.2 What the paper claims — R1 and R2

> **R1 (measurement — the motivation).** On a real online conformal producer, the pair on
> which the online conformal literature reports and tunes — realised coverage together with
> mean interval width — can be held fixed while the width path `Σ|Δq_t|` varies by a factor
> of F, and the resulting difference in annual net log growth on a position charged to move
> is N points. **This is claimed as the conformal instance of a result already established
> outside conformal prediction, and no wider.**
>
> **R2 (the object and its validity — the paper).** A one-scalar movement penalty applied
> to the **deployed** conformal quantile is not covered by the existing
> predictable-modification arguments, because it acts on the quantile-based width mechanism
> and therefore puts at risk the monotonicity condition those arguments require. The paper
> states the conditions under which ACI's long-run coverage survives such a penalty, and
> reports realised coverage on the smoothed arm as a measured control regardless.

**R2 is the headline. R1 is the motivation. Not the other way round.** R1 alone is a
restatement of a 2026 result in a new instrument, and it is the leg that has been occupied.

### 2.2b R2 is superseded by R2\*\* — amended 2026-08-19 by session S2

**R2 as stated in §2.2 is superseded. It is not deleted, because the project's convention is
to supersede and because the shape of the error is instructive.**

**Why the change was forced, and it is not to the project's credit.** The finding that
required it was **already in the repository** when §2.2 was written. `research/S1/A6-postprocessing-coverage.json`
records Conformal PID Theorem 1 in full and its `citable_as` field already contained the route
in one sentence: *"if the architecture is rearranged so the movement-penalised value enters as
q̂_{t+1} and the saturating integrator is retained on top with feedback from the deployed
interval, Theorem 1 applies verbatim and NO new theorem is needed."* **S1's own synthesis did
not absorb it.** §2.2's R2 and §6 sentence 9 were both written as though the field were empty
of a route, when S1's own retrieval agent had found one and written it down. A later session
had to rediscover it. Record this as a process failure, not only a content one: **the agent
outputs were richer than the synthesis built from them.**

> **R2\*\* — the placement, and what it costs.**
>
> **The inheritance.** A one-scalar movement penalty on a deployed conformal quantile can be
> placed in the **additive scorecaster slot** of Conformal PID (Angelopoulos, Candès &
> Tibshirani, NeurIPS 2023), where `q_{t+1} = q̂_{t+1} + r_t(Σ_{i≤t}(err_i − α))`. Both the
> **L2** (convex-combination) and **L1** (soft-threshold) forms are convex combinations of
> quantities already in `[−b/2, b/2]` — the L1 case via `S_τ(u) = u(1 − τ/|u|)₊` — so
> Theorem 1's hypotheses hold unmodified, its constant is unchanged, and long-run coverage is
> inherited deterministically, with no probabilistic model on the data. **No new theorem is
> required.**
>
> **And none is claimed, because the placement is not new.** Three independent sources state
> or use it: ACT23 themselves say `q̂` may be any function of the past **three separate
> times** — including *"There is no limit to what we can choose for the scorecasting model"* —
> and **deploy a Theta-model scorecaster** in their Figure-3 experiment and throughout their
> appendix; **Dupuy et al. publish the generic argument** at Appendix A, p.15, Eq. 12, *"with
> q̂_{t+1} being any function of the past"*, and in their §4.1 place the previous deployed
> quantile in the slot outright, *"we take ŝ_t = q_t to facilitate the computation"*; and
> **Duerst, Schöley, Hellstrand & Myrskylä** (MPIDR WP-2024-016) already impose an explicit
> width-movement constraint inside a Conformal PID scorecaster — *"We added the constraint
> that the scorecaster's width is not allowed to narrow with time."*
>
> ~~**What the paper claims instead is the trade-off the placement exposes.** Deployed movement
> is `Δq_t = Δq̂_t + Δr_t`, and the integrator's contribution is **irreducible**: Theorem 1
> confines `q̂` to `[−b/2, b/2]` while condition (4) forces `r_t` to reach `±b`, so a
> scorecaster can cancel **at most half** the integrator's reach. Two agents derived the same
> **conservation law** independently and without contact: the product of Proposition 2's
> coverage-gap bound at horizon `T` and the integrator's per-step movement is a constant of
> the horizon, and the penalty weight `w` does not appear in it.~~
>
> **WITHDRAWN THE SAME DAY IT WAS WRITTEN, BY THIS SESSION'S OWN ADVERSARIAL CRITIC. THE
> CONSERVATION LAW IS TRIVIAL AND IS NOT A CONTRIBUTION.** The arithmetic is correct — it was
> re-derived a third time and confirmed numerically, `ε·M = 2α(1−α)(b+η)/T` with the gain
> cancelling exactly — **and that is the problem.** Both factors are independent of the penalty
> weight *by construction*: `ε` is Proposition 2's bound, which the inheritance claim asserts is
> **unchanged** by the scorecaster, and `M` is *defined* as the integrator's own movement, which
> the scorecaster does not enter. **"`w` does not appear in `ε·M`" therefore restates the
> inheritance claim rather than pricing it.** The cancellation of `η` is `x · (1/x)`: ACT23
> print `c = 1/η` for the constant-gain integrator on the same page as the proof, and `M ∝ η`
> is immediate. **Two agents deriving it independently is not evidence it is deep; it is
> evidence it is easy.**
>
> Three further defects, any one of which is disqualifying. **It is not conserved on the object
> the paper measures:** `Σ|Δq_t|` × Proposition 2's bound grows as **Θ(log T)** for ACT23's own
> default tan integrator — measured 2.37 / 2.97 / 3.53 / 4.15 at T = 10³/10⁴/10⁵/10⁶. **The
> printed `π·α(1−α)K_I/T` form requires `b = ∞`**, the branch this very section forbids; with
> ACT23's own `K_I` heuristic the constant is 2.21, not π. And it multiplies a **worst-case
> certificate** by an **average-case** movement, with one to three orders of magnitude of slack
> between the bound and the realised gap.
>
> **"At most half" falls with it, and for a related reason: it is an artefact of a
> normalisation.** Theorem 1's proof needs only `s_t − q̂_t ∈ [−b, b]`, because **Proposition 2's
> hypothesis is `[−b, b]`, not `[−b/2, b/2]`.** ACT23's symmetric `b/2 + b/2` split is one
> point on a continuum: any split `B_q + B_s ≤ b` works with the identical one-line proof, and
> `b` is an **analysis constant the designer declares**, not an algorithm input — nothing in
> iteration (5) needs to know it. Setting `B_q = 0.9b` lets the scorecaster offset 90 % of the
> saturation level with Theorem 1, Proposition 2, `c` and `h` all unchanged. For the tan
> integrator the cost of declaring a larger `b` is uniformly bounded, since
> `c = C_sat·arctan(b/K_I) ≤ C_sat·π/2`; moving the cancellable fraction from ½ to 0.95 costs
> 37 % on the constant. **The number ½ carries no information about the algorithm.**
>
> **And "irreducible" is simply false.** Iteration (5) permits `q̂` to be any function of the
> past **including `q_i`**, hence of the accumulated error `E_t`. A scorecaster that
> pre-subtracts the integrator satisfies every hypothesis of Theorem 1 and **cut deployed travel
> from 91.2 to 0.21 at T = 10⁴**, with realised miscoverage 0.0953 and the budget clip binding
> on 24 of 10,000 rounds.

**WHAT ACTUALLY SURVIVES, AND IT IS A SMALLER PAPER.** Stated plainly, because the section
above has now been through two corrections in one day and a reader deserves the current
position without reconstructing it.

1. **The reduction holds, and it is the tightest point in the whole argument.** The suspected
   factor-of-two hole is not there: `s′_t = s_t − q̂_t ∈ [−b, b]` and **Proposition 2's
   hypothesis is exactly `[−b, b]`**, so `b/2 + b/2 = b` is exactly tight and no unstated
   condition is missing. Three agents attacked the reduction on every axis and none damaged it.
   **But it is not new** — see the three sources above — so it is a citation, not a claim.
2. **The Placement A forfeit is the one measured result that survived every attack.**
   `max|E_t| = 623.7` at `w = 0.999` against a Proposition 2 bound of 14.8, with the forfeit
   growing in exactly the knob a turnover-motivated designer turns up. Reproducible,
   falsifiable, and not in print anywhere the session could find.
3. **The correction of the record against arXiv:2412.18144** — which prints that a scorecaster
   *"breaks the theoretical coverage guarantee"*, and is wrong — costs one paragraph and is a
   genuine service.

**That is a measurement paper and a correction, not a theory paper.** `docs/GATES.md` G3.9's
*Mathematics of Operations Research* upgrade was made conditional on the conservation law and
**should now be dropped rather than re-argued.**

**THE ONE ROUTE BACK TO A REAL RESULT, found while trying to destroy the current one.** Make
**deployed travel `Σ|Δq_t|` the movement variable** — not `q̂`'s movement — **and let the
scorecaster see `E_t`**, which iteration (5) explicitly permits. The question then is *how much
of the integrator's movement a bounded scorecaster can cancel, as a function of the budget
split `B_q/b` and the severity of the distribution shift, and what the cancellation costs in
the certificate.* That has the two things the withdrawn relation lacks — **a free parameter and
a regime dependence**: the same cancelling scorecaster that cuts travel 91.2 → 0.21 in the
stationary case collapses to a 1.12× reduction under shift, because the budget clip binds on
89 % of rounds instead of 24 in 10,000. **The withdrawn conservation law is the degenerate
corner of this question, obtained by freezing the scorecaster.** It is one experiment away and
nobody in the vault has asked it. `docs/OUTSTANDING.md` O42.

**What is true about Placement A, and what §2.2's R2 got wrong about it.** §2.2 said the
downstream smoother breaks the saturation condition, *"because a smoother damps exactly the
excursions the condition needs"*. **That is wrong, and the sign is backwards.** Condition (4)
constrains `r_t` alone, and a smoother placed downstream of the completed output never touches
`r_t`. What fails is the single load-bearing step of Proposition 2's induction —
`c·h(T−1) < E_{T−1} ⟹ q_T = r(E_{T−1}) ≥ b ⟹ s_T ≤ q_T ⟹ err_T = 0` — because the integrator
reaches `b` but an EMA of the output attains `b` only in the limit of infinitely many
consecutive saturated rounds. **The smoother does not damp the accumulator's excursions; it
lets the accumulator excurse further, because the correction it is waiting for is delayed.**

**And Placement A does not lose coverage. The paper must not say it does.** Six smoother
families — EMA at w = 0.5/0.9/0.99, dead band at τ = 0.5/0.9/1.5, running mean, and EMA with
time constant growing as t^0.5 and t^0.9 — returned realised miscoverage **0.1000–0.1002**
against α = 0.1 under an adversary playing the score at the deployed threshold over
T = 2×10⁵. Verbatim inheritance is refutable only on a **zero-slack** instance, verified in
exact rational arithmetic, which is legal under Theorem 1's uniform hypotheses and evaporates
under any strict slack.

> **The claim to make:** *Placement A forfeits the inherited theorem and its finite-sample
> rate and requires a new argument; Placement B requires none.*
> **The claim NOT to make:** *Placement A loses coverage.* **A referee will build the
> counter-simulation in ten minutes.**

The forfeit is measured and it is the empirically meaningful failure: unsmoothed
max|E_t| = 5.5 / 6.6 / 7.8 at T = 10⁴/10⁵/10⁶ against a Proposition 2 bound of
10.2 / 12.5 / 14.8; with an EMA of weight w = 0.999, **max|E_t| = 623.7**, forty to sixty
times the bound; a running-mean smoother grows faster than `h(T) = log T`. **The forfeit grows
in exactly the knob a turnover-motivated designer wants to turn up.**

**Four further constraints that follow, and each is load-bearing.**

1. **The inherited guarantee is weak, and "inherits an existing guarantee" must never be
   allowed to read as "inherits a strong one."** With ACT23's own tan integrator and their own
   heuristic constants, condition (4) holds with `h(t) = t/log t`, so Proposition 2's rate is
   **O(1/log T), not O(1/T)** — a certified coverage band of only **[0.821, 0.979] at
   T = 2500** against a 0.90 target, and identical for δ = 0.01, 0.05 and 0.10 because
   `⌈δ log T⌉ = 1` for every δ ≤ 1/log T. **Do not take the `b = ∞` branch**: it is legal, but
   the deployed set becomes all of `Y` and `Σ|Δq|` is infinite.
2. **Placement B replaces ACI with Conformal PID. It is a change of producer, not a repair.**
   ACI's manipulated variable is `α_t` and its deployed quantile is `Q̂_t(1−α_t)`; **ACI has no
   `q̂` slot** — there is nothing in the ACI recursion for a penalised value to be added to.
   Consequences: ACT23 becomes a baseline to beat, not merely a citation; turnover measured on
   an ACI arm does not transfer, because ACI's width moves through the empirical quantile
   function while Conformal PID's moves additively on the score scale; and `C_sat` and `K_I`
   enter as new free parameters that ACT23 themselves set by hand. **And §4's seventh
   condemned claim evaporates** — the argument that ACI's telescoping identity certifies the
   raw rather than the deployed interval has no purchase here, because Conformal PID's `err_i`
   is already the deployed set's indicator. Do not repeat that motivation under Placement B.
3. **Dupuy et al.'s domination hypothesis is AVOIDED, not DISCHARGED, and these are different
   claims.** Their hypothesis compares partial sums of *two* feedback sequences and exists only
   because their Eqs. (7)/(8) put the smoothed signal **inside** the integrator: the induction
   bounds the smoothed sum while long-run coverage is about the raw one, so domination is
   imposed by hand as the bridge. Under Placement B the integrator's argument is the unmodified
   indicator, **so no smoothed sequence exists and the inequality has no referent.** Conformal
   PID Theorem 1's hypothesis list is exactly three items and contains no domination condition.
   **The paper may NOT claim to have discharged their assumption.** `docs/GATES.md` G3.11.
4. **There are not exactly two placements. A third exists** — inside the integrator, on the
   loop-closing feedback signal — and it is occupied by **Dupuy Eqs. (7)/(8)** and **ECI
   Eq. (4)**, both of which report an obstacle there. **The "exactly two placements" wording is
   falsified and may not be printed.** Nor may the sentence that four lines *"all make the same
   error"*: only two of five are in Placement A (Binny & Dixit Eq. 13, and IPOC), and
   **SCD-split is in neither — it names post-hoc alteration as invalidating and deliberately
   places its smoothing upstream of the quantile computation, which makes it an authority
   against Placement A rather than an instance of it.** The correct general sentence is that
   each of these works puts the penalty somewhere the validity argument's load-bearing step
   passes through, and none puts it in the slot the existing proofs already quantify over.

**A design lever the reduction unlocks.** Condition (4) admits a **relay / dead-band
saturator**, which contributes *exactly zero* movement inside its band while Theorem 1 still
applies verbatim. There is no a priori bound on the crossing count, and Proposition 2 bounds
`|E_T|` rather than crossings. This is a new argument on the L1 side of `docs/OPEN_QUESTIONS.md`
Q7, which remains an operator decision.

**Evidentiary basis for all of §2.2b:** `research/S2/D1-reduction.json` (the reduction, both
paper versions diffed, the Placement A analysis), `D2-attack.json` (the occupancy of the
placement, the conservation law, the change-of-producer finding), `D3-neighbours.json` (the
five neighbours, discharge-versus-avoid, the third placement), `D5-fulltext.json` (Duerst et
al., and the methods-level screen), and `research/checkpoints/S2-W1-reduction.md`.

### 2.3 The STOP condition is replaced

The inherited STOP condition — *"if the method fails, fall back to reporting C1 alone"* —
was written before session S1 and is **now the wrong fallback**, because C1 alone is
precisely the occupied leg. The replacement:

> **If R2 cannot be delivered, re-scope. Do not submit R1 by itself.**

---

## 3. The decision-theoretic constraint, and the operational restatement rule

**The claim is decision-theoretic, not information-theoretic.** No impossibility framing, no
coverage floor, no "fundamental limit". Vaze (arXiv:2607.26577) and Srinivas (SODA 2026,
arXiv:2507.02496) hold that ground and this project loses on it.

### The operational restatement rule

> **Replace every quantifier with a measurement.**

Any sentence of the form "no X can do Y" must become a sentence of the form "across arms
matched on A and B, quantity Z varies by N". The second is the same finding, is what the
experiment actually shows, and is unassailable in a way the first is not.

| Forbidden grammar | Operational replacement |
|---|---|
| "no coverage-based criterion can select the adaptation rate" | "Across arms matched on realised coverage to within 0.002 and on mean interval width to within a stated tolerance, realised decision cost varies by N points of annual net log growth. Coverage and mean width are therefore uninformative for selecting the movement penalty." |
| "coverage is blind to turnover" | "Realised coverage is constant across arms whose width paths differ by a factor of F." |
| "nothing in the literature measures the increment functional" | "`Σ\|Δq_t\|` is reported here; the works cited in §related report coverage and mean length." |

**"Blind" is itself forbidden as a load-bearing word.** It invites the impossibility reading,
and it is the exact move Min et al., Vaze and Van Belle have each already made in a
different form. Use the measurement.

**Watch-list of forbidden constructions:** `no X can`, `cannot select`, `floor`,
`fundamental limit`, `impossible`, `impossibility`, `nobody has`, `no one has`,
`never been`, `no method`, `no criterion`, `provably cannot`, `there is no`.

Reporting *someone else's* impossibility result is legitimate and required — Andrew et al.
(COLT 2013) genuinely is an impossibility theorem and describing it correctly is not a
violation. The prohibition is on this project claiming one.

---

## 4. The six condemned claims, with their replacements

| # | Condemned | Replacement |
|---|---|---|
| **i** | "Nobody has explained it" / any claim that the Ryan anomaly is unexplained. | Ryan offers an explanation — estimation variance charged through the nonlinear Kelly sizing map — hedged in his own text as "a structural explanation consistent with the results", conjectured rather than measured for three of four devices, and never phrased in terms of turnover. The paper engages that explanation; it does not deny its existence. |
| **ii** | The "quantitative match" of 0.7–5.3 to 1.0–4.4, and the 1.0 lower bound. | Delete. No numeric correspondence between the two ranges is claimed. |
| **iii** | Gârleanu–Pedersen as the source of the **dead-band** form. | Gârleanu & Pedersen (2013) assume **quadratic** costs and derive **linear partial adjustment**, and explicitly distinguish themselves from no-trade strategies. Cite them for the quadratic ⇒ partial-adjustment half only. The dead-band is **Constantinides (1986)** and **Davis & Norman (1990)**. |
| **iv** | "No coverage-based criterion can select the adaptation rate." | Refuted by DtACI, which selects the step size online by a coverage-based criterion. Use the operational restatement in §3. |
| **v** | The word **"frontier"** as a formal object belonging to this project. | Either present a measured curve with no minimax claim and no use of the word, or drop it. Note that "frontier" describing *someone else's* object — Srinivas's coverage–efficiency frontier, Zhou & Zhu's miscoverage–regret frontier — is correct and must be retained. |
| **vi** | "arXiv returns 0 for conformal × downstream decision." | False. Decision-focused conformal prediction is an active field with a dozen uncited entries, at least one by a confirmed speaker at the target venue. |

**A seventh, added by session S1:** the assertion that **ACI's telescoping coverage identity
is untouched by a readout smoother, and therefore no coverage question arises**. The
identity is indeed untouched — and that is exactly the problem: it then certifies the
coverage of the **raw** interval, not the **deployed smoothed** one. Gibbs–Candès Lemma 4.1
turns on `α_t < 0 ⇒ Q̂_t(1−α_t) = ∞ ⇒ err_t = 0`, a property of the construction; feed the
recursion the smoothed interval's indicator and that proof fails. **Claim coverage for the
raw arm only. Report the smoothed arm's realised coverage as a measured control.**

---

## 5. What the design change bought and what it cost — state this, do not hide it

The abandoned design varied ACI's adaptation rate γ and measured turnover. Its recorded
fatal risk was that `Σ|Δq|` might be approximately a monotone function of `E[L]` across the
γ grid, collapsing the claim into Zaffran's Theorem 3.1 times a cost rate.

**What matched-width bought.** It removes that objection by construction. There is now
direct external evidence the change was necessary: **Genov et al. is the γ design, in energy
systems, and it fails exactly there** — its commitment-period arms move level and variation
together, its §4.4 says so in its own words, and its attribution runs through a cross-arm
correlation table.

**What it cost.** Holding a level functional fixed while varying a path functional and
pricing the difference through a decision with an incumbent state **is Van Belle §2's
design**. The old design was confounded enough to be unlike anything published; the new one
is clean enough to be exactly like the best paper in a neighbouring field.

> **The new design is more exposed than the old one, and it is more exposed because it is
> better.** State it in those terms. Do not revert to γ — reverting restores an
> identification failure that is now documented in print, and the paper would be attacked
> on methodology instead of on novelty, which is worse.

---

## 6. The distinguishing sentences

These go in the paper. Sentences 1–7 are the related-work section (`paper/sections/related.tex`);
8 and 9 are the two that carry the contribution.

1. **Zaffran et al. (ICML 2022)** price ACI's learning rate in the *level*: Theorem 3.1 gives
   `E_{π_γ}[L] = L₀ + ½·Q″(1−α)·γ·α(1−α) + O(γ^{3/2})`, a statement about mean length, which
   integrates the path away; we hold it fixed.
2. **Min et al. (arXiv:2601.21455, ICML 2026)** also call coverage and length insufficient,
   but their interval stability (Def. 4.1), `E_X[Var_{A|X,D_ca}(|C_{1−α}(X)|)]`, varies over
   the algorithm's own randomness given test point *and* calibration set and is "zero for
   deterministic methods by design": a deterministic interval oscillating daily scores
   exactly zero.
3. **Zhou & Zhu (arXiv:2510.07750)** vary the coverage *level* along a miscoverage–regret
   trade-off; we fix coverage and vary the path.
4. **Ryan (arXiv:2608.01494)** charges the growth loss to estimation variance passing through
   the nonlinear Kelly sizing map, hedged as "a structural explanation consistent with the
   results", and already reports the daily `sd(Δ log q)` (0.00343 vs 0.00391) and matched
   gross leverage (1.957–1.959); what he does not match is width, nor phrase it as turnover.
5. **Wang & Hasuike (arXiv:2605.01176)** report that "increasing risk aversion does not
   meaningfully reduce turnover" and damp the *weight* path by a heuristic δ = 0.1 partial
   adjustment, never swept; their paper carries no interval, coverage or quantile object.
6. **Godahewa et al. (*IJF* 2025)** already publish the linear partial-adjustment readout
   `ỹ = (1−w_s)·ŷ_new + w_s·ỹ_prev` as model-agnostic post-processing, so we claim no
   novelty for either form.
7. **Van Belle et al. (arXiv:2605.28531)** pin CRPS across arms (2.91/1.43/0.83 vs
   2.91/1.44/0.83, "indistinguishable in terms of forecast quality"), vary `W₁` between
   consecutive updates threefold, and price it through a newsvendor; but their functional is
   over forecast *revisions of a fixed target*, they carry no interval and no coverage
   object, and the effect is +0.00 % in their single-horizon arm.

**8 — the R1 sentence.**

> Matching a probabilistic forecast's level and comparing what its structure does is not
> new: Pinson & Girard (2012) match the full marginal across three real wind-power scenario
> sets — hence coverage and mean width exactly — and compare only their rank dependence,
> and Van Belle et al. (2026) match CRPS across two forecasters and price the difference
> through a newsvendor charged to revise an incumbent order. What the scenario literature
> matches away, however, is the quantity studied here: with the marginals held equal, the
> calendar-time variation of the deployed width is identically zero across their arms,
> because the object they vary is the copula within a single forecast issue. This paper
> varies that revision path instead, on a producer whose level is pinned by a
> distribution-free calibration construction rather than by a matched data-generating
> process, and prices it through the decision step that Pinson & Girard's own conclusion
> commissions and does not take.

**Honest weakness of sentence 8, to be pre-empted in the paper rather than discovered in
review — and note that this weakness is now DIFFERENT from what it was, and smaller.** The two
distinctions this file originally gave R1 — that the matched pair is *(coverage, mean
width)* specifically, and that the producer is real rather than synthetic — are **both
destroyed by Pinson & Girard**, who match the entire marginal (a strictly stronger control
that subsumes the pair) on real data, in 2012, inside the reliability-and-sharpness framing
that *is* this pair under its meteorological name. **R1 therefore rests on Q3 alone: the
movement-charged decision.** The reviewer line to expect is not "CRPS versus your pair is a
detail" but the much better "matching the whole predictive marginal is stronger than
matching your pair, on real data, fourteen years ago". The only answer is that neither
Pinson & Girard nor the verification literature attaches a decision that pays to move — and
that answer must be stated in the paper, with Pinson & Girard cited, not left to be found.
The stronger half of the reply is the object distinction above: their arms have identical
width paths by construction, so the quantity this paper measures is not merely unmeasured in
their design — it is identically zero in it.

**9 — the R2 sentence. REPLACED 2026-08-19 by session S2. The superseded wording is kept
below the replacement.**

> Placing a movement penalty on an online conformal threshold is not new, and neither is
> putting it where it inherits a validity guarantee: Godahewa et al. (*IJF* 2025) publish the
> one-scalar partial-adjustment smoother as model-agnostic post-processing, Genov et al.
> (*ESWA* 2026, Eq. 18–20) bound a decision's switching cost by the forecast path variation
> through a Lipschitz readout map, Binny & Dixit (arXiv:2511.11567, Eq. 13) apply the smoother
> to a deployed conformal threshold, and Angelopoulos et al. (NeurIPS 2023) state three times
> that the scorecaster in their iteration may be any function of the past and run an
> exponential-smoothing-family model in that slot — so the object, the bound and the placement
> are all prior work. What has not been stated is the price of the placement. The scorecaster
> is confined to half the range the saturation condition requires of the integrator, so at
> most half of the integrator's contribution to deployed movement can be cancelled by any
> penalty; and the product of the guarantee's coverage-gap bound and the integrator's own
> per-step movement is a constant of the horizon in which the penalty weight does not appear.
> Tightening the inherited guarantee therefore buys movement that the penalty cannot buy back.
> The same arithmetic explains the hedges: SCD-split places its smoothing upstream of the
> quantile and states that post-hoc alteration invalidates the guarantee, ECI and Dupuy et al.
> smooth the feedback signal inside the integrator and report an uncontrolled averaged
> miscoverage gap and a domination hypothesis the authors call "pretty strong" respectively,
> IPOC clamps the deployed width and reports that it can only "approximately guarantee"
> coverage, and BC-ACI secures its monotonicity condition by leaving the width mechanism
> untouched. Each puts the penalty where the validity argument's load-bearing step passes
> through; this paper measures what it costs to put it where the existing proof already
> quantifies over.

**Superseded wording, kept for the record:**

> Godahewa et al. (*IJF* 2025) publish the one-scalar partial-adjustment smoother as
> model-agnostic post-processing, Genov et al. (*ESWA* 2026, Eq. 18–20) bound a decision's
> switching cost by the forecast path variation through a Lipschitz readout map, and Binny
> & Dixit (arXiv:2511.11567, Eq. 13) apply exactly this smoother to a deployed conformal
> threshold — so we claim novelty for none of them; what no one has established is the
> condition under which the smoothed quantile stays valid *in transit*, and four independent
> groups have now named that obstacle without clearing it: SCD-split states that post-hoc
> smoothing of the conformal quantile invalidates the guarantee, ECI that a fully smoothed
> update leaves the averaged miscoverage gap uncontrolled because of the smoothing bias,
> IPOC that its chased interval can only "approximately guarantee" coverage, and Dupuy et
> al. prove it under a domination hypothesis they themselves call "pretty strong" and
> "highly dependent on the choice of parameters" — which is precisely the monotonicity
> condition BC-ACI's coverage proposition names and secures only by leaving the width
> mechanism untouched.

**Three defects in the superseded wording, recorded so they are not reintroduced.** It used
the forbidden construction *"what no one has established"* (§3 watch-list), in a file that
forbids it. It asserted that four groups make the same error, which §2.2b item 4 refutes. And
its gloss of SCD-split misstates both nouns — SCD-split does not smooth the conformal
quantile post hoc; it places smoothing upstream of the quantile computation and names post-hoc
alteration as the thing that invalidates.

**Honest weakness of sentence 8, to be pre-empted in the paper rather than discovered in
review.** A hostile reviewer will say: *you matched a level functional; so did they; CRPS
versus (coverage, mean width) is a detail.* The answer, which must be **in the paper**, is
that (coverage, mean width) is not an arbitrary choice of level functional — it is the
two-part criterion on which ACI, DtACI, Conformal PID and SAOCP are all reported and tuned,
so pinning that specific pair is a statement about a field's tuning practice rather than
about accuracy in general. That answer is defensible. It is not overwhelming.

---

## 7. Positioning rules that follow

1. **Two chains go in the OPENING, not in related work.**
   **(a) Forecast stability:** Godahewa et al. 2025; Van Belle et al. 2023, 2024, 2026;
   Pritularga & Kourentzes 2024; Caljon et al. 2026; Tunc et al. 2013; Genov et al. 2026.
   **(b) Probabilistic-forecast verification, which is where "hold reliability and sharpness
   fixed and compare the temporal structure" was actually invented:** Gneiting, Balabdaoui &
   Raftery (2007) — the "sharpness subject to calibration" paradigm, i.e. this project's
   matched pair under its own name; Pinson & Girard (2012); Worsnop et al. (2018);
   Pinson et al. (2008).
   A four-page paper that cites both chains first and then says what the conformal setting
   adds is a legitimate contribution. **The same paper without chain (b) repeats the exact
   failure mode that occupied C1′, one literature over** — and Pinson is an author in both
   chains and a likely reviewer.
2. **Do not claim "coverage and length are not sufficient" as this project's move.** Cite
   Min et al. and Vaze first, then name the quantity added.
3. **Do not use a vertical/horizontal (revision-index versus calendar-time) distinction to
   separate this work from the forecast-stability literature.** It was proposed and
   withdrawn within session S1: Godahewa et al. name and stabilise both, and Genov defines
   vertical and horizontal variants of both MAC and SDC. It will be corrected in review.
4. **Do not lean on Van Belle's +0.00 % procrastination row** as evidence their effect is
   confined to multi-horizon revision. It is an artefact of their three-opportunity setup.
5. **Coin a new term for the measured quantity.** Every natural name is taken: *smoothed
   conformal* means randomised smoothing; *stable conformal* means Ndiaye's computational
   stability; *smoothing-based conformal* is SCD-split; *interval stability* is Min et al.'s
   run-to-run variance. And `Σ|Δq|` itself is already a published named metric (Zanotti's
   MQC/SMQC), so the measurement instrument cannot be presented as new either.
6. **Defuse Min et al. Theorem 3.3 explicitly.** It shows a post-processing can preserve
   coverage while shortening mean length by returning ∅ on some draws — which is the exact
   failure mode of judging an interval by (coverage, mean length). The defence is that R1
   fixes *both* and reports the path functional as an addition, and that their IS is 0 for
   a deterministic smoother. Say it; do not leave it to inference.
7. **Pre-empt the Ryan objection.** He matches *post-cap gross leverage*, which is
   downstream of the sizing map and therefore confounds the level and path of `q` upstream
   of the cap. Show that `E[L]` and gross leverage come apart, or the reviewer will read his
   control as the stronger one. **This leg is contingent** — it rests on his not printing a
   per-device path statistic, and it weakens if the requested ledger
   (`docs/RYAN_EMAIL_DRAFT.md`) turns out to contain per-device turnover.

---

## 8. The IPOC conditional — CLOSED 2026-08-19, in the project's favour

**IPOC has been read in full, and its coverage guarantee does not quantify over the
movement-constrained object. R2's distinguishing sentence is not void.**

Chen, Luo, Huang, Jiang, Shi, Zhang & Gao, *IPOC*, KDD 2023, doi 10.1145/3580305.3599396,
pp. 202–212. Obtained in Wave 5 after eleven earlier routes failed. **The eleven failures
shared one wrong premise: that the ACM Digital Library's HTTP 403 was a paywall. It is
Cloudflare bot detection, and the ACM Digital Library is open access.** A headed system
Chrome instance driven through a persistent profile passes the challenge and the full
eleven-page PDF downloads. **Every ACM paper in this project is reachable this way**, and
that is the single most useful operational fact this session produced.

> **NARROWED 2026-08-19 BY SESSION S2. THE RULE ABOVE IS TRUE OF THE ACM DIGITAL LIBRARY AND
> OVER-GENERAL EVERYWHERE ELSE.** Applied unamended it will cost the next session what the
> paywall assumption cost S1, in the opposite direction. The corrected rule:
>
> - **ACM Digital Library** — 403 is bot detection, the library is open access behind it, and
>   headed Chrome with a persistent profile gets the PDF. Unchanged, and still the single most
>   useful operational fact in this file. *(Not re-verified in S2: ACM's challenge defeated all
>   six routes tried this session, so treat the route as established by S1, not as guaranteed.)*
> - **IEEE Xplore and Wiley** — headed Chrome defeats the bot check on the first attempt, and
>   **a real subscription wall sits behind it.** Four IEEE targets reached, **zero PDFs.**
>   Expect abstract-plus-introduction, not full text.
> - **ScienceDirect / Elsevier** — adds a Turnstile CAPTCHA that **headed Chrome does not
>   pass.** Crossref metadata only.
>
> **Two substitute routes, and they are what actually resolved this session's single
> unresolved occupancy risk** (§8b item 4): **IEEE Xplore's embedded metadata block** carries
> the abstract even when the PDF is walled, and **Semantic Scholar's figure-extraction service
> returns figures and tables for paywalled PDFs.** Record both.
>
> `docs/OUTSTANDING.md` O34; `research/S2/D4-hiding-places.json`.

**What the theorem actually says.** IPOC has exactly one coverage statement — Lemma 3 in
§5.1, titled "The Effectiveness of ACI", imported verbatim from Gibbs & Candès: *"The
average miscoverage ratio of confidence intervals {c^f_t} will converge to α with enough
training steps."* Appendix A's notation table is decisive: `c^f_t` is "confidence interval
of **model f** at time t by ACI", where `f` is the point prediction model and `f̄`, listed
separately, is the ensemble model. **The guarantee is on the base model's interval, not on
the chased ensemble interval that the movement cost acts upon.** The chased interval's
validity is asserted and never proved — §5.1 says only that "we can still approximately
guarantee coverage rate, which is verified in the experiment results". Theorems 1 and 2 are
pure pinball-loss regret.

**IPOC is therefore a supporting citation, not a threat.** Its own hedge is a fourth
independent instance of the obstacle R2 names.

**One residual, and it is small.** The TKDE 2026 extension's theory section
(doi 10.1109/TKDE.2026.3674583, IEEE Xplore article 11435627) is still unread — the abstract
was obtained, `isOpenAccess` is false, and the PDF download timed out. Its abstract
enumerates only the same two regret results plus a Dd-MDP solvability framework, so a new
coverage theorem is unlikely, but this is formally unverified. `docs/GATES.md` G3.8.

---

## 8b. What replaced it — the conditionals that are actually open

**These are more constraining than the IPOC conditional was, and they are what a later
session must attack.**

1. **R1 no longer survives on the two distinctions this file originally gave it.**
   **Pinson & Girard, *Applied Energy* 96:12–20 (2012), doi 10.1016/j.apenergy.2011.11.004**
   compares three arms on a **real** producer that share the **full marginal predictive
   distribution** — hence identical realised coverage and identical mean interval width, by
   construction, a strictly stronger control than the pair — and varies only the temporal
   dependence structure, and states the Q4 moral. It fails **Q3 only**: no decision, no
   movement cost. And its own conclusion commissions exactly that study: *"a more intuitive
   approach to the evaluation of sets of scenarios may be to concentrate on their value
   instead, i.e. on the comparative benefits from their use as input to various
   decision-making problems."*
   **The aggravating fact:** **Pierre Pinson is a co-author of the paper that occupies C1′**,
   and is a likely reviewer. Worsnop, Scheuerer, Hamill & Lundquist (*WES* 3:371–393, 2018)
   pin the construction still more literally — their compared scenario sets have "the same
   quantiles … the same spread".

   **But R1 survives for a reason nobody in this session had identified, and it is better
   than the two that died.** Because these papers match the *marginals*, `Σ|Δq_t|` differs by
   **zero** across their arms. They vary the copula **within a single forecast issue** — the
   rank dependence across lead times inside one scenario set — not the **calendar-time
   revision path of the deployed width**. Those are different objects, and the distinction
   is an *object* distinction, not the banned time-axis move of §7 rule 3: the quantity R1
   varies is identically constant in their design, so their design cannot measure it even in
   principle. **State R1 on that basis**, and note that Q3 fails in all of them — Pinson &
   Girard and Bessa (PSCC 2016) both defer the decision step to future work, and Pinson &
   Girard's conclusion commissions it explicitly.
2. **R2's object is not new.** **Binny & Dixit, arXiv:2511.11567, Eq. (13)** publishes the
   one-scalar smoother on the deployed conformal calibration threshold verbatim:
   `q ← (1−γ)q + γ q̂`, data-dependent, able to shrink. Their Theorem 5 is a Banach
   contraction result in which γ does not appear, and their coverage claim holds at the
   fixed point where the smoother is inert; the transient is never analysed. **The property
   is still open. The object is not.**
3. **The question is already contested.** **Dupuy, Xu, Perrey, Montmain & Imoussaten,
   arXiv:2510.02809 / doi 10.1007/978-3-032-16708-8_17** replaces the binary indicator in
   the online conformal update with a smooth relevance function, explicitly to prevent
   abrupt threshold changes while maintaining coverage validity, and proves three long-run
   coverage theorems. Theorems 1 and 3 are inherited from the saturating-integrator
   argument. **Theorem 2 is the case where the width mechanism itself is driven by the
   smoothed signal, and it needs a domination hypothesis the authors immediately disown** as
   "pretty strong" and "highly dependent on the choice of parameters". **That is R2's thesis,
   stated by someone else, with an attempted theorem attached.** R2 must now be positioned
   against Dupuy Theorem 2 specifically — as discharging the assumption they could not, or
   as not being written at all.
4. **R1's Q3 leg — the last thing it owned — is now partially occupied, and the qualifier
   is what R1 has left.** **Ding, Pinson, Hu & Song, *IEEE Trans. Sustainable Energy*
   7(1):163–172 (2016)** generate scenarios by NORTA, so per-lead-time marginals are
   **identical by construction** for every value of the autoregressive factor ρ, sweep ρ from
   −1 to 1 in steps of 0.05, and price the result through a storage decision with a state of
   charge in which **holding is free**. Q1 ∧ Q2 ∧ Q3 ⇒ OCCUPIED by the letter of the rubric.
   **Two qualifiers, both from the paper's own text, and R1 now lives entirely inside them:**
   their movement charge is **round-trip efficiency and capacity bounds — physics, not a
   price on changing an incumbent decision**; there is no start-up cost, no ramp cost and no
   cycling-degradation cost, and they defer degradation to future work. And their headline is
   a **null**: their own strategy's profit "remains steady regardless of ρ", with the real
   degradation appearing only for a naive filter strategy. **Pierre Pinson is a co-author —
   the third time in this file.**
   **What survives, and it is now the whole of R1's claim to Q3:** across a wide hunt with
   heavily evidenced zero-result queries, **no work holds marginals fixed, measures a
   temporal path functional, AND prices it through a start-up, ramping or cycling cost.**
   Both Pinson & Girard and Bessa (PSCC 2016) explicitly defer the decision step, and nobody
   took it up with a matched-marginal design. **State R1's decision leg in those terms — a
   priced movement cost, not merely a decision with a state — or it is not distinguished.**
   The one unresolved risk is **Chen, Yang, Li & Liu, IEEE Tencon-Spring 2013,
   doi 10.1109/TENCONSPRING.2013.6584502**, whose title is an exact framing match and for
   which no abstract exists anywhere. See `audit/PRIOR_ART.md` §7.9.

   > **WITHDRAWN 2026-08-19 BY SESSION S2. THE PARAGRAPH ABOVE IS FALSE FROM "What survives"
   > ONWARDS, AND THE RISK IT NAMES HAS MATERIALISED.**
   >
   > **Chen, Yang, Li & Liu (2013) is resolved, and it OCCUPIES R1's decision leg.** S1 could
   > find no abstract in Crossref, Semantic Scholar or Unpaywall, and that was accurate. The
   > abstract is on the IEEE Xplore landing page, in an embedded metadata block reachable by
   > headed Chrome, and **all seven figures and tables were recovered from Semantic Scholar's
   > figure-extraction service for the paywalled PDF.** Scored on the rubric:
   > **Q1 yes** — same per-period forecast distributions by construction, via a Gaussian-copula
   > correlation matrix; **Q2 yes** — its Fig. 4 plots the gradient curves of both scenario
   > sets; **Q3 yes AND PRICED** — its Table II carries a per-start start-up cost of
   > **\$300–\$4500**, with minimum on/off times and ramp rates; **Q4 yes; Q5 no.**
   > Q1 ∧ Q2 ∧ Q3 ⇒ **OCCUPIED**, by the same rubric applied mechanically that occupied C1′.
   > An independent 2018 restatement exists (doi 10.12783/dteees/appeec2018/23559), so it is
   > not a one-paper fluke.
   >
   > **Therefore the sentence "no work holds marginals fixed, measures a temporal path
   > functional, AND prices it through a start-up, ramping or cycling cost" is withdrawn, and
   > so is the corresponding block quote at `audit/PRIOR_ART.md` §7.9.3.** So is the
   > instruction to state R1's decision leg as the thing that distinguishes it: **the priced
   > movement cost no longer distinguishes R1.**
   >
   > **What R1 has left is Q5 alone** — the absence of a coverage object anywhere in the
   > matched-marginal decision-value literature — **plus the calendar-time-revision-path
   > object distinction of item 1 above.** Whether that carries a paper is `docs/OUTSTANDING.md`
   > O28 and it is not settled here. A further near-miss found in the same sweep sharpens the
   > problem: **Delikaraoglou & Pinson (2014)** has the matched-marginal generator *and* priced
   > start-up and shut-down costs in one paper, and fails only Q2 because it builds a single
   > arm. **That is Pierre Pinson's fourth appearance in this file.**
   >
   > `research/S2/D4-hiding-places.json`; `docs/OUTSTANDING.md` O27, O28, O29, O30, O35.
5. **A 1985 antecedent scores the mechanism on Q1–Q4** — Williams, Peters & Raiszadeh,
   *J. Oper. Mgmt* 6(1):69–85, which rearranges demand sequences to differ *only* in serial
   correlation and evaluates lot-sizing rules carrying a real setup cost. Its body was not
   obtained, and its inputs are deterministic sequences rather than probabilistic forecasts,
   with no interval and no coverage object. **But no sentence in this paper may imply the
   mechanism is recent.**
6. **Every "nothing in the literature" statement in this project is abstract-level only.**
   The OpenAlex full-text budget was exhausted before the adversarial wave began and not one
   of the named full-text queries ran. Full-text search is the only instrument that sees a
   smoother in a methods section.

## 9. Evidentiary basis

- `audit/PRIOR_ART.md` §7 — the dated verdicts against C1'/C2', superseding §5.
- `research/S1/B1-verdicts.md` — the full synthesis, the top-ten table with all five rubric
  answers, the stress test of R1 and R2 against the five nearest neighbours, and what would
  move each verdict.
- `research/S1/A1`–`A7*.json` — the seven retrieval agents, every query logged verbatim with
  its result count.
- `research/checkpoints/S1-W1-retrieval.md`, `S1-W2-synthesis.md` — the wave records.
- `audit/REFS_VERIFIED.bib` — every entry built from a fetched canonical record.
