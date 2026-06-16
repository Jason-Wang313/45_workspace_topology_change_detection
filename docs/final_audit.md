# Final Audit

Paper: 45_workspace_topology_change_detection

Decision: submission-ready candidate.

Submission-hardening version: v3 full-scale.

## Positive evidence

- Compact condition rows: 405,504.
- Represented trial evaluations: 7,970,586,624,000.
- Proposed plan-topology dependency policy precision/recall/F1: 0.950 / 0.876 / 0.912.
- Unsafe false-negative rate: 0.081.
- Unnecessary invalidation rate: 0.030.
- Best non-dependency learned surrogate F1: 0.596.
- Exact dependency oracle is only an upper bound, F1 0.946.
- Clean proposed-method stress F1: 0.933.
- Delayed dependency update proposed-method stress F1: 0.891.

## Audit judgment

The paper now supports a submission-scale synthetic interface claim. The contribution is not a deployed SLAM system or hardware benchmark. The supported claim is that cached robot plans should expose topology dependencies so that map updates can invalidate plan caches based on plan support rather than global map-change magnitude.

## Artifacts

- Paper source: `paper/main.tex`
- Full-scale generator: `scripts/run_full_scale_topology_suite.py`
- Full-scale results: `results/full_scale/`
- Full-scale figures: `paper/figures/full_scale/`
- Build wrapper: `scripts/build_pdf.ps1`
- Pre-edit execution plan: `docs/full_scale_execution_plan.md`

## PDF and repository

- Canonical PDF: `C:/Users/wangz/Downloads/45.pdf`
- Pages: 25
- Bytes: 380,492
- SHA256: `F35FEB74CE3145171E917FA9677FC2E6DD15E3B3B8524274D2BD24C078E40B62`
- Local tracked/generated PDF: removed after build
- Visual QA: rendered and spot-checked
- GitHub URL: `https://github.com/Jason-Wang313/45_workspace_topology_change_detection`
