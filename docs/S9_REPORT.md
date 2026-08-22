# S9 report — the theoretical elevation

**Session S9, 2026-08-22.** Working folder `~/Desktop/Turnover-Blind`, branch `main`. Wave 0
preflight, four sub-sessions (A–D), one orchestrator-applied consistency wave, three commits
(`c830909`, `f2c1ef7`, `95b59e6`).

---

## The single most important sentence

**The proof split cleanly into two directions with two different scopes: necessity — losing
coverage past the boundary — is now proved over the entire admissible class with no
restriction at all; sufficiency — retaining coverage inside it — is also proved over the
entire admissible class, but the two directions meet with no gap, giving a genuine
if-and-only-if, only on a real, bounded sub-class (constant scorecaster, a saturator that
attains its extremes at the condition-(4) radius); outside that sub-class, for a genuinely
time-varying scorecaster, there is an open band where neither direction is currently
established.** The paper's original unrestricted general claim — as it read before this
session, with no such restriction stated — is **false**: it was independently falsified twice,
once by the sub-session that drafted the proof and once more by the sub-session that attacked
it, using three separate constructions, one of which is now printed in the paper's own new
Table 2. This is not a hedge and not a partial success dressed up — it is a precise, checked
result, and it is stronger than what the paper had before on both counts that matter: the
necessity direction, which the paper's original text also asserted but only ever tested at one
point, is now a real theorem over the whole class; and the previously-invisible mirror boundary
(coverage failing from *below*, not just above) turns out to already be sitting, measured, in
this project's own committed results from six days ago.

---

## The proposition, as it now stands in the paper (`paper/sections/forfeit.tex`)

Write $A^{\pm}_t = \sup_x r_t(x)$ / $\inf_x r_t(x)$ for the saturator's actual extremes, and
$\Lambda^{+}_t = \inf_{x \ge c\,h(t)} r_t(x)$, $\Lambda^{-}_t = \sup_{x \le -c\,h(t)} r_t(x)$ for
the levels condition (4) *guarantees* the saturator reaches once the accumulator clears the
radius — condition (4) says exactly $\Lambda^{+}_t \ge b$, $\Lambda^{-}_t \le -b$, and nothing
about $A^{\pm}_t$ at all; that a saturator's *attained* extreme equals its *guaranteed* reach
is an extra hypothesis condition (4) does not supply. Define

$$\tau^{\star\pm} = \sup_t\big(|A^{\pm}_t| \pm \hat q_{t+1}\big) - b/2, \qquad \sigma^{\pm} = \inf_t\big(|\Lambda^{\pm}_t| \pm \hat q_{t+1}\big) - b/2.$$

- **Failure, over the whole admissible class, no restriction:** if $\tau > \tau^{\star+}$, every
  round loses coverage against the paper's specified adversary; if $\tau \ge \tau^{\star-}$,
  every round loses coverage against the mirror legal adversary $s_t \equiv -b/2$. Neither
  direction requires $\hat q$ constant, the saturator's extremes attained anywhere, or
  $A^{\pm}_t$ finite beyond what condition (4) already forces.
- **Retention, over the whole admissible class, keyed to the guaranteed reach rather than the
  supremum:** if $\tau \le \sigma^{+}$ and $\tau < \sigma^{-}$, coverage is retained against
  *every* legal adapted adversary, and Proposition 2's own bound $|E_T| \le c\,h(T)+1$ is
  retained verbatim, not merely the weaker $o(T)$.
- **The sharp iff, on the sub-class the five originally tested settings all inhabit:** if
  $\hat q_t \equiv \hat q$ is constant and $\Lambda^{\pm}_t = A^{\pm}_t$ (the saturator attains
  its extremes exactly where condition (4) puts them, at every $t$), the two boundaries
  coincide ($\sigma^{\pm} = \tau^{\star\pm}$) and coverage is retained against every legal
  adapted adversary **if and only if** $\tau \le \tau^{\star+}$ and $\tau < \tau^{\star-}$. For a
  symmetric saturator this collapses to one line: coverage iff $\tau \le \sup_x r_t(x) - b/2 -
  |\hat q|$, with the endpoint included only when $\hat q < 0$.

## How the two degenerate cases were handled

