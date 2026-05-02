# Trustworthy Agentic RAG for Enterprise AI — Survey Companion Repository

This repository is the supplementary-material package for the IEEE Access survey article *"Trustworthy Agentic RAG for Enterprise AI: A Systematic Survey and Framework for Architectures, Evaluation, Security, Governance, and Cloud-Native Deployment"* by Vinoth Nageshwaran (Business Insider, New York, NY, USA).

The repository releases the systematic-review protocol, search strings, screening log, BibTeX bibliography, and reusable artifacts that the paper contributes — the eight-dimension taxonomy of enterprise agentic RAG systems, the threat-to-control matrix, the agentic-RAG evaluation matrix, the cloud-native reference architecture component model, the governance and human-oversight checklist, the enterprise lifecycle, and the TERA framework grid.

## TERA — Trustworthy Enterprise RAG Agents

TERA is a layered, cloud-native, enterprise-focused framework for designing, evaluating, securing, governing, deploying, and operating agentic Retrieval-Augmented Generation (RAG) systems. It is organized as a 6×5 grid of vertical processing layers (L0 cloud foundation through L5 application) and cross-cutting concerns (C1 security, C2 evaluation, C3 observability, C4 governance, C5 LLMOps and continuous improvement).

## Why this repository exists

Three forms of usefulness:

1. **Reproducibility.** Every step of the systematic literature review is documented — search dates, search strings, inclusion criteria, deduplication procedure, screening log, quality assessment rubric, and PRISMA flow counts. A second reviewer can re-execute the protocol and arrive at a comparable corpus.
2. **Transparency.** The full BibTeX bibliography is published with provenance annotations and source-confidence flags. Preprints, peer-reviewed papers, standards, and industry reports are distinguished.
3. **Reuse.** The taxonomy, threat-to-control matrix, evaluation matrix, governance checklist, and reference architecture are released as machine-readable CSVs and structured Markdown. Practitioners can adopt them directly; researchers can extend them.

## Repository layout

```
tera-agentic-rag/
├── README.md
├── CITATION.cff
├── LICENSE
├── changelog.md
├── .gitignore
│
├── paper/
│   ├── contribution-summary.md
│   ├── supplementary-material-description.md
│   └── ai-use-disclosure.md         (author-authored)
│
├── literature-review/
│   ├── search-protocol.md
│   ├── search-strings.md
│   ├── inclusion-exclusion-criteria.md
│   ├── prisma-flow-data.csv
│   ├── screening-log.csv
│   ├── quality-assessment.csv
│   └── selected-papers.bib
│
├── taxonomy/
│   ├── enterprise-agentic-rag-taxonomy.csv
│   ├── architecture-patterns.csv
│   ├── autonomy-levels.csv
│   └── risk-classification.csv
│
├── evaluation/
│   ├── benchmarks-and-metrics.csv
│   ├── evaluation-framework.md
│   └── rag-agent-evaluation-checklist.md
│
├── security/
│   ├── threat-model.csv
│   └── mitigations-checklist.md
│
├── governance/
│   ├── governance-checklist.md
│   ├── human-in-the-loop-controls.md
│   ├── auditability-checklist.md
│   └── cloud-ops-controls.md
│
├── cloud-reference-architecture/
│   ├── architecture-description.md
│   └── components.csv
│
├── scripts/
│   ├── deduplicate_bibtex.py
│   ├── generate_prisma_counts.py
│   └── generate_summary_tables.py
│
└── release-notes/
    └── v1.0.md
```

## How to cite

If you use any artifact from this repository, please cite the IEEE Access paper and this repository. See `CITATION.cff` for machine-readable metadata; the recommended citation form is given there.

A Zenodo release will be archived at the time of acceptance with a citable DOI; please cite the Zenodo DOI when available.

## Quick references to key artifacts

| Artifact | Path | Description |
|---|---|---|
| Eight-dimension taxonomy | `taxonomy/enterprise-agentic-rag-taxonomy.csv` | Locate any enterprise agentic-RAG system as an eight-tuple coordinate |
| Threat-to-control matrix | `security/threat-model.csv` | 22 threats mapped to TERA layers, empirical anchors, mitigations, and open problems |
| Evaluation matrix | `evaluation/benchmarks-and-metrics.csv` | 28+ benchmarks classified by agentic capability and prescribed by autonomy level |
| Cloud-native components | `cloud-reference-architecture/components.csv` | 18 vendor-neutral components with security control and observability signal per component |
| Governance checklist | `governance/governance-checklist.md` | 32 controls anchored in NIST, OWASP, ISO/IEC, CSA |
| Bibliography | `literature-review/selected-papers.bib` | 149 verified entries; 74% peer-reviewed |

## Status

- **Version:** 0.9.0 (pre-submission scaffold)
- **Visibility:** Private during drafting and peer review; will be made public at acceptance, with a Zenodo-archived tagged release for citation.
- **Last refresh:** 2026-05-01 (round-3 corpus freeze)
- **Planned final search refresh:** 30 days before submission

## Maintenance plan

The repository will be maintained for at least 12 months after publication. Issues and pull requests are welcome. Maintenance commitments include: refreshing the bibliography on a six-month cycle for the first year; correcting verifiable errata; and accepting community contributions of additional empirical anchors for the threat matrix and benchmark matrix.

## Restrictions

Not included in this repository, by design:

- Copyrighted full-text PDFs of cited papers.
- Tables or figures copied or directly adapted from any prior work.
- Any private, employer-confidential, or customer material.
- API keys, cloud credentials, or internal architecture diagrams.

The repository is intended exclusively for legitimate scholarly utility, reproducibility, and practical adoption. Citations and stars should accrue from genuine use and not from artificial promotion.

## Contact

Vinoth Nageshwaran — vnageshwaran@gmail.com
