# Outstanding items

Every unresolved technical item, ranked by whether it blocks gate G1. Items requiring an
operator decision rather than work are in `docs/OPEN_QUESTIONS.md` and are cross-referenced
here.

Ranking is by **blocking status first, then by consequence if left undone** — not by
effort.

---

## Tier 1 — Blocks G1

G1 is "prior-art verdict accepted; framing locked; venue chosen". These four must be
resolved before the project commits to what it is claiming.

| # | Item | Why it blocks G1 | Effort |
|---|---|---|---|
| **O1** | **Run the forward-citation screen of Gibbs–Candès ACI**, filtered for cost, turnover, trading and execution. Needs a Semantic Scholar API key; the API returned HTTP 429 on every call this session, and OpenAlex's citation coverage for this paper is visibly incomplete (27 citations recorded for a paper with far more). | This is the single instrument that indexes across venue types. Without it the novelty verdict rests on an arXiv-centric sweep that has already been shown to miss the closest-titled work in the field. | Hours, once a key exists |
| **O2** | **Extend the prior-art sweep beyond arXiv** — Springer LNCS, INFORMS journals, quantitative-finance journals, SSRN (403 on every direct endpoint this session). | Jia & Han (PAKDD 2026) was missed for exactly this reason. The blind spot is systematic, not incidental. | Days |
| **O2b** | **Re-run the prior-art screen on MECHANISM keywords across application domains**, not on conformal-plus-finance. Two works were missed this session by screening on domain: one about evaluation metrics, one in wireless sensing. | The mechanism — a moving uncertainty estimate driving a decision that pays to move — recurs in wireless scheduling, inventory control, data-centre right-sizing and electricity dispatch. A domain-screened sweep will keep missing it. | Days |
| **O2c** | **Fetch IPOC (KDD 2023, doi 10.1145/3580305.3599396).** Non-arXiv; combines online chasing, a movement-cost framework, with conformal-style intervals and regret guarantees. Surfaced by a partial OpenAlex citation pull. | Closest known unexamined neighbour to C2 outside arXiv. | Hours |
| **O2d** | **Read Wang & Hasuike (arXiv:2605.01176) in full.** `audit/PRIOR_ART.md` calls it the single most important comparison for C2 and the verdict still rests on its abstract. | The nearest published neighbour to C2 has not actually been read. | Hours |
| **O3** | **Obtain Jia & Han, doi 10.1007/978-981-92-2014-4_25, in full text** and assess its proximity to C1 and C2 from the paper rather than the abstract. Springer serves a JavaScript challenge to every direct fetch. | It is the closest-titled published work to F7 and one month older. Its abstract suggests it does not sweep adaptation rate against turnover, but that is an inference from an abstract. | Hours |
| **O4** | **Decide the C-a fork**: dead-band on the quantile update, or on the decision map. See `docs/OPEN_QUESTIONS.md` Q4. | C2's novelty, its risk, its theorem and its page budget all follow from this. Deciding it after implementation begins wastes the implementation. | Operator decision |

---

## Tier 2 — Blocks G2, the critical path

G2 is "C1 reproduced and hardened". Everything downstream is blocked on it, so in practice
these are the most urgent items even though they do not block G1.

| # | Item | Consequence if left undone |
|---|---|---|
| **O4b** | **Request Ryan's `results.tsv` from the author.** Appendix A of arXiv:2608.01494 states it is "available from the author on request", and it almost certainly contains the per-device turnover figures that the paper itself does not publish. | **The cheapest high-value action available to this project.** The depth investigation established that Ryan's published tables cannot discriminate the variance channel from the turnover channel, because per-device turnover is never printed. That single file could settle the paper's central dispute on real multi-asset data, at the cost of one email, without rebuilding anything. | One email |
| **O5** | **Recover `scratchpad/confloor5.py`, or establish that it cannot be recovered.** Ten search commands across the machine returned nothing (`audit/REPRO_C1.md` §1). See `docs/OPEN_QUESTIONS.md` Q1. | This is the highest-value single action available to the project. Recovery collapses most of the current uncertainty; non-recovery means a full rebuild is the critical path and every schedule estimate must be redone. |
| **O6** | **Freeze R1–R13 in a committed configuration before running anything.** `audit/RECONSTRUCTION_SPEC.md` lists thirteen choices the plan leaves open, several of which change the answer. | Rebuilding against a table you have already read is a fitting exercise. If the parameters are tuned until the table appears, the agreement carries no evidential weight and the paper has no answer to "how were these chosen?" |
| **O7** | **Resolve R1: is the interval empirical-quantile ACI or a Gaussian proxy?** The plan's `q_t = ŝ_t·z(α_t)` is not split conformal if `z` is a Gaussian quantile. | Highest-severity specification risk. The empirical quantile is a *step function* of α_t, so it has a dead-band for free — which may absorb part of the effect the paper attributes to γ. A conformal-literate reviewer will catch this immediately. |
| **O8** | **Run the Zaffran discriminator in its STRICT form**: does `Σ\|Δq\|` predict net growth **conditional on** `E[L]` across the γ grid? Not the weak form ("is turnover monotone in γ") — that discriminates nothing, because the plan's own turnover column is already approximately affine in γ (slopes 67, 78, 86, 70 per unit γ), the same functional form Zaffran proves for mean length. | Still cheap, and now actually decisive. C1's entire defence is that turnover is a *variation* functional where Zaffran's is a *level* functional. If `Σ\|Δq\|` adds nothing over `E[L]`, that defence fails and C1 reduces to an existing theorem times a cost rate. This is the paper's load-bearing assumption and it has never been measured. |
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
