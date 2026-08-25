# S15 report — the paper fits TS-LIMITS' page limit; the repository is the open risk

**Session S15, 2026-08-24 / 2026-08-25.** Working folder `~/Desktop/Turnover-Blind`, branch
`main`. Wave 0 (A, venue verification), Wave 1 (B, C, D, E, F, G in parallel isolated
worktrees), Wave 2 (H, merge and measure), the operator-authorised cut (D2), Wave 3 (three
parallel critics, I1/I2/I3), the patch pass, and this report. Commits: `380d591`, `fc8328a`,
`72cc82f`, `93dba49`, and this report's commit.

---

## 1. The most important sentence in this report

S15's dedicated identity-leak critic (I2, Opus, working independently of the Wave 1 identity
sweep) returned this verdict, quoted verbatim from
`research/S15/I2-identity-critic-findings.json`, field `verdict.statement`:

> This build is NOT confirmed safe, and here is exactly what remains uncertain: the GitHub
> repository that is this working tree's `origin` remote is PUBLIC (unauthenticated API returns
> "private": false, pushed 2026-08-24), every commit on its published branch is authored under
> the operator's real name and email, and its published tree contains (a) a single-blind build
> of paper/main.pdf whose page 1 and /Author field carry the real name, affiliation and email
> and whose title and abstract are identical to the submission, (b) paper/main.tex and all six
> section files including the plaintext name and email, and (c) docs/S6_REPORT.md,
> docs/S5_REPORT.md and docs/S12_REPORT.md, which share 364, 93 and 92 distinct verbatim 8-word
> runs respectively with the submitted paper's own prose. Any reviewer who searches one
> distinctive sentence from the submission can reach that repository and read the author's name,
> so the anonymity of this submission is not established by the cleanliness of the PDF alone and
> requires an operator decision about the repository's visibility before submission.

**Current status of that finding.**

- **The compiled PDF itself is clean.** I2 verified `paper/main.pdf` under `dblblindworkshop`
  across three independent surfaces — raw bytes (ascii, utf-16-be, utf-16-le), the
  zlib-decompressed concatenation of every stream object (1,003,179 bytes recovered), and
  extracted page text — against 13 search terms, with **zero hits on all 13 terms across all
  three surfaces**. `/Author` is `Anonymous Author(s)`, no XMP block, no embedded files, no URI
  link annotations, page 1 renders the anonymous block. I2 repeated the whole check against the
  artefact as committed, not only its own rebuild; both clean. The general adversarial critic
  (I1) and the patch pass each re-ran a narrower version of the same check and agreed.
- **The blocking issue was never the file. It was the public repository.** The exposure is the
  bylined single-blind PDF, the plaintext `main.tex`, the real name and email on every commit,
  and hundreds of verbatim eight-word runs shared between the git-tracked session reports and
  the submitted paper's own prose — a searchable path from an anonymous submission to a named
  author in one step.
- **The operator's decision, recorded as `docs/OPERATOR_DECISIONS.md` entry 3, is to make the
  repository private before submission.** The operator will do this themselves, outside any
  session. That entry is marked **OPEN**. No session executed it and this one did not attempt
  it. (Note recorded there and repeated here: making the repository private is sufficient;
  deleting files from `HEAD` would not be, because they remain in git history.)

**Stated plainly: this paper is NOT yet confirmed submission-safe.** It does not become
submission-safe until the operator executes the repository-privacy step. The PDF being clean
does not settle it, and nothing in the rest of this report changes it.

I2 also recorded five lower-severity findings, none blocking, all judged non-identifying but
flagged rather than silently cleared: the real name/affiliation/email standing in plaintext in
`paper/main.tex` and in the shipped Overleaf package (F1 — by design, the dual-venue switch, and
demonstrably kept out of the compiled double-blind PDF); a distinctive research-process
vocabulary saturating the `.tex` comments and the shipped `.bib`'s `annote` fields (F2, a source
fingerprint, not a name); the `+05'30'` build timestamp (F3, narrows the timezone); the
date-shaped RNG seed `20260820` in the rendered Limitations (F4); the candid
"harness was rebuilt against numbers already read" disclosure (F5, a stylistic tell that is also
a genuine strength of the paper, recommended kept); and the named literature-search surfaces in
the Introduction (F6, standard scholarly practice). F7 records that `paper/main.log` carries the
OS username in absolute paths — it is not git-tracked and the Overleaf package correctly
excludes it.

