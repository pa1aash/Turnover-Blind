# Outstanding items

Every unresolved technical item, ranked by whether it blocks a gate. Items requiring an
operator decision rather than work are in `docs/OPEN_QUESTIONS.md` and are cross-referenced
here.

Ranking is by **blocking status first, then by consequence if left undone** — not by
effort.

> **RE-SCOPED 2026-08-20 BY SESSION S3 — read the S3 section below before any tier.** R1 is
> dropped and R2\*\* is superseded (`docs/FRAMING.md` §2.2c), `docs/GATES.md` retires **G2,
> G2-pre, G3 and G4** and writes **G7**, and roughly two dozen items in the tiers below lose
> their referents with them. **Every retired item keeps its full text where it stands and
> carries a `RETIRED 2026-08-20` marker in its own row.** The tier structure itself is now
> historical: the tiers are named for gates that are retired, and the live ranking is the S3
> section's own tables. **OI-1 and OI-2 are marked SUPERSEDED there. They are not answered and
> no automated session may answer them.**
>
> > **AMENDED 2026-08-20 BY SESSION S4 (agent K1).** **OI-1 is CLOSED**, and it is closed the
> > only way an automated session may close an operator item: **it turned out not to be one.**
> > L1-versus-L2 is `docs/FRAMING.md` §2.2c R3b restated — the L1 dead band on the completed
> > threshold is the family that leaves li2025o2cp Corollary 2's admissible radius, at
> > `τ* = sup r_t + sup q̂ − b/2`, and past it miscoverage is `1.000000` with condition (4)
> > holding on every round. **L2 is not certified by that**: at the null scorecaster it forfeits
> > the rate (`623.70` vs `14.8155`) while keeping coverage (`0.100035`), and at the equally
> > legal `q̂ ≡ −b/2` it returns `1.000000` too. `docs/OPEN_QUESTIONS.md` Q7;
> > `results/forfeit-variations-20260820T101445Z.json`. **OI-2 is untouched and stays
> > SUPERSEDED and unanswered. No gate is signed by this.**

**Re-ranked 2026-08-19 by session S1**, after the prior-art sweep found the first claim
occupied. Read `docs/FRAMING.md` first: the claims these items serve are not the claims
most of them were written against. A new **Tier 0** sits above everything, holding the
three items that can each make a large amount of downstream work worthless and none of
which needs a simulator.

---

---

## Session S3 — the re-scope, and what it retires

*Added 2026-08-20 by session S3, whose wave 1 ran five agents in parallel (H1 anti-windup
kill-check, H2 venue, H3 full-text close, H4 the simulator, H5 the four-literature bridge).
All five returned. Working records: `research/S3/H1..H5*.json`, `research/S3/ft/`,
`research/S3/records/`, `research/checkpoints/S3-W0-rescope.md` and `S3-W1-findings.md`.*

**The headline is in `docs/FRAMING.md` §2.2c and the enforcement in `docs/GATES.md` G7.** In one
line: **R1 is dropped, R2\*\* is superseded, and the paper is R3a (a correction), R3b (the
measurement, and the headline) and R3c (one scoped bridge cell).** What lands in this file is
the bookkeeping — and it is mostly subtraction.

**The convention, unchanged: supersede and retire, never delete.** An item retired here keeps
its full original text below. A later session reviving the decision-cost paper inherits every
one of them.

### The three that changed status on their own merits, not by scope

| # | Item | Resolution |
|---|---|---|
| **O42** | Whether a bounded scorecaster can offset the integrator's movement — the successor to the withdrawn conservation law, and the project's last named route to a theory result | **CLOSED. OCCUPIED.** H1's verdict. The object is **integrator anti-windup with a feedforward path**, and the free-until-saturation dichotomy is that field's **problem statement** (Galeani, Tarbouriech, Turner & Zaccarian, two named items). The (authority, severity) boundary exists in three published forms, the sharpest a measured saturation-ratio threshold swept over a 3-D grid (**arXiv:2606.01959**, June 2026); the budget split is printed (**arXiv:2606.07208**, eq. 46–47); and `Σ\|Δq_t\|` is the discrete-time **IACER**. **O42 does not come back.** What is unoccupied is narrow and it is not an experiment: the conformal↔anti-windup connection is **unnamed on the surface measured** — arXiv full text returns 0 for `windup AND conformal` against a well-formed 730-byte empty feed, 2026-08-20. **That is two sentences of related work, drafted by H5, and it is not a fifth column and not a fifth experiment.** `research/S3/H1-antiwindup.json` |
| **O43** | Regenerate S2's verification numbers from committed code before any of them is printed | **DISCHARGED FOR THE ROWS THE PAPER PRINTS. NOT CLOSED.** `src/forfeit.py` and `src/test_forfeit.py` exist, and every number R3b prints traces to one of the four `results/forfeit-*.json`. **Rows 55–58 of `audit/NUMBERS.md` §11 remain orphaned** — the `Σ\|Δq_t\|`×bound Θ(log T) series, the 91.2 → 0.21 cancellation, the 1.12× under shift, and the 0.36–0.40 exact-arithmetic check. **They are the withdrawn conservation law's numbers and the re-scoped paper prints none of them**, so the orphan is by design; the row is kept open so that a later session that revives them re-runs them first. The criterion is now `docs/GATES.md` **G7.1** |
| **O20** | Verify the TS-LIMITS page limit and anonymity regime | **CLOSED. 4–7 pages plus references, double-blind.** The call was never JavaScript-gated in any way that mattered: the site's own last two lines name `content.js`, and one fetch of that asset returns the entire call. Recorded alongside it, because the venue decision turns on both: **E-values is 4 pages, single-blind as of 2026-08-14 after three anonymity flips in 17 days, deadline 2026-08-29 23:59 AoE**, and it names conformal prediction in its call. **H2's recommendation is E-values, on room. It is a recommendation and the choice stays with the operator** (`docs/OPEN_QUESTIONS.md` Q3, `docs/GATES.md` G1.7). `research/S3/H2-venue.json` |

### O45 — partly closed, and its Google Scholar leg has now defeated two sessions

| Leg | Status |
|---|---|
| **OpenReview** | **CLOSED.** 88 queries against `api2/notes/search`. The decisive measurement is the rare token: `scorecaster` returns **exactly 4 notes in the entire index** (31,202-byte response), all four read, lying in two forums only — ICLR 2026 Submission 18277 (DDCI) and ICLR 2025 Submission 3886 (ECI); `scorecasters` returns 0. **No occupant.** Two instrument warnings that must not be lost: api2 search uses **OR semantics** and its `count` saturates at 10,000, so multi-word queries are uninterpretable — a nonsense control returned 297 hits as a phrase and 0 as a single token — and eight queries returned a 313-byte transient rate-limit body that the size guard refused to bank as zeros |
| **Google Scholar** | **STILL OPEN, and it is the leg that matters.** Eight unblock probes 06:03:34Z–07:03:38Z, **every one an HTTP 429 with a 3,322-byte `/sorry` interstitial**, served identically to headless `curl`, to `hyperresearch fetch` and to headed Chrome — the block is **host- or IP-level** and no fingerprint defeated it. **The `GS_MIN_BYTES = 20000` guard held and not one zero entered the record from this surface.** The battery is armed and idempotent at **`research/S3/ft/gs_battery.py`**, 50 queries numbered 31–80 (the eight S2 queries that produced no valid data, plus 42 new methods-section-vocabulary queries), and it writes `response_bytes` and `zero_is_real` on every row. It remains the surface that produced both of S2's decisive hits |
| **Institutional repositories** | **STILL OPEN. Re-opened headlessly — see O49.** 52 queries. HAL reached at full text (`text_fulltext:"scorecaster"` = 1 across all of HAL, audited and cleared), OpenAIRE and Zenodo reached at metadata only. **DTU Orbit, DiVA, MPIDR/PuRe and RePEc all hard-blocked, and no zero was recorded from any of them** |

### Retired by the re-scope

**Each of these serves the matched-width experiment, the simulator-for-R1 critical path, the
finance arm, the Ryan replication or a venue that is no longer in the set.** None is deleted;
each keeps its full text in its original tier below.

