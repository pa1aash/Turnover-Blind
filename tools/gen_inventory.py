#!/usr/bin/env python3
"""Regenerate audit/INVENTORY.md from the current working tree.

Emits one row per file with size, line count, SHA-256 and a one-line description,
classified as source / output / scratch. Files matched by .gitignore are listed in
a separate section: they exist on disk but can never reach a commit.

Descriptions live in DESCRIPTIONS below, keyed by exact path or by a path prefix
ending in '/'. Anything unmatched is reported as UNDESCRIBED so the inventory
cannot silently go stale.

Usage:  python3 tools/gen_inventory.py
"""
import hashlib
import os
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# (kind, description). kind is one of: source, output, scratch, third-party.
DESCRIPTIONS = {
    ".gitignore": ("source", "Exclusion rules. Keeps research/, data/ contents, credentials and build artefacts out of this public repository."),
    "LICENSE": ("third-party", "MIT licence text fetched verbatim from the SPDX license-list-data registry; only the copyright placeholder was substituted. Provenance in docs/PROVENANCE.md."),
    "README.md": ("source", "Project front page: the claim, repository layout, reproduction status, licence."),
    "tools/check_hygiene.sh": ("source", "Authorship hygiene guard. Scans the committable working tree, all commit messages and all commit identities; exits nonzero on any hit. Run before every commit."),
    "tools/gen_inventory.py": ("source", "Generator for audit/INVENTORY.md. Regenerate rather than hand-editing the inventory."),
    "docs/PLAN_ORIGINAL.md": ("source", "The planning document produced in a prior session, moved here unmodified. Historical artefact and the object of this audit; NOT a specification to be trusted."),
    "docs/PROVENANCE.md": ("source", "Fetch record for every third-party text in the repository: canonical URL, retrieval date, SHA-256 of retrieved bytes, and any local modification."),
    "docs/OUTSTANDING.md": ("source", "Unresolved technical items, ranked by whether they block gate G1."),
    "docs/OPEN_QUESTIONS.md": ("source", "Questions requiring an operator decision. Each is phrased as a specific answerable question."),
    "docs/VENUE.md": ("source", "Venue scoring across ML*OR and five alternatives, with a ranked recommendation and a desk-rejection compliance checklist."),
    "docs/GATES.md": ("source", "Stage gates G0-G6 with acceptance criteria fixed in advance. No gate may be recorded as signed by an automated session."),
    "docs/COMPUTE.md": ("source", "Compute plan. CPU-only working assumption, with the conditions that would change it and the instance spec if one is ever needed."),
    "docs/HYPERRESEARCH_REPORT.md": ("output", "Consolidated output of the research-pipeline run: scope, aim, novelty, references, claims, current state, forward pipeline."),
    "docs/G0_REPORT.md": ("output", "The G0 characterisation report. Session deliverable; opens with the five findings that most change what the project should do next."),
    "audit/INVENTORY.md": ("output", "This file. Complete file-by-file state of the repository."),
    "audit/NUMBERS.md": ("output", "Every numeric claim in docs/PLAN_ORIGINAL.md traced to its source, with an orphan count and percentage."),
    "audit/CLAIMS.md": ("output", "Atomic claim decomposition of docs/PLAN_ORIGINAL.md, tagged by status, load-bearingness and evidence."),
    "audit/PRIOR_ART.md": ("output", "Three prior-art sweeps and the CLEAR / NARROW / OCCUPIED verdicts for claims C1 and C2."),
    "audit/REFS_VERIFIED.bib": ("output", "Bibliography entries built only from fetched canonical records. Nothing here is written from memory."),
    "audit/REFS_REJECTED.md": ("output", "Every reference that failed identifier resolution, metadata agreement or attribution accuracy, with the reason."),
    "audit/CODE_READ.md": ("output", "Line-level reading of the simulator, if one is ever recovered."),
    "audit/REPRO_C1.md": ("output", "Reproduction attempt for the C1 table in docs/PLAN_ORIGINAL.md, cell by cell."),
    "audit/RECONSTRUCTION_SPEC.md": ("output", "Specification a rebuild of the missing simulator would need, with every underdetermined choice listed."),
    "audit/CODE_READ.md": ("output", "Line-level reading of the simulator, if one is ever recovered."),
}
EXTRA = {
    "paper/neurips_2026.sty": ("third-party", "NeurIPS 2026 LaTeX style file, fetched verbatim from the official author kit. Provenance in docs/PROVENANCE.md. Never edit."),
    "paper/neurips_2026.tex": ("third-party", "NeurIPS 2026 template and its usage documentation, fetched verbatim from the official author kit."),
    "paper/checklist.tex": ("third-party", "NeurIPS 2026 paper checklist, fetched verbatim. NOT to be submitted to ML*OR, which requires no checklist."),
}
DESCRIPTIONS.update(EXTRA)

