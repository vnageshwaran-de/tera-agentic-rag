# Cloud and Operations Controls for Enterprise Agentic RAG

The TERA L0 (cloud foundation) and C5 (LLMOps and continuous improvement) controls. Read alongside `cloud-reference-architecture/architecture-description.md` and `governance/governance-checklist.md` rows G19–G26.

## Identity and access management

- Per-agent identity (machine identity), not shared service accounts.
- Scoped credentials with short TTL.
- Least privilege on tools, vector stores, memory stores, and external APIs.
- Audit of role assignments per release.

## Network and isolation

- Default-deny egress; allow-list per agent.
- Private endpoints for vector store and KMS where the cloud supports it.
- Per-tenant cache namespace at every cache layer (KV, retrieval, output) to mitigate PROMPTPEEK-class attacks `wu2025promptpeek`.

## Secrets

- Centralized secrets manager (KMS / Vault).
- Per-agent secret scoping.
- Rotation policy with automated key rotation where possible.

## Continuous integration and deployment

- GitOps with eval-gated promotion `llmcicdenterprise2025ieee`.
- Pinned dependencies; lockfiles; immutable container images.
- Pre-promotion red-team gate (HarmBench / Agent Security Bench / AgentDojo).
- Rollback runbook tested per release.

## Observability

- OpenTelemetry GenAI semantic conventions `otel2024genai`.
- End-to-end traces (request → retrieval → plan → tool → response).
- Metrics: token cost, latency, error rate, retrieval hit ratio, faithfulness score, escalation rate.
- Logs: structured, signed, append-only.

## Drift detection

- Embedding drift: KL divergence of embedding distributions over time.
- Retrieval drift: distribution of retrieved sources / scores.
- Outcome drift: action success rate, escalation rate, faithfulness score.
- Alert thresholds reviewed quarterly.

## Cost management

- Per-agent token budget with circuit breakers.
- Cost-per-task tracked and reported.
- Cost-aware planning configured for long-horizon agents.

## Incident response

- Agent-specific runbook covering: prompt-injection incident, retrieval-poisoning incident, tool-misuse incident, memory-poisoning incident, multi-tenant leak.
- Forensic capability: replay any request from immutable audit log.
- Mandatory post-incident review.
