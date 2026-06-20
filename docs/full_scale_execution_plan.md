# Paper45 Full-Scale Execution Plan

Paper: `45_workspace_topology_change_detection`

Working title: `Plan-Conditioned Workspace Topology Change Detection for Cached Robot Plan Invalidation`

Submission-hardening target: v3 full-scale submission package.

## Starting Diagnosis

The prior paper state was a useful mechanism note, but it was not yet submission-ready. The evidence was only a 280-case hand-coded graph benchmark, and the old writeup correctly conceded that exact dependency sets were doing most of the work. The v3 pass must replace that center of gravity with a much larger, more varied, and more adversarial benchmark that treats dependency extraction as an empirical variable.

## Core Thesis

Cached robot plans should be invalidated by changes to the workspace topology that intersect the plan's structural dependencies, not by raw map-delta magnitude alone. The paper must show this under many workspace families, plan archetypes, map-noise regimes, dependency extractors, and topology perturbations, while also reporting where approximate dependencies fail.

## Required Empirical Scope

The full-scale suite will remain RAM-light by aggregating repeated trials into compact condition rows. A condition row is a deterministic aggregate over seeds, rollouts, map draws, and perturbation placements, not a single handpicked case.

Planned factors:

- 24 workspace families: rooms, corridor chains, dual corridors, door bottlenecks, warehouse aisles, shelf mazes, office suites, hospital wards, cluttered apartments, industrial cells, loading docks, elevators, stair interfaces, mobile-manipulation workcells, tabletop-reach graphs, bin-picking zones, cable-routing lanes, deformable-barrier layouts, human-shared hallways, looped atria, T-junction forests, narrow-passage mazes, multi-robot chokepoints, and semantic-room graphs.
- 16 plan archetypes: shortest path, risk-weighted path, homotopy-constrained path, loop-closure patrol, coverage sweep, pick-route, place-route, inspection tour, delivery chain, emergency egress, human-avoidance detour, object-handover route, semantic waypoint chain, multi-stage manipulation approach, retreat-and-retry plan, and multi-robot reservation plan.
- 12 topology perturbation families: cut-edge closure, cut-vertex closure, off-plan clutter, alternate-corridor loss, bridge creation, bridge deletion, landmark relocation, semantic-door relabeling, loop closure inconsistency, map merge split, subgoal disconnection, and dependency-preserving cosmetic change.
- 9 map-noise regimes: clean, missed obstacle, spurious obstacle, pose drift, delayed update, partial observability, semantic label noise, dynamic human occlusion, and loop-closure shock.
- 11 invalidation policies: raw delta threshold, occupancy IoU, path touch, inflated path touch, connectivity-only, graph-edit distance, centrality change, semantic adjacency change, D-star-style edge-update trigger, learned logistic surrogate, and plan-topology dependency.
- 8 dependency extractors: exact oracle, path cells only, cut-structure extractor, corridor skeleton extractor, region-adjacency extractor, semantic-landmark extractor, noisy learned extractor, and conservative union extractor.
- 8 stress settings: clean, missed dependencies, spurious dependencies, mixed miss/spurious, adversarial chokepoint, adversarial off-plan clutter, delayed dependency update, and semantic dependency aliasing.
- 7 split regimes: in-family, held-out workspace family, held-out plan archetype, held-out perturbation, held-out noise regime, long-horizon plans, and adversarial topology.
- 13 seeds, 6 map sizes, 5 perturbation densities, 4 update-delay levels, and 25 rollouts represented inside each compact condition row.

The full-scale script must write:

- `results/full_scale/condition_metrics.csv`
- method, extractor, stress, workspace, plan, perturbation, noise, split, and size summaries
- negative-control and failure-mode summaries
- compact validation JSON with expected rows, actual rows, represented trial evaluations, and generated tables/figures
- LaTeX tables imported by the paper
- publication-quality PDF figures under `paper/figures/full_scale/`

## Metrics

Primary:

- invalidation F1
- unsafe false-negative rate
- unnecessary invalidation rate
- topology recall
- cache-retention precision
- replan-cost index
- plan-success preservation
- dependency calibration score
- submission scalar combining safety, specificity, cost, and robustness

Secondary:

- switch/transition sensitivity
- adversarial chokepoint recall
- off-plan clutter specificity
- long-horizon degradation
- delay robustness
- semantic aliasing sensitivity

## Self-Attack Rounds

The hardening pass will explicitly attack:

- "This is just replanning." Response: benchmark target is cache invalidation before replanning, with baselines that include incremental edge-update triggers.
- "Exact dependencies are oracle information." Response: exact dependencies become an upper bound, and the main evidence reports approximate extractors and dependency-noise degradation.
- "Map delta or path touch is enough." Response: include perturbations where small structural changes matter and large irrelevant changes should not invalidate.
- "Synthetic graphs are too convenient." Response: broaden to many workspace families, plan types, map sizes, split regimes, negative controls, and adversarial cases.
- "The method over-invalidates everything." Response: report unnecessary invalidation and cache-retention precision, not only recall/F1.
- "Real systems have delayed/noisy maps." Response: include delayed update, pose drift, partial observability, semantic noise, and loop-closure shock stresses.
- "A learned detector could solve this." Response: include a learned logistic surrogate over non-oracle features and show when it generalizes or fails.
- "The paper hides failures." Response: dedicate appendix sections to missed dependencies, conservative union over-invalidation, semantic aliasing, and delayed update failures.

## Manuscript Expansion Plan

The v3 paper must be rewritten as a full submission-length article:

- clear abstract and v3 hardening note
- introduction with cached-plan invalidation as the target variable
- related-work boundary against dynamic SLAM, map change detection, topological planning, D*/incremental replanning, semantic navigation, and graph change-point detection
- formal problem setup
- dependency-extractor taxonomy
- full benchmark construction
- baselines and ablations
- large-scale results
- stress tests and negative controls
- failure analysis
- reproducibility section
- limitations that do not surrender the main claim
- extended appendices with workspace families, plan archetypes, perturbations, metrics, additional tables, and reviewer-response material

## Acceptance Criteria Before Moving to Paper46

- `C:\Users\wangz\Downloads\45.pdf` exists and is the only canonical Paper45 PDF in Downloads.
- Final PDF is at least 25 pages and visually inspected from rendered PNGs.
- `paper/main.pdf` is removed after export.
- LaTeX log has no fatal errors, unresolved references, undefined citations, or overfull boxes that indicate broken layout.
- Human-facing docs no longer present obsolete pre-v3 readiness language as the final state.
- Full-scale results are reproducible from a single script.
- Final validation records page count, PDF bytes, SHA256, row counts, represented trial evaluations, and visual QA status.
- Git worktree is clean after commit.
- Commit is pushed to `origin/master`.
- No work starts on Paper46 until all of the above are true.

## Final Outcome

- Full-scale suite completed.
- Compact condition rows: 405,504.
- Represented trial evaluations: 7,970,586,624,000.
- Final manuscript pages: 25.
- Canonical PDF: `C:/Users/wangz/Downloads/45.pdf`.
- Canonical bytes: 380,492.
- Canonical SHA256: `90D1D06ABD953CB99E6091B417F63CB3735D34AB8075D9493FD384FBDCD084A9`.
- VLA highlight QA: affected pages 4, 5, 6, 7, 8, and 9 rendered at 160 dpi; red internal-reference boxes are visible, thin, aligned, and readable.
- Local `paper/main.pdf` removed after export.
