# Numeric-claim trace for `docs/PLAN_ORIGINAL.md`

Every number that appears anywhere in the planning document, one row each.

**Column definitions.**

- **source** — one of exactly three values.
  - `reproduced-from-code` — the number was produced by running code in this
    repository during this audit.
  - `present-in-plan-only` — the number is displayed in the plan's own table, is
    arithmetically derivable from that table, or is corroborated by an external record
    that was verified outside this repository. It has a traceable basis, but not one
    this repository can execute.
  - `orphan` — the number is asserted in prose, is displayed in no table, is not
    derivable from any displayed table, and has no external corroboration. Nothing in
    the document or the repository supports it.
- **load-bearing** — would the paper's argument survive if this number were false or
  materially different?

**The `reproduced-from-code` column is empty for every row in this document.** No
simulator exists (`audit/REPRO_C1.md`), so nothing could be reproduced. That is the
governing fact of this trace and it is not a per-row observation.

---

## 1. Header and metadata

| # | number | claim it supports | source | load-bearing | note |
|---|---|---|---|---|---|
| 1 | 2026 (NeurIPS) | target venue year | present-in-plan-only | no | Externally verified. |
| 2 | Aug 31 2026 AoE | submission deadline | present-in-plan-only | **yes** | Externally verified. Fixes the entire schedule. |
| 3 | 4pp | main-body page limit at ML×OR | present-in-plan-only | **yes** | Externally verified. Determines what fits; see `docs/VENUE.md`. |
| 4 | Sep 5 | TS-LIMITS backup deadline | present-in-plan-only | no | Unverified in the plan; checked in `docs/VENUE.md`. |
| 5 | 4–7pp | TS-LIMITS page range | present-in-plan-only | no | Unverified in the plan; checked in `docs/VENUE.md`. |
| 6 | ~90 seconds | "the core result already runs in ~90 seconds" | **orphan** | no | No code, no timing record, no machine specified. Plausible for the described computation but wholly unsupported. |
| 7 | 2 weeks | estimated remaining effort | **orphan** | **yes** | Directly contradicted by `audit/REPRO_C1.md`: the estimate is conditioned on a simulator that does not exist. Drives every scheduling decision. |

## 2. The published anomaly (Conformal Kelly)

| # | number | claim it supports | source | load-bearing | note |
|---|---|---|---|---|---|
| 8 | arXiv:2608.01494 | identifier of the anomaly paper | present-in-plan-only | **yes** | Externally verified: the work exists. |
| 9 | Aug 2026 | date of that preprint | present-in-plan-only | no | Externally verified: submitted 2 Aug 2026. |
| 10 | 0.7 to 5.3 points | the growth cost of faster adaptation, which the plan calls unexplained | present-in-plan-only | **yes** | Externally verified against the preprint's abstract. This is the empirical anomaly the paper exists to explain. Note Ryan does offer an explanation for it — hedged, measured for one device, and not a turnover account; see `docs/FRAMING.md`. |

## 3. The C1 table — configuration

| # | number | claim it supports | source | load-bearing | note |
|---|---|---|---|---|---|
| 11 | 60 | number of simulated paths | present-in-plan-only | **yes** | Sets every standard error in the table. |
| 12 | 15 bps | proportional cost rate of the displayed table | present-in-plan-only | **yes** | The only cost level actually tabulated. |
| 13 | 0.90 | nominal coverage target | present-in-plan-only | **yes** | Note this differs from Ryan's 75 % interval — see §7 and `audit/CLAIMS.md` C-c. |
| 14–19 | 0.000, 0.005, 0.020, 0.050, 0.150, 0.400 | the γ grid | present-in-plan-only | **yes** | The independent variable. |

## 4. The C1 table — measured cells

All 23 cells. None emitted by any code available here; all internally consistent with
each other (checks in the note column and in §8).

