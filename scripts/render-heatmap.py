#!/usr/bin/env python3
from __future__ import annotations
"""
render-heatmap.py

Renders Figure 8 — Threats x Controls x Observability heatmap on the TERA grid —
as a vector PDF for IEEE Access submission.

Each cell of the 6 (layer L0-L5) x 5 (concern C1-C5) grid is drawn as three
horizontal bars encoding threat density (red), control density (green), and
observability-signal density (blue). Bar lengths are computed by joining
the threat-model, governance-checklist, and components CSVs against the
(layer, concern) coordinate.

Usage:
    python3 scripts/render-heatmap.py \\
        --threats security/threat-model.csv \\
        --components cloud-reference-architecture/components.csv \\
        --output figures/figure-08-threats-controls-heatmap.pdf

The control-density column is hand-computed (see CONTROL_DENSITY below)
because the governance-checklist.md is markdown rather than CSV; future
work could move the checklist to CSV for full automation.

License: MIT.
"""

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import LinearSegmentedColormap

LAYERS = ["L0", "L1", "L2", "L3", "L4", "L5"]
LAYER_LABELS = [
    "L0 Cloud foundation",
    "L1 Data and knowledge",
    "L2 Retrieval",
    "L3 Reasoning and planning",
    "L4 Tool and action",
    "L5 Application",
]
CONCERNS = ["C1", "C2", "C3", "C4", "C5"]
CONCERN_LABELS = [
    "C1 Security",
    "C2 Evaluation",
    "C3 Observability",
    "C4 Governance",
    "C5 LLMOps",
]

# Hand-curated control density per (layer, concern). Each value is the count
# of governance-checklist rows (G1-G32) whose anchor reference applies. This
# is a single-author judgment derived from governance/governance-checklist.md.
CONTROL_DENSITY = {
    ("L0", "C1"): 3, ("L0", "C2"): 0, ("L0", "C3"): 2, ("L0", "C4"): 4, ("L0", "C5"): 3,
    ("L1", "C1"): 2, ("L1", "C2"): 1, ("L1", "C3"): 1, ("L1", "C4"): 3, ("L1", "C5"): 1,
    ("L2", "C1"): 2, ("L2", "C2"): 3, ("L2", "C3"): 1, ("L2", "C4"): 2, ("L2", "C5"): 1,
    ("L3", "C1"): 2, ("L3", "C2"): 2, ("L3", "C3"): 2, ("L3", "C4"): 2, ("L3", "C5"): 1,
    ("L4", "C1"): 4, ("L4", "C2"): 1, ("L4", "C3"): 2, ("L4", "C4"): 4, ("L4", "C5"): 1,
    ("L5", "C1"): 1, ("L5", "C2"): 1, ("L5", "C3"): 2, ("L5", "C4"): 3, ("L5", "C5"): 3,
}


def parse_threat_density(threat_csv: Path) -> dict[tuple[str, str], int]:
    """Threat density per (layer, concern). Concern is C1 (security) for every
    threat by default; some threats also touch C3 observability or C4 governance."""
    density = Counter()
    rows = list(csv.DictReader(threat_csv.open(encoding="utf-8")))
    for r in rows:
        layers_raw = (r.get("tera_layers") or "").strip()
        if not layers_raw:
            continue
        # tera_layers is a semicolon-separated list, e.g., "L1;L2;L3"
        for layer in [t.strip() for t in layers_raw.replace(",", ";").split(";")]:
            if layer in LAYERS:
                density[(layer, "C1")] += 1
    return dict(density)