| # | Retired because |
|---|---|
| **O0a3** | Re-argue R1 on Q3 and read Pinson & Girard in full. **R1 is dropped.** The reading obligation survives in a different place: R3c's L1×L3 cell is the verification literature, and `docs/FRAMING.md` §7 rule 1 chain (b) is unaffected |
| **O0c / O4b** | The Ryan author data request and the `results.tsv` ledger. **G4 is retired**, the per-device turnover figures served R1's Ryan leg, and Ryan survives at most as one motivating sentence. **`docs/RYAN_EMAIL_DRAFT.md` keeps its `[OPERATOR INPUT]` header and is not sent by any automated session** |
| **O5** | Recover `scratchpad/confloor5.py`. The simulator it would have recovered is the matched-width simulator. `src/forfeit.py` exists and is a different instrument |
| **O6** | Freeze R1–R13 before running anything. `docs/PROTOCOL.md` did the freeze; **the sweep it froze is not being run** (`docs/GATES.md` G2-pre, retired). The freeze is not withdrawn and still binds a revival |
| **O7** | Empirical-quantile ACI versus a Gaussian proxy. **The re-scoped experiment has no ACI producer** — R3b runs against a Conformal PID threshold |
| **O9, O10, O11, O12, O13** | The three untabulated results, `Var(q)` alongside `Var(Δq)`, the equivalence test and its margin, the α_t clipping rule and time-at-clip, and the path count from the smallest claimed γ difference. **All five are properties of the matched-width sweep** |
| **O14, O15, O16, O17, O17b, O18** | The dead-band asymmetry against ACI's `+0.1γ / −0.9γ` increment, the Online Balanced Descent potential-function template for the C-a bound, Chopra (1993), the per-device decomposition of Ryan's cost sweep, the Config A/B counter-evidence, and Ryan's `z = 1.2816` / `1.1503` inconsistency. **Tier 3 in full: it blocked G3 or G4, and both are retired.** Two contents outlive their items — the dead band is now R3b's coverage-losing family, on a different producer and for a different reason; and G4.5's principle, that silently fixing someone else's disclosed defect makes a replication not a replication, is worth keeping |
| **O19** | The three ML×OR compliance questions. **ML×OR is out of the venue set**; the live pair is E-values and TS-LIMITS (O20) |
| **O23** | `paper/sections/related.tex` overruns its 0.3-page budget at 0.485 pages. **The rewrite supersedes the measurement** — the section being budgeted no longer exists in that form. The page limit itself is unchanged and harder: `docs/GATES.md` G7.7, exactly 4 pages of body |
| **O25, O25b, O25c** | The three hiding places, Chen, Yang, Li & Liu (2013), and the body of Williams, Peters & Raiszadeh (1985). **All three hunt occupants of R1.** O25b already resolved — it OCCUPIES, which is part of why R1 is dropped |
| **O27** | Withdraw the false "no work prices a matched-marginal path difference" claim and re-state R1's decision leg. **First half already DONE by S2** — the withdrawal is in place at `audit/PRIOR_ART.md` §7.9.3 and `docs/FRAMING.md` §8b item 4. **Second half retired with R1** |
| **O28** | Re-state R1 on Q5 alone and stress-test whether it carries a paper. **The re-scope is the answer: it does not, and R1 is dropped** |
| **O29, O30, O35, O36** | The body of Chen et al. (2013), the 2018 restatement, Delikaraoglou & Pinson (2014) and Bitran, Haas & Matsuo (1986). **All four are R1's neighbouring-literature obligations.** O36's warning survives on its own terms — **no sentence in this paper may imply the mechanism is recent** |
| **O31, O32, O33** | Position R2 against AQA; the three ScienceDirect items; the TKDE IPOC extension's ACCI module. **All three are occupancy hunts for a placement claim that is now conceded outright**, and a conceded claim cannot be occupied further. O32's blocker is also now moot as a *route* question: ScienceDirect's Turnstile is unreachable under the headless retrieval policy and is an **instrument gap** (O34) |
| **O37** | Decide what the paper is. **CLOSED: this session is the decision.** `docs/FRAMING.md` §2.2c, `docs/GATES.md` G7 |
| **O41** | Fix the G3 numbering defect. **RETIRED WITH G3, NOT REPAIRED.** Sorting the table would mean updating every cross-reference in the repository to a retired gate. The defect is recorded and left visible |
| **O4 (Tier 1)** | Decide the movement penalty's functional form. **This is OI-1 — see below. SUPERSEDED, not answered.** **RESOLVED 2026-08-20 (S4): closed by measurement, not by decision. The L1 form is the object of study whose failure is characterised; the L2 form is the reference arm and is not certified by that role. `docs/OPEN_QUESTIONS.md` Q7** |

### What survives, and where it now sits

| # | Status after the re-scope |
|---|---|
| **O3** | **OPEN.** The body of Jia & Han. It is a G1.3 residual and G1 stands. Low risk: a five-paper workshop-track chapter with one citation, scored CLEAR / CLEAR on abstract and reference list |
| **O21** | **OPEN, and promoted.** Rebuild the reference list from `audit/REFS_VERIFIED.bib` rather than from `docs/PLAN_ORIGINAL.md`. Now `docs/GATES.md` **G7.8** |
| **O22** | **DISCHARGED, with the concession enlarged.** The term is coined — *travel* / *quantile travel* — with the collision check recorded in `paper/sections/setup.tex` (`"quantile travel"` at 0 hits, rejected alternatives logged with counts). **What changed is the concession: six taken names, not four** (`docs/FRAMING.md` §7 rule 5; `docs/GATES.md` G7.11), and three of the six need bibliography entries the repository does not have — O48 |
| **O24** | **OPEN until the build is green.** Unescaped `_` and raw math in `audit/REFS_VERIFIED.bib` `note` fields. G7.8 requires the fix **before** the build, not after it fails |
| **O34** | **OPEN, and REWRITTEN BELOW under a binding operator policy.** The recommendation of headed Chrome is withdrawn |
| **O38** | **OPEN.** The three broken provenance records and the false provenance label. Partially repaired in S2. It is the same failure class G7.1 exists to prevent |
| **O39** | **OPEN, and promoted to a gate criterion.** Re-scope every negative claim to the instrument that supports it. Now `docs/GATES.md` **G7.3**, and S3 supplies both the model sentence and 286 further logged queries with counts and dates |
| **O40** | **OPEN, and promoted to a gate criterion.** Answer arXiv:2412.18144 by name. Now `docs/GATES.md` **G7.6**, and it has become the whole of R3a |
| **O44** | **OPEN.** Restate Theorem 1's boundedness hypothesis on realised scores rather than on score functions. **Still live**: the re-scoped paper leans on Theorem 1 and Proposition 2 harder than the old one did, and the repair is one sentence |
| **O45** | **PARTLY CLOSED** — see the table above |

### New items booked by session S3

| # | Item | Why | Effort |
|---|---|---|---|
| **O46** | **Audit arXiv:2410.08852, "intermittent quantile tracking".** Surfaced by H3's dead-band screen and **not read** | **It is the nearest thing to an occupant of R3b, which is the paper's headline.** An intermittently updated quantile is a dead band by another name, and R3b's new result is precisely that a dead band with `τ > b/2` loses long-run coverage. *(**`τ > b/2` corrected 2026-08-20 by S4 to `τ > τ*` — the fourth unmarked residual of the superseded boundary, found by the wave-4 instruction critic outside wave 0's sweep list.**)* If that paper states a coverage result for intermittent updating, R3b's boundary claim needs re-positioning before it is printed, not after. **Read it before the submission, and record the verdict whichever way it falls** | Hours |
| **O47** | **Pin the Zanotti version, or quote v3.** arXiv:2506.05776 **v2 and v3 differ in the title and in a load-bearing sentence**: v2 §5 p.26 carries *"the resulting quantiles may primarily capture the stability of the conformal adjustment rather than that of the underlying predictive distributions"*, and **v3 p.24 deletes it** | The sentence is the one the project quotes Zanotti for. Quoting a deleted sentence without a version pin is the citation defect this repository has already committed twice in other forms. Both PDFs were downloaded and read by H5 on 2026-08-20. `audit/REFS_VERIFIED.bib` `zanotti2026smqc` carries the v3 title | Minutes |
| **O48** | **Fetch canonical records for the seven bibliography gaps H5 lists, four of them HIGH.** HIGH: **Zsótér, Buizza & Richardson** (doi 10.1175/2009MWR2960.1), **Ehret** (doi 10.1127/0941-2948/2010/0480), **Pappenberger, Cloke, Persson & Demeritt** (doi 10.5194/hess-15-2391-2011) and **Stankevičiūtė, Alaa & van der Schaar**, *Conformal Time-series Forecasting*, NeurIPS 34:6216–6228, 2021. MEDIUM: Chen, Agarwal, Wierman, Barman & Andrew (SIGMETRICS 2015, doi 10.1145/2796314.2745854) and Chen, Comden, Liu, Gandhi & Wierman (SIGMETRICS 2016, doi 10.1145/2896377.2901464). LOW: Berrisch & Ziel, *CRPS Learning* (doi 10.1016/j.jeconom.2021.11.008) | **The first three are three of the six taken names**, so the paper cannot make its own concession without them (G7.11), and the fourth is what lets the forecast-stability→conformal citation cell be named rather than counted. All are reachable headlessly from Crossref or DBLP; HESS is fully open access. **G7.8 forbids writing any of them from memory** | ~1 h |
| **O49** | **Re-run the institutional-repository leg headlessly.** DTU Orbit, DiVA, MPIDR/PuRe and RePEc were hard-blocked in wave 1 and no zero was recorded from any of them | **This is the class of the project's own worst surprise** — Duerst et al. was an MPIDR working paper, and DTU Orbit is the Pinson group's own repository. The demonstrated headless routes are named in O34, and the strongest of them for this leg is **the Internet Archive Wayback Machine for repository PDFs**, which is how the Delikaraoglou & Pinson PDF was obtained from DTU Orbit, together with **HAL's `text_fulltext` API** and the OpenAIRE and Zenodo metadata APIs. **OpenAIRE indexes Duerst et al. as metadata only, which is exactly why a metadata index would still miss it** | ~2 h |
| **O50** | **Correct the two remaining occurrences of the Andrew et al. Theorem 7 gloss**: `docs/HYPERRESEARCH_REPORT.md` (twice) and `docs/OPEN_QUESTIONS.md` Q4 | Theorem 7 is a **trade-off**, not a one-dimensional free lunch: at fixed θ it gives a constant competitive ratio with **linear** regret, and sublinear regret needs θ growing with `T`, which grows the ratio (arXiv:1508.03769v1 p.10, verified by H5 2026-08-20). `docs/FRAMING.md` §3 and `docs/GATES.md` G3.5 are corrected; these two are not, and the Q4 occurrence is the one that could feed an operator decision | Minutes |

