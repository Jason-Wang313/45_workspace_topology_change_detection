# Workspace Topology Change Detection

Paper 45 in the robotics 60-paper batch.

## V2 hardening decision

Decision: workshop-only.

The v2 dependency-noise stress narrows the claim. The clean topology-dependency trigger reaches 1.000 F1, but 20% missed dependencies reduce F1 to 0.862 and combined 10% missed plus 10% spurious dependencies reduce F1 to 0.873. The paper is therefore a mechanism note about plan-conditioned dependency invalidation, not a deployed SLAM/planning system.

Canonical PDF: `C:/Users/wangz/Downloads/45.pdf`

## Contents

- `paper/main.tex`: ICLR-style source with the v2 hardening note.
- `paper/v2_dependency_noise_stress_table.tex`: v2 dependency-noise stress table.
- `paper/figures/topology_invalidation_metrics.png`: synthetic evidence figure.
- `docs/topology_invalidation_cases.csv`: generated perturbation cases.
- `docs/topology_invalidation_summary.json`: original trigger metrics.
- `docs/v2_dependency_noise_stress.json` and `docs/v2_dependency_noise_stress.csv`: v2 stress metrics.
- `scripts/recover_paper45.py`: original recovery generator.
- `scripts/v2_dependency_stress.py`: v2 stress generator.
- `scripts/build_pdf.ps1`: canonical PDF build wrapper.

## Reproduce

Run the v2 stress:

```powershell
python scripts/v2_dependency_stress.py
```

Build the canonical PDF:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/build_pdf.ps1
```
