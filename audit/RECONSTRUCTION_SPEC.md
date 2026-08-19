# Reconstruction specification for the C1 simulator

**Status: the simulator named in the planning document does not exist (see
`audit/REPRO_C1.md`). No simulator was written for this audit.** This document is the
specification a rebuild would need, and — more importantly — the register of every
choice the planning document leaves open. Several of those choices change the answer.

A warning that governs this whole document. Rebuilding a simulator against a table you
have already read is a fitting exercise, not a reproduction. If the free parameters
below are tuned until the output matches the C1 table, the resulting agreement carries
no evidential weight whatsoever, and a reviewer who asks "how were these constants
chosen?" will get an answer that destroys the paper. **The free choices must be fixed
and written down before the sweep is run**, and the frozen specification committed with
a timestamp. That is the purpose of gate G2.

---

## 1. What the plan actually determines

These are stated explicitly and are not in dispute.

| Element | Specified value |
|---|---|
| Update rule | `α_{t+1} = α_t + γ(α − err_t)`, the Gibbs–Candès ACI recursion |
| Interval | `q_t = ŝ_t · z(α_t)` — a scale estimate times a level-dependent multiplier |
| Nominal miscoverage `α` | 0.10 (coverage target 0.90) |
| γ grid | {0.000, 0.005, 0.020, 0.050, 0.150, 0.400} |
| Volatility process | regime-switching |
| Decision map | `π_t = f(q_t)`, a fractional-Kelly position driven by the interval half-width |
| Cost | proportional, applied to position changes |
| Cost grid | {0, 5, 15} bps |
| Paths | 60 |
| Pairing | common random numbers across γ arms |
| Reported quantities | coverage, net annual log growth, paired difference with SE, annual turnover |

Everything below is *not* determined.

---

## 2. The free-choice register

Each entry gives what is missing, whether it can change the sign or the magnitude of
the C1 effect, and a recommended default. **Recommendations are recommendations. Items
marked OPERATOR are decisions the audit is not authorised to make; they are mirrored in
`docs/OPEN_QUESTIONS.md`.**

### R1. Is the interval conformal at all? — OPERATOR, highest severity

The plan writes the interval as `q_t = ŝ_t · z(α_t)`. If `z(·)` is the Gaussian
quantile function, this is **not split conformal prediction**. It is a parametric
Gaussian interval whose nominal level is steered by the ACI recursion. Adaptive
conformal inference as published sets the interval from the empirical quantile of
trailing nonconformity scores, `Q̂_t(1 − α_t)`, with no distributional assumption.

Why it matters, beyond nomenclature:

- **Smoothness.** `z(α_t)` is smooth and unbounded in `α_t`; `Q̂_t(1 − α_t)` is a step
  function of `α_t` with jumps at order statistics of the calibration window. The
  entire mechanism of this paper is how `α_t` jitter propagates into `q_t` jitter and
  thence into position jitter. The two constructions transmit jitter differently — the
  empirical quantile is *quantised*, so small `α_t` movements often produce **zero**
  `q_t` movement. That is a dead-band arising for free from the estimator, and it may
  absorb part of the effect the paper attributes to γ.
- **Generality.** C1 is stated for "any online conformal method". Demonstrating it on a
  Gaussian proxy does not establish it for the empirical-quantile methods the paper
  names as baselines (ACI, DtACI, conformal PID, SAOCP).
- **Reviewer exposure.** The programme committee includes researchers who work
  directly on conformal prediction. A parametric interval presented as conformal will
  be caught.

**Recommendation:** implement both. Make the empirical-quantile ACI the primary
specification, since it is what the literature means by ACI and what the baselines
are; keep the Gaussian version as a secondary arm and report both. If the effect
survives only in the Gaussian version, that is a finding about the paper, not a
detail of the implementation.

### R2. Regime-switching process — OPERATOR

Unspecified: number of states, the volatility level in each, the transition
mechanism, whether the drift also switches, and the expected regime durations.

Consequential, because the whole point of an adaptive method is that it earns its
keep at regime boundaries. Regimes that are too persistent make γ irrelevant (nothing
to adapt to, so slow always wins and the result is trivial); regimes that switch too
often make even the fastest γ unable to track, and the ranking can invert.

Minimum that must be pinned down:

- number of states `K` (2 is the natural default)
- per-state annualised volatility, e.g. `σ_lo`, `σ_hi`, and their ratio — the ratio,
  not the levels, is what drives the tracking problem