def parse_observability_density(components_csv: Path) -> dict[tuple[str, str], int]:
    """Observability density: count components that emit an observability signal,
    keyed by their layer. Concern is C3 (observability)."""
    density = Counter()
    rows = list(csv.DictReader(components_csv.open(encoding="utf-8")))
    # Heuristic mapping from component id (C1-C18) to TERA layer.
    component_to_layer = {
        "C1": "L1", "C2": "L1", "C3": "L1",
        "C4": "L2",
        "C5": "L5", "C6": "L3", "C7": "L4", "C8": "L4",
        "C9": "L0", "C10": "L3", "C11": "L5",
        "C12": "L0", "C13": "L0", "C14": "L0", "C15": "L0", "C16": "L0", "C17": "L0", "C18": "L0",
    }
    for r in rows:
        cid = (r.get("id") or "").strip()
        signal = (r.get("observability_signal") or "").strip()
        if not signal or signal in ("N/A", "n/a"):
            continue
        layer = component_to_layer.get(cid)
        if layer:
            density[(layer, "C3")] += 1
    return dict(density)


def render(threat_csv: Path, components_csv: Path, output: Path) -> None:
    threat_d = parse_threat_density(threat_csv)
    obs_d = parse_observability_density(components_csv)

    # Normalize each channel to [0, 1] for color intensity.
    def norm(d: dict) -> dict:
        if not d:
            return {}
        m = max(d.values())
        return {k: v / m for k, v in d.items()} if m else {k: 0 for k in d}

    threat_n = norm(threat_d)
    control_n = norm(CONTROL_DENSITY)
    obs_n = norm(obs_d)

    fig, ax = plt.subplots(figsize=(7.16, 4.8))

    cell_w, cell_h = 1.0, 1.0
    bar_h = cell_h / 4.5

    for li, layer in enumerate(LAYERS):
        for ci, concern in enumerate(CONCERNS):
            x0 = ci * cell_w
            y0 = (len(LAYERS) - 1 - li) * cell_h

            # Cell background
            ax.add_patch(patches.Rectangle((x0, y0), cell_w, cell_h,
                                           facecolor="white",
                                           edgecolor="#cccccc",
                                           linewidth=0.6))

            # Three bars: threat (red), control (green), observability (blue)
            t = threat_n.get((layer, concern), 0)
            c = control_n.get((layer, concern), 0) if concern == "C4" or True else 0
            o = obs_n.get((layer, concern), 0)

            ax.add_patch(patches.Rectangle(
                (x0 + 0.05, y0 + 0.65 * cell_h),
                0.9 * cell_w * t, bar_h,
                facecolor="#d62728", alpha=0.9, edgecolor="none"))
            ax.add_patch(patches.Rectangle(
                (x0 + 0.05, y0 + 0.40 * cell_h),
                0.9 * cell_w * c, bar_h,
                facecolor="#2ca02c", alpha=0.9, edgecolor="none"))
            ax.add_patch(patches.Rectangle(
                (x0 + 0.05, y0 + 0.15 * cell_h),
                0.9 * cell_w * o, bar_h,
                facecolor="#1f77b4", alpha=0.9, edgecolor="none"))

    ax.set_xlim(0, len(CONCERNS) * cell_w)
    ax.set_ylim(0, len(LAYERS) * cell_h)
    ax.set_xticks([i * cell_w + cell_w / 2 for i in range(len(CONCERNS))])
    ax.set_xticklabels(CONCERN_LABELS, rotation=20, ha="right", fontsize=8)
    ax.set_yticks([i * cell_h + cell_h / 2 for i in range(len(LAYERS))])
    ax.set_yticklabels(list(reversed(LAYER_LABELS)), fontsize=8)
    ax.set_aspect("equal")
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(axis="both", which="both", length=0)

    # Legend
    handles = [
        patches.Patch(facecolor="#d62728", label="threat density"),
        patches.Patch(facecolor="#2ca02c", label="control density"),
        patches.Patch(facecolor="#1f77b4", label="observability density"),
    ]
    ax.legend(handles=handles, loc="upper center",
              bbox_to_anchor=(0.5, -0.18), ncol=3, fontsize=8, frameon=False)

    plt.tight_layout()
    output.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output, format="pdf", bbox_inches="tight",
                metadata={"Title": "TERA threats x controls x observability heatmap",
                          "Author": "Vinoth Nageshwaran"})
    print(f"Wrote {output}", file=sys.stderr)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--threats", required=True, type=Path)
    ap.add_argument("--components", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args()
    render(args.threats, args.components, args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
