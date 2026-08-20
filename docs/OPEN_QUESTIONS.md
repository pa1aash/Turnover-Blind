# Open questions for the operator

Every item marked [OPERATOR INPUT] during the characterisation session, phrased as a
specific answerable question. Nothing here was guessed at and no thread past one of these
was carried forward on the session's own authority.

Ordered by how much the answer changes what happens next.

---

## Q1 — Does `scratchpad/confloor5.py` exist anywhere you can reach?

**The question.** The planning document attributes the C1 table to a file at
`scratchpad/confloor5.py`. Ten search commands across your machine — filename, content
string, the distinctive number `0.8993`, every prior-session scratch directory, and every
retained session transcript — returned nothing (`audit/REPRO_C1.md` §1). No
`scratchpad/` directory exists anywhere under your home directory.

**Answer one of:**
- (a) It exists on other hardware — name the machine or medium; or
- (b) It existed and is lost; or
- (c) It never existed as a file.

**Why it matters more than anything else here.** Under (a), most of the current
uncertainty collapses immediately: the table becomes checkable, the three untabulated
results may be recoverable, and the schedule returns to something like the plan's
estimate. Under (b) or (c), a full rebuild against a frozen specification is the critical
path, every number is unverified, and the "2 weeks, the central experiment is already
done" premise is void. **The audit cannot distinguish these three, and they imply very
different projects.**

---

## Q2 — Do you accept the corrected framing, given that Ryan does offer an explanation?

**The question.** The plan opens with "Conformal Kelly reports, and cannot explain..." and
"Nobody has explained it. I have." Ryan's paper explains it, in the abstract and again in
the conclusion, attributing the effect to estimation variance charged through a nonlinear
sizing map. The explanation is hedged — "consistent with the results", conjectured rather
than measured for three of four devices — and it is **not** a turnover account.

**Answer one of:**
- (a) Adopt the corrected framing: *Ryan proposes an unmeasured variance mechanism; F7's
  zero-cost arm separates the variance and turnover channels and finds the variance channel
  does not transmit.* This is a correction of a published explanation.
- (b) Something else — state it.

**Why it matters.** The audit's assessment is that (a) is **stronger** than what it
replaces: a specific falsifiable disagreement with a named paper beats an unfalsifiable
universal negative that one reviewer can puncture. But it changes the paper's opening
paragraph, its contribution statement, and which result is the centrepiece — the falsified
variance hypothesis moves from a defensive aside to the core of the argument. That is the
operator's call, not the audit's.

---

## Q3 — Venue, and is the 2026 cycle being attempted?

**The question, in two parts.**

**Q3a — which venue?** `docs/VENUE.md` recommends **ML×OR** on merit: the only room that
can evaluate both halves of the paper, and the only one with a journal pathway
(*Stochastic Systems* / *Mathematics of OR* / *Operations Research*). The genuine
alternative is **E-values: From Statistics to ML**, which names conformal prediction
explicitly in its call and is organised by Ramdas and Grünwald, but has no journal pathway
and cannot price the decision-cost half.

**Q3b — this cycle or the next?** The ML×OR deadline is **2026-09-01 11:59 UTC**, thirteen
days from the session date. In that window the project would need to rebuild a simulator
that does not exist, freeze thirteen modelling choices, produce three results that have
never been tabulated, resolve the C-a fork, rebuild a reference list with a 31.8 % failure
rate, and write four pages — with sign-off required at three gates.

**The audit's assessment is that the 2026 cycle is not reachable at an acceptable
standard.** That is a judgement about available effort, which is yours to make. The venue
question has a clear answer; the calendar question does not.

---

## Q4 — Which fork does the dead-band take?

> **RE-POSED 2026-08-19, NOT ANSWERED. Read this block before the question below it.**
>
> The question as written offers two branches: the dead-band on the **decision map**, or on
> the **quantile update**. Session S1 adopted a design in which the movement penalty sits on
> the **width path** — the readout — which is **neither branch**. `docs/GATES.md` G3.1
> records that placement, and G1.8 is marked `superseded` rather than answered.
>
> **This is a reclassification, and the session flags it as such rather than letting it pass
> as a closure.** The placement changed because the manipulated variable changed, not
> because anyone chose between branch (a) and branch (b). If the operator's answer to the
> original question would have been branch (a) — the dead-band on the decision map, giving
> coverage identical to ACI's and a trivial theorem — **then the S1 design is a different
> project from what was intended, and that should be said now rather than at G3.**
>
> **What remains genuinely open, and is `Q7` below:** the movement penalty's functional form,
> L1 (proportional, dead-band) or L2 (quadratic, linear partial adjustment). G3.4's
> tractability depends on it.
>
> > **RESOLVED 2026-08-20 by session S4 — see Q7 below.** The sentence above is kept as the S1
> > record. The form is no longer open and was never a preference: it is R3b's result restated.
> > G3.4 is retired with G3.
>
> **The question below is the original text, preserved unedited.**


**The question.** C2 adds a cost-aware dead-band. The plan is inconsistent about what the
dead-band acts on, and the two readings are different projects.

