# Pre-deployment Evaluation Checklist for Agentic RAG

This checklist operationalizes the evaluation lifecycle of Section 6.10 of
*Trustworthy Agentic RAG for Enterprise AI* (Nageshwaran, IEEE Access 2026).
Use it as a release-gating instrument before promoting a deployment to a
new autonomy or risk tier. Each item references the corresponding
benchmark in `evaluation/benchmarks-and-metrics.csv` and the corresponding
governance control in `governance/governance-checklist.md`.

The checklist is **compositional**: a deployment at coordinate
(autonomy = X, risk = Y) inherits the union of metric requirements of all
lower autonomy levels and is gated on the corresponding governance
evidence. Skipping a lower-tier gate at a higher tier is not permitted.

---

## Phase 1 — Pre-deployment evaluation

### Retrieval-quality gates (all autonomy levels)

- [ ] **R1.** Recall@k and NDCG measured on a held-out evaluation set at
      every retriever or embedding change. Anchor: BEIR
      (`thakur2021beir`), MTEB (`muennighoff2023mteb`).
- [ ] **R2.** Joint retrieval-quality metric (e.g.
      Eval-Retrieval-Quality, `salemi2024evalretrieval`) measured on a
      RAG-aware fixture set. Failures gate promotion regardless of
      isolated retriever scores.

### Faithfulness and grounding gates (all autonomy levels)

- [ ] **F1.** Reference-free faithfulness against an enterprise fixture
      set: RAGAS (`esragas2024`), ARES (`saadfalcon2024ares`), or
      RefChecker (`hu2024refchecker`). Faithfulness service-level
      objective is named explicitly in the deployment's eval contract.
- [ ] **F2.** Hallucination-corpus regression at every model or
      retriever change: RAGTruth (`niu2024ragtruth`),
      TruthfulQA (`lin2022truthfulqa`), HaluEval (`li2023halueval`).
- [ ] **F3.** Citation faithfulness explicitly verified against the
      Wallat et al. attribution test (`wallat2025correctnessfaithfulness`)
      because correctness alone is documented to fail at up to 57% on
      this dimension.

### Tool-use gates (assisted and above)

- [ ] **T1.** Tool-call correctness and parameter F1 at every change to
      the tool registry. Anchor: BFCL (`patil2025bfcl`),
      ToolBench (`qin2023toolllm`).
- [ ] **T2.** Side-effect correctness on a non-production sandbox
      environment with read-only tools. Production write access is
      gated on T1 + T2 passing.

### Agent-capability gates (supervised action and above)

- [ ] **A1.** Multi-turn task completion: AgentBench
      (`liu2024agentbench`), AgentBoard (`ma2024agentboard`),
      TaskBench (`shen2024taskbench`).
- [ ] **A2.** Domain-specific capability: FinBen (`xie2024finben`),
      SearchExpertBench-25 (`li2026searchexpert`), or domain analog.
- [ ] **A3.** For code agents: RedCode risky-execution evaluation
      (`guo2024redcode`).

### Adversarial / safety gates (supervised action and above)

- [ ] **S1.** Red-team baseline: HarmBench (`mazeika2024harmbench`)
      and AILuminate (`ailuminate2025`).
- [ ] **S2.** Agent-specific adversarial: Agent Security Bench's 27
      attack-defense combinations (`zhang2025agentsecuritybench`),
      AgentDojo (`debenedetti2024agentdojo`), InjecAgent
      (`zhan2024injecagent`), Open Prompt Injection
      (`liu2024promptinjectionbench`).
- [ ] **S3.** Memory-poisoning probes: AgentPoison
      (`chen2024agentpoison`), MemoryGraft (`memorygraft2025`).
- [ ] **S4.** Tool-selection adversarial probes: ToolHijacker
      (`shi2026toolhijacker`), ObliInjection (`wang2026obliinjection`).
      Mandatory for autonomous-action deployments.

### Cost and operational gates (advisory and above)

- [ ] **C1.** Token cost per task measured against budget.
- [ ] **C2.** p95 and p99 latency measured against SLO.
- [ ] **C3.** Fine-tune-versus-RAG cost trade-off documented for
      knowledge surfaces where it applies (`soudani2024finetunevsrag`).

---

## Phase 2 — CI/CD-gated promotion

- [ ] **CI1.** All Phase 1 gates run in CI on every model, prompt,
      retriever, or tool-registry change.
- [ ] **CI2.** Promotion blocked on regression in any prescribed
      metric. Override requires risk acceptance signed by the
      governance owner of record.
- [ ] **CI3.** Eval contract is versioned alongside the deployment;
      eval-set hash recorded in the deployment manifest
      (governance G30).

---

## Phase 3 — Online evaluation

- [ ] **O1.** Reference-free faithfulness sampled on production
      traffic: RAGAS (`esragas2024`), SYNCHECK (`wu2024synccheck`).
- [ ] **O2.** Sample rate calibrated to budget; alert thresholds
      tuned against false-positive cost.
- [ ] **O3.** OpenTelemetry GenAI semantic conventions
      (`otel2024genai`) followed for trace export.

---

## Phase 4 — Drift detection

- [ ] **D1.** Embedding-distribution drift monitored against the
      retrieval-store baseline.
- [ ] **D2.** Retrieval-quality drift monitored against fixture
      baseline.
- [ ] **D3.** Faithfulness-score drift monitored against the
      faithfulness SLO.
- [ ] **D4.** Outcome drift (task-completion rate, escalation rate,
      tool-call success rate) monitored against operational
      baselines.
- [ ] **D5.** Slow-drift recalibration scheduled at minimum a
      monthly cadence; recalibration informs the next eval contract.

---

## Phase 5 — Re-evaluation triggers

A new round of Phase 1 evaluation is required when any of the
following occurs:

- Model version change (major or minor)
- Retriever or embedding-model change
- Tool registry change (addition, removal, schema change)
- New corpus ingestion above 10% of indexed volume
- New regulatory class (EU AI Act tier escalation, sector-specific
  compliance addition)
- Drift alert breaching D1-D4 thresholds for more than the recovery
  window
- Red-team disclosure of a new attack class

---

## Notes

This checklist is **proposed**, not empirically validated as a
release-gating instrument. The individual metrics it composes are
validated in the cited literature; the composition (autonomy-tier
gating, evaluation-lifecycle phasing) is the article's synthesis. We
recommend the checklist as a coordination map and invite empirical
validation against a controlled deployment baseline.
