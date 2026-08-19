# Venue analysis

Six candidates scored. All deadlines below were read from **OpenReview's own submission
invitation records** via the OpenReview API — the most canonical source available — and
cross-checked against each workshop's published call for papers. Where the two disagree,
the OpenReview record is authoritative because it is what the submission form enforces.

**The final venue choice is [OPERATOR INPUT].** This file recommends; it does not decide.
The question is stated in `docs/OPEN_QUESTIONS.md`.

---

## 0. The finding that dominates every other consideration

The ML×OR deadline is **2026-09-01 11:59 UTC**. Today is 2026-08-19. That is **thirteen
days**.

In those thirteen days the project would have to: rebuild a simulator that does not exist
(`audit/REPRO_C1.md`), freeze thirteen underdetermined modelling choices
(`audit/RECONSTRUCTION_SPEC.md` R1–R13), reproduce a table it has never run, produce the
three untabulated results the argument depends on (0 bps, 5 bps, the variance diagnostic),
implement the dead-band arm, resolve the coverage-theorem fork (`audit/CLAIMS.md` C-a),
rebuild a reference list with a 31.8 % failure rate (`audit/REFS_REJECTED.md`), and write
four pages — with operator sign-off required at three gates along the way.

**The audit's assessment is that the 2026 workshop cycle is not reachable at an acceptable
standard.** Every ranking below is therefore given twice: on merit, and on merit
conditional on the deadline being met. The operator may reasonably disagree about
feasibility — that is a judgement about available effort, not about evidence — which is
exactly why it is an operator decision. What the audit can say is that the "2 weeks, the
central experiment is already done" premise on which the 2026 target was chosen is false.

The `docs/GATES.md` STOP condition inherited from the plan matters here: if only C1
survives, a 4-page paper reporting the dissociation alone is a legitimate and much
smaller submission. It still requires the simulator.

---

## 1. Verified facts for all six candidates

| Workshop | Site | Deadline (OpenReview, UTC) | AoE equivalent | Days from 2026-08-19 |
|---|---|---|---|---|
| **EconML** | Atlanta | 2026-08-30 11:59 | Aug 29 | 11 |
| **E-values: From Statistics to ML** | Paris | 2026-08-30 13:00 | Aug 29 | 11 |
| **ML×OR (2nd)** | Atlanta | **2026-09-01 11:59** | **Aug 31** | **13** |
| **DynaFront** | Atlanta | 2026-09-05 11:59 | Sep 4 | 17 |
| **OPT 2026** | Sydney | 2026-09-05 12:00 | Sep 4 | 17 |
| **TS-LIMITS** | Paris | 2026-09-06 11:59 | Sep 5 | 18 |

Each invitation carries a 30-minute expiry buffer after the due date. **It is not a grace
period to plan around.**

Common to all six, as NeurIPS 2026 workshops: notification 2026-09-29, workshop days
December 12–13 2026 (OPT is listed as December 11 or 12), non-archival, and the NeurIPS
2026 LaTeX format.

**The style file was fetched and inspected** (see `docs/PROVENANCE.md`). From
`neurips_2026.sty` line 85:

```
\DeclareOption{sglblindworkshop}{
  \@workshoptrue
  \@anonymousfalse
  ...
```

`sglblindworkshop` sets `\@anonymousfalse` — **author names are printed**. A
`dblblindworkshop` option exists for anonymous workshops. This confirms at source level
that a `sglblindworkshop` submission is non-anonymous.

### Corrections to the planning document

- The plan gives TS-LIMITS as "**Sep 5**". Correct, as an AoE date — the OpenReview record
  is 2026-09-06 11:59 UTC, the same instant. No error.
- The plan gives TS-LIMITS as "**4–7pp**". **Not verified.** The TS-LIMITS site is
  JavaScript-rendered and its call-for-papers section could not be retrieved by any method
  available in this session. Recorded in `docs/OUTSTANDING.md`.
- The plan calls TS-LIMITS the backup venue. **That assessment does not survive contact
  with its actual scope** — see §2.3.

---

## 2. Scoring

Four axes, as specified: topical fit; reviewer expertise in conformal prediction **and**
in decision-focused learning, scored separately because no venue is strong in both;
whether a 4-page mechanism-plus-method paper is the natural unit; and downstream value.

### 2.1 ML×OR — NeurIPS 2026 Second Workshop on ML×OR (Atlanta)

*Mathematical Foundations and Operational Integration of Machine Learning for
Uncertainty-Aware Decision-Making.*

