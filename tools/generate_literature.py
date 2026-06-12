import csv
import json
import os
import re
import sys
import time
from collections import defaultdict
from datetime import datetime

import requests


OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs")
os.makedirs(OUT_DIR, exist_ok=True)

RELATED_PATH = os.path.join(OUT_DIR, "related_work_matrix.csv")
STATE_PATH = os.path.join(OUT_DIR, "literature_state.json")

QUERIES = [
    "robot topology change detection",
    "workspace change detection robotics",
    "dynamic environment map change detection robot",
    "topological map maintenance robot",
    "cached plan invalidation robot",
    "map update detection robot navigation",
    "topological navigation dynamic environments",
    "semantic map change detection robotics",
    "environment change detection SLAM",
    "place recognition dynamic environment robotics",
    "change detection occupancy grid robotics",
    "topological planning changing environment",
    "robot map maintenance dynamic obstacles",
    "robust robot planning topology changes",
    "workspace topology robotics",
    "graph-based navigation dynamic environments",
    "incremental mapping change detection robot",
    "loop closure map change detection",
    "robotic workspace topology",
    "physical reasoning map changes robotics",
]

FIELDS = [
    "query",
    "source",
    "doi",
    "title",
    "year",
    "venue",
    "authors",
    "abstract",
    "url",
    "problem_claimed",
    "mechanism",
    "hidden_assumptions",
    "fixed_variables",
    "failure_modes",
    "novelty_effect",
    "open_questions",
]


def load_state():
    if os.path.exists(STATE_PATH):
        with open(STATE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"seen": {}, "rows": 0}


def save_state(state):
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, sort_keys=True)


def norm(s):
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def clean_text(s):
    if not s:
        return ""
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def summarize(title, abstract):
    text = (title + " " + abstract).lower()
    problem = "detect or track changes in robot workspace structure or map state"
    mechanism = "metadata-only screening from title/abstract"
    hidden = []
    fixed = []
    failure = []
    novelty = "candidate related work for topology-change detection framing"
    openq = "needs full-text validation"
    if "topolog" in text:
        hidden.append("topology can be represented reliably in a graph or symbolic abstraction")
        fixed.append("workspace discretization")
    if "slam" in text or "mapping" in text or "map" in text:
        hidden.append("map updates are sufficiently local and observable from sensors")
        fixed.append("sensor noise model")
        failure.append("sensitive to perceptual aliasing and unobserved occlusions")
    if "dynamic" in text or "change" in text:
        hidden.append("environment change is slow enough to be segmented from motion")
        failure.append("false alarms from temporary clutter")
    if "plan" in text or "navigation" in text or "path" in text:
        fixed.append("planner and cost function")
    if "place recognition" in text or "loop closure" in text:
        hidden.append("training/test appearance distributions overlap")
        failure.append("domain shift causes missed matches")
    if not hidden:
        hidden = ["unknown from abstract"]
    if not fixed:
        fixed = ["unknown from abstract"]
    if not failure:
        failure = ["unknown from abstract"]
    return problem, mechanism, "; ".join(sorted(set(hidden))), "; ".join(sorted(set(fixed))), "; ".join(sorted(set(failure))), novelty, openq


def crossref_query(query, rows=100, offset=0):
    url = "https://api.crossref.org/works"
    params = {
        "query.title": query,
        "rows": rows,
        "offset": offset,
        "select": "DOI,title,author,issued,container-title,abstract,URL,type",
    }
    r = requests.get(url, params=params, timeout=30, headers={"User-Agent": "codex-literature-sweep/1.0"})
    r.raise_for_status()
    return r.json()["message"]["items"]


def arxiv_query(query, start=0, max_results=50):
    url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": f"all:{query}",
        "start": start,
        "max_results": max_results,
    }
    r = requests.get(url, params=params, timeout=30, headers={"User-Agent": "codex-literature-sweep/1.0"})
    r.raise_for_status()
    return r.text


