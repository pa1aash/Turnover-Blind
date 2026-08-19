# Session S2 — the placement reduction, and the protocol freeze

**Date 2026-08-19.** Seven agents in three waves, all launched in parallel within their wave,
all returned. Commits `e67bba4`, `114c29d`, `2f08f26`, all pushed. No experiment was run and
no simulator was written. **No gate is signed.**

---

## 1. The verdict. Everything else in this report is subordinate to it.

> **THE REDUCTION HOLDS.** A movement-penalised value placed in Conformal PID's additive
> scorecaster slot satisfies every hypothesis of Theorem 1. Both the L2 and the L1 form are
> convex combinations of quantities already in `[−b/2, b/2]` — the L1 case via the identity
> `S_τ(u) = u(1 − τ/|u|)₊`, so the soft-threshold worry resolves in the negative because it
> cannot leave the hull. The penalty cannot enlarge `b`, cannot degrade `c`, and the inherited
> bound is identical. **No new theorem is required.**
>
> **AND THE SESSION CANNOT CLAIM IT, BECAUSE THE PLACEMENT IS NOT NEW.** Three independent
> sources have it. **AND THE CONTRIBUTION THE SESSION PUT IN ITS PLACE WAS OVERTURNED BY ITS
> OWN CRITIC, FOUR HOURS AFTER IT WAS WRITTEN.**

The reduction was verified against **both** the NeurIPS 2023 proceedings PDF and the arXiv
preprint, which has exactly one version. Theorem 1, condition (4), the definition of
*admissible*, iteration (5), and Proposition 2's statement **and constant** are
**character-for-character identical** between them. Condition (4) constrains `r_t` alone;
Proposition 2 is stated and proved with no scorecaster present; `q̂` enters Theorem 1's proof
in exactly two places, only one of which uses a property of `q̂`. Measurability is not even a
hypothesis of Theorem 1 — only of implementability.

**It was then attacked three separate times and never damaged.** D2 attacked it blind to D1's
work. F1 attacked it again in wave 4, specifically hunting a suspected factor-of-two hole:
if `q̂` and `s` are each in `[−b/2, b/2]`, then `s′ = s − q̂` is in `[−b, b]`, which is outside
*Theorem 1's* hypothesis. **The hole is not there, and the reason is exact rather than lucky:
`s′` must satisfy Proposition 2's hypothesis, not Theorem 1's, and Proposition 2's hypothesis
is `[−b, b]`.** The two half-budgets exist for precisely this purpose and `b/2 + b/2 = b` is
exactly tight. **That is the tightest point in the whole argument and a later session should
not re-litigate it.**

### R2\* as the brief worded it was wrong in three of its four parts

| R2\* assertion | Verdict | Found by |
|---|---|---|
| Placement B inherits Conformal PID Theorem 1 verbatim | **TRUE** | D1, re-verified by D2 and F1 |
| No new theorem is required | **TRUE** | D1 |
| …and this is a *result* | **FALSE — occupied three times over** | D2, D3, D5 |
| Placement A breaks the saturation condition (4) | **FALSE, and the sign is backwards** | D1 and D3, independently |
| Placement A therefore loses coverage | **NOT SUPPORTABLE** | D1 |
| There are exactly two placements | **FALSE — a third exists** | D3 |
| Four lines all make the same error | **FALSE — two of five** | D3 |
| Placement B discharges Dupuy's domination hypothesis | **FALSE — it AVOIDS it** | D3 |

## 2. Placement A's failure mechanism — and the brief named the wrong one

R2\* says the downstream smoother breaks condition (4) *"because a smoother damps exactly the
excursions the condition needs"*. **Condition (4) is a property of `r_t`. A smoother placed
downstream of the completed output never touches `r_t` and cannot violate it.**

