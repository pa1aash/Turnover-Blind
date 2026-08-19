# C1 reproduction attempt

**Verdict: NOT REPRODUCIBLE. Every cell of the C1 table is NOT-EMITTED.**

The planning document states, in its header table, that *"the central experiment is
already done"*, and attributes the C1 table to a named file:

> ## The result (already computed — `scratchpad/confloor5.py`)

and again in its closing section:

> `scratchpad/confloor5.py` already produces the C1 table.

**That file does not exist in this repository, and no file matching it — by name, by
output, or by content signature — exists anywhere on the operator's machine.** The
plan's central claim about its own state is therefore unsupported by the repository
contents. This is the single most consequential finding of the G0 session.

This document takes branch **B2-ABSENT** of the audit brief. No simulator was written
to fill the gap; `audit/RECONSTRUCTION_SPEC.md` records what a rebuild would need
instead.

---

## 1. Search evidence

Every command below was run on 2026-08-19 from the operator's account. Empty output
means no match.

| # | Command | Scope | Result |
|---|---|---|---|
| 1 | `find /Users/palaash -maxdepth 6 -name 'confloor*'` | home tree, 6 levels | no match |
| 2 | `find /Users/palaash -name 'confloor*'` (excluding `Library/Caches`) | whole home tree, unbounded depth | no match |
| 3 | `find /Users/palaash -maxdepth 4 -type d -name 'scratchpad'` | home tree | **no `scratchpad/` directory exists anywhere under the home directory** |
| 4 | `find … -name '*.py' \( -iname '*conformal*' -o -iname '*aci*' -o -iname '*kelly*' -o -iname '*turnover*' \)` | home tree, 7 levels, excluding `site-packages` | 8 hits, all unrelated (hyperbolic-geometry enumeration scripts, a physics eigenvalue check, three linter test fixtures, one `pluggy` internal) |
| 5 | `grep -rIl 'confloor' ~/Desktop ~/Downloads ~/Documents` | all text files in the three working trees | no match |
| 6 | `grep -rIl '0\.8993' ~/Desktop ~/Downloads ~/Documents` | all text files in the three working trees | no match |
| 7 | `find <session-scratch-root> -maxdepth 6 -name '*.py'` | every retained prior-session scratch directory on the machine (49 of them) | 40 hits, none a conformal simulator; the four prior scratch directories belonging to this project are empty |
| 8 | `grep -rIl 'confloor' <transcript-store>` | all retained session transcripts | one hit: the transcript of **this** session, which contains the string only because the planning document does |
| 9 | `grep -rIli 'turnover.blind' <transcript-store>` | all retained session transcripts | one hit: this session only |
| 10 | `grep -rIl '0\.8993' <transcript-store>` | all retained session transcripts | this session, plus unrelated hits in an MBO project (a Bayesian-optimisation benchmark table) and in one fetched research note; neither is the C1 table |

`<session-scratch-root>` and `<transcript-store>` are the per-project scratch and
transcript directories maintained by the local agent tooling, under the system
temporary directory and the home directory respectively. They are named indirectly
here so that this file satisfies `tools/check_hygiene.sh`; the operator can resolve
both paths locally.

### What the evidence does and does not establish

**Establishes:** the artefact named in the plan is not recoverable in this
environment. Neither the code, nor its stdout, nor any serialised form of its output,
nor the distinctive numbers it is said to have produced, exist on this machine. The
directory `scratchpad/` that the plan's path presupposes does not exist at all.

**Does not establish:** that the experiment was never run. The planning document
itself was authored outside any session retained on this machine — no transcript
other than the current one mentions the project name or the document's title — so the
work may have been done on other hardware or in an environment whose state was not
preserved. The audit cannot distinguish "run elsewhere and lost" from "never run".

**The consequence is identical either way.** Every number in the C1 table is, from
this repository's standpoint, an unverified assertion. The project cannot cite,
defend, or build on any of them until the simulator is rebuilt and re-run.

