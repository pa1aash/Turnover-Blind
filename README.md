# Where the Admissible Radius Binds

**A correction and a measured boundary in online conformal prediction.**
Internal project identifier: F7. Repository name `Turnover-Blind` is historical and
predates the current claim set; it is kept so that existing clones and links keep working.

**Read `docs/FRAMING.md` before anything else.** It is the governing document: it states
what is claimed, what is conceded, what has been withdrawn, and the forbidden constructions
(§3) that every sentence in `paper/` is checked against. Where this file and `docs/FRAMING.md`
disagree, `docs/FRAMING.md` wins.

## What the paper claims — two things, and no third

**R3a — a correction of the published record.** The literature contains both halves of a
contradiction about the same object and prints them under overlapping authorship.
arXiv:2412.18144 states of Conformal PID that using a scorecaster *"breaks the theoretical
coverage guarantee"*. arXiv:2508.13362 Corollary 2, whose first and last authors are the two
authors of that paper, folds a bounded predictable perturbation into the deployed threshold,
observes that the result has exactly Conformal PID's error-integration form, and concludes
that the saturation result applies. The two halves are not joined in any document this
project's instruments reached, and practitioners act on the first. **This paper joins them
and claims neither the placement nor the derivation** — both are prior art (Angelopoulos,
Candès & Tibshirani 2023 Theorem 1; Li, Menacho & Rodríguez 2025 Corollary 2; AcMCP). It is
ordinary self-correction under overlapping authorship, and the paper says so about the
record, never about the people. This is one paragraph and a real service. It is not a
theorem and is not dressed as one.

**R3b — a tightness result on someone else's admissible set.** O2CP Corollary 2 proves that a
predictable modification of the deployed Conformal PID threshold **retains** Proposition 2's
bound while it stays inside a ball of radius `μ_t(b/2 − |q̂_t|)`. This paper exhibits one legal
perturbation that **leaves** that ball — an L1 dead band on the *completed* threshold — and
locates the edge: `τ* = sup_x r_t(x) + sup_t q̂_t − b/2`. Past it, realised miscoverage is
`1.000000` against `α = 0.1` while the saturation condition fires on every round, so what
fails is not the saturation hypothesis but Proposition 2's other one. **The published
sufficient condition is therefore necessary there, not merely sufficient**, and the price of
leaving the set is coverage rather than the rate.

**Two claims, and the count stops there.** An earlier four-literature disconnection claim (R3c) was
falsified inside session S3 by this project's own agent and is demoted to descriptive related
work. The earlier decision-cost claim (net log growth, position sizing, market series,
turnover) is **dropped**, not compressed — see `docs/FRAMING.md` §2.2 and §5 for the shape of
that loss. A conservation law written in session S2 was withdrawn by this project's own critic
four hours later.

## What is conceded, by name

The placement of a penalty in the scorecaster slot; the derivation that it retains the bound;
the smoother as an object; the arithmetic of `Σ|Δq_t|` and every natural name it already has
across four vocabularies; and both readout forms — quadratic cost ⇒ linear partial adjustment
(Gârleanu & Pedersen 2013), proportional cost ⇒ dead band (Constantinides 1986; Davis &
Norman 1990, **not** Gârleanu & Pedersen, who explicitly distinguish themselves from no-trade
strategies). The concession list with locators is `docs/GATES.md` G7.4 and G7.5, and it is
printed in the paper rather than footnoted.

## What is measured, and what it does not say

Measured under one deterministic adversary with the tie convention fixed, `b = 2`, `α = 0.1`,
`h(t) = log(t+2)`, `c = 1`, to `T = 10⁶`:

- At the harness's null scorecaster, a partial adjustment at `w = 0.999` forfeits Proposition 2's
  rate — `max|E_t| = 623.70` against a bound of `14.8155` — while **keeping** coverage, at
  `0.100035`. A dead band past `τ*` loses coverage outright, at `1.000000`.
