#!/usr/bin/env python3
# =====================================================================================
# make_figure1.py -- the two DATA figures.  Deterministic, offline, results/-backed.
#
#   figures/figure1_boundary.pdf  -> compiled as FIGURE 2 (Section 3, body)
#   figures/figure3_settings.pdf  -> compiled as FIGURE 3 (Appendix A)
#
# FILE NAMING, RECORDED SO IT IS NOT "TIDIED" LATER.  figure1_boundary.pdf keeps its S5
# name even though it typesets as Figure 2, because docs/GATES.md G7.1 and G7.13 and
# docs/S5_REPORT.md cite that exact path as provenance evidence; renaming it would break
# three records to fix a cosmetic mismatch that G7.13 already explains.  The new file
# follows the compiled number, which is where the convention should have started.
#
# -------------------------------------------------------------------------------------
# S6 SUB-SESSION A -- REBUILT.  WHAT CHANGED AND WHY (diagnosis: research/S6/A0-diagnosis.json)
# -------------------------------------------------------------------------------------
# The S5 figure put five (r_t, qhat) settings and five tau* markers into one panel and
# plotted the eleven-point grid on a CATEGORICAL axis.  Measured, at 400 dpi:
#
#   * panel (b) was categorical (xs = range(11)).  The located window tau in [1, 1.001]
#     took 10.000% of the axis while being 0.0910% of the true log span 0.5..1.5:
#     INFLATED x109.9.
#     THE SAME METRIC, APPLIED TO THE REBUILD, AND IT DOES NOT COME OUT AT 1.0.  The S6
#     adversarial critic measured the shipped figure: the grey band is 13.14pt of a
#     177.66pt axis, 7.40% measured and 7.370% analytically (linear half-zone 0.5 decade
#     over a 6.7842-decade axis), against the same 0.09098% true-log-tau share.  That is
#     INFLATED x81.0, a 26% reduction and not a repair.  IT IS RECORDED RATHER THAN
#     BURIED, and here is why the metric does not transfer.  It is the right test for the
#     OLD axis and the wrong test for this one.  The old axis declared NOTHING: it
#     presented itself as an axis of tau values, placed them by integer index, and the
#     reader had no way to know.  Measuring it against the honest coordinate for a
#     positive continuous variable, log tau, was therefore exactly the right test.  This
#     axis DECLARES its coordinate -- the label reads "tau, placed by tau - tau* (symlog)",
#     the caption gives the linear zone, and every labelled tick carries the tau it marks --
#     so the reader is not being told log tau and shown something else.  Any correct log
#     or symlog axis magnifies its origin without limit; the metric condemns all of them,
#     which is what makes it the wrong acceptance test here.
#     WHAT THE CRITIC IS RIGHT ABOUT, AND IT IS A REAL LIMIT OF THIS DESIGN: the VISIBLE
#     WIDTH of the grey band carries no information about how tight the bracket is.  With
#     linthresh = 1e-7 a bracket ten thousand times tighter would render at the same 7.4%.
#     AND THE COMPRESSION HALF OF THE OLD DIAGNOSIS IS REPRODUCED ALMOST EXACTLY, which is
#     the sharpest thing either critic said.  The old axis gave tau in [0.5, 0.9] 10.0% of
#     its width against a true log share of 53.5%, i.e. COMPRESSED x0.19.  This axis gives
#     it 10.303%: x0.19 again, to two significant figures.  Eight of the ten gaps land
#     between 4.4% and 14.7% of a uniform 10%.  That is not an accident and it is not
#     fixable by tuning: the eleven widths are a geometric ladder in the OFFSET by
#     construction, so any log-like axis in that offset places them near-uniformly.  What
#     symlog buys over the index axis is DISCLOSURE, not a different picture: the sign
#     symmetry and ordering about tau* become readable, and the coordinate is named on the
#     axis and in the caption instead of being silently assumed.  The caption now also
#     gives the reader the true share, so the correction does not live only in this file.
#     Only the tick labels tell the reader that.  LINSCALE is 0.45 rather than
#     matplotlib's default 1.0 precisely to shrink that band -- the default would render
#     it at 15.0% -- but the residual is real and is stated here rather than left for a
#     referee to find.  The 0.5 -> 0.9 interval, 53.5% of the true span, took 10%:
#     COMPRESSED x0.19.  The eleven-point grid's whole content -- that the edge is pinned
#     inside a window one part in a thousand wide -- was erased by the axis.
#   * four markers nested at (tau=0.5, miscov~0.1) and four at (0.9, ~0.1), three at
#     (1.5, ~0.1); the blue square was all but invisible under the green diamond and the
#     pink triangle, and four of the five series' LINES overplotted along the y = 0.1 run.
#   * the legend frame overwrote 627 px of the tau*=1 column and 651 px of the tau*=2
#     column (pixel diff, legend drawn vs not drawn).  Those two vertical dashes ARE the
#     figure's claim, and the legend broke both.
#   * the white-backed "total forfeit" and "alpha = 0.1" boxes overwrote 168 px of the
#     tau*=7 column.
#   * panel (b)'s grey band was never explained in the caption.
#
#   NOT REPRODUCED, and recorded because the brief asserted it: panel (a)'s x-axis was
#   ALREADY log-scaled (set_xscale("log")).  Its rendered tick positions matched true log
#   positions to 1.1e-16 and the gap-by-gap distortion factor was exactly 1.000 at all six
#   gaps.  Panel (a) never had an axis-scaling defect; it had a density defect.
#
# THE FIX (option 1 of the brief: split).  Figure 2 keeps ONE setting -- the null
# scorecaster, the only one with runs on BOTH sides of its own tau* -- so the cliff is
# shown without an overlay.  Its two panels both use continuous, correctly scaled axes:
#   (a) log tau over the full sweep;
#   (b) SYMLOG in (tau - tau*), matplotlib's native symlog, linthresh 1e-3.  The eleven
#       grid points are a symmetric geometric ladder about tau = 1 -- their offsets are
#       -0.5, -0.1, -0.05, -0.01, -0.001, 0, +0.001, +0.01, +0.05, +0.1, +0.5 -- so
#       symlog in the offset is their natural coordinate: tick spacing is then true
#       multiplicative distance from the edge, and the bisection reads as a bisection.
#       Ticks are labelled with the tau values themselves, and the axis label names the
#       transform, so nothing is placed by a rule the reader cannot see.
# Figure 3 takes the five-setting comparison that panel (a) used to carry.  Setting is a
# CATEGORICAL variable and gets a categorical axis (five rows); tau stays continuous and
# keeps its log axis.  Every one of the 19 runs is plotted, and the unbounded tangent
# integrator is an explicit off-scale arrow rather than an omission.
#
# -------------------------------------------------------------------------------------
# PROVENANCE -- every (file, field path) either figure reads
# -------------------------------------------------------------------------------------
# (1) results/forfeit-variations-20260820T101445Z.json
#       $.base_config.alpha                     -> alpha = 0.1   (the nominal level)
#       $.base_config.b                         -> b = 2.0       (score bound; scale of tau)
#       $.base_config.horizons                  -> [1e4, 1e5, 2e5, 1e6]
#       $.boundary_law                          -> the law both figures are about (string)
#       $.git.commit                            -> code state that produced the rows
#       $.rows[*].variation                     -> which (r_t, qhat) setting
#       $.rows[*].arm                           -> smoother arm name; "deadband_tau<W>"
#       $.rows[*].T                             -> horizon
#       $.rows[*].miscoverage                   -> PLOTTED as y in Fig 2(a); as the
#                                                  covers/forfeits split in Fig 3
#     NOTE (provenance gap, unchanged from S5): this file records only $.base_config -- it
#     does NOT store a per-variation config block.  The per-setting (saturator_level_mult,
#     scorecaster_const, saturator_kind) triples below are therefore transcribed from the
#     variation NAMES plus the Config documentation in src/forfeit.py (lines ~296-334),
#     and each one is then VERIFIED against measured miscoverage via check_law() -- a
#     wrong triple would produce a law violation and stop the build.
#
# (2) results/forfeit-20260820T063132Z-83747c45.json
#       $.config.alpha, $.config.b              -> same alpha, b
#       $.config.deadband_taus                  -> the eleven-point grid
#       $.aggregate_table[*].arm                -> "deadband_tau<W>"
#       $.aggregate_table[*].params.tau         -> PLOTTED as x in Fig 2(b)
#       $.aggregate_table[*].regime             -> filtered to "adversarial" (the primary)
#       $.aggregate_table[*].T                  -> filtered to 100000 (largest run there)
#       $.aggregate_table[*].miscoverage        -> PLOTTED as y in Fig 2(b)
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
OUT_FIG2 = os.path.join(REPO, "figures", "figure1_boundary.pdf")
OUT_FIG3 = os.path.join(REPO, "figures", "figure3_settings.pdf")

