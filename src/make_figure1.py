#!/usr/bin/env python3
# =====================================================================================
# make_figure1.py -- Figure 1: the dead-band coverage cliff and where its edge sits.
#
# Deterministic, offline.  Reads results/ directly and plots MEASURED values only.
# No value in this figure is computed by this script except tau*, which is computed
# from the boundary law and then CHECKED against every measured point.
#
# -------------------------------------------------------------------------------------
# PROVENANCE -- every (file, field path) this script reads
# -------------------------------------------------------------------------------------
# (1) results/forfeit-variations-20260820T101445Z.json
#       $.base_config.alpha                     -> alpha = 0.1   (the nominal level)
#       $.base_config.b                         -> b = 2.0       (score bound; scale of tau)
#       $.base_config.horizons                  -> [1e4, 1e5, 2e5, 1e6]
#       $.boundary_law                          -> the law this figure is about (string)
#       $.purpose                               -> why the variation wave exists (string)
#       $.git.commit                            -> code state that produced the rows
#       $.rows[*].variation                     -> which (r_t, qhat) setting
#       $.rows[*].arm                           -> smoother arm name; "deadband_tau<W>"
#       $.rows[*].T                             -> horizon
#       $.rows[*].miscoverage                   -> PLOTTED as y in panel (a)
#     NOTE (provenance gap, reported to the orchestrator): this file records only
#     $.base_config -- it does NOT store a per-variation config block.  The per-setting
#     (saturator_level_mult, scorecaster_const, saturator_kind) triples below are
#     therefore transcribed from the variation NAMES plus the Config documentation in
#     src/forfeit.py (lines ~296-334), and each one is then VERIFIED against measured
#     miscoverage via check_law() -- a wrong triple would produce a law violation.
#
# (2) results/forfeit-20260820T063132Z-83747c45.json
#       $.config.alpha, $.config.b              -> same alpha, b
#       $.config.deadband_taus                  -> the eleven-point grid
#       $.aggregate_table[*].arm                -> "deadband_tau<W>"
#       $.aggregate_table[*].params.tau         -> PLOTTED as x in panel (b)
#       $.aggregate_table[*].regime             -> filtered to "adversarial" (the primary)
#       $.aggregate_table[*].T                  -> filtered to 100000 (largest run there)
#       $.aggregate_table[*].miscoverage        -> PLOTTED as y in panel (b)
#
# (3) src/forfeit.py -- read, not imported, for the two structural facts:
#       saturator() (approx. lines 336-342):  r_t(x) = b * saturator_level_mult
#                                             * clip(x/(c*h(t)), -1, +1)
#         => sup_x |r_t(x)| = saturator_level_mult * b, attained (clip is exact).
#       Config.scorecaster_const (line ~303): qhat_t == scorecaster_const for all t
#         => sup_t qhat_t = scorecaster_const.
#       Config.saturator_kind == "tangent" (line ~314): ACT23's tan() integrator,
#         which has NO finite sup => tau* is unbounded.
#
# THE LAW (verbatim from source (1), $.boundary_law):
#       tau* = sup_x r_t(x) + sup_t qhat_t - b/2 ; coverage lost for tau > tau*
# =====================================================================================

import json
import math
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VAR_PATH = os.path.join(REPO, "results", "forfeit-variations-20260820T101445Z.json")
GRID_PATH = os.path.join(REPO, "results", "forfeit-20260820T063132Z-83747c45.json")
OUT_PDF = os.path.join(REPO, "figures", "figure1_boundary.pdf")

# Horizon policy.  The five settings' three widths exist at T in {1e4,1e5,2e5,1e6};
# we take the largest, 1e6.  The four WIDE baseline bands (tau = 2, 2.5, 3, 5) were
# only ever run at T = 2e5, so they are plotted at their largest available T and
# flagged, both in the figure and in the caption.
T_MAIN = 1_000_000
T_WIDE_FALLBACK = 200_000
T_GRID = 100_000