**Topical fit: good, with a real off-theme exposure.** The stated 2026 emphasis is
"decision-making with GenAI+OR", and F7 contains no generative-AI component whatsoever.
It qualifies under the broad-relevance clause — sequential and adaptive decision-making,
distributional robustness, and finance are all named — and the workshop's own title is
about *uncertainty-aware decision-making*, which is precisely what F7 is about. But a
submission that ignores the year's theme competes for slots against submissions that
serve it. This is a live risk, not a formality.

**Reviewer expertise — conformal prediction: strongest of the six.** Yao Xie is a
confirmed speaker and works directly on sequential change detection and conformal
methods. Lihua Lei, per the facts carried into this session, is on the programme
committee, and is a co-author of *Conformal Risk Control* — which the planning document
currently miscites with the wrong author order (`audit/REFS_REJECTED.md` §2.2).

**Reviewer expertise — decision-focused learning: strongest of the six, by a distance.**
Erick Delage is a confirmed speaker and co-authored *Conformal Inverse Optimization*
(NeurIPS 2024), which the plan does not cite. Nathan Kallus, David Simchi-Levi, Assaf
Zeevi, Phebe Vayanos and Benjamin Van Roy are confirmed speakers. Organizers include
Henry Lam, Jing Dong and Enlu Zhou — stochastic simulation and OR.

**This is the double-edged finding of the whole venue analysis.** ML×OR is the only room
that can properly evaluate both halves of F7 — and it is therefore the only room certain
to catch the Gârleanu–Pedersen misattribution, to know Zaffran's Theorem 3.1 by heart,
and to reconstruct the ACI telescoping argument and ask what the dead-band does to it.
Submitting an unfixed version here is worse than submitting it anywhere else.

**4-page unit: yes, and the format is unusually favourable.** Maximum 4 pages for the main
body, with "unlimited references and supplemental materials permitted beyond the page
limit". A mechanism-plus-method paper fits: mechanism and headline table in the body,
derivations and the coverage argument in an unlimited appendix. No paper checklist is
required.

**Downstream value: unique, and it is the deciding factor.** The workshop coordinates
invited post-workshop submissions to *Stochastic Systems*, *Mathematics of Operations
Research*, and *Operations Research*. **No alternative offers anything comparable.** The
2025 edition drew 147 submissions, so the audience is real and established rather than
speculative.

On the journal nomination: the working default is *Stochastic Systems*, with an upgrade
to *Mathematics of Operations Research* conditional on C2's coverage theorem being proved
rather than asserted. Given `audit/CLAIMS.md` C-a, **that upgrade should be treated as
unlikely** and the nomination planned as *Stochastic Systems*.

### 2.2 E-values: From Statistics to ML (Paris) — the genuine alternative

The instruction to give this real consideration rather than treating ML×OR as settled is
correct, and the case is stronger than the plan's one-line mention suggests. It is also
weaker than it first appears, in a way the plan gets backwards.

**Topical fit: an explicit invitation on the method, a mismatch on the object.** The
call names, verbatim, "sequential & adaptive inference (monitoring, anytime-valid
intervals, **conformal prediction**, bandits)" among its topics. F7 is a paper about
online conformal prediction, so it is unambiguously in scope — more explicitly in scope
than at ML×OR, where it enters through a broad-relevance clause.

**But the plan's claim that there is "no off-theme GenAI problem there" mis-states the
comparison.** The workshop's core object is e-values, test martingales and anytime-valid
inference. F7 uses none of that machinery: no e-value, no test martingale, no
anytime-valid construction. The mismatch is symmetric to the GenAI mismatch at ML×OR —
in-scope by an explicit topic listing, off-centre relative to what the workshop is
actually about. Neither venue is a clean thematic fit and both should be argued for, not
assumed.

**Reviewer expertise — conformal prediction: excellent, and differently so.** The
organizers are Shubhada Agrawal, Sebastian Arnold, Yo Joong Choe, **Peter Grünwald** and
**Aaditya Ramdas**. Ramdas is central to the modern conformal and betting-based
sequential-inference literature. This room would grasp a coverage-versus-decision-cost
dissociation immediately, and — more valuable than that — it is the room best equipped to
tell F7 whether the C-a coverage argument is right. Note that the closest competing
method to C2's motivation, *Adaptive Conformal Inference by Betting*
(arXiv:2412.19318), is a betting-based method and squarely in this room's territory; that
is a reason to expect a sharp review, not a reason to avoid it.

**Reviewer expertise — decision-focused learning: weak.** This is a statistics and
sequential-inference audience. The turnover mechanism, the Kelly position map and the
transaction-cost model would read as application detail rather than as the contribution.
The half of F7 that makes it *matter* is the half this room is least equipped to price.

**4-page unit: yes.** "Short papers up to 4 pages, excluding references and optional
appendices" — equivalent in practice to ML×OR's terms.