| # | number | claim it supports | source | load-bearing | note |
|---|---|---|---|---|---|
| 20 | 0.8926 | coverage at γ=0 | present-in-plan-only | **yes** | The only arm that misses the target; supports "γ=0 under-covers". |
| 21 | 0.8993 | coverage at γ=0.005 | present-in-plan-only | **yes** | |
| 22 | 0.8998 | coverage at γ=0.020 | present-in-plan-only | **yes** | |
| 23 | 0.8999 | coverage at γ=0.050 | present-in-plan-only | **yes** | |
| 24 | 0.8999 | coverage at γ=0.150 | present-in-plan-only | **yes** | |
| 25 | 0.9000 | coverage at γ=0.400 | present-in-plan-only | **yes** | Rows 21–25 are the whole of C1's "coverage is blind" evidence. |
| 26 | +0.0136 | net annual log growth, γ=0 | present-in-plan-only | **yes** | |
| 27 | +0.0134 | net annual log growth, γ=0.005 (reference) | present-in-plan-only | **yes** | |
| 28 | +0.0123 | net annual log growth, γ=0.020 | present-in-plan-only | **yes** | |
| 29 | +0.0090 | net annual log growth, γ=0.050 | present-in-plan-only | **yes** | |
| 30 | −0.0050 | net annual log growth, γ=0.150 | present-in-plan-only | **yes** | Sign change: the arm turns loss-making. |
| 31 | −0.0303 | net annual log growth, γ=0.400 | present-in-plan-only | **yes** | |
| 32 | +0.0002 | paired diff, γ=0 vs γ=0.005 | present-in-plan-only | **yes** | Exact: 0.0136 − 0.0134. |
| 33 | −0.0010 | paired diff, γ=0.020 | present-in-plan-only | no | 0.0123 − 0.0134 = −0.0011; consistent once rounding of the unrounded values is allowed (the admissible band is non-empty). |
| 34 | −0.0043 | paired diff, γ=0.050 | present-in-plan-only | no | 0.0090 − 0.0134 = −0.0044; same rounding argument. |
| 35 | −0.0184 | paired diff, γ=0.150 | present-in-plan-only | **yes** | Exact. |
| 36 | −0.0437 | paired diff, γ=0.400 | present-in-plan-only | **yes** | Exact. The headline effect. |
| 37 | ±0.0003 | SE of the γ=0 paired diff | present-in-plan-only | **yes** | Supports "γ=0 is indistinguishable from the best arm". |
| 38 | ±0.0004 | SE, γ=0.020 | present-in-plan-only | no | |
| 39 | ±0.0008 | SE, γ=0.050 | present-in-plan-only | no | |
| 40 | ±0.0019 | SE, γ=0.150 | present-in-plan-only | no | |
| 41 | ±0.0032 | SE, γ=0.400 | present-in-plan-only | **yes** | Denominator of the "13.7 standard errors" claim. |
| 42 | 3.2 | annual turnover, γ=0 | present-in-plan-only | **yes** | Non-zero at γ=0: all of it is scale-estimator churn, not ACI. See `audit/RECONSTRUCTION_SPEC.md` R4. |
| 43 | 3.4 | annual turnover, γ=0.005 | present-in-plan-only | **yes** | |
| 44 | 4.4 | annual turnover, γ=0.020 | present-in-plan-only | **yes** | |
| 45 | 6.9 | annual turnover, γ=0.050 | present-in-plan-only | **yes** | |
| 46 | 15.8 | annual turnover, γ=0.150 | present-in-plan-only | **yes** | |
| 47 | 31.0 | annual turnover, γ=0.400 | present-in-plan-only | **yes** | The turnover column is the paper's real result; see §8. |

## 5. Claims stated about the C1 table

