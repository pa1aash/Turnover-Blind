# Stage gates

Acceptance criteria are written **now, before the work**, so they cannot be retrofitted
to whatever the work happens to produce. That is the entire point of this file. A gate
whose criteria are written after the result is not a gate.

## The rule that governs every entry below

> **Requires explicit operator sign-off. This gate MUST NOT be recorded as signed by an
> automated session under any circumstances.**

That line appears in every gate and is not decorative. An automated session may prepare a
gate, gather the evidence for it, and state that it is *ready for review*. It may not
record it as signed, approved, passed, cleared, or met. If a future session finds itself
writing "gate Gn passed", that session has made an error and should write "Gn ready for
review" instead.

## Status vocabulary

| Status | Meaning |
|---|---|
| `not started` | No work has begun against this gate's criteria. |
| `in progress` | Work is under way; criteria not all evidenced. |
| `ready for review` | Every criterion has evidence in the repository. Awaiting operator sign-off. |
| `signed` | **Only the operator may set this.** |
| `failed` | The operator reviewed and did not sign. Record why. |

---

## G0 — Characterisation complete

**Status: `ready for review`.** This session's output.

**What this gate asks:** does the project know what it actually has?

| # | Criterion | Evidence | Met? |
|---|---|---|---|
| G0.1 | Repository exists, is public, MIT-licensed, sole-authored, with mechanical authorship hygiene enforced and tested | `LICENSE`, `tools/check_hygiene.sh`, `.git/hooks/commit-msg` (rejection demonstrated on two message forms), `git log --format='%an <%ae>'` | yes |
| G0.2 | Complete file inventory a new collaborator can read in one pass | `audit/INVENTORY.md`, regenerable via `tools/gen_inventory.py` | yes |
| G0.3 | The C1 table is either reproduced from code or its reproduction is shown to be impossible, with evidence | `audit/REPRO_C1.md` — ten search commands, all negative; every cell NOT-EMITTED | yes |
| G0.4 | Every numeric claim in the plan traced to a source, with an orphan count | `audit/NUMBERS.md` — 88 numbers, 0 reproduced from code, 12 orphans (13.6 %) | yes |
| G0.5 | Claims decomposed and tagged by status, load-bearingness and evidence | `audit/CLAIMS.md` | yes |
| G0.6 | Every reference resolved against a fetched canonical record on three separate checks | `audit/REFS_VERIFIED.bib` (43 entries), `audit/REFS_REJECTED.md` (7 of 22 failed) | yes |
| G0.7 | Independent prior-art sweep with explicit CLEAR / NARROW / OCCUPIED verdicts | `audit/PRIOR_ART.md` — C1 NARROW, C2 NARROW-conditional | yes |
| G0.8 | Venue candidates scored against live calls for papers | `docs/VENUE.md` — six venues, deadlines from OpenReview's own records | yes |
| G0.9 | Gates, outstanding items, open questions and compute plan written | this file, `docs/OUTSTANDING.md`, `docs/OPEN_QUESTIONS.md`, `docs/COMPUTE.md` | yes |
| G0.10 | A consolidated report that leads with the findings that most change what happens next | `docs/G0_REPORT.md`, `docs/HYPERRESEARCH_REPORT.md` | yes |

**Requires explicit operator sign-off. This gate MUST NOT be recorded as signed by an
automated session under any circumstances.**

---

## G1 — Prior-art verdict accepted; framing locked; venue chosen

**Status: `not started`.**

**What this gate asks:** is the project pointed at something real, and does it know what
it is claiming?

| # | Criterion | How it is evidenced |
|---|---|---|
| G1.1 | **The forward-citation screen of Gibbs–Candès ACI has been run**, filtered for cost, turnover, trading and execution, from an environment with a working Semantic Scholar API key | A logged query, a result list committed to `audit/`, and a written verdict. This is the single largest hole in the G0 sweep. |
| G1.2 | The prior-art sweep has been extended beyond arXiv to Springer, INFORMS and the quantitative-finance journals | Jia & Han (PAKDD 2026) was missed precisely because the sweep was arXiv-centric. That failure must not repeat. |
| G1.3 | Jia & Han (doi 10.1007/978-981-92-2014-4_25) obtained in full text and its proximity to C1 and C2 assessed from the paper, not the abstract | A note in `audit/PRIOR_ART.md` |
| G1.4 | The CLEAR / NARROW / OCCUPIED verdicts are re-affirmed or revised after G1.1–G1.3 | `audit/PRIOR_ART.md` revision with a dated amendment |
| G1.5 | The opening framing no longer claims the anomaly is unexplained | The corrected framing — that Ryan offers an unmeasured, non-turnover-specific conjecture and F7 tests it — is written down and adopted |
| G1.6 | No claim is framed as an impossibility result, a coverage floor or a fundamental limit | A grep of the draft against the two at-risk phrasings named in `audit/PRIOR_ART.md` §6 |
| G1.7 | Venue chosen by the operator | `docs/VENUE.md` updated with the decision and its date |
| G1.8 | The C-a fork is decided: dead-band on the quantile update, or on the decision map | A one-paragraph written decision. C2's scope, novelty and risk all follow from it. |