**Downstream value: no journal pathway.** Non-archival, Paris site. Audience quality is
high but narrower.

**Deadline: 2026-08-30 13:00 UTC — two days before ML×OR.** Under a feasibility
constraint this is strictly worse.

### 2.3 TS-LIMITS (Paris) — the plan's designated backup, and a mis-assessment

Full title: *Generalization for Time Series in Tight Settings: Latency, Inference,
Memory, prIvacy and susTainability.*

**Topical fit: poor.** The workshop is organised around five bottlenecks — latency,
inference cost, memory, privacy and sustainability. Every one is a **computational or
regulatory** constraint on deploying a time-series model. F7's constraint is an
**economic cost of the decision the model drives**. Those are different subjects that
share the word "cost".

The plan lists TS-LIMITS as the backup venue, presumably on the strength of the deadline
and the time-series label. On scope, it is a worse fit than E-values and than ML×OR, and
arguably no better than DynaFront. **The designation should be revisited.**

Its one genuine advantage is the calendar: 2026-09-06 11:59 UTC, five days later than
ML×OR, the latest of the six.

Page limit unverified (§1).

### 2.4 OPT 2026: Optimization for Machine Learning (Sydney)

**Topical fit: very poor.** The 2026 focus is stated as "Can Anything Beat Adam? Frontier
Optimizers", concerned with Muon, K-FAC, Shampoo and the design of neural-network
training optimizers. F7 is not about training optimizers.

There is one thin thread: online convex optimization with switching costs — the
literature F7 must now engage (`audit/PRIOR_ART.md` §4.2) — is optimization theory, and
organizers Courtney Paquette, Sebastian Stich and Frederik Kunstner are strong there. But
a paper whose contribution is a conformal coverage property would be an outlier, and
there is no conformal-prediction expertise in the room.

**Different physical site (Sydney)**, which matters for in-person presentation
requirements. Deadline 2026-09-05 12:00 UTC. No journal pathway.

### 2.5 EconML: Economics for Machine Learning (Atlanta)

**Topical fit: poor.** The workshop maps the economic consequences of machine learning's
success, spanning mechanism design, markets, incentives and alignment. F7 has a
transaction cost in it; it has no economics in the sense this workshop means. A trading
friction is not a mechanism-design contribution.

**Reviewer expertise:** economics, game theory and learning theory. Aaron Roth's presence
in this community is a thin positive — he co-authored the regret↔coverage paper F7 cites
— but it does not make the room a fit.

Note a procedural detail: the call states a **reciprocal reviewing clause** — qualified
authors may be asked to review. Deadline 2026-08-30 11:59 UTC, the earliest of the six.
No journal pathway.

### 2.6 DynaFront (Atlanta)

*Dynamics at the Frontiers of Optimization, Sampling, and Games.*

**Topical fit: poor to moderate.** Online-learning dynamics are in scope in principle,
and F7's switching-cost formulation is a dynamics question. But the 2026 emphasis is
diffusion models, distributed and adversarial training, and agentic AI. Conformal
prediction is absent from the scope.

The deadline was **extended from Aug 29 to Sep 4 AoE** (2026-09-05 11:59 UTC), which is
worth noting as evidence that workshop deadlines in this cycle do move — though none
should be planned around. No journal pathway.

---

## 3. Ranked recommendation

### On merit, deadline aside

| Rank | Venue | Reason in one line |
|---|---|---|
| **1** | **ML×OR** | The only room that can evaluate both halves of the paper, the only journal pathway, and a format that suits a 4-page mechanism-plus-method paper with an unlimited appendix. |
| **2** | **E-values** | Explicitly names conformal prediction; the best room in the world for judging whether the coverage argument is sound; but no journal pathway and it cannot price the decision-cost half. |
| 3 | TS-LIMITS | Latest deadline; weak scope match despite the time-series label. |
| 4 | DynaFront | Dynamics scope could accommodate the switching-cost framing; no conformal audience. |
| 5 | OPT 2026 | Strong on OCO theory, wrong year's focus, wrong hemisphere, no conformal audience. |
| 6 | EconML | Wrong subject. |

### Conditional on the 2026 cycle being attempted

The ordering does not change, but the gap narrows and one option is added.

- **ML×OR remains first**, because the journal pathway is worth more than two days, and
  because everything that would be written for E-values is also written for ML×OR.
- **A deliberate one-cycle deferral is a legitimate third option** and should be on the
  table explicitly rather than by default: ML×OR has run in 2025 and 2026 and is likely
  to recur; the work would be submitted complete rather than assembled in thirteen days
  around an experiment that does not yet exist; and *Stochastic Systems* accepts direct
  submissions independently of the workshop.

