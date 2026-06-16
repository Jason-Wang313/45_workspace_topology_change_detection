# Novelty Decision

Decision after v3 hardening: submission-ready candidate.

Chosen thesis: cached robot plan validity should be tested against topology dependencies of the plan, not only against raw map deltas, path overlap, or generic graph-change magnitude.

Reasoning:
- Dynamic SLAM, occupancy-map change detection, topological navigation, and incremental replanning are crowded.
- Plan-cache invalidation is a narrower interface target that those areas do not directly optimize.
- The final benchmark evaluates approximate dependency extractors rather than relying on perfect dependencies.
- The strongest baselines remain substantially below the proposed plan-topology dependency policy.

Minimal supported claim: topology-aware cache invalidation is a strong interface principle when plan dependencies can be exposed or approximated, and it is empirically superior to map-delta controls in the full-scale synthetic benchmark.
