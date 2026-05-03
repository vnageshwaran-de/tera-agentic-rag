#!/usr/bin/env python3
from __future__ import annotations
"""
render-tera-grid.py

Renders Figure 7(b) — TERA cross-cutting concerns view — and Figure 7(c) —
editorial / content-analytics worked-example overlay — as vector PDFs.

Both panels share the same 6 (layer) x 5 (concern) grid layout:
  rows    = L5 (top) ... L0 (bottom) — application down to cloud foundation
  columns = C1 ... C5 — security, evaluation, observability, governance, LLMOps

Panel (b) annotates each cell with its prescription (one short phrase).
Panel (c) highlights six named cells with the editorial deployment choices
from Section 11.6 of the manuscript.

Usage:
    cd path/to/tera-agentic-rag
    source .venv/bin/activate
    python3 scripts/render-tera-grid.py --panel b --output figures/figure-07b-tera-concerns.pdf
    python3 scripts/render-tera-grid.py --panel c --output figures/figure-07c-tera-editorial-overlay.pdf

License: MIT.
"""

import argparse
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as patches

LAYERS = ["L0", "L1", "L2", "L3", "L4", "L5"]
LAYER_LABELS = [
    "L0  Cloud foundation",
    "L1  Data and knowledge",
    "L2  Retrieval",
    "L3  Reasoning and planning",
    "L4  Tool and action",
    "L5  Application",
]
CONCERNS = ["C1", "C2", "C3", "C4", "C5"]
CONCERN_LABELS = [
    "C1\nSecurity",
    "C2\nEvaluation",
    "C3\nObservability",
    "C4\nGovernance",
    "C5\nLLMOps",
]

# Layer band colors from Figure 7(a)
LAYER_FILL = {
    "L0": "#f6f6f6",
    "L1": "#eef5fb",
    "L2": "#e8f7ee",
    "L3": "#fff8e6",
    "L4": "#fdebef",
    "L5": "#f0e8fb",
}

# Panel (b): one-phrase prescription per (layer, concern). From Table 10.
# Lines kept short (~14 chars) to fit cell width at 6pt font.
PANEL_B = {
    ("L0", "C1"): "per-tenant cache\nKMS keys\nnet deny-default",
    ("L0", "C2"): "—",
    ("L0", "C3"): "OTel GenAI\ncorrelation IDs",
    ("L0", "C4"): "append-only audit\nSBOM\nAICM mapping",
    ("L0", "C5"): "GitOps\neval-gated promo\nrollback runbook",
    ("L1", "C1"): "source allow-list\nencrypted\nembeddings",
    ("L1", "C2"): "retrieval-quality\nSLO",
    ("L1", "C3"): "ingest telemetry",
    ("L1", "C4"): "provenance graph\nPII scan log",
    ("L1", "C5"): "embedding\nversioning",
    ("L2", "C1"): "rate-limit\nmulti-source\norder check",
    ("L2", "C2"): "RAGAS / ARES\nSYNCHECK\nCI gate",
    ("L2", "C3"): "retrieval traces",
    ("L2", "C4"): "retrieval-quality\nevidence",
    ("L2", "C5"): "retriever\nversioning",
    ("L3", "C1"): "StruQ queries\nPromptShield\nmulti-turn safety",
    ("L3", "C2"): "agent-capability\nbenchmarks",
    ("L3", "C3"): "plan-trace span",
    ("L3", "C4"): "plan log\nretention",
    ("L3", "C5"): "agent versioning",
    ("L4", "C1"): "hash-pinned tools\nACLs\nToolHijacker mit.",
    ("L4", "C2"): "BFCL\ntool-use\ncorrectness",
    ("L4", "C3"): "tool-call traces\nside-effect logs",
    ("L4", "C4"): "HITL approval\ngates; reversal",
    ("L4", "C5"): "tool registry\nversioning",
    ("L5", "C1"): "output safety\nclassifier\ncollusion canary",
    ("L5", "C2"): "outcome metrics",
    ("L5", "C3"): "user-facing\ntelemetry",
    ("L5", "C4"): "user disclosure\naudit",
    ("L5", "C5"): "deploy / rollback\ncost SLO",
}

