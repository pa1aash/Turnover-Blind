# Provenance

Every third-party text in this repository is fetched from a canonical source and
recorded here with the URL, the retrieval date and a SHA-256 of the bytes as
retrieved. Canonical third-party text — licences, venue style files, published
tables, bibliography entries — is never written from memory.

Session dates are recorded as the operator's working date for the session.

## Fetched artefacts

| Artefact | Canonical source | Retrieved | SHA-256 of retrieved bytes | Local modification |
|---|---|---|---|---|
| `LICENSE` | `https://raw.githubusercontent.com/spdx/license-list-data/main/text/MIT.txt` (SPDX license-list-data, `MIT.txt`) | 2026-08-19 | `b05785f9f18e6716bab63424b11454513b9943a222595b70411009202fc592b5` | The placeholder line `Copyright (c) <year> <copyright holders>` replaced by `Copyright (c) 2026 Palaash Gang`. No other change. |
| `paper/neurips_2026.sty` | `https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip`, linked from the NeurIPS 2026 Call for Papers as "Paper template" | 2026-08-19 | archive `82473931e3ef710fcd3f4a8cd4119b9de32e56825f90f9e5a6d55f2d01b817d9`; extracted file `c3fc2894e83d2517ca18b66741d6c595986d97957dc08ec08bb2125a7ec4555a` | None. Copied verbatim from the archive. |
| `paper/neurips_2026.tex` | same archive | 2026-08-19 | `cf4cee7991665306d1daaa3985be4feec7f8889d6d072ffa12f99a8e1537d797` | None. Copied verbatim. Retained as the template's own usage documentation. |
| `paper/checklist.tex` | same archive | 2026-08-19 | `780ba13c480f652dcc42e69ed61a752ce0ea270f15d332d4a45b059dabad84f6` | None. Copied verbatim. **Not to be included in an ML×OR submission** — that workshop states no checklist is required. |

## Repository artefacts of record

| Artefact | Origin | SHA-256 | Note |
|---|---|---|---|
| `docs/PLAN_ORIGINAL.md` | Planning document produced in a prior session, supplied at the root of the working folder as `F7-turnover-blind-conformal.md` and moved unmodified | `c250fc99186a24b5b0eb0dfa4ada8d81e0c722e6ecfac77821535ed4e975269c` | Historical artefact. Evidence to be audited, not a specification to be trusted. Content byte-identical to the file as supplied. |

## Verified from the fetched style file

`neurips_2026.sty` line 85 declares:

    \DeclareOption{sglblindworkshop}{
      \@workshoptrue
      \@anonymousfalse
      ...

so the `sglblindworkshop` option used by both ML×OR and the E-values workshop sets
`\@anonymousfalse` — **author names are printed**. A separate `dblblindworkshop` option
exists for anonymous workshops. `neurips_2026.tex` further states that for workshop
papers "both `\title{}` and `\workshoptitle{}` are required".

## Not yet fetched

| Artefact | Canonical source | Blocking? | Recorded in |
|---|---|---|---|
| TS-LIMITS call-for-papers detail (page limit, anonymity, archival status) | `https://ts-limits.github.io/` — JavaScript-rendered; no method available in this session retrieved the call text | Blocks nothing at G0; blocks a TS-LIMITS submission | `docs/OUTSTANDING.md` |
| Forward-citation list of Gibbs & Candès ACI | Semantic Scholar graph API (HTTP 429 throughout this session; needs an API key) | **Blocks G1** — it is the prior-art screen most likely to surface a scoop | `docs/OUTSTANDING.md` |

## Facts carried in from external verification

The following were verified outside this repository on 2026-08-19 and are treated as
established inputs rather than re-derived here. They are restated in
`docs/G0_REPORT.md` and used throughout the audit.

- The Conformal Kelly preprint (arXiv:2608.01494) exists, is single-author and
  unrefereed, and does report the 0.7–5.3 point growth cost of faster adaptation.
- That preprint's configuration is a 75% interval on a 2016–2021 development window.
- The NeurIPS 2026 ML×OR workshop is real and accepted, with the deadline, page limit
  and anonymity regime recorded in `docs/VENUE.md`.
