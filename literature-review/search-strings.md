# Search strings used in the systematic literature review

Strings are organized by research question, grouped into five families. Each family is executed across all database tiers per `search-protocol.md` §3. Operators are normalized per source.

## Family 1 — RQ1, RQ2 (architecture, retrieval, agent integration)

```
"agentic RAG"
"agentic retrieval-augmented generation"
"retrieval augmented generation" AND ("LLM agent" OR "tool-using agent")
"multi-agent" AND ("retrieval-augmented" OR "RAG")
"GraphRAG" OR "graph retrieval augmented"
"corrective RAG" OR "self-reflective RAG" OR "self-RAG"
"tool augmented" AND ("LLM" OR "language model")
```

## Family 2 — RQ3 (evaluation)

```
"RAG evaluation" OR "RAG benchmark"
"LLM agent" AND ("benchmark" OR "evaluation")
"faithfulness" AND ("retrieval-augmented" OR "RAG")
"hallucination" AND ("RAG" OR "retrieval-augmented")
"tool use" AND "evaluation" AND "language model"
"agent benchmark" AND ("planning" OR "long-horizon")
```

## Family 3 — RQ4 (security and failure modes)

```
"prompt injection" AND ("LLM" OR "language model")
"indirect prompt injection"
"retrieval poisoning" OR "PoisonedRAG"
"data poisoning" AND ("RAG" OR "embedding")
"vector database" AND ("security" OR "attack")
"excessive agency" AND ("LLM" OR "agent")
"jailbreak" AND ("LLM" OR "agent")
"system prompt leakage"
"memory poisoning" AND ("agent" OR "LLM")
"tool misuse" AND "language model"
```

## Family 4 — RQ5 (cloud, ops, governance)

```
"LLMOps" OR "GenAIOps"
"MLOps" AND ("large language model" OR "RAG")
"cloud" AND "deployment" AND ("LLM agent" OR "RAG")
"observability" AND ("LLM" OR "agent")
"human-in-the-loop" AND ("LLM" OR "agent")
"agentic AI governance" OR "agent governance"
"trustworthy" AND ("LLM agent" OR "agentic AI")
"AI risk management" AND ("generative" OR "agent")
```

## Family 5 — RQ6, RQ7 (open problems, frameworks, competitor surveys)

```
"open challenges" AND ("RAG" OR "LLM agent")
"survey" AND ("RAG" OR "agentic")
"framework" AND ("trustworthy" OR "responsible") AND ("LLM" OR "agent")
```

## Execution notes

- Boolean operators are normalized per database. Where a database does not support full Boolean logic (e.g., Google Scholar), strings are split into sub-queries and result sets are unioned.
- For arXiv, the export API is used with submission-date filters and primary-category filters (cs.CL, cs.AI, cs.IR, cs.CR, cs.LG, cs.SE).
- For Semantic Scholar, the influential-citation-count and citation-velocity signals are used to rank candidates.
- For peer-reviewed venues that publish proceedings (ACL Anthology, USENIX, OpenReview), the proceedings index is searched directly.

## Search dates

- Initial search window: 2026-05-01.
- Planned final refresh: 30 days before paper submission.
- Inclusion of pre-2021 foundational work is by anchor-citation only and is not driven by these searches.