# Panel (c): editorial / content-analytics worked example. Section 11.6.
# Six named cells get bold-highlighted annotations; other cells dim.
PANEL_C_HIGHLIGHTED = {
    ("L0", "C1"): "Hybrid cloud:\non-prem archive\n+ public LLM\ngateway; per-tenant\ncache namespace",
    ("L1", "C4"): "Provenance:\nchunk -> citation\ntied to editorial\nfact-check\nworkflow",
    ("L2", "C2"): "BM25 + dense\n+ rerank\nRAGAS on\neditorial fixtures\nSYNCHECK online",
    ("L3", "C1"): "Structured queries\nPromptShield\nCrescendo /\nTwinBreak\nrelease gate",
    ("L4", "C1"): "CMS-read only\nhash-pinned tools\nACL-scoped agent",
    ("L4", "C4"): "HITL approval\nbefore any auto-\npublished\ncorrection or\nsummary",
    ("L5", "C5"): "GitOps\neval-gated\nrollback on\nfaithfulness regr.\nper-query cost SLO",
}


def render_panel(panel: str, output: Path) -> None:
    fig, ax = plt.subplots(figsize=(16.0, 10.0))
    plt.subplots_adjust(left=0.14, right=0.99, top=0.88, bottom=0.04)
    cell_w, cell_h = 1.0, 1.0

    # Uniform grid pass: draw every cell with the same gray border so the grid
    # stays geometrically consistent regardless of highlight state.
    GRID_EDGE = "#bbbbbb"
    GRID_LW = 0.6

    for li, layer in enumerate(LAYERS):
        for ci, concern in enumerate(CONCERNS):
            x0 = ci * cell_w
            y0 = (len(LAYERS) - 1 - li) * cell_h
            fill = LAYER_FILL[layer]

            if panel == "b":
                text = PANEL_B.get((layer, concern), "")
                face = fill
                face_alpha = 0.6
                font_size = 6.0
                weight = "normal"
                highlight = False
            elif panel == "c":
                if (layer, concern) in PANEL_C_HIGHLIGHTED:
                    text = PANEL_C_HIGHLIGHTED[(layer, concern)]
                    face = fill
                    face_alpha = 1.0
                    font_size = 6.5
                    weight = "bold"
                    highlight = True
                else:
                    text = ""
                    face = "none"
                    face_alpha = 1.0
                    font_size = 6.5
                    weight = "normal"
                    highlight = False
            else:
                raise ValueError("--panel must be 'b' or 'c'")

            # Layer 1: cell fill plus uniform grid border (every cell).
            ax.add_patch(patches.Rectangle(
                (x0, y0), cell_w, cell_h,
                facecolor=face,
                alpha=(face_alpha if face != "none" else 1.0),
                edgecolor=GRID_EDGE, linewidth=GRID_LW))

            # Layer 2: inset highlight border for highlighted cells only.
            # Drawn 0.04 units inside the cell so the grid geometry is preserved.
            if highlight:
                inset = 0.045
                ax.add_patch(patches.Rectangle(
                    (x0 + inset, y0 + inset),
                    cell_w - 2 * inset, cell_h - 2 * inset,
                    facecolor="none",
                    edgecolor="#0d2b5c", linewidth=2.0))

            if text and text != "—":
                ax.text(x0 + cell_w / 2, y0 + cell_h / 2, text,
                        ha="center", va="center", fontsize=font_size,
                        fontweight=weight, wrap=True)

    # Axes
    ax.set_xlim(0, len(CONCERNS) * cell_w)
    ax.set_ylim(0, len(LAYERS) * cell_h)
    ax.set_xticks([i * cell_w + cell_w / 2 for i in range(len(CONCERNS))])
    ax.set_xticklabels(CONCERN_LABELS, fontsize=10, fontweight="bold")
    ax.set_yticks([i * cell_h + cell_h / 2 for i in range(len(LAYERS))])
    ax.set_yticklabels(list(reversed(LAYER_LABELS)), fontsize=9, fontweight="bold")
    ax.set_aspect("equal")
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(axis="x", which="both", length=0, pad=12)
    ax.tick_params(axis="y", which="both", length=0, pad=10)
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position("top")

    if panel == "b":
        title = "Figure 7(b). TERA layers x cross-cutting concerns: per-cell prescription."
    else:
        title = "Figure 7(c). Editorial / content-analytics worked example: six named cells highlighted."
    ax.set_title(title, fontsize=11, pad=44, fontweight="bold")

    output.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output, format="pdf",
                metadata={"Title": f"TERA grid panel ({panel})",
                          "Author": "Vinoth Nageshwaran"})
    print(f"Wrote {output}", file=sys.stderr)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--panel", required=True, choices=["b", "c"],
                    help="Which sub-panel to render: b (concerns) or c (editorial overlay).")
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args()
    render_panel(args.panel, args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
