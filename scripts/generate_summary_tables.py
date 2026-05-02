#!/usr/bin/env python3
"""
generate_summary_tables.py

Convert the repository's CSV artifacts into LaTeX-ready table fragments for
inclusion in the IEEE Access manuscript. Each output is a self-contained
booktabs-style table that can be \input{...} into the LaTeX source.

Usage:
    python generate_summary_tables.py \
        --in-dir  . \
        --out-dir paper/tables-tex

The script does not depend on pandas; uses csv stdlib.

License: MIT.
"""

import argparse
import csv
import sys
from pathlib import Path

# Map CSV file -> (LaTeX table label, caption snippet, columns to include).
TABLES = {
    "taxonomy/enterprise-agentic-rag-taxonomy.csv": (
        "tab:taxonomy",
        "Eight-dimension taxonomy of enterprise agentic RAG systems.",
        ["dimension", "categories", "description", "dominant_risks"],
    ),
    "security/threat-model.csv": (
        "tab:threats",
        "Threat-to-control matrix for agentic RAG.",
        ["threat", "owasp_or_nist_mapping", "tera_layers", "empirical_anchor_quote", "mitigation_pattern"],
    ),
    "cloud-reference-architecture/components.csv": (
        "tab:components",
        "Cloud-native deployment components.",
        ["component", "function", "failure_risks", "security_control", "observability_signal"],
    ),
    "evaluation/benchmarks-and-metrics.csv": (
        "tab:eval",
        "Agentic-RAG evaluation benchmarks and metrics.",
        ["benchmark_or_metric", "capability", "measure", "enterprise_relevance"],
    ),
    "taxonomy/architecture-patterns.csv": (
        "tab:patterns",
        "Agentic RAG architecture patterns.",
        ["pattern", "advantages", "limitations", "required_controls"],
    ),
}


def latex_escape(s: str) -> str:
    return (
        s.replace("\\", r"\textbackslash{}")
        .replace("&", r"\&")
        .replace("%", r"\%")
        .replace("$", r"\$")
        .replace("#", r"\#")
        .replace("_", r"\_")
        .replace("{", r"\{")
        .replace("}", r"\}")
        .replace(";", "; ")
    )


def emit_table(rows: list[dict], cols: list[str], label: str, caption: str) -> str:
    align = "p{0.18\\textwidth}" + "p{0.20\\textwidth}" * (len(cols) - 1)
    lines = [
        r"\begin{table*}[t]",
        r"\centering",
        rf"\caption{{{latex_escape(caption)}}}",
        rf"\label{{{label}}}",
        rf"\begin{{tabular}}{{{align}}}",
        r"\toprule",
        " & ".join(latex_escape(c.replace("_", " ").title()) for c in cols) + r" \\",
        r"\midrule",
    ]
    for r in rows:
        cells = [latex_escape(r.get(c, "")) for c in cols]
        lines.append(" & ".join(cells) + r" \\")
    lines += [r"\bottomrule", r"\end{tabular}", r"\end{table*}"]
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in-dir", required=True, type=Path)
    ap.add_argument("--out-dir", required=True, type=Path)
    args = ap.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)

    for rel_csv, (label, caption, cols) in TABLES.items():
        csv_path = args.in_dir / rel_csv
        if not csv_path.exists():
            print(f"skip (missing): {csv_path}", file=sys.stderr)
            continue
        rows = list(csv.DictReader(csv_path.open(encoding="utf-8")))
        out = args.out_dir / (csv_path.stem + ".tex")
        out.write_text(emit_table(rows, cols, label, caption), encoding="utf-8")
        print(f"wrote {out} ({len(rows)} rows)", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
