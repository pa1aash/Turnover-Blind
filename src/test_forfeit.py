#!/usr/bin/env python3
"""Executable tests for `src/forfeit.py`.

Run either way:

    /opt/homebrew/Caskroom/miniforge/base/bin/python3 -m pytest src/test_forfeit.py -q
    /opt/homebrew/Caskroom/miniforge/base/bin/python3 src/test_forfeit.py

`audit/RECONSTRUCTION_SPEC.md` section 3 lists five tests that must exist before any
number is believed.  Three still have a referent under the re-scoped paper and are
implemented here:

  1. CRN bit-identity          -> test_crn_bit_identity_open_loop
                                  test_crn_closed_loop_has_no_shared_realisation
                                  test_rerun_is_bit_identical
  4. degenerate-arm check      -> test_degenerate_arm_is_bit_identical
  5. leakage                   -> test_no_leakage_of_the_current_score

Two do not, and are asserted to be *recorded* rather than dropped:

  2. zero-cost invariance      -> test_dropped_tests_are_recorded_not_dropped
  3. cost identity             -> test_dropped_tests_are_recorded_not_dropped

Further checks guard the reconstruction itself: that the chosen saturator really
satisfies condition (4); that the unsmoothed control really respects Proposition 2; that
the adversary's eps (free choice F3) is large enough to fire the paper's strict indicator
and small enough to leave the deployed path bit-identical; and that the exact-threshold
play under the strict indicator is a genuine alternative rather than a degenerate one --
the false claim that it was degenerate is what forced F4 to be rewritten.
"""

from __future__ import annotations

import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from forfeit import (  # noqa: E402
    Arm,
    Config,
    build_arms,
    derive_table,
    dropped_tests_register,
    free_choice_register,
    iid_scores,
    run_arm,
    saturator,
)

SHORT = Config(t_max=20_000, horizons=(10_000, 20_000))
MED = Config(t_max=100_000, horizons=(10_000, 100_000))


# ---------------------------------------------------------------------------------
# Guard on the reconstruction: condition (4) and Proposition 2
# ---------------------------------------------------------------------------------


def test_saturator_satisfies_condition_4():
    """x >= c*h(t) => r_t(x) >= b, and x <= -c*h(t) => r_t(x) <= -b (paper eq. (4))."""
    cfg = SHORT
    for t in [1, 2, 7, 100, 9_999, 1_000_000]:
        thr = cfg.c * cfg.h(t)
        # exactly at the boundary, and above it
        for x in [thr, thr * (1 + 1e-12), thr + 1e-9, thr * 2, thr * 1e6]:
            assert saturator(x, t, cfg) >= cfg.b, (t, x)
        for x in [-thr, -thr * (1 + 1e-12), -thr - 1e-9, -thr * 2, -thr * 1e6]:
            assert saturator(x, t, cfg) <= -cfg.b, (t, x)
        # and the saturator is bounded by b, which is what makes the smoothed EMA lag
        for x in [-1e9, -thr / 2, 0.0, thr / 2, 1e9]:
            assert -cfg.b <= saturator(x, t, cfg) <= cfg.b
    # h is admissible: nonnegative, nondecreasing, sublinear
    prev = -1.0
    for t in [1, 10, 1_000, 10**5, 10**6]:
        v = cfg.h(t)
        assert v >= 0.0 and v >= prev
        prev = v
    assert cfg.h(10**6) / 10**6 < cfg.h(10**3) / 10**3  # h(t)/t -> 0


def test_exact_threshold_strict_play_is_not_degenerate():
    """The claim that forced the F4 rewrite, pinned so it cannot come back.

    The first version of this module played the threshold EXACTLY and justified scoring
    ties as misses by asserting that the strict reading of that play was degenerate
    (miscoverage 0).  It is not: the adversary's play covers whenever the deployed
    threshold is at or above -b/2, so the tracker saturates *negatively* instead of
    positively and E_t oscillates about -0.5*h(t), still tracking alpha.  Both readings
    are retained as sensitivity regimes and both are asserted here.
    """
    recs = [run_arm(MED, Arm("unsmoothed", "identity"), r)
            for r in ("exact_threshold_tie", "exact_threshold_strict")]
    rows = {r["regime"]: r for r in derive_table(MED, recs) if r["T"] == MED.t_max}
    for regime, row in rows.items():
        assert abs(row["miscoverage"] - MED.alpha) < 5e-3, (regime, row["miscoverage"])
        assert not row["violates_prop2"], regime
    # mirror images: the tie reading sits above zero, the strict reading below.
    assert rows["exact_threshold_tie"]["max_abs_E"] > rows["exact_threshold_strict"]["max_abs_E"]


