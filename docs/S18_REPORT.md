# S18 Report

Session date: 2026-08-27. **2 days remain to the E-values deadline** (2026-08-29 23:59 AoE / OpenReview duedate 2026-08-30 13:00 UTC).

## Checklist determination

**A NeurIPS Paper Checklist is required, and one is now included.** This revises the conclusion of a prior session (recorded in commit b4ecb02), which read the E-values CFP's silence on "checklist" as a waiver. That inference didn't check whether the template's own requirement was track-scoped — it isn't.

Evidence, verified from primary sources and independently re-verified by Sub-session F1's adversarial critic:
- The official template's `checklist.tex` states, unconditionally: *"Do not remove the checklist: The papers not including the checklist will be desk rejected."* This sentence contains **zero `\if` conditionals** and no track-scoping language.
- `neurips_2026.tex` (the master document shared by all 7 submission tracks, including this paper's `sglblindworkshop` option) `\input`s `checklist.tex` unconditionally, immediately before `\end{document}`, wrapped in no `\if@...` guard.
- The E-values CFP, fetched fresh this session, is genuinely silent on "checklist" — but silence is not a waiver when the template's own requirement is track-independent.

A completed checklist (16 questions, answered honestly against this paper's actual content — not generic boilerplate) is now wired into `paper/main.tex` via `\input{checklist}`, placed after references and the appendix per the template's own placement rule. **It costs nothing against the 4-page body ceiling** — the template states explicitly that the checklist "does NOT count towards the page limit," and this was confirmed empirically, not just assumed: the body remains exactly 4 pages after the checklist's addition.

## The corrected martingale example (Appendix B)

**The problem.** Appendix B's betting-reading passage previously said λ's "sign is chosen after the fact, not pre-registered" and then called the resulting procedure an anytime-valid test at the 5% level. Those two statements cannot both stand: Ville's inequality requires a genuine test martingale, and a betting sign chosen after seeing the realized path breaks the martingale property $E[M_t \mid \mathcal{F}_{t-1}] = M_{t-1}$ outright. Verified against the primary sources the paragraph already cites (Ramdas, Grünwald, Vovk & Shafer 2023, arXiv:2210.01948v2, §§1.1, 2.2, 2.5, 2.9): a betting factor must be *predictable* ($\mathcal{F}_{t-1}$-measurable) for the martingale guarantee to hold at all.

**The fix.** The diagnostic is now the two-sided mixture $M_t = \tfrac{1}{2}M_t(+1) + \tfrac{1}{2}M_t(-1)$ — a genuine test martingale for the same null (a convex combination of test martingales is one), fixing no direction in advance. This costs a factor of two against a correctly guessed direction but requires no pre-registration claim the paper's runs never made.

**The corrected verdict, verified exact, independently, twice** (once by Sub-session B from the frozen simulation data, once again from scratch by Sub-session F1's adversarial critic, reading `src/forfeit.py` directly): at $\tau = 1.5$ past the edge, on the all-miss trajectory ($\alpha = 0.1$), the mixture reads

$$M_1, \ldots, M_6 = 1.000,\ 1.810,\ 3.430,\ 6.5161,\ 12.3805,\ 23.5229$$

which crosses the rejection threshold $1/0.05 = 20$ on the **sixth interval, not the fifth**. The old "fifth" was $M_t(+1)$ alone — exactly the number the invalid post-hoc sign choice bought. Inside the edge, the same test cannot reject at that level at any horizon: it peaks at $2.03$ ($\tau=0.5$) and $3.92$ ($\tau=0.9$) over the full measured range, and from round 62 on, Proposition 2's own bound on $|E_t|$ forbids rejection on every retained trajectory — this closure was re-derived independently by F1 with a deliberately looser relaxation and confirmed exact, not off by one.

The paper's Appendix B (`paper/sections/appendix.tex`, `\label{app:evalue}`) now reads, in full:

> The boundary is stated in $|E_T|$, which is the net gain of a Skeptic who pays $\alpha$ each round for $\mathrm{err}_t$; that is what gives it a betting reading. The reading Section 3 points at is Ville's inequality applied to the standard martingale $M_t(\lambda) = \prod_{i \le t}(1 + \lambda(\mathrm{err}_i - \alpha))$, whose logarithm depends on the path only through $t$ and $E_t$, under the imposed null that $\mathrm{err}_t \mid \mathcal{F}_{t-1}$ is Bernoulli$(\alpha)$, with $\mathcal{F}_{t-1}$ the history through round $t-1$. Ville's inequality needs each bet to be predictable, fixed by the history before the round it is scored on, so the direction of failure cannot be read off the realised path first. The diagnostic is therefore the two-sided mixture $M_t = \tfrac{1}{2}M_t(+1) + \tfrac{1}{2}M_t(-1)$, which is a test martingale for the same null because a convex combination of test martingales is one, and which fixes no direction in advance; both signs lie in $[-1/(1-\alpha), 1/\alpha]$, the range on which $M_t(\lambda) \ge 0$ on every path, the magnitude 1 is the same for every arm and both directions, and the mixture costs a factor of two against a correctly guessed direction. So read, an anytime-valid test of the deployed intervals' calibration convicts the $\tau = 1.5$ arm on its sixth interval at the 5% level, where $M_5 = 12.38$ and $M_6 = 23.52$ against the rejection threshold $1/0.05 = 20$. Inside the edge the same test cannot reject at that level at any horizon: it peaks at 2.03 for $\tau = 0.5$ and 3.92 for $\tau = 0.9$, and from round 62 on Proposition 2's bound on $|E_t|$ forbids rejection on every retained trajectory.

## The endpoint-framing clarification (Section 3)

The "closed-endpoint contradiction" the external audit flagged is real math and was already the paper's own stated finding — it needed a framing clarification, not a correction. Section 3's "published condition is tight" paragraph now closes with one added clause, naming the mechanism explicitly:

> ...though $\tau = 1.5$ covers there against the specified one. That asymmetry makes ``tight'' a located claim: a tie-convention property of the cited closed statements.

This makes explicit that the closed/open asymmetry is a property of the *cited* results' own closed-interval statements (Corollary 2 is named by number one sentence earlier in the same paragraph), not a new assumption this paper introduces, and that this section's contribution is locating exactly where that convention determines the outcome.

**This sentence was heavily compressed during Wave 3 integration to fit a hard page-budget constraint** (documented below) — the original draft naming "Theorem 1's and Corollary 2's" explicitly did not fit under any phrasing tested. Sub-session F1's adversarial critic reviewed the compressed version independently and found it does not overclaim (does not assert the cited theorems are wrong) or underclaim (the surrounding paragraph already establishes the "not tie-broken" / "strict indicator" framing on the preceding page, so the compressed clause reads as pointed, not vague).

## A page-budget regression was caught and fixed, not silently absorbed

Sub-session D's own page-count check, after adding its clarifying sentence, reported "9 pages total, body still exactly 4 pages, References opens page 5, no overflow." **That check was wrong** — it confirmed only that References landed on page 5, not that References was the *first* content on that page. An independent rebuild (first by Sub-session B's own control-build during its unrelated λ-sign work, then confirmed directly by the Wave 3 integrator before trusting any sub-session's self-report) showed 4 lines of pre-existing body prose spilling onto page 5, ahead of References — a real violation of the zero-margin "body exactly 4 pages, references clean" invariant this project has fought to hold across five prior sessions.

This was fixed by compressing D's own added clause — not by touching any other content — across four rebuild-and-measure cycles, restoring byte-for-byte the same page 4/5 boundary the paper held before D's edit. Both mandatory Wave 4 critics reviewed this: the adversarial critic (F1) independently rebuilt the pre-fix state and confirmed the overflow was real, not gratuitous; the instruction critic (F2) confirmed this was legitimate integration-phase remediation of Sub-session D's own addition (not a scope violation), while flagging it as the one genuinely contestable judgment call in the session.

## Final page count and protected boundary

**17 pages total.** Body is exactly 4 pages (ending "...paper has already run."); References opens page 5 as its first content; the checklist runs from immediately after the appendix to page 17, page-exempt per the template's own rule. This was independently verified three times: by the Wave 3 integrator, by the Overleaf package's isolated compile (SHA-256-identical rendered text to the repo build), and by Sub-session F1's adversarial critic's own from-scratch rebuild (SHA-256-identical again).

The protected boundary — the four-boundary theorem's statement, both proof directions, the closed form, both degenerate cases, every hedge in Limitations, the single-blind author block, the placeholder repository URL, and the venue — is **byte-identical to S17's ending state**, confirmed by direct diff (not narration) in both Wave 3 integration and Sub-session F1's independent check. `paper/sections/limitations.tex`, `setup.tex`, `intro.tex`, and `related.tex` show empty diffs; the only live-text changes anywhere are D's one compressed clause in `forfeit.tex`, B's rewritten betting-reading paragraph in `appendix.tex`, and C's completed `checklist.tex` plus one `\input` line in `main.tex`.

## Minor findings, no action required

Sub-session F1 flagged, and this report records for completeness: (1) the Wave 3 integrator's own commit message inaccurately described Corollary 2 as named in "the same sentence" as D's clarification, when it is in fact the preceding sentence — the anaphoric reference still resolves correctly for a reader, so this is a record-accuracy note, not a paper defect; (2) a stale, non-rendering LaTeX comment in `appendix.tex` quotes a superseded section number, left untouched as outside this session's authorized scope. Neither requires a paper change.

## Is this paper ready for submission?

**Yes, ready for the operator's own final read and submission to E-values**, on the same terms prior sessions have already flagged: the affiliation line and the repository URL are both still explicit, unmissable placeholders (`docs/OPEN_QUESTIONS.md` Q11/Q12), both the operator's own decision, not blocked on anything this session did. Everything this session was scoped to do — verifying and closing the checklist gap, fixing a genuine formal-validity defect in Appendix B, and clarifying the endpoint framing without softening any existing claim — is done, independently re-verified by two adversarial-posture critics, and the page budget holds exactly at 4 body pages with a clean References break, with the checklist correctly excluded from that ceiling.
