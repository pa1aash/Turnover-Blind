# Experimental protocol

**Written 2026-08-19, session S2 wave 2. Status: `draft — awaiting operator freeze`.**

This document is the frozen experimental specification the project has been missing.
`audit/RECONSTRUCTION_SPEC.md` is the register of every choice the planning document left
open; this document resolves that register with a value and a justification for each item,
and adds the items the corrected claim introduces. It is written **before any simulator
exists and before any number is produced**, which is the only condition under which it has
evidential value (`audit/RECONSTRUCTION_SPEC.md` §1, the warning that governs that file).

**This session ran no experiment and wrote no code.** Nothing here is a result.

**No gate is signed by this document.** `docs/GATES.md` G2, G3 and G4 remain `not started`.
This protocol supplies the artefact G2.12 asks for and the configuration G2.1 asks for; the
operator alone may record a gate as signed.

**Scope.** This protocol governs the synthetic experiment behind G2 and G3. The applied
Ryan-configuration replication is governed by G4 and is out of scope except where a choice
here binds it, which is flagged in place. §9 lists what this document does not settle.

**Precedence.** `docs/FRAMING.md` wins over this file wherever they disagree, including its
§3 watch-list of forbidden constructions and its operational restatement rule (*replace every
quantifier with a measurement*). Where a wave-1 finding is naturally described with a word on
that list, this document uses the measurement instead: the recurring object below is called
the **integrator's own movement** or the **irreducible component of deployed movement**, and
it is always accompanied by the quantity that measures it.

---

## 1. What is being measured and why

### 1.1 The claim this protocol tests

Session S2 wave 1 verified the central assertion of the claim carried into the session and
refuted three of its four supporting assertions. What follows is the corrected claim, and it
is what the experiment below is designed against. Nothing in this protocol is designed
against any earlier wording.