**$\tau^{\star+} = \infty$ (unbounded saturator):** an infinite supremum is *not* on its own
enough — a legal saturator with $r_t(x) = x$ for $|x| > t^2$ also has no finite supremum but
fails at $\tau = 1.5$, because its supremum sits on a set the accumulator's own dynamics never
reach. What the tangent integrator (which the Conformal PID literature reports using in all its
own experiments) actually has, and the unreachable-supremum construction does not, is a genuine
*reach*: $\Lambda_t(X) = \tan(\arctan(b)\,X/(c\,h(t)))$, giving a finite accumulator level
$\kappa(\tau)\,c\,h(t)$, $\kappa(\tau) = \arctan(b/2+\tau-\hat q)/\arctan(b)$, at which the
deployed threshold is forced to the boundary — finite at every finite $\tau$, so coverage really
is retained at every width, as measured. But $\kappa(\tau) > 1$ once $\tau > b/2 + \hat q$, so
Proposition 2's *rate constant* (not coverage itself) is genuinely forfeited past that point —
measured directly: at $\tau=1.5$, $T=10^6$ the excursion is $15.10$ against Proposition 2's own
$14.8155$ and against the corrected $\kappa(1.5)\,c\,h(T)+1 = 15.8530$.

**$\tau^{\star+} = 0$ (forced $\hat q \equiv -b/2$):** since $\sup_t \hat q_t = -b/2$ and every
$\hat q_t \ge -b/2$ forces $\hat q_t = -b/2$ at *every* $t$ (not just a boundary artifact of
evaluating the formula), the failing set is absorbing from round 1 with no transient — every
positive $\tau$ fails, confirmed directly from the recursion's first step, not by evaluating the
boundary formula at its own edge.

## The tie case, $\tau = \tau^\star$

Not a residual convention-dependence, and not simply resolved either — genuinely more subtle
than either. The paper's own already-published Appendix A measurement ("the strict indicator
covers, scoring the exact play as a miscoverage does not") turned out, on the attacking
sub-session's re-derivation, to describe a real fact but not the one it looked like: the
"$0.000000$" reading at the tie is $|E_T| = \alpha T$ under the *mirror* adversary's error
process, which is bit-for-bit the same quantity as the paper's own `exact_threshold_strict`
regime already measures — not evidence that the endpoint "covers" in any adversary-general
sense. Once this is untangled: at the paper's own baseline setting (null scorecaster, standard
saturator), $\tau^{\star+} = \tau^{\star-} = 1$ exactly — the endpoint is **simultaneously the
closed upper boundary and the open lower one**, so the specified adversary covers there and the
mirror adversary does not, both true at once, and Appendix A's original two numbers ($0.000000$
and $1.000000$) are both correct, just describing two different adversaries rather than two
conventions for one. Where the two boundaries genuinely separate (any setting with $\hat q \ne
0$ or an asymmetric saturator), the tie is no longer a single point and the question dissolves:
$\tau^{\star+}$ and $\tau^{\star-}$ are just two different numbers, each with its own ordinary
(non-tied) closed/open status, independently derivable from the proof — not convention-dependent
at all in that regime. The one place a genuine, unresolved fork remains: if a saturator's
supremum is *approached but never attained* (as opposed to attained-but-only-in-the-limit), the
tie can fail under the strict indicator even though the attained-extreme case's tie provably
covers — this is a real, narrow residual, stated as such in the paper, not smoothed over.

## The new numerical stress tests (B5/C3), now `Table~\ref{tab:stress}` in the paper

