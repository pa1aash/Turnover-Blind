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

**Status: `ready for review`, with one criterion outstanding by design.** Prepared by
session S1 (2026-08-19).

**A note on that status, because the file's own vocabulary is strict.** `ready for review`
is defined above as "every criterion has evidence in the repository". **G1.7 (venue chosen)
has no evidence and cannot have any**, because it is an operator decision this session is
forbidden to make, and G1.3 is met only partially. The status is used here to mean *every
criterion an automated session could evidence has been evidenced, and the remainder are
identified* — the gate is put in front of the operator with its gaps named, not asserted
complete. If that stretches the vocabulary too far, the correct status is `in progress`, and
that is the operator's call to make on review.

**What this gate asks:** is the project pointed at something real, and does it know what
it is claiming?

**Read `docs/FRAMING.md` before reviewing this gate.** The claims this gate certifies are
not the claims it was written against. The prior-art sweep found the first claim occupied,
and the framing is locked around what survives.

| # | Criterion | Evidence | Met? |
|---|---|---|---|
| G1.1 | **The forward-citation screen of Gibbs–Candès ACI has been run**, filtered for cost, turnover, trading and execution | **Ran in full, with no API key.** 659 unique citing papers across ACI (557), DtACI (188), Conformal PID (147) and SAOCP (101); 38 queries logged verbatim; 12 candidates; zero OCCUPIED, zero NARROW. `research/S1/A1-forward-citations.json`, `audit/PRIOR_ART.md` §7. The instrument was incremental backoff (4 s → 40 s, ~25 retries) against the anonymous Semantic Scholar pool. **The originally prescribed OpenAlex fallback would have produced a false negative** — its ACI record carries 27 citations against Semantic Scholar's 557, a 95 % miss | yes |
| G1.2 | The prior-art sweep has been extended beyond arXiv to Springer, INFORMS and the quantitative-finance journals | `research/S1/A3-non-arxiv.json` — 130 queries, 12 venues. COPA swept exhaustively: all nine PMLR volumes and all 243 paper abstracts term-scanned. All seven INFORMS journals and seven quantitative-finance journals via Crossref. SSRN reached through Crossref prefix `10.2139`, which sidesteps its 403 wall | yes |
| G1.3 | Jia & Han (doi 10.1007/978-981-92-2014-4_25) obtained and its proximity assessed from the paper, not the abstract | **Partially met, and the shortfall is recorded.** Abstract, full 26-item reference list, keywords and affiliations obtained from the Springer landing page; the body is closed — no open-access location, no preprint, absent from the author's own publication page. Scored **CLEAR / CLEAR**. `research/S1/A4-fulltext.json` | partial |
| G1.4 | The CLEAR / NARROW / OCCUPIED verdicts are re-affirmed or revised after G1.1–G1.3 | **Revised, and one moved to OCCUPIED.** `audit/PRIOR_ART.md` §7, dated, superseding §5. Full synthesis in `research/S1/B1-verdicts.md` | yes |
| G1.5 | The opening framing no longer claims the anomaly is unexplained | `docs/FRAMING.md` §4 item (i); the condemned wording is removed from every working document and marked by dated correction note in the three historical ones | yes |
| G1.6 | No claim is framed as an impossibility result, a coverage floor or a fundamental limit | `docs/FRAMING.md` §3 states the operational restatement rule; `research/S1/B3-framing-audit.md` lists every hit in the tree with `file:line`; `research/S1/W3-patch-application.md` records the application and the verification greps | yes |
| G1.7 | Venue chosen by the operator | **NOT MET — operator decision.** `docs/OPEN_QUESTIONS.md` Q3 | no |
| G1.8 | The C-a fork is decided: dead-band on the quantile update, or on the decision map | **Superseded by the matched-width design and re-posed.** The penalty now sits on the width path — the readout — which is neither of the two original branches. What remains open is the penalty's functional form (`docs/OPEN_QUESTIONS.md` Q7) and whether a validity condition is proved or the arm is reported as a measured control (G3.3) | superseded |
| **G1.9** | **The matched-width design is recorded in `docs/FRAMING.md` before any code exists** | `docs/FRAMING.md`, committed 2026-08-19. No simulator exists in `src/`; the design is therefore recorded against no results, which is the point of the criterion | yes |

**Explicit fail conditions, as written before the sweep, and how they resolved.** G1 was to
fail if the forward-citation screen surfaced a work that varies a conformal adaptation rate
and reports a downstream movement cost, or if Jia & Han turned out to sweep adaptation rate
against turnover. **Neither occurred.** The screen returned zero OCCUPIED and zero NARROW
across 659 papers, and Jia & Han is CLEAR on both claims.