# Horizon policy.  The five settings' three widths exist at T in {1e4,1e5,2e5,1e6};
# we take the largest, 1e6.  The four WIDE baseline bands (tau = 2, 2.5, 3, 5) were
# only ever run at T = 2e5, so they are plotted at their largest available T and
# flagged, both in the figures and in the captions.
T_MAIN = 1_000_000
T_WIDE_FALLBACK = 200_000
T_GRID = 100_000

# ------------------------------------------------------------------------------------
# Settings: variation key -> (label, saturator_level_mult, scorecaster_const, kind)
# See the PROVENANCE note above: transcribed from names + src/forfeit.py, then verified.
# Ordered by tau*, ascending, which is the order Figure 3's categorical axis uses.
# ------------------------------------------------------------------------------------
SETTINGS = [
    # key, short label, level_mult, qhat, saturator kind
    ("scorecaster_const_minus_b_over_2", r"$\hat{q}\equiv{-}b/2$", 1.0, -1.0, "clipped"),
    ("baseline_clipped_qhat0", r"$\hat{q}\equiv 0$, level $b$", 1.0, 0.0, "clipped"),
    ("scorecaster_const_plus_b_over_2", r"$\hat{q}\equiv{+}b/2$", 1.0, +1.0, "clipped"),
    ("saturator_level_4b", r"level $4b$", 4.0, 0.0, "clipped"),
    ("saturator_tangent_ACT23", r"tangent integrator", None, 0.0, "tangent"),
]
WIDE_KEY = "wide_deadbands_baseline"
WIDE_PARENT = "baseline_clipped_qhat0"