### OI-1 (**CLOSED 2026-08-20, S4**) and OI-2 (**still SUPERSEDED, not answered**)

**`docs/GATES.md` G2-pre recorded two `[OPERATOR INPUT]` items. Both lose their referent under
the re-scope. Superseding an operator item is not answering it, and no automated session may
answer either.**

- **OI-2 — the Hardy (2001) regime-parameter table.** **SUPERSEDED: it has no referent.** The
  re-scoped paper has **no market model**, so there are no regime parameters to transcribe and
  no blocking pre-sweep check to pass. The underlying rule stands and is worth more than the
  item: **proceeding on unverified numbers presented as a citation is not an option**, which is
  `docs/GATES.md` G7.1 generalised. If a later session revives the market arm, OI-2 revives with
  it, unanswered.
- **OI-1 — the movement penalty's functional form, L1 or L2** (`docs/OPEN_QUESTIONS.md` Q7,
  and Tier 1's O4). **SUPERSEDED: it stops being a decision point**, because R3b's experiment
  **sweeps smoother families rather than choosing one** — eleven arms, EMA at several weights,
  dead bands at several thresholds, a running mean and time-varying time constants.
  **Wave 1 nonetheless handed the L1 side a hard new fact, and it is recorded here as
  information for the operator rather than as a decision by this session: the dead band IS the
  L1 form, and it is exactly the family that loses long-run coverage for `τ > b/2`** — strictly;
  `τ = b/2` covers, with miscoverage 1.000000 and `max|E_t| = 0.9·T` beyond the boundary.
  S2's argument on the same side — that condition (4) admits a relay/dead-band saturator
  contributing exactly zero movement inside its band with Theorem 1 applying verbatim — is
  **unaffected and still correct**, because it concerns the saturator inside the integrator and
  this is a dead band on the completed output. **Q7 stays open.**
  - > **CLOSED 2026-08-20 BY SESSION S4 (agent K1). The bullet above is the S3 record and is
    > kept unedited; three of its statements are now corrected.** (i) **Q7 does not stay open** —
    > it was never an operator preference, and it is closed by measurement.
    > (ii) **`τ > b/2` is the null-scorecaster special case, not the law.** The law is
    > **`τ* = sup_x r_t(x) + sup_t q̂_t − b/2`**, with the failing set `(τ*, ∞)` open at the left;
    > at `q̂ ≡ +b/2` the `τ = 1.5` band **covers** (`0.100010`) and at `q̂ ≡ −b/2` even `τ = 0.5`
    > fails. (iii) **The sweep-rather-than-choose framing understates the result**: the sweep is
    > how the family that leaves Corollary 2's radius was identified, and that departure is the
    > paper's claim. **And L2 is not certified by L1's failure** — `w = 0.999` forfeits the rate
    > at the null scorecaster (`623.70` against `14.8155`) while keeping coverage (`0.100035`),
    > and returns `1.000000` at `q̂ ≡ −b/2`. **The dead band may no longer be presented as a
    > design lever anywhere in `paper/` or `docs/`; it is the object of study.**
    > `results/forfeit-variations-20260820T101445Z.json`; `docs/OPEN_QUESTIONS.md` Q7;
    > `docs/GATES.md` G7.9. **No gate is signed by this.**

---

## Session S2 — the placement reduction, and what it changed

*Added 2026-08-19 by session S2, whose wave 1 ran five agents in parallel (D1 verify the
reduction, D2 attack it, D3 read the neighbours, D4 close the hiding places, D5 run the
full-text screen). All five returned. Working records: `research/S2/D1..D5*.json`,
`research/checkpoints/S2-W0-preflight.md`, `research/checkpoints/S2-W1-reduction.md`.*

**The headline of the session is not in this file — it is in `docs/FRAMING.md` §2.2b. In one
line: the reduction to Conformal PID Theorem 1 HOLDS, and R2\* as it was briefed is
substantially wrong around it.** What lands here is the consequences.

### The two Tier-0 items S2 resolved

| # | Item | Resolution |
|---|---|---|
| **O0a2** | Position R2 against Dupuy et al. Theorem 2. | **RESOLVED, and the answer is the one the project must be careful with. Placement B AVOIDS the domination hypothesis; it does not DISCHARGE it.** Dupuy's hypothesis compares partial sums of *two* feedback sequences and exists only because their Eqs. (7)/(8) put the smoothed signal **inside** the integrator: the induction bounds the smoothed sum while long-run coverage is about the raw one, so domination is imposed by hand as the bridge. Under Placement B the integrator's argument is the unmodified indicator, so no smoothed sequence exists and the inequality has no referent. Conformal PID Theorem 1's hypothesis list is exactly three items and contains no domination condition. **The paper may NOT claim to have discharged their assumption.** The only route to "discharge" is the degenerate reading `f ≡ 1{·}`, which is a refusal to make the substitution. `research/S2/D3-neighbours.json`; `docs/GATES.md` G3.11 |
| **O0b** | Attack G3.4(b) on paper — does deployed miscoverage stay monotone in α_t under a one-scalar smoother on `q_t`? | **RESOLVED, and the question was aimed at the wrong condition.** Two agents established independently that **condition (4) constrains `r_t` alone**, so a downstream smoother cannot violate it, and that monotonicity is a *proof route* of BC-ACI's probabilistic argument rather than the thing that breaks. What actually fails is the load-bearing step of Conformal PID's Proposition 2 induction — `c·h(T−1) < E_{T−1} ⟹ q_T ≥ b ⟹ s_T ≤ q_T ⟹ err_T = 0` — because the integrator reaches `b` but an EMA of the output attains it only in the limit of infinitely many consecutive saturated rounds. **And coverage is not lost:** six smoother families returned realised miscoverage 0.1000–0.1002 against α = 0.1 under adversarial scores over T = 2×10⁵. The forfeit is the finite-sample rate — max\|E_t\| = 623.7 against a bound of 14.8 at w = 0.999. `research/S2/D1-reduction.json`, `D3-neighbours.json` |

### New Tier 0 — added by S2, and O27 outranks everything else in this file

| # | Item | Why | Effort |
|---|---|---|---|
| **O27** | **RETIRED 2026-08-20 (S3 re-scope: first half already done by S2; second half retired with R1). Text kept. See the S3 section at the top of this file.** **WITHDRAW the claim that no work prices a matched-marginal path difference through a start-up, ramping or cycling cost**, from `audit/PRIOR_ART.md` §7.9.3 and `docs/FRAMING.md` §8b item 4, and re-state R1's decision leg. **Chen, Yang, Li & Liu, IEEE Tencon-Spring 2013, doi 10.1109/TENCONSPRING.2013.6584502 does exactly that**: same per-period forecast distributions by construction via a Gaussian-copula correlation matrix (Q1), gradient curves of both scenario sets plotted in its Fig. 4 (Q2), **and a per-start start-up cost of \$300–\$4500 in its Table II** with minimum on/off times and ramp rates (Q3, priced). Q1 ∧ Q2 ∧ Q3 ⇒ **OCCUPIED**. | It is a displayed block-quote claim in the audit and a load-bearing instruction in FRAMING, and **it is false**. A reviewer who finds Chen et al. after reading that sentence will not read the rest of the paper charitably. S1 recorded this paper as having no abstract in any index; D4 recovered the abstract from IEEE Xplore's embedded metadata and **all seven figures and tables from Semantic Scholar's figure-extraction service**. | Hours, on paper. Blocks G1 |
| **O28** | **RETIRED 2026-08-20 (S3 re-scope: R1 is dropped). Text kept. See the S3 section at the top of this file.** **Re-state R1 on Q5 — the absence of a coverage object in every matched-marginal decision-value work — as its only structural distinction, and stress-test whether that alone carries a paper.** | Q3 is now occupied outright; Q1 and Q2 were already occupied (Pinson & Girard 2012, Worsnop et al. 2018). **Q5 plus the calendar-time-revision-path object distinction of FRAMING §8b item 1 is all that remains.** If that is not enough, R1 is not a claim. | Days, on paper. Blocks G2 |
| **O37** | **CLOSED 2026-08-20 — SESSION S3 IS THE DECISION. Text kept. See the S3 section at the top of this file.** **Decide what the paper is, given that the placement is occupied three times over and the trade-off is not.** ACT23 state that `q̂` may be any function of the past three times and **deploy a Theta-model scorecaster**; Dupuy et al. publish the generic argument at Appendix A p.15 Eq. 12; Duerst, Schöley, Hellstrand & Myrskylä (MPIDR WP-2024-016) already impose a width-movement constraint inside a Conformal PID scorecaster. What is unoccupied is the **conservation law** — derived independently by two agents this session — the corrected Placement A mechanism, and the turnover motivation. | **This is the successor to O0a2 and it is now the first task.** The paper's contribution has moved from "where to put the penalty" to "what the placement costs you". `docs/FRAMING.md` §2.2b | Days, on paper |

### New items from S2 waves 1