# ------------------------------------------------------------------------------------
# Settings: variation key -> (label, saturator_level_mult, scorecaster_const, kind)
# See the PROVENANCE note above: transcribed from names + src/forfeit.py, then verified.
# ------------------------------------------------------------------------------------
SETTINGS = [
    # key, short label, level_mult, qhat, saturator kind, colour, marker, ms, lw, dash
    ("baseline_clipped_qhat0", r"$\hat{q}\equiv 0$, level $b$", 1.0, 0.0, "clipped",
     "#000000", "o", 4.0, 0.9, (0, ())),
    ("scorecaster_const_plus_b_over_2", r"$\hat{q}\equiv +b/2$", 1.0, +1.0, "clipped",
     "#0072B2", "s", 6.2, 1.3, (0, (5.0, 1.8))),
    ("scorecaster_const_minus_b_over_2", r"$\hat{q}\equiv -b/2$", 1.0, -1.0, "clipped",
     "#D55E00", "^", 8.6, 1.7, (0, (1.6, 1.6))),
    ("saturator_level_4b", r"level $4b$", 4.0, 0.0, "clipped",
     "#009E73", "D", 7.6, 1.7, (0, (6.0, 1.8, 1.4, 1.8))),
    ("saturator_tangent_ACT23", r"tangent (ACT23)", None, 0.0, "tangent",
     "#CC79A7", "v", 10.2, 2.3, (0, (9.0, 2.4))),
]
WIDE_KEY = "wide_deadbands_baseline"
WIDE_PARENT = "baseline_clipped_qhat0"


def tau_from_arm(arm):
    """'deadband_tau1.5' -> 1.5 ; None for non-dead-band arms."""
    if not arm.startswith("deadband_tau"):
        return None
    return float(arm[len("deadband_tau"):])


def load():
    with open(VAR_PATH) as f:
        var = json.load(f)
    with open(GRID_PATH) as f:
        grid = json.load(f)
    return var, grid


def tau_star(level_mult, qhat, b):
    """tau* = sup_x r_t(x) + sup_t qhat_t - b/2.  level_mult None => tangent => inf."""
    if level_mult is None:
        return math.inf
    return level_mult * b + qhat - b / 2.0


def collect(var):
    """Return {setting_key: [(tau, miscoverage, T), ...]} from the variation rows."""
    out = {k: [] for k, *_ in SETTINGS}
    for r in var["rows"]:
        tau = tau_from_arm(r["arm"])
        if tau is None:
            continue
        if r["variation"] in out and r["T"] == T_MAIN:
            out[r["variation"]].append((tau, r["miscoverage"], r["T"]))
        elif r["variation"] == WIDE_KEY and r["T"] == T_WIDE_FALLBACK:
            out[WIDE_PARENT].append((tau, r["miscoverage"], r["T"]))
    for k in out:
        out[k].sort()
    return out


def collect_grid(grid):
    """The eleven-point baseline grid, primary (adversarial) regime, largest T."""
    pts = []
    for r in grid["aggregate_table"]:
        if not r["arm"].startswith("deadband_tau"):
            continue
        if r["regime"] != "adversarial" or r["T"] != T_GRID:
            continue
        pts.append((float(r["params"]["tau"]), r["miscoverage"], r["T"]))
    pts.sort()
    return pts


def covers(misc, alpha):
    """Binary outcome.  Measured values are either ~alpha or exactly 1.0; nothing between."""
    return misc < 0.5


def check_law(series, taustars, alpha, verbose=True):
    """Every measured point must obey: covers <=> tau <= tau*.  Raises if not."""
    rows, bad = [], []
    for key, label, *_ in [(s[0], s[1]) for s in SETTINGS]:
        pass
    for s in SETTINGS:
        key, label = s[0], s[1]
        ts = taustars[key]
        for tau, misc, T in series[key]:
            c = covers(misc, alpha)
            predicted = tau <= ts + 1e-12
            ok = (c == predicted)
            rows.append(dict(setting=key, label=label, tau_star=ts, tau=tau,
                             T=T, miscoverage=misc, covers=c,
                             predicted_covers=predicted, consistent=ok))
            if not ok:
                bad.append(rows[-1])
            if c and abs(misc - alpha) > 3e-3:
                bad.append(dict(rows[-1], note="covering run not at alpha"))
            if (not c) and misc != 1.0:
                bad.append(dict(rows[-1], note="failing run not at 1.0"))
    if verbose:
        print("=" * 92)
        print("BOUNDARY-LAW CHECK  tau* = sup_x r_t(x) + sup_t qhat_t - b/2")
        print("=" * 92)
        print(f"{'setting':34s} {'tau*':>6s} {'tau':>6s} {'T':>9s} {'miscoverage':>12s} "
              f"{'covers':>7s} {'pred':>6s} {'ok':>3s}")
        for r in rows:
            print(f"{r['setting']:34s} {r['tau_star']:>6.3g} {r['tau']:>6.3g} "
                  f"{r['T']:>9d} {r['miscoverage']:>12.6f} {str(r['covers']):>7s} "
                  f"{str(r['predicted_covers']):>6s} {'OK' if r['consistent'] else 'XX':>3s}")
    if bad:
        raise SystemExit("LAW VIOLATION -- stop and report:\n" + json.dumps(bad, indent=2))
    return rows


