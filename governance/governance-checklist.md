# Governance and Human-Oversight Checklist for Trustworthy Enterprise Agentic RAG

This 32-control checklist (G1-G32) operationalizes Section 8 of
*Trustworthy Agentic RAG for Enterprise AI* (Nageshwaran, IEEE Access
2026). Each control specifies a control objective, an implementation
pattern, the evidence artifact required for audit, the residual risk
that remains after the control is in place, and the anchor reference
among the standards documents inventoried in §8.1.

The checklist is **compositional**: a deployment is admissible at a
given (autonomy, risk, governance) coordinate if and only if the
corresponding subset of these 32 controls is implemented with current
evidence artifacts. The mapping from coordinate to control subset is
specified in §8.1-§8.9 of the article.

Controls are anchored in NIST AI 600-1, NIST SP 800-218A, ISO/IEC
42001:2023, EU AI Act, OWASP Top 10 for LLM Applications (2025),
OWASP Top 10 for Agentic Applications (December 2025), the Cloud
Security Alliance AI Controls Matrix, and the CSA NIST AI RMF
Agentic Profile working draft.

---

## Strategy and risk classification

### G1 — Documented risk tier per use case

- **Objective.** Every agentic-RAG deployment is classified into a
  documented risk tier before promotion.
- **Implementation.** Risk-classification matrix anchored in NIST AI
  600-1 risk areas and EU AI Act tiers.
- **Evidence.** Signed risk register entry per deployment.
- **Residual risk.** Mis-classification.
- **Anchor.** `nist2024genaiprofile`, `euaiact2024`.

---

## Data and retrieval

### G2 — Source provenance for all corpus content

- **Objective.** Every corpus chunk carries source provenance.
- **Implementation.** Source manifest plus content hash at ingestion.
- **Evidence.** Signed manifest, append-only.
- **Residual risk.** Provenance forgery.
- **Anchor.** `niu2024ragtruth`.

### G3 — PII scanning at ingestion

- **Objective.** PII is detected and handled per policy at ingestion.
- **Implementation.** PII scanner with configurable redaction.
- **Evidence.** Scan log and redaction events.
- **Residual risk.** PII leakage in downstream summaries.
- **Anchor.** OWASP LLM02 (sensitive info disclosure).

### G4 — Retrieval-quality service-level objective

- **Objective.** Retrieval quality is monitored against an explicit SLO.
- **Implementation.** Eval harness in CI; production sampling.
- **Evidence.** Continuous eval report.
- **Residual risk.** Drift between deployments.
- **Anchor.** `salemi2024evalretrieval`.

### G5 — Faithfulness SLO

- **Objective.** Generated outputs meet a named faithfulness SLO.
- **Implementation.** RAGAS / ARES / SYNCHECK gates pre-deployment;
  SYNCHECK sampling in production.
- **Evidence.** Per-build eval report with faithfulness score.
- **Residual risk.** Citation faithfulness `wallat2025correctnessfaithfulness`.
- **Anchor.** `esragas2024`, `saadfalcon2024ares`, `wu2024synccheck`.

---

## Reasoning and tool boundaries

### G6 — Plan-trace audit

- **Objective.** Reasoning plans are auditable post-hoc.
- **Implementation.** Capture plan-of-actions trace per request.
- **Evidence.** Plan log with correlation ID.
- **Residual risk.** Plan obfuscation.
- **Anchor.** `liu2024agentbench`.

### G7 — Tool ACL per agent

- **Objective.** Each agent has the minimum tool surface required for
  its role.
- **Implementation.** Per-agent IAM role with tool-scoped permissions.
- **Evidence.** IAM diff per release.
- **Residual risk.** Privilege creep over time.
- **Anchor.** `csa2025aicm`.

### G8 — Tool input/output validators

- **Objective.** Tool calls are validated against schema and against
  prompt-injection signatures.
- **Implementation.** OpenAPI schema validation + StruQ structured
  query.
- **Evidence.** Validation log; rejection events.
- **Residual risk.** Encoded bypass not yet captured by validator.
- **Anchor.** `chen2025struq`.

---

## Memory

### G9 — Memory write authorization

- **Objective.** Writes to long-term memory require authorization.
- **Implementation.** Memory ACL keyed to agent role and session.
- **Evidence.** Write log.
- **Residual risk.** Cross-session contamination.
- **Anchor.** `chen2024agentpoison`.

### G10 — Memory provenance

- **Objective.** Every memory entry carries provenance.
- **Implementation.** Source-tagged memory entries; lineage graph.
- **Evidence.** Lineage graph queryable per entry.
- **Residual risk.** Tag stripping under adversarial conditions.
- **Anchor.** `memorygraft2025`.