| # | Item | Why | Effort |
|---|---|---|---|
| **O29** | **RETIRED 2026-08-20 (S3 re-scope: R1 is dropped). Text kept. See the S3 section at the top of this file.** Obtain the **body** of Chen, Yang, Li & Liu (2013) with institutional IEEE Xplore access and verify two things: whether the two fast-forward-reduced scenario sets have identical empirical marginals, and the exact scope of the start-up charge. | The only two ways the occupancy verdict could soften. Both cheap with a library card; neither likely to reverse it. | Minutes with access; unobtainable without |
| **O30** | **RETIRED 2026-08-20 (S3 re-scope: R1 is dropped). Text kept. See the S3 section at the top of this file.** Cite **Hong Chen, Yu Lei et al. (2018), doi 10.12783/dteees/appeec2018/23559** alongside Chen et al. (2013) as an independent restatement of the same design five years later. | Removes the "one obscure uncited conference paper" defence. Two groups published this comparison. DEStech has no galley, so it is an abstract-level citation. | Minutes |
| **O31** | **RETIRED 2026-08-20 (S3 re-scope: the placement claim is conceded outright). Text kept. See the S3 section at the top of this file.** **Position R2 against AQA (doi 10.1109/CEEPE69795.2026.11552153)** as well as against Dupuy et al. Theorem 2. AQA anchors the conformal threshold to a weighted estimate of recent score quantiles through a regularisation term **inside the threshold update** — R2's own side of the fork — and claims narrower **and** more stable intervals at 90 % coverage, **empirically, with no theorem**. | The first work in this corpus to claim both ends of R2's pair at once, and a fifth independent instance of the obstacle R2 names. 2026 IEEE, energy-storage domain, which is where R1's producer analogy also lives. | Hours to position; body needs access |
| **O32** | **RETIRED 2026-08-20 (S3 re-scope: the placement claim is conceded outright). Text kept. See the S3 section at the top of this file.** Re-run the three ScienceDirect items, in this order: **doi 10.1016/j.dajour.2026.100725** (gold open access, and the highest risk of the three — prediction-interval **width** driving decentralised online convex optimisation), then 10.1016/j.knosys.2026.116702 and 10.1016/j.iot.2026.101795. | **Headed Chrome defeats IEEE's bot check but NOT ScienceDirect's Turnstile CAPTCHA.** One of the three is gold open access and is therefore trivially obtainable by anyone with a working route; this session did not have one. All three remain title-only screens. | Minutes, with a working route |
| **O33** | **RETIRED 2026-08-20 (S3 re-scope: the placement claim is conceded outright). Text kept. See the S3 section at the top of this file.** Read the **TKDE IPOC extension's theory section** (doi 10.1109/TKDE.2026.3674583) with institutional access, specifically for a validity statement attached to the newly named **"Adaptive Copula Conformal Inference (ACCI)"** module. | The abstract-level prediction that there is no new coverage theorem is **verified** — two regret results plus a Dd-MDP framework. But the extension renames the conformal module from plain ACI to a copula conformal method, and copula conformal prediction has its own validity literature. The residual is small but it went **up**, not down. | Hours, with access |
| **O34** | **REWRITTEN 2026-08-20 BY SESSION S3 UNDER A BINDING OPERATOR POLICY. THE RECOMMENDATION OF HEADED CHROME IS WITHDRAWN — see the block immediately below this table.** Correct the operational route note wherever it appears — `docs/OUTSTANDING.md` O0a, `audit/PRIOR_ART.md` §7.8.1, `docs/FRAMING.md` §8 (corrected 2026-08-20), `docs/GATES.md` *Note on gate ordering* (corrected 2026-08-20). | The inherited rule was over-general in one direction and is now **forbidden** in the other. The publisher facts it recorded stand: a 403 is bot detection **at the ACM Digital Library, which is open access behind it**; **IEEE Xplore and Wiley have a real subscription wall behind the bot wall**; **ScienceDirect adds a Turnstile CAPTCHA**. What changes is the permitted instrument. | Minutes |
| **O35** | **RETIRED 2026-08-20 (S3 re-scope: R1 is dropped). Text kept. See the S3 section at the top of this file.** Cite **Delikaraoglou & Pinson (2014)** and add it to the Pinson tally. | It has R1's matched-marginal generator **and** priced start-up and shut-down costs in one paper, failing only Q2 because it builds a single arm. **This is Pinson's fourth appearance in this audit**, after Van Belle et al. (the C1′ occupant), Pinson & Girard (2012) and Ding et al. (2016). He is a likely reviewer. | Minutes |
| **O36** | **RETIRED 2026-08-20 (S3 re-scope: R1 is dropped). Text kept. See the S3 section at the top of this file.** Hand **Bitran, Haas & Matsuo, "Production Planning of Style Goods with High Setup Costs and Forecast Revisions", *Operations Research* 34(2):226–236, 1986** (118 citations) to the neighbouring-literature leg. | Surfaced by the rolling-horizon sweep, not the hydro sweep. It joins forecast **revision** to a setup cost in 1986 — the calendar-time-revision-path half of R1's object, priced — without matched marginals or a dependence-structure arm. **No sentence in this paper may imply the mechanism is recent.** | Hours |
| **O38** | **Repair the three broken provenance records and the false provenance label**, then re-audit every remaining `note` field in `audit/REFS_VERIFIED.bib` that claims a fetched source. | `research/S1/records/s2_2604.13253.json`, `s2_2511.11567.json` and `s2_2601.10863.json` are each a **174-byte stored HTTP 429 error page**, not a record, and all three bib entries claim *"Record from the arXiv abstract page"* — a source for which no saved record existed anywhere. Separately, `research/S1/A6-postprocessing-coverage.json` labels its Conformal PID quotations *"VERBATIM from fetched PDF"* when `research/raw/` holds exactly one PDF and it is not that paper. **The quotations are verbatim-correct, which is the point: a provenance rule satisfied by a correct answer is not a provenance rule.** Partially repaired in S2 — canonical arXiv records for all five now saved under `research/S2/records/arxiv_*.xml`. | Hours |
| **O39** | **Re-scope every negative claim in the project to the instrument that supports it.** D5 logged **176 full-text queries with hit counts, 28 of them zero-hit, across 14 probed indices**, and found that **11 of 12 methods-level hits would have been missed by abstract search**. | "No full-text hit across N indices and M queries" is a much stronger and much more defensible sentence than "nothing in the literature", and it is now available. It also retires the closing sentence of `paper/sections/related.tex`. **Note the instrument inventory has changed: OpenAlex full text is now a metered paid API** (`429: Insufficient budget`), IA Scholar session-blocks after one request, CORE's anonymous tier discards quotation marks, and Google Scholar blocks silently after ~38 queries with a 302 and no CAPTCHA. What works is **arXiv full-text search at search.arxiv.org** (body snippets, back to 2011, counts saturating around 200–260) and a local PDF-plus-regex corpus. | Days |
| **O40** | **Answer arXiv:2412.18144 by name.** It prints the claim that placing a model in the Conformal PID scorecaster slot *"breaks the theoretical coverage guarantee"*, and **that claim is false** — Theorem 1 quantifies over "any function of the past: x_i, y_i, **q_i**". Three deployed studies leave the slot deliberately empty. | It is the clearest available evidence that the placement is worth **stating** even though it is not **new**, and it converts a conceded contribution into a useful correction of the record. | Hours |
| **O41** | **RETIRED 2026-08-20 (S3 re-scope: retired with G3, not repaired). Text kept. See the S3 section at the top of this file.** **Fix the `docs/GATES.md` G3 numbering defect.** The table lists G3.1–G3.8, then G3.11 and G3.12, then G3.9 and G3.10. | The S2 brief asked for two new criteria at G3.9 and G3.10; both identifiers were already occupied, so S2 added them as **G3.13 and G3.14**. The out-of-order table should be sorted once, carefully, with every cross-reference updated. | Minutes |

#### O34, restated — the binding retrieval policy of 2026-08-20

> **Issued by the operator on 2026-08-20, mid-session, and BINDING ON EVERY LATER SESSION.**
> *"Retrieval is headless and API-based. No GUI browser, no headed Chrome, no Playwright
> `channel="chrome"` or `headless=False`, no `launch_persistent_context`, no route that opens a
> window on the operator's desktop or reads his browser profile. Where a source is unreachable
> without one, it is an INSTRUMENT GAP and is recorded as such — never as a measured zero."*

**What this costs, measured rather than assumed.** Less than it looks. S3's H3 ran the
comparison: Google Scholar served the **identical** HTTP 429 and 3,322-byte `/sorry` page to
headless `curl`, to `hyperresearch fetch` **and** to headed Chrome under a persistent profile,
and DTU Orbit's Cloudflare challenge cleared for none of the three. **The block is host- or
IP-level, and no browser fingerprint defeated it.** The headed route is retained in the record
only as evidence of that.

**The demonstrated headless substitutes. Every one of these has worked on this project, and the
second column says on what.**

| Route | Demonstrated on |
|---|---|
| Direct `curl` with a desktop User-Agent | **The NeurIPS proceedings PDF and every arXiv PDF in the repository** |
| The arXiv API, and `search.arxiv.org` for body text | 286 logged full-text queries in S3 alone, with counts, dates and a zero-is-real flag on every row |
| Crossref, DBLP and Unpaywall for canonical records | The bibliography; **SSRN via Crossref prefix `10.2139`, which sidesteps its 403 wall entirely** |
| The Semantic Scholar anonymous pool with 4 s → 40 s incremental backoff | The 659-paper forward-citation screen, with **no API key** |
| **IEEE Xplore's embedded `xplGlobal.document.metadata` JSON block** — abstract and index terms even when the PDF is gated | **This is how Chen 2013 was resolved** |
| **`figures.semanticscholar.org` figure/table extraction for paywalled PDFs** | **This is how Chen 2013's seven figures and tables came out** |
| **HAL's `text_fulltext` API**, and the OpenAIRE and Zenodo metadata APIs | 52 repository queries in S3; HAL's full-text index cleared ACRC as a near-miss |
| **The Internet Archive Wayback Machine for repository PDFs** | **This is how the Delikaraoglou & Pinson PDF was obtained from DTU Orbit** |
| Author copies on personal or institutional pages | **This is how Ding et al. (2016) was obtained** |

