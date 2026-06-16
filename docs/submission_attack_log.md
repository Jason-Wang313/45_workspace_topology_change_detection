# Submission Attack Log

## v3 attack summary

Attack rounds focused on novelty, baselines, dependency extraction, stress tests, failure reporting, and reproducibility.

Key attacks and fixes:

- Oracle dependency attack: added eight dependency extractors and treated exact dependencies only as an upper bound.
- Weak baseline attack: added 11 invalidation policies including incremental edge update and learned surrogate.
- Over-invalidation attack: reported unnecessary invalidation and cache-retention precision.
- Safety attack: reported unsafe false-negative rate and delayed-update stress.
- Synthetic-scope attack: rewrote claims as a synthetic interface contribution and added explicit limitations.
- Hidden-failure attack: added perturbation, stress, workspace, and extractor failure analysis.
- Reproducibility attack: added deterministic streaming generator and validation JSON.
- Layout/submission attack: expanded manuscript to 25 pages and visually checked the exported PDF.

Decision impact: final v3 submission-ready candidate.
