import csv
import json
import os
import re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(__file__))
DOCS = os.path.join(ROOT, "docs")
IN_PATH = os.path.join(DOCS, "related_work_matrix.csv")
OUT_MAP = os.path.join(DOCS, "literature_map.md")
OUT_HOSTILE = os.path.join(DOCS, "hostile_prior_work.md")
OUT_BOUNDARY = os.path.join(DOCS, "novelty_boundary_map.md")
OUT_DECISION = os.path.join(DOCS, "novelty_decision.md")
OUT_CLAIMS = os.path.join(DOCS, "claims.md")
OUT_ATTACKS = os.path.join(DOCS, "reviewer_attacks.md")
OUT_AUDIT = os.path.join(DOCS, "final_audit.md")


def tokens(text):
    return set(re.findall(r"[a-z0-9]+", (text or "").lower()))


def score(row):
    text = " ".join([row.get("title", ""), row.get("abstract", ""), row.get("venue", "")]).lower()
    s = 0
    for kw in [
        "topolog", "map", "slam", "navigation", "planning", "change", "dynamic", "incremental",
        "place recognition", "loop closure", "occupancy", "workspace", "graph", "maintenance",
    ]:
        if kw in text:
            s += 1
    if row.get("year", "").isdigit():
        s += int(row["year"] >= "2015")
    return s


def main():
    with open(IN_PATH, "r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["_score"] = score(r)
    rows.sort(key=lambda r: (r["_score"], r.get("year", "")), reverse=True)
    top300 = rows[:300]
    top200 = rows[:220]
    hostile = [r for r in rows if any(k in ("topology", "topolog", "map", "slam", "navigation") for k in tokens(r.get("title", "") + " " + r.get("abstract", "")))]
    hostile = hostile[:100]

    counts = Counter()
    for r in rows[:1000]:
        counts.update(tokens(r.get("title", "")))

    with open(OUT_MAP, "w", encoding="utf-8") as f:
        f.write("# Literature Map\n\n")
        f.write(f"- Total matrix rows: {len(rows)}\n")
        f.write(f"- Serious skim set: {len(top300)}\n")
        f.write(f"- Deep read set: {len(top200)}\n")
        f.write(f"- Hostile prior-work set: {len(hostile)}\n\n")
        f.write("## Dominant Themes\n\n")
        for k, v in counts.most_common(20):
            if len(k) > 2:
                f.write(f"- {k}: {v}\n")
        f.write("\n## Top 25 Seed Papers\n\n")
        for r in top300[:25]:
            f.write(f"- {r['year']} | {r['title']} | {r['venue']} | {r['source']}\n")

    with open(OUT_HOSTILE, "w", encoding="utf-8") as f:
        f.write("# Hostile Prior Work\n\n")
        for r in hostile:
            f.write(f"- {r['year']} | {r['title']} | {r['venue']}\n")

    with open(OUT_BOUNDARY, "w", encoding="utf-8") as f:
        f.write("# Novelty Boundary Map\n\n")
        f.write("- Seed hypothesis: detect topology changes that invalidate cached robot plans.\n")
        f.write("- Boundary pressure: SLAM/map maintenance, dynamic obstacle handling, topological navigation, place recognition, change detection, replanning.\n")
        f.write("- Candidate novelty gap: a mechanism that infers structural invalidation of cached plans from workspace topology transitions rather than only local obstacle updates or generic replanning triggers.\n")
        f.write("- Stress test: if prior work already treats map-change detection as a planning-invalidation problem, the thesis must shift to a stronger structural abstraction or a new invalidation signal.\n")
        f.write("- Hidden assumption candidates: topology is stable between planning cycles; local occupancy updates imply plan validity; path length is sufficient validity criterion; replanning can be decided from map deltas alone; topological changes are observable from 2D sensing; cached plans remain meaningful under loop-closure/map corrections; dynamic clutter is separable from persistent topology change; environment changes are monotone; navigation and manipulation share the same invalidation rule; semantic labels are unnecessary.\n")

    with open(OUT_DECISION, "w", encoding="utf-8") as f:
        f.write("# Novelty Decision\n\n")
        f.write("Decision: pending deep read of hostile prior work.\n\n")
        f.write("Interim thesis candidates:\n")
        f.write("1. Topology-change detection as cached-plan invalidation for robot navigation and manipulation.\n")
        f.write("2. Workspace structural event detection from incremental map/graph evidence with explicit plan dependency tracing.\n")
        f.write("3. A topology-aware world-state change detector that targets plan cache invalidation instead of generic map differencing.\n")
        f.write("\nCurrent best guess: candidate 3, but only if prior work does not already subsume it.\n")

    with open(OUT_CLAIMS, "w", encoding="utf-8") as f:
        f.write("# Claims\n\n")
        f.write("- The field contains substantial adjacent work on mapping, topology, change detection, and replanning.\n")
        f.write("- The central unresolved gap may be structural invalidation of cached plans rather than mere map updating.\n")
        f.write("- This gap is only novel if the detector uses workspace topology transitions as first-class evidence and demonstrates cases where local occupancy or semantic change signals fail.\n")
        f.write("- Any final claim must be scoped to robotics and embodied physical intelligence.\n")

    with open(OUT_ATTACKS, "w", encoding="utf-8") as f:
        f.write("# Reviewer Attacks\n\n")
        f.write("- This is just map change detection under a new name.\n")
        f.write("- Topology changes are already captured by existing replanners and dynamic SLAM pipelines.\n")
        f.write("- Cached-plan invalidation is an implementation detail, not a research contribution.\n")
        f.write("- The detector may not generalize across sensors, maps, or embodiments.\n")
        f.write("- Improvements may come from better perception rather than a new mechanism.\n")

    with open(OUT_AUDIT, "w", encoding="utf-8") as f:
        f.write("# Final Audit\n\n")
        f.write("Pending paper drafting and evidence collection.\n")

    print(f"wrote summaries from {len(rows)} rows")
    print(f"top300={len(top300)} top200={len(top200)} hostile={len(hostile)}")


if __name__ == "__main__":
    main()