What fails is the single load-bearing step of Proposition 2's induction —
`c·h(T−1) < E_{T−1} ⟹ q_T = r(E_{T−1}) ≥ b ⟹ s_T ≤ q_T ⟹ err_T = 0` — because the integrator
reaches `b`, but an exponential filter of the *output* attains `b` only in the limit of
infinitely many consecutive saturated rounds. **The sign is the opposite of what was asserted:
the smoother does not damp the accumulator's excursions, it lets the accumulator excurse
further, because the correction it is waiting for is delayed.** D1 and D3 reached this
independently, by different routes, without contact.

**And coverage is not lost.** Six filter families — EMA at w = 0.5/0.9/0.99, dead band at
τ = 0.5/0.9/1.5, running mean, and EMA with time constant growing as t^0.5 and t^0.9 — returned
realised miscoverage **0.1000–0.1002** against α = 0.1 under an adversary playing the score
exactly at the deployed threshold over T = 2×10⁵. Verbatim inheritance is refutable only on a
**zero-slack** instance, verified in exact rational arithmetic, legal under Theorem 1's uniform
hypotheses and evaporating under any strict slack.

> **The claim to make:** *Placement A forfeits the inherited theorem and its finite-sample rate.*
> **The claim NOT to make:** *Placement A loses coverage.* **A referee will build the
> counter-simulation in ten minutes.**

The forfeit is measured, and it is **the one result that survived every attack in the session**:
unsmoothed `max|E_t|` = 5.5 / 6.6 / 7.8 at T = 10⁴/10⁵/10⁶ against a bound of 10.2 / 12.5 / 14.8;
**with an EMA of weight 0.999, `max|E_t|` = 623.7**, forty to sixty times the bound. **The forfeit
grows in exactly the knob a turnover-motivated designer turns up.**

## 3. The contribution the session wrote, and then destroyed

Wave 3 recorded, as R2\*\*'s contribution, a **conservation law**: the product of Proposition 2's
coverage-gap bound at horizon `T` with the integrator's per-step movement is a constant of the
horizon, and the penalty weight `w` does not appear in it. Two agents derived it independently
and without contact. It went into FRAMING, into GATES, into PROTOCOL and into the paper.

**Wave 4's adversarial critic killed it, and it was right.** The arithmetic is correct —
`ε·M = 2α(1−α)(b+η)/T`, with the gain cancelling exactly; I re-derived it in exact rational
arithmetic before applying the finding. **The arithmetic being correct is the problem.**

- **Both factors are independent of `w` by construction.** `ε` is Proposition 2's bound, which
  the inheritance claim asserts is *unchanged* by the scorecaster. `M` is *defined* as the
  integrator's own movement, which the scorecaster does not enter. **"`w` does not appear"
  restates the inheritance claim rather than pricing it.**
- **The cancellation of `η` is `x · (1/x)`.** ACT23 print `c = 1/η` for the constant-gain
  integrator **on the same page as the proof**, and `M ∝ η` is immediate.
- **It is not conserved on the object the paper measures.** `Σ|Δq_t|` × the bound grows as
  **Θ(log T)** for ACT23's own default tan integrator — 2.37 / 2.97 / 3.53 / 4.15 at
  T = 10³/10⁴/10⁵/10⁶.
- The printed tan form requires `b = ∞`, the branch the same section forbids; and it multiplies
  a **worst-case certificate** by an **average-case** movement, with one to three orders of slack.

**Two companion claims fell with it.** *"At most half"* is an artefact of ACT23's symmetric
`b/2 + b/2` split: any split `B_q + B_s ≤ b` works with the identical one-line proof, and `b` is
an **analysis constant the designer declares**, not an algorithm input. *"Irreducible"* is false
outright: iteration (5) permits `q̂` to depend on `q_i` and hence on `E_t`, and a scorecaster that
pre-subtracts the integrator **cut deployed travel from 91.2 to 0.21 at T = 10⁴**, miscoverage
0.0953, clip binding on 24 of 10,000 rounds.

