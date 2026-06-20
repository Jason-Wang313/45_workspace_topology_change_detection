# Paper 45 VLA Highlight Hardening Plan

Date: 2026-06-20

## Objective

Harden Paper 45's visible PDF link-box styling so it matches the VLA-v4 role-model PDF's professional red and green boxed callouts while preserving the final 25-page plan-conditioned workspace topology change detection manuscript, its full-scale benchmark, and all scientific claims.

## Current Evidence

- Canonical PDF: `C:/Users/wangz/Downloads/45.pdf`.
- Current page count: 25.
- Current affected link pages: 4, 5, 6, 7, 8, and 9.
- Current link annotations: 0 green citation/link boxes and 8 red internal-reference boxes.
- Current border state: all 8 link annotations use border `(0, 0, 0)`, so the boxes are invisible.
- Current LaTeX source uses `\usepackage[hidelinks]{hyperref}` in `paper/main.tex`.
- Current full-scale benchmark remains 405,504 compact condition rows and 7,970,586,624,000 represented trial evaluations.

## Role-Model Style Target

Match the VLA-v4 role model's link annotation style:

```tex
\usepackage{hyperref}
\hypersetup{
  colorlinks=false,
  pdfborder={0 0 1},
  citebordercolor={0 1 0},
  linkbordercolor={1 0 0},
  urlbordercolor={0 1 0}
}
```

Expected Paper 45 result after rebuild:

- Page count remains 25.
- All 8 internal-reference link annotations remain red.
- All 8 link annotations use visible border `(0, 0, 1)`.
- The source also defines VLA-style green citation/url borders for any future citation or URL annotations.
- No benchmark data, tables, figures, claims, or manuscript body text changes.

## Execution Plan

1. Render the affected pre-change pages to `C:/Users/wangz/highlight_box_hardening/tmp/pdfs/paper45_before` for baseline visual comparison.
2. Replace `\usepackage[hidelinks]{hyperref}` in `paper/main.tex` with plain `\usepackage{hyperref}` plus the VLA-v4 `\hypersetup` block above.
3. Rebuild using `scripts/build_pdf.ps1`, which exports only `C:/Users/wangz/Downloads/45.pdf`, records build metadata, and removes local `paper/main.pdf`.
4. Verify with `pypdf` that the rebuilt PDF has 25 pages, 8 red link annotations, and 8 `(0, 0, 1)` borders.
5. Render affected post-change pages 4, 5, 6, 7, 8, and 9 and visually inspect the boxes for role-model-like color, line weight, alignment, spacing, and legibility.
6. Update README, child status, and tracked audit/readiness metadata with the final hash, size, and visual hardening evidence.
7. Remove Paper 45 temporary render folders after QA while preserving the shared `role_model` render.
8. Commit and push the clean repo before moving to the next paper.

## Non-Goals

- Do not rerun the benchmark.
- Do not pad content or alter the 25-page manuscript.
- Do not revise claims, tables, captions, figures, or body text unless visual QA exposes a layout defect that requires a tiny local fix.

## Final QA Result

- Rebuilt canonical PDF: `C:/Users/wangz/Downloads/45.pdf`.
- Final page count: 25.
- Final size: 380,492 bytes.
- Final SHA256: `90D1D06ABD953CB99E6091B417F63CB3735D34AB8075D9493FD384FBDCD084A9`.
- Verified annotations: 8 red internal-reference boxes and 8 visible `(0, 0, 1)` borders.
- Rendered pages 4, 5, 6, 7, 8, and 9 at 160 dpi; the boxes match the VLA-v4 role model's thin, professional style and do not create layout collisions.
