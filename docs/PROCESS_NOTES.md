# Process notes

Short, binding, and about how this project works rather than what it claims. One rule so far.

---

## 1. The claim-drift check runs before every commit that touches FRAMING or GATES

> **The last step of every wave that touches `docs/FRAMING.md` or `docs/GATES.md` is a run
> of `tools/check_claim_drift.sh` before that wave's commit. This is binding on every future
> session on this project.**

Run it as `sh tools/check_claim_drift.sh <SESSION_TAG>` (e.g. `S5`). It exits non-zero on any
finding. A finding is not a reason to stop: it is a reason to look. Either fix the tracked
document in the session that produced the contradiction, or record the disposition in that
wave's patch log with a reason. **What is not permitted is committing past a finding without
either.**

### Why the rule exists

Three consecutive sessions shipped a load-bearing claim in a **tracked** document that a
**gitignored** `research/` artefact *from the same session* already contradicted. Each time a
critic caught it late, or the next session did.

1. **S1 (2026-08-19) — the synthesis missed its own agent.** Agent A6 had the reduction to
   Conformal PID Theorem 1 in its `citable_as` field. S1's synthesis did not absorb it, and S2
   had to rediscover it from scratch. The evidence was in the repository the whole time.
   Locators: `docs/FRAMING.md:152`, `:518-520`; `research/S1/A6-postprocessing-coverage.json`.

2. **S2 (2026-08-19) — a conservation law reached four tracked files on two agents agreeing.**
   Two agents derived it independently and without contact, which was taken as corroboration.
   This project's own adversarial critic withdrew it **four hours after it was written**. Two
   agents agreeing was evidence the derivation was *easy*, not that it was *deep*.
   Locators: `docs/FRAMING.md:31`, `:143`, `:188`, `:247`.

3. **S3 (2026-08-20) — a falsified claim survived in the two governing documents.** Wave 2's
   own H6 agent falsified R3c's last disconnected cell — Semantic Scholar's citations endpoint
   for `kalai2005lazy` returns 875 citing works, three of them online conformal, one of which
   this paper already cites. The paper text was fixed; `docs/FRAMING.md` and `docs/GATES.md`,
   **both written that same session**, kept asserting the falsified version. The tokens `H6`,
   `875` and `Kalai` returned **zero hits across all of `docs/`**. Booked as `O51`.
   Locators: `docs/S3_REPORT.md:95-99`; `docs/OUTSTANDING.md` O51; `docs/GATES.md` G7.10.

That third catch is the whole method: three tokens, grepped, finding zero support where there
should have been some. The script does exactly that and nothing cleverer.

### What the check does and does not do

It indexes what the session **wrote** — agent JSONs, checkpoints, `results/` — and deliberately
excludes fetched third-party page and PDF text (`records/`, `ft/`, `raw/`, `txt/`). Those are
evidence the session *gathered*, not claims the session *made*, and including them puts
hundreds of megabytes in the way of a check that should take a second.

It then pulls the lines from the two governing documents that name the session and carry a
verdict word or a number — lines presenting themselves as freshly established now — takes up to
four distinctive tokens from each, and reports `UNSUPPORTED` (no same-session artefact carries
the token) or `CONTRADICTED` (an artefact carries it beside a falsifying word).

Lines that announce their own supersession are skipped. This project deliberately never deletes
history, so without that filter the check drowns in its own archive.

**It is a smoke alarm, not a proof.** False positives are expected and are cheap. It will not
catch a claim whose contradiction was never written down, and it cannot judge whether a number
is *right* — only whether the session's own record says something different. `docs/GATES.md`
G7.1 (every printed number traces to a `results/` JSON) is the separate check for that, and the
two are not substitutes.

### What it found on its first live run, 2026-08-20

It fired once, against session S4's own wave-1 and wave-2 output, before that wave committed.

**One finding, and it was partly real.** `docs/FRAMING.md` §2.2b item (iii) asserted that
*"Placement A does not lose coverage"* is "narrowed, not withdrawn: it holds for nine of ten
smoothed arms at 0.099940–0.100060, and it fails for a dead band with `τ > b/2`". Two defects,
neither of which any agent had reported:

1. `τ > b/2` is the null-scorecaster corner, not the law — a residue of the same drift `O51`
   documents, still live in the governing document three sessions later.
2. **The whole sentence was scoped to the null scorecaster and said so nowhere.** The
   nine-of-ten count is a count at `q̂ ≡ 0`; the paper's Table 1 now lists eleven arms; and at
   the equally legal `q̂ ≡ −b/2` the partial-adjustment arm at `w = 0.999` **also** returns
   `1.000000`. An unscoped "nine of ten smoothed arms cover" is too strong.

Both are fixed in place, and the surviving claim is stated more narrowly: no readout is safe by
construction, and what is tight is the radius rather than either form.

**The alarm still fires on that line after the fix, and that is recorded rather than silenced.**
The matcher pairs a numeric token with any falsifying word on the same artefact line, and the
artefact line legitimately contains the phrase *"refutes 'L2 retains the bound'"* — it is
**reporting** a refutation of a different claim, not contradicting the tracked one. The tool
cannot tell those apart and deliberately does not try. The disposition is recorded in
`research/S4/patch-log.json`, which is what the rule requires when a finding is a false
positive. Making the matcher cleverer would trade the property that makes it trustworthy —
that it is fifty lines anyone can read in a minute — for a heuristic nobody would audit.

**The rule paid for itself on its first run.** An under-scoped load-bearing claim in the
governing document was caught and fixed *inside the session that wrote it*, rather than by the
next session's critic. That is precisely the failure S1, S2 and S3 each committed.