---

## 2. TS-LIMITS' rules, verified fresh, and the one assumption that was wrong

Wave 0 (A) re-fetched TS-LIMITS' rules from source on 2026-08-24 — the OpenReview group record,
`https://ts-limits.github.io/content.js`, and the live submission form — treating the prior
project record only as a source of search terms. **No escalation:** every fact matched the
project's 2026-08-20 record exactly, down to the minute of the deadline.

| Rule | Confirmed value |
|---|---|
| Page limit | **4 to 7 pages plus references** — a range, floor 4, ceiling 7. Verbatim: "4 to 7 pages plus references, NeurIPS format, double-blind. Non-archival — recent and concurrent submissions welcome." |
| Anonymity | **Double-blind.** Implemented as `\usepackage[dblblindworkshop]{neurips_2026}`. Nuance on the record: the call says "double-blind" and does not itself name the option string; the mapping comes from the shared NeurIPS template's own documentation. |
| Template | **No separate TS-LIMITS template.** "NeurIPS format" only; no `.sty`/`.zip`/Overleaf/author-kit link anywhere in the call or on the submission form. |
| Required extra sections | **None.** No checklist, no ethics statement, no broader-impact statement, no anonymity attestation. The submission form has ten fields and an optional, explicitly non-required reviewer-nomination field. |
| Deadline | **2026-09-05 23:59 AoE = 2026-09-06 11:59:00 UTC.** The site's stated AoE deadline and OpenReview's enforced `duedate` agree exactly. |

**The assumption that needed correcting: the appendix policy.** The project had been working
under the reading it inherited from the E-values venue, where the page limit applied to the body
and appendices were explicitly excluded. A's targeted full-text search found that **TS-LIMITS'
call does not mention appendices at all**. It says "plus references" and stops. It excludes
nothing else.

Silence in a call is an interpretation question, not a fact question, so the orchestrator
escalated it rather than settling it. **The operator decided the 4–7 pages is a whole-document
limit — body and appendices together, with no page-exempt appendix budget**
(`docs/OPERATOR_DECISIONS.md` entry 1). This overrode the S15 brief's original body-only 5–6pp
target and is the decision every other S15 outcome follows from. Under the old reading the paper
was comfortable. Under the correct one it was, once merged, **2.7 pages over a hard ceiling**.

---

## 3. Final page count, and the target that was missed

**Final measured state, both venue options, from the patch pass's own from-clean builds
(artefacts deleted first, `pdflatex` + `bibtex` + three further `pdflatex` passes):**

| | Pages | Bibliography | Counted content | Ceiling | Inside? |
|---|---|---|---|---|---|
| `dblblindworkshop` (**the submission option**) | 9 | 2.2326pp | **6.767pp** | 7 | yes |
| `sglblindworkshop` | 9 | 2.2362pp | **6.764pp** | 7 | yes |

Zero TeX errors, zero overfull boxes, zero underfull hboxes or vboxes, zero LaTeX warnings, zero
`pdfendlink` warnings, zero undefined references, zero undefined citations, zero BibTeX
warnings, zero `??` in the rendered text — under both options. 40 distinct citation keys in
`main.aux`, 40 rendered bibitems. The counted-content metric is (total pages) − (pages the
bibliography occupies); I1 reproduced it independently to within 0.001pp from its own separate
builds, and the patch pass re-verified the three repaired passages by reading the rendered text
of the final PDFs rather than trusting any prior report.

**The original 5–6pp aspiration was missed, and it is worth saying why rather than rounding it
away.** The brief's 5–6pp target was written under the body-only appendix assumption. Once the
whole-document reading was confirmed, the same document had to fit a budget that also had to
carry every appendix — and the merged paper was genuinely 2.7 pages over the ceiling, not
over-formatted by 2.7 pages. Closing that took **real content cuts** (section 8 below), not
tightening. The honest landing is: **the paper is inside the ceiling but closer to it than to
the original aspiration**, at 6.767pp against a 7pp hard limit.