---

## 2. Cell-by-cell status

Marking per the audit brief: REPRODUCED / MISMATCH / NOT-EMITTED. Nothing was
emitted, so every row is NOT-EMITTED. Column `internal consistency` records whether
the plan's own numbers agree with each other — the only check available without the
code, and the only positive information in this table.

### 2.1 The six gamma rows, at 15 bps

| γ | quantity | plan value | status | internal consistency |
|---|---|---|---|---|
| 0.000 | coverage | 0.8926 | NOT-EMITTED | — |
| 0.000 | net annual log growth | +0.0136 | NOT-EMITTED | — |
| 0.000 | paired diff vs γ=0.005 | +0.0002 ± 0.0003 | NOT-EMITTED | consistent: 0.0136 − 0.0134 = +0.0002 |
| 0.000 | annual turnover | 3.2 | NOT-EMITTED | — |
| 0.005 | coverage | 0.8993 | NOT-EMITTED | — |
| 0.005 | net annual log growth | +0.0134 | NOT-EMITTED | — |
| 0.005 | paired diff | reference arm | NOT-EMITTED | — |
| 0.005 | annual turnover | 3.4 | NOT-EMITTED | — |
| 0.020 | coverage | 0.8998 | NOT-EMITTED | — |
| 0.020 | net annual log growth | +0.0123 | NOT-EMITTED | — |
| 0.020 | paired diff | −0.0010 ± 0.0004 | NOT-EMITTED | consistent to rounding: 0.0123 − 0.0134 = −0.0011 |
| 0.020 | annual turnover | 4.4 | NOT-EMITTED | — |
| 0.050 | coverage | 0.8999 | NOT-EMITTED | — |
| 0.050 | net annual log growth | +0.0090 | NOT-EMITTED | — |
| 0.050 | paired diff | −0.0043 ± 0.0008 | NOT-EMITTED | consistent to rounding: 0.0090 − 0.0134 = −0.0044 |
| 0.050 | annual turnover | 6.9 | NOT-EMITTED | — |
| 0.150 | coverage | 0.8999 | NOT-EMITTED | — |
| 0.150 | net annual log growth | −0.0050 | NOT-EMITTED | — |
| 0.150 | paired diff | −0.0184 ± 0.0019 | NOT-EMITTED | consistent: −0.0050 − 0.0134 = −0.0184 |
| 0.150 | annual turnover | 15.8 | NOT-EMITTED | — |
| 0.400 | coverage | 0.9000 | NOT-EMITTED | — |
| 0.400 | net annual log growth | −0.0303 | NOT-EMITTED | — |
| 0.400 | paired diff | −0.0437 ± 0.0032 | NOT-EMITTED | consistent: −0.0303 − 0.0134 = −0.0437 |
| 0.400 | annual turnover | 31.0 | NOT-EMITTED | — |

The paired-difference column is arithmetically consistent with the growth column in
all five comparisons, to the precision displayed. That is weak evidence that the
table was transcribed from a real computation rather than assembled by hand, but it
is entirely compatible with a table constructed to be self-consistent. It is not
evidence that the simulation exists.

### 2.2 The seven named claims

