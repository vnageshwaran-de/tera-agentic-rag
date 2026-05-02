# Contribution Summary

The IEEE Access survey article and this companion repository together make six concrete contributions.

1. **TERA framework.** A layered, cloud-native, enterprise-focused framework integrating eleven engineering concerns — architecture, retrieval, agent reasoning and planning, tool use and action, security, evaluation, observability, governance, human oversight, operations, and continuous improvement — into a single deployable model. The framework is organized as a 6×5 grid of vertical layers (L0–L5) and cross-cutting concerns (C1–C5). Each cell prescribes a design pattern, evaluation method, security control, governance artifact, and observability signal. Empty cells are explicit deployment risks and become roadmap items.

2. **Eight-dimension taxonomy of enterprise agentic RAG systems.** Dimensions: agent structure, retrieval type, memory type, tool integration, autonomy level, deployment mode, risk class, and governance level. Released as `taxonomy/enterprise-agentic-rag-taxonomy.csv`. Reusable as a coordinate system for any candidate enterprise deployment.

3. **Threat-to-control matrix for agentic RAG.** A formal mapping from each agentic-RAG threat to its root cause, the affected TERA layers, an empirical impact citation, detection signal, mitigation pattern, and the residual research question. Released as `security/threat-model.csv`. Anchored in OWASP LLM Top 10 (2025), OWASP Top 10 for Agentic Applications (2025), NIST AI 600-1, and the CSA AI Controls Matrix.

4. **Agentic-RAG evaluation matrix.** A benchmark and metric matrix specialized to agentic-RAG capabilities (retrieval × planning × tool use × action × cost × safety) with prescriptions tied to autonomy level. Released as `evaluation/benchmarks-and-metrics.csv`. Builds on Mohammadi et al. 2025 (KDD) and Yu et al. 2024 RAG-evaluation survey.

5. **Cloud-native reference architecture component model.** Eighteen vendor-neutral components with function, design options, failure risks, security control, and observability signal per component. Released as `cloud-reference-architecture/components.csv`. Designed to be portable across AWS, Azure, GCP, and on-premise deployments.

6. **Governance, lifecycle, and research roadmap artifacts.** A 32-control governance and human-oversight checklist, a 10-stage enterprise lifecycle, and a 16-item research roadmap derived from empty TERA cells. Released as `governance/governance-checklist.md`, `taxonomy/risk-classification.csv`, and within the manuscript's Table 8.
