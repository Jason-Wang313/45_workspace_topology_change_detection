# Child Status 45

Status: final_v3_full_scale
Attempt: 3
Stage: submission_ready_candidate

Current facts:
- Full-scale suite is present at `scripts/run_full_scale_topology_suite.py`.
- Compact condition rows: 405,504.
- Represented trial evaluations: 7,970,586,624,000.
- Proposed plan-topology dependency policy: precision 0.950, recall 0.876, F1 0.912.
- Exact oracle is retained only as an extractor upper bound, F1 0.946.
- Hardest proposed-method stress is delayed dependency update, F1 0.891.
- Canonical PDF built: `C:/Users/wangz/Downloads/45.pdf`.
- Canonical PDF pages: 25.
- Canonical PDF bytes: 380,492.
- Canonical SHA256: `90D1D06ABD953CB99E6091B417F63CB3735D34AB8075D9493FD384FBDCD084A9`.
- Local generated `paper/main.pdf` is removed after build.
- Visual QA: affected highlight pages 4, 5, 6, 7, 8, and 9 rendered at 160 dpi from the final Downloads PDF.
- Verified 8 red internal-reference boxes and 8 visible `(0, 0, 1)` link borders.
- VLA-style red boxes are thin, aligned, readable, and do not collide with text, figures, tables, or captions.

Decision:
- Submission-ready candidate as a synthetic interface paper with explicit limitations. The supported contribution is plan-conditioned topology-dependency invalidation for cached robot plans, not a deployed SLAM or hardware system.
