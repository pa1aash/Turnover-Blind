# Operator decisions

Policy decisions the operator made **mid-session**, which changed what a session was permitted
to do rather than merely what it did. They are recorded here because the places they would
otherwise live are not durable: `research/` is gitignored (`.gitignore:7`), so a clone of this
repository does not carry it, and a conversation transcript is not part of the repository at
all. A commit message records the *outcome* of a decision; this file records the *decision* —
what was asked, what was granted, how wide the grant was, and what it overrode.

**This file is a record, not an authority.** It does not sign a gate, and nothing written here
discharges any operator sign-off `docs/GATES.md` requires. Entries are written by the automated
session that acted on the decision, from that session's own conversation, and say so.

**Why this file exists.** S15 sub-session I3 (instruction critic) checked S15 against its own
governing brief and found one process gap: the session's mid-session operator authorisations —
including an explicit override of the standing protected-content rule — existed only in
gitignored JSON and, partially, in one commit message. I3's recommendation was a dated,
git-tracked record independent of both. This is it. Created by S15 sub-session J, 2026-08-25.

---

## 1. The page budget is a whole-document limit — 2026-08-24/25 (S15)

**Decision.** TS-LIMITS' stated 4–7 pages is a limit on the **whole document, body and
appendices together**. There is **no separate appendix budget** and no appendix exclusion.

**Who decided, and why it was theirs to decide.** The operator, explicitly. TS-LIMITS' call, as
re-verified from source by S15 wave 0 (`research/S15/A-venue-verification.json`, and see
`docs/VENUE.md`), states no appendix exclusion. Silence in a call is an interpretation question,
not a fact question, so it is not something an automated session may settle for itself.

**What it changed.** Under the earlier reading the paper was comfortable; under this one it was
2.72 pages over a hard ceiling. Every S15 decision downstream of this one — the restructuring,
the de-compression, and then the cut in §2 below — follows from it.

**Recorded at the time in.** `research/S15/D-restructuring.json` (gitignored), as "Operator
decision".

---

## 2. Authorisation to cut protected content to close the budget — 2026-08-25 (S15)

**Standing rule this overrode.** S15's brief protected seven categories of content — the four
boundary definitions, both proof directions, the closed-form statement, both degenerate cases,
every Limitations hedge, the open-band disclosure, and R3a — under a "restore, don't cut" rule.
The session could compress, not delete.

**Decision, in the two steps it was actually made in.**

1. The operator first authorised **cutting or compressing Appendix B**, the promoted e-value
   section (`paper/sections/evalue.tex`), with an instruction to compress before deleting.
2. The orchestrator then measured that Appendix B alone could not close the gap and put that
   arithmetic back to the operator. The operator **then** authorised also cutting **Appendix A's
   five prose paragraphs**.

**Scope of the grant.** Exactly those two targets and nothing else. It was narrow and explicit,
not a general licence to cut. Everything else in the seven protected categories stayed
untouchable, and stayed untouched.

**Executed in.** S15 sub-session D2, commit `72cc82f`. `sections/evalue.tex` deleted in full
(its load-bearing sentences and surviving hedges folded into the body paragraph "The boundary
read as a bet." in `sections/forfeit.tex`); Appendix A's five prose paragraphs deleted, with
Table 2 and its caption kept whole. `sections/limitations.tex` and `sections/setup.tex` were
verified byte-identical across the cut. Recovery: 2.95 pages, 12 pages to 9, counted content
9.72 → 6.77.

**Independently verified after the fact.** S15 wave 3's adversarial critic (I1) rebuilt both
venue options from source, confirmed all seven protected categories survive unweakened,
confirmed no unauthorised cut, and confirmed the page figures to within 0.001pp. It also found
three defects the cut left behind — an orphaned constant, a dropped pre-registration caveat, and
a free parameter carried into the body without its admissible range — which S15 sub-session J
repaired (see §4).

**Recorded at the time in.** `research/S15/D2-budget-closure.json` (gitignored), and in
`72cc82f`'s commit message — which states the final scope of the authorisation correctly but not
the two-step negotiation above.

---

## 3. The repository will be made private before submission — 2026-08-25 (S15)

**The finding.** S15 wave 3's dedicated identity-leak critic (I2) confirmed the compiled
double-blind PDF is clean on every surface it checked, and then found that this does not settle
anonymity. This working tree's `origin` remote is a **public** GitHub repository whose published
branch carries (a) a **single-blind** build of `paper/main.pdf` with the real name, affiliation
and email on page 1 and in `/Author`, under the same title and abstract as the submission,
(b) `paper/main.tex` and the section files with the name and email in plain text, and (c)
session reports in `docs/` sharing hundreds of verbatim eight-word runs with the submitted
paper's own prose. Every commit on that branch carries the real name and email. A reviewer who
searches one distinctive sentence from the submission reaches it in one step.

**Decision.** The operator's explicit decision is to **make the repository private before
submission**.

**Who acts.** The **operator**, themselves, outside any session. No session executed this, and
this session did not attempt to. Note for whoever does it: making the repository private is
sufficient; deleting files from `HEAD` would not be, because they remain in git history.

**Status.** Open action on the operator at the time of writing. It is not verified here and
must not be assumed done.

**Recorded at the time in.** `research/S15/I2-identity-critic-findings.json` (gitignored),
finding F0. That file deliberately does not contain the operator's real name, email or handle;
they are recoverable locally with `git remote -v` and `git log -1 --format='%an %ae'`.

---

## 4. Authorisation for the wave-3 patch fixes — 2026-08-25 (S15)

**Decision.** The operator's wave-3 patch brief directed S15 sub-session J to apply I1's three
substantive findings against the post-cut paper (the orphaned `0.63/(1-w)`; the surviving
"convicts the τ = 1.5 arm … at the 5% level" claim whose pre-registration caveat had been cut;
and λ carried into the body without the range that makes the sentence around it true), and
delegated to J the judgement call on I1's remaining notes. Two clauses in the same brief matter
as much as the grant: **prefer the cheapest correct resolution, and rebuild and measure after
every single fix**, because the margin is quantised at whole pages.

**Why it needed to be an operator decision.** One of the three fixes rewords a **Limitations
hedge**, which the standing rule protects. The brief names that fix explicitly.

**Scope.** The three fixes, the λ-collision call, the stale page figure in the shipped Overleaf
package's README, and this file. Explicitly **not** authorised: reopening the venue decision, or
any further compression of the document.

**Executed in.** S15 sub-session J. Log: `research/S15/patch-log.json` (gitignored). Both venue
options rebuilt and re-measured after every fix; final state 9 pages under both, counted content
6.767 (dbl) / 6.764 (sgl), inside the 7-page ceiling.
