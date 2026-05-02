# Phase 3 — Systematic Literature Review Protocol

This protocol governs the literature review for the manuscript "Trustworthy Agentic RAG for Enterprise AI: A Systematic Survey and Framework for Architectures, Evaluation, Security, Governance, and Cloud-Native Deployment" (IEEE Access). It is written so that another reviewer could reproduce the search, screening, and extraction steps and arrive at a comparable corpus.

---

## 1. Review objective

To identify, classify, evaluate, and synthesize the body of work on agentic Retrieval-Augmented Generation (RAG) systems with sufficient breadth across architecture, retrieval, agent reasoning, tool use, security, evaluation, governance, and cloud-native operations to support (a) a defensible gap statement, (b) a reusable taxonomy and threat-and-control matrix, and (c) the TERA framework's claim of integrative novelty.

The review is intentionally cross-disciplinary. It covers AI/ML research, information retrieval, software engineering, cloud and security engineering, and AI governance.

---

## 2. Research questions

| ID | Research question |
|---|---|
| RQ1 | What architectural patterns are used in enterprise agentic RAG systems? |
| RQ2 | How do agentic RAG systems integrate retrieval, memory, planning, tool use, and action execution? |
| RQ3 | What benchmarks and metrics are used to evaluate agentic RAG systems, and what aspects of agentic capability remain unmeasured? |
| RQ4 | What are the dominant failure modes and security threats specific to agentic RAG, and what mitigations have been proposed and evaluated? |
| RQ5 | What cloud-native deployment, observability, and governance patterns are emerging for agentic RAG in enterprise settings? |
| RQ6 | What open problems must be addressed for trustworthy enterprise adoption? |
| RQ7 | How can architecture, evaluation, security, governance, and operations be unified into a practical enterprise framework (the TERA framework)? |

RQ1–RQ6 are descriptive/synthetic. RQ7 is constructive: it justifies the framework as the survey's primary scholarly contribution.

---

## 3. Databases and information sources

Tier-1 (peer-reviewed primary sources):
- IEEE Xplore
- ACM Digital Library
- ACL Anthology
- SpringerLink
- ScienceDirect / Elsevier
- USENIX (open archives)
- NeurIPS, ICML, ICLR, AAAI, IJCAI, KDD, WWW, SIGIR, EMNLP, NAACL, COLING, ACL — proceedings via openreview.net, arXiv author copies, and association sites

Tier-2 (indexing and discovery):
- Semantic Scholar
- Google Scholar
- DBLP
- Scopus and Web of Science (citation analytics) — used opportunistically; not required

Tier-3 (preprints):
- arXiv (cs.CL, cs.AI, cs.IR, cs.CR, cs.LG, cs.SE)

Tier-4 (standards and authoritative governance sources):
- NIST (AI 600-1, AI RMF, SP 800 series)
- OWASP (LLM Applications Top 10 2025; Agentic Applications Top 10, Dec 2025)
- ISO/IEC (42001 AI management systems, 23894 AI risk, 5338 AI engineering lifecycle, 38507) — abstract level unless full text is procured
- Cloud Security Alliance (Agentic AI working groups)

Tier-5 (industry context, not primary evidence):
- Cloud provider documentation (AWS, Azure, GCP) — for normative primitives only (IAM, KMS, audit logs)
- Vendor whitepapers — used only as context where no peer-reviewed equivalent exists, and explicitly labeled

---

## 4. Search dates

- Search window: **2021-01-01 through 2026-05-31**.
- Foundational works prior to 2021 included only when they are anchor citations (e.g., Lewis et al. 2020 on RAG; Yao et al. 2022 on ReAct; foundational prompt-injection work).
- Final search refresh planned **30 days before submission** to capture late-2026 publications.

---

## 5. Search strings

The following strings are executed against each Tier-1, Tier-2, and Tier-3 source. Where a source supports field-restricted search, the string is applied to title, abstract, and keywords. Strings are grouped by RQ.

### 5.1 RQ1, RQ2 — architecture, retrieval, agent integration
- `"agentic RAG"`
- `"agentic retrieval-augmented generation"`
- `"retrieval augmented generation" AND ("LLM agent" OR "tool-using agent")`
- `"multi-agent" AND ("retrieval-augmented" OR "RAG")`
- `"GraphRAG" OR "graph retrieval augmented"`
- `"corrective RAG" OR "self-reflective RAG" OR "self-RAG"`
- `"tool augmented" AND ("LLM" OR "language model")`

