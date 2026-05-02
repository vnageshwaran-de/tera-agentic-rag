# Supplementary Material Description (for IEEE Access submission)

This document is for the IEEE Access submission portal's supplementary-material field. Copy the relevant section into the cover letter and the supplementary-material upload description.

## Statement for the manuscript

> Supplementary materials for this paper — including the systematic-review protocol, search strings, screening log, BibTeX bibliography, and the reusable artifacts of the TERA framework (eight-dimension taxonomy, threat-to-control matrix, agentic-RAG evaluation matrix, cloud-native reference architecture component model, governance and human-oversight checklist, lifecycle, and research roadmap) — are publicly available at the companion repository. A tagged release is archived on Zenodo with a citable DOI.

## What the supplementary package contains

1. `literature-review/search-protocol.md` — full systematic-review protocol with research questions, databases, search dates, inclusion / exclusion criteria, screening process, quality-assessment rubric, and threats to validity.
2. `literature-review/search-strings.md` — exact search strings executed per database family, organized by research question.
3. `literature-review/inclusion-exclusion-criteria.md` — bullet-form criteria for replication.
4. `literature-review/prisma-flow-data.csv` — counts at each PRISMA stage, ready to plot.
5. `literature-review/screening-log.csv` — per-record screening outcomes with TERA layer/concern coding.
6. `literature-review/quality-assessment.csv` — per-record 0–2 ordinal scoring across eight dimensions.
7. `literature-review/selected-papers.bib` — 150-entry verified bibliography with provenance and source-confidence flags.
8. `taxonomy/*.csv` — eight-dimension taxonomy, architecture patterns, autonomy levels, risk classes.
9. `evaluation/benchmarks-and-metrics.csv` — 33 benchmarks classified by agentic capability and prescribed by autonomy level.
10. `evaluation/evaluation-framework.md` — the agentic-RAG evaluation framework narrative.
11. `evaluation/rag-agent-evaluation-checklist.md` — pre-deployment evaluation checklist.
12. `security/threat-model.csv` — 22 threats with empirical anchors and mitigations.
13. `security/mitigations-checklist.md` — defensive-control checklist.
14. `governance/governance-checklist.md` — 32-control governance and human-oversight checklist.
15. `governance/human-in-the-loop-controls.md` — HITL control patterns.
16. `governance/auditability-checklist.md` — audit-readiness controls.
17. `governance/cloud-ops-controls.md` — cloud and ops control patterns.
18. `cloud-reference-architecture/architecture-description.md` — narrative companion to the reference architecture.
19. `cloud-reference-architecture/components.csv` — 18 components with controls and observability signals.
20. `scripts/` — Python utilities for deduplication, PRISMA-count regeneration, and table generation. MIT license.
21. `release-notes/v1.0.md` — version notes for the release tagged at acceptance.

## File formats

- Tables and matrices: machine-readable CSV with UTF-8 encoding, header row, and bibliographic key references in their own columns.
- Narrative artifacts: Markdown.
- Code: Python 3.10+, no external dependencies beyond the standard library.
- Bibliography: BibTeX.

## Reproducibility commitments

- The repository is versioned with semantic versioning and a `changelog.md`.
- A frozen Zenodo-archived release is created at the time of paper acceptance.
- The repository will be maintained for at least 12 months after publication; refresh cadence and acceptance criteria for community contributions are documented in `README.md`.