**The recording rule, and it is the half that matters.** A surface that blocks, rate-limits,
challenges or truncates has produced **no measurement**. It is booked as an **instrument gap**,
named, with its signature and its byte count. **A zero may be recorded only from a response that
a minimum-size guard has passed** — S3's `GS_MIN_BYTES = 20000` is the model, and it is what kept
eight blocked Google Scholar probes out of the record. **An instrument gap written down as a
measured zero is a `docs/GATES.md` G7 failure regardless of whether the underlying claim is
true.**

### Added by session S2's wave-4 critics, after the critics overturned the session's own result

| # | Item | Why | Effort |
|---|---|---|---|
| **O42** | **CLOSED AS OCCUPIED 2026-08-20 (S3, agent H1): it is integrator anti-windup with a feedforward path, and the free-until-saturation dichotomy is that field's problem statement. O42 does not come back. Text kept; see the S3 section.** **Run the question the withdrawn conservation law was the degenerate corner of: how much of the integrator's movement can a bounded scorecaster offset, as a function of the budget split `B_q/b` and the severity of the distribution shift, and what does the offsetting cost in the certificate?** Make **deployed travel `Σ\|Δq_t\|`** the movement variable rather than `q̂`'s movement, and let the scorecaster see `E_t`, which iteration (5) explicitly permits. | **This is now the project's best remaining route to a theory result, and it was found by the critic trying to destroy the previous one.** It has the two properties the withdrawn relation lacked — a free parameter and a regime dependence. Measured: a cancelling scorecaster cut deployed travel from **91.2 to 0.21** at `T = 10⁴` with realised miscoverage 0.0953 and the budget clip binding on 24 of 10,000 rounds; **under shift the same construction collapsed to 1.12×**, with the clip binding on 89 %. Nobody in the vault has asked it. `docs/PROTOCOL.md` arm `B2`, now promoted; `research/S2/F1-adversarial.json` | One experiment |
| **O43** | **DISCHARGED 2026-08-20 FOR THE ROWS THE PAPER PRINTS; rows 55–58 of `audit/NUMBERS.md` §11 remain orphaned by design. Still open as `docs/GATES.md` G7.1.** **Regenerate S2's verification numbers from committed code before any of them is printed in a submitted paper.** `audit/NUMBERS.md` §11 books ten of them under a new `verification-run` source; three are already printed in `paper/sections/`. | **The paper currently prints numbers on the authority of a session transcript**, which is the standard `audit/NUMBERS.md` exists to condemn, and `docs/GATES.md` G5.6 requires every number to trace to a `results/` JSON. The numbers are almost certainly right — one was independently re-derived in exact rational arithmetic — but "almost certainly right" is what the provenance rule is for. | Hours, once `src/` exists |
| **O44** | **Restate Theorem 1's boundedness hypothesis on realised scores rather than on score functions.** The theorem quantifies over "score **functions** with outputs in `[−b/2, b/2]`" — a supremum over all `y`, which fails for an absolute-error score on `Y = ℝ` for every finite `b` — while its proof uses only the realised numbers `s_t`. | A reviewer who reads the hypothesis literally will say the paper's own score is out of scope. The repair is one sentence and it is the paper's, not ACT23's, since their experiments have the same feature. `research/S2/D1-reduction.json`, `research/S2/F1-adversarial.json` | Minutes |
| **O45** | **PARTLY CLOSED 2026-08-20 (S3): the OpenReview leg is CLOSED (88 queries, `scorecaster` = 4 notes in the whole index, all read, no occupant). The Google Scholar leg is STILL OPEN and has now defeated two sessions — eight probes, every one a 429 or a 3,322-byte `/sorry`, and NOT ONE zero entered the record; the 50-query battery is armed at `research/S3/ft/gs_battery.py`. The institutional-repository leg is re-opened headlessly as O49.** **Resume the Google Scholar sweep at query 39, and run the OpenReview `api2/notes/search` surface properly.** | **Google Scholar is the surface that produced both of D5's decisive hits and nothing else did**, and it was cut off mid-sweep after ~38 queries by a silent 302 rather than exhausted. OpenReview indexes reviews and rebuttals plus ICLR/ICML 2026 submissions not yet on arXiv — i.e. concurrent work — and wave 4's eleven queries there found no occupant, which is a partial negative worth completing. Third surface: institutional repositories and theses (DTU Orbit, MPIDR, DiVA, HAL), **which is the class of the session's own worst surprise, Duerst et al.** | 1–2 h, 45 min, ~2 h |

### Closed by session S2

| Item | Resolution |
|---|---|
| **O25 hiding place (a)** — the Schaake-shuffle / ensemble-copula-coupling branch of hydrology and reservoir operations | **CLOSED. It does not occupy R1, and the residual is negligible at abstract level.** The branch is 102 papers and its intersection with movement-cost vocabulary is exactly one. Strongest near-miss **Worsnop et al. (2018)**: Q1 at its strongest ("all methods have the same spread after shuffling"), Q2 yes, **Q3 no** — across 23 pages, "commitment", "start-up", "dispatch" and "economic" occur **zero** times and "cost" occurs twice, once inside a reference title. Seven crossed queries returned literal 0. `research/S2/D4-hiding-places.json` |
| **O25b** — resolve Chen, Yang, Li & Liu (2013) | **RESOLVED — and it OCCUPIES.** See O27. S1's "no abstract exists anywhere" was accurate for Crossref, Semantic Scholar and Unpaywall, and is superseded: the abstract is on the IEEE Xplore landing page and reachable by headed Chrome. |
| **O25 hiding place (b), items 1–3** — AQA, the TKDE IPOC extension, Conformal-ABR | **REACHED at abstract-plus-introduction level**, all three completely unreachable in S1. **No PDFs, because IEEE Xplore's paywall is real.** Conformal-ABR confirmed as a non-threat: its "penalizing variation" acts on the **bitrate**, not on the width path. |
| **O25 hiding place (b), items 4–6** — the three Elsevier title-only screens | **NOT CLOSED, but the reason is now documented rather than unknown.** Full Crossref metadata for all three, abstracts for none. See O32. |
| **O25c** — obtain the body of Williams, Peters & Raiszadeh (1985) | **Assessment redone and CONFIRMED AND STRENGTHENED; body NOT obtained**, and it should be treated as needing a library rather than a better crawler — ten routes logged. The arms are **rearrangements**, so the marginal match is an **exact identity**, stronger than any modern work in the corpus. FRAMING §8b item 5 is right but understated, and wrong on uniqueness: Chen 2013 also scores Q1–Q4 and is closer to R1. |
| **O26** — re-run the OpenAlex full-text queries after the budget resets | **CLOSED AS UNRUNNABLE, and replaced by O39.** OpenAlex full text is no longer a free instrument: it returns `429 "Insufficient budget… Add funds"`. The screen was run anyway, by other means. |


## Tier 0 — Blocks the value of everything else

*Added 2026-08-19 by session S1. These sit above Tier 1 because they can each make a large
amount of downstream work worthless, and neither needs a simulator.*

| # | Item | Why it outranks everything | Effort |
|---|---|---|---|
| **O0a** | **CLOSED 2026-08-19. IPOC read, Q5 = no, R2 not occupied.** Its one coverage statement is Gibbs–Candès imported for the **base model's** interval, not the chased one. **The eleven failed routes all assumed the ACM Digital Library's 403 was a paywall; it is Cloudflare bot detection and the library is open access.** A headed system Chrome instance with a persistent profile passes it. **Apply that route to every remaining closed item** — `audit/PRIOR_ART.md` §7.8.7 item 2 names five. | Closed. |
| **O0a2** | **Position R2 against Dupuy et al. Theorem 2** (arXiv:2510.02809 / doi 10.1007/978-3-032-16708-8_17), which proves long-run coverage for an online conformal update built to prevent abrupt threshold changes, and whose Theorem 2 — the case where the width mechanism is driven by the smoothed signal — rests on a domination hypothesis the authors disown as "pretty strong". | **This is now the first task, and it replaces O0a.** R2's contribution is either discharging that assumption or nothing. It needs reading and thinking, not compute. `docs/GATES.md` G3.11. | Days, on paper |
| **O0a3** | **RETIRED 2026-08-20 (S3 re-scope: R1 is dropped). Text kept. See the S3 section at the top of this file.** **Re-argue R1 on Q3 alone, and read Pinson & Girard (2012), doi 10.1016/j.apenergy.2011.11.004, in full.** It matches the full marginal — a strictly stronger control than (coverage, mean width) — across three arms on a real producer, in the reliability-and-sharpness framing, and states the Q4 moral. **Both distinctions R1 was resting on are gone.** | R1 now survives only on the movement-charged decision. Pierre Pinson co-authors both this and the paper occupying C1′, and is a likely reviewer. The probabilistic-forecast-verification line must join the paper's opening. `docs/FRAMING.md` §8b item 1. | Hours to read, then a rewrite |
| **O0b** | **Attack G3.4(b) on paper, before any code exists**: does deployed miscoverage stay monotone in α_t under a one-scalar smoother on `q_t`? | It is the paper's technical contribution if it holds, and it needs no compute. Discovering during implementation that it fails would waste the implementation. BC-ACI (arXiv:2604.13253) Prop. 3 names this exact condition and secures it only by leaving the width mechanism untouched. | Days, on paper |
| **O0c** | **Send the author data request.** `docs/RYAN_EMAIL_DRAFT.md` is written and ready; no contact address is held by this repository. | **The longest external latency in the project.** Everything else can be redone; a reply cannot be hurried. It also bears on R1's Ryan leg, which is contingent on his not printing a per-device path statistic. `docs/OPEN_QUESTIONS.md` Q10. | One email |

