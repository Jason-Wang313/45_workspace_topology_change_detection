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
- SHA256: `90D1D06ABD953CB99E6091B417F63CB3735D34AB8075D9493FD384FBDCD084A9`
- Local `paper/main.pdf` removed: yes
- Visual QA: render pages 4, 5, 6, 7, 8, and 9 at 160 dpi and confirm VLA-style red internal-reference boxes are thin, aligned, readable, and collision-free.