- **(a) On the decision map.** Run ACI untouched; threshold between the interval and the
  traded position. Coverage is *identical to ACI's*, so the theorem is immediate and
  trivial; turnover is bounded by construction. The method is, in substance, a standard
  no-trade band applied to a conformal interval — defensible, it will work, and a reviewer
  will call it a contribution to practice rather than a theorem.
- **(b) On the quantile update.** The interval itself becomes lazy. Coverage is genuinely
  at risk, because the ACI guarantee is a telescoping identity that a threshold breaks. The
  theorem is hard and unproved. **This is where the novelty is.**

**Why it must be decided before implementation, not during.** C2's novelty and C2's
principal risk are the same object. Under (a) the paper is C1 plus a practical device;
under (b) it is C1 plus a theorem that may not exist. The page budget, the journal
nomination and the STOP condition all follow from the answer.

**One fact that bears on it, found this session:** Andrew et al. (COLT 2013) Theorem 7
gives a **one-dimensional** exception to the switching-cost impossibility, and ACI's state
`α_t` is one-dimensional. So under fork (b) the defensible claim is sublinear regret with
a slowly growing competitive ratio — not unqualified dominance, but a real and citable
position.

---

## Q5 — Which MacLean–Thorp–Ziemba work did you mean, and does its content still serve?

**The question.** The plan cites "MacLean, Thorp & Ziemba" with no year, title or
identifier — the only load-bearing citation in the document with no locator. It has been
resolved, provisionally, to "Good and bad properties of the Kelly criterion" (2010), a
chapter in the 2011 World Scientific handbook.

**Confirm or correct.** And note what reading it produced: the paper warns about
sensitivity to errors in the **mean**, citing Chopra & Ziemba (1993) for a **20:2:1**
importance ratio between errors in means, variances and covariances. A conformal interval
supplies a **scale** estimate — the weak channel. The plan describes MTZ as being about
"noisy scale estimates", which is not what it says.

**The consequence either way:** falsifying the scale channel is easier than the plan
thought, and correspondingly less impressive.

---

## Q6 — Kelly fraction, leverage cap, and drift: known or estimated?

**The question.** `audit/RECONSTRUCTION_SPEC.md` R6 and R7. The position map needs a Kelly
fraction λ, a leverage cap, and a decision about whether the drift `μ` used in the position
is the true value or an estimate. None is stated anywhere in the plan, and all three change
the answer.

**Specifically:**
- **λ:** Ryan uses κ = 0.15 — a very fractional Kelly. At that fraction the overbetting
  channel is close to invisible, which is exactly the objection a Kelly-literate reviewer
  will raise against the falsified-variance result. Match Ryan, or run full Kelly where the
  competing channel is strongest, or both?
- **Leverage cap:** Ryan uses a gross cap of 2.0 with per-asset winsorisation at ±0.75. A
  cap truncates the very jitter the paper measures. Capless, capped, or both?
- **Drift:** true `μ` isolates interval jitter as the only moving part. An estimated `μ̂`
  adds a second noise channel and reopens the estimation-error explanation the paper claims
  to have ruled out.

---

## Q7 — L1 or L2 movement penalty? — **CLOSED**