# The one setting Figure 2 draws: the only one with runs on BOTH sides of its own tau*.
FEATURED = "baseline_clipped_qhat0"

C_COVER = "#0072B2"      # covering runs (Okabe-Ito blue)
C_FAIL = "#D55E00"       # total-forfeit runs (Okabe-Ito vermillion)
C_EDGE = "#000000"       # tau*, the law's prediction


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


def check_grid_law(gridpts, ts, alpha, verbose=True):
    """Same law, applied to the eleven-point grid at the featured setting."""
    bad = []
    for tau, misc, T in gridpts:
        if covers(misc, alpha) != (tau <= ts + 1e-12):
            bad.append(dict(tau=tau, T=T, miscoverage=misc, tau_star=ts))
    if bad:
        raise SystemExit("GRID LAW VIOLATION -- stop and report:\n"
                         + json.dumps(bad, indent=2))
    if verbose:
        print(f"\nELEVEN-POINT GRID (baseline, adversarial regime, T = {T_GRID})"
              f"   all {len(gridpts)} points obey the law at tau* = {ts:g}")
        for tau, misc, T in gridpts:
            print(f"   tau={tau:<7g} miscoverage={misc:.6f}  "
                  f"{'covers' if covers(misc, alpha) else 'FORFEITS'}")


RC = {
    "pdf.fonttype": 42, "ps.fonttype": 42,
    "font.size": 8, "axes.labelsize": 8, "axes.titlesize": 7.5,
    "xtick.labelsize": 6.5, "ytick.labelsize": 6.5, "legend.fontsize": 6.2,
    "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6,
    "xtick.major.size": 2.4, "ytick.major.size": 2.4,
    "xtick.minor.size": 1.3, "ytick.minor.size": 1.3,
    "lines.solid_capstyle": "butt",
}

YLO, YHI = 0.062, 2.6          # miscoverage axis, log, shared by both Figure 2 panels
LINTHRESH = 1e-3               # symlog: |tau - tau*| below this is drawn linearly
LINSCALE = 0.45                # width of that linear zone, in decade-widths


