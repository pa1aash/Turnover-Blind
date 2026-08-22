#!/usr/bin/env python3
"""Stress test of the dead-band boundary law over the admissible class.

WHY THIS FILE EXISTS
--------------------
`src/forfeit.py` sweeps the five (r_t, qhat) settings the paper reports, and every one
of them has (a) a CONSTANT scorecaster, (b) a SYMMETRIC saturator whose extrema are
attained at the condition-(4) radius, and (c) a single adversary, the upward
eps-chaser s_t = clip(q~_t + eps, +-b/2).  Those three coincidences are exactly what
hides the difference between

    the printed law     tau* = sup_x r_t(x) + sup_t qhat_t - b/2
    and the corrected   coverage iff  tau <= inf_t(A^+_t + qhat_{t+1}) - b/2
                                and   tau <  inf_t(|A^-_t| - qhat_{t+1}) - b/2

on the RETENTION side.  This file breaks each coincidence in turn, one at a time, with
legal objects only, and records what the harness actually returns.

WHAT IS AND IS NOT REUSED
-------------------------
`src/forfeit.py` is IMPORTED AND NOT MODIFIED.  `make_deadband` (the frozen dead-band
map, its F6) and `Config` (the frozen constants alpha = 0.1, b = 2, c = 1,
h(t) = log(t+2), eps = 1e-9, q~_1 = 0) are used as they stand.  The loop in `sim()`
below is a transcription of `forfeit.run_arm`'s loop with three pieces made pluggable
that the frozen loop hard-codes: the scorecaster (constant there, any predictable
sequence here), the saturator (clipped or tangent there, any function here) and the
adversary (the upward eps-chaser there, any legal feedback rule here).

A transcription is worthless unless it reproduces the thing it transcribes, so
`validate()` runs FIRST and aborts the battery on any mismatch: with the frozen choices
plugged in, `sim()` must return `forfeit.run_arm`'s own committed numbers, read out of
results/forfeit-20260820T063132Z-83747c45.json, in both of that file's strict-indicator
regimes.  15 checks, all exact.

FREE CHOICES, all recorded in the emitted JSON:
  S1  every configuration below is LEGAL: each r_t satisfies condition (4)
      (|r_t(x)| >= b with the sign of x once |x| >= c h(t)) and each qhat_t lies in
      [-b/2, b/2] and is predictable.  Legality is asserted in code, not by comment.
  S2  two adversaries are run against every configuration, both legal under Theorem 1's
      [-b/2, b/2] score budget: the harness's upward eps-chaser, and the constant
      s_t == -b/2.  The second is the mirror adversary the printed law does not model.
  S3  the indicator is the paper's strict one, err_t = 1{s_t > q~_t}, everywhere.  No
      result here turns on the tie convention; the two-convention comparison stays in
      forfeit.py's exact_threshold_* regimes.
  S4  horizons are 1e5 for every configuration and additionally 1e6 for the
      time-varying scorecaster, whose failure mode is an oscillation that needs the
      longer horizon to separate from a transient.

Run:  python3 src/boundary_stress.py            # validate, run, write results/
      python3 src/boundary_stress.py validate   # validation only, writes nothing
"""

from __future__ import annotations

import json
import math
import os
import platform
import subprocess
import sys
import time
from typing import Callable, Dict, List, Optional, Sequence, Tuple

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO_ROOT, "src"))

from forfeit import Config, make_deadband, saturator  # noqa: E402

SCHEMA = "turnover-blind/boundary-stress/1"

CFG = Config()
B = CFG.b                              # 2.0
C = CFG.c                              # 1.0
ALPHA = CFG.alpha                      # 0.1
HALF = B * CFG.score_bound_frac        # b/2 = 1.0
EPS = CFG.adversary_eps                # 1e-9

REF_RUN = "results/forfeit-20260820T063132Z-83747c45.json"


# --------------------------------------------------------------------------------------
# Saturators.  Signature r(x, t) -> float.
# --------------------------------------------------------------------------------------


def r_clipped(mult: float = 1.0):
    """The harness's own saturator at level mult*b.  Extrema attained AT the radius."""

    cfg = Config(saturator_level_mult=mult)

    def r(x: float, t: int) -> float:
        return saturator(x, t, cfg)

    return r