**Explicit fail conditions.** G1 fails if the forward-citation screen surfaces a work that
varies a conformal adaptation rate and reports a downstream movement cost; or if Jia & Han
turns out to sweep adaptation rate against turnover. Either would move C1 to OCCUPIED, and
the honest response is to stop and re-scope, not to re-word.

**Requires explicit operator sign-off. This gate MUST NOT be recorded as signed by an
automated session under any circumstances.**

---

## G2 — C1 reproduced and hardened; protocol frozen and pre-registered

**Status: `not started`.** This is the gate that the missing simulator makes into the
project's critical path.

| # | Criterion | How it is evidenced |
|---|---|---|
| G2.1 | A simulator exists in `src/`, and every free choice in `audit/RECONSTRUCTION_SPEC.md` R1–R13 is fixed in a committed configuration file **before** the sweep is run | Config file, committed, with a timestamp preceding the first results JSON |
| G2.2 | The five tests in `audit/RECONSTRUCTION_SPEC.md` §3 pass: CRN bit-identity, zero-cost invariance, the cost identity, γ=0 degeneracy, and leakage | A test file and a green run recorded in `results/` |
| G2.3 | Every run emits a `results/` JSON carrying the full config, the git commit, wall-clock time, library versions, **per-path raw quantities**, and the aggregate table as a derived field | The files themselves |
| G2.4 | The reproduction targets in `audit/RECONSTRUCTION_SPEC.md` §4 are met, or the failure to meet them is reported as the result | A written comparison |
| G2.5 | **The interval is the empirical-quantile ACI, not a Gaussian proxy** — or both are run and both reported | R1 is the highest-severity specification risk and a conformal-literate reviewer will find it |
| G2.6 | The 0 bps and 5 bps tables are **displayed**, not asserted | Tables in the repository |
| G2.7 | `Var(Δq)` reported **both** normalised and absolute, **and** the level statistic `Var(q)` reported alongside | `audit/CLAIMS.md` C-d: the plan may be falsifying a statistic the competing channel does not depend on |
| G2.8 | An equivalence test with a stated margin replaces "flat within 1 SE" | Absence of evidence is not evidence of absence |
| G2.9 | Time-at-α-clip and time-at-leverage-cap reported per arm | R5 and R7: the headline γ=0.400 arm may be governed by an undocumented clip |
| G2.10 | **The Zaffran discriminator is run**: is turnover a monotone function of mean interval width across the γ grid? | If it is, C1 reduces to Zaffran's theorem times a cost rate. Cheap, decisive, and it must be run early |
| G2.11 | Path count set by the smallest γ difference the paper intends to claim, not the largest | The γ=0.020 comparison sits at 2.5 SE in the plan's own table |
| G2.12 | The protocol is pre-registered before the applied arm is touched | A committed, timestamped protocol document |

**Explicit fail condition.** If the free parameters are adjusted after seeing whether the
output matches the plan's table, G2 has failed regardless of the numbers. The agreement
would carry no evidential weight, and the question "how were these constants chosen?" has
no good answer.

**Requires explicit operator sign-off. This gate MUST NOT be recorded as signed by an
automated session under any circumstances.**

---

## G3 — C2 implemented; theorem proved or claim demoted; journal nomination fixed

**Status: `not started`.**

| # | Criterion | How it is evidenced |
|---|---|---|
| G3.1 | The C-a fork decision from G1.8 is implemented as specified | Code in `src/` |
| G3.2 | The dead-band asymmetry is tested: with α = 0.10 the ACI increment is +0.1γ on cover and −0.9γ on miss, so a symmetric threshold suppresses one direction only | A measured over-coverage result, or a demonstration that an asymmetric threshold is required |
| G3.3 | **Either** a coverage theorem is proved for the implemented update, with the accumulated-suppression term bounded sublinearly, **or** the claim is demoted to the a-posteriori certificate in `audit/CLAIMS.md` C-a | A proof, or a written demotion. Not a sentence that reads like a theorem and is not one |
| G3.4 | The Online Balanced Descent potential-function template has been attempted for G3.3 | It is the one concrete technique this audit surfaced for the problem |
| G3.5 | The dominance claim is stated compatibly with Andrew et al. Theorem 2, using the one-dimensional Theorem 7 exception | "Dominates both" without qualification is not available |
| G3.6 | The switching-cost literature is engaged in related work | Kalai–Vempala, shrinking dartboard, Andrew et al., smoothed OCO |
| G3.7 | Journal nomination fixed by the operator | Working default *Stochastic Systems*; the *Mathematics of Operations Research* upgrade is conditional on G3.3 being a proof rather than a demotion |
| G3.8 | If C2 is demoted, the STOP condition is exercised deliberately: report C1 alone | A written decision, not a drift |

