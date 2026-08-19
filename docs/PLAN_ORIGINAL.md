# F7 — Coverage Is Turnover-Blind: Why Adaptive Conformal Is Mis-Tuned for Costly Decisions

**One sentence:** The adaptation rate of every online conformal method is **invisible to coverage** but
directly controls interval jitter, which drives position turnover and cost drag — so tuning by coverage
is systematically wrong for any decision that pays to trade, and this explains a published, unexplained
empirical anomaly with a quantitative match.

| | |
|---|---|
| **Target venue** | NeurIPS 2026 **ML×OR** (Atlanta) — "distributional robustness", "sequential and adaptive decision-making", finance named |
| **Deadline / format** | **Aug 31 2026 AoE**, 4pp main body, **non-anonymous**, journal fast-track |
| **Backup venue** | TS-LIMITS (Paris, **Sep 5**, 4–7pp) |
| **Prior-art verdict** | **NARROW — positioned on a gap a prior sweep identified independently.** See §Prior art. |
| **Compute** | CPU-only. The core result already runs in ~90 seconds. |
| **Data** | Simulation for the mechanism; free daily series for the applied arm |
| **Est. effort** | 2 weeks — **the central experiment is already done** |

---

## The anomaly this explains

**Conformal Kelly (arXiv:2608.01494, Aug 2026)** reports, and cannot explain, that
*"every tweak that adapts the interval faster to market conditions costs 0.7 to 5.3 points of annual
growth"* — slow unweighted per-asset rolling quantiles beat ACI, DtACI, and conformal PID. This runs
directly against the adaptive-conformal literature's premise that faster adaptation is better under
non-stationarity.

Nobody has explained it. **I have, and the explanation is mechanical rather than empirical.**

## The result (already computed — `scratchpad/confloor5.py`)

ACI-style update with step size γ on a regime-switching volatility path; interval half-width maps to a
fractional-Kelly position; 60 paths with **common random numbers** so γ comparisons are paired.

At 15 bps proportional cost:

| γ | coverage | net annual log growth | paired diff vs γ=0.005 | annual turnover |
|---|---|---|---|---|
| 0.000 | 0.8926 | +0.0136 | +0.0002 ± 0.0003 | 3.2 |
| 0.005 | 0.8993 | +0.0134 | reference | 3.4 |
| 0.020 | 0.8998 | +0.0123 | −0.0010 ± 0.0004 | 4.4 |
| 0.050 | 0.8999 | +0.0090 | −0.0043 ± 0.0008 | 6.9 |
| 0.150 | 0.8999 | −0.0050 | −0.0184 ± 0.0019 | 15.8 |
| 0.400 | 0.9000 | −0.0303 | **−0.0437 ± 0.0032** | 31.0 |

**Coverage is pinned at the 0.90 target for every γ ≥ 0.005** while net growth swings 4.4 points —
13.7 standard errors. At **0 bps the effect vanishes entirely** (all diffs within 1 SE); at 5 bps it is
intermediate. The effect is monotone in the cost rate, so the channel is unambiguously transaction cost.

**Magnitude match to the published anomaly:** Conformal Kelly reports 0.7–5.3 points; this simulation
gives 1.0–4.4 points across the γ range. An independently derived quantitative match to someone else's
unexplained empirical finding is the strongest evidence this file contains.

### A falsified hypothesis, recorded honestly

My *first* explanation was that log-utility is variance-averse and coverage is variance-blind, so
quantile jitter would hurt growth directly. **This is false.** With zero costs, Var(Δq) rises **330×**
across the γ sweep while net growth stays flat within 1 SE. The variance channel does not transmit.
Only the turnover channel does. Keep this in the paper — it rules out the competing explanation and
pre-empts a reviewer proposing it.

## Primary claim (C1)

For any online conformal method, the adaptation rate is **first-order in downstream turnover and
zeroth-order in coverage**: coverage is achieved over a wide range of adaptation rates whose realised
decision cost differs by several percentage points of annual growth. Therefore **no coverage-based
criterion — marginal, conditional, or adaptive — can select the adaptation rate for a decision that pays
for turnover.** Formalise the turnover-vs-tracking-error frontier and show the coverage-optimal point
sits at the wrong end of it.

## Secondary claim (C2) — the method

