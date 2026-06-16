# Reproducibility Checklist

## Commands

Run full-scale suite:

```powershell
python scripts/run_full_scale_topology_suite.py
```

Build canonical PDF:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/build_pdf.ps1
```

## Generated artifacts

- `results/full_scale/condition_metrics.csv`
- `results/full_scale/experiment_summary.json`
- `results/full_scale/experiment_validation.json`
- `results/full_scale/factor_maps.json`
- `results/full_scale/*_summary.csv`
- `results/full_scale/table_*.tex`
- `paper/figures/full_scale/*.pdf`
- `C:/Users/wangz/Downloads/45.pdf`

## Final PDF metadata

- Pages: 25
- Bytes: 380,492
- SHA256: `F35FEB74CE3145171E917FA9677FC2E6DD15E3B3B8524274D2BD24C078E40B62`
- Local `paper/main.pdf` removed: yes
- Visual QA: rendered to 25 PNG pages and spot-checked
