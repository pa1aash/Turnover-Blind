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

## Repository artefacts of record

| Artefact | Origin | SHA-256 | Note |
|---|---|---|---|
| `docs/PLAN_ORIGINAL.md` | Planning document produced in a prior session, supplied at the root of the working folder as `F7-turnover-blind-conformal.md` and moved unmodified | `c250fc99186a24b5b0eb0dfa4ada8d81e0c722e6ecfac77821535ed4e975269c` | Historical artefact. Evidence to be audited, not a specification to be trusted. Content byte-identical to the file as supplied. |

## Not yet fetched

| Artefact | Canonical source | Blocking? | Recorded in |
|---|---|---|---|
| NeurIPS 2026 LaTeX style files (`neurips_2026.sty` and the `sglblindworkshop` option) | The NeurIPS 2026 author-kit distribution linked from the workshop / conference site | Blocks G5, not G0 | `docs/OUTSTANDING.md` |

## Facts carried in from external verification

The following were verified outside this repository on 2026-08-19 and are treated as
established inputs rather than re-derived here. They are restated in
`docs/G0_REPORT.md` and used throughout the audit.

- The Conformal Kelly preprint (arXiv:2608.01494) exists, is single-author and
  unrefereed, and does report the 0.7–5.3 point growth cost of faster adaptation.
- That preprint's configuration is a 75% interval on a 2016–2021 development window.
- The NeurIPS 2026 ML×OR workshop is real and accepted, with the deadline, page limit
  and anonymity regime recorded in `docs/VENUE.md`.