---

## Tier 1 — Blocks G1

*Re-ranked 2026-08-19. Four of the seven items in the previous Tier 1 are closed; the
sweep that closed them is recorded in `audit/PRIOR_ART.md` §7 and
`research/S1/A1`–`A7*.json`.*

| # | Item | Why it blocks G1 | Effort |
|---|---|---|---|
| **O3** | **Obtain the body of Jia & Han**, doi 10.1007/978-981-92-2014-4_25. The abstract, the full 26-item reference list, keywords and affiliations were obtained in S1 from the Springer landing page; the body is closed — no open-access location, no preprint, and it is absent from the author's own publication page. | Scored **CLEAR / CLEAR** on the abstract and reference list, so it does not block the verdict — but G1.3 asks for an assessment from the paper, and that criterion is met only partially. It is a five-paper PAKDD workshop-track chapter with one citation, so the residual risk is low. | Hours, with library access |
| **O4** | **CLOSED 2026-08-20 (S4) by measurement, not by operator decision — `docs/OPEN_QUESTIONS.md` Q7. The L1 dead band on the completed threshold is the family that leaves li2025o2cp Corollary 2's admissible radius at `τ* = sup r_t + sup q̂ − b/2`; L2 is the reference arm and is not certified by that role, forfeiting the rate at the null scorecaster and losing coverage at the legal `q̂ ≡ −b/2`.** *(Previous status, kept as the record: "SUPERSEDED 2026-08-20 (S3): this is OI-1, and R3b's experiment sweeps smoother families rather than choosing one. NOT ANSWERED, NOT CLOSED — `docs/OPEN_QUESTIONS.md` Q7 stays open, and the S3 section at the top of this file records the new fact wave 1 handed the L1 side.")* **Decide the movement penalty's functional form**: L1 (proportional ⇒ dead-band) or L2 (quadratic ⇒ linear partial adjustment). `docs/OPEN_QUESTIONS.md` Q7. | The old C-a fork (G1.8) is superseded — the penalty now sits on the width path, which is neither of its two branches. What remains is the form, and G3.4's tractability depends on it: partial adjustment gives measurability trivially and boundedness with lag of order 1/λ. **G3.4 is retired with G3, and the form is settled by `results/forfeit-variations-20260820T101445Z.json` rather than by preference.** | ~~Operator decision~~ **Closed by measurement, S4** |
| **O22** | **Coin a term for the measured quantity.** Every natural name is taken: *smoothed conformal* is randomised smoothing, *stable conformal* is Ndiaye's computational stability, *smoothing-based conformal* is SCD-split (arXiv:2509.22529), *interval stability* is Min et al.'s run-to-run variance, and `Σ\|Δq\|` itself is already published as Zanotti's MQC/SMQC. | A collision makes the paper look unread. `docs/FRAMING.md` §7 item 5, G2.14. | Hours |

### Closed by session S1

| # | Resolution |
|---|---|
| **O1** — run the forward-citation screen of ACI | **CLOSED. It ran, with no API key.** 659 unique citing papers across ACI (557), DtACI (188), Conformal PID (147) and SAOCP (101); 12 candidates; zero OCCUPIED, zero NARROW. The instrument was incremental backoff against the anonymous pool, not a key. **The prescribed OpenAlex fallback would have produced a false negative** — its ACI record carries 27 citations against 557, a 95 % miss. `research/S1/A1-forward-citations.json` |
| **O2** — extend the sweep beyond arXiv | **CLOSED.** 130 queries across 12 venues. COPA swept exhaustively (all nine PMLR volumes, all 243 abstracts term-scanned); seven INFORMS and seven quantitative-finance journals via Crossref; **SSRN reached through Crossref prefix `10.2139`, which sidesteps the 403 wall entirely**. `research/S1/A3-non-arxiv.json` |
| **O2b** — re-run the screen on MECHANISM keywords across domains | **CLOSED, and it is what found the occupant.** 100+ queries across wireless, inventory, datacentre, electricity, robotics/control, advertising, networking, mobility and Bayesian optimisation. `research/S1/A2-cross-domain.json` |
| **O2c** — fetch IPOC | **NOT CLOSED. Escalated to O0a.** |
| **O2d** — read Wang & Hasuike in full | **CLOSED, and the previous assessment was wrong.** Full 8-page text read. It contains **zero** occurrences of "conformal", "coverage", "quantile" or "prediction interval" — it has no interval object at all, and calling it "the closest published neighbour to C2" overstated it. What it does pre-empt is the argument *shape*: Table 1's caption already publishes "Increasing risk aversion does not meaningfully reduce turnover". `research/S1/A4-fulltext.json` |

---

## Tier 2 — Blocks G2, the mechanical critical path

G2 is now "R1 measured under the matched-width design". Everything downstream is blocked on
the simulator, so these remain mechanically urgent — but note the inversion recorded in
`docs/GATES.md` under *Note on gate ordering*: **G3 now carries the paper and G2 is its
motivation.** G2 comes first because the smoother cannot be measured before the producer
exists, not because it is the more important result.

| # | Item | Consequence if left undone |
|---|---|---|
| **O4b** | **RETIRED 2026-08-20 (S3 re-scope: the Ryan replication is out of scope; the draft is not sent). Text kept. See the S3 section at the top of this file.** **ESCALATED to O0a's tier as O0c, and the draft is now written.** Request Ryan's `results.tsv`. Appendix A of arXiv:2608.01494 offers it "available from the author on request" — verbatim text confirmed against the fetched full text — and it almost certainly carries the per-device turnover figures the paper does not print. `docs/RYAN_EMAIL_DRAFT.md`. | Unchanged in substance, and now additionally bears on R1: the Ryan leg of the residual claim rests on his not printing a per-device path statistic, so the ledger could weaken the paper as easily as strengthen it. That is a reason to ask sooner, not later. |
| **O5** | **RETIRED 2026-08-20 (S3 re-scope: the matched-width simulator is not being built). Text kept. See the S3 section at the top of this file.** **Recover `scratchpad/confloor5.py`, or establish that it cannot be recovered.** Ten search commands across the machine returned nothing (`audit/REPRO_C1.md` §1). See `docs/OPEN_QUESTIONS.md` Q1. | This is the highest-value single action available to the project. Recovery collapses most of the current uncertainty; non-recovery means a full rebuild is the critical path and every schedule estimate must be redone. |
| **O6** | **RETIRED 2026-08-20 (S3 re-scope: the sweep the freeze governs is not being run). Text kept. See the S3 section at the top of this file.** **Freeze R1–R13 in a committed configuration before running anything.** `audit/RECONSTRUCTION_SPEC.md` lists thirteen choices the plan leaves open, several of which change the answer. | Rebuilding against a table you have already read is a fitting exercise. If the parameters are tuned until the table appears, the agreement carries no evidential weight and the paper has no answer to "how were these chosen?" |
| **O7** | **RETIRED 2026-08-20 (S3 re-scope: the re-scoped experiment has no ACI producer). Text kept. See the S3 section at the top of this file.** **Resolve R1: is the interval empirical-quantile ACI or a Gaussian proxy?** The plan's `q_t = ŝ_t·z(α_t)` is not split conformal if `z` is a Gaussian quantile. | Highest-severity specification risk. The empirical quantile is a *step function* of α_t, so it has a dead-band for free — which may absorb part of the effect the paper attributes to γ. A conformal-literate reviewer will catch this immediately. |
| **O8** | **DELETED 2026-08-19, with reason. Do not re-open.** The item asked for the Zaffran discriminator in its strict form — does `Σ\|Δq\|` carry information about net growth *conditional on* `E[L]` across the γ grid? | **The test is rank-deficient and cannot be estimated.** Across the only manipulated variable of the abandoned design, both `E[L]` and `Σ\|Δq\|` are approximately affine in γ: the plan's own turnover column gives slopes of 67, 78, 86 and 70 per unit γ, and Zaffran's Theorem 3.1 gives mean length as affine in γ to leading order. Two regressors both affine in the single manipulated variable are collinear, so the conditional coefficient is not identified. The test could be *computed*; it could not be *estimated*, and reporting its output would have been reporting a number that meant nothing. **What replaces it is not a weaker test but a different one:** the matched-width design holds `E[L]` fixed by construction, achieving what the regression was attempting, and the new G2.10 verifies that the construction actually held. See `docs/GATES.md` G2. |
| **O9** | **RETIRED 2026-08-20 (S3 re-scope: matched-width sweep). Text kept. See the S3 section at the top of this file.** **Produce the three untabulated results**: the 0 bps null, the 5 bps intermediate case, and the variance diagnostic. | These are the paper's four strongest stated pieces of evidence and none has a displayed table (`audit/NUMBERS.md` §10). Even recovering the simulator does not recover them. |
| **O10** | **RETIRED 2026-08-20 (S3 re-scope: matched-width sweep). Text kept. See the S3 section at the top of this file.** **Report `Var(q)` (level) alongside `Var(Δq)` (increment).** | The Kelly overbetting channel depends on the dispersion of the scale estimate, not on its period-to-period jitter. As specified, the falsification may target a statistic the competing channel does not depend on (`audit/CLAIMS.md` C-d). |
| **O11** | **RETIRED 2026-08-20 (S3 re-scope: matched-width sweep). Text kept. See the S3 section at the top of this file.** **Replace "flat within 1 SE" with an equivalence test and a stated margin.** | Failure to reject is being reported as refutation, with no power statement. |
| **O12** | **RETIRED 2026-08-20 (S3 re-scope: matched-width sweep). Text kept. See the S3 section at the top of this file.** **Resolve R5, the α_t clipping rule, and report time-at-clip per arm.** | At γ = 0.400 with α = 0.10 the increment is +0.04 on cover and −0.36 on miss, so the headline arm may spend most of its time pinned at an undocumented bound. If so the 4.4-point swing and the 13.7 SE are artefacts of the clip. |
| **O13** | **RETIRED 2026-08-20 (S3 re-scope: matched-width sweep). Text kept. See the S3 section at the top of this file.** **Set the path count from the smallest γ difference the paper intends to claim.** | At 60 paths the γ = 0.020 comparison sits at 2.5 SE — below the plan's own claimed 5× floor, and γ = 0.020 is where a realistic practitioner would sit. |

