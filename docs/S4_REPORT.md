# Session S4 — retitle, resize, close

**Date 2026-08-20.** Six agents across six waves: four in parallel (K1–K4), then the orchestrator's
merge, then both mandatory critics (N1, N2). All returned. **No new experiments. No new retrieval
fronts except the title collision check. No gate is recorded as signed. No `[OPERATOR INPUT]` is
answered except OI-1, which turned out not to be one.**

Five commits, one per wave, each pushed. A connectivity failure cut the session at the wave-3/wave-4
boundary; nothing was half-written, and the four completed waves were already committed.

---

## 1. The title, and why it changed twice

**`Where the Admissible Radius Binds: a Correction and a Measured Boundary in Online Conformal
Prediction`**

Wave 1 proposed and wave 2 applied **"The Admissible Radius Is Tight"**. Wave 4's adversarial critic
overturned it on the paper's own numbers. Corollary 2's radius `μ_t(b/2 − |q̂_t|)` does not depend on
the saturator; the measured edge `τ*` does. At `μ = 1`:

| setting | Corollary 2's radius | measured | verdict |
|---|---|---|---|
| null scorecaster, minimal saturator | 1.0 | `τ = 1.000` covers, `1.001` fails | **tight** |
| `q̂ ≡ −b/2` | 0.0 | `τ = 0.5` fails | tight, degenerate |
| `q̂ ≡ +b/2` | 0.0 | `τ = 1.5` covers | **loose** |
| saturator level `4b` | 1.0 | `τ = 1.5` covers | **loose, ≥1.5×** |
| ACT23's tangent integrator | 1.0 | `τ = 1.5` covers (`0.100001`) | **loose, ≥1.5×** |

The last row decides it. The paper itself prints, in bold, that the tangent integrator is the one
Conformal PID's authors report using in all their experiments — so the flat title asserted as
headline a property that fails at the deployed configuration and holds at one corner of the harness.

"Tight" is existential in standard mathematical usage, and on that reading the flat title was
defensible; that was the orchestrator's reason for accepting it at wave 2. It does not survive the
practical test: **a referee meets the title 130 words before the qualifier that repairs it.**
"Binds" locates the claim instead of asserting it, and locating is what the paper actually does — it
says where the condition binds *and* where it does not.

Collision-checked headlessly on arXiv's classic **full-text** index (`searchtype=ft`), calibrated in
both directions in the same session so a zero is known to be a zero: nonsense token `2,844 B`
("No Results"); positive control `"conformal prediction"` `12,337 B`, 258 hits; **`"admissible
radius binds"` `2,843 B`, a real zero.** Records under `research/S4/records/title/`.

Changed in `paper/main.tex`, `README.md` and `docs/FRAMING.md`'s running header. **No GitHub
repository description is set** (`description: null`), so there was nothing to change there. The
repository name `Turnover-Blind` is historical and is kept so existing clones and links keep working;
`README.md` says so.

## 2. The contributions list, in full

The paper has no `\paragraph{Contributions}`; its contributions surface is the abstract plus the two
`\paragraph` leads of the introduction. Printed in full, as built:

> **Abstract.** Conformal PID states long-run coverage for an arbitrary bounded scorecaster, and a
> published corollary retains its rate under any predictable perturbation of the deployed threshold
> inside an admissible radius. The opposite reading is in print too, under overlapping authorship,
> and acted on. **We make two claims.** The record holds both halves and we join them, conceding
> placement and derivation by name. And at the null scorecaster the corollary's condition is tight:
> a legal `L₁` dead band on the *completed* threshold leaves that set past
> `τ* = sup_x r_t(x) + sup_t q̂_t − b/2`, which is the published radius itself there, and past it
> realised miscoverage is `1.000000` against `α = 0.1` while saturation fires every round. Leaving
> the set costs coverage and not only the rate: partial adjustment there overruns Proposition 2's
> bound `42×` at `T = 10⁶` and still covers, `0.100035`. The edge belongs to the saturator–scorecaster
> pair, not to the readout, and elsewhere the condition is sufficient only: under the equally legal
> `q̂ ≡ +b/2` the failing band covers, and under `q̂ ≡ −b/2` both the failing band and partial
> adjustment at `w = 0.999` return `1.000000`.