def r_asym(a_plus: float, a_minus: float):
    """Piecewise linear, saturating at a_plus above +c h(t) and a_minus below -c h(t).

    Legal iff a_plus >= b and a_minus <= -b.  Extrema attained AT the radius.
    """
    assert a_plus >= B and a_minus <= -B, "condition (4) requires |r_t| >= b at the radius"

    def r(x: float, t: int) -> float:
        z = x / (C * CFG.h(t))
        if z >= 1.0:
            return a_plus
        if z <= -1.0:
            return a_minus
        return a_plus * z if z >= 0.0 else (-a_minus) * z

    return r


def r_far_sup(a_far: float):
    """Condition (4) holds and sup_x r_t(x) = a_far, but a_far is attained only on
    |x| > t^2, which the dynamics can never reach: |E_t| <= max(alpha, 1-alpha) t < t^2
    for every t >= 1.  The printed law reads a_far; the reachable ceiling is b."""
    assert a_far >= B

    def r(x: float, t: int) -> float:
        if x > t * t:
            return a_far
        if x < -t * t:
            return -a_far
        return saturator(x, t, CFG)

    return r


def r_far_sup_infinite():
    """The same construction with sup_x r_t(x) = +infinity: r_t(x) = x past |x| > t^2.
    The printed law reads tau* = +infinity; the reachable ceiling is still b."""

    def r(x: float, t: int) -> float:
        if x > t * t or x < -t * t:
            return x
        return saturator(x, t, CFG)

    return r


def r_unattained(a_sup: float):
    """sup_x r_t(x) = a_sup, approached at rate 1/x and NEVER attained on any reachable x.

    Meets condition (4) with equality at the radius: r_t(c h(t)) = a_sup - (a_sup - b) = b.
    The 1/x approach matters: an exponential approach is closed by double precision within
    ~40 rounds and the construction then silently becomes an attained one.
    """
    assert a_sup > B

    def r(x: float, t: int) -> float:
        th = C * CFG.h(t)
        if x >= th:
            return a_sup - (a_sup - B) / (1.0 + (x - th))
        if x <= -th:
            return -(a_sup - (a_sup - B) / (1.0 + (-x - th)))
        return B * x / th

    return r


def r_wild_inband(a_plus: float, a_minus: float):
    """Extrema attained at the radius, but the WRONG SIGN inside |x| < c h(t), which
    condition (4) permits: it constrains r_t nowhere inside the band."""

    def r(x: float, t: int) -> float:
        th = C * CFG.h(t)
        if x >= th:
            return a_plus
        if x <= -th:
            return a_minus
        return -a_plus * (x / th) * 0.9

    return r


def r_tangent():
    """ACT23's tangent family, transcribed from forfeit.run_arm's `tangent` branch."""
    atan_b = math.atan(B)
    lim = math.pi / 2.0 - 1e-9

    def r(x: float, t: int) -> float:
        u = atan_b * (x / (C * CFG.h(t)))
        if u > lim:
            u = lim
        elif u < -lim:
            u = -lim
        return math.tan(u)

    return r


# --------------------------------------------------------------------------------------
# Scorecasters.  Signature qhat(t) -> float, t the round the value is DEPLOYED at.
# --------------------------------------------------------------------------------------


def qhat_const(v: float):
    assert -HALF <= v <= HALF, "Theorem 1 requires qhat_t in [-b/2, b/2]"
    return lambda t: v


def qhat_pow2(hi: float = HALF, lo: float = 0.0):
    """qhat_t = hi on t a power of two, lo otherwise.  Predictable and in [-b/2, b/2],
    hence legal under Theorem 1, and NOT constant."""
    assert -HALF <= hi <= HALF and -HALF <= lo <= HALF

    def q(t: int) -> float:
        return hi if (t & (t - 1)) == 0 else lo

    return q


# --------------------------------------------------------------------------------------
# Adversaries.  Signature adv(q_dep) -> score in [-b/2, b/2].
# --------------------------------------------------------------------------------------


