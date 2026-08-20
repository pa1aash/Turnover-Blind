#!/usr/bin/env python3
"""What a downstream smoother forfeits of Conformal PID's finite-sample rate.

This module reproduces, from committed code, the numbers that session S2 measured in an
ephemeral workspace and that `audit/NUMBERS.md` section 11 books under the
`verification-run` source class precisely because no committed code could regenerate
them.  It exists to discharge `docs/OUTSTANDING.md` O43 and to let `docs/GATES.md` G5.6
trace every printed number to a `results/` JSON.

-------------------------------------------------------------------------------
1.  THE MATHEMATICS, QUOTED FROM THE SOURCE
-------------------------------------------------------------------------------

Angelopoulos, Candes and Tibshirani, "Conformal PID Control for Time Series
Prediction", NeurIPS 2023 (arXiv:2307.16895).  Statements below are transcribed from
the proceedings PDF held at
`research/S2/records/angelopoulos2023pid_neurips_proceedings.pdf`, pages 3, 5-6 and 14
of the PDF (paper pages 2, 6-7 and 14).

Iteration (5), p.2:

    let q^_{t+1} be any function of the past: x_i, y_i, q_i, for i <= t,
    then update   q_{t+1} = q^_{t+1} + r_t( sum_{i<=t} (err_i - alpha) ).

Condition (4), p.2 -- the saturation condition on the integrator, and note that it
constrains `r_t` and nothing else:

    x >=  c*h(t)  ==>  r_t(x) >=  b,
    x <= -c*h(t)  ==>  r_t(x) <= -b,

for constants b, c > 0 and an *admissible* h -- nonnegative, nondecreasing, sublinear.

Theorem 1, p.2:

    Let {q^_t} be any sequence of numbers in [-b/2, b/2] and let {s_t} be any sequence
    of score functions with outputs in [-b/2, b/2] ... Assume r_t satisfies (4) for an
    admissible h.  Then the iterations in (5) achieve long-run coverage (2).

Proposition 2, p.6:

    Let {s_t} be any sequence of numbers in [-b, b] ... Assume r_t satisfies (4) for an
    admissible h.  Then the error integration iteration (8) satisfies
        | (1/T) sum_{t<=T} (err_t - alpha) |  <=  ( c*h(T) + 1 ) / T,
    i.e.  |E_T| <= c*h(T) + 1.

Proof of Proposition 2, p.14, the single load-bearing step:

    "In the first case, note that (4) implies q_T = r_t(E_{T-1}) >= b and therefore
     s_T <= q_T and err_t = 0."

Because h is nondecreasing, the induction bounds E_t at *every* t <= T by c*h(t) + 1
<= c*h(T) + 1, so `max_{t<=T} |E_t| <= c*h(T) + 1` is a valid reading of the bound and
is the one measured here.

-------------------------------------------------------------------------------
2.  THE OBJECT UNDER TEST -- PLACEMENT A
-------------------------------------------------------------------------------

The tracker computes `q_{t+1}` by iteration (5).  What is *deployed* is a smoothed
version of the completed output,

    q~_{t+1} = smooth( q~_t, q_{t+1} ),

and the miscoverage indicator that closes the integrator's loop is computed on the
deployed threshold: `err_t = 1{ s_t > q~_t }`.

A downstream smoother never touches `r_t`, so it *cannot* violate condition (4).  What
it breaks is the quoted induction step: the integrator reaches `b`, but an exponential
moving average of the *output* attains `b` only in the limit of infinitely many
consecutive saturated rounds, so "saturated at T" no longer implies "covered at T".
The sign is the opposite of the intuitive one -- the smoother does not damp the
accumulator's excursions, it lets the accumulator excurse further, because the
correction it is waiting for is delayed.  `n_sat_pos` and the traces emitted by this
script are there to make that visible.

-------------------------------------------------------------------------------
3.  THE FROZEN FREE CHOICES
-------------------------------------------------------------------------------

`audit/RECONSTRUCTION_SPEC.md` opens with the warning that rebuilding against a table
one has already read is a fitting exercise and not a reproduction.  Every choice this
script had to make is listed here, with its justification and the consequence if it is
wrong.  They were fixed before the sweep was run; the run happened once; the comparison
against S2 is reported in `research/S3/H4-repro.json` without reconciliation.

F1. Saturator form.  `r_t(x) = b * clip( x / (c*h(t)), -1, +1 )`.
    The two forms the brief offers -- `clip(x*(b/(c*h(t))), -b, +b)` and
    `b*clip(x/(c*h(t)), -1, +1)` -- are the *same function* for b > 0; the second is
    the first with `b` factored out of the clip.  Both satisfy condition (4) with
    equality at the boundary: at `x = c*h(t)` the argument of the clip is exactly 1, so
    `r_t(x) = b >= b`, and symmetrically at `-c*h(t)`.  Condition (4) is a >= / <=
    condition, so attaining the bound is enough; a strict-inequality reading would need
    a saturator that overshoots, which no clip does.  `test_forfeit.py` checks this on a
    grid.  If wrong: a saturator that only approaches `b` asymptotically (e.g. `b*tanh`)
    fails (4) outright and Proposition 2 would not apply even unsmoothed.

F2. Scorecaster.  `q^_t == 0` for all t.
    The null scorecaster.  It is legal -- 0 lies in [-b/2, b/2] -- and it reduces (5) to
    pure error integration (8), which is the object Proposition 2 is stated about.  It
    is also the only choice that isolates the smoother as the single manipulated
    variable.  If wrong: any non-trivial scorecaster changes the level of the deployed
    threshold and therefore how often the adversary can sit on it; the forfeit would be
    measured against a different, less interpretable baseline.

F3. Adversary and its legality rule.  `s_t = clip( q~_t + eps, -b/2, +b/2 )`, eps = 1e-9.

    THE ADVERSARY IS SPECIFIED, NOT TIE-BROKEN.  "An adversary sets the score at the
    deployed threshold" means the eps-above-the-threshold play `s_t = q~_t + eps`: the
    adversary lands *just* above the threshold and misses, which is the eps-decreasing-
    to-0 limit of sitting on it.  Written this way the paper's own strict indicator
    `err_t = 1{ s_t > q~_t }` fires with no tie rule needed anywhere, and the whole
    ambiguity that used to live in F4 is gone.  The resulting indicator is exactly
    `err_t = 1{ q~_t < b/2 }`.

    Legality is Theorem 1's hypothesis -- scores in [-b/2, +b/2] -- not Proposition 2's
    [-b, b], and the clip enforces it on both sides.  The two half-budgets exist for
    exactly this purpose: with q^ == 0 in [-b/2, b/2] and s in [-b/2, b/2] the
    reparameterised score s - q^ lies in [-b, b] and `b/2 + b/2 = b` is exactly tight.
    Taking the [-b, b] reading instead would let the adversary match the *saturated*
    threshold `r_t = +b`, which destroys the induction's slack and makes even the
    unsmoothed control violate Proposition 2 -- the zero-slack knife edge recorded in
    `research/S2/D1-reduction.json`.

    WHY eps = 1e-9, in both directions.  Large enough: deployed thresholds live in
    [-b, b] = [-2, 2], where one double-precision ulp is 2**-51 = 4.4e-16, so eps is
    about 2.3e6 ulps and `q~_t + eps` is always a strictly greater representable double,
    which is what makes the strict indicator fire at all.  Small enough: the finest
    scale the recursion resolves is the slowest smoother's gain, 1 - w = 1e-3 acting on
    displacements of order 1, so eps sits six orders of magnitude below anything the
    dynamics can see.  Both ends are checked rather than asserted --
    `test_adversary_eps_is_immaterial` re-runs the primary regime at eps = 1e-6, 1e-9
    and 1e-12 and requires the deployed path to be BIT-identical across all three.

    If wrong: too small and the strict indicator never fires, so the tracker sees no
    errors at all; too large and the adversary is no longer at the threshold but above
    it, which weakens the attack rather than strengthening it.

F4. Tie-breaking.  NO LONGER A FREE CHOICE.  The indicator is the paper's, strict
    everywhere and in every regime: `err_t = 1{ s_t > q~_t }`.  There is no tie rule in
    this module.

    HISTORY, KEPT DELIBERATELY, because it is the part of this register a reader should
    weigh most heavily.  The first version of this module made the adversary play the
    threshold *exactly*, `s_t = clip(q~_t, -b/2, +b/2)`, which forces a tie rule, and it
    chose to score ties as misses.  Its written justification claimed that the strict
    reading of that play was degenerate -- that the adversary would never miscover, that
    `E_t` would fall at rate alpha forever, and that realised miscoverage would be 0
    rather than alpha.  THAT CLAIM WAS FALSE, and the run disproved it: the strict
    reading of the exact-threshold play is the mirror image of the tie reading, tracking
    alpha with `E_t` oscillating about -0.5*h(t) instead of +0.5*h(t).  Worse, the two
    readings of the same play disagree by a factor of about 8.8 on the headline
    excursion -- 623.70 against 70.80 at w = 0.999, close to (1-alpha)/alpha = 9 -- so a
    genuine and large free choice was sitting underneath the paper's most-cited number.

    The eps specification in F3 SUPERSEDES that choice rather than vindicating it.  It
    is not that the tie reading turned out to be right.  It is that the ambiguity was
    never really about how to count a tie; it was about what the adversary plays, and
    once the adversary is specified properly the tie never arises.  That the primary
    numbers come out unchanged is a fact about this construction, not a defence of the
    earlier reasoning, and it should not be read as one.

    Both exact-threshold plays are RETAINED, as the sensitivity regimes
    `exact_threshold_tie` and `exact_threshold_strict`, so that the paper can cite the
    size of the dependence rather than hope no referee asks.

F5. Growing time constant.  `gain_t = 1 / (1 + t**p)` on the new sample, i.e.
    `q~_{t+1} = (1 - gain_t) * q~_t + gain_t * q_{t+1}` with p in {0.5, 0.9}, and t the
    index of the update.  Equivalently `w_t = 1 - 1/(1 + t**p)` as the brief writes it.
    At t = 1 the gain is 1/2 (a genuine average of the two available values) and it
    decays as t**-p, so the effective time constant grows as t**p.  If wrong: a
    parameterisation with gain `t**-p` is singular at t = 1 and one with `1/(c + t**p)`
    introduces a second free constant.

F6. Dead band update.  `q~_{t+1} = q_{t+1} - sign(u)*tau` when `|u| > tau`, else `q~_t`,
    where `u = q_{t+1} - q~_t`.  This is algebraically identical to the brief's
    `q~_t + S_tau(u)` with `S_tau(u) = sign(u)*(|u| - tau)_+`, but in floating point it
    returns the target pulled back by exactly tau, so at tau = 0 it is *bit*-identical
    to the unsmoothed arm.  The `q~_t + (q_{t+1} - q~_t)` form is not, in general.
    If wrong: nothing, in exact arithmetic; the degenerate-arm test would fail on
    representation rather than on substance.

F7. Initial conditions.  `E_0 = 0`, `q_1 = 0` (which is `r_0(E_0)` for every saturator
    satisfying F1), and `q~_1 = q_1`.  The running mean is seeded with `q_1` so that
    `q~_{t+1} = mean(q_1 .. q_{t+1})` as specified.  If wrong: a transient of length
    O(1/(1-w)) at the head of the sequence; irrelevant at the reported horizons.

F8. Accumulator arithmetic.  `E_t = n_err_t - alpha*t` with `n_err_t` an exact integer
    count, rather than accumulating `E += err - alpha`.  Over 10**6 steps the
    accumulating form drifts by order 1e-11; the counted form is exact to one rounding.
    If wrong: nothing measurable, but the reported `max|E_t|` would no longer sit on
    the exact 0.1 lattice that alpha = 0.1 implies.

F9. Seed.  20260820, consumed only by the secondary open-loop `iid` regime.  The
    primary `adversarial` regime is fully deterministic and consumes no randomness at
    all; its "seed" is a formality recorded for completeness.

F10. The secondary regime.  A seeded i.i.d. uniform score sequence on [-b/2, b/2],
    shared bit-identically across every arm.  It is not in the brief.  It is here
    because the CRN test the brief requires -- "every arm must see the identical score
    realisation" -- is *unsatisfiable by construction* under a closed-loop adversary,
    whose score is a function of the arm's own deployed threshold.  The open-loop regime
    gives that test a referent, and doubles as a robustness column showing the forfeit
    is not an artefact of the adversary.

-------------------------------------------------------------------------------
4.  THE TWO TESTS THAT NO LONGER HAVE A REFERENT
-------------------------------------------------------------------------------

`audit/RECONSTRUCTION_SPEC.md` section 3 lists five tests.  Two of them are not dropped
silently; they are dropped for cause and the cause is recorded here and in
`research/S3/H4-repro.json`.

  * "Zero-cost invariance: at 0 bps, net growth equals gross growth exactly."
    NO REFERENT.  It was written against the C1 design, in which a fractional-Kelly
    position is priced with a proportional transaction cost drawn from a {0, 5, 15} bps
    grid.  The re-scoped paper has no position, no growth column and no cost model, and
    this module has no `gross`, `net` or `cost_rate` to compare.  The test cannot be
    written because the quantities it equates do not exist.

  * "Cost identity: gross - net equals cost_rate * turnover to floating-point tolerance."
    NO REFERENT, for the same reason, and additionally because `turnover` in that spec
    is `sum |pi_t - pi_{t-1}|` over positions.  The nearest surviving quantity is the
    deployed travel `sum |q~_t - q~_{t-1}|`, which is not priced in anything and so
    supports no identity.  Deployed travel is emitted per arm anyway, as `travel`, so a
    later session that reintroduces a cost model has the raw material.

The three that do survive are implemented in `src/test_forfeit.py`.

-------------------------------------------------------------------------------
5.  USAGE
-------------------------------------------------------------------------------

    /opt/homebrew/Caskroom/miniforge/base/bin/python3 src/forfeit.py

writes `results/forfeit-<runid>.json` and never overwrites an existing file.  Options:
`--tmax` to shorten the sweep, `--out` to name the file, `--no-iid` to skip the
secondary regime, `--quiet`.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import platform
import subprocess
import sys
import time
from array import array
from dataclasses import asdict, dataclass, field
from typing import Callable, Dict, List, Optional, Sequence, Tuple

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA = "turnover-blind/forfeit/1"
REGIMES = ("adversarial", "exact_threshold_tie", "exact_threshold_strict", "iid")


# --------------------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------------------


@dataclass(frozen=True)
class Config:
    """The single frozen configuration object.  Nothing else carries state."""

    alpha: float = 0.1
    b: float = 2.0
    c: float = 1.0
    t_max: int = 1_000_000
    horizons: Tuple[int, ...] = (10_000, 100_000, 200_000, 1_000_000)
    seed: int = 20260820
    # F3: legality of the adversary's score, as a multiple of b.
    score_bound_frac: float = 0.5
    # F3: how far above the deployed threshold the adversary lands.  Strictly positive,
    # about 2.3e6 double-precision ulps at |q~| <= b = 2, and six orders of magnitude
    # below the finest scale the recursion resolves (the slowest gain, 1 - w = 1e-3).
    adversary_eps: float = 1e-9
    # Downsampled trace length per arm, per series.
    trace_points: int = 512
    ema_weights: Tuple[float, ...] = (0.5, 0.9, 0.99, 0.999)
    deadband_taus: Tuple[float, ...] = (0.5, 0.9, 1.5)
    growing_exponents: Tuple[float, ...] = (0.5, 0.9)
    h_name: str = "log(t+2)"
    saturator_name: str = "clipped: r_t(x) = b*clip(x/(c*h(t)), -1, +1)"
    # ----------------------------------------------------------------------------------
    # ADDED 2026-08-20, WAVE 5, in response to the adversarial critic (F1).  The critic
    # showed that the dead-band boundary printed by wave 3 -- tau > b/2 -- is the
    # NULL-SCORECASTER special case and not the law.  The law is
    #
    #     tau* = sup_x r_t(x) + sup_t qhat_t - b/2,
    #
    # so both of the knobs below MOVE the boundary while remaining legal under Theorem 1,
    # whose hypothesis on qhat is "any sequence of numbers in [-b/2, b/2]".  They exist so
    # that the numbers the paper prints about those variations come from COMMITTED code
    # and land in results/, rather than from an agent's scratch directory.  Defaults
    # reproduce the wave-3 configuration exactly, bit for bit.
    # ----------------------------------------------------------------------------------
    # A CONSTANT scorecaster qhat_t == scorecaster_const, added to the integrator output.
    # Legal for any value in [-b/2, b/2]; 0.0 is the null scorecaster of the primary run.
    scorecaster_const: float = 0.0
    # Multiplies the saturator's LEVEL b.  F1 established that the saturator's level, not
    # its shape, carries the result, so this is the knob that matters.  1.0 is the
    # primary run; the level is sup_x |r_t(x)| = saturator_level_mult * b.
    saturator_level_mult: float = 1.0
    # Saturator FAMILY.  "clipped" is the primary run.  "tangent" is ACT23's own
    # unbounded family, which they state they use "in all our experiments": it is
    # calibrated so that r_t(c*h(t)) = b exactly and then diverges past it, so it meets
    # condition (4) a fortiori and has NO finite sup.  Under it the boundary law
    # tau* = sup r_t + sup qhat - b/2 has sup r_t = infinity, so no finite dead band can
    # cap the deployed threshold below the score range -- which is why the failure this
    # note measures does not arise there.  Form transcribed from the critic's probe so
    # the committed run reproduces the number the paper prints.
    saturator_kind: str = "clipped"

    def h(self, t: int) -> float:
        """The admissible threshold function.  Nonnegative, nondecreasing, sublinear."""
        return math.log(t + 2.0)

    def prop2_bound(self, T: int) -> float:
        """Proposition 2's bound c*h(T) + 1."""
        return self.c * self.h(T) + 1.0

    def live_horizons(self) -> Tuple[int, ...]:
        return tuple(T for T in self.horizons if T <= self.t_max)


