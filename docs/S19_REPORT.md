# S19 Report

Session date: 2026-08-27. **2 days remain to the E-values deadline** (2026-08-29 23:59 AoE / OpenReview duedate 2026-08-30 13:00 UTC).

## Findings by category

Six parallel Wave-1 audits (sub-sessions B–G) applied the full prose-audit specification's 16 categories across the entire manuscript, main text and appendix. 300 raw findings were produced, then merged and deduplicated (Sub-session H) into 166 distinct, consolidated findings.

| Category | Description | Consolidated findings |
|---|---|---|
| 1 | Rhetorical negation | 37 |
| 2 | Sentences announcing their own significance | 3 |
| 3 | Roadmap / forward-pointer sentences | 10 |
| 4 | Trailing appositive qualifications | 26 |
| 5 | Softening adverbs on binary claims | 22 |
| 6 | "What"-clefts and expletive constructions | 14 |
| 7 | Headers and bold paragraph leads | 18 |
| 8 | Figure and table captions | 7 |
| 9 | Run-on and over-nested sentences | 26 |
| 10 | Aphoristic paragraph endings | 20 |
| 11 | Process-record and internal-code leakage | 3 (one collapsed into a 4-way merge with categories 1/6/7) |
| 12 | Terminology and notation drift | 32 |
| 13 | Numbers and internal consistency | 19 |
| 14 | Structural and framing problems | 14 |
| 15 | Spelling and convention consistency | 11 |
| 16 | Anything else | 19 |
| **Total** | | **166** (34 duplicate merges beyond the raw 166 shown; see below) |

134 raw entries were merged away as duplicates across 52 merge groups (a single sentence often tripped more than one category — e.g. `forfeit.tex:431` was independently flagged by four different sub-sessions under three different categories before being merged into one finding).

## Triage: BIN A / B / C

Sub-session I, the session's risk-management gate, classified all 166 consolidated findings:

- **BIN A (53)** — safe to apply directly: no protected-content contact, no judgment call, no page-length risk.
- **BIN B (52)** — apply with extra care: judgment calls or possible length impact, individually logged for adversarial re-check.
- **BIN C (61)** — do not apply without explicit escalation: touches or borders protected content, or requires rephrasing a hedge/mathematical claim.

All 33 findings with conflicting proposed fixes (from different Wave-1 sub-sessions disagreeing on the right wording) were resolved by Sub-session I with individual reasoning before handoff to Wave 4.

## What was applied

60 fixes were applied across four parallel fix sub-sessions, each owning a distinct, non-overlapping file set:

- **J1** (abstract + Introduction): 18 fixes.
- **J2** (Setup + Section 3, connective prose only): 24 fixes, all six protected mathematical ranges independently verified byte-identical before and after.
- **J3** (Limitations + references): 5 fixes, under a hedge-inventory discipline — every one of Limitations' 13 individual hedges was catalogued before editing and re-verified as claim-, strength-, and scope-identical after.
- **J4** (Appendices, checklist excluded): 13 fixes, including one self-caught-and-reverted citation-merge that rendered with a misattributed locator.

## K3's surgical escalation — triggered, and resolved surgically

After Wave 4 merged, the body had overflowed: two lines of pre-existing body prose spilled onto page 5, ahead of References, breaking the zero-margin page budget. This was **not** treated as an all-or-nothing failure. Both responsible fixes — two BIN B additions to the abstract (`H-163`, `H-055`) — were independently flagged by two different fix sub-sessions during their own isolated checks, then reverted one at a time by the integrator, rebuilding and re-measuring after each: the first revert alone was insufficient, the second restored the clean break. No BIN A fix, no fix outside the body, and none of J3's Limitations work was touched — the gap closed with the minimum possible reversion. 58 of the 60 applied fixes stand.

**One further fix was made after Wave 4/5 closed, prompted by Wave 7's adversarial critic**: `H-165` (removing the identifier "AcMCP" from the Introduction) was locally reasonable but orphaned a downstream sentence two lines later ("Both identifiers... were searched") that depended on it as a backward reference — a cross-sentence dependency no sub-session checked jointly. Reverted; page count unaffected; the Overleaf package was re-synced.

## BIN C: known, explicitly unresolved issues

61 findings remain unresolved by design. The two most important are **not prose defects**:

**SMF-1 — possible sub-class overclaim.** `forfeit.tex:430-431` states "Every setting run here is in that sub-class, so the sharp form applies to all five." Sub-session F's audit argues this may be contradicted by Figure 3's own caption ("$\tau^{\star+}$ unbounded under [the] tangent integrator"): the sub-class hypothesis requires $\Lambda^{\pm}_t = A^{\pm}_t$, which may not hold for the tangent saturator, making the true count four (or three) rather than five. This claim sits inside a W0.3-protected range and is repeated at three further locations (`limitations.tex:163-164`, `forfeit.tex:611-612`, `appendix.tex:264`). **This session deliberately did not attempt to verify or refute the argument** — that requires adversarial mathematical re-verification outside a prose-only charter. Six findings are blocked on this pending operator review.

