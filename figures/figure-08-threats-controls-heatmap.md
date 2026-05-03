# Figure 8 — Threats × Controls × Observability Heatmap on the TERA Grid

A 6 × 5 cell projection of Tables 5 (threats), 7 (governance controls), and 6 (observability signals from cloud components) onto the same TERA grid as Figure 7. The visualization is a heatmap with three encoded channels per cell.

## Visual encoding

Each cell is divided into three sub-regions (e.g., a triangulated cell or three vertical bars) encoding:

- **Threat density (red).** Number of distinct threat IDs from `security/threat-model.csv` whose `tera_layers` field contains the cell's layer L_x. Higher density = darker red.
- **Control density (green).** Number of distinct control IDs from `governance/governance-checklist.md` whose anchor reference applies to the cell's (layer × concern). Higher density = darker green.
- **Observability density (blue).** Number of components from `cloud-reference-architecture/components.csv` whose layer matches L_x and whose `observability_signal` is non-empty. Higher density = darker blue.

Cells with high red and low green are explicit deployment risks; cells with high blue and low green are observable but ungoverned; cells with all three high are well-served.

## Computed cell summaries (representative)

| Cell | Threats | Controls | Observability |
|---|---|---|---|
| L0 × C1 | High (PROMPTPEEK, embedding inversion via store) | Medium (G16, G20, G21) | High (audit log, traces) |
| L1 × C1 | High (PoisonedRAG, jamming, Phantom, backdoored retriever, embedding inversion) | Medium (G3, G4, G5) | Medium |
| L2 × C2 | High | High (G6, G7) | High |
| L3 × C1 | High (direct injection, jailbreak, multi-turn) | Medium | Low — plan tracing under-instrumented |
| L4 × C1 | Very high (ToolHijacker, Prompt-to-SQL, plugin Trojan, excessive agency) | High (G10, G11, G12) | Medium |
| L4 × C4 | Medium | Very high (G15, G16) | High |
| L5 × C1 | Medium (multi-agent collusion) | Low — open problem | Low — collusion detection unsolved |

## Production notes

- Best rendered as a colored heatmap in `matplotlib` or as a draw.io grid with per-cell tri-color bars.
- Companion repository `scripts/generate_summary_tables.py` can be extended to compute the three channel values automatically by joining the threat-model, governance, and components CSVs against the (layer × concern) coordinates.
- Caption ≤ 75 words highlighting that L4 × C1 (tool / action × security) and L5 × C1 (multi-agent application × security) are the densest deployment-risk cells.