- **Neither form is safe by construction.** `τ*` moves with both the saturator and the
  scorecaster. Under the equally legal constant scorecaster `q̂ ≡ −b/2`, Corollary 2's radius
  is `0` and both families return `1.000000`; under `q̂ ≡ +b/2` the dead band that fails at
  the null scorecaster covers. That is precisely why the result is a tightness statement about
  the radius and **not** a safety certificate for the partial-adjustment form.
- **"Smoothing loses coverage" is refuted by this project's own control arms**, which return
  realised miscoverage in `0.099940–0.100060`. Both directions are stated, and neither is
  stated unqualified (`docs/GATES.md` G7.9).
- No dead band is recommended as a design. It appears only as the object of study whose
  failure is characterised.

The claim is **not** an impossibility result, **not** a coverage floor, and **not** a claim
about a fundamental limit; `docs/FRAMING.md` §3 forbids that grammar and gives the operational
replacement rule — replace every quantifier with a measurement.

## Status

**Re-scope stage.** The re-scoped paper is a four-page workshop note carrying R3a and R3b.
The live gate is `docs/GATES.md` **G7** (G7.1–G7.12); G2, G2-pre, G3 and G4 are retired with
their reasons recorded. **No gate in this project may be recorded as passed or signed by an
automated session; only the operator signs.** Nothing in this repository asserts that any gate
has been met.

**The venue is `[OPERATOR INPUT]` and stays open** (`docs/OPEN_QUESTIONS.md` Q3,
`docs/GATES.md` G1.7). `docs/VENUE.md` records the analysis; on scope fit,
*E-values: From Statistics to ML* is the recommended option because it names conformal
prediction explicitly, and the body is written to its 4-page ceiling. The alternative on the
table is TS-LIMITS (4–7 pages, double-blind). `paper/main.tex` carries both style options with
exactly one active, and the body is written anonymity-neutral so the same text is legal under
both. **No automated session chooses the venue.**

Author block and co-author sign-off are also open (`docs/OPEN_QUESTIONS.md` Q8); no co-author
has been contacted or named here.

## Repository layout

| Path | Contents |
|---|---|
| `paper/` | LaTeX source (`main.tex` plus five sections) and the venue style file |
| `src/` | `forfeit.py` — the Placement-A harness that produces every measured number; `test_forfeit.py` — its executable tests |
| `results/` | One JSON per run, each carrying its config, git commit, wall-clock time and library versions. Append-only; never overwritten. Every number printed in the paper traces to one of these (`docs/GATES.md` G7.1) |
| `figures/` | Figure generation scripts and their outputs. Empty under the re-scoped paper, which prints two tables and no figure |
| `audit/` | Inventory, numeric-claim trace, claim ledger, prior-art sweep, and `REFS_VERIFIED.bib` — the only bibliography source |
| `docs/` | `FRAMING.md` (governing), stage gates, protocol, venue analysis, open questions, outstanding items, session reports |
| `data/` | Cached market series for the abandoned applied arm. Contents are not tracked and the re-scoped paper uses none |
| `research/` | Research-tool working files. Not tracked, never committed |
| `tools/` | Hygiene and build scripts |

## Reproducing

The measurement:

```sh
python3 src/forfeit.py --out results/forfeit-$(date -u +%Y%m%dT%H%M%SZ).json
python3 -m pytest src/test_forfeit.py -q
```

`src/forfeit.py --help` lists the horizon (`--tmax`) and the dead-band grid
(`--deadband-taus`) used to bracket the `τ*` edge. Runs are seeded and re-runs are
bit-identical; `src/test_forfeit.py` asserts that, along with the common-random-numbers
property, the degenerate-arm check and the no-leakage check. The committed runs are
`results/forfeit-*.json`, and the scorecaster / saturator / tangent-integrator sweep that
established `τ*` as a law rather than a null-scorecaster special case is
`results/forfeit-variations-20260820T101445Z.json`.

The paper, from `paper/`:

```sh
pdflatex main && bibtex main && pdflatex main && pdflatex main
```

No `TEXINPUTS`/`BIBINPUTS` needed — the style file sits beside `main.tex` and the
bibliography is reached by relative path. Build artefacts (`*.aux *.log *.bbl *.blg *.out`)
are untracked.

## Licence

MIT. See `LICENSE`.