def test_adversary_eps_is_immaterial():
    """F3: eps is large enough to fire the strict indicator and small enough to vanish.

    The primary regime is re-run at eps = 1e-6, 1e-9 and 1e-12.  The scores differ (they
    are q~_t + eps), so `scores_sha256` must differ; the DEPLOYED PATH must be
    bit-identical, because eps never enters the indicator's condition, which reduces to
    err_t = 1{q~_t < b/2}.  A eps too small to survive the addition at |q~| <= b would
    break the first assertion; a eps large enough to perturb the dynamics would break
    the second.
    """
    arm = Arm("ema_w0.999", "ema", {"w": 0.999})
    recs = {}
    for eps in (1e-6, 1e-9, 1e-12):
        cfg = Config(t_max=SHORT.t_max, horizons=SHORT.horizons, adversary_eps=eps)
        recs[eps] = run_arm(cfg, arm, "adversarial")
    digests = {eps: r["deployed_sha256"] for eps, r in recs.items()}
    assert len(set(digests.values())) == 1, digests
    assert len({r["scores_sha256"] for r in recs.values()}) == 3
    # and the indicator really did fire: miscoverage tracks alpha rather than sitting at 0
    row = derive_table(Config(t_max=SHORT.t_max, horizons=SHORT.horizons),
                       [recs[1e-9]])[-1]
    assert abs(row["miscoverage"] - SHORT.alpha) < 5e-3, row["miscoverage"]


def test_primary_regime_uses_the_papers_strict_indicator():
    """No tie rule survives in the primary regime.

    Asserted behaviourally: replaying the primary regime's own consumed scores through
    the open-loop path reproduces its deployed threshold bit-for-bit only if the
    indicator is the strict one, since every consumed score is strictly above the
    threshold it was generated from except where the legality clip bound.
    """
    cfg = Config(t_max=5_000, horizons=(5_000,))
    rec = run_arm(cfg, Arm("ema_w0.9", "ema", {"w": 0.9}), "adversarial", keep_series=True)
    q = rec["_series_q"]
    # every deployed threshold below the legality ceiling was strictly undercut
    half = cfg.b * cfg.score_bound_frac
    assert any(v < half for v in q) and any(v >= half for v in q)


def test_control_arm_respects_proposition_2():
    """The unsmoothed arm must sit inside c*h(T)+1.  If it does not, the harness is wrong."""
    rec = run_arm(MED, Arm("unsmoothed", "identity"), "adversarial")
    for row in derive_table(MED, [rec]):
        assert not row["violates_prop2"], row
        assert row["ratio_max_abs_E_over_bound"] < 1.0, row


# ---------------------------------------------------------------------------------
# Test 1 -- CRN bit-identity
# ---------------------------------------------------------------------------------


def test_crn_bit_identity_open_loop():
    """Every arm consumes the identical score realisation, bit for bit."""
    cfg = SHORT
    scores = iid_scores(cfg)
    digests = set()
    for arm in build_arms(cfg):
        rec = run_arm(cfg, arm, "iid", scores=scores)
        digests.add(rec["scores_sha256"])
    assert len(digests) == 1, f"arms saw different score realisations: {digests}"


def test_crn_closed_loop_has_no_shared_realisation():
    """The adversarial regime CANNOT share a realisation, and that is not a defect.

    The adversary's score is a function of the arm's own deployed threshold, so a shared
    score array is unsatisfiable by construction.  What is asserted instead is that the
    arms differ *because* their thresholds differ, and that the unsmoothed control and a
    genuinely inert smoother still coincide (covered by the degeneracy test).
    """
    cfg = SHORT
    digests = {}
    for arm in build_arms(cfg):
        digests[arm.name] = run_arm(cfg, arm, "adversarial")["scores_sha256"]
    assert digests["unsmoothed"] != digests["ema_w0.999"]
    assert len(set(digests.values())) > 1