---

## Tier 3 — Blocks G3 or G4

| # | Item | Consequence |
|---|---|---|
| **O14** | **RETIRED 2026-08-20 (S3 re-scope: G3/G4 retired). Text kept. See the S3 section at the top of this file.** **Test the dead-band asymmetry.** With α = 0.10 the ACI increment is +0.1γ on a cover and −0.9γ on a miss, so a symmetric threshold suppresses one direction only and should produce systematic over-coverage. | Determines whether the naive form of C2 is viable at all. One day's work, and it should be day one of C2. |
| **O15** | **RETIRED 2026-08-20 (S3 re-scope: G3/G4 retired). Text kept. See the S3 section at the top of this file.** **Attempt the Online Balanced Descent potential-function template** for the C-a coverage bound. | The one concrete technique this session surfaced for an otherwise open problem. Converts C-a from "no known approach" to "a template to try". |
| **O16** | **RETIRED 2026-08-20 (S3 re-scope: G3/G4 retired). Text kept. See the S3 section at the top of this file.** **Obtain Chopra (1993), *Journal of Investing* 2(3):51–59** — the primary source for the turnover-versus-input-error figure. Currently known only as reproduced by MacLean–Thorp–Ziemba. | If the paper cites the 1993 turnover antecedent, the primary must be read first. Paywalled; no open version located. |
| **O17** | **RETIRED 2026-08-20 (S3 re-scope: G3/G4 retired). Text kept. See the S3 section at the top of this file.** **Decompose Ryan's cost sweep (0/5/10/20/50 bps) per losing device.** Ryan applies it only to the two aggregate headline configurations, and the depth investigation confirmed his only zero-cost ablation is on an orthogonal axis (Config A versus Config B's drawdown dial), not on the adaptation-speed devices. | This is precisely the analysis Ryan did not do, on real data, and it is the sharpest available statement of F7's contribution. Requires O4b or a rebuild. |
| **O17b** | **RETIRED 2026-08-20 (S3 re-scope: G3/G4 retired). Text kept. See the S3 section at the top of this file.** **Confront the Config A/B counter-evidence.** In Ryan's only published zero-cost ablation, the 2.56 pp growth gap between his two headline configurations is **98.1 % present at zero cost**, with only 1.9 % attributable to turnover at his 5 bps rate — and Ryan attributes it to regime timing rather than to turnover or variance. | This is a published data point pointing **against** F7's implicit prior that activity correlates with growth loss. It is on an orthogonal axis so it does not refute C1, but it is the first thing a reader of Ryan will raise, and the paper must address it rather than omit it. |
| **O18** | **RETIRED 2026-08-20 (S3 re-scope: G3/G4 retired). Text kept. See the S3 section at the top of this file.** **Handle Ryan's disclosed z = 1.2816 versus 1.1503 inconsistency** explicitly and both ways in the replication. | It is disclosed in his paper. Silently correcting it makes the replication not a replication. |

---

## Tier 4 — Blocks G5, or is administrative

| # | Item | Consequence |
|---|---|---|
| **O25** | **RETIRED 2026-08-20 (S3 re-scope: it hunts occupants of R1). Text kept. See the S3 section at the top of this file.** **The three hiding places (`audit/PRIOR_ART.md` §7.8.7). (a) is HUNTED and largely closed — see §7.9; (b) and (c) remain open.** (a) The named unclosed candidate, **Rachunok et al., *Applied Energy* 268:114986** (not 274 or 270 as two agents reported — Crossref gives 268), is **Q1 = NO** and therefore NARROW, not OCCUPIED. But the hunt found **Ding, Pinson, Hu & Song, *IEEE TSTE* 7(1):163–172 (2016)**, which is Q1 ∧ Q2 ∧ Q3 by the letter. (b) The applied conformal layer behind publisher bot walls, starting with **"AQA", doi 10.1109/CEEPE69795.2026.11552153**. (c) **The Schaake-shuffle / ensemble-copula-coupling branch of hydrology and reservoir operations** — `Schaake`, `copula coupling`, `variogram` and `PINAW` still return zero occurrences across the tree. | (a) is answered but not clean: Ding et al.'s movement charge is round-trip efficiency and capacity bounds, not a priced movement cost, and their headline is a null. **R1's decision leg now survives only if it is stated as a PRICED movement cost.** (c) is the sharpest remaining kill: ECC preserves the univariate margins exactly by construction, so every such comparison is automatically matched on coverage and width on a real producer, and reservoir operations charge for changing releases. Routes and exact queries in §7.8.7 and §7.9. |
| **O25b** | **RETIRED 2026-08-20 (S3 re-scope: it hunts occupants of R1). Text kept. See the S3 section at the top of this file.** **Resolve Chen, Yang, Li & Liu, "The value of wind generation temporal correlation information for SBS-UC", IEEE Tencon-Spring 2013, pp. 535–539, doi 10.1109/TENCONSPRING.2013.6584502.** No abstract exists in Crossref, Semantic Scholar or Unpaywall; no open copy; zero citations. | **The single unclosed occupancy risk on R1's Q3 leg.** Its title is an exact framing match — the *value* of temporal-correlation information for scenario-based stochastic unit commitment, a decision carrying start-up and ramping costs. Whether its compared arms share marginals is the entire question. Try the headed-browser route that defeated the ACM Digital Library. | Hours |
| **O25c** | **RETIRED 2026-08-20 (S3 re-scope: it hunts occupants of R1). Text kept. See the S3 section at the top of this file.** **Obtain the body of Williams, Peters & Raiszadeh, *J. Oper. Mgmt* 6(1):69–85 (1985), doi 10.1016/0272-6963(85)90036-1**, and redo its assessment from the paper. | On its abstract it scores the mechanism on Q1–Q4 **in 1985**: demand sequences rearranged to differ only in serial correlation, evaluated by lot-sizing rules with a real setup cost. Its inputs are deterministic sequences and it has no interval or coverage object, so it does not occupy R1 — **but it must be cited, and no sentence in the paper may imply the mechanism is recent.** | Hours |
| **O26** | **Re-run the OpenAlex full-text queries after the budget resets.** Not one of the named full-text queries ran in either the retrieval wave or the adversarial wave. | **Every "nothing in the literature" statement in this project is abstract-level only.** Full-text search is the only instrument that sees a smoother in a methods section, and the hole is demonstrably non-empty. |
| **O23** | **RETIRED 2026-08-20 (S3 re-scope: the rewrite supersedes the measured overrun). Text kept. See the S3 section at the top of this file.** **`paper/sections/related.tex` overruns its budget: 315.2 pt measured against a 650.4 pt NeurIPS text height = 0.485 pages, against a 0.3-page target.** Deleting both one-clause blocks still leaves roughly 0.38 pages, so the target is not reachable with every must-cite present. | In a 4-page body the section is spending about 0.18 pages more than budgeted, and it must come from another section or from a decision to drop a citation. The cut candidates, in the order they should be considered: the three one-clause insurance citations (Jia & Han, Lin–Delage–Chan, Zhu–Yan–Gao); then compressing the Ryan sentence, which currently carries four numbers. **None of the forecast-stability citations may be cut** — `docs/GATES.md` G3.7 makes them load-bearing, and without them the paper reads as a rediscovery. A ranked list with measured savings is in `research/S1/B2-notes.md`. |
| **O24** | **`audit/REFS_VERIFIED.bib` `note` fields contain unescaped `_` and raw math**, which will break a `plainnat` bibliography build. | Caught by the related-work drafter and confirmed by the instruction critic. Cheap to fix and it will otherwise surface as a confusing build failure at G5. |
| **O19** | **RETIRED 2026-08-20 (S3 re-scope: ML×OR is out of the venue set). Text kept. See the S3 section at the top of this file.** Resolve the three open ML×OR compliance questions: in-person presentation requirement, reciprocal reviewing clause, and whether an arXiv preprint affects eligibility under "previously published works". | Desk-rejection risk. `docs/VENUE.md` §4. |
| **O20** | **CLOSED 2026-08-20 (S3): 4–7 pages plus references, double-blind — the call was reachable through the site's own `content.js`. See the S3 section.** Verify the TS-LIMITS page limit and anonymity regime. Its site is JavaScript-rendered and the call text could not be retrieved by any method available this session. | Only matters if TS-LIMITS is chosen. |
| **O21** | Rebuild the paper's reference list from `audit/REFS_VERIFIED.bib` rather than from `docs/PLAN_ORIGINAL.md`. | The plan's list has a 31.8 % failure rate, a duplicate entry, an entry with no locator, and an entry cited for the opposite of what it says. |

