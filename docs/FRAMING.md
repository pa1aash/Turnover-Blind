# FRAMING — locked 2026-08-19

**This file governs every later session.** Where it and any other document in this
repository disagree, this file wins, except that `audit/PRIOR_ART.md` §7 is its evidentiary
basis and `docs/GATES.md` is its enforcement mechanism.

It was written at the end of session S1, after a seven-agent prior-art sweep whose
governing finding is that **the first claim, as it was worded going into that session, is
occupied.** Nothing here is a softening of that. The framing is locked *around* it.

---

## 0. The one thing to read if you read nothing else

A published paper three months older than this framing already runs the identifying design
the project intended to claim: **Van Belle, Wen, Verbeke & Pinson, "Stabilizing
distribution-free probabilistic forecasts", arXiv:2605.28531, 27 May 2026.** It matches two
forecasters on a level functional by construction, varies only the temporal path of their
updates, prices the difference through a decision charged to revise an incumbent, includes
a placebo arm that shows no effect, and states the evaluation moral explicitly. It does all
of this without the words "coverage", "interval width" or "conformal", which is why no
conformal-anchored query in any instrument would ever have returned it.

**What survives is narrower than what was intended, and it is stated in §2 as R1 and R2.
R2 is the paper. R1 is the motivation.**

---

## 1. The aim

### Repeatable form

> An online conformal interval can be held to the same coverage and the same average width
> and still move very differently from day to day, and a decision that pays to move is
> charged for the difference.

### Precise form

> Fix an online conformal interval producer and hold two quantities constant across arms:
> realised coverage, and mean interval width `E[L]`. These are the two quantities on which
> the online conformal literature reports and tunes. Vary a one-scalar movement penalty
> applied to the width path — a smoother on the conformal quantile `q_t`. Measure the path
> variation `Σ|Δq_t|`, the induced turnover, and the net log growth of a position charged
> to move. Then ask what the movement penalty does to the validity of the interval that is
> actually deployed.

Identification comes from **holding LEVEL fixed and varying VARIATION**. That is the whole
methodological content, and it is also the reason the claim is exposed — see §5.

---

## 2. The claims, as they will be stated in the paper

The claims **C1'** and **C2'** as they were carried into session S1 are superseded. They
are recorded here so later sessions can see what changed, followed by what replaces them.

### 2.1 Superseded

> **C1' (superseded — OCCUPIED).** At fixed coverage AND fixed mean interval width, the
> temporal variation of an online conformal interval varies materially and carries a
> decision cost, measured in annual net log growth. Neither coverage nor efficiency (mean
> length) measures it.
>
> **C2' (superseded — subsumed into R2, with a longer concession list).** The
> movement-penalised readout map is the right object for setting that variation: quadratic
> movement cost gives linear partial adjustment, proportional cost gives a dead-band. No
> novelty is claimed for either form.

C1' is occupied by Van Belle et al. §2. C2''s no-novelty concession, which used to cover
the two functional forms, must now extend to **the readout-map formulation itself**: Genov
et al. (*ESWA* 2026), Eq. 18–20, already write `x_t = M(ŷ_t)` with `M` assumed Lipschitz
with constant `L_M`, and bound the switching cost by `β·L_M·Σ‖ŷ_t − ŷ_{t−v}‖`.

### 2.2 What the paper claims — R1 and R2

> **R1 (measurement — the motivation).** On a real online conformal producer, the pair on
> which the online conformal literature reports and tunes — realised coverage together with
> mean interval width — can be held fixed while the width path `Σ|Δq_t|` varies by a factor
> of F, and the resulting difference in annual net log growth on a position charged to move
> is N points. **This is claimed as the conformal instance of a result already established
> outside conformal prediction, and no wider.**
>
> **R2 (the object and its validity — the paper).** A one-scalar movement penalty applied
> to the **deployed** conformal quantile is not covered by the existing
> predictable-modification arguments, because it acts on the quantile-based width mechanism
> and therefore puts at risk the monotonicity condition those arguments require. The paper
> states the conditions under which ACI's long-run coverage survives such a penalty, and
> reports realised coverage on the smoothed arm as a measured control regardless.

**R2 is the headline. R1 is the motivation. Not the other way round.** R1 alone is a
restatement of a 2026 result in a new instrument, and it is the leg that has been occupied.

### 2.3 The STOP condition is replaced

The inherited STOP condition — *"if the method fails, fall back to reporting C1 alone"* —
was written before session S1 and is **now the wrong fallback**, because C1 alone is
precisely the occupied leg. The replacement:

> **If R2 cannot be delivered, re-scope. Do not submit R1 by itself.**

---

## 3. The decision-theoretic constraint, and the operational restatement rule

**The claim is decision-theoretic, not information-theoretic.** No impossibility framing, no
coverage floor, no "fundamental limit". Vaze (arXiv:2607.26577) and Srinivas (SODA 2026,
arXiv:2507.02496) hold that ground and this project loses on it.

### The operational restatement rule

> **Replace every quantifier with a measurement.**

Any sentence of the form "no X can do Y" must become a sentence of the form "across arms
matched on A and B, quantity Z varies by N". The second is the same finding, is what the
experiment actually shows, and is unassailable in a way the first is not.

| Forbidden grammar | Operational replacement |
|---|---|
| "no coverage-based criterion can select the adaptation rate" | "Across arms matched on realised coverage to within 0.002 and on mean interval width to within a stated tolerance, realised decision cost varies by N points of annual net log growth. Coverage and mean width are therefore uninformative for selecting the movement penalty." |
| "coverage is blind to turnover" | "Realised coverage is constant across arms whose width paths differ by a factor of F." |
| "nothing in the literature measures the increment functional" | "`Σ\|Δq_t\|` is reported here; the works cited in §related report coverage and mean length." |

**"Blind" is itself forbidden as a load-bearing word.** It invites the impossibility reading,
and it is the exact move Min et al., Vaze and Van Belle have each already made in a
different form. Use the measurement.

**Watch-list of forbidden constructions:** `no X can`, `cannot select`, `floor`,
`fundamental limit`, `impossible`, `impossibility`, `nobody has`, `no one has`,
`never been`, `no method`, `no criterion`, `provably cannot`, `there is no`.

Reporting *someone else's* impossibility result is legitimate and required — Andrew et al.
(COLT 2013) genuinely is an impossibility theorem and describing it correctly is not a
violation. The prohibition is on this project claiming one.

---

## 4. The six condemned claims, with their replacements

| # | Condemned | Replacement |
|---|---|---|
| **i** | "Nobody has explained it" / any claim that the Ryan anomaly is unexplained. | Ryan offers an explanation — estimation variance charged through the nonlinear Kelly sizing map — hedged in his own text as "a structural explanation consistent with the results", conjectured rather than measured for three of four devices, and never phrased in terms of turnover. The paper engages that explanation; it does not deny its existence. |
| **ii** | The "quantitative match" of 0.7–5.3 to 1.0–4.4, and the 1.0 lower bound. | Delete. No numeric correspondence between the two ranges is claimed. |
| **iii** | Gârleanu–Pedersen as the source of the **dead-band** form. | Gârleanu & Pedersen (2013) assume **quadratic** costs and derive **linear partial adjustment**, and explicitly distinguish themselves from no-trade strategies. Cite them for the quadratic ⇒ partial-adjustment half only. The dead-band is **Constantinides (1986)** and **Davis & Norman (1990)**. |
| **iv** | "No coverage-based criterion can select the adaptation rate." | Refuted by DtACI, which selects the step size online by a coverage-based criterion. Use the operational restatement in §3. |
| **v** | The word **"frontier"** as a formal object belonging to this project. | Either present a measured curve with no minimax claim and no use of the word, or drop it. Note that "frontier" describing *someone else's* object — Srinivas's coverage–efficiency frontier, Zhou & Zhu's miscoverage–regret frontier — is correct and must be retained. |
| **vi** | "arXiv returns 0 for conformal × downstream decision." | False. Decision-focused conformal prediction is an active field with a dozen uncited entries, at least one by a confirmed speaker at the target venue. |

**A seventh, added by session S1:** the assertion that **ACI's telescoping coverage identity
is untouched by a readout smoother, and therefore no coverage question arises**. The
identity is indeed untouched — and that is exactly the problem: it then certifies the
coverage of the **raw** interval, not the **deployed smoothed** one. Gibbs–Candès Lemma 4.1
turns on `α_t < 0 ⇒ Q̂_t(1−α_t) = ∞ ⇒ err_t = 0`, a property of the construction; feed the
recursion the smoothed interval's indicator and that proof fails. **Claim coverage for the
raw arm only. Report the smoothed arm's realised coverage as a measured control.**

---

## 5. What the design change bought and what it cost — state this, do not hide it

The abandoned design varied ACI's adaptation rate γ and measured turnover. Its recorded
fatal risk was that `Σ|Δq|` might be approximately a monotone function of `E[L]` across the
γ grid, collapsing the claim into Zaffran's Theorem 3.1 times a cost rate.

