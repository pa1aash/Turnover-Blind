# S12 report — the closed form, the promoted e-value section, and a body table

**Session S12, 2026-08-22.** Working folder `~/Desktop/Turnover-Blind`, branch `main`. Wave 0
preflight, four parallel sub-sessions (A/B/C1/D), one serial adversarial attack (C2, after C1),
one serial integration sub-session (E), two mandatory parallel critics (F1/F2), and a patch wave
closing their findings. Three commits this session (`e9444e7` integration, `e1c33f2` patch), not
yet pushed as of this report.

---

## A's two reconfirmations: both held

**Yes, plainly.** A1 (the footer/template question) reconfirmed: `paper/neurips_2026.sty`'s
footer is gated by `\if@neuripsfinal`, not by the workshop or anonymity option, and a fresh live
fetch of the E-values workshop's current call is byte-identical to S8's record. A2 (the Corollary 2
anchor's version history) reconfirmed: a fresh arXiv API query on 2508.13362 shows v3 is still the
sole latest version, matches the bibliography's pinned citation, and the corollary's restatement in
the paper still matches v3's text word for word. Neither check escalated. Both were independently
re-verified a second time by F1 in Wave 4, with the same result. This closes the footer question
(raised twice, S8 and now S12) and the Corollary 2 version question (raised three times, S3/S4, S8,
now S12) for good — a fourth re-litigation of either would be diminishing returns, not diligence.

---

## The closed-form corollary, now in the paper, in full

> **The sharp form is one number, and its hypotheses are what buy it.** Specialise to a symmetric
> saturator that meets (4) with equality and attains its extremes there ($\Lambda^{\pm}_t =
> A^{\pm}_t = \pm b$; the harness's $r_t = b\,\mathrm{clip}(x/(c\,h(t)),\pm 1)$ is one, Section 2),
> and to a constant $\hat{q}$. Then
> $$\min(\tau^{\star+},\tau^{\star-}) = b/2 - |\hat{q}|, \qquad (3)$$
> with the endpoint admissible only when $\hat{q} < 0$: exactly Corollary 2's radius at $\mu_t = 1$,
> now as an if-and-only-if. **The necessity direction above assumes none of it**: $\tau >
> \tau^{\star+}$, or $\tau \ge \tau^{\star-}$, forfeits coverage against every admissible $r_t$ and
> every legal predictable $\{\hat{q}_t\}$, extremes attained or not, and that unrestricted
> statement is what this section claims. The two hypotheses are load-bearing rather than
> decorative: the unattained supremum and the varying-$\hat{q}$ split two paragraphs above are
> exactly what they rule out. Equation (3) is where the reach meets the supremum, not evidence that
> they always do.

It sits in Section 3, immediately after the paragraph that ends "And $\tau^{\star-}$ was missing
entirely" — right next to the two counterexamples ($\tau^{\star+}=19$ unattained;
$\tau^{\star+}=2$ vs $\sigma^{+}=1$ under a time-varying $\hat q$) it leans on rather than restates.
Both F1 and the drafting sub-session independently confirm it reads as a clarifying special case:
the necessity direction is stated unrestricted in the same breath, and the reach-vs-supremum
distinction is explained by naming what the hypotheses rule out, not asserted as decoration.

---

## The promoted e-value section: shipped, with a fix

**Final status: shipped as Appendix D, with one HIGH-severity fix applied before shipping and
three cosmetic fixes applied afterward.**

C1 drafted a full promotion of the old single disclaimed paragraph — an explicit Bernoulli($\alpha$)
null stated as a hypothesis of a *test*, the full construction of the martingale $M_t$, and a
worked example computed from this paper's own frozen $\tau=1.5$ arm (the run's `n_err == T` at
every recorded horizon pins the per-round path exactly, no reconstruction). C2's adversarial attack
found a genuine mathematical error the promotion had introduced — "the test never rejects, at any
level" confuses $M_T \to 0$ with $\sup_t M_t$, which is what Ville's inequality actually prices —
and fixed it with a uniform-supremum bound ($S(1) = 2.448$, giving $M_t \le 11.57$ at every round
inside the retained band). C2 also found the retained disclaimer, "we construct no e-value here and
claim none," was literally false at the promoted length (a test martingale is, formally, an
e-variable for its own null), and replaced it with a sharper, correct formulation that concedes the
technical point without conceding the substance: *"$M_t$ is itself an e-value, and we say so: an
e-value for $H_0$ alone... No result of this paper is an e-value result or rests on one."* Both
fixes shipped verbatim. F1's independent re-attack in Wave 4 re-derived every number in the worked
example to the same digit and confirmed the uniform-bound fix genuinely closes the error, then
found one further defect neither C1 nor C2 caught: an overfull display box, 74.6pt into the right
margin — the only overfull box in the document — which is now split into a three-line `gather*` and
fixed. F1 also flagged, and this session closed, an unclosed point: the worked example fixes
$\lambda$'s magnitude but chooses its sign after seeing which way an arm failed, which a genuine
anytime-valid deployment cannot do; a sentence now says so explicitly rather than leaving it
implicit.

It lives in the appendix, not the body — C2's placement recommendation, on the grounds that a
numbered body section on the one construction the paper explicitly disclaims, in a paper whose
workshop title is "E-values: From Statistics to ML," would reopen exactly the framing question the
current abstract avoids. The body signposts it from one place: `sections/intro.tex`'s roadmap
sentence. A second, more detailed local pointer was drafted for Section 3 and cut entirely during
page-budget reconciliation (see below) — not because it was wrong, but because it was the one piece
of this session's new content that duplicated the appendix rather than adding to it.

