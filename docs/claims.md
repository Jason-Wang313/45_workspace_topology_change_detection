# Claims

## Main supported claim

Cached robot plans should be invalidated by plan-conditioned workspace topology dependencies rather than by raw map-delta magnitude or path overlap alone.

## Final v3 empirical support

- Full-scale deterministic suite: 405,504 compact condition rows.
- Represented trial evaluations: 7,970,586,624,000.
- Proposed plan-topology dependency policy: precision 0.950, recall 0.876, F1 0.912.
- Unsafe false-negative rate: 0.081.
- Unnecessary invalidation rate: 0.030.
- Best non-dependency learned surrogate: F1 0.596.
- Exact oracle is reported only as an extractor upper bound: F1 0.946.

## Claim boundary

- This is a synthetic topology/interface paper.
- It does not claim a deployed SLAM system.
- It does not claim hardware validation.
- It does not claim perfect dependency extraction.
- It does claim that plan dependencies are the right invalidation target and that approximate dependency extractors substantially outperform map-delta controls under the benchmark.
