# Outstanding items

Every unresolved technical item, ranked by whether it blocks a gate. Items requiring an
operator decision rather than work are in `docs/OPEN_QUESTIONS.md` and are cross-referenced
here.

Ranking is by **blocking status first, then by consequence if left undone** — not by
effort.

**Re-ranked 2026-08-19 by session S1**, after the prior-art sweep found the first claim
occupied. Read `docs/FRAMING.md` first: the claims these items serve are not the claims
most of them were written against. A new **Tier 0** sits above everything, holding the
three items that can each make a large amount of downstream work worthless and none of
which needs a simulator.

---

## Tier 0 — Blocks the value of everything else

*Added 2026-08-19 by session S1. These sit above Tier 1 because they can each make a large
amount of downstream work worthless, and neither needs a simulator.*

| # | Item | Why it outranks everything | Effort |
|---|---|---|---|
| **O0a** | **Read IPOC** — Chen, Luo, Huang, Jiang, Shi, Zhang & Gao, KDD 2023, doi 10.1145/3580305.3599396, pp. 202–212, and its extension, IEEE TKDE 38(5):3277–3290, doi 10.1109/TKDE.2026.3674583. **Eleven retrieval routes failed** in S1: ACM DL returns 403 to direct fetch, to a real browser and to a server-side fetch; ResearchGate 403; Unpaywall reports it closed; no arXiv preprint despite the first author having four others; nothing on the authors' pages; IEEE Xplore is JavaScript-gated. | Its abstract claims validation "through sublinear regret analysis and satisfaction of confidence interval requirements", and the extension states "The chasing regret of the Chasing Oracle is O(L_c)" — a coverage-type guarantee and an explicit movement cost in one sentence. **If that guarantee quantifies over the movement-constrained object, R2 is occupied and the paper has no headline.** This is the single question that could make the entire build pointless, and it costs a library login. | One institutional login |
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
| **O4** | **Decide the movement penalty's functional form**: L1 (proportional ⇒ dead-band) or L2 (quadratic ⇒ linear partial adjustment). `docs/OPEN_QUESTIONS.md` Q7. | The old C-a fork (G1.8) is superseded — the penalty now sits on the width path, which is neither of its two branches. What remains is the form, and G3.4's tractability depends on it: partial adjustment gives measurability trivially and boundedness with lag of order 1/λ. | Operator decision |
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
| **O4b** | **ESCALATED to O0a's tier as O0c, and the draft is now written.** Request Ryan's `results.tsv`. Appendix A of arXiv:2608.01494 offers it "available from the author on request" — verbatim text confirmed against the fetched full text — and it almost certainly carries the per-device turnover figures the paper does not print. `docs/RYAN_EMAIL_DRAFT.md`. | Unchanged in substance, and now additionally bears on R1: the Ryan leg of the residual claim rests on his not printing a per-device path statistic, so the ledger could weaken the paper as easily as strengthen it. That is a reason to ask sooner, not later. |
| **O5** | **Recover `scratchpad/confloor5.py`, or establish that it cannot be recovered.** Ten search commands across the machine returned nothing (`audit/REPRO_C1.md` §1). See `docs/OPEN_QUESTIONS.md` Q1. | This is the highest-value single action available to the project. Recovery collapses most of the current uncertainty; non-recovery means a full rebuild is the critical path and every schedule estimate must be redone. |
| **O6** | **Freeze R1–R13 in a committed configuration before running anything.** `audit/RECONSTRUCTION_SPEC.md` lists thirteen choices the plan leaves open, several of which change the answer. | Rebuilding against a table you have already read is a fitting exercise. If the parameters are tuned until the table appears, the agreement carries no evidential weight and the paper has no answer to "how were these chosen?" |
| **O7** | **Resolve R1: is the interval empirical-quantile ACI or a Gaussian proxy?** The plan's `q_t = ŝ_t·z(α_t)` is not split conformal if `z` is a Gaussian quantile. | Highest-severity specification risk. The empirical quantile is a *step function* of α_t, so it has a dead-band for free — which may absorb part of the effect the paper attributes to γ. A conformal-literate reviewer will catch this immediately. |
| **O8** | **DELETED 2026-08-19, with reason. Do not re-open.** The item asked for the Zaffran discriminator in its strict form — does `Σ\|Δq\|` carry information about net growth *conditional on* `E[L]` across the γ grid? | **The test is rank-deficient and cannot be estimated.** Across the only manipulated variable of the abandoned design, both `E[L]` and `Σ\|Δq\|` are approximately affine in γ: the plan's own turnover column gives slopes of 67, 78, 86 and 70 per unit γ, and Zaffran's Theorem 3.1 gives mean length as affine in γ to leading order. Two regressors both affine in the single manipulated variable are collinear, so the conditional coefficient is not identified. The test could be *computed*; it could not be *estimated*, and reporting its output would have been reporting a number that meant nothing. **What replaces it is not a weaker test but a different one:** the matched-width design holds `E[L]` fixed by construction, achieving what the regression was attempting, and the new G2.10 verifies that the construction actually held. See `docs/GATES.md` G2. |
| **O9** | **Produce the three untabulated results**: the 0 bps null, the 5 bps intermediate case, and the variance diagnostic. | These are the paper's four strongest stated pieces of evidence and none has a displayed table (`audit/NUMBERS.md` §10). Even recovering the simulator does not recover them. |
| **O10** | **Report `Var(q)` (level) alongside `Var(Δq)` (increment).** | The Kelly overbetting channel depends on the dispersion of the scale estimate, not on its period-to-period jitter. As specified, the falsification may target a statistic the competing channel does not depend on (`audit/CLAIMS.md` C-d). |
| **O11** | **Replace "flat within 1 SE" with an equivalence test and a stated margin.** | Failure to reject is being reported as refutation, with no power statement. |
| **O12** | **Resolve R5, the α_t clipping rule, and report time-at-clip per arm.** | At γ = 0.400 with α = 0.10 the increment is +0.04 on cover and −0.36 on miss, so the headline arm may spend most of its time pinned at an undocumented bound. If so the 4.4-point swing and the 13.7 SE are artefacts of the clip. |
| **O13** | **Set the path count from the smallest γ difference the paper intends to claim.** | At 60 paths the γ = 0.020 comparison sits at 2.5 SE — below the plan's own claimed 5× floor, and γ = 0.020 is where a realistic practitioner would sit. |

