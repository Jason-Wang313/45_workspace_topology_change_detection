# Novelty Decision

Decision after v2 hardening: workshop-only.

Chosen thesis: cached robot plan validity should be tested against topology dependencies of the plan, not only against raw map deltas.

Reasoning:
- Map change detection and replanning are crowded areas.
- The narrower interface, plan-conditioned invalidation, remains a useful mechanism.
- The evidence is synthetic and dependency sets are hand-defined.
- V2 dependency-noise stress shows calibrated extraction is required.

Minimal surviving claim: topology-aware cache invalidation is promising when plan dependencies are available and reasonably reliable.
