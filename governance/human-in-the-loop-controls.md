# Human-in-the-Loop Controls for Enterprise Agentic RAG

This document is the deployable companion to G15 and G16 of the governance checklist. It draws on the systematic review of HITL in AI by Mou et al. and others published in Entropy 2026 [`hitl2025entropy`], extending the in/on/out-of-the-loop framing to the four autonomy levels of the TERA taxonomy.

## In-the-loop / on-the-loop / out-of-the-loop

| Stance | Meaning | Use when |
|---|---|---|
| In-the-loop | Human approves every action before it occurs | Safety-critical or first-of-its-kind action; high regulatory tier |
| On-the-loop | Human samples and reviews automated actions | Business-critical; mature deployments |
| Out-of-the-loop | Human reviews only ex-post via audit | Low-stakes; high-volume routine actions |

Per `hitl2025entropy`, mature HITL systems target a 10–15% escalation rate with confidence thresholds in the 80–90% range. We adopt these as default design heuristics.

## Risk-tier policy

The risk-class taxonomy (Dimension 7) maps to HITL stance:

| Risk tier | Default stance | Override conditions |
|---|---|---|
| Low-stakes | Out-of-the-loop | None |
| Business-critical | On-the-loop | First-of-its-kind action returns to in-the-loop |
| Regulated | On-the-loop with mandatory full audit | Sectoral regulation may require in-the-loop |
| Safety-critical | In-the-loop | None |

## Approval workflow

1. **Trigger.** Action confidence < threshold OR action class is in the policy's escalation list OR risk score above threshold.
2. **Routing.** Approval routed to the queue corresponding to the action class and the agent's role.
3. **Approval evidence.** Cryptographic sign-off; timestamped; tied to the agent's session and action ID.
4. **Outcome capture.** Approval log linked to the action's eventual outcome for retrospective calibration.

## Calibration loop

- Periodic review of escalation rate vs. SLO.
- Adjust threshold to maintain the 10–15% target band, balanced against approval-fatigue indicators.
- Review false-approval rate on adversarial samples; tune up if attackers slip approvals.

## Anti-patterns

- Approval queues larger than human capacity, leading to silent auto-approval after timeout.
- Single approver bottleneck.
- Approval based solely on the agent's self-confidence without external evidence.
- HITL gates downstream of irreversible action (e.g., approval after payment posted).
