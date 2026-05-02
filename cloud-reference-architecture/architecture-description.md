# Cloud-Native Reference Architecture for Trustworthy Enterprise Agentic RAG

This document is the narrative companion to `components.csv` and to Figure 3 of the IEEE Access manuscript. The reference architecture is intentionally vendor-neutral. It identifies the components that any enterprise deployment needs and the trust boundaries that constrain how those components interact. It does not endorse any specific cloud provider, agent framework, or vector store.

## Layered model

The architecture is organized along the TERA vertical layers:

- **L0 — Cloud foundation.** Compute, storage, network, IAM, secrets, audit-log substrate.
- **L1 — Data and knowledge.** Source ingestion, parsing, chunking, embedding, indexing into vector and graph stores.
- **L2 — Retrieval.** Sparse, dense, hybrid, graph, multimodal, late-interaction retrieval; reranking.
- **L3 — Reasoning and planning.** Plan construction, reflection, memory, scratchpad, sub-goal decomposition.
- **L4 — Tool and action.** Tool discovery, parameter validation, action execution, side-effect handling.
- **L5 — Application and orchestration.** Single- or multi-agent workflow, user interaction, response composition.

## Trust boundaries

Trust boundaries are drawn explicitly:

- **Data trust boundary.** Between external sources and the L1 ingestion layer. Source authentication, hashing, and content scanning enforce the boundary.
- **Action trust boundary.** Between the L4 tool layer and external systems (databases, APIs, file systems, downstream services). Per-agent IAM, per-tool ACLs, and parameter validation enforce the boundary.
- **Human-oversight boundary.** Around the human-approval service. Cryptographic sign-off and queue-based approval enforce the boundary for high-risk actions.

## Cross-cutting concerns

The five TERA cross-cutting concerns overlay every layer:

- **C1 Security and privacy.** Input/output validation, secret handling, threat detection, privacy controls.
- **C2 Evaluation.** Continuous and pre-deployment evaluation against the agentic-RAG matrix.
- **C3 Observability and telemetry.** Tracing of retrievals, plans, tool calls, outcomes.
- **C4 Governance and human oversight.** Policy enforcement, approvals, audit trails, evidence artifacts.
- **C5 LLMOps and continuous improvement.** Versioning, deployment, rollback, feedback loops, drift detection.

## Vendor neutrality

For each component in `components.csv`, the design options column lists multiple vendor- and cloud-neutral implementations. We do not benchmark vendors; we identify the primitive that any deployment needs (e.g., a vector or graph store), what can go wrong (e.g., cross-tenant leakage), the security control required (e.g., tenant isolation), and the observability signal it should emit (e.g., query rate and hit ratio).

## Centralized vs. federated orchestration

The architecture supports both topologies:

- **Centralized orchestration.** A single agent orchestrator coordinates retrieval, planning, tool use, and action. Easier to monitor and govern; potential bottleneck and single point of failure.
- **Federated orchestration.** Multiple coordinating orchestrators, each controlling a subset of agents. Better scale, fault tolerance, and data locality; harder governance and observability.

Choice between the two is a function of the deployment's risk class (Dimension 7), regulatory environment (Dimension 7), and scale.

## Cloud vs. edge

For latency-sensitive or privacy-sensitive deployments, edge or hybrid deployments are appropriate. The component model is the same; what changes is which components run at the edge vs. the cloud and where the trust boundaries are drawn.

## Anti-patterns

- Single-tenant assumptions in multi-tenant infrastructure.
- IAM over-permissioning.
- Embedding stores without access control or encryption at rest.
- Tool registries without provenance pinning.
- Memory stores without write authorization or lineage.
- Agent communications without an audit log.

## How to walk this architecture

For a candidate deployment, traverse `components.csv` and confirm each component has: (a) a chosen design option, (b) the security control implemented, (c) the observability signal emitted, and (d) the corresponding governance evidence artifact from `governance/governance-checklist.md`. Components missing any of (a)–(d) are explicit deployment risks.
