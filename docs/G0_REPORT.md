# G0 characterisation report

**Project:** F7 — *Coverage Is Turnover-Blind: Why Adaptive Conformal Is Mis-Tuned for
Costly Decisions*
**Session date:** 2026-08-19
**Status: G0 is ready for review. It is not signed, and no automated session may sign it.**

---

## The five findings that most change what this project should do next

Worst news first.

### 1. The central experiment does not exist, and neither do the results it is said to have produced

The planning document states that "the central experiment is already done" and attributes
its headline table to `scratchpad/confloor5.py`. **That file does not exist in this
repository, and no trace of it exists anywhere on the machine** — not the filename, not the
string `confloor`, not the distinctive value `0.8993`, not a `scratchpad/` directory at
all. Ten search commands, all negative, are logged in `audit/REPRO_C1.md` §1.

The consequence is not merely that a file is missing. Of **88 numeric claims** catalogued
from the planning document, **0 are reproduced from code**. And **five load-bearing
quantities have no displayed table anywhere in the document, at any cost level**:

- the 0 bps null — the result that identifies the mechanism as turnover rather than variance;
- the 5 bps intermediate case — the middle point of the monotonicity claim;
- the 330× rise in `Var(Δq)` — the sole evidence for the falsified variance hypothesis;
- the claimed 1.0–4.4 point match to the published anomaly;
- the claimed 5–100× statistical power, marked "**Confirmed**".

**Four of the five are precisely the results the plan identifies as its strongest
evidence.** Recovering the simulator would not recover them; they were never tabulated.

Two arithmetic findings follow from the plan's own table, and both matter. The growth
column is almost exactly the accounting identity `Δgrowth = −c × Δturnover`, with residuals
between −0.23 and +0.09 points against effects up to 4.37 — so **the growth column carries
almost no information beyond the turnover column**, and leading with the 4.4-point swing
invites the "this is just transaction costs, obviously" objection the plan itself names as
most likely to kill the paper. And the claimed statistical power of "5–100×" is, on the
plan's own numbers, **0.67× to 13.7×** — two of five comparisons fall below the stated
floor.

### 2. The paper's opening move is false: the anomaly has been explained, by the paper that reported it

The plan opens with *"Conformal Kelly reports, and cannot explain..."* and *"Nobody has
explained it. I have."*

Ryan's paper explains it. From the abstract: *"We read this as a consequence of the job the
interval is doing: when it sizes a position rather than describing a single forecast, the
stability of the width matters more than its local sharpness."* From the conclusion: *"A
structural explanation consistent with the results: a scale estimator consumed by a
nonlinear sizing map is charged for its own estimation variance, so there is an interior
optimum in adaptation speed."*

Two qualifications, both material. Ryan's mechanism is **hedged and largely unmeasured** —
conjectured for six of seven devices, measured for one. And it is **not a turnover
account**; he never connects the growth cost to turnover. So F7's turnover-specific
explanation is not scooped. Only its claim to be the first explanation is.

**This is better for the project than what it replaces.** "Nobody explained it" is an
unfalsifiable universal negative that one reviewer can puncture. "The published explanation
is a different mechanism, and here is the experiment that separates them" is specific,
falsifiable, and more interesting — and it moves the falsified-variance result from a
defensive aside to the centre of the paper.

### 3. C2's coverage theorem has no available proof route on the branch where the novelty is

Two independent depth investigations, reasoning from different directions, converged on the
same conclusion.

Reasoning from **construction**: every known coverage guarantee for a conformal update that
does not fire every round — deterministic round-robin scheduling, exogenous skip
probabilities, bounded update gaps — relies on the suppression being **independent of the
tracked error process**. An evidence-triggered dead-band is by definition correlated with
it.

Reasoning from **proof technique**: a black-box "linearized regret implies coverage"
reduction that looked like it might supply the theorem turns out to re-derive the
Gibbs–Candès telescoping identity verbatim in its own appendix. It imposes the same
unconditional-update requirement under a second name.

So the fork in `audit/CLAIMS.md` C-a resolves, and not in the direction the plan assumes.
**Route (a) — prove low regret, invoke a reduction — is closed.** The only design left
standing is: accumulate `α_t` unconditionally so the telescoping identity is untouched, and
apply the dead-band to the **readout** into the traded position. Its coverage property is
then **inherited from ACI rather than newly proved** — which makes C2 tractable and
modest, and close to a standard no-trade band applied to a conformal interval.

C2's novelty and C2's risk are the same object. The project has to choose which it wants.

### 4. The novelty is NARROW on both claims, and narrower than the plan believes

The plan's inherited finding — that "arXiv returns 0" for the relevant pairings — is
**false**, and four separate antecedents narrow the claim further:

- **Zaffran et al. (ICML 2022) Theorem 3.1** proves ACI's coverage is valid for every step
  size while mean interval **length** degrades **linearly** in it. That is C1's exact
  structure, with length in place of turnover, published four years earlier.