def adv_eps_up(q_dep: float) -> float:
    """The harness's primary adversary: s_t = clip(q~_t + eps, +-b/2)."""
    s = q_dep + EPS
    if s > HALF:
        return HALF
    if s < -HALF:
        return -HALF
    return s


def adv_const_low(q_dep: float) -> float:
    """s_t == -b/2.  Legal, constant, and the MIRROR of the harness's adversary."""
    return -HALF


def adv_exact(q_dep: float) -> float:
    """s_t = clip(q~_t, +-b/2): forfeit.py's `exact_threshold_*` play."""
    if q_dep > HALF:
        return HALF
    if q_dep < -HALF:
        return -HALF
    return q_dep


ADVERSARIES = {
    "eps_up": adv_eps_up,
    "const_low": adv_const_low,
    "exact": adv_exact,
}


# --------------------------------------------------------------------------------------
# The loop.  Transcribed from forfeit.run_arm (src/forfeit.py:508-582).
# --------------------------------------------------------------------------------------


def sim(
    T: int,
    tau: float,
    r: Callable[[float, int], float],
    qhat: Callable[[int], float],
    adv: Callable[[float], float],
    horizons: Optional[Sequence[int]] = None,
) -> Dict[int, Dict[str, float]]:
    horizons = sorted(horizons or [T])
    smooth = make_deadband(tau) if tau > 0.0 else (lambda p, y, t: y)
    q_dep = 0.0  # q~_1 = 0.0, forfeit.run_arm's F7
    n_err = 0
    E = 0.0
    max_abs_E = 0.0
    n_sat = 0
    out: Dict[int, Dict[str, float]] = {}
    hset = set(horizons)
    for t in range(1, T + 1):
        q_t = q_dep
        s = adv(q_t)
        err = 1 if s > q_t else 0  # the paper's strict indicator
        n_err += err
        E = n_err - ALPHA * t
        aE = -E if E < 0.0 else E
        if aE > max_abs_E:
            max_abs_E = aE
        thr = C * CFG.h(t)
        if E >= thr or E <= -thr:
            n_sat += 1
        q_raw = qhat(t + 1) + r(E, t)
        q_dep = smooth(q_dep, q_raw, t)
        if t in hset:
            out[t] = {
                "T": t,
                "miscoverage": n_err / t,
                "max_abs_E": max_abs_E,
                "E_at_T": E,
                "abs_E_at_T_over_T": abs(E) / t,
                "prop2_bound": CFG.prop2_bound(t),
                "ratio_max_abs_E_over_bound": max_abs_E / CFG.prop2_bound(t),
                "frac_saturated": n_sat / t,
            }
    return out


# --------------------------------------------------------------------------------------
# Boundaries
# --------------------------------------------------------------------------------------


def printed_tau_star(sup_r: float, sup_qhat: float) -> float:
    """The law as paper/sections/forfeit.tex prints it before this run."""
    return sup_r + sup_qhat - HALF


def sigma_plus(reach_plus: float, inf_qhat: float) -> float:
    """Corrected upward RETENTION boundary: reachable ceiling + inf_t qhat - b/2."""
    return reach_plus + inf_qhat - HALF


def sigma_minus(reach_minus: float, sup_qhat: float) -> float:
    """Corrected downward RETENTION boundary: |reachable floor| - sup_t qhat - b/2,
    and it is STRICT: coverage needs tau < sigma_minus."""
    return abs(reach_minus) - sup_qhat - HALF


# --------------------------------------------------------------------------------------
# Validation
# --------------------------------------------------------------------------------------


