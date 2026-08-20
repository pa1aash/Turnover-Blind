#!/bin/sh
# ---------------------------------------------------------------------------
# check_prose_hygiene.sh -- mechanical prose checks over paper/ body text.
#
# Session S5 wave 0 built this because the two checks the session brief
# specified BOTH have a false-negative mode that the brief's own spec walks
# into, and both were demonstrated live against this repository:
#
#   1. DUPLICATE WORDS.  The specified regex \b(\w+)\s+\1\b does NOT match
#      "dead-band dead-band", because \w excludes the hyphen.  The known
#      instance in sections/forfeit.tex is exactly that shape.  This script
#      uses ([\w-]+) instead.
#
#   2. LINE BREAKS.  That instance is ALSO split across a source newline
#      ("... Every dead-band\ndead-band configuration ..."), so any per-line
#      grep misses it even with the corrected character class.  This script
#      joins each file's body into one string before matching.
#
#   3. COMMENTS.  paper/ carries long % comment headers that legitimately
#      contain "---" and prose fragments.  Counting them makes the em-dash
#      total ~116 when the compiled PDF shows 16.  This script strips
#      comments, and its em-dash total agrees with pdftotext on the PDF.
#
# Usage:  sh tools/check_prose_hygiene.sh [--pdf paper/main.pdf]
# Exits non-zero if any em-dash or duplicate word survives in body text.
# ---------------------------------------------------------------------------
set -e
cd "$(dirname "$0")/.."

PDF=""
if [ "$1" = "--pdf" ]; then PDF="$2"; fi

python3 - "$PDF" <<'PY'
import re, sys, glob, subprocess, os

pdf = sys.argv[1] if len(sys.argv) > 1 else ""
files = ['paper/main.tex'] + sorted(glob.glob('paper/sections/*.tex'))
fail = 0

def body_of(path):
    """Return (joined_body_text, offset->lineno map) with % comments stripped."""
    lines = open(path, encoding='utf-8').read().split('\n')
    out, spans, pos = [], [], 0
    for i, line in enumerate(lines, 1):
        s = '' if line.lstrip().startswith('%') else re.split(r'(?<!\\)%', line)[0]
        out.append(s)
        spans.append((pos, pos + len(s), i))
        pos += len(s) + 1
    return ' '.join(out), spans

def lineno(spans, off):
    for a, b, l in spans:
        if a <= off <= b:
            return l
    return '?'

# --- check 1: em-dashes (LaTeX --- and Unicode U+2014) ---------------------
print("== em-dash check (body text, comments stripped) ==")
total = 0
for f in files:
    body, spans = body_of(f)
    hits = [(m.start(), '---') for m in re.finditer(r'---', body)]
    hits += [(m.start(), 'U+2014') for m in re.finditer('—', body)]
    for off, kind in sorted(hits):
        total += 1
        print(f"  FAIL {f}:{lineno(spans, off)}: {kind}  ...{body[max(0,off-55):off+60].strip()}...")
print(f"  em-dash total in body: {total}")
if total:
    fail = 1

# --- check 2: duplicate words (hyphen-aware, across line breaks) ----------
print("== duplicate-word check (hyphen-aware, joined body) ==")
dup = re.compile(r'(?<![\w-])([\w-]+)\s+\1(?![\w-])', re.IGNORECASE)
dtotal = 0
for f in files:
    body, spans = body_of(f)
    for m in dup.finditer(body):
        dtotal += 1
        print(f"  FAIL {f}:{lineno(spans, m.start())}: '{m.group(0)}'")
print(f"  duplicate-word total in body: {dtotal}")
if dtotal:
    fail = 1

# --- check 3: same two checks against the compiled PDF, if given ----------
if pdf and os.path.exists(pdf):
    print(f"== compiled-PDF check ({pdf}) ==")
    txt = subprocess.run(['pdftotext', pdf, '-'], capture_output=True, text=True).stdout
    flat = re.sub(r'\s+', ' ', txt)
    em = len(re.findall('—', flat))
    print(f"  PDF em-dash (U+2014): {em}")
    if em:
        fail = 1
    dm = list(dup.finditer(flat))
    print(f"  PDF duplicate words: {len(dm)}")
    for m in dm:
        print(f"    FAIL '{m.group(0)}' ... {flat[max(0,m.start()-55):m.start()+60]}")
    if dm:
        fail = 1
    # en-dashes are legitimate (numeric ranges) and are reported, never failed
    print(f"  PDF en-dash (U+2013), reported not failed: {len(re.findall(chr(0x2013), flat))}")

print("PASS" if not fail else "FAIL")
sys.exit(fail)
PY