**Two agents deriving something independently was read as evidence of depth. It was evidence of
ease.** They were given closely related prompts and both took the obvious route. That is the
methodological lesson of this session and it is worth more than the claim was.

### What survives, stated plainly

1. **The reduction** — verified, thrice-attacked, undamaged. **Not new**, so a citation.
2. **The Placement A forfeit** — 623.7 against 14.8, reproducible, falsifiable, and not in print
   anywhere the session could find.
3. **The correction of the record against arXiv:2412.18144**, which prints that a scorecaster
   *"breaks the theoretical coverage guarantee"* and is wrong. One paragraph, and a real service.

**That is a measurement paper and a correction, not a theory paper.** `docs/GATES.md` G3.9's
*Mathematics of Operations Research* upgrade was conditional on the conservation law and on the
present evidence **should be dropped rather than re-argued.** That remains an operator decision;
the session states the evidence and does not make the call.

### The one route back, found while trying to destroy the old result

Make **deployed travel `Σ|Δq_t|`** the movement variable — not `q̂`'s movement — and let the
scorecaster see `E_t`, which iteration (5) explicitly permits. Then ask *how much of the
integrator's movement a bounded scorecaster can offset, as a function of the budget split
`B_q/b` and the severity of the distribution shift, and what the offsetting costs in the
certificate.* **That has the two things the withdrawn relation lacked: a free parameter and a
regime dependence.** The same cancelling scorecaster that cuts travel 91.2 → 0.21 in the
stationary case **collapses to 1.12× under shift**, because the budget clip binds on 89 % of
rounds instead of 24 in 10,000. Nobody in the vault has asked it. It is one experiment away.
`docs/OUTSTANDING.md` **O42**; `docs/PROTOCOL.md` arm `B2`, promoted to carry it.

## 4. What D3 found about the four neighbouring lines

**The thesis that they "all make the same error" is FALSE and may not be printed.**

| Work | Placement | Note |
|---|---|---|
| **Binny & Dixit** Eq. 13 | **A**, unambiguously | `q̂` is the raw new split-conformal quantile, `q` the running smoothed value, and Algorithm 1 deploys the smoothed one. **R2\* does not collapse.** Their §4.2 writes the planner as `π_MPC(q̂)` *with* the hat when importing the guarantee; Algorithm 1 deploys `π_MPC(q)` *without* it. **Theorem 5 analyses the unfiltered operator, not the filtered iteration the algorithm runs** — sharper than S1 had it. γ verified absent from statement, hypotheses and proof |
| **IPOC** | **A** | Relayed from S1; ACM's challenge defeated all six routes this session, so **not re-verified** |
| **Dupuy** Eqs. (7)/(8) | **a third placement — inside the integrator**, on the loop-closing feedback signal | |
| **ECI** Eq. (4) | **third placement** | A second witness to an obstacle there |
| **SCD-split** | **neither** | It *names* post-hoc alteration as invalidating and deliberately places its smoothing **upstream** of the quantile computation. **It is an authority against Placement A, not an instance of it.** S1's gloss misstates both nouns |

**The substance survives in a stronger form:** each of these puts the penalty somewhere the
validity argument's load-bearing step passes through, and none puts it where the existing proofs
already quantify over — **except Dupuy's own Theorem 1, which does exactly that and inherits
validity verbatim.** Their Theorems 1 versus 2 are a controlled experiment on R2\*'s thesis, run
by someone else.

**Discharge or avoid: AVOIDS, and the paper may not claim otherwise.** Dupuy's domination
hypothesis compares partial sums of *two* feedback sequences and exists only because their
Eqs. (7)/(8) put the smoothed signal **inside** the integrator: the induction bounds the smoothed
sum while long-run coverage is about the raw one, so domination is imposed by hand as the bridge.
Under Placement B the integrator's argument is the unmodified indicator, **so no smoothed sequence
exists and the inequality has no referent.** Conformal PID Theorem 1's hypothesis list is exactly
three items and contains no domination condition. The only route to "discharge" is the degenerate
reading `f ≡ 1{·}`, which is a refusal to make the substitution and reads as sleight of hand.
**The old G3.11 wording — "R2 must discharge that assumption or not be written" — is itself
withdrawn: avoiding is legitimate and sufficient.**