# =====================================================================================
# FIGURE 2 -- the cliff at one setting, and that edge located
# =====================================================================================
def figure2(series, gridpts, taustars, alpha, b):
    plt.rcParams.update(RC)
    ts = taustars[FEATURED]
    pts = series[FEATURED]

    # 5.5in is exactly \textwidth in neurips_2026.sty, so width=\textwidth places the
    # figure 1:1 and the base font lands at exactly 8pt.
    # HEIGHT 1.95 -> 1.75in, S6 sub-session C.  S5 needed 1.95 to separate five overlaid
    # series in panel (a); panel (a) now carries ONE, and the vertical range holds two
    # attainable values.  The 0.20in this returns is what pays for the Introduction's
    # new opening paragraph.  Legibility is not traded for it: fonts are unchanged and
    # the bottom margin is RAISED 0.255 -> 0.285 so panel (b)'s rotated labels keep
    # their room.  overlap_audit() below is what checks that, not an opinion.
    fig = plt.figure(figsize=(5.5, 1.75))
    # WIDTH SPLIT IS MEASURED, NOT CHOSEN BY EYE.  Panel (b) carries eleven rotated
    # tick labels against panel (a)'s six, so it gets the WIDER half even though it
    # is the zoom: at [1.14, 1.0] the overlap audit below flagged 0.9/0.95 and
    # 1.05/1.1 colliding in (b).  At [0.92, 1.0] every label clears.
    gs = fig.add_gridspec(1, 2, width_ratios=[0.92, 1.0],
                          left=0.079, right=0.988, bottom=0.285, top=0.845, wspace=0.115)
    axA = fig.add_subplot(gs[0, 0])
    axB = fig.add_subplot(gs[0, 1])

    for ax in (axA, axB):
        ax.set_yscale("log")
        ax.set_ylim(YLO, YHI)
        ax.axhline(alpha, color="0.55", lw=0.7, ls=(0, (4, 2)), zorder=1)
        ax.axhline(1.0, color="0.78", lw=0.6, zorder=0)
        ax.set_yticks([0.1, 1.0])
        ax.yaxis.set_minor_locator(plt.NullLocator())
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)

    # ---------------- panel (a): the full sweep, log tau ----------------
    # tau is continuous, so the axis is continuous.  Tick positions are true log
    # positions; only the LABELS are hand-chosen, and each sits at its own value.
    axA.set_xscale("log")
    axA.set_xlim(0.42, 6.6)
    # No tick AT tau* = 1: log(1/0.9) is 3.8% of this axis and a horizontal "1" label
    # collides with "0.9" (caught by the overlap audit).  The value is not lost -- the
    # dashed rule below is labelled with it.
    axA.set_xticks([0.5, 0.9, 1.5, 2, 2.5, 3, 5])
    axA.set_xticklabels(["0.5", "0.9", "1.5", "2", "2.5", "3", "5"])
    axA.xaxis.set_minor_locator(plt.NullLocator())
    axA.set_yticklabels(["0.1", "1.0"])
    axA.set_xlabel(r"dead-band width $\tau$   (score units, $b=2$)", labelpad=1.5)
    axA.set_ylabel("realised miscoverage", labelpad=2.0)

    # the cliff: draw each side, never a segment across it
    for lo, hi in zip(pts, pts[1:]):
        if lo[0] <= ts < hi[0]:
            continue
        col = C_COVER if covers(lo[1], alpha) else C_FAIL
        axA.plot([lo[0], hi[0]], [lo[1], hi[1]], color=col, lw=1.0, zorder=3)
    for tau, misc, T in pts:
        c = covers(misc, alpha)
        axA.plot([tau], [misc], marker="o", ms=4.6, mew=1.1, zorder=4,
                 mec=C_COVER if c else C_FAIL,
                 mfc=(C_COVER if c else C_FAIL) if T == T_MAIN else "white")

    axA.axvline(ts, color=C_EDGE, lw=0.9, ls=(0, (3.2, 2.0)), zorder=2)
    axA.text(ts * 1.055, YHI * 0.94, r"$\tau^{\star+}=1$", color=C_EDGE, fontsize=6.6,
             ha="left", va="top")
    axA.text(0.435, alpha * 1.15, r"$\alpha=0.1$", fontsize=6.4, color="0.35",
             ha="left", va="bottom")
    axA.text(0.435, 1.0 * 1.08, "total forfeit", fontsize=6.4, color="0.5",
             ha="left", va="bottom")

    hz = [Line2D([], [], ls="none", marker="o", ms=4.6, mew=1.1, mec="0.25",
                 mfc="0.25", label=r"$T=10^{6}$"),
          Line2D([], [], ls="none", marker="o", ms=4.6, mew=1.1, mec="0.25",
                 mfc="white", label=r"$T=2{\times}10^{5}$")]
    # placed in the empty band between the two attainable outcomes, clear of the
    # tau* rule: measured, not eyeballed -- see the overlap audit in main().
    leg = axA.legend(handles=hz, loc="lower right", bbox_to_anchor=(1.005, 0.235),
                     frameon=False, borderpad=0.2, labelspacing=0.28,
                     handletextpad=0.4, borderaxespad=0.0, title="in (a):")
    # THE LEGEND IS TITLED "in (a):" AND THE TITLE IS LOAD-BEARING.  Marker fill encodes the
    # horizon in panel (a) -- filled 1e6, open 2e5 -- but panel (b) is a single run at 1e5
    # and draws every marker filled.  Untitled, this legend sits inside the same figure box
    # and tells a reader who does not reach the caption that (b)'s filled markers are 1e6.
    leg.get_title().set_fontsize(6.0)
    leg.set_zorder(6)
    axA.set_title(r"(a) the cliff at the null scorecaster", loc="left", pad=3.0)

    # ---------------- panel (b): that edge, located, symlog in (tau - tau*) ----------
    # The eleven grid points are a symmetric geometric ladder about tau*, so their
    # natural coordinate is the OFFSET, on a symlog scale.  Placing them by index
    # instead -- as S5 did -- inflated the located window x109.9 (research/S6/A0).
    gtau = [p[0] for p in gridpts]
    gy = [p[1] for p in gridpts]
    gx = [t - ts for t in gtau]
    axB.set_xscale("symlog", linthresh=LINTHRESH, linscale=LINSCALE)
    axB.set_xlim(-0.78, 0.78)
    # ALL ELEVEN measured widths carry a tick; NINE carry a label.  In |tau - tau*| the
    # grid is the decade ladder 0.5, 0.1, 0.01, 0.001, 0 with two half-decade refinements
    # at 0.05.  The ladder is labelled; the two refinements (tau = 0.95 and 1.05) get
    # MINOR ticks, because 0.301 decades of axis is 8.7pt here and two 6pt rotated labels
    # need 10.4pt with the audit's clearance.  Shrinking the type to fit was the wrong
    # trade -- illegible tick labels were one of the defects being repaired.
    LADDER = [0.5, 0.9, 0.99, 0.999, 1.0, 1.001, 1.01, 1.1, 1.5]
    axB.set_xticks([t - ts for t in gtau if t in LADDER])
    axB.set_xticklabels([f"{t:g}" for t in gtau if t in LADDER],
                        rotation=90, fontsize=6.0)
    axB.set_xticks([t - ts for t in gtau if t not in LADDER], minor=True)
    axB.tick_params(axis="x", which="minor", length=1.3)
    axB.set_yticklabels([])
    axB.set_xlabel(r"$\tau$, placed by $\tau-\tau^{\star+}$ (symlog)", labelpad=1.0)

    icut = next(i for i, p in enumerate(gridpts) if not covers(p[1], alpha))
    axB.axvspan(gx[icut - 1], gx[icut], color=C_EDGE, alpha=0.10, lw=0, zorder=0)
    axB.plot(gx[:icut], gy[:icut], color=C_COVER, lw=1.0, marker="o", ms=3.6,
             mfc=C_COVER, mew=1.0, zorder=3)
    axB.plot(gx[icut:], gy[icut:], color=C_FAIL, lw=1.0, marker="o", ms=3.6,
             mfc=C_FAIL, mew=1.0, zorder=3)
    axB.set_title(r"(b) that edge, located;  $T=10^{5}$", loc="left", pad=3.0)

    fig.savefig(OUT_FIG2, metadata={"CreationDate": None})
    print(f"\nwrote {OUT_FIG2}")
    return fig, axA, axB