**Recommendation: ML×OR, with the timing decision separated from the venue decision.**
The venue question has a clear answer. The calendar question does not, and it belongs to
the operator.

---

## 4. Compliance checklist for ML×OR

Every line is a desk-rejection risk. Verified against the ML×OR call for papers, the
OpenReview submission invitation, and the fetched `neurips_2026.sty` and
`neurips_2026.tex`. Unverified items are marked.

### Submission mechanics

- [ ] Submitted via OpenReview at `NeurIPS.cc/2026/Workshop/MLxOR`.
- [ ] Submitted before **2026-09-01 11:59 UTC** (2026-08-31 AoE). The invitation expires
      at 12:29 UTC; do not treat the 30 minutes as usable time.
- [ ] Journal nomination made **at submission**: at most one of *Stochastic Systems*,
      *Mathematics of Operations Research*, *Operations Research*. Working default:
      *Stochastic Systems*.

### Format

- [ ] `\usepackage[sglblindworkshop]{neurips_2026}` — **not** `main`, **not**
      `dblblindworkshop`, and **not** with `final` (that option is for camera-ready only).
- [ ] `\workshoptitle{...}` set **in addition to** `\title{...}`. The template states
      both are required for workshop papers; the footnote track name is incomplete
      without it. This is the single most commonly missed item in the NeurIPS workshop
      format.
- [ ] Style file used verbatim as fetched (`paper/neurips_2026.sty`, SHA-256 recorded in
      `docs/PROVENANCE.md`). No margin, font-size or spacing modification of any kind.
- [ ] Main body **at most 4 pages**.
- [ ] References beyond the 4 pages — unlimited, and permitted.
- [ ] Supplementary material beyond the 4 pages — unlimited, and permitted. The coverage
      derivation and the reconstruction specification belong here.
- [ ] **No paper checklist.** ML×OR states it is not required. Do not include
      `checklist.tex` in the submission.

### Anonymity and eligibility

- [ ] Author names and affiliations **present and visible**. Submissions are
      non-anonymous, and `sglblindworkshop` sets `\@anonymousfalse` in the style file, so
      an accidental anonymisation would fight the template.
- [ ] The work is **not previously published**. The call states explicitly: "Previously
      published works, including papers accepted to and presented at this year's main
      NeurIPS conference, are not eligible."
- [ ] No overlap with a NeurIPS 2026 main-conference acceptance by the same authors on
      the same content.
- [ ] The public repository is compatible with non-anonymous submission. **If a
      double-blind venue is chosen instead, the repository must be made private before
      submission** — this reverses an operator decision already taken and must be raised
      explicitly, not done silently.

### Content integrity — the items this audit found

- [ ] Gârleanu–Pedersen is **not** cited as the source of the dead-band form.
      Constantinides (1986) and Davis–Norman (1990) are cited instead
      (`audit/REFS_REJECTED.md` §1.1).
- [ ] Conformal PID dated **2023**, not 2024.
- [ ] *Conformal Risk Control* attributed to **Angelopoulos** et al., not "Bates,
      Angelopoulos et al." — a programme-committee member is an author.
- [ ] arXiv:2502.10947 appears **once** in the reference list.
- [ ] MacLean–Thorp–Ziemba given a year and an identifier, or removed.
- [ ] Zaffran et al. Theorem 3.1 engaged **on page one**, not in related work.
- [ ] The switching-cost literature cited (Kalai–Vempala; shrinking dartboard; Andrew et
      al.; smoothed OCO) — an ML×OR audience will notice its absence.
- [ ] Conformal Inverse Optimization (Lin, **Delage** & Chan) cited. Delage is a
      confirmed speaker.
- [ ] No claim framed as an impossibility result, a coverage floor or a fundamental
      limit (`audit/PRIOR_ART.md` §6).
- [ ] No unproved theorem stated as proved (`audit/CLAIMS.md` C-a).
- [ ] Every number in the paper traceable to a `results/` JSON.

### To verify before submission — not established by this audit

- [ ] Whether ML×OR requires **in-person presentation** by at least one author in
      Atlanta. EconML states such a requirement explicitly; ML×OR's call as retrieved
      does not, and this was not confirmed either way.
- [ ] Whether ML×OR operates a **reciprocal reviewing** clause.
- [ ] Whether a preprint posted to arXiv before the deadline affects eligibility. The
      "previously published" language most naturally targets peer-reviewed publication
      rather than preprints, and the workshop is non-archival, but this was not confirmed
      and it interacts with the decision to keep the repository public.

These three are recorded in `docs/OUTSTANDING.md`.