- **"Questioning the Coverage-Length Metric in Conformal Prediction" (arXiv:2601.21455)**
  argues the coverage-length metric pair is insufficient and introduces a metric named
  **interval stability**. F7's framing move is in print.
- **Chopra (1993)**, reproduced as Figure 2 of the very MacLean–Thorp–Ziemba paper the plan
  cites and dismisses, charts **portfolio turnover as a function of input-estimate error**.
  "Moving estimates cause turnover" is a thirty-three-year-old result.
- **arXiv:2607.26547** combines online conformal calibration with an explicit **switching
  cost** in a decision. This session's own sweep returned it and dismissed it in one line
  on its application domain rather than its mechanism.

There is also a contradiction internal to the plan, and it is sharp. C1's thesis is that
*"no coverage-based criterion — marginal, conditional, or adaptive — can select the
adaptation rate"*. **DtACI selects the step size online, by aggregating over a set of step
sizes on a coverage-based criterion — and DtACI is item (iii) in the plan's own baseline
list.** The thesis is refuted by an algorithm the paper proposes to compare against. The
claim has to be restated as a measurement about what coverage-based selection *achieves*,
not as a statement about what it *can* do.

**What survives is real but must be argued rather than assumed:** turnover is a
*variation* functional (`Σ|Δq|`) where every existing result concerns a *level* functional
(`E[L]`); the variation is monetised through a decision with memory; and no coverage
guarantee exists under a movement-penalised update. **The critical caveat is that the
level-versus-variation distinction — C1's entire defence — has never been measured**, and
the obvious test is weaker than it looks. On the plan's own table turnover is already
approximately affine in γ (slopes 67, 78, 86 and 70 per unit γ), which is the same
functional form Zaffran proves for mean length — so monotonicity separates nothing. The
test that decides it is whether `Σ|Δq|` predicts growth *conditional on* `E[L]`. It is
still cheap, and it should be run first.

### 5. A third of the reference list fails, one citation says the opposite of what is claimed, and the deadline is thirteen days away

**7 of 22 references failed at least one check — 31.8 %.** The most serious is not a
metadata slip. The plan calls Gârleanu & Pedersen (2013) "the source of the dead-band
form". That paper assumes **quadratic** costs, derives **linear partial adjustment**, and
writes a sentence specifically to distinguish itself: *"Our trade-toward-the-aim strategy is
qualitatively different from the optimal strategy with proportional or fixed transaction
costs, which exhibits periods of no trading."* C2's method derivation currently claims
descent from a paper that says the opposite. The correct citations are Constantinides
(1986) and Davis & Norman (1990).

Also: conformal PID is dated 2024 and is NeurIPS **2023**; *Conformal Risk Control* is
attributed to "Bates, Angelopoulos et al." when Angelopoulos is first author and Lihua Lei
— a programme-committee member at the target venue — is a co-author; one identifier appears
twice under two descriptions; and one load-bearing citation has no locator at all.

The ML×OR deadline is **2026-09-01 11:59 UTC — thirteen days from this session** — with no
simulator, no results, no draft, and operator sign-off required at three gates. **The
audit's assessment is that the 2026 cycle is not reachable at an acceptable standard.**
That is a judgement about available effort and it belongs to the operator; what the audit
can say is that the premise the target was chosen on — "2 weeks, the central experiment is
already done" — is void.

---

## The finding that is not bad news

**Nothing in this audit undermines the idea.** The conjecture survived every check that was
run. Coverage really is insensitive to the adaptation rate; the adaptation rate really does
have a monotone downstream cost, corroborated independently on real ETF data by Ryan's own
γ sweep; the switching-cost literature really has no notion of coverage, confirmed by
full-text search across four papers; and Conformal Decision Theory's trading experiment
really is zero-cost synthetic GBM, verified against its own text, so the differentiation
from the headline baseline holds.

The problem is not the idea. **The problem is that nothing underneath the idea is currently
load-bearing.** That is a recoverable position, and it is a different diagnosis with a
different remedy from "the idea is in trouble".

---

## Required figures

| Quantity | Value |
|---|---|
| **Orphan numbers** (`audit/NUMBERS.md`) | **12 of 88 = 13.6 %** |
| Numbers reproduced from code | **0 of 88 = 0.0 %** |
| Load-bearing quantities with no displayed table | **5 of 5 = 100 %** |
| **Novelty verdict, C1** | **NARROW** |
| **Novelty verdict, C2** | **NARROW, conditional — and both legs must be carried.** NARROW if the coverage guarantee is delivered; **effectively OCCUPIED if it is not**. Since no proof route was found for the branch where the novelty lives, **the OCCUPIED leg is the live one on present evidence** |
| **Reference-audit failures** (`audit/REFS_REJECTED.md`) | **7 of 22 = 31.8 %** — 1 substantive attribution failure, 1 qualified attribution, 4 metadata, 1 duplicate list entry. The per-check counts sum to 8 because one entry fails two checks; it is counted once |
| **Venue recommendation** (`docs/VENUE.md`) | **ML×OR (NeurIPS 2026, Atlanta)**, with E-values as a genuine second and the calendar decision separated from the venue decision |