| # | number | claim it supports | source | load-bearing | note |
|---|---|---|---|---|---|
| 48 | γ ≥ 0.005 | the range over which coverage is "pinned" | present-in-plan-only | **yes** | Derivable: rows 21–25 lie within 0.0007 of 0.90. |
| 49 | 4.4 points | "net growth swings 4.4 points" | present-in-plan-only | **yes** | Derivable: 0.0437 → 4.37 points from the γ=0.005 reference (4.39 from γ=0). |
| 50 | 13.7 | "13.7 standard errors" | present-in-plan-only | **yes** | Derivable: 0.0437 / 0.0032 = 13.66. |
| 51 | 0 bps | the cost level at which "the effect vanishes entirely" | present-in-plan-only | **yes** | The cost level is named; its results are not. |
| 52 | 1 SE | "at 0 bps … all diffs within 1 SE" | **orphan** | **yes** | **No 0 bps table appears anywhere in the plan.** This is the paper's identification argument — it is what makes the mechanism *turnover* rather than anything else — and it is a bare assertion. |
| 53 | 5 bps | "at 5 bps it is intermediate" | **orphan** | **yes** | **No 5 bps table appears anywhere in the plan.** The middle point of the monotonicity claim. |
| 54 | 1.0–4.4 points | "this simulation gives 1.0–4.4 points across the γ range" | **orphan** | **yes** | The upper end 4.4 is derivable; **the lower end 1.0 is not**. The plan's own paired differences are 0.02, 0.10, 0.43, 1.84 and 4.37 points. No comparison in the table yields 1.0. The stated range is the basis of the "quantitative match" to Ryan's 0.7–5.3, so the mismatch is material. See `audit/CLAIMS.md` C-c. |
| 55 | 330× | "Var(Δq) rises 330× across the γ sweep" | **orphan** | **yes** | **No variance table appears anywhere in the plan.** Sole evidence for the falsified-variance-hypothesis finding, which the plan calls the difference between an over-determined observation and an identified mechanism. Appears twice (also in §7); counted once. |

## 6. Protocol and preflight

| # | number | claim it supports | source | load-bearing | note |
|---|---|---|---|---|---|
| 56 | ≥60 | minimum paths in the full protocol | present-in-plan-only | no | Consistent with row 11. |
| 57 | ~5× | "common random numbers … cut the SE by ~5×" | **orphan** | no | No unpaired standard errors are reported anywhere, so the reduction factor cannot be checked against anything. |
| 58 | 0.0003–0.003 | "paired CRN gives SE ≈ 0.0003–0.003" | present-in-plan-only | no | Derivable: the table's SEs run 0.0003 to 0.0032. |
| 59 | 0.004–0.044 | "against effects of 0.004–0.044" | present-in-plan-only | no | Derivable only for the top three arms. The table's full effect range is 0.0002–0.0437; the stated lower bound silently drops the γ=0 and γ=0.020 comparisons. |
| 60 | 5–100× | "the design resolves its own question by 5–100×" | **orphan** | **yes** | **Not derivable and materially overstated.** The per-comparison ratios implied by the table are 0.67×, 2.5×, 5.4×, 9.7× and 13.7×. The maximum is 13.7×, not 100×, and two of the five comparisons fall below the stated 5× floor. This is the plan's minimum-detectable-effect argument, marked "**Confirmed**". |
| 61 | γ=0, γ=0.05, 15 bps | the single comparison said to decide C2 | present-in-plan-only | no | Restates rows 14, 17, 12. |
| 62 | ~15 lines | size of the dead-band implementation | **orphan** | no | An estimate of work on a file that does not exist. |

## 7. Prior-art identifiers and years

Existence, metadata and attribution accuracy for every entry are audited in
`audit/REFS_VERIFIED.bib` and `audit/REFS_REJECTED.md`. Load-bearing here means the
paper's *framing* depends on the citation being right, not merely on it existing.