> **CLOSED 2026-08-20 by session S4, agent K1 — resolved by measurement, not by operator
> decision.** This question is not an [OPERATOR INPUT] and never should have been carried as
> one. It is `docs/FRAMING.md` §2.2c's R3b restated. **The original text below is preserved
> unedited**; read it as the record of how the question was posed, not as a live choice.
>
> **What closes it.** li2025o2cp (arXiv:2508.13362) **Corollary 2** proves that a predictable
> modification of the deployed Conformal PID threshold **retains** Proposition 2's bound while
> it stays inside a ball of radius `μ_t(b/2 − |q̂_t|)`. The **L1 (dead-band) form on the
> completed threshold is exactly the family that leaves that ball**, and this project measured
> where: the law is
>
> > **`τ* = sup_x r_t(x) + sup_t q̂_t − b/2`; bands with `τ ≤ τ*` cover, and the failing set is
> > `(τ*, ∞)`, open at the left.**
>
> Past `τ*` the deployed threshold is pinned below the adversary's reachable score range, the
> loop stops closing, `|E_t| = (1−α)t` grows linearly and realised miscoverage is **`1.000000`**
> against `α = 0.1` — with **`frac_saturated = 1.0000`**, so condition (4) holds on every single
> round and what fails is Proposition 2's *other* hypothesis, that the threshold closing the
> loop *is* the integrator's output. **So L1 is not one of two styles to pick between; it is the
> perturbation family whose failure is the paper's result.**
>
> **And L2 is not thereby certified — this is not a softening, it is the finding.** At the
> harness's null scorecaster the L2 arm (EMA `w = 0.999`) **forfeits the rate** — `max|E_t| =
> 623.70` against a Proposition 2 bound of `14.8155` at `T = 10⁶`, 42× — while **keeping**
> coverage at `0.100035`. At the **equally legal** constant scorecaster `q̂ ≡ −b/2`, Corollary 2's
> radius is `0` and the **L2 arm returns `1.000000` as well**, alongside every dead band measured
> there; at `q̂ ≡ +b/2` the dead band that fails at the null scorecaster **covers**, at
> `0.100010`. The boundary is a property of the **(saturator, scorecaster) pair**, which is
> exactly why the paper's claim is a **tightness statement about Corollary 2's radius** and not a
> blanket "L2 is safe".
>
> **Evidence.** `results/forfeit-variations-20260820T101445Z.json` (rows
> `scorecaster_const_minus_b_over_2` / `ema_w0.999` and `.../deadband_tau*`;
> `scorecaster_const_plus_b_over_2` / `deadband_tau1.5`; `boundary_law`),
> `results/forfeit-20260820T063045Z-83747c45.json`, `results/forfeit-20260820T063132Z-83747c45.json`;
> code `src/forfeit.py`, `src/test_forfeit.py`; `docs/FRAMING.md` §2.2c;
> `docs/GATES.md` G7.9. The paper states it in `paper/sections/setup.tex` and
> `paper/sections/forfeit.tex`.
>
> **Consequence, and it binds every document here.** No residual dead-band framing may survive
> as a **design recommendation** in `paper/` or `docs/`. The dead band appears only as the object
> of study whose failure is characterised, or as a historical record marked as superseded. Its
> original motivation is doubly dead: S1 found the Gârleanu–Pedersen attribution wrong (they
> derive L2 from quadratic costs), and S3 measured the L1 form's failure.
>
> **What this does NOT close.** OI-2 stays superseded and unanswered. Q3 (venue) stays
> `[OPERATOR INPUT]`. Q8 (co-authors) stays open. **No gate is signed by this.**

**The question.** The plan specifies an L1 movement penalty, which gives soft-thresholding
and a dead-band, and attributes that form to Gârleanu & Pedersen (2013). **That
attribution is wrong** — G–P assume *quadratic* costs and derive linear partial adjustment,
and explicitly distinguish their solution from proportional-cost strategies "which exhibit
periods of no trading" (`audit/REFS_REJECTED.md` §1.1).

The mis-citation concealed a real design choice:

- **L1 (proportional):** dead-band, soft-threshold, matches real proportional trading
  costs, correct citations are Constantinides (1986) and Davis & Norman (1990).
- **L2 (quadratic):** linear partial adjustment toward a target, smooth and differentiable,
  much easier to analyse, and *this* is what Gârleanu–Pedersen actually derive.

Which does C2 use? The L2 route is analytically far more tractable and may make the C-a
theorem reachable, at the cost of losing the dead-band that gives the paper its name.

*(End of the original S1 text. The answer is in the CLOSED block at the top of this question,
and the paper's name is no longer the dead band's — see `docs/FRAMING.md`'s running header.)*

---

## Q8 — Author management and co-author sign-off

Out of scope for this session by instruction, and recorded so it is not lost: the paper has
co-authors, the venue is non-anonymous, and G6.2 requires co-author approval of the
submitted version. No co-author has been contacted or named in this repository.

---

## Q9 — Semantic Scholar API key (added S1, 2026-08-19)

**The question.** `SEMANTIC_SCHOLAR_API_KEY` is not present in the session environment,
and the anonymous pool returned HTTP 429 on every **unthrottled** call this session —
through the direct API, through the connected Semantic Scholar server, and through a
server-side fetch from a different network egress. The 429 is therefore a property of the
anonymous quota, not of this machine's address. It is a rate limit, not a wall:
**incremental backoff (4 s → 40 s, ~25 retries) clears it**, which is how the screen below
was in fact run.

**Consequence — superseded, S1 2026-08-19.** The screen was subsequently run **without a
key**, using incremental backoff against the anonymous pool, returning **659 unique citing
papers** across ACI, DtACI, conformal PID and SAOCP. G1.1 is therefore satisfiable on the
present environment and O1 is closed. A key would still make the screen faster and
re-runnable on demand, so the question below is worth answering, but nothing is blocked on
it. Note also that the OpenAlex fallback prescribed above would have produced a **false
negative**: OpenAlex's ACI record carries `cited_by_count = 27` against Semantic Scholar's
557, a 95 % miss.

**Answer one of:**
- (a) A key exists / can be obtained — supply it and the screen is re-run properly in S2;
- (b) No key is available — then nothing is blocked: the backoff route already produced the
  screen, and it is the documented fallback.

**Why it is not closed here.** Applying for a key is an action taken in the operator's
name against a third party. The session records the question and runs the fallback.

---

## Q10 — Ryan email: address and dispatch (added S1, 2026-08-19)

`docs/RYAN_EMAIL_DRAFT.md` is written and ready. The session does not hold a contact
address for Robert Jacob Ryan (ACS Athens) and does not send mail on the operator's
behalf. **Palaash sends this himself.** It is the longest external latency in the
project; everything else can be redone, a reply cannot be hurried.