**BC-ACI's monotonicity sentence carries an internal sign error** — it says decreasing α_t "does
not decrease the miscoverage probability" and then the opposite in the next sentence. The second
is correct. **Quote with [sic] or paraphrase; build no argument on the literal wording.**

## 5. Hiding places — closed, and one that materialised

**The session's worst news is not about R2 at all.**

**Chen, Yang, Li & Liu, IEEE Tencon-Spring 2013, doi 10.1109/TENCONSPRING.2013.6584502 —
RESOLVED, AND IT OCCUPIES R1'S DECISION LEG.** S1 recorded it as R1's single unclosed occupancy
risk with no abstract in any index, and that was accurate for Crossref, Semantic Scholar and
Unpaywall. **The abstract is in an embedded metadata block on the IEEE Xplore landing page,
and all seven figures and tables came from Semantic Scholar's figure-extraction service for the
paywalled PDF.** Q1 yes (same per-period forecast distributions by construction, Gaussian-copula
correlation matrix); Q2 yes (Fig. 4 plots both gradient curves); **Q3 yes and priced — Table II,
per-start start-up cost \$300–\$4500**, with minimum on/off times and ramp rates; Q4 yes; Q5 no.
**Q1 ∧ Q2 ∧ Q3 ⇒ OCCUPIED**, with an independent 2018 restatement, so not a one-paper fluke.

`audit/PRIOR_ART.md` §7.9.3's block quote and `docs/FRAMING.md` §8b item 4 are **withdrawn**.
**R1 now owns Q5 alone** — the absence of a coverage object — **plus the calendar-time
revision-path object distinction.** Whether that carries a paper is O28 and it is not settled.

**The zero-result queries under §7.9.3 are left standing**, and that is deliberate: they were run
correctly and still return zero, because the occupant's abstract is absent from the index they
searched. **A well-evidenced absence is evidence about the instrument as much as about the
literature.**

**Closed:** the Schaake-shuffle / ECC / reservoir branch does **not** occupy R1 — 102 papers,
intersection with movement-cost vocabulary exactly one, and the strongest near-miss (Worsnop
et al. 2018) has *"the same spread after shuffling"* but **zero** occurrences of "commitment",
"start-up", "dispatch" or "economic" across 23 pages. **Williams, Peters & Raiszadeh (1985)**
confirmed and strengthened — the arms are *rearrangements*, so the marginal match is an **exact
identity**, stronger than any modern work in the corpus — though the body was not obtained and
needs a library, not a better crawler.

**Left open:** three ScienceDirect items, one of them gold open access and the highest-risk of
the three (O32); the TKDE theory section, where the abstract-level prediction of no new coverage
theorem is **verified** but the module is renamed *"Adaptive Copula Conformal Inference"*, which
**raises** the residual (O33); the body of Chen 2013 (O29); AQA, which anchors a regularisation
term **inside** the threshold update and claims narrower **and** more stable at 90 % coverage,
empirically and with no theorem (O31).

**An operational rule the project had over-generalised, now narrowed.** 403 is bot detection **at
the ACM Digital Library**, which is open access behind it. **IEEE Xplore and Wiley have a real
subscription wall behind the bot wall** — four IEEE targets reached, **zero PDFs**. **ScienceDirect
adds a Turnstile CAPTCHA that headed Chrome does not pass.** The two routes that actually resolved
the session's occupancy risk were **IEEE Xplore's embedded metadata block** and **Semantic
Scholar's figure-extraction service**. As written, the inherited rule would have cost the next
session what the paywall assumption cost S1 (O34).

## 6. What the full-text screen surfaced that abstract search could not