def validate(verbose: bool = True) -> Tuple[bool, List[Dict[str, object]]]:
    """`sim()` must reproduce forfeit.run_arm's committed numbers on the frozen settings."""
    ref = json.load(open(os.path.join(REPO_ROOT, REF_RUN)))
    want: Dict[Tuple[float, str], float] = {}
    for row in ref["aggregate_table"]:
        if row["arm"].startswith("deadband_tau") and row["T"] == 100_000:
            want[(float(row["arm"][12:]), row["regime"])] = row["miscoverage"]

    checks: List[Dict[str, object]] = []
    ok = True
    grid = (0.5, 0.9, 0.95, 0.99, 0.999, 1.0, 1.001, 1.01, 1.05, 1.1, 1.5)
    for tau in grid:
        got = sim(100_000, tau, r_clipped(), qhat_const(0.0), adv_eps_up)[100_000]
        exp = want[(tau, "adversarial")]
        hit = abs(round(got["miscoverage"], 6) - exp) < 1e-9
        ok &= hit
        checks.append(
            {
                "regime": "adversarial",
                "tau": tau,
                "committed": exp,
                "transcribed": round(got["miscoverage"], 6),
                "match": hit,
            }
        )
    for tau in (0.5, 0.9, 1.0, 1.5):
        got = sim(100_000, tau, r_clipped(), qhat_const(0.0), adv_exact)[100_000]
        exp = want[(tau, "exact_threshold_strict")]
        hit = abs(round(got["miscoverage"], 6) - exp) < 1e-9
        ok &= hit
        checks.append(
            {
                "regime": "exact_threshold_strict",
                "tau": tau,
                "committed": exp,
                "transcribed": round(got["miscoverage"], 6),
                "match": hit,
            }
        )
        # The load-bearing identity: under the strict indicator both s = clip(q~, +-b/2)
        # and s == -b/2 give err_t = 1{q~_t < -b/2}, so they are the SAME error process.
        got2 = sim(100_000, tau, r_clipped(), qhat_const(0.0), adv_const_low)[100_000]
        hit2 = abs(round(got2["miscoverage"], 6) - exp) < 1e-9
        ok &= hit2
        checks.append(
            {
                "regime": "exact_threshold_strict == s_t == -b/2",
                "tau": tau,
                "committed": exp,
                "transcribed": round(got2["miscoverage"], 6),
                "match": hit2,
            }
        )
    if verbose:
        for ch in checks:
            print(
                f"  {'OK ' if ch['match'] else 'MISMATCH'} {ch['regime']:<38} "
                f"tau={ch['tau']:<6} committed={ch['committed']:<9} "
                f"transcribed={ch['transcribed']}"
            )
        print("VALIDATION", "PASSED" if ok else "FAILED", f"({len(checks)} checks)")
    return ok, checks


# --------------------------------------------------------------------------------------
# The battery
# --------------------------------------------------------------------------------------


