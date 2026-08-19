# Compute plan

**Working assumption: CPU-only, on a laptop. Nothing is provisioned, and nothing should
be.**

## Why CPU-only is the right assumption

The core experiment is a scalar recursion. Per path it maintains one state variable
`α_t`, one rolling scale estimate, one position, and an accumulator — a few floating-point
operations per step. The planning document reports roughly 90 seconds for six γ arms over
60 paths, which is unverified (`audit/NUMBERS.md` row 6) but entirely plausible for that
shape of computation, and if anything conservative for a vectorised implementation.

Scale it up to the full factorial the protocol implies and it stays small:

| Factor | Levels |
|---|---|
| Methods | 7 (fixed-α, ACI, DtACI, conformal PID, SAOCP, CDT, turnover-aware) |
| γ or equivalent | 6 |
| Cost rates | 4 |
| Paths (common random numbers) | 100 |

That is 16,800 path-runs. At one second per path-run — which is a very pessimistic figure
for a scalar recursion over a few thousand steps — the whole grid is under five hours
single-threaded, and minutes across a laptop's cores with `multiprocessing` over the path
index. The path dimension is embarrassingly parallel and the arms share cached input
paths by construction (common random numbers), so the natural parallelisation is one
worker per path with the γ and cost loops inside.

**There is no model training anywhere in this project.** No neural network, no
gradient-based fitting, no large dataset. The only estimators are rolling quantiles and
rolling standard deviations.

## What would actually change this

Exactly one candidate, and it is worth stating precisely because everything else is noise.

### The Ryan-configuration replication

The applied arm replicates a specific published configuration: 8 liquid US ETFs, daily
data, 2016–2021 development window (1,511 days) plus a 2022–2024 out-of-sample window,
with a W = 500 rolling conformal quantile per asset.

Even this is small. Eight assets × roughly 2,300 trading days is under 20,000
observations. A rolling 500-day quantile over that is trivial. The cost is not compute;
it is:

- **data acquisition and cleaning** — dividend and split adjustment, survivorship, the
  exact daily series Ryan used, and reconciling any differences;
- **wall-clock spent by a person**, not by a processor.

The one thing that could push it out of laptop range is a **bootstrap or permutation
inference layer over the replication** — for instance the 40-way timing placebo Ryan runs,
or a block bootstrap with several thousand resamples across the full method × γ × cost
grid. Ten thousand resamples of the full grid is roughly 10⁸ path-runs, which is a
cluster-shaped job rather than a laptop one.

**Even then the right answer is probably not a GPU.** This workload is
branch-heavy scalar recursion with negligible arithmetic intensity. It parallelises across
resamples, not within them. A many-core CPU box is the correct instrument; a GPU would sit
idle.

## If an instance is ever provisioned

Not now, and not without an explicit operator decision. Specified here only so the
decision is cheap when it arrives.

| Requirement | Value | Why |
|---|---|---|
| Instance type | **CPU-only, high core count.** 16–32 vCPU, 32–64 GB RAM | The work is embarrassingly parallel across paths and resamples; memory is trivial |
| GPU | **None** | No training, no dense linear algebra, no arithmetic intensity. A GPU is wasted spend here |
| Storage | 20 GB | Daily series for 8 ETFs is megabytes; `results/` JSONs are the bulk and are small |
| Wall-clock | Hours, not days | A 32-core box takes a 10⁸ path-run bootstrap into single-digit hours |
| Egress | Minimal | Fetch the price series once, then compute locally |
| Reproducibility | Pin Python and library versions; record them in every `results/` JSON | `audit/RECONSTRUCTION_SPEC.md` §3 requires it |
| Determinism | Seed policy recorded per run; CRN paths cached and hash-checked | A bit-identity assertion across arms is one of the five required tests |

**Vultr or an equivalent general-purpose CPU instance is the right shape.** A RunPod-style
GPU instance is the wrong instrument for this workload and would cost more to do less. If
the operator's default is to route compute to a GPU pod, this project is the exception and
should be routed to CPU.

## What must be true before any instance is provisioned

1. G2 signed — the simulator exists, is frozen, and passes its five tests locally.
2. A measured local runtime for one full grid, so the scale-up factor is known rather than
   guessed. Provisioning before measuring is how a laptop job becomes a cloud bill.
3. A specific inference layer that genuinely does not fit locally, named and sized.

Until all three hold, the correct compute plan is a laptop.

## Current spend

**Zero.** Nothing has been provisioned in this session, and this session ran no experiment
of any kind — there was no simulator to run (`audit/REPRO_C1.md`).