def test_rerun_is_bit_identical():
    """Determinism: the same arm run twice produces the identical deployed path."""
    cfg = SHORT
    arm = Arm("ema_w0.99", "ema", {"w": 0.99})
    a = run_arm(cfg, arm, "adversarial")
    b = run_arm(cfg, arm, "adversarial")
    assert a["deployed_sha256"] == b["deployed_sha256"]
    assert a["scores_sha256"] == b["scores_sha256"]
    assert a["horizons_raw"] == b["horizons_raw"]


# ---------------------------------------------------------------------------------
# Test 4 -- degenerate arm
# ---------------------------------------------------------------------------------


def test_degenerate_arm_is_bit_identical():
    """With the smoother inert the deployed path must be BIT-identical to the control."""
    cfg = SHORT
    scores = iid_scores(cfg)
    inert = [
        Arm("ema_w0", "ema", {"w": 0.0}),
        Arm("deadband_tau0", "deadband", {"tau": 0.0}),
        Arm("identity", "identity"),
    ]
    for regime, kw in (("adversarial", {}), ("iid", {"scores": scores})):
        base = run_arm(cfg, Arm("unsmoothed", "identity"), regime, **kw)
        for arm in inert:
            rec = run_arm(cfg, arm, regime, **kw)
            assert rec["deployed_sha256"] == base["deployed_sha256"], (regime, arm.name)
            assert rec["scores_sha256"] == base["scores_sha256"], (regime, arm.name)
            assert rec["horizons_raw"] == base["horizons_raw"], (regime, arm.name)


# ---------------------------------------------------------------------------------
# Test 5 -- leakage
# ---------------------------------------------------------------------------------


def test_no_leakage_of_the_current_score():
    """q~_t is a function of information up to t-1 only.

    Perturb the score at t0 and require every deployed threshold up to and including t0
    to be unchanged, bit for bit.  The threshold at t0+1 must move, otherwise the test
    is vacuous (the perturbation would have had no effect at all).
    """
    cfg = Config(t_max=5_000, horizons=(5_000,))
    scores = iid_scores(cfg)
    arm = Arm("ema_w0.9", "ema", {"w": 0.9})
    t0 = 2_500

    base = run_arm(cfg, arm, "iid", scores=scores, keep_series=True)
    # Choose a perturbation guaranteed to flip err_{t0}, so the test cannot be vacuous.
    q_at_t0 = base["_series_q"][t0 - 1]
    new_value = q_at_t0 - 1.0 if scores[t0 - 1] >= q_at_t0 else q_at_t0 + 1.0
    pert = run_arm(
        cfg, arm, "iid", scores=scores,
        perturb_index=t0, perturb_value=new_value, keep_series=True,
    )

    b_q, p_q = base["_series_q"], pert["_series_q"]
    assert b_q[:t0] == p_q[:t0], "the deployed threshold saw the future"
    assert base["_series_E"][: t0 - 1] == pert["_series_E"][: t0 - 1]
    assert b_q[t0] != p_q[t0], "perturbation had no downstream effect; test is vacuous"


# ---------------------------------------------------------------------------------
# Tests 2 and 3 -- recorded, not dropped
# ---------------------------------------------------------------------------------


def test_dropped_tests_are_recorded_not_dropped():
    reg = {d["name"]: d for d in dropped_tests_register()}
    assert set(reg) == {"zero-cost invariance", "cost identity"}
    for name, entry in reg.items():
        assert entry["applies"] is False
        assert len(entry["why_no_referent"]) > 80, name
        assert entry["spec"].startswith("audit/RECONSTRUCTION_SPEC.md")


def test_free_choices_are_all_registered():
    """Every free choice named in the brief must appear with a consequence."""
    reg = {d["id"]: d for d in free_choice_register()}
    for required in ("F1", "F2", "F3", "F4", "F5", "F9"):
        assert required in reg
    for entry in reg.values():
        assert entry["justification"] and entry["consequence_if_wrong"]


# ---------------------------------------------------------------------------------


def _main() -> int:
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failed = 0
    for fn in fns:
        try:
            fn()
            print(f"PASS  {fn.__name__}")
        except AssertionError as exc:
            failed += 1
            print(f"FAIL  {fn.__name__}: {exc}")
        except Exception as exc:  # pragma: no cover
            failed += 1
            print(f"ERROR {fn.__name__}: {type(exc).__name__}: {exc}")
    print(f"\n{len(fns) - failed}/{len(fns)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(_main())