### 5.2 RQ3 — evaluation
- `"RAG evaluation" OR "RAG benchmark"`
- `"LLM agent" AND ("benchmark" OR "evaluation")`
- `"faithfulness" AND ("retrieval-augmented" OR "RAG")`
- `"hallucination" AND ("RAG" OR "retrieval-augmented")`
- `"tool use" AND "evaluation" AND "language model"`
- `"agent benchmark" AND ("planning" OR "long-horizon")`

### 5.3 RQ4 — security and failure modes
- `"prompt injection" AND ("LLM" OR "language model")`
- `"indirect prompt injection"`
- `"retrieval poisoning" OR "PoisonedRAG"`
- `"data poisoning" AND ("RAG" OR "embedding")`
- `"vector database" AND ("security" OR "attack")`
- `"excessive agency" AND ("LLM" OR "agent")`
- `"jailbreak" AND ("LLM" OR "agent")`
- `"system prompt leakage"`
- `"memory poisoning" AND ("agent" OR "LLM")`
- `"tool misuse" AND "language model"`

### 5.4 RQ5 — cloud, ops, governance
- `"LLMOps" OR "GenAIOps"`
- `"MLOps" AND ("large language model" OR "RAG")`
- `"cloud" AND "deployment" AND ("LLM agent" OR "RAG")`
- `"observability" AND ("LLM" OR "agent")`
- `"human-in-the-loop" AND ("LLM" OR "agent")`
- `"agentic AI governance" OR "agent governance"`
- `"trustworthy" AND ("LLM agent" OR "agentic AI")`
- `"AI risk management" AND ("generative" OR "agent")`

### 5.5 RQ6, RQ7 — open problems and frameworks
- `"open challenges" AND ("RAG" OR "LLM agent")`
- `"survey" AND ("RAG" OR "agentic")` — for competitor identification
- `"framework" AND ("trustworthy" OR "responsible") AND ("LLM" OR "agent")`

