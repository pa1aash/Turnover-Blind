# S14 report — hedge-preserving compression attempted, insufficient, reverted in full

**Session S14, 2026-08-24.** Working folder `~/Desktop/Turnover-Blind`, branch `main`. Wave 0
preflight, six parallel/serial sub-sessions (A–F), one conditional sub-session (G), one serial
integration-and-revert sub-session (H), two mandatory parallel critics (I1/I2). Four commits
this session (`6735732`, `8da631c`, `e733075`, and this report's commit), not yet pushed as of
writing this section.

---

## The single most important fact: this session did not close the gap, and reverted to S13's state

**No.** This session did not close the 4-page gap. The combined real, measured savings from
every lever this session opened — including the previously-forbidden lever of tightening
Limitations' own wording — were **27pt against a 208pt shortfall**. That is not a close miss.
Per this session's own pre-declared all-or-nothing rule, every content change from Wave 1 and
Wave 2 (sub-sessions A through G) was reverted before any final commit. **The paper, at this
report's HEAD, is byte-for-byte identical to session S13's ending state** — confirmed by an
empty `git diff 3ad0f8c HEAD` across the entire repository, independently re-derived by an
adversarial critic who also md5'd every source file and rebuilt the PDF from scratch.

Limitations sits entirely on page 5, unsplit — the same clean break S13 ended on. Nothing about
the paper's content, wording, typography, or layout changed as a result of this session.

---

## The baseline had drifted, and was re-measured before anything else happened

S13's adversarial critic measured a 202pt shortfall. This session's own preflight (W0.2)
re-measured it by the identical binary-search method — a temporary, reversible
`\vspace{-Npt}` inserted after `\maketitle`, rebuilt with 4 pdflatex passes + bibtex, reverted
before any edit — and found the real shortfall had drifted to **208pt** (a 6pt increase, source
not investigated further, not load-bearing to this session's outcome). The session's own target
was adjusted proportionally: at least 236pt of real savings (208pt to close the gap, plus the
same ~28pt margin S13's brief specified against its own 202pt reading), so that the paper would
not sit exactly at the boundary, fragile to any future edit.

---

## Savings by sub-session, individually, not just the aggregate

| Sub-session | Scope | Model | Self-reported savings | Real contribution to the page break |
|---|---|---|---|---|
| A | Limitations wording, hedge-preserving | Opus | 63 chars / 7 edits, ~1 typeset line (11pt) | Included in Wave 1's 27pt total, not separable by sub-session once merged |
| B | Section 3 connective prose only | Opus | 97 chars / 6 edits | ″ |
| C | Introduction remaining prose | Sonnet | 5 chars / 1 edit (near-zero; six prior sessions had already exhausted this file) | ″ |
| D | Setup (Section 2) prose | Sonnet | 38 chars / 3 edits (near-zero; precise definitions leave little safe slack) | ″ |
| E | Micro-typography sweep | Sonnet | 27pt, directly measured (caption skip, display-equation skip; `\parskip` attempted and reverted after it visibly broke the title/abstract block) | **27pt — this was effectively the entirety of Wave 1's real yield** |
| F | Table 1 (body table) compactness | Sonnet | 2.71pt (arraystretch + redundant header trim); row reduction considered and correctly declined (no overflow to justify it) | Below the threshold that shifts any page break |
| **Wave 1 total, measured by rebuild** | | | (self-reports summed to roughly 60–100pt-equivalent) | **27pt, real** |
| G | Figure 1 (Placement A/B schematic) compaction | Sonnet | Referential-integrity check confirmed Placement B is referenced substantively in Section 3's own prose, so removal was correctly ruled out; a safe compact rendering was applied instead (caption skip, trailing vspace) | **0pt** — figure height was never the binding constraint; float packing quantizes the break regardless, exactly as a prior session's own comment in `setup.tex` already warned |
| **Session total, measured by rebuild** | | | | **27pt against a 208pt gap (target ≥236pt)** |

The gap between self-reported character counts and the real, rebuilt-and-measured number is the
headline lesson of this session: scattered sub-line trims across four files rarely cross the
full-line threshold that actually moves a LaTeX page break. Only Sub-session E's direct
typographic-parameter adjustment — a real, uniform, legitimate change to caption and
display-equation skip values, the same class of edit as the pre-existing float-separation
override from S5/S10 — survived contact with the real layout.

---

## Hedge-by-hedge comparison (I1's adversarial check)

Because Sub-session A's edits to `paper/sections/limitations.tex` were fully reverted along with
everything else, the file at this report's HEAD is byte-identical to S13's version — confirmed
by `git diff 3ad0f8c HEAD -- paper/sections/limitations.tex` returning empty and independently by
md5 checksum. There is no edited text to compare against the original, so every hedge below
survives by identity, not by judgment call:

1. **Sub-class scope restriction** — "a constant scorecaster and a saturator attaining its
   extremes at the condition-(4) radius, which is every setting run here" — unchanged.
2. **Open time-varying band (touchpoint 1)** — "a genuinely time-varying $\hat q$ leaves the band
   $\sigma^+ < \tau \le \tau^{\star+}$ open in neither direction" — unchanged.
3. **Saturator-specific fitted constant** — "$0.63/(1-w)$ is specific to the saturator's level,
   which condition (4) bounds only from below" — unchanged.
4. **Weak O(1/log T) rate under the tangent integrator** — "the certified gap $(c h(T)+1)/T$
   decays as $O(1/\log T)$ rather than $O(1/T)$" — unchanged.
5. **Adversary-specific absolute failure** — "the failure is total only against the adversary...
   Under i.i.d. scores it returns $0.249376$ at $T = 10^6$" — unchanged.
6. **Harness-rebuilt-against-seen-numbers disclosure** — "which carries less weight than a rerun
   done without sight of them" — unchanged.
7. **Placement B conceded, not tested** — unchanged.
8. **One-seed i.i.d. check + null-scorecaster-only bracket** — "used one seed ($20260820$, $T =
   10^6$)... only its null-scorecaster edge is bracketed; the others are one-sided" — unchanged.
9. **Open band, future work (touchpoint 2)** — "coverage in $\sigma^+ < \tau \le \tau^{\star+}$ is
   neither proved nor falsified... closing that band is future work" — unchanged.

**All ten hedge claims (nine numbered clusters, #2/#9 being one concession stated twice) survive
at identical strength, trivially, because the file was never actually shipped edited.** The draft
edits Sub-session A produced (which I1 also reviewed, out of an abundance of caution, in the
recovered conversation record) would themselves have preserved every hedge under the same test —
but that draft never reached HEAD, so it is not what this paper currently contains, and is not
what a reader of the current PDF will ever see.

---

## Sub-session G, in detail

Wave 1 alone (27pt) fell far short of the ≥236pt target, correctly triggering Sub-session G
(Figure 1 redesign) rather than skipping it. G's mandatory referential-integrity check found
Placement B named and explained in Section 3's own prose (`forfeit.tex`: "Placement B keeps
$\{\hat q_t\}$ inside the admissible radius, so Theorem 1 carries it already..."), independent of
the figure — so panel removal was correctly ruled unsafe. G instead attempted a more compact
joint rendering (tighter caption skip, smaller trailing vspace), measured 0pt of real savings by
the same binary-search method, tried more aggressive geometry, found a genuine legibility defect
(a panel title colliding with its bounding box) with zero compensating benefit, and reverted that
attempt — keeping only the safe, zero-risk version. This confirms a warning already on record in
`setup.tex`'s own S5-wave-2 comment: float packing around the body's tables quantizes the page
break, and the figure's own height was never the actual constraint.

---

## What the two critics found

**I1 (adversarial, Opus):** independently re-verified the revert from scratch — did not trust
any report handed to it. Confirmed `git diff 3ad0f8c HEAD` empty across the whole repository
(not just `paper/`), md5-matched every section file against S13's committed blobs, confirmed both
of this session's intermediate commits are genuinely empty-diff, independently rebuilt the PDF
(4 fresh pdflatex passes + bibtex) and confirmed pixel-identical output against the tracked PDF
(0 of 13 rendered pages differ visually), and confirmed the clean-break signature directly: page
4 full to the same body baseline as every other full page, page 5 opening with the entire
Limitations section unsplit before References begins. **Zero findings at any severity.** Its one
substantive note, not a defect: the underlying page-vertical-space gap is now confirmed, across
two independent sessions, to have no further compressible slack in the prose under a
meaning-preserving test — a future session revisiting this needs a structural lever (further
appendix relocation), not more wording tightening.

**I2 (instruction, Sonnet):** confirmed Sub-session G was correctly triggered by a real,
measured shortfall rather than skipped or run gratuitously; confirmed Sub-session H applied the
all-or-nothing rule correctly, independently re-verifying the empty diff rather than trusting the
checkpoint's own prose; confirmed protected mathematical content, frozen fields, and gate-signing
status all pass (the first trivially, given the empty diff). One flagged, defensible process
deviation: sub-sessions A through G never committed individually as the brief's letter specified,
because several ran in parallel via the Agent tool against one shared working tree, and
per-sub-agent `git commit` calls would have raced — a risk Sub-session G's own near-miss
`git stash`/`checkout` collision with Sub-session E's uncommitted edits demonstrated was real
(recovered cleanly via a saved patch before any data was lost, independently confirmed by direct
diff inspection rather than trusting G's own account). Commits were centralized in the
orchestrator instead. Given the all-or-nothing outcome, nothing from A–G survives to commit
regardless, so this cost nothing in practice, but it is recorded as a process gap rather than
waved through as full compliance. Full findings: `research/S14/patch-log.json` (gitignored, not
committed, consistent with every other session's audit-trail convention).

---

## Is this paper ready for the operator's final read before submission?

**No — for the same reason S13 ended on: the body does not fit the venue's 4-page ceiling, and
this session has now established, with a second independent measurement and a second exhausted
compression attempt, that wording-level and typographic tightening cannot close a shortfall of
this size while preserving every hedge and every piece of protected mathematical content at full
strength.** Two paths remain, neither decided by this session, both already named in S13's report
and both still open: find a genuinely new class of authorized cut (a scope this session was not
given — the wording lever was the last one available and it returned 27pt), or switch to
TS-LIMITS, which allows 4–7 body pages and comfortably fits the paper's current length as-is (a
two-line change in `paper/main.tex`, already marked `[OPERATOR INPUT]`, untouched by this
session). The paper's content, at HEAD, is otherwise in the same state S13 left it: every item
from both adversarial reviews addressed, both critics passing S13's own checks, the Overleaf
package a faithful mirror.

---

## Days remaining before the E-values deadline

**5 days.** Today is 2026-08-24; the E-values deadline is 2026-08-29 23:59 AoE (`docs/GATES.md`,
`docs/OUTSTANDING.md` O20) — unchanged from S13's reading, since this session did not touch the
deadline and no time has passed between the two sessions' dates.