# --------------------------------------------------------------------------------------
# Saturator
# --------------------------------------------------------------------------------------


def saturator(x: float, t: int, cfg: Config) -> float:
    """F1: r_t(x) = b * clip(x / (c*h(t)), -1, +1).  Satisfies condition (4)."""
    z = x / (cfg.c * cfg.h(t))
    if z > 1.0:
        z = 1.0
    elif z < -1.0:
        z = -1.0
    return cfg.b * cfg.saturator_level_mult * z


# --------------------------------------------------------------------------------------
# Smoothers.  Each factory returns a fresh stateful callable (q~_t, q_{t+1}, t) -> q~_{t+1}.
# --------------------------------------------------------------------------------------


Smoother = Callable[[float, float, int], float]


def make_identity() -> Smoother:
    def f(q_dep: float, q_raw: float, t: int) -> float:
        return q_raw

    return f


def make_ema(w: float) -> Smoother:
    one_minus = 1.0 - w

    def f(q_dep: float, q_raw: float, t: int) -> float:
        return w * q_dep + one_minus * q_raw

    return f


def make_deadband(tau: float) -> Smoother:
    def f(q_dep: float, q_raw: float, t: int) -> float:
        u = q_raw - q_dep
        if -tau <= u <= tau:
            return q_dep
        return q_raw - math.copysign(tau, u)  # F6

    return f