| # | number | claim it supports | source | load-bearing | note |
|---|---|---|---|---|---|
| 63 | 2005 | Vovk, Gammerman & Shafer | present-in-plan-only | no | |
| 64 | 2021 | Gibbs & Candès, ACI | present-in-plan-only | **yes** | The update rule the paper modifies. |
| 65 | 2022 | Gibbs & Candès, DtACI | present-in-plan-only | no | |
| 66 | 2024 | Angelopoulos, Candès & Tibshirani, conformal PID | present-in-plan-only | no | |
| 67 | 2023 | Bhatnagar et al., SAOCP, ICML | present-in-plan-only | no | |
| 68 | 2024 / arXiv:2310.05921 | Lekeufack et al., Conformal Decision Theory, ICRA | present-in-plan-only | **yes** | The headline baseline; the differentiation argument depends on its trading experiment being zero-cost synthetic. |
| 69 | arXiv:2602.03903 | Schmitt, RWCP | present-in-plan-only | no | |
| 70 | 2013 | Gârleanu & Pedersen | present-in-plan-only | **yes** | **The plan calls this "the source of the dead-band form". It is not.** G–P assume *quadratic* costs and derive *linear partial adjustment*, explicitly distinguishing themselves from proportional-cost strategies "which exhibit periods of no trading". The dead-band's sources are Constantinides (1986) and Davis & Norman (1990). G–P remains a correct citation for *quadratic costs ⇒ partial adjustment* only. See `audit/REFS_REJECTED.md` §1.1. |
| 71 | 2022 / arXiv:2202.07282 | Zaffran et al., ICML | present-in-plan-only | **yes** | The closest existing analysis of the ACI learning rate; the plan concedes it must be engaged directly. |
| 72 | 2024 / arXiv:2402.01139 | Angelopoulos, Barber & Bates, ICML | present-in-plan-only | **yes** | Existing partial account of slow-beats-fast that F7 must be distinguished from. |
| 73 | arXiv:2607.26577 | Vaze | present-in-plan-only | **yes** | Basis of the hard "do not frame as an impossibility result" constraint. |
| 74 | 29 Jul 2026 | date of the Vaze preprint | present-in-plan-only | no | |
| 75 | Theorem 7 | the specific result cited from Vaze | present-in-plan-only | **yes** | A theorem *number* asserted for a preprint. Highest-risk citation form in the document. |
| 76 | Ω(T^{2/3}·V_T^{1/3}) — exponents 2/3, 1/3 | the minimax lower bound on cumulative miscoverage | present-in-plan-only | **yes** | If the exponents are wrong the framing constraint is stated against a result that does not exist in that form. |
| 77 | 2026 / arXiv:2507.02496 | Srinivas, SODA | present-in-plan-only | **yes** | Second pillar of the same framing constraint. |
| 78 | 2025 / arXiv:2502.10947 | Ramalingam, Kiyani & Roth, ICML | present-in-plan-only | no | |
| 79 | 2022 | Elmachtoub & Grigas, SPO, *Mgmt Sci* | present-in-plan-only | no | |
| 80 | arXiv:2605.01176 | decision-induced turnover in SPO | present-in-plan-only | no | Wang & Hasuike. Closest cited neighbour on the *pathology* (decision-focused learning churns; damping helps). Read in full S1: it contains no conformal, coverage, quantile or prediction-interval content. See `audit/PRIOR_ART.md` §4.3. |
| 81 | 2003 | Zinkevich | present-in-plan-only | no | |
| 82 | arXiv:2502.10947 (second occurrence) | "no-regret ↔ online conformal" | present-in-plan-only | no | **The same identifier appears twice in the reference list under two different descriptions** (row 78 and this row). See `audit/REFS_REJECTED.md`. |
| 83 | 1956 | Kelly | present-in-plan-only | no | |
| 84 | 2000 | Rockafellar & Uryasev | present-in-plan-only | no | |
| 85 | — | MacLean, Thorp & Ziemba, Kelly under estimation error | present-in-plan-only | **yes** | **No year and no identifier given anywhere.** The only load-bearing citation in the document with no locator at all, and it is the one the plan claims to have experimentally ruled out. |

## 8. The prior novelty sweep

| # | number | claim it supports | source | load-bearing | note |
|---|---|---|---|---|---|
| 86 | 100 titles | size of the Semantic Scholar forward-citation screen of ACI | **orphan** | no | Inherited from a prior sweep; no log, no output, no query record. |
| 87 | 0 | "arXiv returns 0 for `conformal` × `downstream decision` × `variance`" | **orphan** | **yes** | Inherited and **materially wrong**: `audit/PRIOR_ART.md` lists works in exactly this territory that the plan does not cite. |
| 88 | 0 | "arXiv returns 0 for `prediction interval` × `Kelly`" | **orphan** | **yes** | Same provenance, same problem. A zero-hit count from an unrecorded query is not evidence of absence. |

---

## 9. Two arithmetic findings that the trace produced

Both follow from the plan's own table and required no external information.

### 9.1 The growth column is almost exactly the cost identity

At 15 bps, the predicted growth difference from turnover alone is
`−0.0015 × (turnover_γ − turnover_0.005)`. Against the plan's stated paired
differences:

| γ | stated paired diff | `−c × Δturnover` | residual |
|---|---|---|---|
| 0.000 | +0.0002 | +0.0003 | −0.0001 |
| 0.020 | −0.0010 | −0.0015 | +0.0004 |
| 0.050 | −0.0043 | −0.0053 | +0.0009 |
| 0.150 | −0.0184 | −0.0186 | +0.0002 |
| 0.400 | −0.0437 | −0.0414 | −0.0023 |

The residuals are between −0.23 and +0.09 points against effects of up to 4.37
points. Gross growth is therefore flat across the γ grid to within about 5 % of the
effect size.

This cuts two ways and both must be said.

**In the plan's favour:** it is exactly what the untabulated 0 bps null asserts. If
gross growth is flat, then at zero cost the arms are indistinguishable. The table is
internally coherent with a claim the document never displays, which is mild evidence
the 0 bps run was really done.

**Against the plan:** it means the growth column contains essentially no information
beyond the turnover column. A reviewer will perform this subtraction immediately and
conclude that "growth falls because turnover rises and turnover is charged" is an
accounting identity, not a finding. **The result that is not an identity is that
coverage does not constrain turnover.** The paper should lead with the turnover
column and the coverage column, and present the growth column as the monetisation of
a dissociation already visible without it. Leading with the 4.4-point swing invites
the "this is just transaction costs, obviously" objection that the plan itself names
as the thing most likely to kill the paper.

### 9.2 The stated statistical power is overstated

"The design resolves its own question by 5–100×. **Confirmed.**" The ratios of effect
to standard error implied by the plan's own table are:

| comparison | \|diff\| | SE | ratio |
|---|---|---|---|
| γ=0 vs 0.005 | 0.0002 | 0.0003 | 0.67× |
| γ=0.020 | 0.0010 | 0.0004 | 2.5× |
| γ=0.050 | 0.0043 | 0.0008 | 5.4× |
| γ=0.150 | 0.0184 | 0.0019 | 9.7× |
| γ=0.400 | 0.0437 | 0.0032 | 13.7× |

The maximum is 13.7×. There is no 100×, and two of five comparisons sit below the
stated 5× floor. The design comfortably resolves the top three comparisons and does
not resolve the γ=0.020 one. That is a perfectly good design — it simply is not the
design the preflight section claims to have confirmed. Since the γ=0.020 arm is where
a realistic practitioner's γ would sit, its being unresolved at 60 paths matters:
the path count needs to be set by the smallest γ difference the paper wants to claim,
not by the largest.

---

## 10. Tally

| source | count | share |
|---|---|---|
| `reproduced-from-code` | **0** | **0.0 %** |
| `present-in-plan-only` | 76 | 86.4 % |
| `orphan` | 12 | **13.6 %** |
| total numbers catalogued | 88 | 100 % |

Counting convention: the unit is a **number**, not a table row. The single row
covering the six γ values counts as six. The tally is recomputed from this file's own
tables rather than asserted; the orphans are rows 6, 7, 52, 53, 54, 55, 57, 60, 62,
86, 87 and 88.

**Orphans: 12 of 88, 13.6 %. Numbers reproduced from code: 0 of 88, 0 %.**

The headline percentage understates the problem, so the more decision-relevant cuts
are these. Restrict attention to the numbers that are supposed to come from the
simulation (rows 11–62), and then to the load-bearing ones among them.

| category | count | orphans | orphan share |
|---|---|---|---|
| Simulation-derived numbers (rows 11–62) | 52 | 7 | **13.5 %** |
| Load-bearing simulation-derived numbers | 41 | 5 | **12.2 %** |
| Load-bearing numbers whose supporting table is **not shown anywhere** (rows 52, 53, 54, 55, 60) | 5 | 5 | **100 %** |

The last line is the one that matters. Five load-bearing quantities — the 0 bps null,
the 5 bps intermediate case, the claimed 1.0–4.4 point match, the 330× variance rise,
and the claimed 5–100× statistical power — are asserted in prose with no displayed
table behind any of them. Four of the five are precisely the claims the plan
identifies as its strongest evidence:

- the 0 bps null is what identifies the mechanism as turnover,
- the 330× is what falsifies the competing variance explanation,
- the 1.0–4.4 match is what ties the simulation to the published anomaly,
- the 5–100× is what certifies the design has the power to answer its own question.

And the fifth, the 5 bps case, is the middle point of the monotonicity claim.