**SMF-2 — possible Limitations/Table-3 contradiction.** `limitations.tex:199-202`'s hedge cites Table 3's two power-of-two rows as living in an unresolved "open band." Sub-session F argues that against the mirror adversary ($s_t \equiv -b/2$), those same rows print `0.000000` — a **proved failure**, not an open question — so the rows cited as evidence for openness may be the paper's own counterexamples to the sentence as stated. Two candidate repairs exist (scope the claim to one adversary, or drop the pointer) but **both would change what the hedge asserts**, so neither is authorized under this session's charter. Five further findings are blocked pending operator review.

Two smaller, already-diagnosed items from Category 11 (process-leakage) also remain open by design:

- **E-1** (HIGH severity in its own audit): `forfeit.tex:431`'s bold lead, "What was printed before is the failure half," has no valid in-document antecedent — traced via `git log -S` to an autobiographical remnant of this paper's own pre-S9 draft state, not a statement about the literature. It sits inside a protected mathematical range, so it was correctly escalated rather than fixed.
- **E-4** (LOW severity): Appendix B's "a correctly guessed direction" is loosely worded (the mixture martingale's whole point is that no direction needs to be guessed). The proposed fix touches zero numbers, but the triage conservatively routed the entire martingale passage to BIN C rather than exercise the narrower claim-neutral carve-out.

Both are genuine, low-risk candidates for a future session's quick pass, not urgent.

## Final page count

**17 pages total. Body exactly 4 pages, References the first content on page 5** — matches the pre-S19 baseline exactly, confirmed independently four times: by the integrator (Sub-session K), by the Overleaf package's isolated compile (SHA-256-identical rendered text to the repo build), by the adversarial critic's own from-scratch rebuild, and again after the post-Wave-7 AcMCP fix.

## The five highest-leverage changes (per the prose-audit specification's own closing instruction)

Sub-session G's mandatory whole-manuscript triage note, produced from a full read across all 16 categories. **All five are structural/framing recommendations outside S19's prose-only charter** — they were not applied this session and are recorded here as forward guidance for a future session, per the specification's own instruction to name them regardless of whether they're actioned immediately:

1. **Give the paper a landing** — a two-sentence recommendation at the end of Limitations, so the body's last words tell a reader what to do rather than what wasn't swept. ~30 min.
2. **Fix the abstract in one pass** — name the two-sided theorem it currently omits, add the anytime-valid clause the venue nearly requires, clear four sentence-level defects. ~90 min.
3. **Buy the lines that pay for 1 and 2** — delete two claim-free passages (setup.tex's travel paragraph, the Introduction's restated opening paragraph), re-homing their unique content. ~75 min. (Enabling change — nothing above is affordable without it.)
4. **Reorder Section 3** to open on the theorem rather than the rate forfeit it later distances itself from, and rescope the Introduction's "is tight" head to "binds." ~60 min.
5. **Mechanical convention sweep** — spelling, serial commas, citation-locator formats, one stray heading. Under +10 characters net, zero page-geometry risk. ~40 min.

## Protected content: confirmed survived unchanged

Per Sub-session M1's independent adversarial review (not the applying sub-sessions' own self-reports): all six W0.3-protected `forfeit.tex` ranges (the theorem statement, both proof directions, the closed form, both degenerate cases) are byte-identical to the pre-S19 state at identical line numbers. `paper/checklist.tex` and the corrected martingale passage (`appendix.tex:432-457`) are byte-identical, full-range diffs empty. All 13 individual Limitations hedges were independently re-verified as claim-, strength-, and scope-identical (M1 rebuilt its own hedge inventory from the pre-S19 file rather than trusting Sub-session J3's). The author block, repository-URL placeholder, and venue switch are unchanged. M1 additionally read all 24 of Sub-session B's "keep this negation" judgment calls (not a sample) and all 67 fixes actually applied across J1–J4 (not a sample), and found zero weakened, narrowed, or vaguer claims — one real cross-sentence defect (the AcMCP case, above), already fixed.

## Is this paper ready for submission?

**Yes, ready for the operator's own final read and submission to E-values**, with one qualification that did not exist before this session: **the two substantive mathematical flags (SMF-1, SMF-2) should be looked at before that final read**, not because either is confirmed to be a real defect — this session's charter explicitly did not authorize determining that — but because both are plausible enough, and consequential enough if real (one touches the paper's own headline "sharp form applies to all five" scope claim; the other touches a Limitations hedge against the paper's own printed data), that they warrant five minutes of direct arithmetic before this paper is called finished. The affiliation line and repository URL remain the operator's own long-standing placeholders, unrelated to this session. Everything else this session was scoped to do — an exhaustive presentation-only pass across all 16 categories, applied and adversarially re-verified — is done, and the page budget holds exactly at 4 body pages with a clean References break.
