# Novelty Boundary Map

## Already crowded

- Dynamic SLAM and map maintenance.
- Occupancy-grid change detection.
- Topological navigation.
- Incremental replanning.
- Visual place recognition in changing environments.
- Generic graph change-point detection.

## Remaining boundary

Plan-cache invalidation as a separate target variable: detect whether a workspace change touches the graph, semantic, resource, or manipulation relations that a cached plan relies on.

## Final v3 boundary

The paper does not claim a new map updater, topological planner, or hardware robot system. It claims that cached-plan validity should be evaluated against plan-conditioned topology dependencies. The full-scale benchmark supports this claim with approximate dependency extractors, strong baselines, stress tests, negative controls, and explicit failure modes.