def make_running_mean(q_first: float) -> Smoother:
    state = [q_first, 1]  # [running sum over q_1..q_n, n]

    def f(q_dep: float, q_raw: float, t: int) -> float:
        state[0] += q_raw
        state[1] += 1
        return state[0] / state[1]

    return f


def make_growing_ema(p: float) -> Smoother:
    def f(q_dep: float, q_raw: float, t: int) -> float:
        gain = 1.0 / (1.0 + t**p)  # F5
        return (1.0 - gain) * q_dep + gain * q_raw

    return f


@dataclass(frozen=True)
class Arm:
    name: str
    family: str
    params: Dict[str, float] = field(default_factory=dict)

    def make(self, q_first: float) -> Smoother:
        if self.family == "identity":
            return make_identity()
        if self.family == "ema":
            return make_ema(self.params["w"])
        if self.family == "deadband":
            return make_deadband(self.params["tau"])
        if self.family == "running_mean":
            return make_running_mean(q_first)
        if self.family == "growing_ema":
            return make_growing_ema(self.params["p"])
        raise ValueError(f"unknown smoother family: {self.family}")


def build_arms(cfg: Config) -> List[Arm]:
    """The control plus the ten smoothed arms named in the brief."""
    arms = [Arm("unsmoothed", "identity")]
    arms += [Arm(f"ema_w{w:g}", "ema", {"w": w}) for w in cfg.ema_weights]
    arms += [Arm(f"deadband_tau{tau:g}", "deadband", {"tau": tau}) for tau in cfg.deadband_taus]
    arms += [Arm("running_mean", "running_mean")]
    arms += [Arm(f"growing_ema_p{p:g}", "growing_ema", {"p": p}) for p in cfg.growing_exponents]
    return arms