---

## Resolved during this session

Recorded so a later session does not re-open them.

| Item | Resolution |
|---|---|
| NeurIPS 2026 style files not fetched | **Resolved.** Fetched from the official author kit; `sglblindworkshop` confirmed at source to set `\@anonymousfalse`. `paper/`, `docs/PROVENANCE.md`. |
| MacLean–Thorp–Ziemba unresolvable as cited | **Resolved** to the 2010 paper "Good and bad properties of the Kelly criterion", and read. Its content does not support what the plan attributes to it. |
| Whether Conformal Decision Theory's trading experiment is zero-cost synthetic GBM | **Resolved: yes**, verified against the paper's own text. The differentiation from CDT holds. |
| Whether Vaze's Theorem 7 says what the plan claims | **Resolved: substantially, with a correction.** Right rate, right theorem number; the tight bound is on dynamic regret, and the author's own Remark 11 says the coverage-side bound is not tight. |
| Whether the switching-cost literature already has a coverage guarantee | **Resolved: no.** Full-text search across four papers found zero occurrences of "conformal", "coverage" or "prediction interval" in the statistical sense. |
| Whether "Expert-Calibrated Learning for Online Optimization with Switching Costs" scoops C2 | **Resolved: no.** "Calibration" there is learning-augmented expert combining, not statistical coverage. |
| Whether Ryan explains the anomaly | **Resolved: yes, in a hedged and unmeasured form**, and not via turnover. The plan's "nobody has explained it" is false; F7's turnover-specific account is not scooped. |

---

## Added by session S3, waves 2, 4 and 5 — the corrections that arrived after wave 1

*These reached `docs/` only at wave 5. Wave 4's instruction critic caught that they were living
in gitignored `research/` alone, which is the exact defect this file exists to prevent. Recorded
here so a later session finds them without reading an ignored directory.*

| # | Item | Status |
|---|---|---|
| **O51** | **R3c's last disconnected cell is FALSIFIED, and no disconnection may be claimed between any pair of the four literatures.** Semantic Scholar's *citations* endpoint for `kalai2005lazy` returns **875 citing works, three of them online conformal** — `chen2023ipoc` (**which this project's own paper cites**), arXiv:2410.02561, and one 2026 cloud-systems paper classified by content. Found by **H6**, verified independently by the orchestrator. `research/S3/ft/h6/s2b_results.json`; `research/S3/H6-repositories.json`. | **CLOSED as a claim; withdrawn from the paper.** The methodological lesson is the item: H5 measured *outgoing* references and found the cell empty, H6 measured *incoming* citations and found it occupied. **One direction of one instrument is not the literature.** | **CLOSED 2026-08-20 BY SESSION S4, AND CLOSED IN THE RIGHT ORDER.** S4 agent K3 re-ran the sweep and found the falsification HAD reached `docs/FRAMING.md` and `docs/GATES.md` — `H6|875|Kalai` now returns **25 hits across 9 tracked files**, against the **zero** `docs/S3_REPORT.md` §5 item 1 records — but that **three unmarked stale statements still stood**: `docs/GATES.md` G7.10 printed the superseded `900` / `1.4 %` denominator against the corrected `862` / `1.5 %`; `audit/PRIOR_ART.md` §7.3 asserted *"the bridge between the two literatures is unbuilt"* with no marker, in the one audit file whose convention is inline marking; and `docs/FRAMING.md` §0 still summarised the four-way disconnection as *"false, leaving one cell"*. **K3 recommended not closing O51 until those were applied, on the ground that closing it while the residue stood would be the third repetition of the failure O51 documents. That recommendation was followed.** All three are fixed, plus `docs/S1_REPORT.md` §7.3's equivalent. Verification after the fixes: absence-claim greps over `paper/` return **0** on all twelve patterns (`disconnect`, `does not cite`, `uncited`, `non-citation`, `sparse`, `no cross`, `no overlap`, `no bridge`, `four-literature`, `claim no disconnection`, `no connection`, `do not cite`). The paper no longer prints *"We claim no disconnection"* either — a bolded denial of a claim the paper does not make was the last residue of the contribution. Evidence: `research/S4/K3-demotion.json` (33 classified hits, 24 zero-hit greps). **A second instance of the same failure mode was found in passing and is recorded rather than quietly fixed: the tracked paper printed "two" online-conformal citers of Kalai–Vempala while every tracked doc printed "three".** Moot now — the sentence is deleted — but two tracked surfaces disagreed on the headline number of the very finding that killed R3c.
| **O52** | **R3b's boundary is not `τ > b/2` in general.** The law is **`τ* = sup r_t + sup q̂ − b/2`**; `b/2` is the null-scorecaster corner. Both constant scorecasters `q̂ ≡ ±b/2` are legal and move it — at `+b/2` the failing arm covers, at `−b/2` the failure is worse than measured and reaches arms printed as covering. The failing set is unbounded above, not `(b/2, b]`. Found by **F1**. **The '31 of 32 grid points' verification recorded here is WITHDRAWN 2026-08-20 by session S4 as untraceable** — it rests on one line of gitignored `research/S3/patch-log.json`, the grid is not reconstructible from `results/`, and G7.1 forbids printing an untraceable number. **Replaced by a traceable 19-of-19 check** recomputed from `results/forfeit-variations-20260820T101445Z.json`: three widths under each of five (saturator, scorecaster) settings plus four wider bands, no counterexample. O52's remaining open leg is that **no bisection in `τ` at fixed `(sup r, sup q̂)` is booked into `results/`**, so each edge is bracketed by three tested widths rather than located. | **APPLIED to the paper and to `docs/GATES.md` G7.9.** The boundary at `μ = 1, q̂ = 0` is exactly O2CP Corollary 2's admissible radius, so the measurement shows **the conceded result is tight** rather than locating a new boundary. |
| **O53** | **ACT23's own tangent integrator dissolves the headline.** They state they use it *"in all our experiments"*. Under it the failing dead band **covers** (0.100001), `623.70` falls to **20.10**, and the i.i.d. control falls from 0.249376 to 0.100025. Run by **F1**. | **OPEN and load-bearing.** `paper/sections/limitations.tex` previously said "nothing here says what that would do"; it now must say what was measured. **A later session should run the tangent integrator as a first-class arm rather than as a caveat.** |
| **O54** | **The project's reading of Duerst et al. (MPIDR WP-2024-016) was wrong.** S2 made it a load-bearing witness for "a width-movement constraint inside a Conformal PID scorecaster". The full text shows monotonicity in **forecast horizon** — the authors' own reason is *"as the forecast length increases, so does the forecast uncertainty"* — inside a forecast-path calibration pipeline. `"online"` occurs once, in a URL. They do adopt the scorecaster and cite Angelopoulos explicitly. | **CORRECTED** in the paper and in `audit/REFS_VERIFIED.bib`. The slot is still occupied; the movement reading is withdrawn. **Correcting it REMOVES the nearest known threat to R3b.** |
| **O55** | **`gao2025coloke`** (arXiv:2511.12760, *Conformal Online Learning of Deep Koopman Linear Embeddings*) runs the online conformal recursion and gates **model** updates on the conformity score. Its assumption **(A3) bounds the accumulated conformity thresholds and is supported by a figure rather than derived** — the quantity R3b measures diverging. | **CITED.** Not an occupant: `"miscoverage"`, `"marginal coverage"` and `"scorecaster"` each occur **0** times in its full text. |
| **O56** | **The `[0.821, 0.979]` figure at `T = 2500` has no `results/` trace.** F1 reproduced it — [0.8210, 0.9790] — **but only with two constants the paper does not state.** | **OPEN.** Either state the constants or drop the figure. It is the one untraced number in the body. | **CLOSED BY DELETION 2026-08-20, SESSION S4 (agent K2).** The figure is gone from `paper/sections/limitations.tex`. What survives is the rate, which derives by hand from the printed `(c·h(T)+1)/T` at `h(t) = t/log t` and asserts no constant: `O(1/log T)` rather than `O(1/T)`. **No untraced number remains in the body** — K2 also deleted `0.100025` (the i.i.d. control under the tangent, which lived only in gitignored `research/S3/f1_probe_iid.json`) and "coverage survives to `τ = b`" (a prediction from the law printed as a measurement; no band of width `b` was ever run at `q̂ = +b/2`). G7.1 is applied as written: a number that cannot be traced is deleted, not footnoted.
| **O57** | **The paper's count of taken names is wrong.** It prints six; its own Table 2 caption names ten, eleven with IACER, and F1 adds path length / variation budget, total variation, and forecast-revision volatility (arXiv:2510.04487). | **OPEN.** A printed count the paper's own caption contradicts is worse than no count. |
| **O58** | **Two search-instrument claims are unsafe.** `"windup" ∧ "conformal"` returns **9 hits** on `search.arxiv.org`, the index the sentence names — the zero came from the arXiv API. And `search.arxiv.org`'s phrase matching **is not exact**: F1 showed it returns a paper for a phrase absent from all 137,412 characters of that paper, so the printed `192` is an upper bound. | **OPEN.** Both clauses were candidates for cutting to pay for O55. |
| **O59** | **Four waves were not committed or pushed as they completed**, against the brief's standing instruction. `HEAD` and `origin/main` both sat at S2's last commit through waves 1–4. | **CLOSED at wave 5.** Recorded rather than quietly fixed; the cause was a mid-session connectivity failure followed by interleaved wave-3 and wave-5 edits, and the honest statement is that the instruction was not followed. |
