# Session S3 — the re-scope, the correction, and the paper

**Date 2026-08-20.** Nine agents across five waves — H1–H5 in parallel, then J1/J2/H6, then two
mandatory critics, then one applier. All returned. **One simulator written and extended; no
experiment beyond it. No gate is recorded as signed. No `[OPERATOR INPUT]` is answered.**

---

## 1. The correction survived the adversarial pass. That is the paper.

> **R3a survived, and it survived on the evidence rather than on the absence of a search.**
> Wave 4's adversarial critic hunted it on four surfaces and found **no occupant of the
> correction**. OpenReview's *entire* corpus returns four records for "scorecaster". There is no
> v2 of the corrected paper quietly fixing the sentence — and the sentence **survives verbatim in
> the refereed AAAI 2025 camera-ready, printed page 18443**, which the critic fetched.
>
> **But it survived smaller than it was briefed, and it was cut down by this session's own wave 1,
> not by the critic.** The *derivation* is already in print twice — **arXiv:2508.13362 Corollary 2**
> folds a bounded predictable perturbation into the scorecaster slot in Conformal PID's own
> notation and concludes *"The CPID saturation result therefore applies"*, and arXiv:2410.13115v2
> is an independent second instance. **And the first and last authors of arXiv:2508.13362 are the
> authors of arXiv:2412.18144, the paper that prints the opposite.** The record contains both the
> false claim and its refutation, by the same people, unjoined.
>
> **So the paper claims neither the placement nor the derivation.** It joins the halves, names the
> aside for what it is, and says so. That is a genuine service and a smaller claim than the brief
> wrote.

## 2. The headline was damaged, and repairing it made it honest

R3b as wave 3 printed it — *a dead band on the completed output loses long-run coverage for
`τ > b/2`* — **was wrong.** `b/2` is the **null-scorecaster** special case. The law, bisected by
the critic at 15/15 points and **verified independently by the orchestrator at 31 of 32**, is

> **`τ* = sup_x r_t(x) + sup_t q̂_t − b/2`.**

Both constant scorecasters `q̂ ≡ ±b/2` are legal under Theorem 1's *"any sequence of numbers in
`[−b/2, b/2]`"*, and both move the boundary. Measured from committed code
(`results/forfeit-variations-20260820T101445Z.json`, `T = 10⁶`):