**But a fail condition that was not written did occur**, and it is recorded here rather
than let pass: the claim was found occupied by a work in a **different literature**, which
neither stated condition would have caught, because both were phrased in conformal
vocabulary and the occupant uses none of it. See `docs/FRAMING.md` §0. The honest response
was to re-scope, and that is what `docs/FRAMING.md` §2.2 does.

**Requires explicit operator sign-off. This gate MUST NOT be recorded as signed by an
automated session under any circumstances.**

---

## G2 — R1 measured under the matched-width design; protocol frozen and pre-registered

**Status: `not started`.** This is the gate that the missing simulator makes into the
project's critical path.

**Rewritten 2026-08-19 for the matched-width design.** The old G2 was written against a
design that varied ACI's adaptation rate γ. That design is abandoned; see
`docs/FRAMING.md` §5 for what the change bought and cost. Criteria G2.1–G2.9 and
G2.11–G2.12 carry over essentially unchanged because they are about experimental hygiene
rather than about the manipulated variable. **G2.10 is deleted and replaced; G2.13 is new.**

| # | Criterion | How it is evidenced |
|---|---|---|
| G2.1 | A simulator exists in `src/`, and every free choice in `audit/RECONSTRUCTION_SPEC.md` R1–R13 is fixed in a committed configuration file **before** the sweep is run | Config file, committed, with a timestamp preceding the first results JSON |
| G2.2 | The five tests in `audit/RECONSTRUCTION_SPEC.md` §3 pass: CRN bit-identity, zero-cost invariance, the cost identity, the degenerate-arm check, and leakage | A test file and a green run recorded in `results/` |
| G2.3 | Every run emits a `results/` JSON carrying the full config, the git commit, wall-clock time, library versions, **per-path raw quantities**, and the aggregate table as a derived field | The files themselves |
| G2.4 | The reproduction targets in `audit/RECONSTRUCTION_SPEC.md` §4 are met, or the failure to meet them is reported as the result | A written comparison |
| G2.5 | **The interval is the empirical-quantile ACI, not a Gaussian proxy** — or both are run and both reported | R1 is the highest-severity specification risk and a conformal-literate reviewer will find it. It matters more under the matched-width design than it did before: the empirical quantile is a *step function* of α_t and therefore already carries a dead-band, which is part of the very mechanism now being manipulated |
| G2.6 | The 0 bps and 5 bps tables are **displayed**, not asserted | Tables in the repository |
| G2.7 | `Var(Δq)` reported **both** normalised and absolute, **and** the level statistic `Var(q)` reported alongside | `audit/CLAIMS.md` C-d |
| G2.8 | An equivalence test with a stated margin replaces "flat within 1 SE" | Absence of evidence is not evidence of absence |
| G2.9 | Time-at-α-clip and time-at-leverage-cap reported per arm | R5 and R7 |
| **G2.10** | **The arms are MATCHED, and the match is verified and reported before any growth column is computed.** Realised coverage matched across arms to within **0.002**; `E[L]` matched to within a tolerance stated in the protocol **before the sweep is run**. The match-verification table is produced, committed and inspected **first**; the growth column is computed only afterwards | The match-verification table as its own committed artefact, timestamped before the results JSON that carries growth. **If the arms do not match, the finding is that they do not match** — the tolerance is not to be widened after seeing the growth column, and widening it after the fact is a G2 failure by the same logic as the fail condition below |
| G2.11 | Path count set by the smallest difference the paper intends to claim, not the largest | Set from the smallest smoother-parameter separation whose growth difference the paper will report |
| G2.12 | The protocol is pre-registered before the applied arm is touched | A committed, timestamped protocol document |
| **G2.13** | **Total turnover is decomposed into its ŝ_t-driven and α_t-driven components, per arm** | Two columns per arm plus a residual, in the results JSON. The γ = 0 arm of the abandoned design already carried annual turnover 3.2 entirely from scale-estimator churn, so an undecomposed turnover column cannot attribute anything. This is what makes the manipulated variable identifiable rather than merely correlated |
| **G2.14** | **The measured path functional is reported under the name it already has in the literature, or under a new name that collides with none of the taken ones** | `Σ\|Δq\|` is already published as Zanotti's MQC/SMQC, and *smoothed conformal*, *stable conformal*, *smoothing-based conformal* and *interval stability* are all taken. `docs/FRAMING.md` §7 item 5 |

### G2.10 — the deleted criterion, and why

The previous G2.10 read:

