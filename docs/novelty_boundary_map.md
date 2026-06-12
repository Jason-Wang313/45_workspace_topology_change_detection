# Novelty Boundary Map

- Seed hypothesis: detect topology changes that invalidate cached robot plans.
- Boundary pressure: SLAM/map maintenance, dynamic obstacle handling, topological navigation, place recognition, change detection, replanning.
- Candidate novelty gap: a mechanism that infers structural invalidation of cached plans from workspace topology transitions rather than only local obstacle updates or generic replanning triggers.
- Stress test: if prior work already treats map-change detection as a planning-invalidation problem, the thesis must shift to a stronger structural abstraction or a new invalidation signal.
- Hidden assumption candidates: topology is stable between planning cycles; local occupancy updates imply plan validity; path length is sufficient validity criterion; replanning can be decided from map deltas alone; topological changes are observable from 2D sensing; cached plans remain meaningful under loop-closure/map corrections; dynamic clutter is separable from persistent topology change; environment changes are monotone; navigation and manipulation share the same invalidation rule; semantic labels are unnecessary.
