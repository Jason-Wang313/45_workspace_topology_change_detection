# Final Audit

1. Chosen thesis: cached robot plans should be invalidated by workspace topology dependencies, not raw map-delta magnitude.
2. Field assumption broken: local occupancy changes are enough to decide whether a cached plan remains valid.
3. New central mechanism: plan-conditioned dependency sets over corridor, cut, adjacency, and cached-path structure.
4. Literature coverage: 1200-row matrix with 300 serious skim, 220 deep read, and 100 hostile prior entries.
5. Evidence: synthetic topology benchmark with 280 perturbations.
6. Local delta accuracy/F1: 0.286/0.000.
7. Topology dependency accuracy/F1: 1.000/1.000.
8. Biggest weaknesses: synthetic graph evidence, hand-defined dependencies, no hardware or noisy SLAM integration.
9. Paper-readiness judgment: recovered workshop-style mechanism draft.
10. Exact Downloads PDF path: C:/Users/wangz/Downloads/45.pdf
11. GitHub URL: https://github.com/Jason-Wang313/45_workspace_topology_change_detection
12. Desktop PDF copy: C:/Users/wangz/OneDrive/Desktop/45.pdf
