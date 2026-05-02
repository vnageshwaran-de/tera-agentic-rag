# Governance and Human-Oversight Checklist for Enterprise Agentic RAG

This checklist is the operational artifact of TERA's C4 cross-cutting concern. It is anchored in NIST AI 600-1 (Generative AI Profile) [`nist2024genaiprofile`], NIST SP 800-218A (Secure Software Development Practices for Generative AI) [`nist2024ssdfgenai`], OWASP Top 10 for LLM Applications 2025 [`owasp2025llmtop10`], OWASP Top 10 for Agentic Applications [`owasp2025agentictop10`], ISO/IEC 42001:2023 (AI Management System) [`iso420012023`], and the CSA AI Controls Matrix [`csa2025aicm`].

Each control specifies its objective, an implementation pattern, the evidence artifact required for audit, the residual risk that remains after the control is in place, and the anchor reference. The 32 controls below are designed to be cited individually by row ID (e.g., "G15") in compliance documents and successor research.

## Strategy and Risk

**G1 — Risk classification per use case.** *Objective.* Every deployed agentic-RAG use case has a documented risk tier from Section 4 Dimension 7. *Implementation.* Risk classification matrix mapped to NIST AI 600-1 risk areas and EU AI Act tier. *Evidence.* Signed risk register. *Residual risk.* Mis-classification on edge cases. *Anchor.* `nist2024genaiprofile`, `euaiact2024`.

**G2 — AI inventory and ownership.** *Objective.* Every agent, retriever, tool, and memory store has a named owner. *Implementation.* AI asset inventory linked to IAM identities. *Evidence.* Inventory report with named owners and last-review date. *Residual risk.* Stale ownership after personnel changes. *Anchor.* `iso420012023`.

## Data and Knowledge (TERA L1)

**G3 — Source provenance.** *Objective.* Every corpus source can be traced from chunk to citation. *Implementation.* Source manifest with content hashing and ingestion-time signature. *Evidence.* Signed manifest per ingestion run. *Residual risk.* Provenance forgery from a compromised upstream source. *Anchor.* `niu2024ragtruth`.

**G4 — PII scanning at ingestion.** *Objective.* PII is identified and either redacted, encrypted, or excluded from the corpus per data-classification policy. *Implementation.* Scanner + redaction pipeline integrated into ingestion. *Evidence.* Scan log with redaction counts per source. *Residual risk.* PII leakage through generated summaries even when input is clean. *Anchor.* OWASP LLM02 `owasp2025llmtop10`.

**G5 — Retention and deletion.** *Objective.* Source documents and embeddings honor retention policy and DSAR / RTBF deletion requests. *Implementation.* Retention metadata on each chunk and embedding; deletion APIs. *Evidence.* Retention audit; deletion-request log. *Residual risk.* Delayed propagation to derived caches and replicas. *Anchor.* GDPR Art. 17; EU AI Act `euaiact2024`.

## Retrieval (TERA L2)

**G6 — Retrieval-quality SLO.** *Objective.* Retrieval quality (NDCG, recall, retrieval-quality `salemi2024evalretrieval`) meets a documented SLO before deployment. *Implementation.* Eval harness in CI. *Evidence.* Continuous eval report per build. *Residual risk.* Drift between deployments. *Anchor.* `salemi2024evalretrieval`.

**G7 — Faithfulness SLO.** *Objective.* RAG faithfulness ≥ X measured by RAGAS / ARES / SYNCHECK before production promotion. *Implementation.* Per-build eval gates. *Evidence.* Faithfulness report; drift dashboard. *Residual risk.* 57% of attributions can lack faithfulness even when correctness is high. *Anchor.* `esragas2024`, `saadfalcon2024ares`, `wu2024synccheck`, `wallat2025correctnessfaithfulness`.

## Reasoning and Planning (TERA L3)

**G8 — Plan-trace audit.** *Objective.* The agent's plan-of-actions is captured for every consequential request. *Implementation.* Structured plan log with reasoning trace. *Evidence.* Plan log retention. *Residual risk.* Plan obfuscation by adversarial inputs. *Anchor.* `liu2024agentbench`.

**G9 — Multi-turn safety calibration.** *Objective.* The system resists multi-turn jailbreak and prompt-injection escalation. *Implementation.* Conversation-safety classifier; refusal calibration. *Evidence.* Red-team report (HarmBench / Crescendo / TwinBreak coverage). *Residual risk.* Long-context defense gaps. *Anchor.* `russinovich2025crescendo`, `krauss2025twinbreak`, `mazeika2024harmbench`.