# --------------------------------------------------------------------------------------
# The recursion
# --------------------------------------------------------------------------------------


def run_arm(
    cfg: Config,
    arm: Arm,
    regime: str,
    scores: Optional[Sequence[float]] = None,
    perturb_index: Optional[int] = None,
    perturb_value: Optional[float] = None,
    keep_series: bool = False,
) -> Dict:
    """One pass of Placement A to `cfg.t_max`, snapshotting at every reporting horizon.

    `regime` is one of

      "adversarial"             PRIMARY (F3).  Closed loop, the adversary lands just
                                above the deployed threshold:
                                s_t = clip(q~_t + eps, -b/2, +b/2).
      "exact_threshold_tie"     SENSITIVITY.  The adversary plays the threshold exactly,
                                s_t = clip(q~_t, -b/2, +b/2), with a tie scored as a
                                miscoverage.  Retained to show the headline number's
                                dependence on the adversary's specification (F4).
      "exact_threshold_strict"  SENSITIVITY.  The same exact-threshold play under the
                                strict indicator, where the adversary's move covers.
      "iid"                     SECONDARY (F10).  Open loop, `scores` consumed in order.

    The indicator is `err_t = 1{s_t > q~_t}` -- the paper's, strict -- in every regime
    except `exact_threshold_tie`, which exists precisely to exhibit the alternative.

    Returns a raw record.  Aggregates are NOT computed here -- see `derive_table`.
    """
    if regime not in REGIMES:
        raise ValueError(regime)
    if regime == "iid" and scores is None:
        raise ValueError("the iid regime needs a score array")

    alpha, b, c = cfg.alpha, cfg.b, cfg.c
    half = b * cfg.score_bound_frac
    T = cfg.t_max
    log = math.log
    closed_loop = regime != "iid"
    tie = regime == "exact_threshold_tie"
    eps = cfg.adversary_eps if regime == "adversarial" else 0.0

    q_raw = 0.0  # q_1, F7
    q_dep = 0.0  # q~_1, F7
    smooth = arm.make(q_raw)

    n_err = 0
    max_abs_E = 0.0
    argmax_abs_E = 0
    E_min = 0.0
    E_max = 0.0
    n_sat_pos = 0
    n_sat_neg = 0
    n_adv_clipped = 0
    travel = 0.0
    E = 0.0

    tangent = cfg.saturator_kind == "tangent"
    atan_b = math.atan(cfg.b)   # calibration: r_t(c*h(t)) = tan(atan(b)) = b exactly
    TAN_LIM = math.pi / 2.0 - 1e-9

    consumed = array("d")  # every score the arm actually saw -- the CRN evidence
    deployed = array("d")  # every deployed threshold q~_t -- the degeneracy evidence

    horizon_set = set(cfg.live_horizons())
    snapshots: List[Dict] = []

    stride = max(1, T // max(1, cfg.trace_points))
    trace_t: List[int] = []
    trace_E: List[float] = []
    trace_q: List[float] = []

    series_E: Optional[array] = array("d") if keep_series else None
    series_q: Optional[array] = array("d") if keep_series else None

    for t in range(1, T + 1):
        # ---- the deployed threshold q~_t is fixed BEFORE the score at t is revealed.
        q_t = q_dep
        deployed.append(q_t)

        # ---- the score.
        if closed_loop:
            s = q_t + eps  # F3: the adversary lands just above the deployed threshold
            if s > half:
                s = half
                n_adv_clipped += 1
            elif s < -half:
                s = -half
                n_adv_clipped += 1
        else:
            s = scores[t - 1]
        if perturb_index == t:
            s = perturb_value
        consumed.append(s)

        # ---- the miscoverage indicator, on the DEPLOYED threshold (F4).
        if tie:
            err = 1 if s >= q_t else 0
        else:
            err = 1 if s > q_t else 0
        n_err += err

        # ---- the accumulator (F8).
        E = n_err - alpha * t
        aE = -E if E < 0.0 else E
        if aE > max_abs_E:
            max_abs_E = aE
            argmax_abs_E = t
        if E > E_max:
            E_max = E
        elif E < E_min:
            E_min = E

        # ---- the integrator and the completed output q_{t+1} = q^ + r_t(E_t), q^ == 0.
        thr = c * log(t + 2.0)
        if E >= thr:
            n_sat_pos += 1
        elif E <= -thr:
            n_sat_neg += 1
        z = E / thr
        if z > 1.0:
            z = 1.0
        elif z < -1.0:
            z = -1.0
        # WAVE 5 (F1): saturator family, level multiplier and constant scorecaster.  All
        # three default to the wave-3 values and reproduce it bit for bit.
        if tangent:
            u = atan_b * (E / thr) / 1.0
            if u > TAN_LIM:
                u = TAN_LIM
            elif u < -TAN_LIM:
                u = -TAN_LIM
            q_raw = math.tan(u) + cfg.scorecaster_const
        else:
            q_raw = b * cfg.saturator_level_mult * z + cfg.scorecaster_const

        # ---- Placement A: the smoother acts on the completed output.
        q_next = smooth(q_dep, q_raw, t)
        d = q_next - q_dep
        travel += -d if d < 0.0 else d
        q_dep = q_next

        if keep_series:
            series_E.append(E)
            series_q.append(q_t)
        if t % stride == 0 or t == 1:
            trace_t.append(t)
            trace_E.append(E)
            trace_q.append(q_t)

        if t in horizon_set:
            snapshots.append(
                {
                    "T": t,
                    "n_err": n_err,
                    "E_at_T": E,
                    "max_abs_E": max_abs_E,
                    "argmax_abs_E": argmax_abs_E,
                    "E_min": E_min,
                    "E_max": E_max,
                    "n_sat_pos": n_sat_pos,
                    "n_sat_neg": n_sat_neg,
                    "n_adv_clipped": n_adv_clipped,
                    "travel": travel,
                }
            )

    record: Dict = {
        "arm": arm.name,
        "family": arm.family,
        "params": dict(arm.params),
        "regime": regime,
        "t_max": T,
        "scores_sha256": hashlib.sha256(consumed.tobytes()).hexdigest(),
        "deployed_sha256": hashlib.sha256(deployed.tobytes()).hexdigest(),
        "horizons_raw": snapshots,
        "trace": {
            "t": trace_t,
            "E": [round(v, 6) for v in trace_E],
            "q_deployed": [round(v, 9) for v in trace_q],
        },
    }
    if keep_series:
        record["_series_E"] = series_E
        record["_series_q"] = series_q
    return record


# --------------------------------------------------------------------------------------
# Derived aggregates -- recomputable from the raw record without re-running
# --------------------------------------------------------------------------------------


def derive_table(cfg: Config, raw_records: Sequence[Dict]) -> List[Dict]:
    """Build the reporting table from `horizons_raw` alone.  No simulation happens here."""
    rows: List[Dict] = []
    for rec in raw_records:
        for snap in rec["horizons_raw"]:
            T = snap["T"]
            bound = cfg.prop2_bound(T)
            rows.append(
                {
                    "arm": rec["arm"],
                    "family": rec["family"],
                    "params": rec["params"],
                    "regime": rec["regime"],
                    "T": T,
                    "miscoverage": snap["n_err"] / T,
                    "max_abs_E": snap["max_abs_E"],
                    "prop2_bound": bound,
                    "ratio_max_abs_E_over_bound": snap["max_abs_E"] / bound,
                    "violates_prop2": snap["max_abs_E"] > bound,
                    "argmax_abs_E": snap["argmax_abs_E"],
                    "frac_saturated": (snap["n_sat_pos"] + snap["n_sat_neg"]) / T,
                    "frac_adversary_clipped": snap["n_adv_clipped"] / T,
                    "deployed_travel": snap["travel"],
                }
            )
    return rows


# --------------------------------------------------------------------------------------
# Provenance
# --------------------------------------------------------------------------------------


def git_state() -> Dict[str, object]:
    def run(args: List[str]) -> str:
        try:
            return subprocess.run(
                args, cwd=REPO_ROOT, capture_output=True, text=True, timeout=30
            ).stdout.strip()
        except Exception:  # pragma: no cover - provenance must never abort a run
            return ""

    return {
        "commit": run(["git", "rev-parse", "HEAD"]),
        "branch": run(["git", "rev-parse", "--abbrev-ref", "HEAD"]),
        "dirty": bool(run(["git", "status", "--porcelain"])),
        "describe": run(["git", "describe", "--always", "--dirty"]),
    }


def environment() -> Dict[str, str]:
    versions = {
        "python": sys.version,
        "python_executable": sys.executable,
        "platform": platform.platform(),
        "machine": platform.machine(),
    }
    try:
        import numpy

        versions["numpy"] = numpy.__version__
    except Exception:  # pragma: no cover
        versions["numpy"] = "not importable"
    return versions


def free_choice_register() -> List[Dict[str, str]]:
    """Section 3 of the module docstring, in machine-readable form."""
    return [
        {
            "id": "F1",
            "choice": "saturator form",
            "value": "r_t(x) = b*clip(x/(c*h(t)), -1, +1)",
            "justification": (
                "The two forms the brief offers are the same function for b > 0.  Both "
                "satisfy condition (4) with equality at the boundary: at x = c*h(t) the "
                "clip argument is exactly 1 so r_t(x) = b >= b.  Checked on a grid in "
                "src/test_forfeit.py."
            ),
            "consequence_if_wrong": (
                "A saturator that only approaches b asymptotically fails (4) and "
                "Proposition 2 would not apply even to the unsmoothed control."
            ),
        },
        {
            "id": "F2",
            "choice": "scorecaster q^_t",
            "value": "0 for all t",
            "justification": (
                "The null scorecaster is legal (0 lies in [-b/2, b/2]) and reduces "
                "iteration (5) to pure error integration (8), the object Proposition 2 "
                "is stated about.  It isolates the smoother as the only manipulated "
                "variable."
            ),
            "consequence_if_wrong": (
                "A non-trivial scorecaster shifts the level of the deployed threshold "
                "and therefore how often the adversary can sit on it; the forfeit would "
                "be measured against a different baseline."
            ),
        },
        {
            "id": "F3",
            "choice": "adversary specification and legality rule",
            "value": "s_t = clip(q~_t + eps, -b/2, +b/2) with eps = 1e-9; legality is Theorem 1's [-b/2, b/2]",
            "justification": (
                "THE ADVERSARY IS SPECIFIED, NOT TIE-BROKEN.  'An adversary sets the "
                "score at the deployed threshold' means the eps-above-the-threshold "
                "play: it lands just above and misses, which is the eps-decreasing-to-0 "
                "limit of sitting on it.  Written this way the paper's own strict "
                "indicator err_t = 1{s_t > q~_t} fires with no tie rule anywhere, and the "
                "resulting indicator is exactly err_t = 1{q~_t < b/2}.  Legality is "
                "Theorem 1's hypothesis and the clip enforces it on both sides: with "
                "q^ == 0 in [-b/2, b/2] and s in [-b/2, b/2] the reparameterised score "
                "s - q^ lies in [-b, b] and b/2 + b/2 = b is exactly tight.  eps = 1e-9 "
                "is about 2.3e6 double-precision ulps at |q~| <= 2, so q~_t + eps is "
                "always a strictly greater representable double, and six orders of "
                "magnitude below the finest scale the recursion resolves (the slowest "
                "smoother gain, 1 - w = 1e-3); test_adversary_eps_is_immaterial checks "
                "both ends by requiring bit-identical deployed paths at eps = 1e-6, 1e-9 "
                "and 1e-12."
            ),
            "consequence_if_wrong": (
                "Reading legality as Proposition 2's [-b, b] lets the adversary match the "
                "saturated threshold +b, destroying the induction's slack; the unsmoothed "
                "control then violates Proposition 2 too and stops being a control.  This "
                "is the zero-slack knife edge of research/S2/D1-reduction.json.  On eps: "
                "too small and the strict indicator never fires so the tracker sees no "
                "errors at all; too large and the adversary is no longer at the threshold "
                "but above it, which weakens the attack rather than strengthening it."
            ),
        },
        {
            "id": "F4",
            "choice": "tie-breaking of err_t",
            "value": "NOT A FREE CHOICE.  err_t = 1{s_t > q~_t}, strict, in every regime; no tie rule exists.",
            "justification": (
                "SUPERSEDED BY F3, AND THE HISTORY IS KEPT ON PURPOSE.  The first version "
                "of this module made the adversary play the threshold EXACTLY, which "
                "forces a tie rule, and scored ties as misses.  Its written justification "
                "claimed the strict reading of that play was degenerate -- adversary never "
                "miscovers, E_t falls at rate alpha forever, realised miscoverage 0.  THAT "
                "CLAIM WAS FALSE and the run disproved it: the strict reading is the "
                "mirror image, tracking alpha with E_t about -0.5*h(t).  Worse, the two "
                "readings of the same play disagree by a factor of about 8.8 on the "
                "headline excursion (623.70 vs 70.80 at w = 0.999, close to "
                "(1-alpha)/alpha = 9), so a large free choice sat under the paper's "
                "most-cited number.  The eps specification SUPERSEDES that choice rather "
                "than vindicating it: the ambiguity was never about how to count a tie, it "
                "was about what the adversary plays, and once the adversary is specified "
                "the tie never arises.  That the primary numbers come out unchanged is a "
                "fact about this construction, not a defence of the earlier reasoning."
            ),
            "consequence_if_wrong": (
                "None remaining in the primary regime -- there is no tie to break.  The "
                "size of what was at stake is measured rather than argued: both "
                "exact-threshold plays are retained as the regimes exact_threshold_tie "
                "and exact_threshold_strict, and the paper should cite that sensitivity "
                "instead of hoping no referee asks."
            ),
        },
        {
            "id": "F5",
            "choice": "growing time constant parameterisation",
            "value": "gain_t = 1/(1 + t**p) on the new sample, p in {0.5, 0.9}",
            "justification": (
                "Equivalent to w_t = 1 - 1/(1 + t**p).  Gain 1/2 at t = 1 (a genuine "
                "average of the two available values) decaying as t**-p, so the effective "
                "time constant grows as t**p."
            ),
            "consequence_if_wrong": (
                "gain = t**-p is singular at t = 1; 1/(c + t**p) adds a second free "
                "constant.  Either changes the head transient and, for p near 1, the "
                "measured excursion."
            ),
        },
        {
            "id": "F6",
            "choice": "dead band update form",
            "value": "q~_{t+1} = q_{t+1} - sign(u)*tau when |u| > tau, else q~_t",
            "justification": (
                "Algebraically identical to q~_t + S_tau(u), but in floating point it "
                "returns the target pulled back by exactly tau, so at tau = 0 it is "
                "bit-identical to the unsmoothed arm.  The additive form is not."
            ),
            "consequence_if_wrong": "Nothing in exact arithmetic; the degenerate-arm test would fail on representation.",
        },
        {
            "id": "F7",
            "choice": "initial conditions",
            "value": "E_0 = 0, q_1 = 0, q~_1 = q_1; running mean seeded with q_1",
            "justification": "q_1 = r_0(E_0) = 0 for every saturator satisfying F1; the smoother starts at the first output.",
            "consequence_if_wrong": "A head transient of length O(1/(1-w)); irrelevant at the reported horizons.",
        },
        {
            "id": "F8",
            "choice": "accumulator arithmetic",
            "value": "E_t = n_err_t - alpha*t with n_err an exact integer count",
            "justification": "The accumulating form drifts by order 1e-11 over 10**6 steps; the counted form is exact to one rounding and keeps E on the exact 0.1 lattice alpha = 0.1 implies.",
            "consequence_if_wrong": "No measurable change to any reported quantity.",
        },
        {
            "id": "F9",
            "choice": "seed",
            "value": "20260820",
            "justification": "Consumed only by the secondary open-loop regime.  The primary adversarial regime is fully deterministic and consumes no randomness.",
            "consequence_if_wrong": "No effect on any primary number.",
        },
        {
            "id": "F10",
            "choice": "the secondary open-loop regime",
            "value": "i.i.d. uniform scores on [-b/2, b/2], shared bit-identically across arms",
            "justification": (
                "Not in the brief.  Added because the required CRN test -- every arm sees "
                "the identical score realisation -- is unsatisfiable by construction under "
                "a closed-loop adversary whose score is a function of the arm's own "
                "deployed threshold.  Doubles as a robustness column."
            ),
            "consequence_if_wrong": "The CRN test would have no referent and would have to be recorded as inapplicable.",
        },
    ]


def dropped_tests_register() -> List[Dict[str, str]]:
    return [
        {
            "name": "zero-cost invariance",
            "spec": "audit/RECONSTRUCTION_SPEC.md section 3, test 2",
            "applies": False,
            "why_no_referent": (
                "It equates net growth with gross growth at a 0 bps cost level.  The "
                "re-scoped paper has no position, no growth column and no transaction-cost "
                "model, so this module defines no gross, net or cost_rate.  The quantities "
                "the test equates do not exist."
            ),
        },
        {
            "name": "cost identity",
            "spec": "audit/RECONSTRUCTION_SPEC.md section 3, test 3",
            "applies": False,
            "why_no_referent": (
                "It asserts gross - net = cost_rate * turnover, where turnover is "
                "sum|pi_t - pi_{t-1}| over positions.  There is no decision priced in "
                "basis points in the re-scoped paper.  The nearest surviving quantity is "
                "deployed travel sum|q~_t - q~_{t-1}|, emitted per arm as `travel`, but it "
                "is not priced in anything and supports no identity."
            ),
        },
    ]


# --------------------------------------------------------------------------------------
# Driver
# --------------------------------------------------------------------------------------


def iid_scores(cfg: Config) -> "array":
    """Seeded, shared, open-loop score realisation.  Identical for every arm (F10)."""
    import numpy as np

    rng = np.random.default_rng(cfg.seed)
    half = cfg.b * cfg.score_bound_frac
    return array("d", rng.uniform(-half, half, size=cfg.t_max))


def sweep(cfg: Config, with_iid: bool = True, verbose: bool = True) -> Dict:
    started = time.time()
    arms = build_arms(cfg)
    raw: List[Dict] = []

    scores = iid_scores(cfg) if with_iid else None
    regimes = ["adversarial", "exact_threshold_tie", "exact_threshold_strict"]
    if with_iid:
        regimes.append("iid")

    for regime in regimes:
        for arm in arms:
            t0 = time.time()
            kw = {"scores": scores} if regime == "iid" else {}
            raw.append(run_arm(cfg, arm, regime, **kw))
            if verbose:
                print(
                    f"  {regime:19s}{arm.name:22s} {time.time() - t0:6.2f}s",
                    file=sys.stderr,
                )

    table = derive_table(cfg, raw)
    elapsed = time.time() - started

    return {
        "schema": SCHEMA,
        "purpose": (
            "Regenerate, from committed code, the Placement A forfeit numbers that "
            "audit/NUMBERS.md section 11 rows 50-54 book under the verification-run "
            "source class.  Discharges docs/OUTSTANDING.md O43; feeds docs/GATES.md G5.6."
        ),
        "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "wall_clock_seconds": elapsed,
        "git": git_state(),
        "environment": environment(),
        "seed": cfg.seed,
        "config": _config_json(cfg),
        "free_choices": free_choice_register(),
        "dropped_tests": dropped_tests_register(),
        "arms_raw": raw,
        "aggregate_table": table,
        "aggregate_table_note": (
            "Derived from arms_raw[*].horizons_raw by derive_table(); recomputable "
            "without re-running the sweep."
        ),
        "regimes": {
            "adversarial": (
                "PRIMARY.  Closed loop.  The adversary lands just above the deployed "
                "threshold, s_t = clip(q~_t + eps, -b/2, +b/2) with eps = 1e-9, and the "
                "indicator is the paper's own strict err_t = 1{s_t > q~_t}.  No tie rule "
                "exists anywhere in this regime.  These are the numbers that go in the "
                "paper."
            ),
            "exact_threshold_tie": (
                "SENSITIVITY.  The adversary plays the deployed threshold EXACTLY, "
                "s_t = clip(q~_t, -b/2, +b/2), which forces a tie rule; here the tie is "
                "scored as a miscoverage.  This was the primary regime of the first "
                "version of this module.  Retained so the paper can cite how much the "
                "headline number depends on the adversary's specification."
            ),
            "exact_threshold_strict": (
                "SENSITIVITY.  The same exact-threshold play under the strict indicator, "
                "where the adversary's signature move COVERS rather than misses.  It is "
                "the mirror image of the tie reading and it is what shows that the "
                "exact-threshold play, not the counting convention, was the real "
                "ambiguity: see free choice F4."
            ),
            "iid": (
                "SECONDARY (F10).  Open-loop seeded i.i.d. uniform scores on [-b/2, b/2], "
                "shared bit-identically across every arm.  Gives the CRN test a referent "
                "and shows which failures survive without an adversary."
            ),
        },
    }


def _config_json(cfg: Config) -> Dict:
    d = asdict(cfg)
    d["horizons"] = list(cfg.horizons)
    d["ema_weights"] = list(cfg.ema_weights)
    d["deadband_taus"] = list(cfg.deadband_taus)
    d["growing_exponents"] = list(cfg.growing_exponents)
    d["h_values_at_horizons"] = {str(T): cfg.h(T) for T in cfg.live_horizons()}
    d["prop2_bound_at_horizons"] = {str(T): cfg.prop2_bound(T) for T in cfg.live_horizons()}
    return d


def default_run_id(commit: str) -> str:
    return time.strftime("%Y%m%dT%H%M%SZ", time.gmtime()) + "-" + (commit[:8] or "nogit")


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--tmax", type=int, default=Config.t_max)
    ap.add_argument("--out", type=str, default=None)
    ap.add_argument("--no-iid", action="store_true")
    ap.add_argument(
        "--deadband-taus",
        type=str,
        default=None,
        help=(
            "comma-separated dead-band widths, replacing the default grid.  Used to "
            "locate the tau = b/2 cliff at which the dead band caps the reachable "
            "deployed threshold below the adversary's score ceiling and coverage "
            "collapses; see the finding recorded in research/S3/H4-repro.json."
        ),
    )
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    kwargs: Dict[str, object] = {"t_max": args.tmax}
    if args.deadband_taus:
        kwargs["deadband_taus"] = tuple(float(x) for x in args.deadband_taus.split(","))
    cfg = Config(**kwargs)
    verbose = not args.quiet
    if verbose:
        print(f"forfeit: sweeping {len(build_arms(cfg))} arms to T = {cfg.t_max}", file=sys.stderr)

    payload = sweep(cfg, with_iid=not args.no_iid, verbose=verbose)
    run_id = default_run_id(str(payload["git"].get("commit", "")))
    payload["run_id"] = run_id

    out = args.out or os.path.join(REPO_ROOT, "results", f"forfeit-{run_id}.json")
    if os.path.exists(out):
        raise SystemExit(f"forfeit: refusing to overwrite {out}")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as fh:
        json.dump(payload, fh, indent=1, sort_keys=False)
        fh.write("\n")

    if verbose:
        print(f"forfeit: wrote {out} in {payload['wall_clock_seconds']:.1f}s", file=sys.stderr)
        _print_headline(cfg, payload)
    return 0


def _print_headline(cfg: Config, payload: Dict) -> None:
    rows = [r for r in payload["aggregate_table"] if r["regime"] == "adversarial"]
    print(
        f"\n{'arm':22s} {'T':>9s} {'miscov':>8s} {'max|E_t|':>10s} "
        f"{'bound':>8s} {'ratio':>8s}",
        file=sys.stderr,
    )
    for r in rows:
        print(
            f"{r['arm']:22s} {r['T']:9d} {r['miscoverage']:8.4f} {r['max_abs_E']:10.2f} "
            f"{r['prop2_bound']:8.2f} {r['ratio_max_abs_E_over_bound']:8.2f}",
            file=sys.stderr,
        )


if __name__ == "__main__":
    raise SystemExit(main())
