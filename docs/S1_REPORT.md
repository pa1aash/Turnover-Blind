# S1 report — prior-art closure and framing lock

**2026-08-19.** Seven retrieval agents, three synthesis agents, one patch applier, two
critics. No experiment was run, no simulator was written, no gate was signed.

**Read `docs/FRAMING.md` before acting on anything here.** This report says what happened;
that file says what the project now claims.

---

## The five findings that most change what S2 does. Worst news first.

### 1. The first claim was occupied, and the paper that occupies it uses none of our words.

**Van Belle, Wen, Verbeke & Pinson, "Stabilizing distribution-free probabilistic
forecasts", arXiv:2605.28531, 27 May 2026.** Read in full and independently by two agents.
It scores Q1 ∧ Q2 ∧ Q3 on the occupancy rubric and pre-empts Q4 verbatim.

Its §2 builds a stable and an unstable forecaster with identical bias variances and
identical bias magnitudes, differing only in the **sign** of the bias recursion, so every
marginal functional coincides by construction. Table 2 verifies it — CRPS 2.91/1.43/0.83
against 2.91/1.44/0.83, "indistinguishable in terms of forecast quality". The varied
quantity is the Wasserstein distance between consecutive forecast updates, 2.00/1.00 against
6.00/3.00. It is priced through a newsvendor with an incumbent order, charged to add and to
cancel, **retain free**, giving +0.83 % to +3.49 % profit, and a "procrastination" arm that
never revises shows **+0.00 %** — a placebo isolating the movement channel. And it draws the
moral: instability "may go unnoticed if forecasts are evaluated solely from a forecast
quality perspective".

**C1′ as worded should not be submitted.** That is stated plainly, and the session did not
soften it.

### 2. The design change that made the claim identifiable is the same change that made it occupied.

The abandoned design varied ACI's adaptation rate γ. Its recorded fatal risk was that
`Σ|Δq|` might track `E[L]` across the γ grid. Matched-width removes that by construction —
and there is now external proof the change was necessary: **Genov et al. (*ESWA* 2026) is
the γ design, in energy systems, and it fails exactly there.** Its §4.4 says level and
variation move together across its arms, and its attribution is a cross-arm correlation
table.

But holding a level functional fixed while varying a path functional and pricing the
difference through a decision with an incumbent state **is Van Belle §2's design**.

> **The new design is more exposed than the old one, and it is more exposed because it is
> better.** Reverting to γ restores a documented identification failure and moves the attack
> from novelty to methodology, which is worse.

### 3. R1's two stated survival arguments were destroyed by the adversarial critic, fourteen years early.

The session's own synthesis rested the residual measurement claim on exactly two
distinctions from Van Belle: that the matched pair is *(realised coverage, mean interval
width)* specifically, and that the producer is real rather than synthetic.

**Both are false.** **Pinson & Girard, *Applied Energy* 96:12–20 (2012)** compares three arms
on a **real** producer that share the **full marginal predictive distribution** — hence
coverage and mean width exactly, a strictly stronger control that subsumes the pair — varies
only temporal dependence, and does it inside the "sharpness subject to calibration" paradigm
of Gneiting, Balabdaoui & Raftery, which is this project's matched pair under its
meteorological name. Worsnop et al. (*WES* 2018) pin it more literally still: "the same
quantiles … the same spread". **Pierre Pinson also co-authors the paper that occupies C1′,
and is a likely reviewer.**

**R1 survives, for a better reason than either dead argument.** Because those papers match
the *marginals*, the calendar-time variation of the deployed width is **identically zero**
across their arms — they vary the copula *within a single forecast issue*, not the revision
path of the deployed width. The quantity R1 measures is not merely unmeasured in their
design; it is constant in it. Plus Q3 fails throughout: Pinson & Girard and Bessa (PSCC
2016) both defer the decision step, and Pinson & Girard's conclusion commissions it
explicitly.

**Consequence for S2:** the probabilistic-forecast-verification chain joins the
forecast-stability chain in the paper's **opening**. Omitting it repeats the exact failure
mode that occupied C1′, one literature over.