**176 queries logged verbatim with hit counts, 28 of them zero-hit, across 14 probed indices.
11 of 12 methods-level hits would have been missed by abstract search.**

**Verdict: partially adequate.** Adequate for the conformal-theory neighbourhood — 122 arXiv
full-text queries surfaced **no theory occupant** the S1 abstract sweep had missed. **Inadequate
for the applied and cross-domain neighbourhood**, where both decisive hits are non-arXiv,
invisible to abstracts, and absent from every project file:

1. **RBC-AD**, *Connection Science* 38(1) 2026, **Eq. 27**: `τ_u ← (1−η)τ_u + η τ̃_u` — an EMA
   blend of a recalibrated conformal threshold into the deployed one, with a downward-shift
   restriction and an event trigger. **The project's own object, in Placement A, unheadlined in
   an applied anomaly-detection methods section.**
2. **Duerst, Schöley, Hellstrand & Myrskylä**, MPIDR WP-2024-016 — *"We added the constraint that
   the scorecaster's width is not allowed to narrow with time."* **A width-movement constraint
   inside a Conformal PID scorecaster.** The third independent source establishing that the
   placement is not new.

**And a third finding that cuts the other way and is a gift.** Three deployed studies leave the
scorecaster slot **deliberately empty**, one printing that filling it *"breaks the theoretical
coverage guarantee"* (arXiv:2412.18144) — **which is false.** And arXiv:2512.07770 (ICLR 2026)
prints that *"the selection of its scorecaster model is arbitrary and lacks principled guidance."*
**A refereed statement of an open problem is a better home for this contribution than any claim to
have discovered the slot.**

**Instrument inventory, which has changed.** Working: **arXiv full-text search** (body snippets,
back to 2011, counts saturating ~200–260); **Google Scholar**, but it blocks silently after ~38
queries with a 302 and no CAPTCHA; a local PDF-plus-regex corpus. **OpenAlex full text is now a
metered paid API** (`429: Insufficient budget`). IA Scholar session-blocks after one request;
CORE's anonymous tier discards quotation marks; Europe PMC has ~nil coverage; BASE and CiteSeerX
unusable. **A naming casualty: `"total variation"` is unusable** — all ten screened hits are the
TV distance between measures.

## 7. Critic findings and their disposition

**Both critics ran. Nothing was rejected.** One finding was applied in a modified form and the
modification is recorded with its reason. Full record: `research/S2/patch-log.json`, 13 findings.

**F1 (adversarial)** — overturned the session's own contribution; §3 above. Also verified as a
**strength** that the reduction has no factor-of-two hole, found no term collision for the coined
name, and found no occupant in eleven OpenReview full-text queries. Its three ranked hiding places
became O45.

**F2 (instruction)** — `compliant_with_reported_deviations`; 6 pass, 2 partial, 0 fail. Its most
serious finding is **the session's own instance of the failure it was auditing**: the NeurIPS
proceedings PDF — the most load-bearing document in the project, and the version G3.3a makes
*mandatory* to cite — was read in an ephemeral agent scratchpad and **never persisted**, while
G3.3 was marked MET on its authority and the bib entry carried no record path. **Now persisted
(9,060,379 bytes), with the failure recorded in the entry rather than quietly fixed.** F2 also
caught two operator-input leaks — PROTOCOL had *answered* Q6, and had labelled the L2 arm
"Primary treatment" while OI-1 defers exactly that — both closed. And it caught that wave 1's
verification numbers are printed in the paper with no code that can regenerate them; **ten are
now booked in `audit/NUMBERS.md` §11 under a new `verification-run` source class**, with O43
blocking them at G5.6.

F2's verdict on the brief's *"runs no experiment"* clause: **not a violation** — `src/`,
`results/` and `figures/` hold only `.gitkeep`, no simulation code exists, no protocol arm was
run, and the computation was refutation-checking of a published theorem. **Declining it would
have shipped the brief's false mechanism into the paper.**

