# Final Audit

Paper: 45_workspace_topology_change_detection

Decision: workshop-only

Submission-hardening version: v2

## Original positive evidence

- Synthetic topology benchmark size: 280 perturbations.
- Local delta accuracy/F1: 0.286 / 0.000.
- Path touch accuracy/F1: 0.786 / 0.727.
- Topology dependency accuracy/F1: 1.000 / 1.000.

## V2 dependency-noise stress

- 10% dependency misses: F1 0.923.
- 20% dependency misses: F1 0.862.
- 10% spurious dependencies: F1 0.949.
- 10% missed plus 10% spurious dependencies: F1 0.873.

## Audit judgment

The paper survives as a narrow workshop mechanism note. It supports plan-conditioned topology invalidation in a synthetic graph setting, but the perfect clean score depends on hand-defined dependencies. The paper does not establish real SLAM robustness, learned dependency extraction, or hardware readiness.

## Artifacts

- Paper source: `paper/main.tex`
- Original recovery generator: `scripts/recover_paper45.py`
- V2 stress generator: `scripts/v2_dependency_stress.py`
- Original summary: `docs/topology_invalidation_summary.json`
- V2 stress JSON: `docs/v2_dependency_noise_stress.json`
- V2 stress CSV: `docs/v2_dependency_noise_stress.csv`
- V2 stress table: `paper/v2_dependency_noise_stress_table.tex`
- Build wrapper: `scripts/build_pdf.ps1`

## PDF and repository

- Canonical PDF: `C:/Users/wangz/Downloads/45.pdf`
- Local tracked/generated PDF: removed after build
- Desktop copy: absent
- GitHub URL: `https://github.com/Jason-Wang313/45_workspace_topology_change_detection`
