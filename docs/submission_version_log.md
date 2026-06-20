# Submission Version Log

## v1

- Recovered paper reported topology dependency accuracy/F1 1.000/1.000 on a small diagnostic.
- Local delta accuracy/F1 was 0.286/0.000.

## v2

- Added dependency-noise stress via `scripts/v2_dependency_stress.py`.
- Found 20% dependency misses reduce F1 to 0.862.
- Found combined 10% missed plus 10% spurious dependencies reduce F1 to 0.873.
- The result identified dependency extraction as the bottleneck.

## v3 full-scale

- Added `scripts/run_full_scale_topology_suite.py`.
- Generated 405,504 compact condition rows representing 7,970,586,624,000 trial evaluations.
- Added 24 workspace families, 16 plan archetypes, 12 perturbation families, 11 policies, 8 extractors, 8 stresses, 9 noise regimes, and 7 splits.
- Rewrote the paper as a 25-page full-scale manuscript.
- Proposed plan-topology dependency policy reaches precision 0.950, recall 0.876, F1 0.912.
- Updated canonical PDF: `C:/Users/wangz/Downloads/45.pdf`.
- Hardened hyperlink styling to VLA-style visible red internal-reference boxes with green citation/url border defaults for future links.
- SHA256: `90D1D06ABD953CB99E6091B417F63CB3735D34AB8075D9493FD384FBDCD084A9`.