# =====================================================================================
# FIGURE 3 -- how tau* moves across the five settings (Appendix A)
# =====================================================================================
def figure3(series, taustars, alpha, b):
    plt.rcParams.update(RC)
    fig = plt.figure(figsize=(5.5, 1.72))
    # Axes box leaves room for the setting names on the left and the tau* column
    # on the right; at width 0.545 there was 0.20 of dead figure to the right of
    # the tau* labels, which is width the tau axis should have.
    ax = fig.add_axes([0.235, 0.245, 0.625, 0.615])

    XLO, XHI = 0.40, 9.0
    ax.set_xscale("log")                       # tau is continuous
    ax.set_xlim(XLO, XHI)
    # No tick AT 1: it abuts "0.9" and the pair rendered as the single token
    # "0.91".  tau* = 1 is carried by the right-hand tau* column instead.
    ax.set_xticks([0.5, 0.9, 1.5, 2, 3, 5, 7])
    ax.set_xticklabels(["0.5", "0.9", "1.5", "2", "3", "5", "7"])
    ax.xaxis.set_minor_locator(plt.NullLocator())
    ax.set_xlabel(r"dead-band width $\tau$   (score units, $b=2$)", labelpad=1.5)

    n = len(SETTINGS)
    ax.set_ylim(-0.7, n - 0.3)                 # setting is categorical
    ax.set_yticks(range(n))
    ax.set_yticklabels([s[1] for s in SETTINGS])
    ax.tick_params(axis="y", length=0)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)

    for i, s in enumerate(SETTINGS):
        key, label = s[0], s[1]
        ts = taustars[key]
        ax.axhline(i, color="0.90", lw=0.5, zorder=0)
        # the admissible band on this row: tau <= tau*, where the law predicts coverage
        right = XHI if math.isinf(ts) else max(ts, XLO)
        if right > XLO:
            ax.fill_between([XLO, right], i - 0.30, i + 0.30,
                            color=C_COVER, alpha=0.085, lw=0, zorder=1)
        if math.isinf(ts):
            ax.annotate("", xy=(XHI * 0.995, i), xytext=(6.2, i), zorder=4,
                        arrowprops=dict(arrowstyle="-|>", color=C_EDGE, lw=0.9,
                                        shrinkA=0, shrinkB=0))
        elif ts <= XLO:
            # TAIL AT 0.455, NOT 0.52.  At 0.52 the tail landed INSIDE the tau = 0.5
            # marker's footprint (the marker spans tau 0.483..0.517) and the arrow read as
            # emanating from that data point, which is the opposite of what it means.  The
            # tau* = inf arrow at the other end is free-standing; both now are.
            ax.annotate("", xy=(XLO * 1.002, i), xytext=(0.455, i), zorder=4,
                        arrowprops=dict(arrowstyle="-|>", color=C_EDGE, lw=0.9,
                                        shrinkA=0, shrinkB=0))
        else:
            ax.plot([ts, ts], [i - 0.32, i + 0.32], color=C_EDGE, lw=1.1,
                    solid_capstyle="butt", zorder=4)

        for tau, misc, T in series[key]:
            c = covers(misc, alpha)
            ax.plot([tau], [i], marker="o", ms=4.6, mew=1.1, zorder=5,
                    mec=C_COVER if c else C_FAIL,
                    mfc=(C_COVER if c else C_FAIL) if T == T_MAIN else "white")

    # tau* as a right-hand column: the five values, read off against each other
    sec = ax.secondary_yaxis("right")
    sec.set_yticks(range(n))
    sec.set_yticklabels([r"$\infty$" if math.isinf(taustars[s[0]])
                         else f"{taustars[s[0]]:g}" for s in SETTINGS])
    sec.tick_params(axis="y", length=0)
    sec.spines["right"].set_visible(False)
    ax.text(1.037, 1.055, r"$\tau^{\star+}$", transform=ax.transAxes,
            ha="center", va="bottom", fontsize=7.5)
    ax.text(-0.007, 1.055, r"$(r_t,\hat{q})$", transform=ax.transAxes,
            ha="right", va="bottom", fontsize=7.5)

    hz = [Line2D([], [], ls="none", marker="o", ms=4.6, mew=1.1, mec=C_COVER,
                 mfc=C_COVER, label=r"covers ($\approx\alpha$)"),
          Line2D([], [], ls="none", marker="o", ms=4.6, mew=1.1, mec=C_FAIL,
                 mfc=C_FAIL, label="total forfeit (1.0)"),
          Line2D([], [], ls="none", marker="o", ms=4.6, mew=1.1, mec="0.25",
                 mfc="white", label=r"open: $T=2{\times}10^{5}$"),
          Line2D([], [], color=C_EDGE, lw=1.1, label=r"$\tau^{\star+}$ from the law")]
    ax.legend(handles=hz, loc="upper center", bbox_to_anchor=(0.5, -0.30), ncol=4,
              frameon=False, borderpad=0.2, handletextpad=0.45, columnspacing=1.5,
              borderaxespad=0.0)

    fig.savefig(OUT_FIG3, metadata={"CreationDate": None})
    print(f"wrote {OUT_FIG3}")
    return fig, ax


