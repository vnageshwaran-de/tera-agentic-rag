# Figures — How to Render

This directory contains the source files for the eight manuscript figures and the scripts to render them. The output format is vector PDF, which IEEE Access prefers and which prints at any DPI without quality loss. The `300 DPI` requirement IEEE Access lists is the *minimum* for raster figures; vector PDFs satisfy it intrinsically because they are resolution-independent.

## Source files in this directory

| Figure | Source | Format | Renderer |
|---|---|---|---|
| F1 PRISMA flow | `figure-01-prisma.mmd` | Mermaid | `scripts/render-mermaid-figures.sh` |
| F2 RAG evolution | `figure-02-rag-evolution.mmd` | Mermaid | `scripts/render-mermaid-figures.sh` |
| F3 Cloud reference architecture | `figure-03-reference-architecture.mmd` | Mermaid | `scripts/render-mermaid-figures.sh` |
| F4 Failure propagation | `figure-04-failure-propagation.mmd` | Mermaid | `scripts/render-mermaid-figures.sh` |
| F5 Evaluation lifecycle | `figure-05-evaluation-lifecycle.mmd` | Mermaid | `scripts/render-mermaid-figures.sh` |
| F6 Governance loop | `figure-06-governance-loop.mmd` | Mermaid | `scripts/render-mermaid-figures.sh` |
| F7 TERA framework (3 sub-panels) | `figure-07-tera-framework.md` | Mermaid + draw.io spec | mixed (see below) |
| F8 Threats × controls × observability heatmap | `figure-08-threats-controls-heatmap.md` | matplotlib spec | `scripts/render-heatmap.py` |

## Step 1 — Render F1 through F6 (Mermaid)

From the repository root:

```bash
cd path/to/tera-agentic-rag
bash scripts/render-mermaid-figures.sh
```

The script installs `@mermaid-js/mermaid-cli` locally on first run (one-time, ~150 MB Chromium download) and caches it under `figures/node_modules/`. It then renders every `.mmd` file in `figures/` to a sibling `.pdf`.

Expected output:
```
figures/figure-01-prisma.pdf
figures/figure-02-rag-evolution.pdf
figures/figure-03-reference-architecture.pdf
figures/figure-04-failure-propagation.pdf
figures/figure-05-evaluation-lifecycle.pdf
figures/figure-06-governance-loop.pdf
```

## Step 2 — Render F7 sub-panels

Figure 7 has three sub-panels:

- **F7(a)** — Stacked layered view. Inline Mermaid in `figure-07-tera-framework.md`. To render, either copy that Mermaid block into a new file `figure-07a-tera-layers.mmd` and run the bash script, or paste it into `https://mermaid.live` and export as PDF.
- **F7(b)** — Cross-cutting concerns view. Best rendered in **draw.io** (free, https://app.diagrams.net) for the translucent-overlay effect that Mermaid does not support cleanly. Use the structured spec in `figure-07-tera-framework.md` as the drawing guide.
- **F7(c)** — Editorial / content-analytics worked-example overlay. Same approach as F7(b); use the cell-by-cell spec table.

For IEEE Access submission, the three sub-panels are composited into a single Figure 7 via LaTeX `subfigure` package or by composing them in draw.io and exporting one PDF.

## Step 3 — Render F8 (heatmap)

```bash
cd path/to/tera-agentic-rag
python3 scripts/render-heatmap.py \
    --threats security/threat-model.csv \
    --components cloud-reference-architecture/components.csv \
    --output figures/figure-08-threats-controls-heatmap.pdf
```

The script reads the threat-to-control matrix and the cloud-component CSV, computes per-cell densities for threats, controls, and observability, and emits a vector PDF heatmap. matplotlib (3.10+) is the only dependency.

## Step 4 — Verify each PDF

Open each output PDF in Preview (macOS) or any PDF viewer and check:

- [ ] Text is selectable (confirms vector text, not rasterized).
- [ ] Zooming reveals no pixelation (confirms vector rendering throughout).
- [ ] Page size is approximately the figure's natural extent (no excessive whitespace).
- [ ] Color palette is colorblind-friendly (Wong palette in the Mermaid sources, matplotlib defaults for the heatmap).
- [ ] Any text labels are readable at IEEE Access two-column width (typically 3.5 inches per column or 7.16 inches double-column).

## Step 5 — Embed in the manuscript LaTeX

In the IEEE Access LaTeX source, include each figure with:

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=\columnwidth]{figures/figure-01-prisma.pdf}
  \caption{PRISMA-style literature-selection flow. Counts: 420 records identified, 89 deduplicated, 331 records screened, 149 included.}
  \label{fig:prisma}
\end{figure}
```

Use `\columnwidth` for single-column figures (F1, F2, F4, F5, F6) and `\textwidth` inside `figure*` for double-column figures (F3, F7, F8).

## Troubleshooting

- **`mmdc` install hangs or fails.** Mermaid CLI bundles a Chromium download (~150 MB). On a slow connection, retry with `npm install @mermaid-js/mermaid-cli --no-fund --no-audit --verbose` from `figures/`. As a fallback, paste each `.mmd` source into `https://mermaid.live` and export PDF manually.
- **Mermaid output looks small or has padding.** Edit the figure header to add `%%{init: {'flowchart': {'htmlLabels': false}}}%%`, or post-process with `pdfcrop figure-01-prisma.pdf figure-01-prisma-cropped.pdf`.
- **matplotlib heatmap text overlaps cells.** Adjust the `figsize` parameter in `render-heatmap.py` from `(7.16, 4.8)` to a wider value such as `(9.0, 5.5)`.
- **draw.io export looks raster.** Use File > Export As > PDF with "Crop" enabled and "Embed Images" disabled.

## License

Figure source files and renderers are released under the same dual-license as the rest of the repository: CC-BY-4.0 for the figure content, MIT for the rendering scripts.
