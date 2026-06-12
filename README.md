# Workspace Topology Change Detection

Recovered paper 45 in the robotics 60-paper batch.

## Contents

- `paper/main.tex` and `paper/main.pdf`: ICLR-style source and built PDF.
- `paper/figures/topology_invalidation_metrics.png`: synthetic evidence figure.
- `docs/topology_invalidation_cases.csv`: generated perturbation cases.
- `docs/topology_invalidation_summary.json`: metrics for invalidation triggers.
- `docs/`: literature sweep outputs and final audit.
- `scripts/recover_paper45.py`: recovery generator.

## Build

Run from `paper/`:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```