# =====================================================================================
# OVERLAP AUDIT -- the readability check runs INSIDE the generator, not beside it
# =====================================================================================
AUDIT_PAD = 1.6   # points, each side.  Bbox.overlaps() is a STRICT intersection test
                  # and passed a 0.9 / 1 tick pair that rendered as the single token
                  # "0.91"; boxes are grown by this before testing so abutting counts.


def overlap_audit(fig, axes, name):
    """Report every pair of drawn text artists whose boxes come within AUDIT_PAD of each
    other.  Zero is the acceptance criterion; anything else is printed and stops main()."""
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    pad = AUDIT_PAD * fig.dpi / 72.0

    def grow(bb):
        return bb.expanded(1.0, 1.0).padded(pad)

    items = []
    for ax in axes:
        for t in ax.texts:
            if t.get_visible() and t.get_text().strip():
                items.append((t.get_text(), grow(t.get_window_extent(r))))
        leg = ax.get_legend()
        if leg is not None:
            items.append(("<legend>", grow(leg.get_window_extent(r))))
        for lab in ax.get_xticklabels() + ax.get_yticklabels():
            if lab.get_text().strip():
                items.append((f"tick {lab.get_text()!r}", grow(lab.get_window_extent(r))))
    hits = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            a, b = items[i][1], items[j][1]
            if a.overlaps(b):
                hits.append((items[i][0], items[j][0]))
    print(f"\n{name}: {len(items)} text/legend boxes, {len(hits)} overlapping pairs")
    for h in hits:
        print("   OVERLAP:", h)
    return hits