---

## Human-in-the-loop

### G11 — Risk-tiered checkpoint

- **Objective.** Higher-risk actions require human approval.
- **Implementation.** Tiered approval gates calibrated to autonomy
  level and risk class.
- **Evidence.** Approval evidence with cryptographic sign-off.
- **Residual risk.** Approval fatigue degrading judgment.
- **Anchor.** `hitl2025entropy`.

### G12 — Escalation SLO

- **Objective.** Escalation rate is measured and meets an SLO.
- **Implementation.** Routing and queue with SLA monitoring; mature
  deployments target a 10–15% escalation rate.
- **Evidence.** Escalation telemetry.
- **Residual risk.** Quiet auto-approval.
- **Anchor.** OWASP Agentic LLM06.

---

## Security

### G13 — Threat model per release

- **Objective.** A current threat model exists for every release.
- **Implementation.** TERA threat-to-control matrix (article Table V)
  refreshed per release.
- **Evidence.** Threat-model document with residual-risk register.
- **Residual risk.** Drift between threat model and deployed system.
- **Anchor.** `aiagentsthreat2025acm`.

### G14 — Red-team evaluation

- **Objective.** Every release is challenged with a current
  red-team suite.
- **Implementation.** HarmBench, Agent Security Bench, AgentDojo,
  with domain-specific probes added at higher tiers.
- **Evidence.** Red-team report.
- **Residual risk.** Coverage gap against novel attack classes.
- **Anchor.** `mazeika2024harmbench`, `zhang2025agentsecuritybench`.

### G15 — Prompt-injection detection

- **Objective.** Prompt-injection attempts are detected at the input
  boundary.
- **Implementation.** DataSentinel, PromptShield (65.3% TPR at 0.1%
  FPR), or PromptLocate.
- **Evidence.** Detection log with FPR/TPR rates per release.
- **Residual risk.** High-FPR cost on legitimate user prompts.
- **Anchor.** `datasentinel2025sp`, `jacob2025promptshield`.

---

## Privacy and cloud isolation

### G16 — Cross-tenant isolation

- **Objective.** Multi-tenant infrastructure does not leak across
  tenants.
- **Implementation.** Per-tenant cache namespacing; vector-store ACL;
  KMS-managed keys.
- **Evidence.** Cross-tenant isolation test report.
- **Residual risk.** KV-cache leakage `wu2025promptpeek`.
- **Anchor.** NIST SP 800-218A `nist2024ssdfgenai`.

---

## Multi-agent governance

### G17 — Inter-agent message audit

- **Objective.** Inter-agent communications are logged and
  monitorable.
- **Implementation.** Logged communications with content hashing.
- **Evidence.** Message log; cross-agent trace.
- **Residual risk.** Steganographic collusion `motwani2024secretcollusion`.
- **Anchor.** OWASP Agentic Top 10.

### G18 — Role-policy enforcement

- **Objective.** Each agent role is enforced at run-time, not only
  at design time.
- **Implementation.** Per-role prompts and validators.
- **Evidence.** Role-fidelity report.
- **Residual risk.** Role drift over long sessions.
- **Anchor.** `qian2024chatdev`.

### G19 — Multi-agent admissibility

- **Objective.** Multi-agent deployments at supervised-action or
  autonomous-action autonomy levels require strong inter-agent
  message canaries and conservative role policies until
  collusion-detection at production scale exists.
- **Implementation.** Inter-agent canary tokens; conservative role
  policies.
- **Evidence.** Canary-detection report.
- **Residual risk.** Novel collusion patterns not captured by
  canaries.
- **Anchor.** `motwani2024secretcollusion`.

---

## Operations

### G20 — Versioned deploys with eval-gated promotion

- **Objective.** Deployments are versioned, evaluated, and reversible.
- **Implementation.** GitOps with eval-gated promotion; tested
  rollback runbook.
- **Evidence.** Deploy manifest with eval contract version.
- **Residual risk.** Bad rollback under partial-failure conditions.
- **Anchor.** `llmcicdenterprise2025ieee`.

### G21 — Drift detection

- **Objective.** Embedding, retrieval, faithfulness, and outcome
  distributions are monitored.
- **Implementation.** Distribution monitors with calibrated alert
  thresholds.
- **Evidence.** Drift report per monitored metric.
- **Residual risk.** Slow drift below alert threshold.
- **Anchor.** `llmopsreview2025`.

### G22 — Cost SLO

- **Objective.** Per-agent token cost is measured and bounded.
- **Implementation.** Token budget per agent at the LLM gateway;
  cost-shaping policy.