## Tools and Actions (TERA L4)

**G10 — Tool ACLs per agent identity.** *Objective.* Each agent has the minimum tool set needed for its role. *Implementation.* Per-agent IAM role with scoped credentials. *Evidence.* IAM diff and review log. *Residual risk.* Privilege creep. *Anchor.* `csa2025aicm`.

**G11 — Tool input/output validation.** *Objective.* Every tool call's inputs and outputs are validated against schema. *Implementation.* Schema validators plus StruQ-style structured queries. *Evidence.* Validation log with reject reasons. *Residual risk.* Encoded bypass. *Anchor.* `chen2025struq`.

**G12 — Tool provenance.** *Objective.* Tool definitions and code are provenance-pinned and signed. *Implementation.* Hash-pinned tool registry; SBOM. *Evidence.* Tool registry diff; SBOM per release. *Residual risk.* ToolHijacker via malicious tool-doc injection. *Anchor.* `shi2026toolhijacker`, `dong2025philosophersstone`.

## Memory (TERA L3)

**G13 — Memory write authorization.** *Objective.* Only authorized agents and processes can write to long-term memory. *Implementation.* Memory ACL with per-write authentication. *Evidence.* Memory write log. *Residual risk.* Cross-session contamination. *Anchor.* `chen2024agentpoison`.

**G14 — Memory provenance and lineage.** *Objective.* Every memory entry is tagged with its source agent, source action, and time. *Implementation.* Source-tagged entries; lineage graph. *Evidence.* Lineage export. *Residual risk.* Tag stripping by an attacker. *Anchor.* `memorygraft2025`, `memorypoisoning2026arxiv`.

## Human-in-the-Loop (TERA C4)

**G15 — Risk-tiered HITL checkpoints.** *Objective.* Higher risk tiers require human approval before action. *Implementation.* Tiered approval gates; cryptographic sign-off. *Evidence.* Approval log per action. *Residual risk.* Approval fatigue at high escalation rate. *Anchor.* `hitl2025entropy` (10–15% escalation rate is a citable design heuristic).

**G16 — Escalation SLO.** *Objective.* Escalations from autonomous to human review meet a documented SLO. *Implementation.* Routing rules with queues. *Evidence.* Escalation telemetry. *Residual risk.* Quiet auto-approval when humans are unavailable. *Anchor.* OWASP Agentic LLM06 `owasp2025agentictop10`.

## Security (TERA C1)

**G17 — Per-release threat model.** *Objective.* Each release is mapped to the TERA threat-to-control matrix; new threats trigger review. *Implementation.* Threat-modeling artifact per release. *Evidence.* Threat-model document. *Residual risk.* Drift from threat model in production. *Anchor.* `aiagentsthreat2025acm`.

**G18 — Red-team evaluation.** *Objective.* Agent system passes a red-team evaluation suite covering at least HarmBench, Agent Security Bench, AgentDojo, AILuminate. *Implementation.* Automated red-team in CI; manual red-team pre-major release. *Evidence.* Red-team report with pass/fail per test. *Residual risk.* Coverage gap on novel attack classes. *Anchor.* `mazeika2024harmbench`, `zhang2025agentsecuritybench`, `debenedetti2024agentdojo`, `ailuminate2025`.

**G19 — Prompt-injection detection at runtime.** *Objective.* Production traffic is monitored for prompt-injection attempts. *Implementation.* DataSentinel or PromptShield (or equivalent) at the LLM gateway. *Evidence.* Detection log with alert rate and human-confirmed precision. *Residual risk.* High-FPR cost; novel injection patterns. *Anchor.* `datasentinel2025sp`, `jacob2025promptshield`, `promptlocate2026sp`.

## Privacy and Cloud Isolation (TERA L0)

**G20 — Cross-tenant cache isolation.** *Objective.* No tenant's prompt or response is exposed via shared infrastructure caches (KV cache, retrieval cache, or output cache). *Implementation.* Per-tenant cache namespace; isolation tests. *Evidence.* Isolation test results. *Residual risk.* PROMPTPEEK-class side-channel attacks even with isolation. *Anchor.* `wu2025promptpeek`, `nist2024ssdfgenai`.