| Claim | Plan text | Status | Note |
|---|---|---|---|
| Coverage pinned at 0.90 for every γ ≥ 0.005 | "Coverage is pinned at the 0.90 target for every γ ≥ 0.005" | **NOT-EMITTED** | The tabulated values 0.8993, 0.8998, 0.8999, 0.8999, 0.9000 do lie within 0.0007 of 0.90, so the wording is fair *given* the table. Note the γ=0.005 arm is 0.8993, a 0.07pp shortfall, and γ=0 is 0.8926, a 0.74pp shortfall — the dissociation is between γ≥0.005 arms, not between all six. |
| 4.4-point growth swing | "net growth swings 4.4 points" | **NOT-EMITTED** | Consistent: 0.0437 → 4.37 points from the γ=0.005 reference; 0.0439 → 4.39 from γ=0. |
| 13.7 standard errors | "13.7 standard errors" | **NOT-EMITTED** | Consistent: 0.0437 / 0.0032 = 13.66. |
| 0 bps arm: all diffs within 1 SE | "at 0 bps the effect vanishes entirely (all diffs within 1 SE)" | **NOT-EMITTED** | **No 0 bps table appears anywhere in the plan.** This is an assertion about a table that is not shown. It is one of the two load-bearing zero-cost results and it has no displayed numbers at all. |
| 5 bps arm intermediate | "at 5 bps it is intermediate" | **NOT-EMITTED** | **No 5 bps table appears anywhere in the plan.** Same defect. |
| Monotonicity in the cost rate | "The effect is monotone in the cost rate" | **NOT-EMITTED** | Asserted over three cost levels of which only one is tabulated. Three points is in any case a weak basis for a monotonicity claim; the paper will need a denser cost grid. |
| 330× rise in Var(Δq) at 0 bps | "Var(Δq) rises 330× across the γ sweep while net growth stays flat within 1 SE" | **NOT-EMITTED** | **No variance table appears anywhere in the plan.** This number is the entire evidentiary basis for the falsified-variance-hypothesis finding, which the plan calls "the difference between an over-determined observation and an identified mechanism". It rests on one unshown figure. |

### 2.3 Runtime

| Quantity | Plan value | Status |
|---|---|---|
| Wall-clock runtime of the core experiment | "~90 seconds", "CPU-only" | **NOT-EMITTED** — nothing was run, so no wall-clock time was measured. The figure is plausible for 6 γ arms × 60 paths of a scalar recursion, but it is unverified. |

---

## 3. Findings

**F-B2-1 (blocking).** The plan's self-assessment — "the central experiment is already
done", "Est. effort 2 weeks", "Day-1 starting point: add the dead-band arm, it is ~15
lines" — is unsupported. The realistic day-1 task is to build the simulator from
scratch against a specification that does not yet exist, not to add fifteen lines to
one that does. Every schedule estimate in the planning document is downstream of this
and should be treated as unreliable until the simulator exists and reproduces the
table.

**F-B2-2 (blocking).** The three most rhetorically load-bearing results in the
document — the 0 bps null, the 5 bps intermediate case, and the 330× variance rise —
are stated without any table, at any cost level, anywhere in the document. Even if
`confloor5.py` were recovered tomorrow, there would be no recorded output to check
those three claims against. They must be re-derived, not re-found.

**F-B2-3.** The C1 table's arithmetic is internally consistent, which is worth
recording as a point in the plan's favour and as a target: a correct rebuild should
reproduce this table, and failure to do so is then informative about the
reconstruction rather than about the table.

**F-B2-4.** The reported paired standard errors imply a per-path standard deviation
of the growth difference of roughly 0.0023 at γ=0.005→0.020 and 0.025 at
γ=0.005→0.400, over 60 paths. Any rebuild that produces standard errors of a
materially different magnitude has a different data-generating process from the one
that produced this table, regardless of whether the point estimates agree.

---

## 4. What would close this

1. Recover `confloor5.py` from wherever it was actually run, or establish that it
   cannot be recovered. This is an operator action; see `docs/OPEN_QUESTIONS.md`.
2. Failing recovery, build the simulator to a frozen specification. The
   underdetermined choices are enumerated in `audit/RECONSTRUCTION_SPEC.md`; several
   of them change the answer, so the specification must be decided by the operator
   and pre-registered before the sweep is run, not tuned until the table matches.
3. Emit, for every run, a JSON record in `results/` carrying the full parameter set,
   the seed policy, the git commit, the wall-clock time and the raw per-path
   quantities — not only the aggregated table. The absence of such a record is the
   reason this audit has nothing to check.