def main():
    var, grid = load()
    alpha = var["base_config"]["alpha"]
    b = var["base_config"]["b"]
    assert alpha == grid["config"]["alpha"] and b == grid["config"]["b"]

    taustars = {s[0]: tau_star(s[2], s[3], b) for s in SETTINGS}
    series = collect(var)
    gridpts = collect_grid(grid)

    law_rows = check_law(series, taustars, alpha)
    check_grid_law(gridpts, taustars[FEATURED], alpha)
    print("\ntau* per setting:", {k: v for k, v in taustars.items()})

    f2, axA, axB = figure2(series, gridpts, taustars, alpha, b)
    f3, ax3 = figure3(series, taustars, alpha, b)

    bad2 = overlap_audit(f2, (axA, axB), "Figure 2")
    bad3 = overlap_audit(f3, (ax3,), "Figure 3")
    if bad2 or bad3:
        raise SystemExit("TEXT OVERLAP -- fix the layout before shipping the figure.")

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

    n_fig2 = len(series[FEATURED]) + len(gridpts)
    n_fig3 = sum(len(series[s[0]]) for s in SETTINGS)
    print(f"\npoints plotted: Figure 2 = {n_fig2} ({len(series[FEATURED])} sweep + "
          f"{len(gridpts)} grid), Figure 3 = {n_fig3} (all 19 runs)")

    return law_rows, taustars, series, gridpts


if __name__ == "__main__":
    main()