**The paper's four strongest stated pieces of evidence are the four with no table.**
Together with the absence of the simulator, this is the finding that should govern
what the next session does.

---

## 11. Numbers introduced by session S2, 2026-08-19

**These are a new class and the file's existing three-value `source` vocabulary does not
cover them, so a fourth is defined here.**

- **`verification-run`** — produced by a numerical check written and run *inside a session
  agent's ephemeral workspace* to test a mathematical claim against a published theorem. The
  number is not an experimental result and no arm of `docs/PROTOCOL.md` was executed, **but the
  generating code was not persisted, so no file in this repository can regenerate it.**

**Why this matters and why it is booked rather than left in prose.** S2's brief said the
session *"runs no experiment and writes no simulator"*, and it did not: `src/`, `results/` and
`figures/` still hold only `.gitkeep`. The computations below are refutation checks — they
exist because the brief's stated mechanism for Placement A's failure turned out to be wrong,
and declining to check it would have shipped a false mechanism into the paper. **That is the
right call and the numbers are load-bearing: three of them are printed in
`paper/sections/intro.tex` and `limitations.tex`.** But they are orphans by this file's own
standard, and a paper must not print a number it cannot regenerate. **`docs/GATES.md` G5.6
requires every number in the paper to trace to a `results/` JSON; none of these does yet.**

| # | number | what it is | source | in the paper? | load-bearing |
|---|---|---|---|---|---|
| 50 | 623.7 | `max\|E_t\|` under an exponential filter of weight 0.999, adversarial scores, clipped saturator, `h(t) = log(t+2)`, `c = 1`, `b = 2`, α = 0.1 | `verification-run` | **yes**, intro and limitations | **yes** — it is the paper's surviving quantitative result |
| 51 | 14.8 | Proposition 2's bound `c·h(T)+1` at `T = 10⁶` under the same constants | `verification-run` (derivable by hand from the printed bound) | **yes** | **yes** — the denominator of the forfeit |
| 52 | 10.2 / 12.5 / 14.8 | the same bound at `T = 10⁴/10⁵/10⁶` | `verification-run` | partly | yes |
| 53 | 5.5 / 6.6 / 7.8 | unsmoothed `max\|E_t\|` at the same horizons, comfortably inside the bound | `verification-run` | no | yes — it is the control |
| 54 | 0.1000–0.1002 | realised miscoverage of six filter families against α = 0.1 over `T = 2×10⁵`, adversarial scores | `verification-run` | **yes**, intro and limitations | **yes** — it is what forbids the claim that Placement A loses coverage |
| 55 | 2.37 / 2.97 / 3.53 / 4.15 | `Σ\|Δq_t\|` × Proposition 2's bound for ACT23's tan integrator at `T = 10³/10⁴/10⁵/10⁶` — the Θ(log T) growth that helped withdraw the conservation law | `verification-run` | no | **yes** — it is one of the three defects that killed the claimed contribution |
| 56 | 91.2 → 0.21 | deployed travel with and without a scorecaster that pre-subtracts the integrator, `T = 10⁴`, realised miscoverage 0.0953, clip binding 24/10,000 | `verification-run` | referred to without figures in limitations | **yes** — it is what refutes "irreducible" |
| 57 | 1.12× | the same reduction under distribution shift, clip binding on 89 % of rounds | `verification-run` | referred to without figures | **yes** — it is the regime dependence that makes the open question non-degenerate |
| 58 | 0.36–0.40 vs 0.36 | measured `(Σ\|Δq\|)×(Prop-2 bound)` against the predicted `2α(1−α)b`, η ∈ {0.01, 0.05, 0.2}, `T` ∈ {10³,10⁴,10⁵} | `verification-run`, **and independently re-derived in exact rational arithmetic by the orchestrator** | no | yes — it confirms the withdrawn relation's arithmetic is correct, which is why the objection had to be to its *status* |

**What must happen before any of these is printed in a submitted paper.** Rows 50, 51, 54 and
their supporting rows must be regenerated by committed code under `src/`, emitted to a
`results/` JSON with config, commit and versions, and re-cited from there. **`docs/OUTSTANDING.md`
O43.** Until then the paper is printing numbers on the authority of a session transcript, which
is the same standard this file was written to condemn.
