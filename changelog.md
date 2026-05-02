# Changelog

All notable changes to this repository are documented here. The repository follows [Semantic Versioning](https://semver.org/) and the [Keep a Changelog](https://keepachangelog.com/) format.

## [Unreleased]

### Planned for v1.0
- Final search refresh 30 days before paper submission.
- Manuscript draft (Phase 8 deliverable).
- Final tagged release archived to Zenodo for citable DOI.
- Public visibility on acceptance.

## [0.9.0] — 2026-05-01

### Added
- Initial systematic review protocol (`literature-review/search-protocol.md`).
- Bibliography of 150 verified entries (`literature-review/selected-papers.bib`); 88 peer-reviewed conference, 22 peer-reviewed journal, 9 standards/governance, 2 industry protocols, 29 preprints retained where peer-reviewed equivalents are absent.
- Screening log (`literature-review/screening-log.csv`).
- PRISMA-style flow data (`literature-review/prisma-flow-data.csv`); 420 identified → 89 deduplicated → 150 included.
- Eight-dimension taxonomy of enterprise agentic-RAG systems (`taxonomy/`).
- Threat-to-control matrix of 22 threats (`security/threat-model.csv`).
- Agentic-RAG evaluation benchmark and metric matrix (`evaluation/benchmarks-and-metrics.csv`).
- Cloud-native deployment component matrix of 18 components (`cloud-reference-architecture/components.csv`).
- Governance and human-oversight checklist of 32 controls (`governance/governance-checklist.md`).
- TERA framework grid (6×5) cell summaries.
- Reproducibility scripts for deduplication, PRISMA counts, and table generation.

### Provenance
- Round-1 corpus (71 entries) compiled 2026-05-01.
- Round-2 expansion (33 additions) committed same day.
- Round-3 expansion (45 additions, plus 1 SearchExpert via author-supplied PDF) committed same day; 21 originally-Anonymous entries upgraded with verified author lists, DOIs, and provenance notes.

### Notes
- AI assistance was used in the literature search, screening synthesis, and artifact drafting. The disclosure statement is authored separately by the author and is included in the manuscript Acknowledgments.
- The repository is private during drafting and review; planned public release at acceptance with a Zenodo DOI.
