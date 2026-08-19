#!/bin/sh
# ---------------------------------------------------------------------------
# check_hygiene.sh - authorship hygiene guard for the Turnover-Blind repository
#
# Every commit in this repository is authored by Palaash Gang alone. No file,
# comment, docstring, README line, LaTeX comment or commit message may carry an
# assistant-attribution string.
#
# This script checks three surfaces:
#   1. the working tree (tracked files + untracked files that are not ignored,
#      i.e. exactly the set that could reach a commit),
#   2. every commit message in history,
#   3. every commit author and committer identity in history.
#
# Ignored paths (research/, data/, .venv/ ...) are deliberately NOT scanned:
# they can never be committed, and fetched third-party page text in research/
# would otherwise make this guard permanently red.
#
# The forbidden patterns are assembled from fragments so that this file does
# not itself contain the literal strings it forbids.
#
# Usage:  sh tools/check_hygiene.sh
# Exit:   0 clean, 1 on any hit.
# ---------------------------------------------------------------------------

set -u

repo_root=$(git rev-parse --show-toplevel 2>/dev/null) || {
  echo "check_hygiene: not inside a git repository." >&2
  exit 1
}
cd "$repo_root" || exit 1

# Fragment-assembled patterns (case-insensitive matching is applied below).
p1="cl""aude"
p2="anthro""pic"
p3="co-auth""ored-by"
p4="genera""ted with"
p5="ai-""assisted"
p6="ai ass""isted"
PATTERN="$p1|$p2|$p3|$p4|$p5|$p6"

status=0

# --- 1. working tree ---------------------------------------------------------
printf 'check_hygiene: scanning working tree ...\n'
files=$(git ls-files --cached --others --exclude-standard)
if [ -n "$files" ]; then
  hits=$(printf '%s\n' "$files" \
    | while IFS= read -r f; do
        [ -f "$f" ] || continue
        grep -IEin "$PATTERN" "$f" 2>/dev/null | sed "s|^|$f:|"
      done)
  if [ -n "$hits" ]; then
    printf '%s\n' "$hits" >&2
    printf 'check_hygiene: FAIL - disallowed string(s) in working tree.\n' >&2
    status=1
  fi
fi

# --- 2. commit messages ------------------------------------------------------
if git rev-parse --verify HEAD >/dev/null 2>&1; then
  printf 'check_hygiene: scanning commit messages ...\n'
  msg_hits=$(git log --format='%H %s%n%b' | grep -Ein "$PATTERN")
  if [ -n "$msg_hits" ]; then
    printf '%s\n' "$msg_hits" >&2
    printf 'check_hygiene: FAIL - disallowed string(s) in commit message history.\n' >&2
    status=1
  fi

  # --- 3. author / committer identities -------------------------------------
  printf 'check_hygiene: scanning commit identities ...\n'
  bad_ident=$(git log --format='%an <%ae>%n%cn <%ce>' | sort -u \
              | grep -v '^Palaash Gang <palaashgang@gmail\.com>$')
  if [ -n "$bad_ident" ]; then
    printf '%s\n' "$bad_ident" >&2
    printf 'check_hygiene: FAIL - unexpected author/committer identity.\n' >&2
    status=1
  fi
fi

if [ "$status" -eq 0 ]; then
  printf 'check_hygiene: PASS - no disallowed strings, all commits by Palaash Gang.\n'
fi
exit "$status"
