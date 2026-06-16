# Reviewer Attacks

## Resolved or mitigated in v3

1. Exact dependencies are an oracle.
   - Mitigation: exact oracle is only an upper bound; approximate extractors are evaluated.

2. Path touch is enough.
   - Mitigation: path touch reaches only 0.436 F1 in the full benchmark.

3. Raw map deltas are enough.
   - Mitigation: raw-delta threshold reaches only 0.236 F1 and high unsafe false negatives.

4. The method over-invalidates.
   - Mitigation: proposed unnecessary invalidation is 0.030.

5. The paper hides failure cases.
   - Mitigation: landmark relocation, semantic-door relabeling, missed dependencies, delayed update, and conservative over-invalidation are explicit failure modes.

6. This is just replanning.
   - Mitigation: an incremental edge-update baseline is included; the target is cache invalidation before repair.

7. Synthetic evidence is not deployment.
   - Mitigation: hardware and real-SLAM deployment are explicitly outside scope.

## Remaining honest limitations

- No real robot logs.
- No hardware validation.
- Modeled dependency extractors rather than planner-instrumented extractors.
- No continuous dynamics or controller tracking.
- No claim that arbitrary planners can expose perfect dependencies.