### 4. A bibliography-provenance rule was broken, and it was broken in the way that is hardest to catch.

Three of sixteen new entries were not built from a saved fetched record. Two asserted
"Record from Crossref" for fetches whose output was printed and never persisted. The third,
`gupta2022nested`, asserted a volume, a page range, a year and an author's given name that
appeared in **no** saved record — a reconstruction that went unnoticed **because it was
correct**.

All three have been fetched, saved and verified field by field; nothing needed changing. The
failure is logged as `audit/REFS_REJECTED.md` §8, because:

> A provenance rule that is satisfied by a correct answer rather than by a saved record is
> not a provenance rule.

The adversarial critic then supplied a live demonstration of why the rule exists: it
reported the wind-scenario method paper as "Pinson, Papaefthymiou, Klöckl, Nielsen &
Verboomen (2009)". Crossref gives a different author list and a 2008 date. The fetched
record won.

### 5. The single most reusable thing this session produced is not a finding about the literature.

**The ACM Digital Library's HTTP 403 is Cloudflare bot detection, not a paywall. The library
is open access.** Eleven retrieval routes across two waves failed on IPOC because all eleven
assumed a paywall. A headed system Chrome instance with a persistent profile passes the
challenge and the full PDF downloads.

`audit/PRIOR_ART.md` §7.8.7 names five more items likely behind the same misdiagnosis,
including the closest remaining method match to R2's object.

---

## The verdicts

> **C1′ — OCCUPIED as worded.** By Van Belle et al. §2. A residual **R1** survives and is
> NARROW, on the argument in finding 3.
>
> **C2′ — NARROW.** Nothing states a distribution-free validity property for a
> movement-penalised conformal quantile that can shrink where the shrinkage is
> data-dependent. **The conditional that stood against this has been closed in the project's
> favour** — see below. Its object and its formulation are conceded as prior work.

### The distinguishing sentences

**For C1′ as worded there is none, and none was manufactured.** For the residual R1 and for
R2 they exist and are in `docs/FRAMING.md` §6, sentences 8 and 9. R2's is the stronger,
because every clause is a citation to a published object and the gap it names is a specific
unmet hypothesis rather than an absence of work.

### What the paper is

**R2 is the headline. R1 is the motivation.** R1 alone is a restatement of a 2026 result in
a new instrument, and it is the occupied leg.

**The inherited STOP condition is replaced.** "Fall back to reporting C1 alone" was written
before this sweep; C1 alone is precisely what is occupied. The replacement: **if R2 cannot
be delivered, re-scope rather than submit R1 by itself.**

---

## Did the forward-citation screen run, or run degraded?

**It ran in full, and it was not degraded.** This corrects the session's own Wave-0
preflight, which recorded Semantic Scholar as dead after three attempts.

Semantic Scholar is **intermittent, not dead**: with incremental backoff (4 s → 40 s, up to
~25 retries, **no API key**) every page eventually returns 200, and `/paper/{id}`,
`/citations` and `/references` keep working even while `/paper/search` is throttled. Full
citing sets pulled: **ACI 557, DtACI 188, Conformal PID 147, SAOCP 101 → 659 unique papers.**
Twelve candidates. **Zero OCCUPIED, zero NARROW.**

