# Novelty Boundary Map

## Already crowded

- Dynamic SLAM and map maintenance.
- Occupancy-grid change detection.
- Topological navigation.
- Incremental replanning.
- Visual place recognition in changing environments.

## Remaining boundary

Plan-cache invalidation as a separate target variable: detect whether a workspace change touches the graph relations that a cached plan relies on.

## V2 boundary update

The mechanism depends on calibrated dependency sets. Missing dependencies produce unsafe false negatives, while spurious dependencies produce unnecessary invalidations. Future work must expose, learn, or audit these dependencies from actual planners and maps.