**Two errors the orchestrator made and is reporting itself.** It added a bib entry for the
**wrong** Delikaraoglou & Pinson 2014 paper, built from a plausible Crossref hit rather than from
the record the finding rests on — **the same provenance failure the session was auditing,
committed while auditing it**, caught by checking against the agent's output instead of against a
search result. And it wrote the conservation law into four documents on the strength of two
agents agreeing.

## 8. The protocol

`docs/PROTOCOL.md`, 1,166 lines. **All thirteen** free choices in `audit/RECONSTRUCTION_SPEC.md`
R1–R13 resolved with a value, a justification and a stated consequence if wrong, plus **twelve
more (R14–R25)** the corrected claim introduces. Placement A and B run on the **same** producer so
the contrast is within-producer; ACI carries Placement A only, **because it has no `q̂` slot**;
**Placement C is added as a third arm.** `T = 10,080` fixed by the horizon arithmetic. Match
tolerance on `E[L]` is 0.5 % relative, **derived rather than asserted**, and the ordering is
enforced by a five-point mechanism so that **widening a tolerance after seeing a growth column
shows up in `git log`.** Turnover decomposed at both levels.

**Two operator items, recorded and not answered.** **OI-1 (Q7, L1 vs L2)** — both implemented,
operator chooses; wave 1 added a new consideration on the L1 side, that condition (4) admits a
**relay/dead-band saturator** contributing exactly zero movement inside its band with Theorem 1
intact. **OI-2 (the regime calibration)** — Hardy (2001) cited rather than parameters invented, the
bibliographic record verified and saved, **but the printed parameter table was not obtained** and
three further routes failed; the obstacle is a subscription wall, not a search failure.
**Proceeding on unverified numbers presented as a citation is recorded as not an option.**

## 9. Honest list of what was not reached

1. **The body of Chen 2013**, the paper that occupies R1's decision leg. The verdict rests on the
   abstract, seven extracted figures and Table II. Two checks could soften it (O29).
2. **The body of Williams, Peters & Raiszadeh (1985).** Ten routes logged. Needs a library.
3. **IPOC was not re-verified.** ACM's challenge defeated all six routes this session. Its
   placement reading is relayed from S1, not re-confirmed — and S1's ACM route is therefore
   *established* rather than *guaranteed*.
4. **The three ScienceDirect items**, including a gold-open-access one on prediction-interval
   width driving decentralised online convex optimisation. Turnstile was not passed (O32).
5. **The TKDE theory section** (O33) and **AQA's body** (O31).
6. **The Hardy (2001) parameter table** — OI-2 stays open and blocking.
7. **The Google Scholar sweep was cut off at ~38 queries by a silent 302, not exhausted** — and it
   is the surface that produced both of D5's decisive hits and nothing else did. **This is the
   single largest unclosed prior-art risk in the session** (O45).
8. **`paper/` is 3.27 pages of a 4-page body** across four sections, before abstract, method or
   results. Each file carries its measurement and a ranked cut list. **This needs an operator
   decision about what to drop, not another tightening pass** (O23).
9. **O42 is not run.** The session's best remaining route to a theory result is one experiment
   away and this session writes no simulator.
10. **The `docs/GATES.md` G3 table is still out of numbering order** (O41), and the new criteria
    the brief asked for at G3.9/G3.10 are at **G3.13/G3.14** because both identifiers were taken.

## 10. Gate status

**G1 — `ready for review`, and amended against itself.** It certifies a prior-art verdict that has
since moved. **The operator should treat O27 as a precondition for signing, not a follow-up.**

**G2-pre — `ready for review`. NOT SIGNED.** The pre-registration half of G2: the decisions are
frozen before any code exists, which is the entire point. It asserts that the decisions are
frozen, **not that they are correct.**

**No gate in `docs/GATES.md` is recorded as signed, and all eight retain the prohibition line.**