The pattern screen — co-occurrence of a level-fixing notion with a path-variation or
movement-cost notion — returned 5 hits across 659 papers, of which 4 were verified as false
positives by reading the matching sentence in context ("turnover" = *feature* turnover; "total
variation" ×2 = TV *distance*; SAOCP's "fixed length" = intervals of *time*). The sole
survivor, Conformal-ABR, was cleared: its risk control is on prediction error from the
calibration layer and its smoothness penalty is on the bitrate, downstream — two separate
objects.

**The prescribed fallback would have produced a false negative.** OpenAlex's ACI record
carries `cited_by_count = 27` against Semantic Scholar's 557 — a 95 % miss. Screening 27
papers and reporting a null would have been worse than not running the screen at all.

**`docs/OUTSTANDING.md` O1 is closed, and it never needed an API key. It needed backoff.**

---

## What Wave 1 found in the NEW square that G0 never searched

G0 never searched here, because the claim did not exist yet.

**In conformal prediction, the square is empty and the emptiness is well evidenced.**
`"matched average width"` 0, `"same average interval length"` 0, `"held the average width
fixed"` 0, `"matched width" conformal` 0. `"smoothed conformal quantile"` 0, `"prediction
set instability"` 0, conformal + hysteresis 0, conformal + dead-band 0, conformal +
"movement cost" 0. Conformal always runs the comparison the other way: fix coverage, compare
width. **Nobody in conformal even argues for the matched-width design.**

**Outside conformal, there are two large literatures the project had never cited, and they
own most of what it intended to claim.**

**(a) Forecast stability**, roughly seventeen years old, largely in the *International
Journal of Forecasting*. It has the increment metrics (MASC / RMSSC) and it publishes **both**
readout maps. **Godahewa et al. (*IJF* 2025) publish the linear partial-adjustment readout
`ỹ = (1−w_s)·ŷ_new + w_s·ỹ_prev`, one scalar, as model-agnostic post-processing** — C2′'s
quadratic-cost map, in print. **Genov et al. (*ESWA* 2026), Eq. 18–20, publish the
readout-map formulation itself**: `x_t = M(ŷ_t)` with `M` Lipschitz, switching cost bounded
by `β·L_M·Σ‖ŷ_t − ŷ_{t−v}‖`. Alongside: Pritularga & Kourentzes (2024) on forecast
congruence; Tunc et al. (2013) on the cost of system nervousness; Van Belle et al. 2023,
2024; Caljon et al. 2026.

**(b) Probabilistic-forecast verification**, where the matched pair was invented — Gneiting,
Balabdaoui & Raftery (2007); Pinson & Girard (2012); Worsnop et al. (2018); Pinson et al.
(2008). Found only by the adversarial critic, in Wave 4.

**The bridge is unbuilt.** On arXiv, `"conformal"` crossed with `"forecast stability"`,
`"forecast instability"`, `"forecast congruence"`, `"jumpiness"` and `"forecast revision"`
returns **zero** on every pairing in both directions. Not one of the papers citing Van Belle
et al. 2023 is conformal. **That zero is abstract-level** — see the limits section.

**On the validity question**, four independent groups have now named the obstacle R2
addresses without clearing it: SCD-split (post-hoc smoothing invalidates the guarantee);
ECI (a fully smoothed update leaves the averaged miscoverage gap uncontrolled, "due to the
smoothing bias"); IPOC (its chased interval can only "approximately guarantee" coverage);
and Dupuy et al., who prove it under a domination hypothesis they themselves call "pretty
strong". **Four groups hitting the same obstacle is better evidence that the obstacle is
real than the one remark the session originally cited.**

**And a correction to the design's own justification.** ACI's telescoping identity is
untouched by a readout smoother — and therefore certifies the **raw** interval, not the
**deployed smoothed** one. Gibbs–Candès Lemma 4.1 turns on `α_t < 0 ⇒ Q̂_t(1−α_t) = ∞ ⇒
err_t = 0`, a property of the construction. **Claim coverage for the raw arm only; report the
smoothed arm's coverage as a measured control.** This corrects the session brief's own
premise.

---

## Condemned claims removed, and where

**Ten CONDEMNED hits in working documents, all patched.** Eight AMBIGUOUS hits also patched;
59 LEGITIMATE-REPORTING hits deliberately left alone, because quoting a condemned sentence
inside its own condemnation is correct and so is describing someone else's impossibility
result.

| File | Removed |
|---|---|
| `README.md` | 1 — the "no coverage-based criterion can select" universal, on the public front page. The file was then rewritten entirely, because it still sold the abandoned design. |
| `audit/PRIOR_ART.md` | 5 — including "no explanation exists for it" (a bare universal negative, load-bearing for the old C1 verdict, contradicted by the project's own resolved finding) and the page-one distinguishing sentence "a functional that no coverage-based and no efficiency-based criterion measures" |
| `audit/CLAIMS.md` | 3 — plus C1b, C1c and C1d withdrawn outright, which the instruction critic caught still sitting at status `planned` |
| `audit/NUMBERS.md` | 1 — the only surviving unqualified Gârleanu–Pedersen dead-band attribution in the tree |

**Eleven further condemned claims sit in the three historical documents and were NOT
removed.** `docs/PLAN_ORIGINAL.md` (6), `docs/HYPERRESEARCH_REPORT.md` (3),
`docs/G0_REPORT.md` (2) each carry a dated correction note pointing to `docs/FRAMING.md`.
`git diff --numstat` confirms **47/0, 35/0, 37/0** — additions only, zero deleted lines.
Rewriting a historical document to remove an error destroys the evidence that the error was
made and caught.

**A seventh condemned claim was added** — the assertion that the telescoping identity makes
the coverage question moot.

**Two traps the framing auditor caught and the patcher did not walk into:** the repository's
own §6 *proposed replacement wording* reinstated the condemned word "frontier" for this
project's own object, and `audit/CLAIMS.md:32` proposed "no published explanation" as the
weakening of "nobody has explained it" — **which is also false**, because Ryan's explanation
is published. Patching naively would have installed a second wrong claim in place of the
first.

---

## The critics, and what they did

**Both ran. Both returned. Neither was skipped.** `research/S1/patch-log.json` records all
20 findings with their disposition: **12 accepted and fixed, 6 accepted and recorded, 2
partially accepted, 0 rejected.**

### The adversarial critic overturned nothing and damaged both verdicts

Its own headline: *neither verdict falls; both are weakened; one conditional closes in your
favour.*

- **It read IPOC**, which nobody else could reach, on the twelfth route. **Q5 = no.** Its
  only coverage statement is Gibbs–Candès imported for the **base model's** interval `c^f_t`,
  verified against Appendix A's notation table and a 300-dpi page render to disambiguate the
  superscript; the paper itself says the deployed object differs. **The session's largest
  open conditional is closed, and IPOC converts to a supporting citation.**
- **It destroyed both of R1's stated survival arguments** (finding 3) — and supplied a
  better one.
- **It found R2's object already published.** Binny & Dixit (arXiv:2511.11567) Eq. (13) is
  the one-scalar smoother on a deployed conformal calibration threshold, verbatim. **The
  no-novelty concession now covers three things, not one.**
- **It found the question already contested.** Dupuy et al. prove three coverage theorems
  for an update built to prevent abrupt threshold changes; **their Theorem 2 is R2's thesis
  with an attempted proof and a disowned assumption.** R2 must now be positioned against it
  specifically, or not written.
- **It found a sentence in `docs/FRAMING.md` that was false** and whose correction makes the
  argument stronger.
- **It named three places a scoop is still hiding**, with routes.

### The instruction critic found one critical and seven major violations

The critical one is finding 4. The majors: an operator question closed by reclassification;
the README contradicting the framing lock; two must-cites missing from `related.tex`; the
page overrun recorded only in scratch; incomplete rubric evidence in three agents; G1's
status contradicting the file's own vocabulary; and condemned claims left standing in
`audit/CLAIMS.md`. **All fixed.**

It also verified clean, by inspection rather than assumption: identity and hygiene; `research/`
untracked with zero files in either commit; **no gate recorded as signed, passed or met
anywhere**; the three historical documents with zero deleted lines; G2.10 deleted with its
old text quoted and its reason given; G3.2 retained; §5 of `audit/PRIOR_ART.md` preserved
under §7; O8 closed with reason; all checkpoints present; and **no work discarded on
application domain** — the failure mode this session existed to correct.

---

## What this session could not reach

Stated so the verdicts are read with their instrument.

1. **Every "nothing in the literature" statement here is abstract-level only.** OpenAlex
   exhausted its anonymous full-text budget in Wave 1 and had not recovered by Wave 4. **Not
   one** of the named full-text queries ran, in either wave. Full-text search is the only
   instrument that sees a smoother buried in a methods section, and **the hole is
   demonstrably non-empty**: two SSRN papers carry "turnover" and "transaction cost" in full
   text but not in their abstracts and appear in no citing set. `docs/OUTSTANDING.md` O26.
2. **Three named hiding places, none closed.** The decision-value follow-up that Pinson &
   Girard commissioned in 2012 — with **Rachunok et al., *Applied Energy* 274:114986** as the
   named candidate, unreachable on three attempts. The applied conformal layer behind
   publisher bot walls, starting with "AQA" (doi 10.1109/CEEPE69795.2026.11552153). And the
   **Schaake-shuffle / ensemble-copula-coupling branch of hydrology and reservoir
   operations, which is entirely absent from this repository** — `Schaake`, `copula
   coupling`, `variogram` and `PINAW` return zero occurrences across the whole tree. ECC
   preserves the univariate margins *exactly by construction*, so every such comparison is
   automatically matched on coverage and width on a real producer. `audit/PRIOR_ART.md` §7.8.7.
3. **Jia & Han's body is closed.** Abstract, full reference list, keywords and affiliations
   obtained; no open-access location, no preprint, absent from the author's own page. Scored
   CLEAR/CLEAR on what was read. G1.3 is marked **partial**, not met.
4. **Chopra (1993) was not obtained in any form** — six routes dead; Google Scholar holds it
   as a link-free `[CITATION]` stub. Nothing was reconstructed.
5. **The IPOC TKDE extension's theory section is unread.** Its abstract enumerates only the
   same two regret results, so a new coverage theorem is unlikely, but this is formally
   unverified.
6. **No forward-citation screen was run on Godahewa or Van Belle.** Semantic Scholar returns
   404 for Godahewa's DOI. Two agents independently name this as the highest-value follow-up.
7. **Zanotti's MQC/SMQC could not be resolved to a canonical record**, so no entry was
   written for it. It is the existing published name for `Σ|Δq|` and is carried as a pointer
   in O22.
8. **A6 logged zero queries**, although its negative-existence finding is a premise G3 cites.
   Not repairable without re-running it. This is why the obstacle is now argued from four
   named quotations with locators rather than from any agent's claim of absence.
9. **Process gaps, disclosed rather than tidied away.** Wave 2 had no commit of its own —
   `related.tex` landed in the Wave-3 commit. **B1 was deliberately held until A7 returned**
   rather than launched with B2 and B3, because a verdict written without the four decisive
   full-text reads would have been provisional exactly where it mattered; that deviation is
   recorded here, in `research/checkpoints/S1-W2-synthesis.md`, and was given to the
   instruction critic to judge. Q9's original wording was overwritten rather than superseded.
   None of this was retro-fixed: rewriting history to make the cadence look right would be
   worse than recording that it was not.

---

## Status, and what S2 needs

**G1 is `ready for review`, with one criterion outstanding by design.** It is **not signed**,
and no automated session may sign it. G1.7 (venue) has no evidence and cannot have any — it
is an operator decision. G1.3 is partial. The status line says so itself, and offers `in
progress` as the alternative if the operator judges the vocabulary stretched.

**S2 requires operator sign-off plus answers to `docs/OPEN_QUESTIONS.md`** — in particular
Q3 (venue and cycle), **Q4, which this session re-posed rather than answered** (the movement
penalty's placement changed to the width path, which is *neither* of the original branches;
if the intended answer was branch (a), the S1 design is a different project and that should
be said now), Q7 (L1 or L2), and Q10 (send the author request).

**Three things S2 can start without compute and without sign-off**, in order:

1. **O0a2 — position R2 against Dupuy et al. Theorem 2.** R2's contribution is either
   discharging the assumption they disowned, or nothing.
2. **O0b — attack G3.4(b) on paper:** does deployed miscoverage stay monotone in α_t under
   the smoother? It is the technical contribution if it holds, and finding out during
   implementation that it does not would waste the implementation.
3. **O0a3 — read Pinson & Girard in full and re-argue R1** on the object distinction in
   finding 3.

**Not begun, deliberately:** no protocol freeze, no simulator, no gate marked passed.

**The binding constraints are not novelty.** The simulator does not exist
(`audit/REPRO_C1.md`), and the nearest deadline is thirteen days out (`docs/VENUE.md`).
Novelty is now sufficient for a workshop paper and insufficient on its own to justify the
build.