def parse_arxiv(xml_text):
    items = []
    for entry in re.findall(r"<entry>(.*?)</entry>", xml_text, flags=re.S):
        def tag(name):
            m = re.search(rf"<{name}[^>]*>(.*?)</{name}>", entry, flags=re.S)
            return clean_text(re.sub(r"<.*?>", "", m.group(1))) if m else ""

        title = tag("title")
        abstract = tag("summary")
        doi = ""
        m = re.search(r'<arxiv:doi>(.*?)</arxiv:doi>', entry, flags=re.S)
        if m:
            doi = clean_text(m.group(1))
        authors = ", ".join(re.findall(r"<name>(.*?)</name>", entry))
        year = ""
        m = re.search(r"<published>(\d{4})-", entry)
        if m:
            year = m.group(1)
        items.append({
            "source": "arxiv",
            "doi": doi,
            "title": title,
            "year": year,
            "venue": "arXiv",
            "authors": authors,
            "abstract": abstract,
            "url": re.search(r'<id>(.*?)</id>', entry).group(1) if re.search(r'<id>(.*?)</id>', entry) else "",
        })
    return items


def main():
    state = load_state()
    seen = state.get("seen", {})
    rows = []
    if os.path.exists(RELATED_PATH):
        with open(RELATED_PATH, "r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
                key = norm(row.get("doi") or row.get("title"))
                if key:
                    seen[key] = 1

    for q in QUERIES:
        try:
            items = crossref_query(q, rows=100, offset=0)
        except Exception:
            items = []
        for item in items:
            title = clean_text(" ".join(item.get("title") or []))
            doi = clean_text(item.get("DOI", ""))
            key = norm(doi or title)
            if not key or key in seen:
                continue
            year = ""
            issued = item.get("issued", {}).get("date-parts", [[]])
            if issued and issued[0]:
                year = str(issued[0][0])
            authors = ", ".join(
                f"{a.get('family','')}, {a.get('given','')}".strip(", ")
                for a in item.get("author", [])[:10]
            )
            abstract = clean_text(re.sub(r"<.*?>", "", item.get("abstract", "") or ""))
            prob, mech, hidden, fixed, failure, novelty, openq = summarize(title, abstract)
            rows.append({
                "query": q,
                "source": "crossref",
                "doi": doi,
                "title": title,
                "year": year,
                "venue": clean_text(" ".join(item.get("container-title") or [])),
                "authors": authors,
                "abstract": abstract,
                "url": item.get("URL", ""),
                "problem_claimed": prob,
                "mechanism": mech,
                "hidden_assumptions": hidden,
                "fixed_variables": fixed,
                "failure_modes": failure,
                "novelty_effect": novelty,
                "open_questions": openq,
            })
            seen[key] = 1
            if len(rows) >= 1200:
                break
        if len(rows) >= 1200:
            break
        time.sleep(0.2)

    if len(rows) < 1000:
        try:
            xml = arxiv_query("robot topology change detection", start=0, max_results=200)
            for item in parse_arxiv(xml):
                key = norm(item.get("doi") or item.get("title"))
                if not key or key in seen:
                    continue
                title = item["title"]
                abstract = item["abstract"]
                prob, mech, hidden, fixed, failure, novelty, openq = summarize(title, abstract)
                rows.append({
                    "query": "arxiv fallback",
                    **item,
                    "problem_claimed": prob,
                    "mechanism": mech,
                    "hidden_assumptions": hidden,
                    "fixed_variables": fixed,
                    "failure_modes": failure,
                    "novelty_effect": novelty,
                    "open_questions": openq,
                })
                seen[key] = 1
        except Exception:
            pass

    with open(RELATED_PATH, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in FIELDS})

    state["seen"] = seen
    state["rows"] = len(rows)
    state["updated"] = datetime.utcnow().isoformat() + "Z"
    save_state(state)
    print(f"Wrote {len(rows)} rows to {RELATED_PATH}")


if __name__ == "__main__":
    sys.exit(main())