**And the margin is thinner than 0.233pp suggests.** The metric is quantised at whole pages: the
bibliography runs 2.23–2.25 pages, so a 9-page document scores 6.75–6.77 and a 10-page document
scores 7.72–7.75, with no value in between. The patch pass discovered the hard way that I1's
"3.7 lines of `dbl` headroom" estimate was wrong — the binding constraint is **Table 2's float
fit**, not line count. The first attempted F1 wording added about 22 rendered characters and
took the paper from 9 pages to 10 (counted content 7.724, i.e. 0.72pp **over** the ceiling) by
evicting the float. It was caught by the brief's rebuild-and-measure-after-every-fix rule and
reworded before shipping. **The real `dbl` margin is zero typeset lines.** Any future edit that
adds a body line needs a line paid back.

---

## 4. What moved back into the body — and the finding that moving things saves nothing

Sub-session D re-took every body/appendix placement decision from scratch, because each one's
recorded rationale turned out to be arithmetic about the *old* venue's 4-page body ceiling
rather than an editorial judgement:

- **Table 1 (the eleven-arm measurement table) merged into one table, in the body.** It had been
  split — four rows duplicated in the body, all eleven in the appendix — purely to fit a 4pp
  body while appendix pages were free. The split made a reader meet the same four rows twice,
  four pages apart, behind a five-line caption whose only content was bookkeeping reconciling
  the two tables. The duplicate was deleted.
- **Figures 2 and 3 promoted into the body, Section 3.** Figure 2 is the picture of the paper's
  headline sentence (the cliff, and the located edge on a symlog axis); Figure 3 is the
  nineteen-run, five-setting evidence that the boundary is a law rather than a fit to the null
  scorecaster, including both degenerate rules, and it exists nowhere else in the document.
- **"Where this sits" promoted from an appendix to numbered body Section 4**, between Section 3
  and Limitations. This is where the paper's concessions are made by name, and the Introduction
  ends on the bolded sentence those concessions cash out.
- **"The four vocabularies" merged into Section 4** as its first paragraph (a `\section` heading
  over a single paragraph since its table was deleted in S13), retiring a heading, a forwarding
  pointer, a cross-reference and a now-pointless `\clearpage`.
- **Table 2 stayed in Appendix A — re-earned, not inherited.** Its only recorded reason was void,
  so the decision was re-taken: a reader following the argument needs none of its thirteen rows,
  because the body states all three configurations in words and with the numbers; a referee
  auditing it wants all thirteen.
- **The e-value section was split into its own file** (`sections/evalue.tex`) and kept as
  Appendix B, on merit rather than inheritance — its S12 rationale had been an *E-values venue*
  argument that evaporates at TS-LIMITS. It was subsequently deleted under the operator's cut
  (section 8).

**The session's second major structural finding is that none of this saves pages.** Under a
whole-document ceiling, relocation between body and appendix is budget-neutral by construction —
so every placement above was decided on reader experience alone, which is the right basis but
also means the page problem was untouched by it. D recovered **0.91pp**, and every bit of it was
duplication and dead structure (the four-row duplicate table and its reconciling caption, a
`\clearpage`, a redundant section heading), not content. A rendered-text numeric-token and
word-level diff confirmed no measurement number disappeared. D reported the paper still
**2.08pp over the 7pp ceiling** after all of it, and explicitly declined to cut further without
authorisation — recommending instead that the document needed *one* content decision of about
two pages, taken once, with the protected list in hand.

---

## 5. What E's de-compression restored