**A turnover-aware conformal update.** Add a cost-aware **dead-band / hysteresis** to the ACI update:
move the interval only when accumulated coverage evidence exceeds the cost of moving the position it
implies. Concretely, penalise |Δq_t| by the induced |Δposition| × cost, giving an update that is
optimally sluggish rather than heuristically slow.

Primary claim of C2: this dominates *both* fast ACI (which churns) and fixed-α slow quantiles (which
under-adapt in genuine regime shifts) at matched coverage — recovering adaptivity where it is worth
paying for and suppressing it where it is not. **Conformal Kelly found slow beats fast; the correct
answer is neither, and the dead-band is why.**

## Method

1. Standard ACI: α_{t+1} = α_t + γ(α − err_t); interval q_t = ŝ_t·z(α_t).
2. Decision map: position π_t = f(q_t) (fractional Kelly, or any turnover-bearing map).
3. **Turnover-aware update:** choose Δα_t to minimise
   `coverage-deviation-penalty + λ·cost·|f(q_{t+1}) − f(q_t)|`,
   yielding a soft-threshold/dead-band update in closed form for a proportional cost (the L1 penalty
   gives shrinkage-to-no-trade, exactly as in the Gârleanu–Pedersen dynamic-trading solution).
4. Prove coverage is retained: the dead-band delays but does not prevent adaptation, so long-run
   coverage is preserved while turnover is bounded — this is the theorem to state.

## Experimental protocol

- **Data:** the simulation above (mechanism, with ground truth) **plus** free daily equity/ETF series
  for the applied arm.
- **Baselines (must include the trivial one):** (i) **fixed-α split conformal, never adapted** — the
  degenerate baseline that Conformal Kelly found hard to beat; (ii) ACI (Gibbs–Candès); (iii) DtACI;
  (iv) conformal PID; (v) SAOCP; (vi) **Conformal Decision Theory** (Lekeufack et al., ICRA 2024) —
  the decision-loss incumbent; (vii) turnover-aware (yours).
- **Metric:** net growth **and** coverage **and** turnover, jointly. Reporting coverage alone is the
  error the paper is about.
- **Statistics:** common random numbers across methods (as above — it cut the SE by ~5×); ≥60 paths;
  report paired differences with SEs.

## S4 preflight — already largely run

1. **Degenerate floor:** fixed-α no-adaptation. **Already shown competitive** (γ=0 is statistically
   indistinguishable from the best arm at every cost level) — the paper must beat it, not ACI.
2. **MDE:** paired CRN gives SE ≈ 0.0003–0.003 on growth differences against effects of 0.004–0.044.
   The design resolves its own question by 5–100×. **Confirmed.**
3. **Leakage:** the interval must use only trailing data.
4. **STOP condition:** if the dead-band update does not beat *both* fixed-α and ACI at matched coverage
   on real data, report the C1 dissociation alone — it stands on its own as an ML×OR contribution.

## What kills this paper

**"This is just transaction costs, obviously."** The response is that it is obvious only in hindsight
and the field demonstrably did not account for it: the entire adaptive-conformal line optimises coverage
or coverage-regret, and Conformal Kelly's authors reported the consequence as a *surprise*. The paper's
value is the mechanism plus the corrected update, and the falsified variance hypothesis shows the
mechanism was not a given.

**"Conformal Decision Theory already updates on decision loss."** True and it must be the headline
baseline — but a prior sweep established that CDT's trading experiment is explicitly **"no trading
cost" on synthetic GBM**, so the turnover-penalised case is exactly its stated gap. Also note CDT's
guarantee is risk control (empirical average loss ≤ ε), not a turnover-bounded one.

**"Path-dependence breaks the regret analysis."** Real and must be handled: the turnover-penalised loss
depends on the incumbent position, so per-round loss is not a fixed function of α_t. State the
bounded-memory/lag assumption explicitly — this is a genuine quantifier-order trap, not a formality.

## Prior art you must cite