PREFIXES = {
    "results/": ("output", "Experiment run record. One JSON per run; append-only."),
    "figures/": ("output", "Figure generation script or rendered figure."),
    "src/": ("source", "Simulator, dead-band arm or baseline implementation."),
    "paper/": ("source", "LaTeX source or venue style file."),
    "data/": ("output", "Cached market series for the applied arm. Contents untracked."),
}


def classify(path):
    if path in DESCRIPTIONS:
        return DESCRIPTIONS[path]
    if path.endswith(".gitkeep"):
        return ("scratch", "Placeholder so the empty directory survives in git. No content.")
    for pre, val in PREFIXES.items():
        if path.startswith(pre):
            return val
    return ("UNDESCRIBED", "UNDESCRIBED - add an entry to tools/gen_inventory.py")


def stat(path):
    b = (ROOT / path).read_bytes()
    sha = hashlib.sha256(b).hexdigest()
    try:
        text = b.decode("utf-8")
        lines = text.count("\n") + (1 if text and not text.endswith("\n") else 0)
        lines = str(lines)
    except UnicodeDecodeError:
        lines = "binary"
    return len(b), lines, sha


def git(*args):
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    return [p for p in r.stdout.split("\n") if p]


def main():
    tracked = sorted(set(git("ls-files")))
    untracked = sorted(set(git("ls-files", "--others", "--exclude-standard")))
    ignored = sorted(set(git("ls-files", "--others", "--ignored", "--exclude-standard")))

    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT,
                          capture_output=True, text=True).stdout.strip() or "(no commit yet)"

    out = []
    w = out.append
    w("# Repository inventory\n")
    w("Generated by `tools/gen_inventory.py`. Do not hand-edit; regenerate.\n")
    w(f"Snapshot taken at commit `{head}` during the G0 characterisation session.\n")
    w("`kind` is one of **source** (written for this project, meant to be read and\n"
      "maintained), **output** (produced by an audit or an experiment; regenerable in\n"
      "principle), **third-party** (fetched verbatim from a canonical external source),\n"
      "or **scratch** (placeholder or working residue with no informational content).\n")

    total_bytes = 0
    for title, lst, note in (
        ("Tracked files", tracked,
         "These are in git and are pushed to the public remote."),
        ("Untracked but committable", untracked,
         "Present on disk, not ignored, not yet added. An empty section here means the "
         "working tree and the index agree."),
        ("Ignored", ignored,
         "Present on disk and excluded by `.gitignore`. These can never reach a commit. "
         "Listed for completeness so a reader knows what is on the operator's disk that "
         "is not in the repository."),
    ):
        w(f"\n## {title}\n")
        w(note + "\n")
        if not lst:
            w("\n*(none)*\n")
            continue
        w("\n| path | kind | bytes | lines | sha256 | what it is |")
        w("|---|---|---:|---:|---|---|")
        for p in lst:
            if not (ROOT / p).is_file():
                continue
            size, lines, sha = stat(p)
            kind, desc = classify(p)
            if title == "Ignored":
                kind, desc = ("scratch", desc if p in DESCRIPTIONS else
                              "Tool or OS working file. Not part of the project record.")
            total_bytes += size
            w(f"| `{p}` | {kind} | {size} | {lines} | `{sha}` | {desc} |")
        w("")

    w(f"\n## Totals\n")
    w(f"- tracked files: **{len([p for p in tracked if (ROOT/p).is_file()])}**")
    w(f"- untracked-but-committable files: **{len([p for p in untracked if (ROOT/p).is_file()])}**")
    w(f"- ignored files on disk: **{len([p for p in ignored if (ROOT/p).is_file()])}**")
    w(f"- total bytes across all three sets: **{total_bytes}**")

    w("\n## What is absent\n")
    w("Recorded here because absence is the single most consequential fact about this\n"
      "repository's state.\n")
    w("- **No simulator.** `docs/PLAN_ORIGINAL.md` attributes the central C1 table to\n"
      "  `scratchpad/confloor5.py`. No file of that name, and no file producing that\n"
      "  table, exists in this repository or anywhere on the operator's machine. See\n"
      "  `audit/REPRO_C1.md`.\n"
      "- **No results.** `results/` contains only its placeholder. No run record, no\n"
      "  stdout capture, no serialised table backs any number in the plan.\n"
      "- **No figures.** `figures/` contains only its placeholder.\n"
      "- **No paper source.** `paper/` contains only its placeholder. The NeurIPS 2026\n"
      "  style files have not been fetched; see `docs/OUTSTANDING.md`.\n"
      "- **No data.** `data/` contains only its placeholder. The applied arm has no\n"
      "  cached series.\n")

    (ROOT / "audit" / "INVENTORY.md").write_text("\n".join(out) + "\n")
    undescribed = [p for p in tracked + untracked if classify(p)[0] == "UNDESCRIBED"]
    if undescribed:
        print("UNDESCRIBED paths (add to DESCRIPTIONS):", *undescribed, sep="\n  ")
        return 1
    print("audit/INVENTORY.md regenerated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
