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
- Canonical SHA256: `F35FEB74CE3145171E917FA9677FC2E6DD15E3B3B8524274D2BD24C078E40B62`.
- Local generated `paper/main.pdf` is removed after build.
- Visual QA: final Downloads PDF rendered to 25 PNG pages and spot-checked.

Decision:
- Submission-ready candidate as a synthetic interface paper with explicit limitations. The supported contribution is plan-conditioned topology-dependency invalidation for cached robot plans, not a deployed SLAM or hardware system.