Vovk, Gammerman & Shafer (2005); **Gibbs & Candès (ACI 2021; DtACI 2022)**; **Angelopoulos, Candès &
Tibshirani, conformal PID (2024)**; Bhatnagar et al., SAOCP (ICML 2023); Bates, Angelopoulos et al.,
conformal risk control; **Lekeufack, Angelopoulos, Bajcsy, Jordan & Malik, Conformal Decision Theory
(ICRA 2024, arXiv:2310.05921)**; **Ryan, Conformal Kelly (arXiv:2608.01494)** — the anomaly;
Schmitt, RWCP (arXiv:2602.03903); **Gârleanu & Pedersen (2013)** — turnover-penalised dynamic trading,
the source of the dead-band form;
**Zaffran, Féron, Goude, Josse & Dieuleveut (ICML 2022, arXiv:2202.07282)** — theoretically analyse the
impact of the ACI **learning rate on efficiency**; this is the closest existing analysis of γ and must be
engaged directly;
**Angelopoulos, Barber & Bates (ICML 2024, arXiv:2402.01139)** — show *decaying/slower* step sizes give
per-timepoint coverage when the distribution is stable, i.e. an existing partial account of
slow-beats-fast that your cost mechanism must be distinguished from;
**Vaze (arXiv:2607.26577)** and **Srinivas (SODA 2026, arXiv:2507.02496)** — the coverage/efficiency
minimax frontier; cite to make clear you are *not* claiming a floor;
**Ramalingam, Kiyani & Roth (ICML 2025, arXiv:2502.10947)** — the regret↔coverage correspondence holds
i.i.d. but fails adversarially (the tight version needs *swap* regret); relevant if you attempt any
regret-style argument;
**MacLean, Thorp & Ziemba** — Kelly under estimation error; cite as the mechanism you **tested and
ruled out**;
Elmachtoub & Grigas, SPO (*Mgmt Sci* 2022); arXiv:2605.01176
(decision-induced turnover in SPO); Zinkevich (2003); arXiv:2502.10947 (no-regret ↔ online conformal);
Kelly (1956); Rockafellar & Uryasev (2000).

## Dedicated novelty sweep — result, and one place where my data overrules it

A sweep run specifically on this territory (Semantic Scholar forward-citation screen of Gibbs–Candès ACI,
100 titles; arXiv HTML full-text theorem extraction) returned two findings.

**Good news — it independently identified this file's exact square as unoccupied:**
> *"nothing exists on how variance in adaptive conformal interval widths propagates into downstream
> decision loss (arXiv returns 0 for `conformal`×`downstream decision`×`variance`, 0 for
> `prediction interval`×`Kelly`). That is a decision-theoretic claim — coverage-based theory is blind to
> a Jensen penalty."*

**Hard constraint — do NOT frame this as an impossibility or coverage floor.** That is occupied by
**Vaze, arXiv:2607.26577 (29 Jul 2026)**, whose Theorem 7 gives a matching minimax lower bound
Ω(T^{2/3}·V_T^{1/3}) on cumulative miscoverage over all online algorithms, and by **Srinivas (SODA 2026,
arXiv:2507.02496)** on the joint coverage–efficiency Pareto frontier. Any "there is a floor nobody
stated" framing is dead on arrival. **F7's claim is decision-theoretic, not information-theoretic** —
keep it that way.

**Where the sweep is wrong, and my simulation is the evidence.** It argues the anomaly is already
explained, partly via MacLean–Thorp–Ziemba: noisy scale estimates asymmetrically punish Kelly log-growth,
so noisier widths → overbetting → growth loss. **My experiment falsifies that channel.** At 0 bps,
Var(Δq) rises 330× across the γ sweep and net growth stays flat within 1 SE; the effect appears only
when costs are switched on and scales monotonically with the cost rate. So the mechanism is turnover,
not Kelly estimation noise. **Report this explicitly** — it is the difference between an over-determined
observation and an identified mechanism, and it is exactly the objection a reviewer will raise.

## ⚠️ Verify before committing

This session's WebSearch budget was exhausted, so the specific pairing "online conformal adaptation rate
× transaction costs" has **not** had a dedicated sweep. Run first: `conformal prediction transaction
costs turnover`, `adaptive conformal step size tuning decision cost`, `online conformal hysteresis
dead-band`, plus forward citations of ACI (Gibbs–Candès) filtered for cost/turnover/trading. Also sweep
SSRN, which this session could not reach.

## Day-1 starting point

`scratchpad/confloor5.py` already produces the C1 table. Add the dead-band arm to it — it is ~15 lines —
and check whether it beats both γ=0 and γ=0.05 at 15 bps. That single comparison decides C2.
