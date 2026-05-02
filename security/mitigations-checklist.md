# Security Mitigations Checklist for Enterprise Agentic RAG

A defensive-control checklist that maps mitigations from `threat-model.csv` to deployable patterns. Use alongside `governance/governance-checklist.md`.

## Input boundary (TERA L1, L3 × C1)

- [ ] Source allow-list at ingestion; per-source content-scan and hash.
- [ ] PII scanner with redaction or rejection per data classification.
- [ ] Input validators on user prompts (StruQ structured queries `chen2025struq`).
- [ ] Prompt-injection detector at the LLM gateway (DataSentinel `datasentinel2025sp`, PromptShield `jacob2025promptshield`, PromptLocate `promptlocate2026sp`).
- [ ] Multi-source ordering verifier where retrieval merges sources (`wang2026obliinjection`).

## Retrieval boundary (TERA L2 × C1)

- [ ] Retrieval rate-limit per user / per agent.
- [ ] Anomaly detection on retrieval distribution (jamming `shafran2025jamming`).
- [ ] Provenance-aware retrieval: untrusted sources require a stronger generator-side verifier.
- [ ] Backdoored-retriever audit at promotion (`backdooredretrievers2024`).

## Reasoning boundary (TERA L3 × C1)

- [ ] Plan-trace audit; high-risk plans require HITL.
- [ ] Multi-turn safety calibration (Crescendo `russinovich2025crescendo`, TwinBreak `krauss2025twinbreak`).
- [ ] Refusal calibration tested with HarmBench `mazeika2024harmbench` and AILuminate `ailuminate2025`.

## Tool / action boundary (TERA L4 × C1)

- [ ] Per-agent IAM with minimum tool ACL.
- [ ] Tool registry with hash-pinned tool definitions (mitigates ToolHijacker `shi2026toolhijacker` and Philosopher's Stone `dong2025philosophersstone`).
- [ ] Tool input/output schema validation.
- [ ] Side-effect logging for every tool call.
- [ ] Mandatory HITL gate on irreversible or high-risk actions.

## Memory boundary (TERA L3 × C1)

- [ ] Memory write authorization with per-write authentication.
- [ ] Memory provenance tags (mitigates AgentPoison `chen2024agentpoison` and MemoryGraft `memorygraft2025`).
- [ ] Periodic memory diff against canonical baseline.
- [ ] Memory rollback capability.

## Multi-agent boundary (TERA L5 × C1)

- [ ] Inter-agent message audit log.
- [ ] Role-policy enforcement; roles hashed and signed.
- [ ] Linguistic anomaly monitoring for steganographic collusion (`motwani2024secretcollusion`).

## Cloud boundary (TERA L0 × C1)

- [ ] Per-tenant cache namespace at LLM gateway, retrieval cache, and KV cache (mitigates PROMPTPEEK `wu2025promptpeek`).
- [ ] Encrypted-at-rest embeddings where data classification requires (mitigates embedding inversion `embeddinginversion2024arxiv`, `transferableinversion2024`).
- [ ] Plugin / model SBOM with signing (mitigates Philosopher's Stone `dong2025philosophersstone`).
- [ ] Network egress allow-list; default deny.

## Application boundary (TERA L5 × C1)

- [ ] User-facing safety classifier on outbound responses (Llama Guard `inan2023llamaguard` or comparable).
- [ ] Output validators for sensitive-information disclosure (mitigates PLeak `hui2024pleak`).
- [ ] Monitoring for keylogging-style side channels (`weiss2024remotekeylogging`).

## Continuous

- [ ] Quarterly red-team review using the latest Agent Security Bench attack catalogue.
- [ ] Monthly review of OWASP Top 10 (LLM and Agentic) and update of corresponding control rows.
