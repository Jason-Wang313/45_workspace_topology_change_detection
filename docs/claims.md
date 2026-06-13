# Claims

## Main claim

Cached robot plans should be invalidated by plan-conditioned topology dependencies rather than raw map-delta magnitude.

## V2 narrowed claim

The clean synthetic result depends on calibrated dependency extraction. The topology-dependency trigger reaches 1.000 F1 when dependencies are exact, but 20% missed dependencies reduce F1 to 0.862 and combined 10% missed plus 10% spurious dependencies reduce F1 to 0.873.

## What not to overclaim

- No deployed SLAM or planning system.
- No real robot sensing noise.
- No learned dependency extraction.
- No proof that dependency sets can be extracted reliably from arbitrary planners.
