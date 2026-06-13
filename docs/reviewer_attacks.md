# Reviewer Attacks

- This is just replanning.
- This is just occupancy-grid change detection.
- The dependency set is hand-defined.
- The topology benchmark is synthetic and graph-only.
- Real SLAM changes include loop closure and semantic noise.
- Dependency misses will create unsafe false negatives.
- Spurious dependencies will cause unnecessary replanning.

## V2 outcome

The dependency-calibration attacks are real. With 20% dependency misses, F1 falls to 0.862. With 10% misses plus 10% spurious dependencies, F1 falls to 0.873. The paper should be framed as a workshop mechanism note whose core open problem is extracting calibrated plan dependencies.
