# Hostile Reviewer Response

The strongest hostile review is that dependency extraction is the true bottleneck. The final paper accepts that criticism and makes it empirical: exact dependencies are only an upper bound, while the main policy uses an audited approximate dependency ensemble and reports extractor ablations.

Key responses:

- "This is just replanning." The benchmark target is cache invalidation before repair; an incremental edge-update baseline is included.
- "Exact dependencies make it easy." Exact oracle is only an upper bound. Path-only, cut-structure, corridor, region, semantic, noisy learned, and conservative extractors are reported.
- "Path touch is enough." Path touch reaches only 0.436 F1 in the full benchmark because many relevant dependencies are indirect or semantic.
- "The method over-invalidates." The proposed method has unnecessary invalidation 0.030, while also reducing unsafe false negatives to 0.081.
- "Synthetic evidence is limited." Correct. The paper is framed as a synthetic interface contribution and explicitly excludes hardware and real-SLAM deployment claims.
