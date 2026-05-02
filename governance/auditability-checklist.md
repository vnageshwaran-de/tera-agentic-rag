# Auditability Checklist for Enterprise Agentic RAG

Operational artifact of TERA C4 governance and audit. The checklist is designed so an external auditor can answer "what happened, who authorized it, and was it within policy" for any production action.

## Event capture

- [ ] Every consequential agent action emits a signed event to the audit log store (G27 in the governance checklist).
- [ ] Events conform to a documented schema covering: timestamp, agent identity, request ID, retrieved-set ID, plan ID, tool calls, action outcome, approval evidence, and policy decisions.
- [ ] Event log is append-only (WORM) with cryptographic chaining.
- [ ] Audit log retention meets regulatory requirements for the applicable risk tier.

## Provenance

- [ ] Source provenance for retrieval (G3): chunk ID → source document ID → ingestion-time hash.
- [ ] Memory provenance (G14): memory entry → source agent → source action.
- [ ] Tool provenance (G12): tool ID → tool definition hash → registry version.
- [ ] Model provenance (G26): model ID → checksum → SBOM entry.

## Lineage

- [ ] Lineage graph available from any output back to: input prompt, retrieved set, plan, tool calls, model invocations.
- [ ] Lineage graph queryable by agent, by user, by request ID, by time window.

## Tracing

- [ ] OpenTelemetry GenAI semantic conventions applied (G28; `otel2024genai`).
- [ ] End-to-end correlation IDs propagated.
- [ ] Trace sampling policy documented; tail traffic captured.

## Approval evidence

- [ ] HITL approvals stored with cryptographic signatures and tied to the request ID.
- [ ] Approval-to-action latency measured and bounded.
- [ ] Override actions logged with explicit override reason.

## Audit reports

- [ ] Periodic audit report generation (monthly or per regulatory cadence).
- [ ] Per-control evidence collection scripted and reproducible.
- [ ] Mapping to control framework (AICM, ISO/IEC 42001 Annex A, NIST AI 600-1) refreshed quarterly.

## Incident response

- [ ] Incident-response runbook for agent-specific incidents (G27).
- [ ] Forensic capability: trace any action to its root cause within agreed SLO.
- [ ] Post-incident review process with explicit documentation of the missing control.

## External attestations

- [ ] Annual third-party assessment for regulated tiers.
- [ ] Public disclosure of attestations where required.