- **Evidence.** Cost-per-task report.
- **Residual risk.** Hidden cost growth from tool-call recursion.
- **Anchor.** `llmopsreview2025`.

---

## Audit

### G23 — Append-only event store

- **Objective.** All consequential events are recorded in an
  append-only audit store.
- **Implementation.** WORM storage with cryptographic signing per
  event.
- **Evidence.** Audit-chain manifest.
- **Residual risk.** Schema evolution invalidating older entries.
- **Anchor.** NIST AI 600-1 `nist2024genaiprofile`.

### G24 — End-to-end trace per request

- **Objective.** Every user request is reconstructable from
  immutable telemetry.
- **Implementation.** OpenTelemetry GenAI semantic conventions; per-
  request correlation ID propagated through every component.
- **Evidence.** Trace export keyed by correlation ID.
- **Residual risk.** Sampling loss at high request volume.
- **Anchor.** `otel2024genai`.

---

## Compliance

### G25 — Mapping to controls framework

- **Objective.** Controls map to the organization's control
  framework.
- **Implementation.** AICM mapping to ISO 27001, ISO 42001, NIST AI
  RMF, BSI AIC4.
- **Evidence.** Control register with mapping references.
- **Residual risk.** Mapping staleness as frameworks evolve.
- **Anchor.** `csa2025aicm`, `iso420012023`.

### G26 — Regulatory classification

- **Objective.** Deployments are classified under applicable
  regulatory regimes.
- **Implementation.** EU AI Act tier classification; sector-specific
  classification for healthcare, finance, etc.
- **Evidence.** Conformance pack.
- **Residual risk.** Re-classification trigger on functional
  changes.
- **Anchor.** `euaiact2024`.

---

## Vendor and supply chain

### G27 — Model and tool provenance

- **Objective.** Models and tools are pinned and provenance-checked.
- **Implementation.** SBOM for AI components; signing of pinned
  artifacts.
- **Evidence.** SBOM with signatures.
- **Residual risk.** Trojan plugin `dong2025philosophersstone`.
- **Anchor.** `nist2024ssdfgenai`.

---

## Incident response

### G28 — IR runbook for agent incident

- **Objective.** Pre-defined runbooks exist for prompt-injection,
  retrieval-poisoning, tool-misuse, memory-poisoning, and multi-
  tenant-leak incidents.
- **Implementation.** Runbook library with contact tree and
  rollback procedures.
- **Evidence.** IR records per drill and per incident.
- **Residual risk.** Novel attack class not yet runbooked.
- **Anchor.** OWASP Agentic Top 10 `owasp2025agentictop10`.

---

## User-facing transparency

### G29 — Disclosure to end users

- **Objective.** Users are informed when they are interacting with
  an agentic system.
- **Implementation.** UI badge, in-product disclosure, documentation.
- **Evidence.** UX evidence (screenshots, copy decks).
- **Residual risk.** Disclosure clarity at low salience.
- **Anchor.** EU AI Act Article 50 `euaiact2024`.

---

## Reproducibility

### G30 — Pinned dependencies

- **Objective.** All deployment dependencies are pinned.
- **Implementation.** Lockfiles, immutable container images.
- **Evidence.** Image digests in deployment manifest.
- **Residual risk.** Live-call non-determinism for hosted models.
- **Anchor.** `llmopsreview2025`.

### G31 — Evaluation reproducibility

- **Objective.** Eval results are reproducible from a frozen eval
  set with explicit seeds.
- **Implementation.** Frozen eval set; recorded seeds; eval-set
  hash in deployment manifest.
- **Evidence.** Eval-set hash + seeds.
- **Residual risk.** Test contamination from hosted-model training
  exposure.
- **Anchor.** `tamber2025faithevolving`.

---

## Continuous improvement

### G32 — Post-incident review and AI-use disclosure

- **Objective.** Incidents and AI-use authorship are documented.
- **Implementation.** Blameless post-incident review for incidents;
  per-paper / per-system AI-use disclosure for authorship.
- **Evidence.** PIR document; AI-use disclosure statement.
- **Residual risk.** PIR fatigue; disclosure-statement boilerplate
  fatigue.
- **Anchor.** `nist2024genaiprofile`; IEEE Access AI-use disclosure
  guidance.

---

## Notes on synthesis status

This checklist is **synthesized**, not empirically validated as a
release-gating instrument. The individual controls draw on cited
normative sources (NIST, ISO, OWASP, CSA, EU AI Act) and on
empirical literature (cited per control). The composition into 32
controls along the development-and-operations governance loop and
the autonomy-tier gating is the article's contribution. We
recommend the checklist as a coordination map and invite empirical
validation against a controlled deployment baseline.
