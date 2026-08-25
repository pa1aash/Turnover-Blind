# S16 report — the body meets E-values' 4-page ceiling, by tier C+D; the paper is ready pending the operator's read

**Session S16, 2026-08-26.** Working folder `~/Desktop/Turnover-Blind`, branch `main`, remote
`git@github.com:pa1aash/Turnover-Blind.git`. Wave 0 (A, venue reconfirmation), Wave 1 (B, C, E),
Wave 2/3 (F, integrate/measure/escalate to D), Wave 4 (G, Overleaf package rebuild), Wave 5 (H,
both critics), this report (I). Commits: `279079b`, `da2c39e`, `86db0d1`, `c5c54af`, `19e168a`,
`3f433a8`, `d49aa5b`, `c04edce`, and this report's commit.

---

## 1. The single most important fact

**The body reached E-values' 4-page ceiling, and it took both authorized tiers — C alone was
not enough.** Sub-session C (reversing S15's TS-LIMITS-specific promotions of Table 1, Figure 2
and Figure 3 into the body) recovered the placement but left the body at exactly **5 pages** —
one full page, about 50 typeset lines, over the ceiling — because the body had also accumulated
real prose since S14 (S15 sub-session E's de-compression, and S15 sub-session D2's folding of
the deleted e-value section into body prose) that a placement reversal alone cannot pay for.
Sub-session D was invoked immediately per the operator's pre-authorization, no pause to ask, and
closed the remaining gap through genuine content removal and compression. **Verified by the
opened-page method, independently, twice** (by the orchestrating session after D, and again by
sub-session H1's from-scratch rebuild): page 4 ends with Limitations' closing sentence; page 5
opens with the literal word "References" as its first content. **9 total pages, body exactly 4,
0 TeX errors, 0 undefined references or citations, 0 bibtex warnings.**

---

## 2. Everything relocated to the appendix (sub-session C)

Reversing S15's whole-document-ceiling-driven promotions, restoring the S10/pre-S15 placement
that held the paper at exactly 4 body pages from S10 through S14:

- **Table 1, the eleven-arm measurement table** (`tab:forfeit`) — moved back to the head of
  Appendix A ("Supporting measurements"), before Table 2 (boundary stress). Moved whole, cell
  for cell: caption, all eleven rows, no content lost.
- **A compact four-row illustrative table restored in the body** in its place (the S12/S13
  precedent): control, partial adjustment (w = 0.999), dead band τ = 0.9, dead band τ = 1.5 —
  two covering arms and two failing/near-boundary arms, every cell a straight copy from the
  full table, no new computation. Caption points to the appendix table for the remaining seven
  arms and finer detail.
- **Figure 2, "the cliff"** (`fig:boundary`) — moved to Appendix A, immediately after the
  restored table.
- **Figure 3, the 19 dead-band runs across five settings** (`fig:settings`) — moved to Appendix
  A, beside Figure 2.
- **`sections/related.tex`, "Where this sits"** (carrying the merged-in "One quantity, four
  names" paragraph) — moved back out of the body `\input` list, now `\input` after
  `sections/appendix`, rendering as an appendix section exactly as S10 had it. The
  four-vocabularies merge itself stays merged; that simplification was unrelated to venue.

Full inventory with before/after cross-reference locators: `research/S16/C-appendix-reversal.json`.

This alone was not sufficient (body still at 5 pages), and sub-session C's own record says so
plainly rather than overstating the recovery.

---

## 3. Everything genuinely removed or compressed (sub-session D)

Worked the operator's candidate list in order, stopping once the gap closed — **tier 5,
illustrative examples beyond the minimum, was not needed.**

- **Tier 1 — the folded-in e-value diagnostic paragraph** ("The boundary read as a bet.")
  compressed in the body from roughly 35 lines to 6. Its full derivation — the test martingale,
  Ville's inequality, three citations, the pre-registration caveat, the five-interval verdict —
  relocated verbatim in substance to a new appendix section, `sections/appendix.tex`,
  \section{The betting reading}, `app:evalue`. Both hedges the brief specifically protects for
  this paragraph — "It adds a diagnostic and a reading, not a result" and "no result above
  assumes that null or is certified by that test" — stay in the body pointer; the second is also
  restated inside the appendix section, so neither half can be read alone and over-claim.
- **Tier 2 — S15 sub-session E's TS-LIMITS-driven de-compression reversed**, itemized against
  that commit's own accounting of what it added versus what were the section's original hedges:
  Limitations' opening orienting sentence, two paragraph breaks, and one explanatory clause
  S15-E's own commit names as new — not one of the section's eleven original hedges, all eleven
  of which remain byte-identical. An unpacked degenerate-case paragraph in `forfeit.tex`
  reverted to its pre-S15-E terse form; both degenerate cases (tangent integrator, q̂ = +b/2)
  keep their full mathematical content, only the added explanatory wrapper is cut. Related
  aphorism unpacking in `intro.tex`/`setup.tex` reverted where the compressed form loses no
  number or hedge.
- **Tier 3 — redundant restatement.** One whole paragraph cut ("The constructive reading, and it
  is the corollary's rather than ours."), every one of its four clauses checked against a
  surviving site elsewhere in the paper before cutting. One triple-stated contrast trimmed to
  its two surviving instances (abstract, intro).
- **A related correctness fix, folded in rather than deferred:** `setup.tex`'s citation
  enumeration for the four-vocabularies discussion was compressed to a pointer to save body
  lines — a compression that would otherwise have silently dropped seven bibliography entries
  cited nowhere else. All seven were relocated, with their locators, into `sections/related.tex`
  (now appendix content after sub-session C's move), so nothing drops from the bibliography.

Full before/after text for every removal, and the pre-edit hedge inventory it was checked
against: `research/S16/D-content-removal.json`.

**A note on how this record was produced.** The sub-agent executing sub-session D was cut off by
an API error twice while writing its own final report. Its file edits were complete and sound —
visible directly in the commit diff — but its JSON's own itemized removal log was lost with it.
The orchestrating session reconstructed sub-session D's summary above from the actual commit
diff and message, and independently re-verified the result from scratch (its own fresh rebuild,
its own diff of the protected paragraphs, its own cross-check of S15-E's commit line by line)
rather than trusting the incomplete report. This is recorded here rather than smoothed over.

---

## 4. The protected boundary survived intact

Per sub-session H1's independent, from-scratch check (not taken on any prior sub-session's own
word): all five protected elements read directly from `paper/sections/forfeit.tex` and
`limitations.tex`, on the rendered PDF, right now —

1. **The theorem statement** — the iff condition, stated in bold, intact.
2. **Necessity, over the whole admissible class** — the "Failure, over the whole admissible
   class." paragraph, with its freedom-from-hypotheses hedge, intact verbatim.
3. **Retention, keyed to the reach rather than the supremum** — intact verbatim, including the
   bound retained rather than weakened.
4. **The closed form** — the equation and its endpoint condition, plus both of its own guarding
   hedges, intact.
5. **Both degenerate cases** — the tangent-integrator edge and the q̂ = −b/2 edge, both fully
   stated with every printed numeric value unchanged.

H1 additionally checked all 68 items of sub-session D's pre-edit hedge inventory against the
current text, one by one: 55 exact matches, 13 chased individually and all accounted for
(relocated to the appendix with a body pointer, merged into an adjacent surviving sentence, or —
in one case — a reassurance clause rather than a qualifying hedge, correctly outside the
protected set). **No hedge was silently lost.**

Two gray-area items surfaced (one from each critic) and were reviewed rather than waved through
silently — both judged authorized relocations, not violations, reasoning recorded in
`research/S16/patch-log.json`:

- The λ "sign chosen after the fact, not pre-registered" caveat is now appendix-only; the
  specifically protected hedge for that paragraph ("not a result... not certified") stays in the
  body, and the full caveat survives verbatim in the appendix with an explicit body pointer.
- A justificatory clause trimmed near the tangent-integrator degenerate case removed explanatory
  prose only; the case's mathematical claim and every numeric value are independently confirmed
  unchanged by both critics.

---

## 5. Single-blind identity is correctly restored

- `sglblindworkshop` is the active package option; `dblblindworkshop` is commented out.
- `\workshoptitle{E-values: From Statistics to ML}` is active; the TS-LIMITS title is commented
  out.
- The author block prints real values — **Palaash Gang, Independent Researcher,
  palaashgang@gmail.com** — and renders visibly on page 1. `pdfinfo` confirms `Author: Palaash
  Gang`.
- Zero "Anonymous" residue anywhere in the rendered text (`pdftotext` and `strings`, both zero
  hits); the one live `dblblindworkshop`-only string in the source is correctly dead code inside
  an `\if@anonymous` guard that `sglblindworkshop` clears.
- The repository URL is still exactly the placeholder,
  `https://[REPOSITORY LINK - INSERTED BY AUTHOR PRIOR TO SUBMISSION]` — a real fact, not a new
  decision, unchanged by this session.

**S15's open repository-privacy question is moot under this venue.** S15's final report flagged
the public GitHub repository (real name, real email, in every commit and several `docs/*`
files sharing hundreds of verbatim word-runs with the submission) as an unresolved risk under
TS-LIMITS' double-blind anonymity. Under E-values' single-blind option — non-anonymous, author
block permitted — that same fact is no longer a leak; it is simply the correct, expected state.
Nothing about the repository needed to change for this switch, and nothing was changed.

---

## 6. The Overleaf package

Rebuilt fresh (sub-session G): every stale TS-LIMITS-double-blind file deleted first, not
patched, and re-copied from `paper/` with the three relative-path rewrites that let it compile
standalone. Test-compiled twice in genuine isolation — once by sub-session G itself, once again
independently by sub-session H1 from a separate fresh copy — both times: 0 TeX errors, 0
undefined references or citations, 9 pages, rendered text byte-identical (same SHA-256) to
`paper/main.pdf`. `README.md` rewritten to match the current venue, page count and page-margin
framing (zero lines of headroom, not a fractional page margin).

---

## 7. Is this ready for E-values?

**Yes, pending the operator's own final read.** Both mandatory Wave 5 critics — H1 (adversarial,
independently re-derived every measurement and claim from scratch) and H2 (instruction
compliance, checked this brief item by item) — returned clean: no finding required a body or
appendix revert, the two gray-area items are authorized relocations with their reasoning on
record, and every hygiene gate (`check_hygiene.sh`, `check_prose_hygiene.sh`,
`check_claim_drift.sh`) passes.

What specifically remains, and it is unchanged from before this session, not new:

1. **The affiliation line** (`Independent Researcher`) is a placeholder that lets the document
   build, not a decision — `docs/OPEN_QUESTIONS.md` Q11. It prints as-is under the active
   option, so it is live now.
2. **The repository URL placeholder** needs the real link inserted before submission —
   `docs/OPEN_QUESTIONS.md` Q12.

Neither is a defect this session could resolve on its own authority; both are named explicitly
rather than left to be discovered at submission time.

---

## Days remaining

**3 days** to E-values' submission deadline (2026-08-29, 23:59 AoE) as of this session's date,
2026-08-26.