> **First: the record carries a claim and its refutation, and this paper joins them.**
> **Second: that admissible set has an edge, and the condition there is tight.**

**Framing constraint, honoured and checked.** Nothing anywhere says or implies that Li & Rodríguez
erred. The framing is that the published record contains both the claim and its refutation,
unjoined, and this paper joins them — ordinary self-correction under overlapping authorship, said
about the record and never about the people. Greps for `erred`, `were wrong`, `was wrong`,
`a mistake`, `mistaken`, `incorrectly`, `error by` over typeset prose: **0**, across the whole paper
and not only where it was drafted.

**There is no third claim.** R3c — the four-literature bridge — is demoted to descriptive related
work. Its negative claim was falsified inside S3 by that session's own agent, and S4 deleted the
machinery that carried it, including the bolded "We claim no disconnection": a printed denial of a
claim the paper does not make is the last residue of the contribution and points a referee straight
at it. Absence-claim greps over `paper/` return **0** on all twelve patterns.

## 3. OI-1, closed as a finding

`docs/OPEN_QUESTIONS.md` Q7 / `docs/PROTOCOL.md` OI-1 was never an operator preference. It is R3b
restated, and it is now written into the paper where L1 and L2 are defined:

> *The dead band (L1) is not a stylistic alternative to the partial-adjustment (L2) form*; it is the
> specific perturbation family whose failure §3 characterises. Neither is safe by construction: L2
> forfeits Proposition 2's rate while covering, L1 past `τ*` loses coverage, and at the legal
> `q̂ ≡ −b/2` both lose it. What is tight is the radius, not a form.

**The honest qualifier is load-bearing and was added by the orchestrator against the brief's own
wording.** The brief said L2 "stays inside the admissible radius and therefore retains the sublinear
bound". That is true at the null scorecaster and at `q̂ ≡ +b/2`. It is **false** at the equally legal
`q̂ ≡ −b/2`, where the radius is `0` and the L2 arm at `w = 0.999` also returns `1.000000`. Writing
the unqualified version would have shipped a claim a referee could break with the session's own data.
Every "primary treatment pending operator choice" hedge is resolved across `PROTOCOL`,
`OPEN_QUESTIONS`, `OUTSTANDING`, `GATES` and `FRAMING`, in house style — original kept, dated block
appended. **No dead band survives anywhere as a design recommendation.**

## 4. The claim-drift check: written, run, and it found something

`tools/check_claim_drift.sh` (49 executable lines). It indexes what a session **wrote** — agent
JSONs, checkpoints, `results/` — deliberately excluding fetched third-party text, pulls the
load-bearing lines from `docs/FRAMING.md` and `docs/GATES.md` that name the session, takes up to four
distinctive tokens from each, and reports `UNSUPPORTED` or `CONTRADICTED`.

**Validated retrospectively before being trusted.** Run against S3 it independently flags
`docs/GATES.md` G7.9 against S3's own `F1-adversarial.json` — the same drift wave 0 had found by
hand.

**What it found on this session's own work.** One finding, **partly real**. `docs/FRAMING.md` §2.2b
(iii) claimed *"it holds for nine of ten smoothed arms"* — scoped to the null scorecaster and saying
so nowhere, carrying the superseded `τ > b/2`, and with an arm count the resize had made stale.
**Fixed in the wave that wrote it**, which is the entire point.

**The alarm still fires on that line, and that is recorded rather than silenced.** The matcher pairs
a numeric token with any falsifying word on the same artefact line, and the artefact legitimately
contains *"refutes 'L2 retains the bound'"* while reporting a refutation of a **different** claim. By
wave 4 it was also matching the instruction critic's report **quoting the tool's own output** —
self-referential, and the clearest possible demonstration that this is a smoke alarm and not a proof.
Dispositioned as a false positive in `research/S4/patch-log.json`, which is what the rule requires.