---

## The body results table, now in the body, in full

> **Table 1.** Placement A, primary regime, $T = 10^6$: four arms of Table 2 (App. A), which lists
> the remaining seven and finer detail. Proposition 2's bound is $14.8155$; "ratio" is
> $\max_t|E_t|$ over it.

| Arm | miscov. $10^6$ | $\max_t|E_t|$ $10^6$ | ratio |
|---|---|---|---|
| none (control) | 0.100007 | 7.80 | 0.53 |
| partial adj. $w=0.999$ | **0.100004** | 623.70 | 42.10 |
| dead band $\tau=0.9$ | 0.100012 | 13.20 | 0.89 |
| dead band $\tau=1.5$ | **1.000000** | 900,000 | 60,747 |

Every cell is a straight copy of the appendix's own Table 1 (now Table 2 by document order), traced
to `results/forfeit-20260820T063045Z-83747c45.json`, `aggregate_table`, regime `adversarial`,
$T=10^6$. F1 re-verified all twelve cells independently against that file. It sits at the end of
Section 3's opening paragraph — the first table a reader meets, before the appendix, and the venue's
call names appendices "optional" reading. A reader who never opens the appendix now sees the
central phenomenon (coverage holds to the boundary, fails completely past it) without leaving the
body.

---

## Final page count: the paper no longer fits E-values' strict 4-page ceiling

**Body is 5 pages under the committed `sglblindworkshop` (E-values) option, verified by the
opened-page method independently by both the integration sub-session and F1.** Page 4 ends exactly
at the last line of Section 3's open-band disclosure paragraph, with zero slack; Section 4
("Limitations," 18 body lines, entirely pre-existing and untouched) is displaced whole onto page 5,
which opens with "Limitations" rather than "References." This is a real, honestly-reported
regression from S10's exactly-4-page, offset-0 baseline, not a rounding artifact — F1 measured the
overrun at 18 rendered lines, "if anything slightly generous to the problem."

Six rounds of non-protected trimming were attempted before stopping (compressing, then fully
cutting, the local e-value body signpost; compressing the closed form's restated counterexample
numbers into a back-reference; compressing two captions and one intro pointer; tightening float
separation glue past S5/S10's own precedent, which alone pulled the entire protected open-band
paragraph back onto page 4). Both categories the session's own brief authorized for trimming
(section-level related-work relocation, redundant appendix/body duplication) are now exhausted.
What remains is genuinely required by this session's mandate — the closed form and the results
table must sit in Section 3 by explicit instruction — against a body that had exactly zero slack
before this session began. Closing the rest of the gap would mean cutting into either the protected
proof content or the intro's independently, extensively audited prior-art paragraph, and this
session did not take that decision unilaterally, per its own escalation rule.

**The paper still builds cleanly (0 TeX errors) under the other live venue option.** Under
`dblblindworkshop` (TS-LIMITS, 4–7 pages, double-blind), a 5-page body is comfortably within
budget — verified by an isolated test build, with the committed venue switch restored to
`sglblindworkshop` immediately after and confirmed unchanged. This session's additions are
therefore fully compatible with the paper as written, provided the eventual venue decision (still
open, `docs/GATES.md` G7.7, `[OPERATOR INPUT]`) lands on TS-LIMITS, or provided a future session is
explicitly authorized to trim intro.tex's prior-art paragraph for E-values specifically.

Total pages: 13 (`sglblindworkshop`) / 12 (`dblblindworkshop`). Zero TeX errors, zero overfull
boxes (one was found and fixed this session), zero undefined references or citations, three
pre-existing underfull hboxes, both `check_hygiene.sh` and `check_prose_hygiene.sh` passing at the
current commit.

---

## Is the e-value section a genuine strengthening or decoration? An honest opinion

**Genuine strengthening of topical fit, not decoration — but a modest one, and it earns that
verdict specifically because of what C2's attack forced it to become.** A statistically literate
reviewer at a workshop titled "E-values: From Statistics to ML" will read past the disclaimer to
the substance underneath it, and the substance is real: a correctly-scoped anytime-valid test built
on a signed accumulator this paper independently proves a pathwise dichotomy for, with a worked
example computed from the paper's own frozen data rather than asserted. That is topically relevant
in the specific sense the venue cares about — it shows the paper's central object has a legitimate
e-values-adjacent reading, worked through carefully enough to survive an adversarial pass that
caught a real error (the sup-vs-limit conflation) before it could reach a reviewer.

What keeps the verdict at "modest" rather than "strong": the section's own honesty is also its
limit. It repeatedly and correctly says it is a diagnostic built on top of the result, not a
result — "no result of this paper is an e-value result or rests on one" is the section's own last
word on itself, twice over. A reviewer scoring topical fit reads that sentence too, and it caps how
much this section can move the needle: the paper's actual contribution is a tightness result for
someone else's admissible radius, proved pathwise, and this section does not and should not claim
otherwise. It is a well-built bridge to the venue's vocabulary, not a paper that happens to also
prove a conformal result. Placed in the appendix rather than the body, that is exactly the right
weight for it to carry.

---

## Days remaining before the E-values deadline

**Seven days.** Today is 2026-08-22; the E-values deadline is 2026-08-29 23:59 AoE.

---

Committed (`e9444e7`, `e1c33f2`), pushed, and this sub-session stops here. Venue, affiliation, and
author identity were not touched.
