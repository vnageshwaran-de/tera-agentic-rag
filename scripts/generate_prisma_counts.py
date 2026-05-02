#!/usr/bin/env python3
"""
generate_prisma_counts.py

Recompute PRISMA flow counts from screening-log.csv and refresh
prisma-flow-data.csv. Useful as a CI gate to keep the manuscript's Figure 1
counts consistent with the screening log.

Usage:
    python generate_prisma_counts.py \
        --screening-log literature-review/screening-log.csv \
        --output        literature-review/prisma-flow-data.csv

Expected screening-log.csv columns include at least: id, decision, full_text_reviewed.

License: MIT.
"""

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--screening-log", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args()

    rows = list(csv.DictReader(args.screening_log.open(encoding="utf-8")))

    decisions = Counter(r.get("decision", "").strip().lower() for r in rows)
    full_text = Counter(r.get("full_text_reviewed", "").strip().lower() for r in rows)

    total = len(rows)
    included = decisions.get("include", 0)
    excluded = total - included
    full_text_yes = full_text.get("full-text", 0) + full_text.get("yes", 0)

    out = [
        ("stage", "count", "notes"),
        ("records_after_dedup", total, "Total entries reaching screening"),
        ("included_in_corpus", included, "Decision = include"),
        ("excluded", excluded, "Decision != include"),
        ("full_text_reviewed", full_text_yes, "[O] confidence in screening log"),
    ]

    with args.output.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerows(out)

    print(f"Wrote PRISMA counts to {args.output}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
