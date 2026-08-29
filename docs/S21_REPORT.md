# S21 Report — Anonymity scrub and standalone data release

## Verdicts (Wave 3, sub-session D — independent, from-scratch audit)

**PAPER: confirmed free of identifying detail**

**DATA RELEASE: confirmed free of identifying detail**

The data-release verdict is the result of two remediation rounds. D's first pass (before
seeing Track A/B's own reports) found the paper clean immediately, but found the
data-release package **not** clean: it carried wave/critic/agent process-fingerprint
language that Track B's own scrub had missed (session-numbering and hardcoded paths were
caught; a wave-based, adversarially-reviewed narrative voice was not). That was fixed and
D re-audited the rebuilt archive from scratch a second time, which surfaced one further
low-severity, non-identity residual ("the brief," a dangling reference to an unshipped
internal spec document, same fingerprint category). That was fixed too, and D's final,
independently re-verified verdict is the one above. Full detail in
`research/S21/D-identity-critic.json`.

## The paper

**Page count:** 17 pages total. Body ends on page 4 (Limitations); References begins as
the first content on page 5. Re-verified by the opened-page method (rendered page images,
not just text extraction) both immediately after the author-block edit and again after
the availability-statement edit. Unchanged from the S19 Wave 8 baseline — blanking two
short header fields did not move a line, as expected.

**Every placeholder field and its exact current text**, so the operator knows precisely
what to fill in before submission:

| Field | Location | Current text |
|---|---|---|
| Author name | `paper/main.tex:394`, `\paperauthor` macro | `[AUTHOR NAME]` |
| Author email | `paper/main.tex:464`, inside `\author{}` | `[AUTHOR EMAIL]` |
| Affiliation | `paper/main.tex:463` | `Independent Researcher` — **not new**, an existing operator-input placeholder from `docs/OPEN_QUESTIONS.md` Q11, left as-is per this session's brief (operator's own call whether to mark it further) |
| Repository URL | `paper/main.tex:620` | `https://[REPOSITORY LINK - INSERTED BY AUTHOR PRIOR TO SUBMISSION]` — unchanged, still a placeholder |

PDF metadata (`pdfinfo`) confirms `Author: [AUTHOR NAME]`; `Title` is untouched (not
identifying, per the brief). The `\paperauthor` → `\hypersetup{pdfauthor=}` single-source
wiring built in S5 held: one macro edit fixed both the visible page and the PDF Info
dictionary with no drift.

The availability statement ("Code and data" section) was reworded — it used to end "...
and this project's audit trail are at [URL]," a soft self-referential leak that was also
simply inaccurate against what the data release ships. It now reads: "The simulator, its
frozen configuration, the `results/` files behind every figure and table, and the scripts
that generate them are at [URL]" — matching the shipped package exactly.

Nothing else in the paper changed. All mathematical content (the four-boundary theorem,
both proof directions, the closed form, both degenerate cases, every Limitations hedge,
the checklist content, the corrected martingale example) is untouched, confirmed by
diffing the full `paper/` tree from immediately before this session's first commit to now.

## The data release

**Archive:** `~/Desktop/conformal-boundary-data-release.zip`
**SHA-256:** `7557a8ff722d9a57e549e213596077153747272ffa6b94f492bb432743ff922c`
**Contents (14 files):**

```
LICENSE
README.md
src/forfeit.py
src/test_forfeit.py
src/boundary_stress.py
src/make_figure1.py
results/forfeit-20260820T061553Z-83747c45.json
results/forfeit-20260820T061751Z-83747c45.json
results/forfeit-20260820T063045Z-83747c45.json
results/forfeit-20260820T063132Z-83747c45.json
results/forfeit-variations-20260820T101445Z.json
results/boundary-stress-20260822T103716Z-cd208b98.json
figures/figure1_boundary.pdf
figures/figure3_settings.pdf
```

No `.git`, no hidden files, no OS metadata (`.DS_Store`, `__MACOSX`, etc.) anywhere in the
package — checked before every zip build and again after extracting the final archive
fresh. The archive is named after the paper's technical subject, not the working repo's
own name, to avoid an unnecessary link between the two.

**LICENSE:** MIT (this project's established choice). Copyright line reads:

```
Copyright (c) 2026 [COPYRIGHT HOLDER NAME — INSERT PRIOR TO RELEASE]
```

— an explicit placeholder, not the real name and not blank. Needs the operator's name
before actual release, same as the paper's author block.

**Smoke test — reproduced in genuine isolation.** The fully scrubbed package was copied to
a fresh location with no path back to the working repo or the staging directory, and the
README's own instructions were run from there:

- Test suite: **12/12 passed**
- `boundary_stress.py validate`: **19/19 checks passed** (transcribed sweep vs.
  `forfeit.py`'s own committed numbers)
- Figures: both regenerate **byte-identical** to the shipped PDFs
- The τ=1.5 dead-band failure (`deadband_tau1.5`, adversarial regime, T=1,000,000):
  miscoverage reproduces at exactly **1.0**
- The w=0.999 partial-adjustment excursion at q̂≡−b/2 (`Config(scorecaster_const=-1.0)` +
  `ema_w0.999` arm): miscoverage reproduces at exactly **1.0**

No import or file reference in any script reached outside the isolated copy.

## What this session found and fixed along the way

- **Paper:** blanked `\paperauthor` and the author-block email literal to explicit
  placeholders (single commit `f314e01`); reworded the availability statement to drop a
  soft self-referential leak and match what the data release actually ships (commit
  `613baf3`).
- **Data release, round 1:** removed session-numbering and dangling internal-doc
  references (`S2`/`S3`/`S5`/`S6`, `research/S*/...`, `audit/RECONSTRUCTION_SPEC.md`,
  `docs/GATES.md`, `docs/OUTSTANDING.md`) and a hardcoded machine-specific Python path,
  from `src/forfeit.py`, `src/make_figure1.py`, and `src/test_forfeit.py`.
- **Data release, round 2** (after D's first independent audit): removed wave/critic/agent
  process-narration ("WAVE 5," "the adversarial critic (F1)," "an agent's scratch
  directory," "either critic said") that round 1's sweep had missed.
- **Data release, round 3** (after D's second independent audit): removed ~20 dangling
  references to "the brief" (an unshipped internal specification document), the last
  residual D's own re-check surfaced.
- Every fix landed in a comment, docstring, or metadata/string field — the escalation rule
  (stop and report rather than edit if a leak sits inside actual numeric result data) was
  never triggered, confirmed independently by both D and E.
- Two out-of-scope, untracked directories were found sitting in the working tree at
  session start and were **not** touched, per the investigate-before-deleting rule:
  `build/turnover-blind-e-values-2026/` (an untracked, older Overleaf-package duplicate
  carrying a `.DS_Store` and a compiled PDF with the real author name) and
  `Formatting_Instructions_For_NeurIPS_2026/` (a generic, non-identifying template copy).
  Neither is part of the paper or the data release; flagging them here so the operator can
  decide whether to clean them up before this repository is shared with anyone.

## Instruction compliance (sub-session E)

All six checked items passed: placeholders (not blank/not "Anonymous"), template option
unchanged, escalation rule correctly not triggered, availability statement reconciled,
frozen content untouched, no gate recorded as signed. Full detail in
`research/S21/E-instruction-check.json`.

## Status

No gate is recorded as signed by this session. This is ready for the operator's own look.
**The paper still needs the real name restored in Overleaf as the very last step before
actual submission — not before.**