| configuration | dead band `τ = 1.5` | EMA `w = 0.999` |
|---|---|---|
| `q̂ ≡ 0` (wave 3's) | **1.000000**, `max\|E\| = 900,000` | 0.100004, `623.70` |
| `q̂ ≡ +b/2` | 0.100010, `11.20` — **covers** | 0.099999, `365.40` |
| `q̂ ≡ −b/2` | **1.000000** | **1.000000** — an arm wave 3 printed as covering |
| saturator level `4b` | 0.100000, `4.60` | 0.100002, `120.60` |
| **ACT23's tangent** | 0.100001, `15.10` — **covers** | 0.100019, **`20.10`** |

And the failing set is **unbounded above**, not `(b/2, b]`: `τ = 2.0, 2.5, 3.0, 5.0` all return
`1.000000`.

**Two consequences the paper now states.** The measured boundary at `μ = 1, q̂ ≡ 0` is **exactly
O2CP Corollary 2's admissible radius** `μ_t(b/2 − |q̂_t|)` — so the measurement shows **the conceded
result is tight**, not that a new boundary was found. And under **ACT23's own tangent integrator,
which they state they use "in all our experiments"**, the failure does not arise and the headline
`623.70` falls to `20.10`. A limitation that previously read *"nothing here says what that would
do"* now says what was measured. **That is the single most important honesty fix in the session.**

## 3. R3c: the bridge lost its negative claim entirely, and is better for it

Wave 1 narrowed the four-way disconnection to one cell, L1×L4. **Wave 2's own agent falsified that
cell.** Semantic Scholar's *citations* endpoint for Kalai–Vempala returns **875 citing works, three
of them online conformal** — including **IPOC, which this paper itself cites**. H5 had measured
*outgoing* references and found the cell empty; H6 measured *incoming* citations and found it
occupied.

> **A negative claim is a claim about an instrument, and one direction of one instrument is not
> the literature.**

The paper now prints **"We claim no disconnection"** and keeps the payload, which never needed it:
four fields name one quantity many ways, and the object that settles its validity sits in one of
them. The name count is dropped in favour of the table's own caption, because the printed "six"
was contradicted by that caption, which names ten.

## 4. What was dropped, closed, and corrected

**R1 is gone** — market model, position map, Kelly, transaction costs, turnover, basis points, net
log growth, the Ryan replication. Verified **absent from the typeset PDF**, not merely from the
sources. That deletion is what made four pages reachable.

**O42 is CLOSED as OCCUPIED.** It is integrator anti-windup with a feedforward path; the
free-until-saturation dichotomy is that field's *problem statement*, the (authority, severity)
boundary exists in three forms, and `Σ|Δq_t|` is the discrete-time IACER. **O20 is CLOSED** — the
TS-LIMITS call that "defeated every retrieval attempt" was one `curl` of the `content.js` its own
page names. **O43 is discharged** for every row the paper prints.

**Four corrections of the project's own record**, each found inside this session: R3c's last cell;
R3b's boundary; the `τ = b/2` endpoint (an agent corrected the orchestrator and was right); and
**Duerst et al.**, which S2 made a load-bearing witness for a calendar-time movement constraint and
which the full text shows is monotonicity in **forecast horizon**. Correcting the last of these
**removes the nearest known threat to R3b**.

## 5. Honest list of what this session did wrong

1. **The session committed the failure it was auditing, and it is the second consecutive session to
   do so.** H6's falsification, the denominator correction and the endpoint error lived **only in
   gitignored `research/`** while `docs/FRAMING.md` and `docs/GATES.md` — *both written this
   session* — kept asserting the falsified claim. `H6`, `875` and `Kalai` returned **zero hits
   across all of `docs/`**. Caught by the instruction critic, fixed at wave 5.
2. **Waves 1–4 were not committed or pushed as they completed**, against a standing instruction.
   `HEAD` sat at S2's last commit for four waves. Recorded as `O59` rather than quietly fixed.
3. **The wave-5 numbers nearly shipped untraceable.** The corrections to the headline came from an
   agent's scratch files in an ignored directory. The applier disclosed it; the simulator was
   extended so they come from committed code and land in `results/`.
4. **Two orchestrator figures were wrong and were corrected by agents or critics**: the `[b/2, b]`
   endpoint, and a duplicate anchor inflating the cross-citation denominators (900→862, 264→226).
   A third, the citer count, was wrong in the other direction — **three, not two**; the
   orchestrator's scan keyed on title text and missed a content-classified case.
5. **No wave-2 checkpoint was written at wave 2.** Written at wave 5 and labelled as such.

## 6. What is not reached

- **Google Scholar ran zero queries.** Eight probes, every one a 429 or a 3,322-byte `/sorry`. It
  is host/IP-blocked and the headless policy does not unblock it. **It has now defeated two
  sessions**, and it is the surface that produced both of S2's decisive hits. `O45` stays open;
  the 50-query battery is armed.
- **DiVA is unreachable by anything** — TCP connect fails on four hostnames. **IPOC's reference
  list** is ACM-closed and Wayback archived the interstitial itself, so the *substance* of its
  Kalai–Vempala citation is unverified, though the citation edge is measured.
- **`[0.821, 0.979]` at `T = 2500`** remains the one untraced number in the body: reproducible, but
  only with two constants the paper does not state (`O56`).
- **The tangent integrator should be a first-class arm, not a caveat** (`O53`).

## 7. Venue and gates

**Recommendation only, and the choice stays `[OPERATOR INPUT]`: E-values**, deadline
**2026-08-29 23:59 AoE**, single-blind as of 2026-08-14 after three flips in 17 days. TS-LIMITS is
4–7 pages, double-blind, 09-05. **The body is exactly 4 pages and builds clean under both**, so the
option is preserved — but it is one-directional and expires on the 29th.

**G7** is written with twelve criteria and states its own weakness: it was written *after* the runs
existed, so it cannot claim G2-pre's pre-registration discipline. **G2, G2-pre, G3 and G4 are
retired with their criteria kept in full.** **OI-1 and OI-2 are SUPERSEDED, not answered** — and
wave 1 handed OI-1 a hard new fact the operator should see: **the dead band is the L1 form, and it
is exactly the family that fails.**

**Nothing is submitted.**