Sub-session E reversed specific compressions taken in S4, S5, S6, S8, S10, S12 and S13 — all of
them originally taken against E-values' 4-page **body** ceiling, a constraint that no longer
exists. E first confirmed that **S14's compression was never in the paper at all**: `git diff
3ad0f8c HEAD -- paper/` was empty, so S14's revert was genuine and there was nothing of S14's to
undo. Eighteen changes across six section files; nine further compressions were examined and
**deliberately not reversed**. Three concrete examples:

**E9 — `setup.tex`**, reversing S4's cut, which had listed it under its own
"WHAT WAS CUT TO PAY FOR IT" header:

> *before:* "Either readout has two positions in (\ref{eq:pid}), drawn in
> Figure~\ref{fig:placements}; **(A)**, Placement~A, is measured here."
>
> *after:* "Either readout has two positions in (\ref{eq:pid}), drawn in
> Figure~\ref{fig:placements}. **(A)**, Placement~A, is the one measured here, and it is the one
> a designer reaches for, because the deployed number is what has to sit still."

This is the only place in the paper that says *why* the paper measures the placement it
measures. S4's header claimed the motivation was "now carried by the finding sentence"; it is
not — the finding sentence is about L1 vs L2, not A vs B.

**E6 — `setup.tex`**, reversing S4's fold of a two-sided condition into one signed line:

> *before:* "condition~(4) requires $|r_t(x)| \ge b$ with the sign of $x$ once $|x| \ge c\,h(t)$…"
>
> *after:* "condition~(4) requires $r_t(x) \ge b$ for $x \ge c\,h(t)$ and $r_t(x) \le -b$ for
> $x \le -c\,h(t)$… In words: once the accumulated error clears $c\,h(t)$ in either direction,
> the correction is at least a full $b$ in the direction that reduces it."

**E12 — `forfeit.tex`**, restoring a sentence S10 deleted to pay for two claim-bearing additions
to a body with zero slack:

> *before:* "…A readout on the completed $q_{t+1}$ touches neither $r_t$ nor the integrator's
> argument, so it cannot put~(4) at risk. It delays a correction already computed, so the
> accumulator excurses *further*…"
>
> *after:* "…**The forfeit's sign is counter-intuitive, so it is worth saying what does and does
> not break.** A readout on the completed $q_{t+1}$ … cannot put~(4) at risk. What it does
> instead is delay a correction that has already been computed, so the accumulator excurses
> *further* rather than less…"

E's restorations were checked for overclaim by I1, which found they run **predominantly in the
conservative direction** — E3 and E15 both narrow claims the compressed one-liners had left
sounding global. All eleven Limitations hedges were verified byte-identical; across the whole of
S15 the diff to `limitations.tex` is additive only. In isolation E cost **zero pages** (13 before,
13 after, the additions absorbed inside page 5) — but E's ~247 added lines landed on top of D's
already-over-budget structure at merge time, which is exactly what both D and E predicted in
their own reports.

---

## 6. Scope fit: F found none, made no changes, and this is an unresolved submission risk

This deserves prominence, because it is the one risk in this report that no amount of
formatting, hedging or anonymity work can touch.

TS-LIMITS is *"Generalization for Time Series in Tight Settings: Latency, Inference, Memory,
prIvacy and susTainability."* Its stated gate is on **five deployment bottlenecks** —
sub-ms inference, memory-efficient architectures, minimal supervision, privacy in temporal data,
sustainability — and the call says submissions should address one or more of them. Sub-session F
assessed the paper against all five and all ten listed topics:

| Bottleneck | Fit |
|---|---|
| Sub-ms inference | **Absent.** The paper reports no timing of any kind — no latency, throughput or wall-clock number anywhere. |
| Memory-efficient architectures | **Absent.** No footprint measured or claimed. |
| Minimal supervision | **Absent.** Online conformal prediction consumes a realised label every round; it is fully supervised at test time. |
| Privacy | **Absent.** The word does not occur in the paper. |
| Sustainability | **Absent.** |

**The paper scores zero on the binding gate — not weakly, zero.** F's verdict: no framing change
is warranted, because the mismatch is at the level of subject matter and not emphasis. The
opening is not E-values-tuned prose needing neutralisation; it is venue-neutral prose about a
coverage guarantee, and there is no sentence in it that could be promoted to touch compute,
memory, labels, privacy or energy. **F edited zero files.** It recorded, for the operator, the
one candidate change it considered and rejected (surfacing that both boundaries are computable
before deployment — verbatim-supported and honest, but a single deployment-flavoured clause that
would not change the fit and would read as reaching), so that the operator can overrule it if
they disagree.

I1 independently re-ran F's load-bearing greps against the *current* paper and confirmed them:
in the rendered body, `drift` 0, `non-stationar` 0, `distribution shift` 0, `latency` 0,
`privacy` 0, `energy` 0, and **`time series` 0**. The only occurrences in the live source are
inside the `\workshoptitle` string itself. I1 went looking for the case that F was too quick,
on the two topics where a stretch was most tempting, and concluded F's refusal to reframe is the
honest call.

Two corroborating priors, found only *after* F reached its own verdict: `research/S3/H2-venue.json`
recorded the same structural mismatch on 2026-08-20, and `docs/VENUE.md` §2.3 already reads
"Topical fit: poor" with "The designation should be revisited." (VENUE.md's *specific* argument
is now stale and should not be quoted forward — it reasons about a turnover/transaction-cost
version of the paper that no longer exists — but its conclusion stands.)

**The standing risk, stated plainly: the paper may not clear TS-LIMITS' topical review gate
regardless of how well-formatted, well-hedged, or well-anonymised it now is.** A paper submitted
to a time-series workshop contains the phrase "time series" zero times in its body. Making it
actually fit would take new content — at minimum a measured deployment quantity (latency,
memory, label cost or energy) attached to the readouts the paper already runs — which is a new
experiment and out of scope for this session. The venue decision was presented to this session as
already made, and **no S15 sub-session reopened it**; I3 verified that. This report supplies one
input to it and does not attempt to reopen it either.

---

## 7. The submission package builds clean in isolation

`build/overleaf-package/` is git-tracked and is the actual submission artefact, so it was
resynced with the cut (D2) and again with the patch pass, and compiled standalone both times
**from a temporary directory with no path back to this repository**:

- **Sync:** `main.tex` and all six section files differ from `paper/` by exactly three path
  rewrites (`\bibliography{../audit/REFS_VERIFIED}` → `{REFS_VERIFIED}`, and two
  `\includegraphics{../figures/...}` → `{figures/...}`) **and nothing else**, verified by diff on
  every file. The deleted `sections/evalue.tex` was removed from the package too.
- **Isolated compile:** **9 pages, bibliography 2.2326pp, counted content 6.767pp, zero
  diagnostics of every class.**
- **Text identity:** the package build's extracted text is **byte-identical** to
  `paper/main.pdf`'s.
- **Its own metadata check:** `/Author = "Anonymous Author(s)"`, and **zero raw-byte matches**
  for the operator's name, email, or `github.com`.
- **README:** every page figure refreshed from the patch pass's own measurements. The stale
  "2.77-page gap" was corrected to **2.72** with its provenance stated rather than silently
  changed — I1 rebuilt the merge commit `fc8328a` from a clean archive and measured 12 pages /
  2.284pp bibliography / 9.716 counted content, so `fc8328a`'s own commit message geometry was
  wrong and D2's re-derivation was right. The margin checklist bullet was rewritten to state the
  float-fit mechanism rather than a line count.

---

## 8. What was cut, honestly

**This was not a routine compression pass.** It was a real deletion of content that this
session's standing rules protected, taken under an explicit, narrowly-scoped operator override,
and it is the most consequential editorial decision of S15.

**How it was authorised.** S15's brief protected seven categories of content — the four boundary
definitions, both proof directions, the closed-form statement, both degenerate cases, every
Limitations hedge, the open-band disclosure, and R3a — under a "restore, don't cut" rule. The
session could compress; it could not delete. The override came in two steps
(`docs/OPERATOR_DECISIONS.md` entry 2):

1. The operator first authorised **cutting or compressing Appendix B**, the promoted e-value
   section, with an instruction to compress before deleting.
2. The orchestrator then measured that **Appendix B alone could not close the gap** — at D's
   measured 1.87pp it was insufficient against a 2.7pp overage even if deleted outright — and
   put that arithmetic back to the operator **before** proceeding. The operator **then** authorised also
   cutting **Appendix A's five prose paragraphs**.

The grant was exactly those two targets and nothing else. Everything else in the seven protected
categories stayed untouchable and stayed untouched.

**What was cut.**

- **Appendix B, "The accumulator as a bet, and a calibration test built on the boundary" —
  deleted in full.** `sections/evalue.tex` is removed, its `\input` removed, `\label{sec:evalue}`
  gone with no surviving `\ref`. It was 1.61pp (dbl) / 1.97pp (sgl), about 21% of the counted
  document. **Compression was tried and measured, not assumed away**: a 9-line compressed version
  was actually built, and it still cost a whole extra page, because the metric is quantised —
  with the bibliography ending 65% down page 9, the remaining appendix either fits the 0.354
  pages left on that page or the document takes a tenth. A second measurement pushed the same
  way: deleting the section outright dropped four bibliography entries, which *shortens* the free
  bibliography and therefore *raises* counted content by ~0.22pp; three of the four were saved by
  carrying them into the body with the construction they support.
- **Its load-bearing content was folded into the body**, into the existing `forfeit.tex`
  paragraph "The boundary read as a bet." (itself restored by E earlier in the session): the test
  martingale $M_t = \prod_{i \le t}(1 + \lambda(\mathrm{err}_i - \alpha))$, Ville's inequality,
  the self-limiting "it adds a diagnostic and a reading, not a result" sentence, and an **added**
  disclosure that $M_t$ is itself an e-value for the imposed null alone — a concession the
  document had not previously stated in that form, added deliberately so that
  "the accumulator itself is neither an e-value nor an e-process" would not stand as the paper's
  only statement on the matter. I1 confirmed the added clause is limiting rather than assertive
  and introduces no overclaim.
- **Appendix A's five prose paragraphs — deleted.** "The primary regime"; "Excursions at
  $T = 10^4$, and where the excursion law holds"; "Realised miscoverage at the covering settings
  of Figure 3"; "What survives of the measurement, and what its status now is"; "Where the rate
  stops being a tell." 1.04pp. **Table 2 and all thirteen of its rows, its caption, its column
  heads, its `\label` and the section heading were untouched.** D had flagged that this project
  treats deleting measurement description as a serious act and declined to do it on that basis;
  the operator weighed that and authorised it anyway. All five paragraphs are quoted in full in
  `research/S15/D2-budget-closure.json` so the deletion is recoverable verbatim.

**Result: 2.949pp recovered, 12 pages to 9, counted content 9.716 → 6.767 (dbl) / 6.749 (sgl).**

**Verification that the cut stayed inside its authorisation.** `limitations.tex` and `setup.tex`
were byte-identical across the cut (`git diff --quiet`, exit 0). 45 literal-string probes against
the rendered text of four builds: **45 of 45 present, 0 regressions.** A 44-token numeric-loss
audit, every token attributed. I1 then re-verified all of it independently from its own builds
and confirmed **all seven protected categories survive unweakened** and no unauthorised cut
occurred.

**What the cut broke, and what was repaired.** I1 found three real defects the cut left behind,
all fixed in `93dba49` and all re-verified from the rendered text of the final PDFs:

| | Defect | Repair |
|---|---|---|
| F1 | A surviving Limitations hedge referenced `$0.63/(1-w)$`, a constant defined **only** in a deleted Appendix A paragraph — an undefined symbol occurring once in the whole document. | Reworded to remove the dependency. Restoring the number was **rejected**: the deleted paragraph qualified it in the same breath ("a fit to those five arms, not a derived bound"), so restoring the number alone would have created a new unqualified claim — the same defect as F2. |
| F2 | The deleted section's pre-registration caveat was gone, but the verdict it qualified — "convicts the $\tau = 1.5$ arm on its fifth interval at the $5\%$ level" — survived in the body. The conclusion outlived its qualifier. This is the one place the cut raised apparent confidence. | Restored the operative half inline, next to the claim: "and its sign above is chosen after the fact, not pre-registered". |
| F3 | The fold-in carried $M_t$'s formula into the body with $\lambda$ free and unquantified. Outside $[-1/(1-\alpha),\,1/\alpha]$ the surviving clause "$M_t$ is an e-value for that imposed null alone" is **false**. A correctness defect, not a cosmetic one. | Range inserted inline immediately before the clause it makes true. |

Two further fixes went in with them: **F4**, a genuine `$\lambda$`/`$w$` notation collision that
this session's fold-in exposed but did not create (the smoothing weight was defined as $\lambda$
in `setup.tex` and used as $w$ everywhere else in the paper, and had been since long before
S15), and **F11**, the stale page-gap figure in the shipped package README (section 7).

**Residuals that were declined on budget, recorded rather than hidden.** The "fifth interval"
figure is still not reproducible from the document alone — F3 restores the range that makes the
sentence *true* but not the stake ($\lambda = 1$) that makes the number *checkable*; F2's
restored caveat covers the disclosure that matters. Appendix A now has no prose at all, and the
undisclosed magnitude of the counting-convention dependence is likewise unbought. Each costs
roughly one line, and the measured budget is zero lines, so buying either back means taking a
tenth page or cutting something else. **Both are live operator calls.**

---

## 9. Instruction compliance (I3)

The instruction critic checked S15 against its own governing brief, item by item, and found
**7 of 9 items compliant**: one commit per sub-session (avoiding S14's git-race anti-pattern),
A's escalation rule working correctly, protected content intact, **no gate signed**, **frozen
identity values unchanged**, headless-only retrieval discipline followed in Wave 0, and **the
venue decision not reopened** despite F's scope-fit finding. The eighth item — B/I2 independence
— was pending at check time and is now confirmed by I2's own report, which records that
`research/S15/B-identity-sweep.json` was opened only after all of I2's independent conclusions
had been reached, with the single exception declared explicitly (I2 adopted B's cross-check
*idea* after reading B, and that is what led to F0).

The ninth item was a genuine process gap, not a rule breach: the session's mid-session operator
authorisations — including an explicit override of the standing protected-content rule — existed
only in gitignored JSON and, partially, in one commit message. `research/` is gitignored, so a
clone of this repository does not carry it. I3 recommended a dated, git-tracked record
independent of both. **That recommendation is fulfilled by `docs/OPERATOR_DECISIONS.md`**, created
this session, which records all four of S15's operator decisions with what was asked, what was
granted, how wide the grant was, and what it overrode.

---

## 10. Final verdict on submission-readiness

**The paper is ready for the operator's final read.** It is inside TS-LIMITS' 7-page
whole-document ceiling at 6.767pp under the actual submission option, builds clean under both
venue options with zero diagnostics of every class, carries a correctly-anonymised PDF verified
on three independent surfaces, has all seven protected content categories intact outside the two
authorised cuts, has the three defects that cut introduced repaired and re-verified from the
rendered text, and ships as a package that compiles standalone to a byte-identical rendering.

**The repository is not safe to leave public through the review period.** I2's verdict is not a
clean "confirmed safe," and the reason has nothing to do with the paper: a public repository
carrying a bylined build of the same paper, its plaintext source, the author's name on every
commit, and hundreds of verbatim sentences from the submission defeats double-blind review
regardless of how clean the submitted file is.

**The one remaining action item before this can be submitted:**

> **The operator must make the GitHub repository private.** It is decided
> (`docs/OPERATOR_DECISIONS.md` entry 3) and **not executed**. No session did it and none can
> verify it. Making it private is sufficient; deleting files from `HEAD` is not, because they
> remain in git history.

Two further open items, both for the operator and neither blocking:

- **Topical fit (section 6).** The paper addresses zero of TS-LIMITS' five stated bottlenecks.
  This is a real risk to acceptance that no editorial work in this session could reduce, and it
  is independent of everything else in this report.
- **Two declined buy-backs (section 8)** and the optional zero-signal build
  (`SOURCE_DATE_EPOCH` or `\pdfinfoomitdate=1`, which would clear I2's F3 timestamp signal at the
  cost of changing the build recipe).

---

## 11. Time remaining

**Deadline: 2026-09-05 23:59 AoE = 2026-09-06 11:59:00 UTC**, independently re-verified this
session against both the call text and OpenReview's enforced `duedate`, which agree exactly.

At the time of writing (**2026-08-25, 17:15 UTC**), that is **11 days and roughly 19 hours —
11.8 days**. Counted in calendar days, the deadline falls twelve days from today.

The remaining work inside that window is one operator action (make the repository private), one
operator read of the paper, and one venue judgement call. None of it is blocked on further
editorial work, and none of it should be left to the last day: the repository has been public
throughout this session, and every day it stays public is another day the submission's anonymity
depends on nobody having looked.