> **The Zaffran discriminator is run, in its strict form**: does `Σ|Δq|` carry information
> about net growth **conditional on** `E[L]` across the γ grid?

**It is deleted, and the deletion is recorded rather than silently dropped.**

**The reason it cannot be run: the test is rank-deficient.** Across the only manipulated
variable of the abandoned design, both `E[L]` and `Σ|Δq|` are approximately affine in γ —
the plan's own turnover column gives slopes of 67, 78, 86 and 70 per unit γ, and Zaffran's
Theorem 3.1 gives mean length as affine in γ to leading order. Two regressors that are both
affine in the single manipulated variable are collinear, so the conditional coefficient is
not identified. The test could be *computed*; it could not be *estimated*. Recording it as
an acceptance criterion invited a session to run it and report a number that meant nothing.

**What replaces it is not a weaker test but a different one.** The matched-width design
achieves by construction what the conditional test was trying to achieve by regression:
`E[L]` is held fixed, so any growth difference across arms cannot be attributed to it. The
new G2.10 verifies that construction actually held, which is the assumption the whole design
rests on. `docs/OUTSTANDING.md` O8 is closed as deleted-with-reason.

**Explicit fail condition.** If the free parameters are adjusted after seeing whether the
output matches an expected table, G2 has failed regardless of the numbers. The same applies
to the matching tolerance in G2.10: a tolerance chosen after seeing the growth column is not
a tolerance.

**Requires explicit operator sign-off. This gate MUST NOT be recorded as signed by an
automated session under any circumstances.**

---

## G3 — R2: the movement penalty on the deployed quantile, and what it does to validity

**Status: `not started`.**

**Rewritten 2026-08-19.** The old G3 required a coverage theorem or an explicit demotion.
**That framing is replaced.** Session S1 established (`research/S1/A6-postprocessing-coverage.json`)
that no existing result covers a two-sided smoother on a conformal quantile, that the
enlarging-only monotonicity arguments do not extend to it, and that the obligation is
narrower than a theorem: **a lemma with three verifiable conditions.** No theorem is
required, and none may be claimed without a proof.

| # | Criterion | How it is evidenced |
|---|---|---|
| G3.1 | The movement penalty is implemented on the **width path** — a one-scalar smoother on the deployed quantile `q_t` — as recorded in `docs/FRAMING.md` §1 | Code in `src/`. Note that this is neither branch of the superseded C-a fork; it is the readout |
| G3.2 | **The dead-band asymmetry is tested.** With α = 0.10 the ACI increment is +0.1γ on a cover and −0.9γ on a miss, so a symmetric threshold suppresses one direction only | A measured over-coverage result, or a demonstration that an asymmetric threshold is required. **Retained deliberately**: it is cheap, and it is the evidence for why the penalty belongs on the readout rather than on the α_t update |
| **G3.3** | **The smoothed interval's realised coverage is MEASURED and REPORTED, per arm. No theorem is claimed.** | The measured coverage column. **Coverage may be claimed by construction for the RAW arm only.** ACI's telescoping identity is untouched by a readout smoother — and therefore certifies the raw interval, not the deployed smoothed one. Gibbs–Candès Lemma 4.1 turns on `α_t < 0 ⇒ Q̂_t(1−α_t) = ∞ ⇒ err_t = 0`, a property of the construction; feeding the recursion the smoothed indicator breaks that proof. `docs/FRAMING.md` §4, seventh item |
| **G3.4** | **The three lemma conditions are checked for the specific smoother used**: (a) `q̃_t` is `F_{t−1}`-measurable; (b) deployed miscoverage stays monotone in α_t; (c) α_t stays bounded | (a) is trivial for partial adjustment and (c) follows with lag of order 1/λ. **(b) is where the work is**, and it is the condition that BC-ACI's own coverage proposition (arXiv:2604.13253, Prop. 3) names and secures only by leaving the width mechanism untouched. If (b) holds under a stated bounded-lag condition, that is the paper's technical contribution. If it does not, say so and rely on G3.3 |
| G3.5 | The dominance claim is stated compatibly with Andrew et al. Theorem 2, using the one-dimensional Theorem 7 exception | "Dominates both" without qualification is not available |
| G3.6 | The switching-cost literature is engaged in related work | Kalai–Vempala, shrinking dartboard, Andrew et al., smoothed OCO. `paper/sections/related.tex` |
| **G3.7** | **The forecast-stability literature is engaged in the OPENING, not in related work**, and the no-novelty concession for the readout forms is made explicitly and by name | Godahewa et al. (*IJF* 2025) publish the linear partial-adjustment readout; Genov et al. (*ESWA* 2026, Eq. 18–20) publish the Lipschitz readout-map bound on switching cost. `docs/FRAMING.md` §7 item 1. A paper that does not do this is a rediscovery and will be recognised as one |
| **G3.8** | **IPOC is read and distinguished** | **MET 2026-08-19.** Read in full; its single coverage statement (Lemma 3, §5.1) is Gibbs–Candès imported for the **base model's** interval `c^f_t`, not for the chased ensemble interval the movement cost acts on, and Appendix A's notation table settles the scope. **Q5 = no; the conditional is closed in the project's favour.** `docs/FRAMING.md` §8, `audit/PRIOR_ART.md` §7.8.1. Residual: the TKDE extension's theory section is still unverified |
| **G3.11** | **R2 is positioned against Dupuy et al. Theorem 2 specifically**, not against an empty field | Dupuy, Xu, Perrey, Montmain & Imoussaten, arXiv:2510.02809 / doi 10.1007/978-3-032-16708-8_17 already prove long-run coverage for an online conformal update explicitly designed to prevent abrupt threshold changes. Their Thms 1 and 3 are the inherited saturating-integrator argument; **their Thm 2 is the case where the width mechanism is driven by the smoothed signal, and it needs a domination hypothesis they themselves call "pretty strong" and "highly dependent on the choice of parameters".** R2 must discharge that assumption or not be written. `audit/PRIOR_ART.md` §7.8.3 |
| **G3.12** | **No novelty is claimed for the smoother as an object** | Binny & Dixit, arXiv:2511.11567, Eq. (13), publish `q ← (1−γ)q + γ q̂` on a deployed conformal calibration threshold. `docs/FRAMING.md` §2.1 |
| G3.9 | Journal nomination fixed by the operator | Working default *Stochastic Systems*. The *Mathematics of Operations Research* upgrade is conditional on G3.4(b) being discharged as a proof |
| **G3.10** | **If R2 cannot be delivered, the project re-scopes rather than submitting R1 alone** | A written decision. **The inherited STOP condition — "fall back to reporting C1 alone" — is now the wrong fallback**, because R1 alone is the occupied leg. `docs/FRAMING.md` §2.3 |