- transition matrix, or equivalently expected dwell time in each state
- whether `μ` is state-dependent (**recommendation: no** — a state-dependent drift
  confounds the mechanism with a market-timing effect and makes the Kelly position
  respond to something other than the interval)
- whether the state is ever observable to the predictor (**recommendation: never**)

**Recommendation:** 2-state Markov chain, unobserved, drift constant across states,
volatility ratio and dwell times chosen from a published regime-switching calibration
and cited, not invented. Report a sensitivity grid over the volatility ratio and the
dwell times — the paper's credibility depends far more on the effect surviving that
grid than on any single cell of it.

### R3. Return distribution within a regime

Unspecified: Gaussian or heavy-tailed; i.i.d. or autocorrelated; the drift `μ`.

`μ` is load-bearing: the reported growth of +1.34 %/yr at γ = 0.005 is a joint
consequence of `μ`, the Kelly fraction and the leverage cap, and none of the three is
stated. Any of infinitely many `(μ, λ, cap)` triples reproduces +0.0134.

**Recommendation:** Gaussian i.i.d. within regime for the primary specification, with
a Student-t robustness arm. State `μ` explicitly and justify it. Note that heavy tails
interact with R1: a Gaussian `z(α_t)` under t-distributed returns will systematically
under-cover, which pushes `α_t` down and changes the jitter regime.

### R4. The scale estimator `ŝ_t`

Unspecified: estimator family and its window.

This is the **most under-appreciated confound in the design**. `ŝ_t` is itself an
adaptive object with its own adaptation rate. `q_t = ŝ_t · z(α_t)` jitters because
`α_t` jitters *and* because `ŝ_t` jitters. The plan's γ = 0 arm has annual turnover
3.2, not zero — that residual turnover is entirely `ŝ_t` movement. So the experiment
as described does not isolate γ; it measures γ's marginal contribution on top of a
fixed, unstated amount of scale-estimator churn. If the window is short, `ŝ_t` churn
dominates and the γ effect is compressed; if long, the estimator cannot track regimes
and the whole setup is unrealistic.

**Recommendation:** fixed-length trailing rolling standard deviation, window stated,
held identical across every γ arm and every cost level. Avoid EWMA in the primary
specification — its half-life is a second adaptation rate confounded with γ, which is
precisely the variable under study. Then run a window sweep and report the γ effect as
a function of it; "the effect exists at every scale-window we tried" is a much stronger
claim than "the effect exists at our window".

### R5. Clipping of `α_t` — high severity, and it dominates the headline arm

ACI's `α_t` is a random walk that leaves `[0, 1]` unless constrained. The published
treatment lets `α_t ≤ 0` produce an infinite interval. The plan says nothing.

Work through the headline arm. With γ = 0.400 and target α = 0.10, each step moves
`α_t` by **+0.04 when covered** and **−0.36 when miscovered**. Starting at 0.10, a
single miscoverage drives `α_t` negative. The γ = 0.400 arm therefore spends a large
fraction of its time pinned at whatever lower bound the implementation imposes,
oscillating between that bound and a few steps above it. Its interval width — and
hence its position — is then governed mainly by the **clipping rule**, not by the ACI
dynamics.

That matters because γ = 0.400 supplies the paper's headline numbers: the 4.4-point
swing, the 13.7 standard errors, the turnover of 31.0. If those are artefacts of an
undocumented clip, the headline is an artefact.

**Recommendation:** state the rule explicitly; report the fraction of time `α_t` sits
at each bound for every γ arm — this diagnostic must appear in the paper's appendix;
and check that the C1 effect survives on a γ grid whose top value does not saturate.
A γ grid whose extreme arm is degenerate is not a sweep.

### R6. The position map `f(q)` and the Kelly fraction — OPERATOR

Unspecified: the functional form, the Kelly fraction `λ`, and whether the drift used
in the position is the true `μ` or an estimate.

The natural reading is: invert the interval for a volatility estimate, then apply
fractional Kelly. `σ̂_t = q_t / z_{1−α/2}` with the **nominal** `α`, giving
`π_t = λ · μ̂ / σ̂_t²`. Note the choice of which `z` to divide by: using `z(α_t)` would
cancel the ACI adjustment out of the position entirely and destroy the mechanism, so
it must be the nominal quantile. The plan does not say this, and it is the difference
between an experiment that works and one that measures nothing.