---

## Tier 3 — Blocks G3 or G4

| # | Item | Consequence |
|---|---|---|
| **O14** | **Test the dead-band asymmetry.** With α = 0.10 the ACI increment is +0.1γ on a cover and −0.9γ on a miss, so a symmetric threshold suppresses one direction only and should produce systematic over-coverage. | Determines whether the naive form of C2 is viable at all. One day's work, and it should be day one of C2. |
| **O15** | **Attempt the Online Balanced Descent potential-function template** for the C-a coverage bound. | The one concrete technique this session surfaced for an otherwise open problem. Converts C-a from "no known approach" to "a template to try". |
| **O16** | **Obtain Chopra (1993), *Journal of Investing* 2(3):51–59** — the primary source for the turnover-versus-input-error figure. Currently known only as reproduced by MacLean–Thorp–Ziemba. | If the paper cites the 1993 turnover antecedent, the primary must be read first. Paywalled; no open version located. |
| **O17** | **Decompose Ryan's cost sweep (0/5/10/20/50 bps) per losing device.** Ryan applies it only to the two aggregate headline configurations, and the depth investigation confirmed his only zero-cost ablation is on an orthogonal axis (Config A versus Config B's drawdown dial), not on the adaptation-speed devices. | This is precisely the analysis Ryan did not do, on real data, and it is the sharpest available statement of F7's contribution. Requires O4b or a rebuild. |
| **O17b** | **Confront the Config A/B counter-evidence.** In Ryan's only published zero-cost ablation, the 2.56 pp growth gap between his two headline configurations is **98.1 % present at zero cost**, with only 1.9 % attributable to turnover at his 5 bps rate — and Ryan attributes it to regime timing rather than to turnover or variance. | This is a published data point pointing **against** F7's implicit prior that activity correlates with growth loss. It is on an orthogonal axis so it does not refute C1, but it is the first thing a reader of Ryan will raise, and the paper must address it rather than omit it. |
| **O18** | **Handle Ryan's disclosed z = 1.2816 versus 1.1503 inconsistency** explicitly and both ways in the replication. | It is disclosed in his paper. Silently correcting it makes the replication not a replication. |

---

## Tier 4 — Blocks G5, or is administrative

| # | Item | Consequence |
|---|---|---|
| **O19** | Resolve the three open ML×OR compliance questions: in-person presentation requirement, reciprocal reviewing clause, and whether an arXiv preprint affects eligibility under "previously published works". | Desk-rejection risk. `docs/VENUE.md` §4. |
| **O20** | Verify the TS-LIMITS page limit and anonymity regime. Its site is JavaScript-rendered and the call text could not be retrieved by any method available this session. | Only matters if TS-LIMITS is chosen. |
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