def battery() -> List[Dict[str, object]]:
    """Each entry: one (r_t, qhat) configuration, its two boundaries, and a tau grid.

    `reach_plus` / `reach_minus` are the levels the saturator is GUARANTEED to reach on
    the set the dynamics can actually visit -- the quantity the corrected law uses.
    `sup_r` is sup_x r_t(x), the quantity the printed law uses.  They differ exactly on
    the configurations built to make them differ.
    """
    return [
        {
            "id": "S-interior-qhat",
            "label": "constant interior scorecaster qhat == +0.4, harness saturator",
            "r": r_clipped(),
            "qhat": qhat_const(0.4),
            "sup_r": 2.0,
            "reach_plus": 2.0,
            "reach_minus": -2.0,
            "sup_qhat": 0.4,
            "inf_qhat": 0.4,
            "attained": True,
            "T": 100_000,
            "taus": [0.3, 0.55, 0.599, 0.6, 0.8, 1.0, 1.4, 1.5],
        },
        {
            "id": "S-interior-qhat-negative",
            "label": "constant interior scorecaster qhat == -0.4, harness saturator",
            "r": r_clipped(),
            "qhat": qhat_const(-0.4),
            "sup_r": 2.0,
            "reach_plus": 2.0,
            "reach_minus": -2.0,
            "sup_qhat": -0.4,
            "inf_qhat": -0.4,
            "attained": True,
            "T": 100_000,
            "taus": [0.6, 0.601, 1.0],
        },
        {
            "id": "S-far-sup-finite",
            "label": "sup_x r_t(x) = 10b, attained only on the unreachable set |x| > t^2",
            "r": r_far_sup(10.0 * B),
            "qhat": qhat_const(0.0),
            "sup_r": 20.0,
            "reach_plus": 2.0,
            "reach_minus": -2.0,
            "sup_qhat": 0.0,
            "inf_qhat": 0.0,
            "attained": False,
            "T": 100_000,
            "taus": [0.9, 1.0, 1.001, 1.5, 5.0],
        },
        {
            "id": "S-far-sup-infinite",
            "label": "sup_x r_t(x) unbounded, on the unreachable set |x| > t^2",
            "r": r_far_sup_infinite(),
            "qhat": qhat_const(0.0),
            "sup_r": float("inf"),
            "reach_plus": 2.0,
            "reach_minus": -2.0,
            "sup_qhat": 0.0,
            "inf_qhat": 0.0,
            "attained": False,
            "T": 100_000,
            "taus": [0.9, 1.0, 1.5, 3.0],
        },
        {
            "id": "S-asymmetric",
            "label": "asymmetric saturator, A+ = 4b and A- = -b, both attained at the radius",
            "r": r_asym(8.0, -2.0),
            "qhat": qhat_const(0.0),
            "sup_r": 8.0,
            "reach_plus": 8.0,
            "reach_minus": -2.0,
            "sup_qhat": 0.0,
            "inf_qhat": 0.0,
            "attained": True,
            "T": 100_000,
            "taus": [0.9, 0.999, 1.0, 1.5, 3.0, 6.9, 7.5],
        },
        {
            "id": "S-level4b-edge",
            "label": "the paper's level-4b setting, taken to its own tau* = 7",
            "r": r_clipped(4.0),
            "qhat": qhat_const(0.0),
            "sup_r": 8.0,
            "reach_plus": 8.0,
            "reach_minus": -8.0,
            "sup_qhat": 0.0,
            "inf_qhat": 0.0,
            "attained": True,
            "T": 100_000,
            "taus": [6.0, 6.9, 6.999, 7.0, 7.001, 7.5],
        },
        {
            "id": "S-unattained-sup",
            "label": "sup_x r_t(x) = 2b approached at rate 1/x and never attained",
            "r": r_unattained(4.0),
            "qhat": qhat_const(0.0),
            "sup_r": 4.0,
            # The sup is NOT reached at the radius; what condition (4) guarantees there is
            # exactly b, so that is the level the retention certificate may use.
            "reach_plus": 2.0,
            "reach_minus": -2.0,
            "sup_qhat": 0.0,
            "inf_qhat": 0.0,
            "attained": False,
            "T": 100_000,
            "taus": [2.5, 2.9, 2.99, 3.0, 3.001],
        },
        {
            "id": "S-attained-sup-control",
            "label": "control for S-unattained-sup: the same sup 2b, attained at the radius",
            "r": r_asym(4.0, -4.0),
            "qhat": qhat_const(0.0),
            "sup_r": 4.0,
            "reach_plus": 4.0,
            "reach_minus": -4.0,
            "sup_qhat": 0.0,
            "inf_qhat": 0.0,
            "attained": True,
            "T": 100_000,
            "taus": [2.9, 3.0, 3.001],
        },
        {
            "id": "S-wild-inband",
            "label": "extrema attained at the radius, wrong sign inside it, which (4) permits",
            "r": r_wild_inband(2.0, -8.0),
            "qhat": qhat_const(0.0),
            "sup_r": 2.0,
            "reach_plus": 2.0,
            "reach_minus": -8.0,
            "sup_qhat": 0.0,
            "inf_qhat": 0.0,
            "attained": True,
            "T": 100_000,
            "taus": [0.5, 1.0, 1.001, 1.5],
        },
        {
            "id": "S-corner-plus",
            "label": "the paper's qhat == +b/2 corner, including the tau = 0 control",
            "r": r_clipped(),
            "qhat": qhat_const(HALF),
            "sup_r": 2.0,
            "reach_plus": 2.0,
            "reach_minus": -2.0,
            "sup_qhat": HALF,
            "inf_qhat": HALF,
            "attained": True,
            "T": 100_000,
            "taus": [0.0, 0.5, 1.5],
        },
        {
            "id": "S-corner-minus",
            "label": "the paper's qhat == -b/2 corner, including the tau = 0 control",
            "r": r_clipped(),
            "qhat": qhat_const(-HALF),
            "sup_r": 2.0,
            "reach_plus": 2.0,
            "reach_minus": -2.0,
            "sup_qhat": -HALF,
            "inf_qhat": -HALF,
            "attained": True,
            "T": 100_000,
            "taus": [0.0, 0.5, 1.5],
        },
        {
            "id": "S-time-varying-qhat",
            "label": "time-varying legal scorecaster: qhat_t = +b/2 on t a power of two, 0 otherwise",
            "r": r_clipped(),
            "qhat": qhat_pow2(),
            "sup_r": 2.0,
            "reach_plus": 2.0,
            "reach_minus": -2.0,
            "sup_qhat": HALF,
            "inf_qhat": 0.0,
            "attained": True,
            "T": 1_000_000,
            "horizons": [100_000, 200_000, 500_000, 1_000_000],
            "taus": [0.5, 0.9, 1.0, 1.01, 1.05, 1.1, 1.5, 1.9, 2.0, 2.5],
        },
        {
            "id": "S-necessity-sweep",
            "label": "necessity: four legal saturators just above their own tau*+",
            "r": None,  # filled per row below
            "qhat": qhat_const(0.0),
            "sup_r": None,
            "reach_plus": None,
            "reach_minus": None,
            "sup_qhat": 0.0,
            "inf_qhat": 0.0,
            "attained": True,
            "T": 100_000,
            "taus": [],
        },
    ]