Sub-choices, all free:
- `λ` (full Kelly, half, quarter) — scales both growth and turnover, so it sets the
  cost sensitivity
- whether `μ̂` is the true drift (**recommended** — isolates interval jitter as the
  only moving part) or estimated (adds a second noise channel and reopens exactly the
  MacLean–Thorp–Ziemba estimation-error explanation the plan claims to have ruled out)
- whether `π_t` may go short, and whether it is a fraction of wealth or of a fixed
  notional

**Recommendation:** `π_t = λ · μ / (q_t / z_{1−α/2})²` with true `μ`, long-only,
fraction of wealth, `λ` stated. Any use of an estimated `μ̂` must be reported, because
it directly weakens the falsified-variance-hypothesis claim.

### R7. Leverage cap — OPERATOR

Unspecified. As `σ̂_t → 0` the Kelly position diverges. Ryan's configuration uses
leverage caps (established fact V2), and the applied arm is a replication of that
configuration, so the simulation should not be capless while the replication is capped.

A cap also **truncates the jitter** the paper is measuring: a position pinned at the
cap does not move when `q_t` moves, which is itself a dead-band. If the low-γ arms sit
at the cap more often than the high-γ arms, the cap is silently doing part of the work
the paper attributes to slow adaptation.

**Recommendation:** state the cap; report per-arm time-at-cap alongside time-at-α-clip;
verify the effect survives capless and at two cap levels.

### R8. Horizon, annualisation and the turnover metric

Unspecified: steps per path `T`, trading days per year, and the definition of
"annual turnover".

Turnover of 3.2 to 31.0 is consistent with one-way annual turnover — `Σ_t |π_t −
π_{t−1}|` over a year — but the two-way convention would halve every figure and the
cost model must agree with whichever is used. `T` matters for the standard errors: 60
paths of one year and 60 paths of ten years give very different SEs on the same
per-path effect.

**Recommendation:** define turnover as `Σ_t |π_t − π_{t−1}|` per annum, one-way;
state `T` and the annualisation factor; state whether growth is annualised by dividing
the total log return by the number of years or by compounding.

### R9. Cost application

Unspecified: whether the proportional cost is subtracted from the log return or
applied to the wealth multiplier, and whether it is charged on `|Δπ|` as a fraction of
wealth.

At 15 bps and turnover 31.0, the cost drag is `0.0015 × 31.0 = 0.0465` — 4.65 points
per year. The γ = 0.400 arm's growth deficit versus γ = 0.005 is 4.37 points, and the
γ = 0.005 arm's own drag is `0.0015 × 3.4 = 0.51` points. The difference in drag is
`0.0015 × (31.0 − 3.4) = 4.14` points, against an observed 4.37-point difference.

**That near-agreement is the strongest internal evidence the table is real, and it is
also a warning.** It says the growth gap is almost entirely explained by the cost
identity `Δgrowth ≈ c × Δturnover`, with only ~0.23 points left over from any other
channel. A reviewer will make this calculation in thirty seconds and conclude the C1
result is arithmetic rather than a finding. The paper must confront that directly: the
contribution cannot be "costs times turnover is a cost" — it must be that **coverage
does not constrain turnover**, so the turnover term is invisible to the tuning
criterion. The interesting quantity is the turnover column, not the growth column.

**Recommendation:** report the decomposition explicitly — gross growth, cost drag, and
residual — for every arm, and lead with the coverage-versus-turnover dissociation
rather than the growth swing.

### R10. Common random numbers

Unspecified: RNG family, seed policy, and what exactly is held common.

To be paired, the return path *and* the regime path must be generated once per path
index and reused byte-identically across every γ arm and every cost level. Any RNG
draw inside the γ loop breaks pairing and inflates the SEs.

**Recommendation:** `numpy.random.Generator(PCG64(seed_base + path_index))`; generate
and cache the full `(regime, return)` path before entering the γ loop; assert
bit-identity of the cached paths across arms in a test; record `seed_base` in every
results JSON.

### R11. Burn-in and measurement window

Unspecified. `ŝ_t` needs at least a full window before it is defined, and `α_t` needs
time to leave its initial value. Whether coverage and growth are measured over the
whole path or post-burn-in changes the γ = 0 coverage figure (0.8926) materially.