def main():
    var, grid = load()
    alpha = var["base_config"]["alpha"]
    b = var["base_config"]["b"]
    assert alpha == grid["config"]["alpha"] and b == grid["config"]["b"]

    taustars = {s[0]: tau_star(s[2], s[3], b) for s in SETTINGS}
    series = collect(var)
    gridpts = collect_grid(grid)

    law_rows = check_law(series, taustars, alpha)

    print("\nELEVEN-POINT GRID (baseline, adversarial regime, T = %d)" % T_GRID)
    for tau, misc, T in gridpts:
        print(f"   tau={tau:<7g} miscoverage={misc:.6f}  "
              f"{'covers' if covers(misc, alpha) else 'FORFEITS'}")
    print("\ntau* per setting:", {k: v for k, v in taustars.items()})

    # ---------------------------------------------------------------------------
    # FIGURE
    # ---------------------------------------------------------------------------
    plt.rcParams.update({
        "pdf.fonttype": 42, "ps.fonttype": 42,
        "font.size": 8, "axes.labelsize": 8, "axes.titlesize": 7.5,
        "xtick.labelsize": 6.5, "ytick.labelsize": 6.5, "legend.fontsize": 6.0,
        "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6,
        "xtick.major.size": 2.4, "ytick.major.size": 2.4,
        "xtick.minor.size": 1.3, "ytick.minor.size": 1.3,
        "lines.solid_capstyle": "butt",
    })

    # 5.5in is exactly \textwidth in neurips_2026.sty, so width=\textwidth places the
    # figure 1:1 and the base font lands at exactly 8pt.  HEIGHT REDUCED 2.45 -> 1.95in
    # in S5 wave 4: the four floats did not pack into a four-page body, and this is the
    # one saving that costs no content at all.  Re-checked visually after the change.
    fig = plt.figure(figsize=(5.5, 1.95))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.68, 1.0],
                          left=0.078, right=0.988, bottom=0.215, top=0.855, wspace=0.20)
    axA = fig.add_subplot(gs[0, 0])
    axB = fig.add_subplot(gs[0, 1])

    YLO, YHI = 0.072, 1.95
    for ax in (axA, axB):
        ax.set_yscale("log")
        ax.set_ylim(YLO, YHI)
        ax.axhline(alpha, color="0.55", lw=0.7, ls=(0, (4, 2)), zorder=1)
        ax.axhline(1.0, color="0.80", lw=0.6, zorder=0)

    # ---------------- panel (a): the five settings ----------------
    XLO, XHI = 0.40, 10.5
    axA.set_xscale("log")
    axA.set_xlim(XLO, XHI)
    axA.set_xticks([0.5, 0.9, 1.5, 2, 3, 5, 7])
    axA.set_xticklabels(["0.5", "0.9", "1.5", "2", "3", "5", "7"])
    axA.xaxis.set_minor_locator(plt.NullLocator())
    axA.set_yticks([0.1, 1.0])
    axA.set_yticklabels(["0.1", "1.0"])
    axA.yaxis.set_minor_locator(plt.NullLocator())
    axA.set_xlabel(r"dead-band width $\tau$   (score units, $b=2$)", labelpad=1.5)
    axA.set_ylabel("realised miscoverage", labelpad=2.0)

    handles = []
    for key, label, lvl, qh, kind, col, mk, ms, lw, dash in SETTINGS:
        ts = taustars[key]
        pts = series[key]
        # segments, split where the run crosses tau* (no line drawn across the cliff)
        for (t0, m0, _), (t1, m1, _) in zip(pts, pts[1:]):
            if t0 <= ts < t1:
                continue
            axA.plot([t0, t1], [m0, m1], color=col, lw=lw, ls=dash,
                     solid_capstyle="round", zorder=3, alpha=0.9)
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        axA.plot(xs, ys, linestyle="none", marker=mk, ms=ms, mfc="none",
                 mec=col, mew=1.05, zorder=4)
        tslab = r"$\infty$" if math.isinf(ts) else f"{ts:g}"
        handles.append(Line2D([], [], color=col, lw=lw, ls=dash, marker=mk,
                              ms=min(ms, 6.0), mfc="none", mec=col, mew=1.0,
                              label=label + r"   $\tau^{\star}\!=\!$" + tslab))

        # tau* marker
        if math.isinf(ts):
            axA.annotate(r"$\tau^{\star}=\infty$", xy=(XHI * 0.985, 0.30),
                         xytext=(4.15, 0.30), color=col, fontsize=6.2, va="center",
                         ha="left",
                         arrowprops=dict(arrowstyle="-|>", color=col, lw=1.0,
                                         shrinkA=1.0, shrinkB=0.0))
        elif ts <= 0:
            axA.annotate(r"$\tau^{\star}=0$", xy=(XLO * 1.005, 1.33),
                         xytext=(0.62, 1.33), color=col, fontsize=6.2, va="center",
                         ha="left",
                         arrowprops=dict(arrowstyle="-|>", color=col, lw=1.0,
                                         shrinkA=1.0, shrinkB=0.0))
        else:
            axA.axvline(ts, color=col, lw=0.85, ls=(0, (3.2, 2.0)), zorder=2, alpha=0.85)
            axA.text(ts, YHI * 0.93, r"$\tau^{\star}$" + f"={ts:g}", color=col,
                     fontsize=6.2, ha="center", va="top",
                     bbox=dict(fc="white", ec="none", pad=0.6, alpha=0.85))

    _bb = dict(fc="white", ec="none", pad=0.8, alpha=0.9)
    axA.text(0.985, alpha * 1.16, r"$\alpha=0.1$", transform=axA.get_yaxis_transform(),
             ha="right", va="bottom", fontsize=6.2, color="0.35", bbox=_bb, zorder=6)
    axA.text(0.985, 1.0 * 1.06, "total forfeit", transform=axA.get_yaxis_transform(),
             ha="right", va="bottom", fontsize=6.2, color="0.55", bbox=_bb, zorder=6)

    leg = axA.legend(handles=handles, loc="center left", bbox_to_anchor=(0.015, 0.475),
                     frameon=True, framealpha=0.92, edgecolor="0.8", fancybox=False,
                     borderpad=0.35, labelspacing=0.30, handlelength=2.4,
                     handletextpad=0.5, borderaxespad=0.0)
    leg.get_frame().set_linewidth(0.4)
    leg.set_title(r"vertical dashes $=\tau^{\star}$ from the law",
                  prop={"size": 5.8})
    leg.get_title().set_color("0.35")

    # the four wide bands come from a shorter run; flag them in situ
    axA.annotate(r"$\tau\!\geq\!2$: $T\!=\!2\!\cdot\!10^{5}$", xy=(3.05, 1.0),
                 xytext=(2.75, 0.46), fontsize=5.8, color="0.35", ha="left", va="center",
                 arrowprops=dict(arrowstyle="-", color="0.6", lw=0.5,
                                 shrinkA=1.0, shrinkB=2.0))

    axA.set_title(r"(a) the edge moves with $(r_t,\hat{q})$;  $T=10^{6}$",
                  loc="left", pad=3.0)

    # ---------------- panel (b): the located edge ----------------
    xs = list(range(len(gridpts)))
    ys = [p[1] for p in gridpts]
    labels = [f"{p[0]:g}" for p in gridpts]
    axB.set_xlim(-0.7, len(gridpts) - 0.3)
    # the cliff sits between the last covering point and the first failing point
    icut = next(i for i, p in enumerate(gridpts) if not covers(p[1], alpha))
    axB.axvspan(icut - 1, icut, color="#000000", alpha=0.075, lw=0, zorder=0)
    axB.plot(xs[:icut], ys[:icut], color="#000000", lw=0.9, marker="o", ms=3.4,
             mfc="none", mew=1.0, zorder=3)
    axB.plot(xs[icut:], ys[icut:], color="#000000", lw=0.9, marker="o", ms=3.4,
             mfc="none", mew=1.0, zorder=3)
    axB.set_xticks(xs)
    axB.set_xticklabels(labels, rotation=90, fontsize=5.6)
    axB.set_yticks([0.1, 1.0])
    axB.set_yticklabels([])
    axB.yaxis.set_minor_locator(plt.NullLocator())
    axB.set_xlabel(r"$\tau$   (eleven-point grid)", labelpad=1.0)
    axB.annotate(r"$\tau^{\star}=1$", xy=(icut - 0.5, 0.315), fontsize=6.2,
                 ha="center", va="center", color="#000000",
                 bbox=dict(fc="white", ec="0.8", lw=0.4, pad=1.2))
    axB.text(0.03, alpha * 1.16, r"$\alpha=0.1$", transform=axB.get_yaxis_transform(),
             ha="left", va="bottom", fontsize=6.2, color="0.35")
    axB.set_title(r"(b) that edge, located;  $T=10^{5}$", loc="left", pad=3.0)

    for ax in (axA, axB):
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)

    # CreationDate is pinned to None so a rerun reproduces the file BYTE FOR BYTE.
    # Without it matplotlib stamps the wall clock and every rerun differs, which
    # would make this figure the one artefact in results/-backed provenance that
    # cannot be checked by re-running the generator and diffing.
    fig.savefig(OUT_PDF, metadata={'CreationDate': None})
    print(f"\nwrote {OUT_PDF}")

    # -------- spot-check: JSON value vs plotted value, printed side by side --------
    print("\n" + "=" * 92)
    print("SPOT-CHECK  (raw JSON value  vs  value handed to matplotlib)")
    print("=" * 92)
    raw_var = {(r["variation"], r["arm"], r["T"]): r["miscoverage"] for r in var["rows"]}
    checks = [
        ("baseline_clipped_qhat0", "deadband_tau0.9", T_MAIN),
        ("baseline_clipped_qhat0", "deadband_tau1.5", T_MAIN),
        ("scorecaster_const_plus_b_over_2", "deadband_tau1.5", T_MAIN),
        ("scorecaster_const_minus_b_over_2", "deadband_tau0.5", T_MAIN),
        ("saturator_level_4b", "deadband_tau1.5", T_MAIN),
        ("saturator_tangent_ACT23", "deadband_tau1.5", T_MAIN),
        (WIDE_KEY, "deadband_tau5", T_WIDE_FALLBACK),
    ]
    for variation, arm, T in checks:
        tau = tau_from_arm(arm)
        target = WIDE_PARENT if variation == WIDE_KEY else variation
        plotted = [m for (t, m, tt) in series[target] if t == tau and tt == T]
        raw = raw_var[(variation, arm, T)]
        assert len(plotted) == 1 and plotted[0] == raw, (variation, arm, T, plotted, raw)
        print(f"  {variation:34s} tau={tau:<5g} T={T:<8d} json={raw:.6f}  "
              f"plotted={plotted[0]:.6f}  MATCH")
    raw_grid = {(r["arm"], r["T"], r["regime"]): r["miscoverage"]
                for r in grid["aggregate_table"]}
    for arm in ("deadband_tau1", "deadband_tau1.001"):
        tau = tau_from_arm(arm)
        plotted = [m for (t, m, _) in gridpts if t == tau]
        raw = raw_grid[(arm, T_GRID, "adversarial")]
        assert len(plotted) == 1 and plotted[0] == raw
        print(f"  grid {arm:29s} tau={tau:<5g} T={T_GRID:<8d} json={raw:.6f}  "
              f"plotted={plotted[0]:.6f}  MATCH")

    return law_rows, taustars, series, gridpts


if __name__ == "__main__":
    main()