**What matched-width bought.** It removes that objection by construction. There is now
direct external evidence the change was necessary: **Genov et al. is the γ design, in energy
systems, and it fails exactly there** — its commitment-period arms move level and variation
together, its §4.4 says so in its own words, and its attribution runs through a cross-arm
correlation table.

**What it cost.** Holding a level functional fixed while varying a path functional and
pricing the difference through a decision with an incumbent state **is Van Belle §2's
design**. The old design was confounded enough to be unlike anything published; the new one
is clean enough to be exactly like the best paper in a neighbouring field.

> **The new design is more exposed than the old one, and it is more exposed because it is
> better.** State it in those terms. Do not revert to γ — reverting restores an
> identification failure that is now documented in print, and the paper would be attacked
> on methodology instead of on novelty, which is worse.

---

## 6. The distinguishing sentences

These go in the paper. Sentences 1–7 are the related-work section (`paper/sections/related.tex`);
8 and 9 are the two that carry the contribution.

1. **Zaffran et al. (ICML 2022)** price ACI's learning rate in the *level*: Theorem 3.1 gives
   `E_{π_γ}[L] = L₀ + ½·Q″(1−α)·γ·α(1−α) + O(γ^{3/2})`, a statement about mean length, which
   integrates the path away; we hold it fixed.
2. **Min et al. (arXiv:2601.21455, ICML 2026)** also call coverage and length insufficient,
   but their interval stability (Def. 4.1), `E_X[Var_{A|X,D_ca}(|C_{1−α}(X)|)]`, varies over
   the algorithm's own randomness given test point *and* calibration set and is "zero for
   deterministic methods by design": a deterministic interval oscillating daily scores
   exactly zero.
3. **Zhou & Zhu (arXiv:2510.07750)** vary the coverage *level* along a miscoverage–regret
   trade-off; we fix coverage and vary the path.
4. **Ryan (arXiv:2608.01494)** charges the growth loss to estimation variance passing through
   the nonlinear Kelly sizing map, hedged as "a structural explanation consistent with the
   results", and already reports the daily `sd(Δ log q)` (0.00343 vs 0.00391) and matched
   gross leverage (1.957–1.959); what he does not match is width, nor phrase it as turnover.
5. **Wang & Hasuike (arXiv:2605.01176)** report that "increasing risk aversion does not
   meaningfully reduce turnover" and damp the *weight* path by a heuristic δ = 0.1 partial
   adjustment, never swept; their paper carries no interval, coverage or quantile object.
6. **Godahewa et al. (*IJF* 2025)** already publish the linear partial-adjustment readout
   `ỹ = (1−w_s)·ŷ_new + w_s·ỹ_prev` as model-agnostic post-processing, so we claim no
   novelty for either form.
7. **Van Belle et al. (arXiv:2605.28531)** pin CRPS across arms (2.91/1.43/0.83 vs
   2.91/1.44/0.83, "indistinguishable in terms of forecast quality"), vary `W₁` between
   consecutive updates threefold, and price it through a newsvendor; but their functional is
   over forecast *revisions of a fixed target*, they carry no interval and no coverage
   object, and the effect is +0.00 % in their single-horizon arm.

**8 — the R1 sentence.**

> Van Belle et al. (2026) match two synthetic forecasters on CRPS and price the difference
> in their update paths through a newsvendor charged to revise an incumbent order; the
> question here begins one step later, inside a producer whose coverage is pinned by the
> conformal construction rather than by a matched data-generating process, and asks what
> the freedom that remains is worth — with realised coverage *and* mean interval width, the
> pair the online conformal literature actually tunes on, both held fixed on a real
> producer, the width path is still free to move, and it is that residual freedom that is
> priced here in annual net log growth on a position charged to move.

**9 — the R2 sentence.**

> Godahewa et al. (*IJF* 2025) publish the one-scalar partial-adjustment smoother as
> model-agnostic post-processing, and Genov et al. (*ESWA* 2026, Eq. 18–20) already bound a
> decision's switching cost by the forecast path variation through a Lipschitz readout map;
> neither object carries a validity property, and the one statement in print about what a
> post-hoc smoother does to a conformal quantile is SCD-split's remark that it invalidates
> the guarantee — so what remains to establish is the condition under which a movement
> penalty on the *deployed* quantile keeps ACI's long-run coverage, which is exactly the
> monotonicity hypothesis that BC-ACI's own coverage proposition names and secures only by
> leaving the width mechanism untouched.