**G21 — Embedding-store privacy.** *Objective.* Embedding stores resist embedding-inversion attacks where required by data classification. *Implementation.* Encrypted embeddings; vector-store ACLs. *Evidence.* Inversion-resistance test. *Residual risk.* Embedding inversion still feasible against unencrypted stores. *Anchor.* `embeddinginversion2024arxiv`, `transferableinversion2024`.

## Multi-Agent Governance (TERA L5)

**G22 — Inter-agent message audit.** *Objective.* Every agent-to-agent message is logged. *Implementation.* Message log with role and content. *Evidence.* Message log retention. *Residual risk.* Steganographic collusion via plain text. *Anchor.* `motwani2024secretcollusion`.

**G23 — Role policy enforcement.** *Objective.* Each agent operates only within its declared role. *Implementation.* Role validators; role-fidelity monitoring. *Evidence.* Role-fidelity report. *Residual risk.* Role drift over time. *Anchor.* `qian2024chatdev`.

## Operations and CI/CD (TERA C5)

**G24 — Versioned deploys with eval-gated promotion.** *Objective.* No deploy reaches production without passing eval gates. *Implementation.* GitOps with eval-gated promotion. *Evidence.* Deploy manifest. *Residual risk.* Bad rollback if rollback target was previously degraded. *Anchor.* `llmcicdenterprise2025ieee`.

**G25 — Drift detection.** *Objective.* Embedding, retrieval, plan, and action distributions are monitored. *Implementation.* Distribution monitors with alerting. *Evidence.* Drift report. *Residual risk.* Slow drift below alert threshold. *Anchor.* `mdpi2025mlopstoLlmops`, `llmopsreview2025`.

**G26 — Cost SLO per agent.** *Objective.* Agent cost per task is monitored and bounded. *Implementation.* Token budget per agent; circuit breakers. *Evidence.* Cost-per-task report. *Residual risk.* Hidden cost growth from longer agent loops. *Anchor.* `mohammadi2025agenteval`.

## Audit and Accountability

**G27 — Append-only event store.** *Objective.* All consequential events are written to an immutable, signed event log. *Implementation.* WORM storage with cryptographic chaining. *Evidence.* Audit-chain export. *Residual risk.* Schema evolution can break consumers. *Anchor.* `nist2024genaiprofile`.

**G28 — End-to-end tracing.** *Objective.* Each user request can be traced through retrieval, planning, tool calls, and outcome. *Implementation.* OpenTelemetry GenAI semantic conventions. *Evidence.* Sampled trace export. *Residual risk.* Sampling loss on tail traffic. *Anchor.* `otel2024genai`.

## Compliance and Disclosure

**G29 — Mapping to controls framework.** *Objective.* Implemented controls map to a recognized framework (AICM, ISO 42001 Annex A, NIST AI RMF). *Implementation.* Control register. *Evidence.* Mapping report. *Residual risk.* Mapping staleness. *Anchor.* `csa2025aicm`, `iso420012023`.

**G30 — End-user disclosure.** *Objective.* Users are informed when interacting with an agent. *Implementation.* UI badge and documentation. *Evidence.* UX evidence. *Residual risk.* Disclosure clarity for embedded agents. *Anchor.* EU AI Act Art. 50 `euaiact2024`.

## Reproducibility

**G31 — Pinned dependencies and frozen eval sets.** *Objective.* Models, retrievers, tool versions, and eval sets are pinned per release. *Implementation.* Lockfiles; immutable container images; eval-set hashes. *Evidence.* Image digest and eval-set hash per release. *Residual risk.* Live-call non-determinism from external models. *Anchor.* `llmopsreview2025`, `tamber2025faithevolving`.

## Continuous Improvement and AI-Use Disclosure

**G32 — Post-incident review and AI-use disclosure for publications.** *Objective.* Incidents prompt a blameless review, and any AI-assisted research output carries an explicit AI-use disclosure. *Implementation.* PIR template; per-publication disclosure statement. *Evidence.* PIR document; signed disclosure. *Residual risk.* PIR fatigue; incomplete disclosure. *Anchor.* IEEE Access AI-disclosure policy; `nist2024genaiprofile`.

---

## How to use this checklist

1. **At design time.** For every new agentic-RAG use case, walk the 32 controls and document which apply at the use case's risk tier (Dimension 7).
2. **At deploy time.** Treat each control's *evidence artifact* as a release gate.
3. **At audit time.** Map each control's evidence to the relevant section of NIST AI 600-1, ISO/IEC 42001 Annex A, or the CSA AICM.
4. **In publications and incident reviews.** Cite controls by row ID for traceability.
