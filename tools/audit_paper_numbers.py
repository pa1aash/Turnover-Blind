#!/usr/bin/env python3
r"""
audit_paper_numbers.py -- numeric provenance audit for the Turnover-Blind paper.

Written for session S5 sub-session A (the numeric provenance audit).

WHAT IT DOES
------------
1. Reads the paper's LaTeX sources and STRIPS every "%" comment.  paper/main.tex
   and paper/sections/setup.tex carry multi-page comment headers stuffed with
   numbers that are never typeset; counting those would swamp the audit.  The
   comment-stripped files are then JOINED into one string per file so that a
   \citep{...} group broken across a %-continued line is still seen as one
   command when the context of a token is examined.
2. Tokenises every numeral that survives in the BODY text.  It understands
   plain decimals, LaTeX thousands separators ($28{,}311$), LaTeX scientific
   notation ($10^{6}$, $2{\times}10^5$, $10^{-9}$), percentages and ratios.
3. Classifies each token against an EXPLICIT ALLOW-LIST of structural numbers
   (section / table / equation / theorem locators, page numbers, years, arXiv
   ids, and the Setup harness constants alpha = 0.1, b = 2, c = 1) which are
   configuration or cross-references rather than measurements.  Every exclusion
   records which allow-list rule fired.
4. Consults an explicit DERIVATIONS table for numbers that are exact arithmetic
   of two or more sourced numbers (e.g. 19 = 5 settings x 3 widths + 4 wide
   bands).  Those are reported DERIVED with the derivation spelled out.
5. For every remaining token, searches results/*.json for a leaf that matches AT
   THE PRINTED PRECISION and reports file + full field path.  Matches are
   ranked: TIER 1 = config / aggregate_table / rows / horizons_raw scalars,
   which is where reported quantities live; TIER 2 = arms_raw[*].trace.*, the
   512-point sampled traces, where a rounded decimal can collide by accident, so
   a TIER-2-only match is reported as WEAK.  Identifier strings (arm and
   variation names such as deadband_tau1.5, ema_w0.999, saturator_level_4b) are
   indexed too, so configuration LABELS resolve to the run that defines them.
6. Anything left over is reported UNSOURCED.

USAGE
    python3 tools/audit_paper_numbers.py [--repo <path>] [--json <out.json>]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import OrderedDict

# ---------------------------------------------------------------------------
# 0.  The three results/ files the paper declares as its sources
# ---------------------------------------------------------------------------
DECLARED = [
    "forfeit-20260820T063045Z-83747c45.json",       # primary
    "forfeit-20260820T063132Z-83747c45.json",       # tau-cliff
    "forfeit-variations-20260820T101445Z.json",     # variations
]

# ---------------------------------------------------------------------------
# 1.  COMMENT STRIPPING
# ---------------------------------------------------------------------------

def strip_tex_comments(text):
    """Return (joined_body, line_of_offset, n_comment_lines)."""
    pieces, linemap, n_comment = [], [], 0
    pos = 0
    for i, line in enumerate(text.split("\n"), start=1):
        body, j, stripped = [], 0, False
        while j < len(line):
            ch = line[j]
            if ch == "\\" and j + 1 < len(line):
                body.append(line[j:j + 2]); j += 2; continue
            if ch == "%":
                stripped = True; break
            body.append(ch); j += 1
        if stripped:
            n_comment += 1
        s = "".join(body) + "\n"
        pieces.append(s)
        linemap.append((pos, pos + len(s), i))
        pos += len(s)
    return "".join(pieces), linemap, n_comment


def offset_to_line(linemap, off):
    for a, b, ln in linemap:
        if a <= off < b:
            return ln
    return linemap[-1][2]


# ---------------------------------------------------------------------------
# 2.  TOKENISER
# ---------------------------------------------------------------------------

NUM_RE = re.compile(
    r"""
      (?P<sci>\d+(?:\.\d+)?\s*(?:\{\s*\\times\s*\}|\\times|\\cdot)\s*10\^\{?-?\d+\}?)
    | (?P<pow>10\^\{?\s*-?\d+\s*\}?)
    | (?P<thou>\d{1,3}(?:\{,\}\d{3})+)
    | (?P<pct>\d+(?:\.\d+)?\s*\\%)
    | (?P<dec>\d*\.\d+)
    | (?P<int>\d+)
    """,
    re.VERBOSE,
)


def parse_token(kind, raw):
    """(value, half_ulp_tolerance, printed_decimals)."""
    s = raw.strip()
    if kind == "sci":
        m = re.match(r"(\d+(?:\.\d+)?)\s*(?:\{\s*\\times\s*\}|\\times|\\cdot)\s*10\^\{?(-?\d+)\}?", s)
        mant, ex = m.group(1), int(m.group(2))
        d = len(mant.split(".")[1]) if "." in mant else 0
        return float(mant) * 10.0 ** ex, 0.5 * 10.0 ** (ex - d), d
    if kind == "pow":
        ex = int(re.match(r"10\^\{?\s*(-?\d+)\s*\}?", s).group(1))
        return 10.0 ** ex, 0.5 * 10.0 ** ex, 0
    if kind == "thou":
        return float(s.replace("{,}", "")), 0.5, 0
    if kind == "pct":
        num = re.match(r"(\d+(?:\.\d+)?)", s).group(1)
        d = len(num.split(".")[1]) if "." in num else 0
        return float(num), 0.5 * 10.0 ** (-d), d
    if kind == "dec":
        d = len(s.split(".")[1])
        return float(s), 0.5 * 10.0 ** (-d), d
    if kind == "int":
        return float(s), 0.5, 0
    return None, None, None


# ---------------------------------------------------------------------------
# 3.  ALLOW-LIST -- structural, not measured.  Recorded verbatim in the output.
# ---------------------------------------------------------------------------

ALLOWLIST_RULES = OrderedDict([
    ("A1-cross-reference-command",
     "The numeral is inside the argument of, or the bracketed locator of, a "
     "LaTeX cross-reference or citation command (\\ref, \\eqref, \\label, "
     "\\cite*, \\citep[Corollary~2]{...}, \\citeauthor).  Includes the year "
     "digits of BibTeX keys such as li2025o2cp."),
    ("A2-numbered-object-locator",
     "The numeral immediately follows a numbered-object word -- Section, Sec., "
     "Table, Figure, Equation, Eq., Theorem, Thm, Proposition, Prop., "
     "Corollary, Cor., Lemma, Appendix, condition, iteration, Placement -- or "
     "a bare \\S, or is a parenthesised equation number such as (4)/(5)."),
    ("A3-page-number",
     "The numeral is introduced as a printed page number ('printed page 18443')."),
    ("A4-year",
     "A four-digit 1900-2099 integer used as a calendar year or part of a date."),
    ("A5-arxiv-identifier",
     "An arXiv-style identifier NNNN.NNNNN with or without a version suffix."),
    ("A6-harness-constant",
     "A harness CONFIGURATION constant stated in Setup -- alpha = 0.1, b = 2, "
     "c = 1, mu_t = 1 -- together with the definitional literals of "
     "h(t) = log(t+2), the saturator clip(x/(c h(t)), -1, 1), the score bound "
     "b/2, and the sign/limit literals of err_t = 1{...}.  Configuration and "
     "definitions, not results."),
    ("A7-symbolic-index",
     "The numeral is a subscript, superscript, summation limit or algebraic "
     "literal inside a symbolic expression -- E_t, q_{t+1}, L_1/L_2, "
     "sum_{i <= t}, 1 - alpha, (1 - w), 1 - lambda, O(1/log T), |E_T| <= c h(T) "
     "+ 1 -- rather than a reported quantity."),
    ("A9-package-option",
     "The numeral is part of a \\documentclass / \\usepackage option or style "
     "file name (utf8, T1, neurips_2026).  Typesetting configuration."),
    ("A8-latex-length",
     "The numeral belongs to a LaTeX length, column specification or font / "
     "spacing declaration (\\setlength, \\tabcolsep 4.5pt, p{3.35cm})."),
])

STRUCT_WORDS = (r"Section|Sec\.|Sections|Table|Tables|Figure|Fig\.|Equation|Eq\.|Eqs\.|"
                r"Theorem|Thm\.?|Proposition|Prop\.?|Corollary|Cor\.?|Lemma|Appendix|"
                r"condition|iteration|item|step|Placement|Claim|Remark|Definition")


def classify_structural(text, start, end, raw, value):
    pre = text[max(0, start - 220):start]
    post = text[end:end + 60]
    ctx = " ".join(text[max(0, start - 70):end + 40].split())

    if re.search(r"\\(?:usepackage|documentclass|RequirePackage|LoadClass)(?:\[[^\]]*)?[^\n]*$", pre[-90:]):
        return "A9-package-option", ctx
    if re.search(r"\\setlength|\\tabcolsep|\\arraystretch|\\hspace|\\vspace", pre[-60:]):
        return "A8-latex-length", ctx
    if re.search(r"p\{\s*$", pre) or re.match(r"^\s*(cm|pt|em|ex|in|mm)\b", post):
        return "A8-latex-length", ctx

    # inside a \cite.../\ref.../\label... brace group (may span %-joined lines)
    if re.search(r"\\(?:ref|eqref|label|pageref|cite[a-zA-Z]*)(?:\[[^\]]*\])*\{[^{}]*$", pre, re.S):
        return "A1-cross-reference-command", ctx
    if re.search(r"\\cite[a-zA-Z]*\[[^\]]*$", pre, re.S):
        return "A1-cross-reference-command", ctx
    if re.search(r"\\citeauthor\{[^{}]*$", pre, re.S):
        return "A1-cross-reference-command", ctx

    if re.search(r"(?:" + STRUCT_WORDS + r")[~ ]*\(?~?$", pre):
        return "A2-numbered-object-locator", ctx
    if re.search(r"\\S~?$", pre) or re.search(r"\\S\\ref\{[^}]*$", pre):
        return "A2-numbered-object-locator", ctx
    if raw in ("4", "5") and re.search(r"\(\s*$", pre) and re.match(r"^\s*\)", post):
        return "A2-numbered-object-locator", ctx

    if re.search(r"\bpages?\b[^.]{0,25}$", pre, re.I):
        return "A3-page-number", ctx

    if re.search(r"arXiv[: ]*[\d.]*$", pre, re.I) or re.match(r"^\d{4}\.\d{4,5}$", raw):
        return "A5-arxiv-identifier", ctx

    if re.match(r"^\d{1,2}$", raw) and re.match(
            r"^\s*(?:January|February|March|April|May|June|July|August|September|"
            r"October|November|December)\b", post):
        return "A4-year", ctx
    if re.match(r"^\d{4}$", raw) and 1900 <= value <= 2099:
        if re.search(r"(?:January|February|March|April|May|June|July|August|September|"
                     r"October|November|December)\s+\d{0,2}\s*$", pre) or \
           re.search(r"\b(?:in|on|from|since|of)\s*$", pre):
            return "A4-year", ctx

    # harness constants and definitional literals
    if re.search(r"\\alpha\s*=\s*$", pre):
        return "A6-harness-constant", ctx
    if re.search(r"(?<![A-Za-z])[bc]\s*=\s*$", pre):
        return "A6-harness-constant", ctx
    if re.search(r"\\mu_t\s*=\s*$", pre):
        return "A6-harness-constant", ctx
    if raw == "2" and re.search(r"(?:b|\\tau|\\hat\{q\}(?:_t)?|q|x|T|t|H)\s*/\s*$", pre):
        return "A6-harness-constant", ctx
    if re.search(r"\\log\(\s*t\s*\+\s*$", pre):
        return "A6-harness-constant", ctx
    if re.search(r"\\mathrm\{clip\}\(|\\mathrm\{err\}|\\mathbf\{1\}\\?\{|\\mathrm\{clip\}", pre[-60:]):
        return "A6-harness-constant", ctx
    if re.search(r"\\pm\s*$", pre) and raw in ("1", "2"):
        return "A6-harness-constant", ctx

    # symbolic indices / algebraic literals
    if re.search(r"(?:_|\^)\s*\{?\s*[-+]?\s*$", pre):
        return "A7-symbolic-index", ctx
    if re.search(r"\\sum_\{[^{}]*$", pre, re.S) or re.search(r"\\le\s*t\s*$", pre):
        return "A7-symbolic-index", ctx
    if value is not None and abs(value) <= 2 and re.search(r"[-+]\s*$", pre) and \
            re.search(r"[A-Za-z}\)]\s*[-+]\s*$", pre):
        return "A7-symbolic-index", ctx
    if value is not None and abs(value) <= 2 and re.search(r"[-+(]\s*$", pre) and \
            re.match(r"^\s*[-+]\s*[\\A-Za-z]", post):
        return "A7-symbolic-index", ctx
    if re.search(r"[Oo]\(\s*1?\s*/?\s*$", pre) and value in (0.0, 1.0):
        return "A7-symbolic-index", ctx
    if re.search(r"\\(?:downarrow|uparrow|to|rightarrow)\s*$", pre):
        return "A7-symbolic-index", ctx
    # \mathbf{1} in err_t = 1{...} is a definitional indicator; \mathbf{0.100004}
    # in a table cell is a MEASUREMENT set in bold and must still be sourced.
    if re.search(r"\\mathbf\{\s*$|\\mathbb\{\s*$", pre) and re.match(r"^\s*\}", post) \
            and re.match(r"^\d$", raw):
        return "A6-harness-constant", ctx
    if raw in ("1", "2") and re.search(r"(?<![A-Za-z])L_?$", pre):
        return "A7-symbolic-index", ctx
    if re.search(r"h\(T\)\s*\+\s*$", pre) and raw == "1":
        return "A7-symbolic-index", ctx

    return None


# ---------------------------------------------------------------------------
# 4.  DERIVATIONS -- exact arithmetic of two or more sourced numbers.
#     Keyed on (relative tex path, printed token, a substring of the context).
# ---------------------------------------------------------------------------

DERIVATIONS = [
    dict(file="paper/sections/forfeit.tex", token="19", ctx="of $19$",
         derivation="19 = 15 + 4.  15 = the 5 (saturator, scorecaster) settings "
                    "{baseline_clipped_qhat0, scorecaster_const_plus_b_over_2, "
                    "scorecaster_const_minus_b_over_2, saturator_level_4b, "
                    "saturator_tangent_ACT23} x the 3 dead-band widths "
                    "{deadband_tau0.5, deadband_tau0.9, deadband_tau1.5} at T = 1e6; "
                    "4 = the wide bands {deadband_tau2, deadband_tau2.5, deadband_tau3, "
                    "deadband_tau5} in variation wide_deadbands_baseline at T = 2e5.",
         inputs=["results/forfeit-variations-20260820T101445Z.json :: rows[*].{variation,arm,T}"]),
    dict(file="paper/sections/forfeit.tex", token="19", ctx="$19$ of",
         derivation="Same count as above; the sentence prints it as 'N of N' because "
                    "every one of the 19 predicted verdicts matched the measured "
                    "miscoverage (no counterexample).",
         inputs=["results/forfeit-variations-20260820T101445Z.json :: rows[*].miscoverage"]),
    dict(file="paper/sections/forfeit.tex", token="0", ctx="tau^{\\star} = 0",
         derivation="tau* = sup_x r_t(x) + sup_t qhat_t - b/2 = b + (-b/2) - b/2 "
                    "= 2 + (-1) - 1 = 0 at the constant scorecaster qhat = -b/2 with "
                    "the clipped level-b saturator.",
         inputs=["results/forfeit-variations-20260820T101445Z.json :: base_config.b = 2.0",
                 "results/forfeit-variations-20260820T101445Z.json :: boundary_law"]),
    dict(file="paper/sections/forfeit.tex", token="0", ctx="permits radius $0$",
         derivation="Corollary 2's radius mu_t(b/2 - |qhat_t|) = 1 x (1 - 1) = 0 at "
                    "qhat_t == +b/2 = 1 with mu_t = 1.",
         inputs=["results/forfeit-variations-20260820T101445Z.json :: base_config.b = 2.0"]),
    dict(file="paper/sections/forfeit.tex", token="0.63", ctx="0.63/(1-w)",
         derivation="FITTED LAW, printed with an explicit approx sign.  0.63/(1-w) "
                    "reproduces max_t|E_t| for the partial-adjustment arms: "
                    "w = 0.9 -> 6.30 (measured 6.30), w = 0.99 -> 63.0 (measured 63.00), "
                    "w = 0.999 -> 630 (measured 623.70).",
         inputs=["results/forfeit-20260820T063045Z-83747c45.json :: aggregate_table[8,12,16].max_abs_E"]),
    dict(file="paper/sections/forfeit.tex", token="0.5", ctx="0.5\\,h(T)+0.9",
         derivation="FITTED LAW, printed with an explicit approx sign.  0.5 h(T) + 0.9 "
                    "reproduces the unsmoothed arm's max_t|E_t| at all four horizons: "
                    "5.51/5.50, 6.66/6.60, 7.00/7.00, 7.81/7.80.",
         inputs=["results/forfeit-20260820T063045Z-83747c45.json :: config.h_values_at_horizons",
                 "results/forfeit-20260820T063045Z-83747c45.json :: aggregate_table[0..3].max_abs_E"]),
    dict(file="paper/sections/forfeit.tex", token="0.9", ctx="0.5\\,h(T)+0.9",
         derivation="Intercept of the same fitted law; see the 0.5 entry.",
         inputs=["results/forfeit-20260820T063045Z-83747c45.json :: aggregate_table[0..3].max_abs_E"]),
    dict(file="paper/sections/limitations.tex", token="0.75", ctx="0.75\\,b",
         derivation="tau/b = 1.5/2 = 0.75, with tau the dead-band width and b = 2 the "
                    "score bound.",
         inputs=["results/forfeit-20260820T063045Z-83747c45.json :: config.deadband_taus[2] = 1.5",
                 "results/forfeit-20260820T063045Z-83747c45.json :: config.b = 2.0"]),
    dict(file="paper/sections/limitations.tex", token="0.5", ctx="b-\\tau = 0.5",
         derivation="b - tau = 2 - 1.5 = 0.5.  Confirmed against the measured deployed "
                    "path: max of arms_raw[deadband_tau1.5].trace.q_deployed = 0.500000.",
         inputs=["results/forfeit-20260820T063132Z-83747c45.json :: arms_raw[10].trace.q_deployed (max = 0.5)",
                 "results/forfeit-20260820T063045Z-83747c45.json :: config.b = 2.0"]),
    dict(file="paper/sections/limitations.tex", token="0.5", ctx="P(s > 0.5)",
         derivation="Same b - tau = 0.5 threshold; see the entry above.",
         inputs=["results/forfeit-20260820T063045Z-83747c45.json :: config.b = 2.0"]),
    dict(file="paper/sections/limitations.tex", token="0.25", ctx="= 0.25",
         derivation="For s ~ U[-b/2, b/2] = U[-1, 1], P(s > 0.5) = (1 - 0.5)/(2) = 0.25 "
                    "exactly.  The measured i.i.d. miscoverage at that arm is 0.249376.",
         inputs=["results/forfeit-20260820T063045Z-83747c45.json :: aggregate_table[163].miscoverage = 0.249376"]),
]


def lookup_derivation(relfile, token, ctx):
    for d in DERIVATIONS:
        if d["file"] == relfile and d["token"] == token and d["ctx"] in ctx:
            return d
    return None


# ---------------------------------------------------------------------------
# 5.  RESULTS INDEX
# ---------------------------------------------------------------------------

TIER1_RE = re.compile(
    r"^(config\.|base_config\.|aggregate_table\[\d+\]\.[A-Za-z_0-9]+$|"
    r"rows\[\d+\]\.[A-Za-z_0-9]+$|arms_raw\[\d+\]\.horizons_raw\[\d+\]\.[A-Za-z_0-9]+$|"
    r"seed$|wall_clock_seconds$)")


def walk_json(obj, path, num_sink, str_sink):
    if isinstance(obj, dict):
        for k, v in obj.items():
            walk_json(v, f"{path}.{k}" if path else str(k), num_sink, str_sink)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            walk_json(v, f"{path}[{i}]", num_sink, str_sink)
    elif isinstance(obj, bool):
        return
    elif isinstance(obj, (int, float)):
        num_sink.append((path, float(obj), 1 if TIER1_RE.match(path) else 2))
    elif isinstance(obj, str):
        str_sink.append((path, obj))


def build_index(results_dir):
    nums, strs = OrderedDict(), OrderedDict()
    for fn in sorted(os.listdir(results_dir), key=lambda f: (f not in DECLARED, DECLARED.index(f) if f in DECLARED else 0, f)):
        if not fn.endswith(".json"):
            continue
        with open(os.path.join(results_dir, fn)) as fh:
            data = json.load(fh)
        n, s = [], []
        walk_json(data, "", n, s)
        nums[fn], strs[fn] = n, s
    return nums, strs


def norm_label(raw):
    """'2.0' -> '2', '1.500' -> '1.5', '4' -> '4'."""
    if "." in raw:
        raw = raw.rstrip("0").rstrip(".")
    return raw or "0"


PARAM_CTX_RE = re.compile(
    r"(?:\\tau(?:\^\{\\star\})?|w|p|\\lambda|level|\\hat\{q\}(?:_t)?)\s*(?:=|\\equiv)?\s*(?:\$|~)?\s*$")


def is_param_context(text, start):
    """True when the paper is writing the numeral as a PARAMETER LABEL --
    'tau = 1.5', 'w = 0.999', 'level $4b$' -- rather than reporting a
    measurement.  Such numerals resolve to an arm / variation identifier."""
    pre = text[max(0, start - 40):start]
    return bool(PARAM_CTX_RE.search(pre))


def search(value, tol, raw, nums, strs, file_rank, cap=3):
    """Return ranked (tier1, tier2, label) match groups.  Numeric hits are
    ranked by absolute error first -- so an exact 0.0 beats a 1e-9 that merely
    rounds to 0.0000 -- then by results-file precedence, then by path."""
    t1, t2, lab = [], [], []
    for fn, leaves in nums.items():
        for path, v, tier in leaves:
            if abs(v - value) <= tol:
                (t1 if tier == 1 else t2).append((fn, path, v))
    key = lambda h: (round(abs(h[2] - value), 15), file_rank.get(h[0], 99), h[1])
    t1.sort(key=key)
    t2.sort(key=key)
    nl = norm_label(raw)
    if re.match(r"^\d+(\.\d+)?$", raw):
        for fn, leaves in strs.items():
            for path, sv in leaves:
                if re.search(r"(?:tau|_w|_p)" + re.escape(nl) + r"(?![0-9.])", sv) or \
                   re.search(r"level_" + re.escape(nl) + r"b", sv):
                    lab.append((fn, path, sv))
    lab.sort(key=lambda h: (file_rank.get(h[0], 99), h[1]))
    return (t1[:cap], len(t1)), (t2[:cap], len(t2)), (lab[:cap], len(lab))


# ---------------------------------------------------------------------------
# 6.  MAIN
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    repo = os.path.abspath(args.repo)
    tex = [os.path.join(repo, "paper", "main.tex")]
    sect = os.path.join(repo, "paper", "sections")
    tex += [os.path.join(sect, f) for f in sorted(os.listdir(sect)) if f.endswith(".tex")]

    nums, strs = build_index(os.path.join(repo, "results"))
    file_rank = {fn: i for i, fn in enumerate(nums.keys())}

    report = OrderedDict([
        ("tool", "tools/audit_paper_numbers.py"),
        ("repo", repo),
        ("declared_results_files", DECLARED),
        ("results_index", OrderedDict((fn, {"numeric_leaves": len(v),
                                            "tier1_leaves": sum(1 for _, _, t in v if t == 1),
                                            "string_leaves": len(strs[fn])})
                                      for fn, v in nums.items())),
        ("allowlist_rules", ALLOWLIST_RULES),
        ("derivations_table", DERIVATIONS),
        ("files", OrderedDict()),
        ("summary", OrderedDict()),
    ])

    tot = dict(tok=0, excl=0, src=0, weak=0, lab=0, der=0, uns=0)

    for path in tex:
        rel = os.path.relpath(path, repo)
        body, linemap, ncom = strip_tex_comments(open(path).read())
        entries = []
        for m in NUM_RE.finditer(body):
            kind = m.lastgroup
            raw = m.group(0)
            value, tol, dec = parse_token(kind, raw)
            if value is None:
                continue
            tot["tok"] += 1
            ln = offset_to_line(linemap, m.start())
            ctx = " ".join(body[max(0, m.start() - 80):m.end() + 55].split())
            rule = classify_structural(body, m.start(), m.end(), raw, value)
            if rule:
                tot["excl"] += 1
                entries.append(OrderedDict([("line", ln), ("token", raw), ("value", value),
                                            ("verdict", "EXCLUDED-STRUCTURAL"),
                                            ("allowlist_rule", rule[0]), ("context", ctx)]))
                continue
            d = lookup_derivation(rel, raw.strip(), ctx)
            if d:
                tot["der"] += 1
                entries.append(OrderedDict([("line", ln), ("token", raw), ("value", value),
                                            ("verdict", "DERIVED"),
                                            ("derivation", d["derivation"]),
                                            ("inputs", d["inputs"]), ("context", ctx)]))
                continue
            (t1, n1), (t2, n2), (lb, nl) = search(value, tol, raw.strip(), nums, strs, file_rank)
            if lb and is_param_context(body, m.start()):
                tot["lab"] += 1
                entries.append(OrderedDict([
                    ("line", ln), ("token", raw), ("value", value),
                    ("verdict", "SOURCED-CONFIG-LABEL"), ("n_label_matches", nl),
                    ("citations", [{"file": "results/" + f, "field_path": p, "identifier": s2}
                                   for f, p, s2 in lb]),
                    ("also_numeric_tier1", [{"file": "results/" + f, "field_path": p,
                                             "json_value": v} for f, p, v in t1]),
                    ("context", ctx)]))
                continue
            if t1:
                tot["src"] += 1
                entries.append(OrderedDict([
                    ("line", ln), ("token", raw), ("value", value), ("printed_decimals", dec),
                    ("verdict", "SOURCED"), ("match_tier", 1), ("n_tier1_matches", n1),
                    ("citations", [{"file": "results/" + f, "field_path": p, "json_value": v}
                                   for f, p, v in t1]),
                    ("config_label_matches", [{"file": "results/" + f, "field_path": p,
                                               "identifier": s2} for f, p, s2 in lb]),
                    ("context", ctx)]))
            elif lb:
                tot["lab"] += 1
                entries.append(OrderedDict([
                    ("line", ln), ("token", raw), ("value", value),
                    ("verdict", "SOURCED-CONFIG-LABEL"), ("n_label_matches", nl),
                    ("citations", [{"file": "results/" + f, "field_path": p, "identifier": s}
                                   for f, p, s in lb]),
                    ("context", ctx)]))
            elif t2:
                tot["weak"] += 1
                entries.append(OrderedDict([
                    ("line", ln), ("token", raw), ("value", value), ("printed_decimals", dec),
                    ("verdict", "SOURCED-WEAK-TIER2-TRACE-ONLY"), ("match_tier", 2),
                    ("n_tier2_matches", n2),
                    ("citations", [{"file": "results/" + f, "field_path": p, "json_value": v}
                                   for f, p, v in t2]),
                    ("context", ctx)]))
            else:
                tot["uns"] += 1
                entries.append(OrderedDict([
                    ("line", ln), ("token", raw), ("value", value), ("printed_decimals", dec),
                    ("verdict", "UNSOURCED"), ("context", ctx)]))
        report["files"][rel] = OrderedDict([("comment_lines_stripped", ncom),
                                            ("tokens", entries)])

    report["summary"] = OrderedDict([
        ("tokens_found_in_body", tot["tok"]),
        ("excluded_structural", tot["excl"]),
        ("derived", tot["der"]),
        ("sourced_tier1", tot["src"]),
        ("sourced_config_label", tot["lab"]),
        ("sourced_weak_tier2_only", tot["weak"]),
        ("unsourced", tot["uns"]),
    ])

    print("=" * 100)
    print("NUMERIC PROVENANCE AUDIT -- tools/audit_paper_numbers.py")
    print("=" * 100)
    for fn, meta in report["results_index"].items():
        print(f"  results/{fn}: {meta['numeric_leaves']} numeric leaves "
              f"({meta['tier1_leaves']} tier-1), {meta['string_leaves']} string leaves")
    print("\nALLOW-LIST (structural; excluded from sourcing):")
    for k, v in ALLOWLIST_RULES.items():
        print(f"  {k}\n      {v}")
    print()
    for rel, blob in report["files"].items():
        print("-" * 100)
        print(f"{rel}   ({blob['comment_lines_stripped']} comment lines stripped)")
        print("-" * 100)
        for e in blob["tokens"]:
            v = e["verdict"]
            if v == "EXCLUDED-STRUCTURAL":
                print(f"  L{e['line']:<4} {e['token']:<16} EXCLUDED   [{e['allowlist_rule']}]")
            elif v == "DERIVED":
                print(f"  L{e['line']:<4} {e['token']:<16} DERIVED    {e['derivation'][:110]}")
            elif v == "SOURCED":
                c = e["citations"][0]
                print(f"  L{e['line']:<4} {e['token']:<16} SOURCED    results/{c['file'].split('/')[-1]} :: "
                      f"{c['field_path']} = {c['json_value']}   [{e['n_tier1_matches']} tier-1 match(es)]")
            elif v == "SOURCED-CONFIG-LABEL":
                c = e["citations"][0]
                print(f"  L{e['line']:<4} {e['token']:<16} LABEL      {c['field_path']} = {c['identifier']!r}"
                      f"   [{e['n_label_matches']}]")
            elif v == "SOURCED-WEAK-TIER2-TRACE-ONLY":
                c = e["citations"][0]
                print(f"  L{e['line']:<4} {e['token']:<16} WEAK(T2)   {c['field_path']} = {c['json_value']}"
                      f"   ctx: {e['context'][:60]}")
            else:
                print(f"  L{e['line']:<4} {e['token']:<16} *** UNSOURCED ***   ctx: {e['context'][:80]}")
        print()
    print("=" * 100)
    for k, v in report["summary"].items():
        print(f"  {k}: {v}")
    print("=" * 100)

    if args.json:
        with open(args.json, "w") as fh:
            json.dump(report, fh, indent=1)
        print(f"\nJSON written to {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