**Requires explicit operator sign-off. This gate MUST NOT be recorded as signed by an
automated session under any circumstances.**

---

## G4 — Ryan-configuration replication complete

**Status: `not started`.** The applied arm is a replication of Ryan's configuration, not a
generic equity experiment.

| # | Criterion | How it is evidenced |
|---|---|---|
| G4.1 | The configuration recorded in `research/checkpoints/02-width-sweep.md` is implemented as stated: 8 ETFs (SPY, QQQ, DIA, MDY, GLD, SLV, USO, DBC), α = 0.25, W = 500 rolling quantile shrunk with λ = 0.3 toward an expanding anchor, σ̂ = q/1.2816, κ = 0.15, winsorised ±0.75 per asset, gross cap 2.0, 1-day lag, 5 bps per unit turnover | Code and config |
| G4.2 | Ryan's reported DEV numbers are reproduced within a stated tolerance, or the discrepancy is reported | 28.45 % net log growth, Sharpe 1.336, 27.7 % max drawdown, realised coverage 0.7483, turnover 14.1×/15.1× |
| G4.3 | The **prediction is pre-registered before the comparison is made**: F7's mechanism predicts Ryan's per-device growth costs | This converts "same order of magnitude" into a real test, and is the strongest single thing this project could produce |
| G4.4 | Ryan's cost sweep (0/5/10/20/50 bps) is **decomposed per losing device** — the analysis Ryan ran only on aggregate configurations | This is the precise gap F7 fills on real data |
| G4.5 | The disclosed z = 1.2816 / 1.1503 inconsistency in Ryan's own configuration is handled explicitly, both ways | It is disclosed in his paper; silently "fixing" it makes the replication not a replication |
| G4.6 | The development-window qualification is carried into the paper: the anomaly is a DEV-window finding from a ~200-configuration search whose sizing map failed out of sample | Honest framing of what is being explained |
| G4.7 | Data provenance recorded; `data/` remains untracked | `docs/PROVENANCE.md` |

**Requires explicit operator sign-off. This gate MUST NOT be recorded as signed by an
automated session under any circumstances.**

---

## G5 — Full draft at four pages; compliance checklist clear

**Status: `not started`.**

| # | Criterion | How it is evidenced |
|---|---|---|
| G5.1 | Every line of the compliance checklist in `docs/VENUE.md` §4 is checked | The checklist, with each box evidenced |
| G5.2 | Main body is at most 4 pages in the unmodified `neurips_2026.sty` | A compiled PDF |
| G5.3 | `\workshoptitle{}` is set alongside `\title{}` | The source |
| G5.4 | Bibliography built from `audit/REFS_VERIFIED.bib` only | No entry written from memory |
| G5.5 | The three open compliance questions in `docs/VENUE.md` are resolved: in-person presentation, reciprocal reviewing, preprint eligibility | Written answers |
| G5.6 | Every number in the paper traces to a `results/` JSON | A trace table |
| G5.7 | `tools/check_hygiene.sh` passes on the full tree including `paper/` | A green run |

**Requires explicit operator sign-off. This gate MUST NOT be recorded as signed by an
automated session under any circumstances.**

---

## G6 — Submission

**Status: `not started`.**

| # | Criterion | How it is evidenced |
|---|---|---|
| G6.1 | G0–G5 all signed by the operator | This file |
| G6.2 | Co-authors have approved the submitted version | Out of scope for automated sessions |
| G6.3 | Journal nomination selected at submission, at most one | The submission form |
| G6.4 | Repository visibility is correct for the chosen venue's anonymity regime | Public is correct for a non-anonymous venue; a double-blind venue requires it to be made private first |
| G6.5 | Submitted before the deadline, without relying on the 30-minute OpenReview expiry buffer | Confirmation |

**Requires explicit operator sign-off. This gate MUST NOT be recorded as signed by an
automated session under any circumstances.**

---

## Note on gate ordering

G2 is the critical path. Nothing in G3, G4 or G5 can be evidenced without a simulator, and
G1.8 (the C-a fork) should be decided *before* G3 work begins rather than discovered
during it. G1 and G2 can proceed in parallel: the citation screen does not depend on the
simulator, and the simulator does not depend on the citation screen.
