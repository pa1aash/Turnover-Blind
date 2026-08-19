# Coverage Is Turnover-Blind

**Why adaptive conformal prediction is mis-tuned for costly decisions.**
Internal project identifier: F7.

## The claim

Online conformal predictors are tuned by coverage. The adaptation rate — the step
size `gamma` in the adaptive conformal inference (ACI) update, and its analogues in
DtACI, conformal PID and SAOCP — is chosen so that realised coverage tracks the
nominal target, and reported on realised coverage together with mean interval width.

This repository tests what that pair leaves free. Hold both fixed across arms, apply a
one-scalar movement penalty to the interval's **width path**, and measure what the
remaining freedom is worth to a decision that must move a position when the interval
moves. The primary measurement is that at matched coverage and matched mean width the
width path still varies materially, and realised decision cost varies with it by a
measurable number of points of annual net log growth. The contribution the paper is
built on is the second question: **what a movement penalty on the deployed quantile
does to the interval's validity**, which existing predictable-modification arguments do
not cover, because they require a monotonicity condition that a width smoother puts at
risk.

**An earlier design, which varied the adaptation rate γ directly and placed a dead-band
on the quantile update, is abandoned.** It could not separate mean width from path
variation, because both are approximately affine in γ. **A prior-art sweep has since
found the primary measurement occupied**, in the forecast-stability literature, by work
that uses no conformal vocabulary at all. **Read `docs/FRAMING.md` before anything
else** — it states what is claimed, what is conceded, and why.

The claim is **decision-theoretic, not information-theoretic**. It is not an
impossibility result, not a coverage floor and not a statement about a fundamental
limit; that territory is already occupied by the minimax coverage/efficiency
literature.

## Status

Characterisation stage (G0). This repository currently contains an audit of a prior
planning document, not an implementation. Nothing here is a result yet. See
`docs/G0_REPORT.md` for what is established, what is asserted, and what is missing;
see `docs/GATES.md` for the stage gates and `docs/OUTSTANDING.md` for the blocking
items. No gate in this project may be recorded as passed without the operator's
explicit sign-off.

## Repository layout

| Path | Contents |
|---|---|
| `paper/` | LaTeX source and venue style files |
| `src/` | Simulator, dead-band arm, baselines |
| `results/` | One JSON per experiment run. Append-only; never overwritten |
| `figures/` | Figure generation scripts and their outputs |
| `audit/` | Inventory, numeric-claim trace, claim ledger, prior-art sweep, reference audit |
| `docs/` | Plan of record, venue analysis, stage gates, provenance, outstanding items, open questions, compute plan |
| `data/` | Cached market series for the applied arm. Contents are not tracked |
| `research/` | Research-tool working files. Not tracked, never committed |
| `tools/` | Hygiene and build scripts |

## Reproducing the core result

Not yet reproducible. The planning document at `docs/PLAN_ORIGINAL.md` attributes the
central table to a simulator named `scratchpad/confloor5.py`; that file is not present
in this repository and was not recoverable. `audit/RECONSTRUCTION_SPEC.md` gives the
full specification a rebuild would need, including every choice the planning document
leaves underdetermined. When the simulator exists, this section will name the exact
command, the seed policy and the expected wall-clock time.

## Licence

MIT. See `LICENSE`.