### 5.6 Search-string execution notes
- Boolean operators are normalized per source. Where a source does not support full Boolean logic (e.g., Google Scholar's degraded operator support), strings are split into sub-queries and results are unioned.
- For arXiv, we use the export API filtered by submission date and primary category.
- For Semantic Scholar, we additionally use the "influential citation count" and "citation velocity" signals to rank candidates.

---

## 6. Inclusion criteria

A source is included if **all** of the following hold:
1. Publication date within 2021-01-01 through 2026-05-31 (or pre-2021 and identified as a foundational anchor).
2. Substantive technical content directly relevant to one or more of: RAG, LLM agents, tool use, multi-agent LLM systems, agentic-RAG evaluation, agentic-RAG security or governance, cloud-native deployment of LLM systems, or LLMOps for generative AI.
3. Source type is one of:
   - Peer-reviewed journal article or conference paper.
   - Preprint with credible authorship and substantive technical claims (typically arXiv).
   - Standards document or authoritative governance publication (NIST, OWASP, ISO/IEC, CSA).
   - Industry technical report with verifiable methodology (Microsoft, Google, AWS research, IBM research, Meta AI, Anthropic, etc.).
4. Sufficient methodological detail to support classification, comparison, or synthesis.
5. Published in English.

---

## 7. Exclusion criteria

A source is excluded if **any** of the following hold:
1. Opinion piece without technical substance.
2. Vendor marketing material (used only as Tier-5 context where labeled).
3. Outside scope of the seven RQs.
4. Duplicate of an already-included work (deduplicated per Section 9).
5. Retracted, withdrawn, or under public correction.
6. Predatory venue per Beall's heritage list updates and DOAJ exclusions.
7. Claims cannot be verified from accessible metadata, abstract, or legally available full text.
8. Non-English without an authoritative English translation.

---

## 8. Deduplication

- All exported records are normalized to a common schema (title, authors, year, venue, DOI/arXiv ID, abstract, source DB).
- Deduplication is performed using a two-step rule: (a) exact DOI or arXiv-ID match; (b) for records lacking both, fuzzy match on (title, first author, year) at Levenshtein distance ≤ 3 on the normalized title.
- arXiv preprints superseded by a peer-reviewed publication are *replaced* by the peer-reviewed record; the arXiv ID is retained as a note for accessibility.
- A deduplication script (`scripts/deduplicate_bibtex.py`) operates on the merged BibTeX library and emits a deduplication log.

---

## 9. Screening process

Three-pass screening:

| Pass | Input | Action | Output |
|---|---|---|---|
| 1. Title screen | Deduplicated record list | Title-only relevance check against RQs | Pass-1 candidates |
| 2. Abstract screen | Pass-1 candidates | Read abstract; apply inclusion/exclusion criteria | Pass-2 candidates |
| 3. Full-text screen | Pass-2 candidates | Read available full text or, where gated, the most authoritative accessible version (publisher abstract + author-posted preprint where it exists); apply quality assessment in Section 10 | Final included corpus |

A second-reader pass is recommended on a 10% random sample at Pass 2 to estimate inter-rater agreement (Cohen's κ). Single-author surveys frequently skip this; we record it as a methodological limitation.

Each included record carries a screening-decision row in `literature-review/screening-log.csv`.

---

## 10. Quality assessment

Each included source is scored on a 0–2 ordinal scale across the following dimensions. Scores are recorded in `literature-review/quality-assessment.csv`.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Technical relevance | Tangential | Adjacent | Directly supports an RQ |
| Methodological rigor | No method described | Method described | Method described and justified |
| Empirical validation | None | Limited (one dataset / small N) | Multi-dataset / replicated |
| Reproducibility | No code/data | Partial | Full code/data/config |
| Clarity of evaluation | Metrics undefined | Metrics defined | Metrics defined with baselines |
| Enterprise/cloud relevance | Pure research | Acknowledges enterprise concerns | Engages enterprise/cloud explicitly |
| Security/governance relevance | None | Mentioned | Engages substantively |
| Source authority | Preprint/industry blog | Conference / lower-tier journal | Top-tier venue or anchor standard |

A record below an aggregate score of 6 is *included only* if it is uniquely necessary for an RQ (e.g., it is the only paper covering a specific threat). Such records are flagged in the extraction as low-quality-but-unique.

Source-type-specific handling:
- **Peer-reviewed**: full quality scoring applied; primary evidence.
- **Preprint**: scored normally, but cited with the "preprint" descriptor in the manuscript, and replaced with the peer-reviewed version if and when one appears.
- **Standards / authoritative governance**: scored on relevance and authority only; treated as normative anchors, not empirical evidence.
- **Industry technical report**: scored normally; cited with explicit attribution and never used as the sole support for a quantitative claim.

---

## 11. Data extraction schema

For every included record we extract:

| Field | Notes |
|---|---|
| `id` | Internal key (cite-key for BibTeX) |
| `bibtex_key` | IEEE numbered reference number assigned at Phase 6 |
| `authors`, `year`, `venue`, `doi`, `arxiv_id`, `url` | Bibliographic |
| `source_type` | journal / conference / preprint / standard / report / book |
| `peer_reviewed` | yes / no |
| `rq_coverage` | Subset of {RQ1..RQ7} |
| `topics` | Multi-label tags (e.g., agentic-RAG, prompt-injection, multi-agent, eval, LLMOps) |
| `taxonomy_dimensions` | Which TERA taxonomy dimensions the work addresses |
| `tera_layers` | Which TERA layers L0..L5 the work touches |
| `tera_concerns` | Which TERA cross-cutting bands C1..C5 the work touches |
| `key_claims` | 1–3 sentences, in our words, of what the paper claims |
| `evidence_type` | empirical / formal / case-study / position |
| `datasets_used` | Named datasets and benchmarks |
| `metrics_used` | Named metrics |
| `limitations_noted` | What the authors acknowledge |
| `our_use` | Which manuscript section will cite this and for what claim |
| `quality_score` | Aggregate 0–16 from Section 10 |
| `full_text_reviewed` | yes / abstract-only / metadata-only |
| `notes` | Free-form |

The schema is materialized in `literature-review/extraction.csv` and the BibTeX cite keys are mirrored in `literature-review/selected-papers.bib`.

---

## 12. Coding schema (synthesis)

Synthesis is performed by coding each extracted record against:

- **Architecture pattern** (taxonomy of Section 4 in the manuscript).
- **Threat / failure mode** (matrix of Section 7).
- **Evaluation metric class** (matrix of Section 6).
- **Governance control** (checklist of Section 8).
- **Cloud component** (reference architecture of Section 9).
- **TERA grid cell** (one or more of the 30 cells in the 6 × 5 layer-by-concern grid).

Codes are reconciled into the manuscript's matrices and checklists.

---

## 13. PRISMA-style flow description

Reported in `literature-review/prisma-flow-data.csv` and rendered as Figure 1 of the manuscript:

```
Identification
  Records identified from databases ........... N_db
  Records identified from other sources ....... N_other
                                                ─────
  Total identified ............................ N_id

Deduplication
  Records after duplicates removed ............ N_dedup

Screening
  Records screened by title ................... N_dedup
    Excluded at title ......................... N_x_title
  Records screened by abstract ................ N_pass1
    Excluded at abstract ...................... N_x_abs
  Records assessed full text .................. N_pass2
    Excluded at full text ..................... N_x_full
      (with reasons grouped)

Inclusion
  Final corpus included in synthesis .......... N_final
```

The exact counts are populated during execution and frozen at the search-refresh deadline. The flow figure follows PRISMA 2020 conventions.

---

## 14. Limitations of the review method

1. **Single-author screening** without a second rater introduces a known risk of selection bias. Mitigated by transparent search strings, an open screening log, and a 10% self-recheck sample at Pass 2.
2. **Database access asymmetry**. Some Tier-1 sources require institutional access. Where full text is unavailable, we use the most authoritative accessible version and flag the record's `full_text_reviewed` status.
3. **English-language restriction** excludes potentially relevant non-English work, particularly recent Chinese-language preprints on agent systems.
4. **Fast-moving field**. Agentic RAG accelerated sharply through 2024–2026. The protocol's planned 30-day-pre-submission refresh reduces but does not eliminate the risk of missing late-breaking work.
5. **arXiv reliance**. Many of the most-cited works are arXiv preprints. The protocol mitigates by replacing preprints with peer-reviewed versions wherever they exist and by labeling preprints as such in the manuscript.
6. **Heterogeneous quality scoring**. The 0–2 ordinal scale is interpretable but coarse. We accept this as a deliberate trade-off against ambiguous fine-grained scales.

---

## 15. Threats to validity

Following Wohlin et al.'s scheme adapted to a literature review:

- **Construct validity**: the operational definition of "agentic RAG" is contested. We adopt Singh et al. (2025) as the anchor definition and explicitly note where we extend it (notably toward enterprise/cloud aspects).
- **Internal validity**: search strings may under-capture cross-disciplinary work in security and cloud engineering. Mitigated by RQ-aligned string families (Section 5) and citation-chasing on the closest 6 competitors.
- **External validity**: findings generalize to enterprise English-language settings; we explicitly limit claims to that context.
- **Reliability**: all artifacts (strings, logs, extractions, scripts) are versioned in the companion repository so that a reviewer or future researcher can re-execute the protocol.

---

## 16. Source-type handling at a glance

| Source type | Primary use | Citation style | Caveat |
|---|---|---|---|
| Peer-reviewed journal/conference | Primary evidence for claims | "[N]" with full IEEE record | Default |
| Preprint (arXiv) | Evidence where peer-reviewed equivalent unavailable; or for emerging topics | "[N]" with "preprint" annotation in text | Replace with peer-reviewed version when available |
| Standard (NIST, OWASP, ISO/IEC, CSA) | Normative anchor | "[N]" with publisher/version | Treated as normative, not empirical |
| Industry technical report | Context, real-world signal | "[N]" with explicit attribution | Never sole support for a quantitative claim |
| Vendor blog/whitepaper | Tier-5 context only | Cite sparingly; label as industry context | Avoid as scholarly evidence |

---

## 17. Reporting

The final manuscript reports the protocol in Section 3 (Review Methodology) with the PRISMA flow diagram. Full search strings, screening log, extraction table, and quality scores are released in the companion repository on acceptance.