**Recommendation:** discard the first `max(window, 250)` steps; state it; report
coverage both ways once, to show the choice is not doing work.

### R12. `Var(Δq)` — the falsified-variance-hypothesis statistic

Unspecified: the 330× figure has no definition anywhere in the plan. Variance of
`q_t − q_{t−1}` pooled over `t` and paths? Per path then averaged? In absolute units,
or normalised by mean `q`? In absolute units the statistic is not scale-free and the
ratio across γ arms is partly an artefact of the arms having different mean widths.

**Recommendation:** report `Var(Δq / q̄)` — normalised — as primary, absolute as
secondary, and state which one the 330× refers to when it is recomputed.

### R13. Coverage and standard-error conventions

Unspecified: coverage pooled over all `(path, t)` or averaged over per-path coverage;
paired SE computed as `sd(per-path difference)/√60`.

**Recommendation:** per-path then averaged, with the per-path standard deviation
reported; paired SE as `sd(d_i)/√60`; state that no multiplicity correction is applied
across the five comparisons, or apply one.

---

## 3. Implementation contract for the rebuild

The rebuild should be a single module in `src/` with no hidden state and the following
externally visible contract.

**Inputs.** A single frozen configuration object carrying: `alpha`, `gamma_grid`,
`cost_grid_bps`, `n_paths`, `T`, `trading_days_per_year`, `burn_in`, `seed_base`,
regime parameters (R2), return parameters (R3), scale-estimator family and window
(R4), `alpha_clip` (R5), position-map parameters (R6), `leverage_cap` (R7), turnover
convention (R8), cost convention (R9), interval construction — empirical or Gaussian
(R1).

**Outputs.** One JSON per run in `results/`, never overwritten, carrying:

- the complete configuration, verbatim
- the git commit hash of the code that produced it
- wall-clock runtime
- library versions
- **per-path, per-arm raw quantities**, not only aggregates: coverage, gross growth,
  cost drag, net growth, turnover, `Var(Δq)` normalised and absolute, fraction of time
  at each `α_t` clip bound, fraction of time at the leverage cap
- the aggregated table as a derived field, so the aggregation can be recomputed
  from the raw record without re-running

The absence of exactly this record is why the current audit has nothing to check. Its
presence is what makes gate G2 checkable.

**Tests that must exist before any number is believed.**

1. CRN integrity: cached paths are bit-identical across γ arms and cost arms.
2. Zero-cost invariance: at 0 bps, net growth equals gross growth exactly.
3. Cost identity: `gross − net` equals `cost_rate × turnover` to floating-point
   tolerance, for every arm. This is the check that makes R9 auditable.
4. γ = 0 degeneracy: with γ = 0 the sequence `α_t` is constant, so all interval
   movement comes from `ŝ_t`. Assert it.
5. Leakage: the interval at time `t` is a function of information up to `t−1` only.
   Assert by perturbing `y_t` and checking `q_t` is unchanged.

---

## 4. What a successful reconstruction must reproduce

Success criteria, to be written into the frozen specification **before** the run:

| Target | Plan value | Tolerance for "reproduced" |
|---|---|---|
| Coverage, every γ ≥ 0.005, 15 bps | 0.8993–0.9000 | within 0.002 of 0.90 |
| Coverage, γ = 0 | 0.8926 | materially below the γ ≥ 0.005 arms |
| Growth swing, γ = 0.005 → 0.400 | 4.4 points | 3.5–5.5 points |
| Turnover ratio, γ = 0.400 / γ = 0.000 | 9.7× | 6×–15× |
| Significance of the top comparison | 13.7 SE | > 8 SE |
| 0 bps: all paired diffs within 1 SE | asserted, untabulated | must hold |
| Cost-rate monotonicity | asserted over 3 levels | must hold over ≥ 5 levels |
| `Var(Δq)` rise across γ at 0 bps | 330× | order of magnitude, ≥ 50× |

If the rebuild misses these under a specification frozen in advance, the honest
conclusion is that the C1 table is not reproducible and the paper's empirical claim
must be restated from whatever the rebuild does show. That outcome is survivable. What
is not survivable is adjusting R2–R7 until the table appears.

---

## 5. Priority

`docs/OUTSTANDING.md` records this as the highest-priority blocking item in the
project. Nothing downstream — the dead-band arm of C2, the Ryan-configuration
replication, the paper — can be started until the C1 simulator exists, is frozen, and
emits the results record described in §3.
