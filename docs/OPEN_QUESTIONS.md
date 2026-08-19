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

## Q7 — L1 or L2 movement penalty?

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