Thirteen new rows, none among the original five settings, run through a newly-committed
`src/boundary_stress.py` (imports `src/forfeit.py` unmodified; self-validates with 19 exact
reproductions of the already-committed harness numbers before running anything new) against a
newly-committed `results/boundary-stress-20260822T103716Z-cd208b98.json`, under *both* legal
adversaries (the paper's specified one and the mirror). Highlights, all traced to that file:

- A saturator satisfying condition (4) but with $\sup_x r_t = 10b$ living outside where the
  dynamics ever go: printed $\tau^\star = 19$, proved window only $\tau < 1$; at $\tau = 1.001$
  — inside the old, unrestricted formula's claimed safe region — miscoverage is $1.000000$.
  This is the cleanest falsification of the paper's original prose, now in the paper itself as
  the demonstration of exactly why the correction was necessary.
- The power-of-two scorecaster ($\hat q_t = b/2$ on $t$ a power of two, $0$ elsewhere — legal,
  predictable, genuinely time-varying): at $\tau = 1.9$ the miscoverage rate reads $0.110960$,
  barely above $\alpha = 0.1$ and easy to mistake for coverage, while $\max_t|E_t| = 84{,}745.70$
  — the paper now states explicitly that the correct failure criterion is $|E_T|$ growing
  unboundedly, not the miscoverage rate, which stops being a reliable tell once $\hat q$ varies.
- A constant interior scorecaster $\hat q \equiv +0.4$ under the paper's own clipped saturator:
  covers under the specified adversary up to $\tau = 0.599$ (inside the proved window,
  $\tau < 0.6$) and *also* under the mirror adversary at that width, but at $\tau = 0.8$ — still
  inside the old formula's claimed safe region of $\tau^\star = 1.4$ — the mirror adversary
  already returns $0.000000$ with $|E_T| = 10{,}000 = \alpha T$, exhibiting the mirror-boundary
  failure directly.

## Page-budget consequence, flagged for S11 (not addressed this session, per this session's own instructions)

The body grew from a clean 4 pages (S8's endpoint) to roughly 5.5–5.6 pages: verified by the
opened-page method, not by trusting `pdfinfo`'s total. Page 6 opens with Related Work and
Limitations, and the References heading starts partway down that same page rather than on a
fresh one. Total document length is now 10 pages (References run pages 6–8, Appendix A pages
8–9, Appendix B alone on page 10 after a forced page break). This is expected and was not
compressed, hedged around, or avoided in order to fit — per this session's explicit brief, "do
not let a page-budget worry cause this session to weaken, hedge, or avoid stating a true
general result." Sub-session C's own output flags three specific, cheap appendix-relocation
options that would recover space without compressing any mathematics, left for S11 to apply
(or not) as part of that session's reframing work. Separately: the paper currently declares
itself under the E-values track (`sglblindworkshop`, 4-page ceiling) with a comment noting the
TS-LIMITS option (4–7 body pages) as the other live choice; at ~5.5–5.6 pages the body already
fits TS-LIMITS as-is. **This venue implication is surfaced here for the record, not decided —
venue remains a frozen field this session did not touch, and any change to which option is
active is explicitly [OPERATOR INPUT] / S11's concern, not this session's.**

## Two things this session found and fixed itself, beyond the brief's four waves

Sub-session D's mechanical integration check (Sonnet, no mathematical judgment) flagged, but
was not authorized to fix, two staleness issues the theorem rewrite left behind — one of them a
direct self-contradiction inside the paper. Because leaving a self-contradicting paper is a
correctness failure squarely inside this session's mandate (not a page-fit concern deferred to
S11), these were corrected directly after D's pass, verified by a full rebuild, and committed
separately (`95b59e6`):

1. `limitations.tex` claimed "the evidence is one construction, one adversary, one saturator" —
   false the moment Table 2 exists (13 configurations, two adversaries). Replaced with an
   accurate statement of the actual remaining limitation (the open band for time-varying
   $\hat q$).
2. `limitations.tex`'s falsification-condition sentence ("what would overturn the claim is a
   legal pair with $\tau \le \tau^\star$ that loses coverage... the sweep has neither") was
   **directly contradicted** by the paper's own new Table 2, which exists specifically to
   exhibit such pairs. Replaced with an honest statement of what is genuinely still open.
3. `appendix.tex`'s Table 3 caption said the admissible set was "measured here to be tight";
   updated to "proved here to be tight" to match the status upgrade.

**Not fixed, flagged only, left for a future session:** `docs/FRAMING.md` and `docs/GATES.md`
(especially gate G7.9, which records the old single-sided "19 of 19, no counterexample" framing
and now materially understates what the paper proves) carry the same kind of staleness at much
larger scale. Touching either file triggers `tools/check_claim_drift.sh` and this project's
gate-integrity conventions, which this session's brief did not authorize it to act on — this is
real drift, not invented busywork, and whoever next touches `docs/GATES.md` should reconcile
G7.9 (and neighboring entries) against `paper/sections/forfeit.tex`'s new Section 3 before
signing anything.

---

## Is this strong enough to justify leading with it in S11's reframing?

**Yes, and it is a stronger result than a straightforward "the general claim held" outcome would
have been.** A clean, unrestricted general theorem would have been a nice confirmation of
existing prose. What this session actually produced is more interesting on its own mathematical
merits: it found the paper's original general statement was false, located exactly why (three
independent, now-explicit reasons — unreached suprema, sup-vs-inf on a time-varying scorecaster,
and a previously invisible mirror boundary), proved a corrected and *sharper* two-sided theorem
that is a strict superset of what the paper's original single-point evidence supported, and
found that the "extra" mirror-boundary evidence needed to demonstrate the correction was already
sitting in this project's own six-day-old committed results, unused. That is a genuine
theoretical elevation, precisely and honestly scoped, not a partial or hedged one — the honest
scope statement (sharp iff only on the constant-$\hat q$/attained-extremes sub-class; an open
band otherwise) is not a weakness to apologize for in S11's reframing, it is the actual finding,
and it is checkable by exactly the equations and Table 2 rows printed in the paper.

---

Committed (`c830909`, `f2c1ef7`, `95b59e6`) and pushed. Nothing was submitted. Venue,
affiliation, and author identity were not touched.

**7 days remain before the E-values submission deadline** (2026-08-29 AoE, as of this
session's date, 2026-08-22).
