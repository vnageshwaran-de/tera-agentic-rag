# Pre-Deployment Evaluation Checklist for Enterprise Agentic RAG

A practitioner-oriented checklist for the release manager. Each item ties to a TERA cell and a row in `benchmarks-and-metrics.csv` or `governance/governance-checklist.md`. Pass/fail per item is the release gate.

## Retrieval

- [ ] Recall@k and NDCG meet documented SLO on frozen eval set (BEIR / MTEB / domain set).
- [ ] Hybrid retrieval ablation completed; reranker gain quantified.
- [ ] Retrieval-quality metric (Salemi & Zamani 2024) measured against held-out query set.
- [ ] Retrieval drift baseline captured.

## Faithfulness and groundedness

- [ ] RAGAS faithfulness ≥ documented SLO.
- [ ] ARES or RefChecker run on a representative slice; results retained.
- [ ] SYNCHECK integrated for online monitoring.
- [ ] Citation-faithfulness manually audited on a sample (the 57%-failure finding from Wallat et al. 2025 is the rationale).

## Hallucination

- [ ] TruthfulQA / HaluEval / FActScore baseline retained.
- [ ] Domain-specific hallucination probe (where applicable) executed.

## Agent capability

- [ ] AgentBench-style multi-environment task success.
- [ ] Tool-use correctness (BFCL or comparable).
- [ ] Plan-quality measured (AgentBoard or comparable).
- [ ] Long-horizon stability tested (OSWorld / WebArena slice or domain analog).

## Safety and adversarial robustness

- [ ] HarmBench refusal rate within documented bounds.
- [ ] Open Prompt Injection benchmark suite executed (`liu2024promptinjectionbench`).
- [ ] Agent Security Bench 27 attack/defense suite executed.
- [ ] Memory-poisoning probe (`chen2024agentpoison`, `memorygraft2025`).
- [ ] Tool-selection adversarial probe (`shi2026toolhijacker`).
- [ ] Multi-source ordering probe (`wang2026obliinjection`).
- [ ] Multi-turn jailbreak suite (Crescendo, TwinBreak).

## Operational

- [ ] Token cost per task within budget.
- [ ] p95 / p99 latency within budget.
- [ ] Error rate within budget.
- [ ] Drift detection live and alerting.
- [ ] Rollback runbook tested.
- [ ] Observability traces complete end-to-end (request → retrieval → plan → tool → response).

## Governance and HITL

- [ ] HITL gates per risk tier configured.
- [ ] Approval evidence stored in audit log.
- [ ] Per-agent IAM scope reviewed.
- [ ] Tool ACL reviewed.
- [ ] Memory ACL reviewed.

## Pass / fail

A release is admitted only if every box is checked. Failures are tracked as risk acceptances or release blockers per the governance process.
