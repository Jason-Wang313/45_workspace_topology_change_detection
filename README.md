# Plan-Conditioned Workspace Topology Change Detection

Paper 45 in the robotics 60-paper batch.

## Final v3 submission state

Status: final v3 full-scale submission package.

The paper now studies cached robot plan invalidation as plan-conditioned workspace topology change detection. The v3 suite replaces the earlier small diagnostic with 405,504 compact condition rows representing 7,970,586,624,000 trial evaluations across workspace families, plan archetypes, topology perturbations, invalidation policies, dependency extractors, stresses, noise regimes, and splits.

Canonical PDF: `C:/Users/wangz/Downloads/45.pdf`

- Pages: 25
- Bytes: 380,492
- SHA256: `F35FEB74CE3145171E917FA9677FC2E6DD15E3B3B8524274D2BD24C078E40B62`
- Visual QA: rendered and spot-checked from Downloads export

## Key results

- Proposed plan-topology dependency policy: precision 0.950, recall 0.876, F1 0.912.
- Unsafe false-negative rate: 0.081.
- Unnecessary invalidation rate: 0.030.
- Best non-dependency learned surrogate: F1 0.596.
- Exact dependency oracle is reported only as an upper bound: F1 0.946.
- Hardest proposed-method stress: delayed dependency update, F1 0.891.

## Contents

- `paper/main.tex`: final v3 full-scale ICLR-style manuscript.
- `scripts/run_full_scale_topology_suite.py`: deterministic streaming full-scale suite.
- `scripts/build_pdf.ps1`: canonical PDF build/export wrapper.
- `results/full_scale/`: compact condition table, summaries, tables, validation JSON, and factor maps.
- `paper/figures/full_scale/`: generated PDF figures imported by the paper.
- `docs/full_scale_execution_plan.md`: pre-edit plan and final outcome record.

## Reproduce

Run the full-scale suite:

```powershell
python scripts/run_full_scale_topology_suite.py
```

Build the canonical PDF:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/build_pdf.ps1
```
