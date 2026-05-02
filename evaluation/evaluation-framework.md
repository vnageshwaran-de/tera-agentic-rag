# Agentic-RAG Evaluation Framework

This is the narrative companion to `benchmarks-and-metrics.csv` and to Section 6 and Figure 5 of the IEEE Access manuscript. The framework specializes generic LLM-agent evaluation (Mohammadi et al. 2025 KDD) and RAG-only evaluation (Yu et al. 2024 RAG eval survey) to the *agentic-RAG* setting where retrieval, planning, tool use, and action interact.

## Evaluation objectives

Agentic-RAG evaluation needs to answer six questions simultaneously:

1. **Is the retrieval relevant?** — Recall@k, NDCG, MRR; retrieval quality `salemi2024evalretrieval`.
2. **Is the answer faithful to the retrieved context?** — RAGAS `esragas2024`, ARES `saadfalcon2024ares`, RefChecker `hu2024refchecker`, SYNCHECK `wu2024synccheck`, FaithJudge `tamber2025faithevolving`.
3. **Is the answer factually correct against the world?** — Factuality / hallucination metrics: TruthfulQA `lin2022truthfulqa`, HaluEval `li2023halueval`, FActScore `min2023factscore`.
4. **Did the agent plan and act correctly?** — Agent capability benchmarks: AgentBench `liu2024agentbench`, GAIA `mialon2023gaia`, SWE-bench `jimenez2024swebench`, ToolBench `qin2023toolllm`, BFCL `patil2025bfcl`, AgentBoard `ma2024agentboard`, TaskBench `shen2024taskbench`, OSWorld `xie2024osworld`, WebArena `zhou2024webarena`.
5. **Is the system safe and robust under adversarial pressure?** — HarmBench `mazeika2024harmbench`, AILuminate `ailuminate2025`, SG-Bench `mou2024sgbench`, Agent Security Bench `zhang2025agentsecuritybench`, AgentDojo `debenedetti2024agentdojo`, InjecAgent `zhan2024injecagent`.
6. **Does the system meet operational SLOs (latency, cost, reliability)?** — Token cost, p95 / p99 latency, error rate, escalation rate.

## Prescription by autonomy level

The metrics applied to a deployment scale with its autonomy level (Dimension 5 of the taxonomy):

- **Advisory.** Faithfulness + hallucination + retrieval-quality.
- **Assisted.** + tool-use correctness + cost.
- **Supervised action.** + agent-capability + safety + adversarial robustness.
- **Autonomous action.** + multi-agent + long-horizon + embodied where applicable.

`benchmarks-and-metrics.csv` encodes this prescription in the four rightmost columns (Y/N per autonomy level).

## Evaluation lifecycle

Evaluation runs in four phases:

1. **Pre-deployment.** Model and retriever selection; ablation on the eval matrix.
2. **CI/CD gate.** Per-build evaluation against frozen test sets; deploy is gated on pass.
3. **Online evaluation.** Sampled production traffic with reference-free metrics (RAGAS, SYNCHECK).
4. **Drift detection.** Distribution monitors over retrieval quality, faithfulness, and outcome metrics.

## Critical empirical anchor

Wallat et al. 2025 (ICTIR `wallat2025correctnessfaithfulness`) reports that up to **57% of citations in current RAG attribution evaluations lack faithfulness even when correctness is high**. This finding is the most compact justification for treating faithfulness — not just correctness — as a deployment gate.

## Adversarial evaluation as a deployment requirement

A pass on functional benchmarks is necessary but not sufficient. The deployment must also pass:

- Prompt-injection robustness (DataSentinel `datasentinel2025sp` / PromptShield `jacob2025promptshield` benchmarks; Open Prompt Injection `liu2024promptinjectionbench`).
- Agent-attack robustness (Agent Security Bench `zhang2025agentsecuritybench` 27 combos; AgentDojo `debenedetti2024agentdojo`).
- Memory-poisoning robustness (`chen2024agentpoison`, `memorygraft2025`).
- Tool-selection robustness (`shi2026toolhijacker`).

Failure on any of these classes — *even if functional benchmarks pass* — is a release blocker.

## Reproducibility

- Eval-set hashes pinned per release.
- Frozen seeds where applicable.
- Eval-tool versions pinned.
- Eval reports archived in the audit log store.