**Its real limitation, found by the instruction critic and worth more than the tool.** The check is
blind to drift in prose that carries no number. It did **not** flag the two further unscoped copies
of that same claim at `FRAMING` §2.2c and `GATES` G7.9 — the O51 shape, inside the same document,
twice. Those were caught by a critic, not by the tool. **The rule is worth keeping; it is not
sufficient on its own.**

The standing rule is in `docs/PROCESS_NOTES.md` with all three prior instances and their locators
(S1's missed A6 route, S2's conservation law, S3's O51), and as a criterion attached to every gate in
`docs/GATES.md`.

## 5. Compliance under E-values

Walked item by item into `docs/VENUE.md`, ten rows, each evidenced against a record fetched
**headlessly by curl** and saved with its sha256 this session. **No GUI browser was used in any wave**
— S3's venue facts had one headed-Chrome route, and S4 re-verified them headlessly rather than
inheriting them.

- **Deadline CONFIRMED unmoved: 2026-08-29 23:59 AoE.** The OpenReview invitation's `tmdate` is
  2026-08-15, i.e. unmodified since before S3 read it. OpenReview enforces `duedate` 2026-08-30 13:00
  UTC — **61 minutes later than the published AoE time**. Plan to the published time.
- **Page limit: up to 4 pages excluding references. Met exactly** — References is the **first content
  on page 5, offset 0**, under both venue options.
- Anonymity **single-blind**, `\usepackage[sglblindworkshop]{neurips_2026}`, verified in the style
  file and in the rendered PDF, not just in the call. **Volatile: it changed three times in
  seventeen days. Re-read within 24 hours of submitting.**
- Non-archival. **No paper checklist required** — verified by enumerating the OpenReview form schema.
- Organizing committee retrieved; **no conflict** with this paper's subject.
- **Two items are not clean, and are recorded as unclean rather than inferred:** the venue publishes
  **no dual-submission rule** (zero occurrences of `dual`, `concurrent`, `preprint`, `arXiv`), and the
  **OpenReview-profile advisory date, 2026-08-15, has already passed**. Both are operator actions.

**Both venue options build clean at exactly 4 body pages**, 0 TeX errors, 0 undefined citations,
0 undefined references, 0 overfull boxes, 0 LaTeX warnings, 0 bibtex warnings, 3 underfull hboxes,
correct anonymisation each way. **The open venue question does not block a clean build.**

## 6. What the critics found, and what it cost

Both landed hits that changed the paper rather than polishing it.

1. **The body was not four pages.** Wave 2 recorded *"References first content on page 5, offset 6"*
   and read it as compliant. Those six lines were **body text on page 5** — the body was four pages
   plus four lines, over E-values' ceiling, asserted in three tracked places. The instruction critic
   caught it by reading page 5 instead of trusting the field. **The operative test is now recorded
   everywhere as "References is the FIRST content on its page"; a bare page count and a non-zero
   offset both hide an overrun.**
2. **The title overclaimed** — §1.
3. **Two factual errors in the measurement section**, both verified against `results/` before acting.
   The paper attributed `623.70` and `70.80` to the tie-rule convention; `623.70` **is** the primary
   regime's own figure and the lever is the adversary's `ε`, not the counting convention. And *"the
   endpoint covers"* is decided by a strict inequality at an **exact float equality** — the one row in
   the entire record where the adversary's convention changes the answer (`0.100030` / `1.000000` /
   `0.000000` across three regimes), previously undisclosed and now printed as what it is.
4. **"No bisection is booked" was false.** An eleven-point `τ` grid is committed and the paper prints
   its result. **The orchestrator's own error from wave 2**, in three places.
5. **The drift check's finding was fixed in one place and survived in two others** inside the same
   governing document.