### The distinguishing sentences, in full

**C1 — NARROW.**
> Zaffran et al. (ICML 2022) prove that ACI's coverage is asymptotically valid for every
> step size while its mean interval **length** degrades linearly in that step size; F7's
> claim is about the **variation** of the interval path rather than its level — a
> functional that no coverage-based and no efficiency-based criterion measures, and the one
> that a position-holding decision actually pays for.

**C2 — NARROW, conditional.**
> Switching-cost online learning has lazy algorithms with regret guarantees but no notion of
> coverage, and the conformal literature has coverage guarantees but no notion of movement
> cost; F7's contribution is a movement-penalised conformal update that provably retains the
> coverage identity, which no existing work supplies — and the gap is not a free
> composition, because regret bounds are known not to imply coverage adversarially.

---

## What was produced

| Artefact | What it establishes |
|---|---|
| `audit/INVENTORY.md` | Complete file-by-file repository state, regenerable |
| `audit/REPRO_C1.md` | The simulator is absent; all 23 table cells and 7 named claims NOT-EMITTED |
| `audit/RECONSTRUCTION_SPEC.md` | 13 underdetermined choices a rebuild must freeze, with severity |
| `audit/NUMBERS.md` | 88 numbers traced; orphan count; two arithmetic findings from the plan's own table |
| `audit/CLAIMS.md` | Atomic claim ledger plus the five required treatments C-a to C-e |
| `audit/PRIOR_ART.md` | Three sweeps, four amendments, CLEAR/NARROW/OCCUPIED verdicts |
| `audit/REFS_VERIFIED.bib` | 45 entries, every one from a fetched canonical record |
| `audit/REFS_REJECTED.md` | 7 failures with reasons |
| `docs/VENUE.md` | Six venues scored from OpenReview's own deadline records, plus a compliance checklist |
| `docs/GATES.md` | G0–G6 with criteria fixed in advance |
| `docs/OUTSTANDING.md` | Every unresolved item, ranked by whether it blocks G1 |
| `docs/OPEN_QUESTIONS.md` | Eight operator decisions, each a specific answerable question |
| `docs/COMPUTE.md` | CPU-only, with the one condition that would change it |
| `docs/HYPERRESEARCH_REPORT.md` | The research run's seven deliverables |
| `paper/neurips_2026.sty` | Fetched from the official author kit; `sglblindworkshop` confirmed non-anonymous at source |

---

## The three cheapest high-value actions

Stated separately because they are disproportionately cheap relative to what they resolve.

1. **Ask the operator whether `confloor5.py` exists on other hardware.** One question.
   Collapses most of the current uncertainty if the answer is yes.
2. **Email Ryan for `results.tsv`.** His Appendix A offers it "available from the author on
   request", and it almost certainly contains the per-device turnover his paper omits —
   which is the exact data that would settle the paper's central dispute, on real
   multi-asset data, without rebuilding anything.
3. **Run the Zaffran discriminator, in its strict form.** Does `Σ|Δq|` predict net growth
   *conditional on* `E[L]` across the γ grid? Not the weak form — "is turnover monotone in
   γ" — which discriminates nothing, because the plan's own turnover column is already
   approximately affine in γ, the same functional form Zaffran proves for mean length. The
   conditional test is still cheap, and it is the one that decides whether C1's defence
   holds. Far better to know in week one than at review.

---

## Status and next step

**G0 is ready for review.**

No gate in this project has been signed, and none may be signed by an automated session.
`docs/GATES.md` carries the prohibition on every entry. The next session requires the
operator's explicit sign-off on G0 before proceeding, and answers to the eight questions in
`docs/OPEN_QUESTIONS.md` — of which Q1 (does the simulator exist?), Q3 (venue and calendar)
and Q4 (which dead-band fork?) determine most of what the project does next.

### One caveat about this report's own reliability

The research run that produced `docs/HYPERRESEARCH_REPORT.md` was specified with four
independent adversarial review passes and ran one. That single pass returned **twelve
findings — two critical, six major, four minor — and all twelve were applied.** The two
critical ones were a gate ladder that contradicted `docs/GATES.md` on three of six rows and
in the process erased the writing gate, and a novelty verdict that had silently dropped the
OCCUPIED leg of its own two-legged conditional. One major finding was a scope violation:
the report had closed an operator question it was required to leave open.

Those defects were found and fixed. The inference to draw is not that the report is now
clean — it is that **a document whose first serious check surfaced two critical defects has
had one check, not four**, and should be read accordingly. The same caution applies to this
file, which no independent pass reviewed at all.

### Status

This session ran no experiment, implemented no method, wrote no paper section, and made no
strategic decision. It produced findings and stopped.