def run_battery(verbose: bool = True) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for cfgd in battery():
        if cfgd["id"] == "S-necessity-sweep":
            continue
        T = int(cfgd["T"])
        horizons = cfgd.get("horizons") or [T]
        sp = (
            sigma_plus(cfgd["reach_plus"], cfgd["inf_qhat"])
            if cfgd["reach_plus"] is not None
            else None
        )
        sm = (
            sigma_minus(cfgd["reach_minus"], cfgd["sup_qhat"])
            if cfgd["reach_minus"] is not None
            else None
        )
        pts = printed_tau_star(cfgd["sup_r"], cfgd["sup_qhat"])
        if verbose:
            print(f"\n== {cfgd['id']}: {cfgd['label']}")
            print(
                f"   printed tau* = {pts}   corrected: tau <= {sp} and tau < {sm}"
                f"   (reach at the radius equals the sup: {cfgd['attained']})"
            )
        for tau in cfgd["taus"]:
            for advname in ("eps_up", "const_low"):
                res = sim(
                    T, tau, cfgd["r"], cfgd["qhat"], ADVERSARIES[advname], horizons=horizons
                )
                for h in horizons:
                    rows.append(
                        {
                            "config": cfgd["id"],
                            "label": cfgd["label"],
                            "adversary": advname,
                            "tau": tau,
                            "printed_tau_star": pts,
                            "corrected_sigma_plus": sp,
                            "corrected_sigma_minus": sm,
                            "reach_at_radius_equals_sup": cfgd["attained"],
                            **res[h],
                        }
                    )
                r1 = res[horizons[-1]]
                if verbose:
                    print(
                        f"   tau={tau:<7} {advname:<10} miscov={r1['miscoverage']:<10.6f} "
                        f"max|E|={r1['max_abs_E']:<12.2f} |E_T|/T={r1['abs_E_at_T_over_T']:.5f}"
                    )

    # The necessity sweep: four legal saturators, four overshoots above their own tau*+.
    if verbose:
        print("\n== S-necessity-sweep: tau just above tau*+, four legal saturators")
    for a_plus, a_minus, lab in (
        (2.0, -2.0, "level b"),
        (3.0, -3.0, "level 1.5b"),
        (8.0, -8.0, "level 4b"),
        (2.0, -8.0, "asymmetric (b, -4b)"),
    ):
        ts = a_plus - HALF
        for d in (1e-6, 1e-3, 0.5, 5.0):
            res = sim(
                100_000, ts + d, r_asym(a_plus, a_minus), qhat_const(0.0), adv_eps_up
            )[100_000]
            rows.append(
                {
                    "config": "S-necessity-sweep",
                    "label": f"necessity overshoot, saturator {lab}",
                    "adversary": "eps_up",
                    "tau": ts + d,
                    "overshoot_above_tau_star_plus": d,
                    "printed_tau_star": ts,
                    "corrected_sigma_plus": ts,
                    "corrected_sigma_minus": abs(a_minus) - HALF,
                    "reach_at_radius_equals_sup": True,
                    **res,
                }
            )
            if verbose:
                print(
                    f"   {lab:<20} tau=tau*+ + {d:<8g} miscov={res['miscoverage']:<10.6f} "
                    f"max|E|={res['max_abs_E']:.1f}"
                )

    # The endpoint sweep.  The upper boundary is CLOSED and the lower one OPEN, and the
    # baseline setting cannot show either, because tau*+ = tau*- = 1 there and the two
    # endpoints coincide.  These four saturators separate them: tau*+ < tau*- in each, so
    # tau = tau*+ exactly is the upper endpoint on its own.
    if verbose:
        print("\n== S-endpoint-sweep: tau = tau*+ exactly, with tau*+ < tau*-")
    for a_plus, a_minus in ((2.0, -8.0), (3.0, -20.0), (8.0, -40.0), (2.5, -12.0)):
        ts = a_plus - HALF
        for advname in ("eps_up", "const_low"):
            res = sim(
                100_000, ts, r_asym(a_plus, a_minus), qhat_const(0.0), ADVERSARIES[advname]
            )[100_000]
            rows.append(
                {
                    "config": "S-endpoint-sweep",
                    "label": f"upper endpoint, saturator (A+, A-) = ({a_plus}, {a_minus})",
                    "adversary": advname,
                    "tau": ts,
                    "printed_tau_star": ts,
                    "corrected_sigma_plus": ts,
                    "corrected_sigma_minus": abs(a_minus) - HALF,
                    "reach_at_radius_equals_sup": True,
                    **res,
                }
            )
            if verbose:
                print(
                    f"   (A+,A-)=({a_plus},{a_minus}) tau=tau*+={ts:<5} {advname:<10} "
                    f"miscov={res['miscoverage']:.6f} max|E|={res['max_abs_E']:.2f}"
                )

    # The tangent family: Proposition A's constant kappa(tau) against the measurement.
    if verbose:
        print("\n== S-tangent: unbounded integrator, Proposition A's constant vs measurement")
    for tau in (0.5, 0.9, 1.5, 3.0):
        kappa = math.atan(HALF + tau) / math.atan(B)
        res = sim(1_000_000, tau, r_tangent(), qhat_const(0.0), adv_eps_up)[1_000_000]
        rows.append(
            {
                "config": "S-tangent",
                "label": "ACT23 tangent integrator, null scorecaster",
                "adversary": "eps_up",
                "tau": tau,
                "kappa": kappa,
                "reach_bound_kappa_c_h_T_plus_1": kappa * C * CFG.h(1_000_000) + 1.0,
                "printed_tau_star": float("inf"),
                "corrected_sigma_plus": float("inf"),
                "corrected_sigma_minus": float("inf"),
                "reach_at_radius_equals_sup": False,
                **res,
            }
        )
        if verbose:
            print(
                f"   tau={tau:<5} kappa={kappa:<7.4f} max|E|={res['max_abs_E']:<8.2f} "
                f"prop2={res['prop2_bound']:.4f} ratio={res['ratio_max_abs_E_over_bound']:.4f} "
                f"reach bound={kappa * C * CFG.h(1_000_000) + 1.0:.4f}"
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
        except Exception:  # pragma: no cover
            return ""

    return {
        "commit": run(["git", "rev-parse", "HEAD"]),
        "branch": run(["git", "rev-parse", "--abbrev-ref", "HEAD"]),
        "dirty": bool(run(["git", "status", "--porcelain"])),
        "describe": run(["git", "describe", "--always", "--dirty"]),
    }


def environment() -> Dict[str, str]:
    return {
        "python": sys.version,
        "python_executable": sys.executable,
        "platform": platform.platform(),
        "machine": platform.machine(),
    }


def free_choices() -> List[Dict[str, str]]:
    return [
        {
            "id": "S1",
            "choice": "legality of every configuration",
            "value": "condition (4) for every r_t; qhat_t in [-b/2, b/2] and predictable",
            "justification": (
                "Condition (4) is a lower bound on |r_t| outside |x| < c h(t) and imposes "
                "nothing inside it and nothing above b outside it, so every saturator here "
                "is admissible.  Theorem 1 asks only that qhat be predictable and lie in "
                "[-b/2, b/2], not that it be constant.  Both are asserted in code."
            ),
            "consequence_if_wrong": (
                "An illegal configuration would falsify nothing: the law is quantified over "
                "the admissible class, so a counterexample must be inside it."
            ),
        },
        {
            "id": "S2",
            "choice": "two adversaries per configuration",
            "value": "s_t = clip(q~_t + eps, +-b/2) and s_t == -b/2",
            "justification": (
                "Both are legal under Theorem 1's score budget.  The printed law models the "
                "first only.  The second is the mirror play, and under the strict indicator "
                "it has the same error process as forfeit.py's exact_threshold_strict regime."
            ),
            "consequence_if_wrong": (
                "Running one adversary measures one direction and reports the other as safe."
            ),
        },
        {
            "id": "S3",
            "choice": "indicator",
            "value": "err_t = 1{s_t > q~_t}, strict, everywhere",
            "justification": (
                "The paper's own indicator.  No result in this file turns on the tie "
                "convention; forfeit.py's exact_threshold_* regimes carry that comparison."
            ),
            "consequence_if_wrong": "A convention-dependent result would be reported as a class result.",
        },
        {
            "id": "S4",
            "choice": "horizons",
            "value": "1e5 everywhere; 1e6 for the time-varying scorecaster and the tangent family",
            "justification": (
                "The time-varying scorecaster's failure is an oscillation whose miscoverage "
                "rate sits near alpha while |E_T| grows linearly, so it needs the longer "
                "horizon and the four-horizon |E_T|/T readout to separate from a transient."
            ),
            "consequence_if_wrong": (
                "A Theta(T) failure read at one short horizon can be mistaken for coverage."
            ),
        },
    ]


def main(argv: Optional[List[str]] = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    only_validate = bool(argv) and argv[0] == "validate"

    print("== VALIDATION: transcribed loop vs committed forfeit.run_arm ==")
    ok, checks = validate()
    if not ok:
        print("aborting: the transcription does not reproduce the frozen harness")
        return 1
    if only_validate:
        return 0

    t0 = time.time()
    rows = run_battery()
    elapsed = time.time() - t0

    git = git_state()
    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    short = (git.get("commit") or "nocommit")[:8]
    payload = {
        "schema": SCHEMA,
        "purpose": (
            "Stress the dead-band boundary law over the admissible class that condition (4) "
            "and Theorem 1 actually define, rather than over the five settings "
            "src/forfeit.py sweeps.  Feeds Table 2 of paper/sections/forfeit.tex."
        ),
        "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "wall_clock_seconds": elapsed,
        "git": git,
        "environment": environment(),
        "reference_run_validated_against": REF_RUN,
        "validation_checks": checks,
        "config": {
            "alpha": ALPHA,
            "b": B,
            "c": C,
            "h_name": CFG.h_name,
            "score_bound_frac": CFG.score_bound_frac,
            "adversary_eps": EPS,
            "q_deployed_init": 0.0,
            "indicator": "err_t = 1{s_t > q~_t} (strict)",
        },
        "boundaries": {
            "printed": "tau* = sup_x r_t(x) + sup_t qhat_t - b/2",
            "corrected_retention": (
                "tau <= inf_t(A^+_t + qhat_{t+1}) - b/2  AND  "
                "tau < inf_t(|A^-_t| - qhat_{t+1}) - b/2, with A^+_t, A^-_t the levels "
                "r_t is guaranteed to reach on the set the dynamics can visit"
            ),
            "corrected_failure": (
                "tau > sup_t(A^+_t + qhat_{t+1}) - b/2  OR  "
                "tau >= sup_t(|A^-_t| - qhat_{t+1}) - b/2"
            ),
        },
        "free_choices": free_choices(),
        "rows": rows,
    }
    out = os.path.join(REPO_ROOT, "results", f"boundary-stress-{stamp}-{short}.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1, sort_keys=False)
    print(f"\nwrote {os.path.relpath(out, REPO_ROOT)}  ({len(rows)} rows, {elapsed:.1f} s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