6. Plus corrections to a printed travel value (`1,024` → `1,023`), an over-scoped "every dead-band
   configuration", a false "both readouts" at form level, a `\ref` that broke `G7.3`'s query-family
   requirement, and a universal quantifier (*"every natural name is taken"*) that the term-based
   forbidden-construction scan **structurally cannot see**.

**Failed attacks, reported as robustness signal.** The boundary law itself is not breakable: the
critic recomputed `τ*` over **all 250 dead-band rows in every committed file, all regimes, all
horizons**, and found no configuration with `τ ≤ τ*` that loses coverage and none with `τ > τ*` that
keeps it. The decision-cost register is genuinely gone (22 patterns, every survivor a required
concession). The harness description matches the harness — 54 of 55 Table 1 cells reproduced exactly.
The Li & Rodríguez framing is clean everywhere. And the i.i.d. control turned out to be **stronger
than the paper claimed**: it is a closed-form, adversary-free confirmation of the mechanism
(threshold pins at `b − τ = 0.5`; uniform scores give `P(s > 0.5) = 0.25` against a measured
`0.249376`), which the paper had been printing as a retreat. It now says so.

**One build hazard, recorded so it is not reintroduced.** pdftex cannot split a hyperref link across
a page. After the wave-4 edits the page 2/3 break landed inside *"Li et al. [2025, Corollary 2]"* and
the build died outright with `! This can't happen (pdfvlistout)`, producing no PDF. That citation is
now wrapped in `\mbox`, with the hazard noted in the file headers.

## 7. What remains

Short, as intended.

- **The venue is `[OPERATOR INPUT]` and expires.** 9 days remain as of 2026-08-20. Two sub-items need
  the operator: the **OpenReview profile** (advisory date already passed) and, only if preprinting or
  dual-submitting, **one email** to the workshop about the unstated dual-submission rule.
- **`O52`'s remaining leg:** the `τ*` edge is *located* only at the null scorecaster, by the
  eleven-point grid. The other four settings are bracketed at three widths. Closing this needs a
  booked bisection per setting — a new experiment, which this session was instructed not to run.
- **`O45`:** Google Scholar is host-blocked and has now defeated three sessions. Recorded as an
  instrument gap, never as a measured zero.
- **`O46`:** arXiv:2410.08852, "intermittent quantile tracking", is still unread and is the nearest
  known neighbour to the measurement.
- **Anonymity volatility** at E-values — re-read the call before submitting.
- One accepted critic point not acted on: of the 19 configurations, most test the *sufficiency*
  direction, which is prior work. The necessity direction rests on the eleven-point grid. The paper
  states the grid; the count is not inflated to compensate.

## 8. Would I submit this?

**Under E-values, if the venue question were answered today: yes, with one caveat that is the
operator's to weigh, not mine.**

What supports that: the body is exactly four pages under both options with a clean build; every
measured number traces to a committed `results/` JSON, and the four that did not are deleted rather
than footnoted; the two claims are stated in a form a referee can check; the concessions are printed
by name rather than buried; the boundary law survived an adversarial recomputation over every
committed row; and the paper now states its own weakest points — the single seed, the
convention-dependent endpoint, the one located edge — in the text rather than in a reviewer's report.

The caveat: **this session found two of its own errors late, and one of them was a compliance failure
it had asserted as met in three places.** The page overrun was caught by a critic in the final wave,
not by the wave that made the claim. That is the third consecutive session in which a tracked
assertion outran its evidence, and the tool written this session to stop it is demonstrably blind to
the class of drift that carries no number. **What I would want before submitting is not more work on
the paper but one independent read of the built PDF by the operator**, specifically checking the
abstract against §3 and the page-5 boundary — because the failure mode this project keeps repeating
is exactly the one an author's own eyes catch and an automated check does not.

**Nothing is submitted. No gate is recorded as signed. The venue remains `[OPERATOR INPUT]`.**
