#!/bin/sh
# ---------------------------------------------------------------------------
# check_claim_drift.sh - catch the failure this project has committed three
# times: a load-bearing claim shipped in a TRACKED document that a gitignored
# research/ artefact from the SAME session already contradicted.
#
#   S1  the synthesis missed its own agent A6's reduction, and S2 had to
#       rediscover it            (research/S1/A6-postprocessing-coverage.json)
#   S2  a conservation law reached four tracked files on two agents agreeing,
#       and this project's own critic killed it four hours later
#   S3  docs/FRAMING.md and docs/GATES.md kept a falsified R3c claim while the
#       session's own H6 agent falsified it. "H6", "875" and "Kalai" returned
#       ZERO hits across docs/ where there should have been support. Booked O51.
#
# Method, deliberately crude - S3's own catch was three tokens grepped:
#   1. index the artefacts this session WROTE - agent JSONs, checkpoints,
#      results/. Fetched third-party page and PDF text is deliberately EXCLUDED
#      (records/ ft/ raw/ txt/): that is evidence the session gathered, not a
#      claim the session made, and including it puts 700 MB in the way of a
#      check that should take a second;
#   2. pull the load-bearing lines out of the tracked governing documents -
#      lines carrying a stated verdict/status word or a number AND naming this
#      session, i.e. lines presenting themselves as freshly established now;
#   3. take up to 4 distinctive tokens from each. Bare years are dropped and
#      integers must run to four digits, because "202" matches every timestamp
#      in the tree and discriminates nothing;
#   4. report UNSUPPORTED (no same-session artefact carries the token) and
#      CONTRADICTED (an artefact carries it beside a falsifying word). Only
#      NUMERIC tokens can be CONTRADICTED: "875" sitting next to "falsified" is
#      a signal, "H1" sitting next to "overturn" is an agent discussing its own
#      method. Identifier tokens still carry the UNSUPPORTED test, which is the
#      one that caught O51 ("H6", "875", "Kalai" -> zero hits across docs/).
#
# It is a smoke alarm, not a proof. False positives are expected and are cheap;
# the failure it exists to stop has cost three sessions.
#
# Usage:  sh tools/check_claim_drift.sh [SESSION_TAG]      (default: S6)
#         The default is bumped BY EACH SESSION.  S5's adversarial critic found the
#         default still reading S4, which makes a bare invocation index the WRONG
#         session's artefacts and report findings that belong to neither.  A bare run
#         must index the CURRENT session or it is worse than no run at all.
#         BUMPED S4 -> S5 (S5 wave 1), S5 -> S6 (S6 sub-session A).
# Exit:   0 clean, 1 if any claim is UNSUPPORTED or CONTRADICTED.
#
# BINDING: this runs as the last step of every wave that touches
# docs/FRAMING.md or docs/GATES.md, BEFORE that wave's commit.
# See docs/PROCESS_NOTES.md.
# ---------------------------------------------------------------------------
set -u
root=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "not a git repo" >&2; exit 1; }
cd "$root" || exit 1

SESSION=${1:-S6}
TRACKED="docs/FRAMING.md docs/GATES.md"
LOADBEARING='occupied|clear|tight|false|falsif|refut|verif|measur|supersede|retired|withdraw|closed|resolved|[0-9]'
FALSIFY='falsif|refut|withdraw|supersede|overturn|wrong|incorrect|does not hold|not supported|corrected from'
# A tracked line that announces its own supersession is history, not a fresh claim.
# This project deliberately never deletes history, so without this filter the check
# drowns in its own archive.
HISTORICAL='SUPERSEDED|RETIRED|NOT DELETED|FALSIFIED|WITHDRAWN|Previously `|as history|Read them as history'
TOKENRE='[0-9]+\.[0-9]{3,}|[0-9]{4,}|arXiv:[0-9]+\.[0-9]+|tau\*|O[0-9]{2}|\b[A-Z][0-9]\b'
d=$(mktemp -d); trap 'rm -rf "$d"' EXIT

# --- 1. index what this session WROTE ----------------------------------------
find "research/$SESSION" results -type f -size -512k \
     \( -name '*.json' -o -name '*.md' -o -name '*.txt' -o -name '*.py' -o -name '*.csv' \) 2>/dev/null \
  | grep -vE '/(records|ft|raw|txt|pdf|assets)/' > "$d/files"
while IFS= read -r a; do sed "s|^|$a:|" "$a"; done < "$d/files" > "$d/idx" 2>/dev/null
printf 'check_claim_drift: session %s - %s artefact file(s), %s lines indexed\n' \
       "$SESSION" "$(wc -l <"$d/files" | tr -d ' ')" "$(wc -l <"$d/idx" | tr -d ' ')"
[ -s "$d/idx" ] || printf '  WARNING: index EMPTY - every claim below will read UNSUPPORTED.\n'

# --- 2-3. load-bearing lines -> "file:line<TAB>token<TAB>text" ---------------
for f in $TRACKED; do
  [ -f "$f" ] || continue
  grep -nE "\b$SESSION\b" "$f" | grep -iE "$LOADBEARING" | grep -vE "$HISTORICAL" | while IFS= read -r hit; do
      no=${hit%%:*}; text=$(printf '%.130s' "${hit#*:}")
      printf '%s' "${hit#*:}" | grep -oE "$TOKENRE" | grep -vE "^(19|20)[0-9]{2}\$|^$SESSION\$" | sort -u | head -4 \
      | while IFS= read -r t; do printf '%s:%s\t%s\t%s\n' "$f" "$no" "$t" "$text"; done
    done
done > "$d/claims"
cut -f2 "$d/claims" | sort -u > "$d/tokens"
printf 'check_claim_drift: %s claim-token pair(s) over %s distinct token(s)\n' \
       "$(wc -l <"$d/claims" | tr -d ' ')" "$(wc -l <"$d/tokens" | tr -d ' ')"

# --- 4. one reducing pass, then cheap per-token lookups ----------------------
if [ -s "$d/tokens" ] && [ -s "$d/idx" ]; then
  grep -Ff "$d/tokens" "$d/idx" > "$d/hits" 2>/dev/null || : > "$d/hits"
else : > "$d/hits"; fi
grep -iE "$FALSIFY" "$d/hits" > "$d/suspect" 2>/dev/null || : > "$d/suspect"

while IFS="$(printf '\t')" read -r loc tok text; do
  if ! grep -qF -- "$tok" "$d/hits"; then
    printf 'UNSUPPORTED   %s  token=%s\n      %s\n' "$loc" "$tok" "$text"
  elif printf '%s' "$tok" | grep -qE '^[0-9]' && grep -qF -- "$tok" "$d/suspect"; then
    printf 'CONTRADICTED  %s  token=%s\n      tracked:  %s\n      artefact: %.130s\n' \
           "$loc" "$tok" "$text" "$(grep -F -- "$tok" "$d/suspect" | head -1)"
  fi
done < "$d/claims" > "$d/out"

if [ -s "$d/out" ]; then
  cat "$d/out"
  printf '\ncheck_claim_drift: %s finding(s). Each MUST be fixed in this session or\n' \
         "$(grep -c '^\(UNSUPPORTED\|CONTRADICTED\)' "$d/out")"
  printf 'explicitly dispositioned in the wave patch log BEFORE the wave commits.\n'
  exit 1
fi
printf 'check_claim_drift: PASS - every %s-marked load-bearing claim in %s is\n' "$SESSION" "$TRACKED"
printf 'carried by a same-session artefact, and none is contradicted by one.\n'
exit 0