**Honest weakness of sentence 8, to be pre-empted in the paper rather than discovered in
review.** A hostile reviewer will say: *you matched a level functional; so did they; CRPS
versus (coverage, mean width) is a detail.* The answer, which must be **in the paper**, is
that (coverage, mean width) is not an arbitrary choice of level functional — it is the
two-part criterion on which ACI, DtACI, Conformal PID and SAOCP are all reported and tuned,
so pinning that specific pair is a statement about a field's tuning practice rather than
about accuracy in general. That answer is defensible. It is not overwhelming.

---

## 7. Positioning rules that follow

1. **The forecast-stability chain goes in the OPENING, not in related work.** Godahewa et
   al. 2025; Van Belle et al. 2023, 2024, 2026; Pritularga & Kourentzes 2024; Caljon et al.
   2026; Tunc et al. 2013; Genov et al. 2026. A four-page paper that cites this chain first
   and then says what the conformal setting adds is a legitimate contribution. The same
   paper without those citations is a rediscovery, and anyone from forecasting will
   recognise it as one.
2. **Do not claim "coverage and length are not sufficient" as this project's move.** Cite
   Min et al. and Vaze first, then name the quantity added.
3. **Do not use a vertical/horizontal (revision-index versus calendar-time) distinction to
   separate this work from the forecast-stability literature.** It was proposed and
   withdrawn within session S1: Godahewa et al. name and stabilise both, and Genov defines
   vertical and horizontal variants of both MAC and SDC. It will be corrected in review.
4. **Do not lean on Van Belle's +0.00 % procrastination row** as evidence their effect is
   confined to multi-horizon revision. It is an artefact of their three-opportunity setup.
5. **Coin a new term for the measured quantity.** Every natural name is taken: *smoothed
   conformal* means randomised smoothing; *stable conformal* means Ndiaye's computational
   stability; *smoothing-based conformal* is SCD-split; *interval stability* is Min et al.'s
   run-to-run variance. And `Σ|Δq|` itself is already a published named metric (Zanotti's
   MQC/SMQC), so the measurement instrument cannot be presented as new either.
6. **Defuse Min et al. Theorem 3.3 explicitly.** It shows a post-processing can preserve
   coverage while shortening mean length by returning ∅ on some draws — which is the exact
   failure mode of judging an interval by (coverage, mean length). The defence is that R1
   fixes *both* and reports the path functional as an addition, and that their IS is 0 for
   a deterministic smoother. Say it; do not leave it to inference.
7. **Pre-empt the Ryan objection.** He matches *post-cap gross leverage*, which is
   downstream of the sizing map and therefore confounds the level and path of `q` upstream
   of the cap. Show that `E[L]` and gross leverage come apart, or the reviewer will read his
   control as the stronger one. **This leg is contingent** — it rests on his not printing a
   per-device path statistic, and it weakens if the requested ledger
   (`docs/RYAN_EMAIL_DRAFT.md`) turns out to contain per-device turnover.

---

## 8. The open conditional

**R2's distinguishing sentence is void if IPOC's confidence-interval theorem quantifies over
the movement-constrained chased object.**

IPOC — Chen, Luo, Huang, Jiang, Shi, Zhang & Gao, KDD 2023, doi 10.1145/3580305.3599396,
pp. 202–212, and its extension, IEEE TKDE 38(5):3277–3290, doi 10.1109/TKDE.2026.3674583 —
is **unread**. Eleven retrieval routes failed in session S1: the ACM Digital Library returns
HTTP 403 to direct fetch, to a real browser and to a server-side fetch; ResearchGate 403s;
Unpaywall reports it closed; there is no arXiv preprint though the first author has four
others; nothing is on the authors' pages; IEEE Xplore is JavaScript-gated. Its abstract
claims validation "through sublinear regret analysis and satisfaction of confidence interval
requirements", and the extension states "The chasing regret of the Chasing Oracle is O(L_c)"
— a coverage-type guarantee and an explicit movement cost in one theory sentence.

**It requires institutional access. Until it is read, R2 is stated with the conditional
visible, and no gate that depends on R2's novelty may be signed.**

---

## 9. Evidentiary basis

- `audit/PRIOR_ART.md` §7 — the dated verdicts against C1'/C2', superseding §5.
- `research/S1/B1-verdicts.md` — the full synthesis, the top-ten table with all five rubric
  answers, the stress test of R1 and R2 against the five nearest neighbours, and what would
  move each verdict.
- `research/S1/A1`–`A7*.json` — the seven retrieval agents, every query logged verbatim with
  its result count.
- `research/checkpoints/S1-W1-retrieval.md`, `S1-W2-synthesis.md` — the wave records.
- `audit/REFS_VERIFIED.bib` — every entry built from a fetched canonical record.