> **The placement.** A one-scalar movement penalty on a deployed conformal quantile can be
> placed in the **additive scorecaster slot** of Conformal PID, where
> `q_{t+1} = q̂_{t+1} + r_t(Σ_{i≤t}(err_i − α))`. Both the **L2** (convex-combination) and
> **L1** (soft-threshold) forms are convex combinations of quantities already in
> `[−b/2, b/2]` — the L1 case because `S_τ(u) = u·(1 − τ/|u|)₊` — so Theorem 1's hypotheses
> hold unmodified, its constant is unchanged, and long-run coverage is inherited
> deterministically with no probabilistic model on the data.
>
> **No new theorem is required, and none is claimed, because the placement is not new.**
> Angelopoulos, Candès & Tibshirani (NeurIPS 2023; arXiv:2307.16895) state three times that
> `q̂` may be any function of the past and deploy a Theta-model scorecaster; Dupuy, Xu,
> Perrey, Montmain & Imoussaten (arXiv:2510.02809v2, Appendix A p.15, Eq. 12;
> doi 10.1007/978-3-032-16708-8_17) publish the generic argument; and Duerst, Schöley,
> Hellstrand & Myrskylä (MPIDR WP-2024-016, doi 10.4054/mpidr-wp-2024-016, §2.5 lines
> 215–224) already impose an explicit width-movement constraint inside a Conformal PID
> scorecaster.
>
> **What the paper contributes is the trade-off the placement exposes.** Deployed movement is
> `Δq_t = Δq̂_t + Δr_t`. The integrator's contribution is irreducible: Theorem 1 confines `q̂`
> to `[−b/2, b/2]` while condition (4) requires `r_t` to reach `±b`, so the largest fraction
> of the integrator's reach a scorecaster can offset is one half. Two independent wave-1
> derivations give the same exchange: *(Proposition 2's coverage-gap bound at horizon T) ×
> (the integrator's per-step movement) is a constant of the horizon, and the penalty weight
> `w` does not appear in it.* For a constant-gain integrator the product is `2α(1−α)b/T`
> exactly, with the gain cancelling; for the tan integrator it is `π·α(1−α)·K_I/T`.
> Tightening the inherited guarantee buys movement, and the measured exchange is unchanged by
> `w`.
>
> **Placement A** — smoothing the completed output of a quantile tracker — **forfeits the
> inherited theorem and its finite-sample rate.** The mechanism is not damping of condition
> (4): condition (4) constrains `r_t` alone and a downstream smoother never touches `r_t`.
> What fails is the load-bearing step of Proposition 2's induction,
> `c·h(T−1) < E_{T−1} ⟹ q_T = r(E_{T−1}) ≥ b ⟹ s_T ≤ q_T ⟹ err_T = 0`, because the
> integrator reaches `b` but an exponential moving average of the output attains `b` only in
> the limit of infinitely many consecutive saturated rounds. **The smoother does not damp the
> accumulator's excursions; it lets the accumulator excurse further, because the correction
> it waits for is delayed.** Long-run coverage is not lost — six smoother families returned
> miscoverage 0.1000–0.1002 against α = 0.10 under adversarial scores over T = 2×10⁵. The
> measured forfeit is in the finite-sample rate: unsmoothed `max_t|E_t|` = 5.5 / 6.6 / 7.8 at
> T = 10⁴ / 10⁵ / 10⁶ against a bound of 10.2 / 12.5 / 14.8; with an EMA of `w = 0.999`,
> `max_t|E_t| = 623.7`, 40–60× the bound; a running-mean smoother grows faster than
> `h(T) = log T`. **The forfeit grows in exactly the knob a turnover-motivated designer turns
> up.**

Locators for every quantity in that block: `research/S2/D1-reduction.json`, blocks
`c_saturation_condition`, `d_deployed_interval`, `e_paper_statements`; and
`research/S2/D2-attack.json`, blocks `numeric_bound_table` and `integrator_movement_…` (the
block keyed on the integrator's own movement — the key's own name uses a word
`docs/FRAMING.md` §3 forbids in this project's prose, so it is cited here by prefix). Those
are working files. The underlying sources are Angelopoulos, Candès & Tibshirani, *Conformal
PID Control for Time Series Prediction*, NeurIPS 2023 / arXiv:2307.16895 — Theorem 1 and
condition (4) at p.3, Proposition 2 at p.6 with its proof at Appendix A p.14, the tan
integrator at p.3, the `C_sat` and `K_I` heuristics in Appendix B — together with the
wave-1 numerical work recorded in those two files.

### 1.2 A third placement exists, and the protocol carries it

Wave 1 also refuted the claim that there are exactly two placements
(`research/S2/D3-neighbours.json`, `dupuy.is_there_a_third_placement`). There is a third,
architecturally distinct from both: the penalised or smoothed quantity is substituted for the
loop-closing feedback **inside** the integrator's argument, `r_t(Σ_i(g_i − α))` with
`g ≠ err`. Two published works occupy it and both report an obstacle there — Dupuy et al.
Eqs. (7)/(8) with the domination hypothesis their authors disown twice (arXiv:2510.02809v2,
p.8), and ECI's fully smoothed update (Wu, Hu, Bao, Xia & Zou, arXiv:2502.00818v2, Eq. (4),
p.5: *"we cannot directly control the averaged miscoverage gap … due to the smoothing
bias"*). **Placement C is therefore a specified arm here** (§2, arm `C1`). Running it costs
almost nothing and it converts an assertion about architecture into a measurement across
three positions rather than two.

### 1.3 The central experiment, stated operationally

> Across arms matched on realised coverage to within 0.002 and on mean deployed width to
> within 0.5 % relative, measure: the deployed width path variation `Σ|Δq_t|` and its two
> decompositions, the induced position turnover, the realised net annual log growth of a
> position charged to move, and the integrator's own contribution to movement. Report the
> measured product (Proposition 2 bound at T) × (integrator per-step movement) against its
> predicted value.

Four things follow from that sentence and they are the design:

1. **Placement A and Placement B are arms of one experiment, not alternatives.** The claim is
   about the difference between them, so they are run on the **same producer**, over the
   **same common random numbers**, at the **same matched coverage and width**.
2. **Turnover is decomposed twice** (§5.2), because an undecomposed turnover column cannot
   attribute anything (`docs/GATES.md` G2.13) and because a reviewer who knows the exchange
   in §1.1 will ask which part of `Σ|Δq|` the penalty actually reduced
   (`research/S2/D2-attack.json`, `integrator_movement_….implication_for_R2star`, consequence
   2).
3. **The match is verified and committed before any growth or turnover column exists**, by a
   two-stage execution mechanism, not by an intention (§3.3).
4. **The exchange in §1.1 is printed as a falsifiable check**, not as prose (§5.5).

### 1.4 What the experiment is not for

It is not for establishing that transaction costs cost money. `audit/NUMBERS.md` §9.1 shows
the inherited growth column is the cost identity `Δgrowth ≈ c × Δturnover` to within about
5 % of the effect, and a reviewer will perform that subtraction in thirty seconds. The
column that is not an identity is the **turnover column at matched coverage and matched
width**, and this protocol leads with it: the primary endpoint is turnover, growth is the
monetisation, and the power calculation in §6.3 is anchored on turnover first.

---

## 2. The arms

### 2.1 Two producers, and why there are two

`research/S2/D2-attack.json`, `is_placement_B_a_change_of_subject`, records the finding that
governs this section: **ACI's manipulated variable is `α_t` and its deployed quantile is
`Q̂_t(1−α_t)`; ACI has no `q̂` slot, so a penalised value has nowhere in the ACI recursion to
be added.** Conformal PID manipulates `q_t` additively on the score scale.
Placement B is therefore not a repair of the ACI design; it replaces ACI with Conformal PID.

Three consequences are absorbed here rather than discovered later:

- **ACT23 becomes a baseline arm, not only a citation.** Arm `N0` below is Conformal PID with
  no movement penalty, and it is the arm every matched comparison is made against.
- **Turnover measured on an ACI arm does not transfer to a Conformal PID arm**, because ACI's
  width moves through the empirical quantile function while Conformal PID's moves additively
  on the score scale. No cross-producer turnover comparison is claimed. Cross-producer rows
  appear in the tables and are labelled descriptive.
- **`C_sat` and `K_I` enter as new free parameters** that ACT23 themselves set by heuristic
  and describe as *"fine-tuned during a burn-in period"*. They are fixed in §4 as R15.

| id | Producer | Role |
|---|---|---|
| **P-PID** | Conformal PID (ACT23), `q_{t+1} = q̂_{t+1} + r_t(E_t)`, `E_t = Σ_{i≤t}(err_i − α)` | **Primary.** Carries placements A, B and C, so the A-versus-B contrast is within-producer and confound-free |
| **P-ACI** | ACI (Gibbs & Candès), `α_{t+1} = α_t + γ(α − err_t)`, deployed `Q̂_t(1−α_t)` | **Secondary.** Carries placement A only, which is the only placement its recursion admits. Retains continuity with the project's inherited framing |

Every arm below is run twice, once under each interval construction of R1 (empirical quantile
primary, Gaussian proxy secondary), and both are reported.

### 2.2 The arm register

`w` is the L2 retention weight, `τ` the L1 threshold in units of the reference arm's mean
deployed width.

| id | Producer | Placement | Definition | Why it is in the experiment |
|---|---|---|---|---|
| `N0` | P-PID | — | No penalty. Rolling-empirical-quantile scorecaster, constant-gain clipped integrator | Reference arm. All matching is to `N0` |
| `N0t` | P-PID | — | As `N0` with ACT23's tan integrator and their own `C_sat`, `K_I` heuristics | The opposite corner of the exchange: weak inherited rate, small injected movement |
| `B1` | P-PID | **B** | L2 penalty on the slot: `q̂_{t+1} = (1−λ)q̂_t + λ q̂ʳᵃʷ_{t+1}`, `λ = 1−w` | **Primary treatment.** The placement the claim describes |
| `B1τ` | P-PID | **B** | L1 penalty on the slot: `q̂_{t+1} = q̂_t + S_τ(q̂ʳᵃʷ_{t+1} − q̂_t)` | The other branch of OI-1. Implemented, not chosen here |
| `B1a` | P-PID | **B** | As `B1τ` with asymmetric thresholds, `τ⁻/τ⁺ = α/(1−α) = 1/9` | Discharges `docs/GATES.md` G3.2: the accumulator's increments are `+(1−α)` on a miss and `−α` on a cover, so a symmetric threshold suppresses one direction only |
| `B2` | P-PID | **B** | The penalty is applied to **deployed** movement: `q̂ʳᵃʷ` pre-subtracts `r_{t}(E_{t})`, then the L2/L1 penalty acts, then the result is clipped to `[−b/2, b/2]` | **The named dilemma arm** (§2.3) |
| `B3` | P-PID | design lever | Relay / dead-band integrator, `r_t(x) = b·sign(x)·1{|x| ≥ c·h(t)}`, no scorecaster penalty | Condition (4) lower-bounds `r_t` past the threshold and requires neither continuity nor strict monotonicity, so this integrator is admissible and Theorem 1 applies to it verbatim. It contributes exactly zero movement inside the band |
| `A1` | P-PID | **A** | EMA on the completed output, `q̃_{t+1} = (1−w)q_{t+1} + w q̃_t`; the recursion is fed the **deployed** indicator `1{s_t > q̃_t}` | **The forfeit arm.** This is what a practitioner who smooths the output actually builds |
| `A1b` | P-PID | **A** | As `A1`, but the recursion is fed the **raw** indicator `1{s_t > q_t}` | The variant in which the inherited identity certifies a set nobody deploys — `docs/FRAMING.md` §4, seventh item |
| `A2` | P-PID | **A** | Running-mean smoother on the completed output (growing time constant) | Wave 1 measured `max_t|E_t|` growing faster than `h(T) = log T` here |
| `C1` | P-PID | **C** | Smoothed feedback inside the integrator's argument, `r_t(Σ_i(g_i − α))` with `g` a sigmoid relevance function, `g(0) = α` | The third placement (§1.2). Diagnostic: the raw miscoverage sum versus the smoothed one |
| `K0` | P-ACI | — | ACI, no penalty, `γ` fixed | ACI reference |
| `K1` | P-ACI | **A** | EMA on the deployed `Q̂_t(1−α_t)` | ACI's only available placement |
| `P0` | P-PID | placebo | Penalty present in the code path but inert (`w = 0`, `τ = 0`) | Must reproduce `N0` **bit-identically**. A placebo that is merely close is a bug report |

**Penalty-strength grid**, applied to `B1`, `B1τ`, `B1a`, `B2`, `A1`, `A1b`, `K1`:
`w ∈ {0.5, 0.9, 0.99, 0.999}` and `τ ∈ {0.10, 0.25, 0.50, 1.00} × E[L]_{N0}`.
`w = 0.999` is included deliberately: it is the setting at which wave 1 measured
`max_t|E_t| = 623.7` under Placement A, and the claim in §1.1 is precisely that the forfeit
grows in the knob a turnover-motivated designer turns up. Omitting it would omit the finding.

### 2.3 The dilemma arm, stated rather than passed over

Under Placement B the penalty acts on `q̂` while turnover is generated by `q = q̂ + r_t`.
Penalising `q̂`'s movement solves a different optimisation problem from the one the paper
poses. Penalising *deployed* movement is legal — `r_t(E_t)` is past-measurable, so `q̂_{t+1}`
may pre-subtract it — but Theorem 1's `b/2` cap on `q̂` against condition (4)'s requirement
that `r_t` reach `±b` means that at most half the integrator's reach can be offset this way
(`research/S2/D2-attack.json`, `integrator_movement_….argument`).

**This protocol resolves the dilemma by measuring it.** Arm `B2` implements the
pre-subtracting scorecaster with the `[−b/2, b/2]` clip in place, and the required output is
the measured **offset fraction**

> `Φ = 1 − Σ_t|Δq_t^{B2}| / Σ_t|Δq_t^{N0,r-only}|`,

the share of the integrator's own movement that the deployed-movement penalty actually
removes, together with the fraction of steps on which the clip binds. The arithmetic above
predicts `Φ ≤ 0.5` in the saturated regime. `Φ` is a reported quantity of the experiment, and
the clip-binding frequency is a required per-arm diagnostic (§7). Arm `B1` remains the primary
treatment because it is the placement the claim describes; `B2` is its named companion and
the two are always reported together.

---

## 3. The matching contract and its enforcement order

### 3.1 What is matched, and to what tolerance

| Quantity | Tolerance | Source of the tolerance |
|---|---|---|
| Realised coverage, arm versus `N0` | **within 0.002** | `docs/GATES.md` G2.10, fixed before this protocol |
| Mean deployed width `E[L]`, arm versus `N0` | **within 0.5 % relative**, i.e. `|E[L]_arm − E[L]_{N0}| ≤ 0.005·E[L]_{N0}` | Derived in §3.2 |

Both are verified and reported **per arm**, in the match-verification table, for every arm in
§2.2 and every cell of the penalty-strength grid.

### 3.2 Why the width tolerance is 0.5 %, derived rather than asserted

The tolerance must be small enough that the *level* channel cannot manufacture a growth
difference comparable to the smallest difference the paper intends to claim. With the position
map of R6, `π = λ·μ·z²/q²`, a relative width mismatch `δ` moves the position by
`Δπ ≈ −2δπ`, and since `dg/dπ = μ(1−λ)` at a `λ`-fractional Kelly position, the induced
annual log-growth difference is

> `Δg ≈ −2·δ·λ·(1−λ)·SR²`, where `SR = μ/σ̄` is the unconditional Sharpe ratio.

At the values fixed in §4 (`μ = 0.06`, `σ̄ = 0.1403`, so `SR² = 0.183`), the coefficient
`2λ(1−λ)SR²` is 0.047 at `λ = 0.15`, 0.092 at `λ = 0.50` and 0 at `λ = 1.00` — full Kelly is
first-order insensitive because growth is stationary in `π` there. The worst case across the
`λ` grid is `λ = 0.50`. A tolerance of `δ = 0.005` therefore caps the level-channel artefact
at `0.005 × 0.092 = 4.6×10⁻⁴`, i.e. **0.046 points of annual log growth, 15 % of the
smallest growth difference the paper intends to claim** (0.30 points, §6.3). The second-order
term is `2δ²σ²π² ≈ 9×10⁻⁶`, negligible.

If `λ`, `μ` or the volatility calibration changes, the tolerance is recomputed from the
displayed formula before the sweep, not after.

### 3.3 The mechanism that enforces the ordering

`docs/GATES.md` G2.10 requires the match-verification table to be produced, committed and
inspected **first**, and warns that a tolerance chosen after seeing the growth column is not a
tolerance. An intention will not survive contact with a session that wants a result. The
mechanism:

1. **The matching knob is fitted before either stage runs.** Each arm carries one scalar
   width multiplier `m_arm`, fitted by bisection on `N_cal = 20` **calibration paths drawn
   from a disjoint seed block** (`seed_base_cal`), to bring `E[L]_arm` within `0.00125`
   relative (a quarter of the tolerance) of `E[L]_{N0}`. `m_arm` is then written into the
   frozen configuration and never refitted. Calibration-path results are not reported and
   their seeds never appear in the measurement run. Coverage is **not** tuned: it is measured.
2. **Stage 1 is a separate executable with no growth code path.** `run_match` emits
   `results/match-<runid>.json` carrying, per arm and per path: realised coverage, `E[L]`,
   `Var(q)`, time-at-clip, time-at-cap, saturation frequency, `max_t|E_t|`, and the CRN
   hashes. It contains **no turnover field, no cost field and no growth field**, because the
   functions that compute them are not imported by it.
3. **Stage 1's output is committed before stage 2 runs.** Its git commit hash and the
   SHA-256 of its content are recorded.
4. **Stage 2 refuses to start** unless it is given the path of a stage-1 JSON whose recorded
   configuration hash equals the hash of the configuration stage 2 is about to run, and whose
   git commit exists in the repository history. It writes that hash and that commit into its
   own output. Stage 2 reads the frozen configuration; it cannot alter it.
5. **The tolerances are fields of the frozen configuration and enter its hash.** Changing a
   tolerance changes the hash, invalidates every stage-1 record, and forces a re-run and a new
   commit — so a post-hoc widening is visible in `git log` rather than invisible in a
   parameter file.

**If an arm does not match, the finding is that it does not match.** Such an arm is reported
in the match table, is excluded from every matched claim, and its growth column is reported
under an explicit unmatched label. The tolerance is not widened.

---

## 4. The free-choice register, resolved

Every entry: **choice**, **value**, **justification**, **what it would change if wrong**.
R1–R13 are `audit/RECONSTRUCTION_SPEC.md`'s register, in its numbering. R14–R25 are the
choices the corrected claim introduces. R1, R2, R6 and R7 are marked OPERATOR in the register;
this protocol fixes values for all four and flags them for operator override at freeze time,
which is not the same as leaving them open. Only OI-1 and OI-2 (§8) are genuinely open.

### R1 — Is the interval conformal at all?

- **Choice.** Empirical-quantile construction or a Gaussian proxy `ŝ_t·z(α_t)`.
- **Value. Both, always, in every table. Primary: the empirical quantile of the trailing
  `W_q = 250` scores.** Under P-ACI the deployed quantile is `Q̂_t(1−α_t)` with the order
  statistic `⌈(W_q+1)(1−α_t)⌉/W_q`. Under P-PID the scorecaster's raw output is `Q̂_t(1−α)` at
  the **nominal** level. **Secondary: the Gaussian proxy** `ŝ_t·z(α_t)` (P-ACI) and
  `ŝ_t·z_{1−α/2}` (P-PID), with `ŝ_t` from R4.
- **Justification.** The register's own reasoning: the empirical quantile is what the
  literature means by ACI and what the named baselines are, and a parametric interval
  presented as conformal will be caught by this programme committee. The quantisation matters
  substantively and not only nominally: the empirical quantile is a step function of `α_t`, so
  small `α_t` movements often produce **zero** width movement — a dead-band arising free from
  the estimator, which may absorb part of the effect. This protocol therefore makes the free
  dead-band a measured quantity (§7, zero-movement fraction) rather than an unexamined
  confound. **A structural asymmetry between the two producers follows and must be reported:**
  the free dead-band exists under P-ACI and largely disappears under P-PID, because the
  integrator's gain term `r_t(E_t) − r_t(E_{t−1})` is driven by `err_t − α ∈ {−α, 1−α}` and is
  therefore never zero on any step (`research/S2/D1-reduction.json`,
  `d_deployed_interval.delta_q_decomposition`).
- **If wrong.** If the effect survives only in the Gaussian arm, that is a finding about the
  paper, not an implementation detail, and it is reported as such.

### R2 — Regime-switching process

- **Choice.** Number of states, per-state volatility, transition mechanism, whether the drift
  switches, whether the state is observable.
- **Value.** `K = 2`, unobserved, first-order Markov, **drift constant across states**.
  Volatility levels and transition probabilities from **Hardy, M. R. (2001), "A
  Regime-Switching Model of Long-Term Stock Returns", *North American Actuarial Journal*
  5(2):41–53, doi 10.1080/10920277.2001.10595984** — the RSLN-2 maximum-likelihood fit to
  monthly S&P 500 total-return data. Monthly parameters used: `σ₁ = 0.0350`, `σ₂ = 0.0748`,
  `p₁₂ = 0.0398`, `p₂₁ = 0.3798`. Converted to a daily step by a mean-dwell-preserving
  embedding at 21 trading days per month:

  | Daily quantity | Value | Annualised (×√252 or ×252) |
  |---|---|---|
  | `σ_lo` | 0.0076376 | 12.12 % |
  | `σ_hi` | 0.0163229 | 25.91 % |
  | volatility ratio | 2.137 | — |
  | `p_lo→hi` | 0.00189524 | mean dwell 527.6 days ≈ 2.09 yr |
  | `p_hi→lo` | 0.01808571 | mean dwell 55.3 days ≈ 0.22 yr |
  | stationary `(π_lo, π_hi)` | (0.9051, 0.0949) | — |
  | unconditional `σ̄` | 0.0088359 | **14.03 %** |

  Sensitivity grid, reported: volatility ratio ∈ {1.5, **2.137**, 3.0} and dwell times scaled
  by {0.5×, **1×**, 2×}.
- **Justification.** The register requires a cited published calibration rather than invented
  numbers, and requires the sensitivity grid to carry more weight than any single cell. Hardy
  (2001) is the standard two-regime equity calibration and its bibliographic record was
  verified against Crossref in this session. The drift is held constant across states on the
  register's own recommendation: a state-dependent drift confounds the mechanism with a
  market-timing effect and makes the Kelly position respond to something other than the
  interval. The state is never observable to the predictor. The daily embedding preserves the
  mean dwell time (geometric with mean `1/p`) and the per-step variance; it does not reproduce
  the exact monthly transition semantics, and that is recorded here rather than left implicit.
- **What is not verified, and how it is handled.** The bibliographic record is verified; **the
  numeric transcription of Hardy's parameter table was not obtained from the printed table in
  this session** — the values above are corroborated second-hand. This is recorded as
  **OI-2** in §8, with both options specified, and it is a blocking pre-sweep check.
- **If wrong.** Regimes too persistent make the adaptation problem trivial; regimes too fast
  make every arm unable to track and can invert the ranking. The sensitivity grid is what
  protects the claim, which is why it is required rather than optional.

### R3 — Return distribution within a regime

- **Choice.** Gaussian or heavy-tailed; i.i.d. or autocorrelated; the drift `μ`.
- **Value.** Gaussian i.i.d. within regime, primary. Student-t with 5 degrees of freedom,
  scaled to match the regime variance, as a robustness arm. **`μ = 0.06` per annum, constant
  across states, known to the position map** (see R6). Sensitivity: `μ ∈ {0.03, 0.06, 0.09}`.
- **Justification.** `μ` is load-bearing and the register records that the inherited growth
  figure is reproducible by infinitely many `(μ, λ, cap)` triples, so it must be stated. 6 %
  per annum is a conventional long-run equity risk premium; it is asserted as a design
  constant, not fitted, and every reported growth quantity is a **paired difference**, in
  which a common `μ` scales both arms identically. Heavy tails interact with R1 exactly as the
  register warns: a Gaussian `z(·)` under t-distributed returns systematically under-covers,
  which pushes `α_t` down and changes the jitter regime, so the t arm is run under both
  constructions.
- **If wrong.** The absolute growth level moves; the paired differences and the turnover
  columns move much less. The `μ` sensitivity grid demonstrates that rather than asserting it.

### R4 — The scale estimator `ŝ_t`

- **Choice.** Estimator family and window.
- **Value.** **Fixed-length trailing rolling standard deviation, window `W_s = 250` steps**,
  held identical across every arm, every penalty level and every cost level. **No EWMA in the
  primary specification.** Window sweep reported: `W_s ∈ {60, 125, 250, 500}`, and the
  calibration window for the empirical quantile `W_q` is swept with it.
- **Justification.** The register calls this the most under-appreciated confound in the design
  and it is right: `ŝ_t` is itself an adaptive object with its own adaptation rate, and an
  EWMA half-life is a second adaptation rate confounded with the variable under study. 250
  steps is one trading year: long enough that estimator churn does not dominate, short enough
  that it tracks the 55-day high-volatility regime imperfectly, which is the realistic case.
  The register's evidence that this is not optional: the inherited γ = 0 arm carried annual
  turnover **3.2, entirely from `ŝ_t` churn** (`audit/NUMBERS.md` row 42;
  `audit/RECONSTRUCTION_SPEC.md` R4).
- **If wrong.** A short window compresses the effect under estimator churn; a long window
  makes the setup unrealistic. "The effect exists at every scale window we tried" is the claim
  the sweep buys, and it is much stronger than "the effect exists at our window".

### R5 — Clipping of `α_t`

- **Choice.** The rule that keeps `α_t` in range, and what happens outside it.
- **Value.** `α_t` is clipped to `[1/(W_q+1), 1 − 1/(W_q+1)] = [0.003984, 0.996016]` at
  `W_q = 250`, and the deployed quantile is always finite. A **secondary arm runs the
  published convention** with no clip and `α_t ≤ 0 ⟹ Q̂ = ∞`, reporting the fraction of
  infinite-width steps. **Time-at-each-bound is a required per-arm diagnostic** (§7).
- **Justification.** The clip bounds are exactly the range over which the empirical quantile of
  a `W_q`-window is defined without extrapolation, so the rule is a property of the estimator
  rather than an arbitrary constant. An infinite deployed width is disqualifying under this
  design for a separate and decisive reason: it destroys `E[L]` matching and makes `Σ|Δq|`
  infinite at the first occurrence, and `Σ|Δq|` is the paper's primary measured quantity. The
  secondary arm exists so that the choice is shown not to be doing the work. The register's
  warning that the clip dominated the inherited headline arm is defused structurally here:
  `γ` is no longer the manipulated variable (R19), so no arm is a saturated-clip artefact by
  construction — but the diagnostic is reported anyway, because that is how one knows.
- **If wrong.** If an arm spends a large fraction of its time at a bound, its width path is
  governed by the clipping rule rather than by the recursion, and any turnover claim about it
  is a claim about the clip. The diagnostic is what makes that visible.

### R6 — The position map and the Kelly fraction

- **Choice.** Functional form, `λ`, and whether the drift in the position is true or estimated.
- **Value.** `π_t = λ·μ / σ̂_t²` with `σ̂_t = q_t / z_{1−α/2}` and **the nominal `α`**
  (`z_{0.95} = 1.6449`), **true `μ`**, **long-only**, **fraction of wealth**.
  `λ ∈ {0.15 (primary), 0.50, 1.00 (full Kelly)}`. **Every null in §6.2 is reported at full
  Kelly as well as at the fractional settings.**
- **Justification.** Dividing by `z(α_t)` rather than the nominal `z_{1−α/2}` would cancel the
  calibration adjustment out of the position entirely and the experiment would measure
  nothing; the register names this as the difference between an experiment that works and one
  that does not, and it is stated here explicitly so the implementation cannot get it wrong
  silently. `λ = 0.15` is primary because it matches the configuration the applied arm
  replicates (`docs/GATES.md` G4.1, `κ = 0.15`). Full Kelly is required because that is where
  the competing MacLean–Thorp–Ziemba overbetting channel is strongest, and a Kelly-literate
  reviewer will raise exactly that objection against a null obtained only at `λ = 0.15`
  (`docs/OPEN_QUESTIONS.md` Q6). True `μ` is used because it isolates interval movement as the
  only moving part; an estimated `μ̂` would add a second noise channel and reopen the
  estimation-error explanation. **Any use of an estimated `μ̂` in any arm must be reported**,
  because it directly weakens the falsified-variance claim.
- **If wrong.** Using `z(α_t)` destroys the mechanism. Reporting the null only at small `λ`
  leaves the overbetting channel untested and the null unpersuasive.

### R7 — Leverage cap

- **Choice.** Whether the position is capped, and at what level.
- **Value.** **Gross cap 2.0**, primary, matching Ryan's configuration (`docs/GATES.md` G4.1).
  Also run: cap 4.0, and **capless**. **Time-at-cap is a required per-arm diagnostic** (§7).
- **Justification.** As `σ̂_t → 0` the Kelly position diverges, and the applied arm is a
  replication of a capped configuration, so a capless simulation would be replicating
  something else. The cap is also a second dead-band: a position pinned at the cap does not
  move when `q_t` moves. If one arm sits at the cap more often than another, the cap is
  silently doing part of the work attributed to the penalty. Three cap levels plus the
  diagnostic is what converts that risk into a measurement. Note the interaction with R6: at
  `λ = 1.00` and `σ_lo`, the uncapped position is `μ/σ_lo² = 4.08`, so the cap binds heavily
  in the low-volatility regime and the time-at-cap column will be large — which is a
  reportable property of full Kelly under a cap, not a defect to be hidden.
- **If wrong.** A cap that binds asymmetrically across arms makes the turnover comparison a
  comparison of cap occupancy. The diagnostic detects it; the capless arm bounds it.

### R8 — Horizon, annualisation and the turnover metric

- **Choice.** Steps per path, trading days per year, and the definition of annual turnover.
- **Value.** **`T_total = 10,330` steps per path; burn-in 250 (R11); measurement window
  `T = 10,080` steps = exactly 40.0 years at 252 trading days per year.** Turnover is
  **one-way**, `Σ_t|π_t − π_{t−1}|` over the measurement window divided by 40. Growth is
  annualised by dividing total log return by the number of years.
- **Justification — and the horizon is not a free parameter.** The exchange in §1.1 closes the
  short-horizon corner arithmetically. With a constant-gain integrator the product of
  Proposition 2's coverage-gap bound `ε` at horizon `T` and the integrator's own per-step
  movement `M` is `2α(1−α)b/T` exactly, with the gain cancelling. Inverting at `α = 0.10`:

  | `T` | movement forced by a 1-point coverage bound (`ε = 0.01`) | in units of `B = b/2` |
  |---|---|---|
  | 500 | `18b/T = 0.036·b` | **0.072·B** |
  | 2,500 | `0.0072·b` | 0.0144·B |
  | **10,080** | **0.001786·b** | **0.0036·B** |

  At `T ≈ 500` — about two years of trading days — a 1-point coverage bound forces roughly
  0.072·B of deployed movement **every step**, which for a plausible `B` of a few daily
  standard deviations is a large fraction of a typical half-width and would swamp any turnover
  reduction. At `T ≈ 10,000` the same bound forces 0.0036·B, small enough that a five- to
  tenfold turnover reduction remains available to be measured. The primary horizon is chosen
  on that arithmetic (`research/S2/D2-attack.json`, `integrator_movement_….argument`,
  numbers block). 40 years is long for an applied claim and this is the synthetic arm; the
  applied arm's window is fixed by the data at about 1,511 development days, where the same
  arithmetic forces 0.024·B, and §9 records that the arithmetic does not close there.
- **If wrong.** Running the headline at a short horizon with a tight coverage claim puts the
  experiment in the corner the arithmetic has already closed. A different annualisation
  convention rescales every turnover figure and must agree with the cost model (R9).

### R9 — Cost application

- **Choice.** Whether the proportional cost is subtracted from the log return or applied to
  the wealth multiplier, and what it is charged on.
- **Value.** Charged **additively on the log scale**: the step's log return is
  `log(1 + π_t·r_{t+1}) − c·|π_t − π_{t−1}|`, with `c` the one-way proportional rate and the
  position expressed as a fraction of wealth. **Cost grid `{0, 5, 10, 15, 20}` bps**, primary
  display at **5 bps** (the applied configuration's rate, G4.1) with 15 bps also displayed.
  The multiplier convention is computed once at the primary configuration and reported
  alongside, to show the choice is not doing work.
- **Justification.** The log-additive convention makes the cost identity `gross − net =
  c × turnover` hold to floating-point tolerance, which is what makes test 3 of §3 of the
  register an actual audit of the cost model rather than a formality. Five cost levels satisfy
  the reproduction target that cost-rate monotonicity hold over at least five levels. The
  difference between the two conventions is `O(c²)` per step and is reported rather than
  argued. **The position map does not depend on `c`** — cost does not feed back into the
  decision — so all five cost levels are derived from one simulation per arm per path, which
  is why the cost grid is free and why the cost identity is exact.
- **If wrong.** A cost model that disagrees with the turnover convention breaks the identity
  test and, with it, the only internal check on the growth column.
- **The register's warning, carried forward.** `audit/NUMBERS.md` §9.1 shows the inherited
  growth column is the cost identity to within about 5 % of the effect. That is why §1.4 puts
  turnover first, and why §5.4 requires the gross/drag/residual decomposition per arm.

### R10 — Common random numbers

- **Choice.** RNG family, seed policy, what is held common.
- **Value.** `numpy.random.Generator(PCG64(seed_base + path_index))`. The complete
  `(regime, return)` path is generated and cached **before** entering the arm loop and is
  reused byte-identically across every arm, every penalty level and every cost level.
  `seed_base = 20260819` for the measurement run; `seed_base_cal = 20260818` for the matching
  calibration paths; `seed_base_pilot = 20260817` for the power pilot. Bit-identity is
  asserted by recording the SHA-256 of each cached path array in the results JSON and checking
  equality across arms.
- **Justification.** Any RNG draw inside the arm loop breaks pairing and inflates every
  standard error. Recording the hashes rather than asserting the property makes the claim
  checkable from the results file alone. The three seed blocks are disjoint so that the
  matching fit and the power pilot cannot contaminate the measurement.
- **If wrong.** Broken pairing inflates the standard errors by roughly the factor the
  inherited plan claimed to have gained by pairing, and every power calculation here becomes
  wrong in the optimistic direction.

### R11 — Burn-in and measurement window

- **Choice.** What to discard.
- **Value.** Discard the first `max(W_s, W_q, 250) = 250` steps. Coverage is **reported both
  ways once** — whole path and post-burn-in — at the primary configuration.
- **Justification.** `ŝ_t` and `Q̂_t` are undefined before a full window, and `α_t` and `E_t`
  need time to leave their initial values. The register notes that this choice materially
  changes the inherited γ = 0 coverage figure, so reporting both once is what shows the choice
  is not doing work.
- **If wrong.** A too-short burn-in imports initialisation transients into the coverage column,
  which is the column the matching contract is enforced on.

### R12 — `Var(Δq)` and `Var(q)`

- **Choice.** Pooled or per-path; absolute or normalised; and by what.
- **Value.** Computed **per path, then averaged, with the per-path standard deviation
  reported** (consistent with R13). **Primary: `Var(Δq_t) / q̄_ref²`, where `q̄_ref` is the
  mean deployed width of the reference arm `N0` in the same matched set** — one common
  constant per matched set. **Secondary: absolute `Var(Δq_t)`.** **`Var(q_t)` at the level is
  reported alongside**, per `docs/GATES.md` G2.7. The per-arm own-mean normalisation
  `Var(Δq/q̄_arm)` is additionally reported once at the primary configuration.
- **Justification — the normalisation question, resolved.** The register recommends
  normalising by mean width because an absolute statistic is not scale-free and the ratio
  across arms is partly an artefact of arms having different mean widths. Dividing by **each
  arm's own** mean, however, makes the statistic non-comparable in precisely the case that
  matters: it silently rescales arms against each other. Dividing by a **single constant per
  matched set** removes the scale dependence without introducing the cross-arm rescaling, and
  under this design the two agree to within the matching tolerance by construction — which is
  itself a check worth printing. Reporting the own-mean version once demonstrates that.
  Whichever version any recomputed multiple refers to must be stated when it is recomputed.
- **If wrong.** A ratio across arms that is partly an artefact of differing mean widths is
  exactly the confound the matched-width design exists to remove, so getting this wrong
  reintroduces it in the statistic while the design has removed it from the arms.

### R13 — Coverage and standard-error conventions

- **Choice.** Pooled or per-path coverage; the paired standard error; multiplicity.
- **Value.** Coverage computed **per path, then averaged**, with the per-path standard
  deviation reported; pooled coverage reported once as a check. Paired standard error
  `sd(d_i)/√N` on the per-path differences. **Multiplicity: Holm–Bonferroni within each of the
  two pre-declared families of §6.2, with the family membership fixed in this document.**
- **Justification.** Per-path-then-averaged is the convention under which the paired standard
  error is the right denominator, since pairing operates at the path level. The register offers
  the choice of stating that no correction is applied or applying one; a correction is applied,
  because the primary family has six members and an uncorrected family of six at 5 % has a
  family-wise error near 26 %.
- **If wrong.** Pooling over `(path, t)` understates the standard error by ignoring
  within-path dependence, and every significance figure inherits the understatement.

---

### R14 — Producer set and placement assignment

- **Choice.** Which producer carries which placement.
- **Value.** As §2.1 and §2.2: **P-PID carries A, B and C; P-ACI carries A only.** The A↔B
  contrast is made **within P-PID**. Cross-producer rows are reported and labelled
  descriptive.
- **Justification.** ACI has no `q̂` slot, so Placement B is unavailable there
  (`research/S2/D2-attack.json`, `is_placement_B_a_change_of_subject`); and ACI's width moves
  through the empirical quantile function while Conformal PID's moves additively on the score
  scale, so a cross-producer turnover comparison would compare two different mechanisms and
  attribute the difference to the placement. Keeping A and B on one producer is what makes the
  paper's central difference identified.
- **If wrong.** A cross-producer A-versus-B comparison is confounded with the producer, and
  the confound is exactly the size of the effect being claimed.

### R15 — The integrator `r_t` and its parameters

- **Choice.** The saturation function, its gain, and the constants `(b, c, h)` that realise
  condition (4).
- **Value.** Three integrators, all satisfying condition (4).
  1. **Primary: constant-gain clipped integrator**, `r(x) = clip(η·x, −b, b)`, which satisfies
     (4) with `h ≡ 1` (constant, hence nonnegative, nondecreasing and sublinear — admissible)
     and `c = b/η`. **`η = b/200`**, so `c = 200` and Proposition 2's bound at the measurement
     horizon is `(c·h(T)+1)/T = 201/10,080 = 0.01994`.
  2. **Secondary: ACT23's tan integrator**, `r_t(x) = K_I·tan(x·log t /(t·C_sat))`, with their
     own Appendix-B heuristics `C_sat = (2/π)(⌈δ·log T⌉ − 1/log T)` and `K_I = B'`, which
     satisfies (4) with `h(t) = t/log t` and `c = C_sat·arctan(b/K_I)`. Finite-`b` reading,
     `K_I = B`, `b = 2B`. At `T = 10⁴` the bound is **0.0683**.
  3. **Design-lever arm `B3`: relay with dead band**, `r_t(x) = b·sign(x)·1{|x| ≥ c·h(t)}`,
     `h ≡ 1`, `c = 200` to match the primary's threshold.
- **Justification.** The primary is the constant-gain integrator for two reasons. First, the
  exchange in §1.1 is **exact** there — `ε·M = 2α(1−α)(b + η)/T` with the gain cancelling from
  the leading term — so the check in §5.5 is a genuine prediction rather than an
  order-of-magnitude gesture. Second, its inherited guarantee is quantitatively meaningful at
  the chosen horizon: `±0.0199` against a target of `α = 0.10`, versus `±0.0683` for ACT23's
  own tan integrator at `T = 10⁴` — 3.4× tighter (`research/S2/D2-attack.json`,
  `numeric_bound_table`, which also records the secondary finding that the tan bound is
  identical for `δ = 0.01, 0.05, 0.10` because `⌈δ·log T⌉ = 1` for every `δ ≤ 1/log T`, so
  asking that heuristic for a tighter guarantee changes nothing). The tan integrator is run as
  the secondary because it is ACT23's default and because it occupies the opposite corner of
  the exchange: wave 1 measured its total injected movement flat against `log²T` at ratios
  0.130 / 0.137 / 0.134 / 0.136 across `T = 10³…10⁶` with the scorecaster frozen, i.e.
  `Θ(log²T)` total, at the price of the `O(1/log T)` rate
  (`research/S2/D1-reduction.json`, `d_deployed_interval.integrator_injected_movement`).
  **Both corners are the paper's point, so both are run.** `η = b/200` is chosen so that the
  integrator's own per-step movement `M = 2α(1−α)η = 0.18η` is 0.88 % of the mean deployed
  width — comparable to the scorecaster's own churn, so the decomposition in §5.2 is
  informative rather than dominated by one term. `η` is swept over `{b/200, b/50, b/12.5}` to
  trace the exchange, which is the figure the conservation check produces.
  The relay is admissible because condition (4) only **lower-bounds** `r_t` past the threshold
  and requires neither continuity nor strict monotonicity; inside the band both the gain term
  and the schedule term vanish, so it contributes exactly zero movement there and Theorem 1
  applies to it verbatim. Proposition 2 bounds `|E_T|` and does not bound the number of band
  crossings, so the crossing count is measured and reported (§7) and the arm is labelled a
  design lever with an empirical question attached, not a theorem.
- **If wrong.** A gain too large makes the integrator's own movement dominate the total and
  leaves the penalty nothing to reduce; too small, and the inherited guarantee is weak enough
  that the "inherits an existing coverage guarantee" sentence over-promises. The `η` sweep
  turns that risk into the paper's own figure.

### R16 — The scorecaster `q̂ʳᵃʷ` and its clipping

- **Choice.** The scorecaster family, its window, and how boundedness is realised.
- **Value.** **Rolling empirical quantile of the trailing `W_q = 250` scores at the nominal
  level `1 − α`** (primary), or the Gaussian proxy (R1 secondary). **The output is clipped to
  the observed score range `[−b/2, b/2]` as an explicit algorithmic step.** The anchor for
  every penalty is **`q̂_t`, the previous value of the slot — never the deployed `q_t`.**
  ACT23's Theta-model scorecaster is **not** run.
- **Justification.** Theorem 1 requires `{q̂_t} ⊂ [−b/2, b/2]`; a rolling empirical quantile of
  clipped scores satisfies it automatically, and the explicit clip is stated so that a learned
  scorecaster could be substituted without silently violating the hypothesis. The anchor choice
  is decisive and is fixed here because it is the easiest thing to get wrong: anchoring to the
  deployed `q_t` gives `q̂_{t+1} = (1−w)q̂ʳᵃʷ_{t+1} + w·q̂_t + w·r_{t−1}(E_{t−1})`, which
  re-injects the integrator's output into the slot. Condition (4) only lower-bounds `r_t` and
  does not cap it — ACT23's own default integrator is unbounded — so the slot loses its a
  priori bound, and even with a bounded saturator the requirement `sup|q̂| ≤ b/2` becomes
  vacuous unless `w < 1/3`, at the cost of a `1/(1−w)` blow-up in the required `b`. It also
  creates a second accumulator in series with the first whose output passes through no
  saturating readout, which is the windup the saturating readout exists to prevent
  (`research/S2/D1-reduction.json`, `b_penalised_qhat.prev_ambiguity_resolved`). A learned
  scorecaster is excluded from the primary because it introduces a second adaptation rate,
  which is the R4 confound in a new place.
- **If wrong.** Anchoring to the deployed value silently breaks the one hypothesis Placement B
  actually incurs, and the inheritance claim in §1.1 becomes false for the implemented
  algorithm while remaining true for the described one.

### R17 — The penalty forms

- **Choice.** L1, L2, or both; and the exact update.
- **Value. Both are implemented.** L2: `q̂_{t+1} = (1−λ)q̂_t + λ·q̂ʳᵃʷ_{t+1}` with
  `λ = 1 − w`. L1: `q̂_{t+1} = q̂_t + S_τ(q̂ʳᵃʷ_{t+1} − q̂_t)`, `S_τ(u) = sign(u)(|u| − τ)₊`.
  **The update step is unit (`κ = 1`); over-relaxed variants are excluded.** Asymmetric L1
  variant `B1a` with `τ⁻/τ⁺ = 1/9`. **Which form is primary is OI-1 and is not decided here.**
- **Justification.** Both forms are convex combinations of quantities already in
  `[−b/2, b/2]`, the L1 case because `S_τ(u) = u(1 − τ/|u|)₊` makes the update an exact convex
  combination with weight `λ_t = (1 − τ/|Δ_t|)₊ ∈ [0,1)`, so neither can enlarge the slot's
  range and neither forces a larger `b`. The unit-step restriction is the one real condition:
  with `κ > 1` the effective weight `κλ_t` exceeds 1 whenever `|Δ_t| > τκ/(κ−1)` and the slot
  leaves the convex hull, at which point the boundedness hypothesis fails
  (`research/S2/D1-reduction.json`, `b_penalised_qhat.master_lemma`). The asymmetric variant
  discharges `docs/GATES.md` G3.2: the accumulator's increments are `+(1−α)` on a miss and
  `−α` on a cover, so a symmetric threshold suppresses one direction only.
- **If wrong.** An over-relaxed update breaks the inheritance claim outright. A symmetric
  threshold alone would leave G3.2's asymmetry untested and invite the over-coverage reading.

### R18 — The score bound `b`

- **Choice.** The analysis constant `b`, and the winsorisation that makes it real.
- **Value.** Scores are `s_t = |y_t − f_t(x_t)|` with the base forecaster **frozen at the
  constant 0** in the synthetic arm. Scores are winsorised at `B_s = 8·σ̄ = 0.070686`
  (8 unconditional daily standard deviations), so `b = 2·B_s = 0.141373`. The winsorisation
  frequency is a required diagnostic.
- **Justification.** `b` is an analysis constant, not an algorithm input — nothing in the
  iteration needs to know it — but Theorem 1's hypotheses are stated in terms of it, so an
  unbounded score range makes the inheritance claim vacuous rather than false. Eight
  unconditional standard deviations is 4.33 high-regime standard deviations, clipping roughly
  1.5 in 10⁵ Gaussian steps and roughly 2.5 in 10⁴ steps of the variance-matched t(5) arm;
  both are reported; essentially all clipping falls in the high-volatility regime. Freezing the base forecaster is what makes `Σ|Δq_t|` **exactly** the
  turnover of the deployed interval half-width: with `s = |y − f|` and `f` constant,
  `C_t = [f ± q_t]` and `Δ(half-width) = Δq_t` identically. If the forecaster were refit the
  interval centre would move too and endpoint turnover would include `Δf_t`, which the penalty
  does not control (`research/S2/D1-reduction.json`,
  `d_deployed_interval.what_sigma_abs_delta_q_measures`).
- **If wrong.** An unbounded score range voids Theorem 1's hypotheses; a refit forecaster makes
  the measured functional something other than what the paper says it is.

### R19 — ACI's step size `γ`, now fixed rather than swept

- **Choice.** `γ` for the P-ACI arms.
- **Value. `γ = 0.02`, identical across every P-ACI arm.** Sensitivity: `γ ∈ {0.005, 0.05}`.
- **Justification.** Under the matched-width design the manipulated variable is the movement
  penalty, so `γ` must be held constant or the design has two manipulated variables and the
  identification failure `docs/FRAMING.md` §5 documents in print returns. `γ = 0.02` is chosen
  because `audit/NUMBERS.md` §9.2 identifies it as where a realistic practitioner's `γ` would
  sit and as the comparison the inherited 60-path design failed to resolve (2.5× effect to
  standard error), so it is the setting at which the new design's power gain is most visible.
- **If wrong.** A `γ` that saturates the clip makes the P-ACI arms a study of the clipping rule
  (R5's warning); the time-at-clip diagnostic detects it.

### R20 — The matching knob and how it is fitted

- **Choice.** What is adjusted to bring arms into the matching tolerance, and on what data.
- **Value.** One scalar width multiplier `m_arm` per arm, fitted by bisection on
  `N_cal = 20` calibration paths from a disjoint seed block to bring `E[L]_arm` within 0.00125
  relative of `E[L]_{N0}`, then frozen into the configuration. **Coverage is not tuned.**
- **Justification.** The matched-width design requires a knob, and it must be one whose use is
  visible and whose fitting data are disjoint from the measurement data. A width multiplier is
  the minimal such knob. Coverage is left untuned because both producers drive realised
  coverage to `α` by feedback, so tuning it would be tuning something the algorithm already
  controls, and because the coverage column is one of the two quantities the matching contract
  verifies — tuning a verified quantity is circular.
- **If wrong.** A knob fitted on the measurement paths is a fit to the answer, and the
  agreement it produces carries no evidential weight (`audit/RECONSTRUCTION_SPEC.md` §1).

### R21 — Execution order and its enforcement

- **Choice.** How the match-before-growth ordering is enforced.
- **Value.** The five-point mechanism of §3.3: knob fitted on disjoint paths; stage-1
  executable with no growth or turnover code path; stage-1 output committed with its content
  hash; stage-2 refuses to run without a committed stage-1 record whose configuration hash
  matches; tolerances inside the hashed configuration.
- **Justification.** `docs/GATES.md` G2.10 requires the ordering and names post-hoc tolerance
  widening as a gate failure. A mechanism that makes the widening produce a visible commit is
  the difference between a rule and a hope.
- **If wrong.** Computing growth first invites tuning to it, which is the specific failure the
  register's opening warning describes.

### R22 — What `Σ|Δq|` is measured on

- **Choice.** Which sequence the movement functional is computed over.
- **Value.** The **deployed** threshold: `Σ_t|q_t − q_{t−1}|` with
  `q_t = q̂_t + r_{t−1}(E_{t−1})`, over the measurement window. Under Placement A it is the
  deployed smoothed sequence `q̃_t`. Position turnover is `Σ_t|π_t − π_{t−1}|` (R8).
- **Justification.** The penalty acts on `q̂` while the measured quantity is `q`; that
  asymmetry is the paper's stated risk and it is real, so the measurement must be on the
  object the decision uses. Measuring on `q̂` would make the penalty look better by measuring
  the thing it directly controls.
- **If wrong.** Reporting the penalty's effect on the quantity it directly controls, rather
  than on the deployed one, is the single easiest way to overstate the result.

### R23 — Which indicator closes the loop

- **Choice.** Whether the recursion is fed the deployed or the raw miscoverage indicator.
- **Value.** Under P-PID with no penalty and under Placement B, `err_t = 1{s_t > q_t}` on the
  **full deployed threshold** — never on `q̂` alone. Under Placement A, **both** variants are
  run: `A1` feeds the deployed smoothed indicator, `A1b` feeds the raw one.
- **Justification.** ACT23's `err_i` is defined on `C_i = {y : s_i(x_i,y) ≤ q_i}` with the full
  threshold, and the proof of Theorem 1 shifts both the score and the quantile by the same
  `q̂_t`, which is exactly the condition under which the transformed system's miscoverage
  indicator equals the deployed one; computing `err` on `q̂` alone collapses the reduction. It
  is also the single easiest implementation error to make
  (`research/S2/D1-reduction.json`, `d_deployed_interval.evidence_locator`). Both Placement A
  variants are run because the difference between them is exactly the concern
  `docs/FRAMING.md` §4 raises in its seventh item: an identity that certifies a set nobody
  deploys.
- **If wrong.** Feeding the wrong indicator makes the inheritance claim false for the
  implemented code and true only for the described one.

### R24 — The penalty-strength grid

- **Choice.** Which penalty strengths are run.
- **Value.** `w ∈ {0.5, 0.9, 0.99, 0.999}`, `τ ∈ {0.10, 0.25, 0.50, 1.00} × E[L]_{N0}`.
- **Justification.** The grid must reach the regime in which the Placement A forfeit is large,
  because the claim is that the forfeit grows in the knob a turnover-motivated designer turns
  up; `w = 0.999` is the setting at which wave 1 measured `max_t|E_t| = 623.7` against a bound
  of 10.2–14.8. Expressing `τ` in units of the reference arm's mean width makes the L1 grid
  scale-free and comparable across configurations.
- **If wrong.** A grid that stops at `w = 0.9` cannot exhibit the forfeit and the Placement A
  claim would rest on the wave-1 numbers alone.

### R25 — The placebo arm

- **Choice.** Whether an inert-penalty arm is run.
- **Value.** Arm `P0`: the penalty code path is active with `w = 0` and `τ = 0`, and its output
  **must equal `N0` bit-identically**. Checked by array hash, not by tolerance.
- **Justification.** Van Belle et al. include a placebo arm and this design is close enough to
  theirs (`docs/FRAMING.md` §0, §5) that omitting one would be conspicuous. Bit-identity rather
  than closeness is the right test because an inert convex combination is an algebraic
  identity; anything else is a defect in the implementation, not noise.
- **If wrong.** A drifting placebo means the penalty code path has a side effect, and every
  treated arm inherits it.

---

## 5. Measurement definitions

All quantities are computed on the measurement window (R11), per path, then averaged across
paths with the per-path standard deviation reported (R13).

### 5.1 Coverage, width, growth

- **Realised coverage**, per path: `1 − (1/T)Σ_t err_t` on the **deployed** interval.
- **Mean width `E[L]`**, per path: `(1/T)Σ_t 2q_t` under the frozen-forecaster convention of
  R18; reported as the half-width `q̄` as well.
- **Gross growth**: `(1/40)Σ_t log(1 + π_t r_{t+1})`.
- **Cost drag**: `(1/40)·c·Σ_t|π_t − π_{t−1}| = c ×` annual turnover.
- **Net growth**: gross minus drag, exactly (R9).
- **Annual turnover**: `(1/40)Σ_t|π_t − π_{t−1}|`, one-way.

### 5.2 The turnover decomposition — two levels, both required

**Level (i): estimator versus calibration path.** Required by `docs/GATES.md` G2.13. The
inherited γ = 0 arm carried annual turnover 3.2 **entirely** from scale-estimator churn
(`audit/NUMBERS.md` row 42; `audit/RECONSTRUCTION_SPEC.md` R4), so an undecomposed turnover
column cannot attribute anything.

Define the **estimator-only path** `q^est_t`: the same width producer re-run on the identical
CRN path with the calibration state frozen — `α_t ≡ α` for P-ACI, `r ≡ 0` for P-PID. Then
report three columns per arm:

| Column | Definition |
|---|---|
| estimator component | `Σ_t|Δq^est_t|` |
| calibration-path component | `Σ_t|Δq_t − Δq^est_t|` |
| interaction residual | `Σ_t|Δq_t| − (previous two)` |

The residual is reported explicitly and may be negative; `Σ|·|` is not additive and pretending
otherwise is how a decomposition becomes a fiction.

**Level (ii): scorecaster versus integrator.** New from wave 1 and required because a reviewer
who knows the exchange in §1.1 will ask which part the penalty reduced. Under P-PID the
increment decomposes **exactly**:

> `Δq_{t+1} = Δq̂_{t+1} + [r_t(E_t) − r_{t−1}(E_{t−1})]`,
> and the bracket splits further into a **gain term** `r_t(E_t) − r_t(E_{t−1})` and a
> **schedule term** `r_t(E_{t−1}) − r_{t−1}(E_{t−1})`.

Report `Σ|Δq̂|`, `Σ|Δr|` split into its gain and schedule parts, `Σ|Δq|`, and the gap
`Σ|Δq̂| + Σ|Δr| − Σ|Δq|`. The gain term is never zero on any step, because
`E_t − E_{t−1} = err_t − α ∈ {−α, 1−α}`; the schedule term is nonzero purely because `r_t` is
indexed by `t`, and for the tan integrator the scale factor `log t/(t·C_sat)` is strictly
decreasing, so the deployed threshold moves even on a round where the accumulator is unchanged
(`research/S2/D1-reduction.json`, `d_deployed_interval.delta_q_decomposition`). The schedule
term appears to be unremarked in the literature and is reported separately for that reason.

**Both decompositions are reported for every arm, including the Placement A and ACI arms**,
where level (ii) is computed on the underlying unsmoothed sequence and the smoother's own
contribution is reported as a third column.

### 5.3 Variance statistics

`Var(q_t)` at the level and `Var(Δq_t)` at the increment, per R12: normalised primary,
absolute secondary, own-mean normalisation once. Also `sd(Δ log q_t)`, because Ryan reports
exactly that statistic (0.00343 versus 0.00391, `docs/FRAMING.md` §6 sentence 4) and the paper
must be able to place its arms next to his numbers.

### 5.4 The growth decomposition

Per arm and per cost level: **gross growth, cost drag, net growth, and the residual**
`gross − drag − net`, which must be zero to floating-point tolerance by R9. This is the
register's R9 recommendation and it is what lets a reader perform `audit/NUMBERS.md` §9.1's
subtraction on this project's own numbers rather than on the inherited table's.

### 5.5 The conservation check — the falsifiable line the paper prints

For every integrator setting, report:

| Symbol | Definition | Predicted |
|---|---|---|
| `ε` | Proposition 2's bound at the measurement horizon, `(c·h(T)+1)/T` | 0.01994 at `η = b/200`, `T = 10,080` |
| `M̂` | measured integrator movement per step, `(1/T)Σ_t|Δr_t|` | `2α(1−α)η = 0.18η = 1.2723×10⁻⁴` |
| `ε·M̂` | the product | `2α(1−α)(b+η)/T = 2.5371×10⁻⁶` |

and the ratio measured/predicted. The prediction is stated in the exact form
`2α(1−α)(b+η)/T` rather than the asymptotic `2α(1−α)b/T`, because the `+1` in Proposition 2's
bound contributes an `η` term that is visible at the top of the `η` sweep.

**Declared in advance:** agreement within **5 %** is expected for the constant-gain arms, where
the derivation is exact; **order-of-magnitude agreement only** is expected for the tan arm,
where the derivation uses the small-`|E|` slope `K_I·log t/(t·C_sat)` and the predicted
constant is `π·α(1−α)·K_I/T`. Also report `E|Δr_t|` against its exact prediction `0.18η` and
the empirical distribution of `|Δr_t|`, which for the constant-gain integrator takes exactly
two values, `ηα` and `η(1−α)`.

The sweep `η ∈ {b/200, b/50, b/12.5}` produces the figure: `ε` falls, `M̂` rises, the product
is flat, and the penalty weight `w` does not appear in it. Failure of that flatness is a
falsification of the paper's central analytical claim and is reported as such.

### 5.6 Placement A's measured forfeit

Per Placement A arm and per `w`: `max_t|E_t|` against Proposition 2's bound `c·h(T)+1`, and
the ratio. Wave 1's reference values under a clipped saturator with `h(t) = log(t+2)`,
`c = 1`, `b = 2`, `α = 0.1` and adversarial scores: unsmoothed `max|E_t|` = 5.5 / 6.6 / 7.8 at
`T = 10⁴ / 10⁵ / 10⁶` against a bound of 10.2 / 12.5 / 14.8; at `w = 0.999`,
`max|E_t| = 623.7`; running mean 10.6 → 41.6 → 71.7. Those are wave-1 numbers under a
different score process and are **not** predictions for this configuration; they are the
reason the diagnostic exists.

**Realised coverage on every Placement A arm is measured and reported as a control, and no
coverage theorem is claimed for it** (`docs/GATES.md` G3.3). The claim the paper makes is
*"Placement A forfeits the inherited theorem and its finite-sample rate and requires a new
argument; Placement B requires none"* — not *"Placement A loses coverage"*, which wave 1
tested against six smoother families and did not observe (miscoverage 0.1000–0.1002 against
`α = 0.10` over `T = 2×10⁵`). A referee can construct that simulation in ten minutes, so the
protocol constructs it first.

### 5.7 The offset fraction, arm `B2`

`Φ` as defined in §2.3, plus the fraction of steps on which the `[−b/2, b/2]` clip binds and
the fraction on which the integrator is saturated. `Φ ≤ 0.5` in the saturated regime is a
prediction of the arithmetic, and it is reported as measured against predicted.

---

## 6. Statistical protocol

### 6.1 Pairing

All comparisons are paired at the path index under common random numbers (R10). The per-path
difference `d_i = X_i^{treat} − X_i^{ref}` is the unit of analysis; the paired standard error
is `sd(d_i)/√N`. Bit-identity of the cached paths across arms is asserted by hash and recorded
(R10), because an unnoticed RNG draw inside the arm loop invalidates every figure in this
section.

### 6.2 The two pre-declared test families

**Family D — difference tests (m = 6), Holm–Bonferroni at family-wise 0.05:**

| # | Comparison | Endpoint |
|---|---|---|
| D1 | `B1` vs `N0` | annual turnover, calibration-path component |
| D2 | `B1` vs `N0` | net annual log growth at 5 bps |
| D3 | `A1` vs `B1` | annual turnover, calibration-path component |
| D4 | `A1` vs `B1` | net annual log growth at 5 bps |
| D5 | `B2` vs `B1` | deployed movement `Σ|Δq|` |
| D6 | `B3` vs `N0` | annual turnover, calibration-path component |

**Family E — equivalence tests (m = 4), TOST, Holm–Bonferroni at family-wise 0.05:**

| # | Null claimed | Test | Margin | Justification of the margin |
|---|---|---|---|---|
| E1 | Gross growth is flat across arms at 0 bps | TOST on paired `d_i` | **±0.06 points of annual log growth** | The paper's attribution claim is that the net difference is a cost-channel effect. A gross difference below 20 % of the smallest claimed net difference (0.30 points, §6.3) leaves at least 80 % of the effect attributable to the cost channel. 20 % is the attribution threshold and it is declared here, before the sweep |
| E2 | Realised coverage is equal, `B1` vs `N0` | TOST | **±0.002** | The matching tolerance fixed by `docs/GATES.md` G2.10, so the equivalence claim and the matching contract are the same statement |
| E3 | `E[L]` is equal, `B1` vs `N0` | TOST on relative difference | **±0.005** | The width tolerance derived in §3.2 |
| E4 | Realised coverage is equal, `A1` vs `N0` | TOST | **±0.002** | The Placement A coverage control required by `docs/GATES.md` G3.3, stated as a test rather than an eyeball |

**"Flat within 1 standard error" is not used anywhere and is not a result**
(`docs/GATES.md` G2.8). Absence of evidence is not evidence of absence, and every null above
carries a margin fixed before the sweep. A TOST that fails is reported as a failure to
establish equivalence at the stated margin, not as evidence of a difference.

### 6.3 Power and the path count

**The path count is set by the smallest difference the paper intends to claim, not the
largest** (`docs/GATES.md` G2.11). The inherited design's failure here is documented: its
stated 5–100× resolution was in fact 0.67×–13.7×, and the `γ = 0.020` comparison — where a
realistic practitioner's setting sits — was unresolved at 60 paths (`audit/NUMBERS.md` §9.2).

**The smallest differences this paper intends to claim, declared now:**

- **Primary endpoint, turnover: 6.0 turns per year** at the primary configuration. This is
  exactly the turnover difference that monetises to the smallest claimed growth difference at
  the primary cost rate: `0.0030 / 0.0005 = 6.0`.
- **Secondary endpoint, net growth: 0.30 points of annual log growth.** Justified two ways:
  it is below the smallest per-device growth cost Ryan reports (0.7 points,
  `audit/NUMBERS.md` row 10), so the design can resolve differences smaller than the published
  anomaly it is trying to explain; and it is an order of magnitude below the inherited headline
  (4.4 points), so the claim does not rest on the largest cell.

**The formula, with its constants fixed here.** For a paired two-sided difference test at
Holm-worst-case `α* = 0.05/6 = 0.008333` and power 0.80:

> `N = ((z_{1−α*/2} + z_{0.80})·sd(d)/Δ)² = (2.6383 + 0.8416)²·(sd(d)/Δ)² = 12.11·(sd(d)/Δ)²`

For a paired TOST at Holm-worst-case one-sided `α* = 0.05/4 = 0.0125` and power 0.80:

> `N = ((z_{1−α*} + z_{0.80})·sd(d)/Δ_eq)² = (2.2414 + 0.8416)²·(sd(d)/Δ_eq)² = 9.505·(sd(d)/Δ_eq)²`

**The one unknown, `sd(d)`, is estimated in a pre-registered pilot and then frozen.** The
pilot runs 20 paths from the disjoint seed block `seed_base_pilot`, under the configuration
frozen by this document, and reports `sd(d_i)` for each endpoint in family D and family E.
`N` is computed from the formulas above as the maximum over all ten tests, written into the
configuration, and the measurement run then uses `seed_base` with the pilot's paths discarded
and its results excluded from every reported table.

**Bounds on `N`.** Minimum **60**, because that is the inherited design's path count
(`audit/NUMBERS.md` row 11) and going below it would make the comparison with the audit's
power analysis unavailable. Maximum **1,000**, from `docs/COMPUTE.md`'s laptop assumption; if
the formula demands more, **the claim is re-scoped rather than `N` grown**, and the re-scoping
is recorded. Note that at `T = 10,080` the paired difference is averaged over 40 years per
path, so `sd(d)` is expected to be small and the minimum of 60 is expected to bind; the pilot
exists to detect the case where it does not.

**Compute.** All five cost levels are derived from one simulation per arm per path (R9), so
the path-run count is `N ×` (number of arm configurations), roughly `N × 60` including the
penalty-strength grid and both interval constructions. At `N = 60` that is 3,600 path-runs of
10,330 steps — comfortably inside `docs/COMPUTE.md`'s laptop budget, with the sensitivity
grids of R2, R4 and R7 multiplying it by a factor of order ten and still fitting.

### 6.4 Multiplicity, stated rather than waived

Holm–Bonferroni within each family, families as declared in §6.2. Sensitivity-grid results
(R2, R3, R4, R7, R15's `η` sweep, R19) are **descriptive** and are reported without inferential
claims; they are not members of either family and no test in them is reported with a p-value
that carries a claim. That boundary is drawn here so that it cannot be redrawn after the
results are seen.

---

## 7. Diagnostics that must be reported per arm

Every one of these appears per arm, per penalty level, in the results JSON, and the starred
ones appear in the paper's appendix.

| # | Diagnostic | Why |
|---|---|---|
| 1 ★ | Realised coverage: per-path mean, per-path sd, pooled | The matching contract's first quantity |
| 2 ★ | `E[L]` and `q̄`, per-path mean and sd | The matching contract's second quantity |
| 3 ★ | **Time at each `α_t` clip bound** | R5. Required by `docs/GATES.md` G2.9 |
| 4 ★ | **Time at the leverage cap**, and time at zero position | R7. Required by G2.9. A capped position is a dead-band the paper is not claiming |
| 5 | Integrator saturation frequency, `Pr(|E_t| ≥ c·h(t))` | Whether the inherited argument's saturation branch is ever exercised |
| 6 | `max_t|E_t|` against `c·h(T)+1`, and the ratio | §5.6. The Placement A forfeit, measured |
| 7 | Band-crossing count, arm `B3` | Proposition 2 bounds `|E_T|` and does not bound crossings, so the count is measured |
| 8 | Zero-movement fraction, `Pr(Δq_t = 0)` | R1's free dead-band from the empirical quantile; and, on L1 and relay arms, the penalty's own dead-band occupancy |
| 9 | Score winsorisation frequency | R18. Whether `b` is doing work |
| 10 | Scorecaster clip frequency | R16. Whether the `[−b/2, b/2]` hypothesis binds |
| 11 | Clip-binding frequency and offset fraction `Φ`, arm `B2` | §5.7 |
| 12 ★ | Both turnover decompositions with their residuals | §5.2. `docs/GATES.md` G2.13 |
| 13 ★ | `Var(q)`, `Var(Δq)` normalised and absolute, `sd(Δ log q)` | §5.3. G2.7 |
| 14 ★ | `ε`, `M̂`, `ε·M̂`, measured against predicted | §5.5 |
| 15 ★ | Gross growth, cost drag, net growth, residual, per cost level | §5.4 |
| 16 ★ | **The match-verification table**, produced and committed before any of rows 12–15 exist | §3.3 |
| 17 | CRN path hashes; `seed_base`; git commit; library versions; wall-clock | `audit/RECONSTRUCTION_SPEC.md` §3 |
| 18 | Infinite-width step fraction, R5 secondary arm | Shows the clip rule is not doing the work |
| 19 | Placebo bit-identity check, arm `P0` | R25 |

**The five tests of `audit/RECONSTRUCTION_SPEC.md` §3 must pass before any number here is
believed**: CRN bit-identity, zero-cost invariance, the cost identity, the degenerate-arm
check (with the penalty inert, all width movement comes from the estimator — assert it), and
leakage (perturb `y_t`, check `q_t` is unchanged). To those five this protocol adds a sixth:
**anchor check** — assert that the penalty's anchor is `q̂_t` and not the deployed `q_t`
(R16), by asserting that the slot sequence is bounded by `max(|q̂_1|, sup|q̂ʳᵃʷ|)` on every
path. That bound is an algebraic consequence of the convex-combination form, so a violation is
a defect, not noise.

---

## 8. [OPERATOR INPUT] items

Two items are left open. Both are recorded with every option fully specified, so that
answering either is a one-line decision and neither blocks implementation.

### OI-1 — L1 or L2? (`docs/OPEN_QUESTIONS.md` Q7)

**The question is recorded and not decided here. Both forms are implemented (R17). The
operator chooses which is primary.**

Considerations, all three of them, stated without resolution:

1. **The L2 form is analytically the cleaner fit to Placement B.** It is a fixed-weight convex
   combination, differentiable in the penalty weight, and it is the form Godahewa et al.
   (*IJF* 2025) publish as model-agnostic post-processing and Binny & Dixit (arXiv:2511.11567,
   Eq. 13) apply to a deployed conformal threshold. Gârleanu & Pedersen (2013) derive linear
   partial adjustment from **quadratic** costs, and that is the correct citation for the L2
   half.
2. **The L1 form is what the title's dead-band language implies.** Proportional costs give
   soft-thresholding and a no-trade region; the correct citations are Constantinides (1986) and
   Davis & Norman (1990), not Gârleanu & Pedersen, whose paper explicitly distinguishes itself
   from strategies "which exhibit periods of no trading" (`audit/REFS_REJECTED.md` §1.1).
3. **A consideration wave 1 added, which the L1 side did not previously have.** Condition (4)
   only lower-bounds `r_t` past its threshold and requires neither continuity nor strict
   monotonicity, so a **relay / dead-band saturator** `r_t(x) = b·sign(x)·1{|x| ≥ c·h(t)}` is
   admissible, Theorem 1 applies to it verbatim, and it contributes **exactly zero movement
   inside its band** — both the gain term and the schedule term vanish there. That places a
   dead-band inside the object the inherited theorem already quantifies over, which is a
   structural argument for the L1 family that did not exist before this session. Its honest
   limit: Proposition 2 bounds `|E_T|` and does not bound the number of band crossings, so the
   crossing count carries no a priori bound and in the worst case is `Θ(T)`. It is a design
   lever with an empirical question attached, not a theorem
   (`research/S2/D1-reduction.json`, `d_deployed_interval.integrator_injected_movement`,
   item 4).

**What the answer changes.** Which of `B1` and `B1τ` is the paper's headline arm, and which of
the two citation chains leads the related-work paragraph. It changes no other choice in this
document; both arms run either way, and the tractability of the lemma route in
`docs/GATES.md` G3.4 depends on it.

### OI-2 — Confirm the regime calibration's numeric transcription (R2)

**The calibration is chosen and is not open. Its transcription is unverified and is a blocking
pre-sweep check.**

- **What is verified.** The bibliographic record: Hardy, M. R. (2001), "A Regime-Switching
  Model of Long-Term Stock Returns", *North American Actuarial Journal* 5(2):41–53,
  doi 10.1080/10920277.2001.10595984 — confirmed against Crossref in this session.
- **What is not verified.** The printed parameter table was not obtained. The values used in
  R2 — `σ₁ = 0.0350`, `σ₂ = 0.0748`, `p₁₂ = 0.0398`, `p₂₁ = 0.3798` — are corroborated
  second-hand and have not been read off the paper.

**Option A (the protocol's default).** Obtain the paper, confirm the four values against the
printed table, record the page and table number in `audit/REFS_VERIFIED.bib` and in the frozen
configuration, and proceed. If a value differs, substitute the printed one, recompute the daily
embedding and the width tolerance of §3.2 from the displayed formulas, and re-freeze.

**Option B.** Substitute a calibration this project can execute and publish: fit a two-state
Gaussian hidden-Markov model by the Hamilton (1989) filter to the SPY daily series over the
G4 development window, record the fitted `(σ_lo, σ_hi, p_lo→hi, p_hi→lo)` in the results JSON,
and cite the **estimator** rather than a published calibration. This is auditable and
reproducible, and it is honest about what it is; it is second choice only because a fit made
by this project is a weaker answer to "where did these constants come from?" than a fit made
by someone else for another purpose.

**Not an option.** Proceeding with unverified numbers presented as a citation.

### Items the register marks OPERATOR that this protocol has fixed

R1, R2, R6 and R7 are marked OPERATOR in `audit/RECONSTRUCTION_SPEC.md`. This protocol assigns
each a value with a justification, and each is flagged for operator override at freeze time.
`docs/OPEN_QUESTIONS.md` Q4 is superseded by the placement taxonomy of §1.1–§1.2 — the penalty
sits in neither of Q4's two branches, and the three placements A, B and C are what the
experiment now varies. Q6's three sub-questions are answered by R6 and R7 as stated.

---

## 9. What this protocol does not settle

1. **OI-1 and OI-2**, as recorded in §8.
2. **Whether the horizon arithmetic closes for the applied arm.** At the G4 development
   window's roughly 1,511 days, a 1-point coverage bound forces about 0.024·`B` of deployed
   movement per step against 0.0036·`B` at the synthetic horizon. The applied arm therefore
   reports the bound rather than claiming it is tight, and any inherited-guarantee sentence in
   the paper must be scoped to the synthetic horizon or restated for the applied one.
3. **Whether the relay arm's band-crossing count is controlled.** Proposition 2 bounds `|E_T|`
   and says nothing about crossings. This protocol measures the count; it does not bound it,
   and the paper may not imply a bound.
4. **Whether Placement B's headline should be `B1` or `B2`.** The protocol fixes `B1` as
   primary because it is the placement the claim describes, and measures `B2`'s offset
   fraction `Φ`. If `Φ` turns out large, the paper's framing of what the penalty acts on
   should be revisited — but that is a finding, and revising the framing after seeing `Φ`
   would need to be recorded as such.
5. **Whether the effect survives on real data.** Everything here is synthetic. The applied arm
   is G4's business and this protocol does not pre-empt it.
6. **The name of the measured path functional.** `docs/GATES.md` G2.14 requires a name that
   collides with none of the taken ones — `Σ|Δq|` is already published as Zanotti's MQC/SMQC,
   and *smoothed conformal*, *stable conformal*, *smoothing-based conformal* and *interval
   stability* are all taken. This document uses the neutral phrase **deployed width path
   variation** and coins nothing; the naming obligation is owned elsewhere.
7. **Whether R1's contribution survives the prior art.** Not this document's business; see
   `docs/FRAMING.md` §8b.
8. **The bibliography entry for Hardy (2001)**, which is not yet in `audit/REFS_VERIFIED.bib`.
   Adding it is wave 3's, not this document's — this file writes nothing outside `docs/`.
9. **Any gate.** G2, G3 and G4 remain as `docs/GATES.md` records them. This protocol is the
   evidence for G2.1 and G2.12 and nothing more. **No gate is recorded as signed here, and no
   automated session may record one.**