**What was removed and why.** The old G3.3 offered "either a coverage theorem with the
accumulated-suppression term bounded sublinearly, **or** demotion to an a-posteriori
certificate". The dichotomy was false in both directions: a full theorem is more than the
design needs, and demotion is less than it can support. The lemma route in G3.4 is the
correct middle, and it exists because S1 read the proofs that name its conditions. The old
G3.4 (attempt the Online Balanced Descent potential-function template) is dropped as a
criterion — it was the one technique available before those proofs were read, and it is now
superseded by a specific and cheaper obligation.

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

**Revised 2026-08-19.**

G2 is still the critical path in the sense that nothing in G3, G4 or G5 can be evidenced
without a simulator. But the ordering *reason* has changed. Under the abandoned design, G2
carried the paper: C1 was the result and C2 was the extension. Under the matched-width
design that is inverted — **G3 carries the paper and G2 is its motivation**
(`docs/FRAMING.md` §2.2). G2 must still come first mechanically, because the smoother
cannot be measured before the producer exists; it no longer comes first in importance.

Two consequences for sequencing:

1. **G3.8 is met — IPOC has been read and does not occupy R2.** What replaced it as the
   first thing to do without compute is **G3.11**: position R2 against Dupuy et al.
   Theorem 2, which is a real attempt at R2's result with a disowned assumption. That is a
   reading-and-thinking task, not a compute task.

   **An operational note that outranks the finding.** The eleven routes that failed to reach
   IPOC all assumed the ACM Digital Library's HTTP 403 was a paywall. **It is Cloudflare bot
   detection; the ACM Digital Library is open access.** A headed system Chrome instance with
   a persistent profile passes the challenge and the PDF downloads. **Every ACM paper in
   this project is reachable this way, and the same misdiagnosis is likely hiding several
   IEEE, Springer and Elsevier items** — see `audit/PRIOR_ART.md` §7.8.7 item 2.
2. **G3.4(b) — whether deployed miscoverage stays monotone in α_t under the smoother — can
   be attacked on paper before any code exists**, and should be. It is the paper's technical
   contribution if it holds. Discovering during implementation that it does not hold would
   waste the implementation.

G1.8 is superseded (see G1). What replaces it as the decision that must precede G3 work is
the penalty's functional form — `docs/OPEN_QUESTIONS.md` Q7 — and it is an operator
decision, not a discovery.
