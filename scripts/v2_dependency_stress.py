import csv
import json
import os
import random

from recover_paper45 import DOCS, PAPER, evaluate_cases, metrics


def noisy_predictions(rows, miss_rate=0.0, spurious_rate=0.0, seed=45):
    rng = random.Random(seed)
    noisy_rows = []
    for row in rows:
        pred = bool(row["topology_dependency"])
        if pred and rng.random() < miss_rate:
            pred = False
        elif not pred and rng.random() < spurious_rate:
            pred = True
        out = dict(row)
        out["noisy_topology"] = pred
        noisy_rows.append(out)
    return noisy_rows


def summarize(rows):
    experiments = [
        ("Path touch", [{**row, "score": row["path_touch"]} for row in rows]),
        ("Topology dependency", [{**row, "score": row["topology_dependency"]} for row in rows]),
        (
            "Topology, 10% dependency misses",
            [{**row, "score": row["noisy_topology"]} for row in noisy_predictions(rows, miss_rate=0.10)],
        ),
        (
            "Topology, 20% dependency misses",
            [{**row, "score": row["noisy_topology"]} for row in noisy_predictions(rows, miss_rate=0.20)],
        ),
        (
            "Topology, 10% spurious dependencies",
            [{**row, "score": row["noisy_topology"]} for row in noisy_predictions(rows, spurious_rate=0.10)],
        ),
        (
            "Topology, 10% miss + 10% spurious",
            [
                {**row, "score": row["noisy_topology"]}
                for row in noisy_predictions(rows, miss_rate=0.10, spurious_rate=0.10)
            ],
        ),
    ]
    out = []
    for name, scored_rows in experiments:
        m = metrics(scored_rows, "score")
        out.append(
            {
                "method": name,
                "accuracy": m["accuracy"],
                "precision": m["precision"],
                "recall": m["recall"],
                "f1": m["f1"],
            }
        )
    return out


def tex_escape(text):
    return text.replace("%", "\\%")


def write_outputs(rows):
    os.makedirs(DOCS, exist_ok=True)
    summary_path = os.path.join(DOCS, "v2_dependency_noise_stress.json")
    csv_path = os.path.join(DOCS, "v2_dependency_noise_stress.csv")
    table_path = os.path.join(PAPER, "v2_dependency_noise_stress_table.tex")

    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2)
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["method", "accuracy", "precision", "recall", "f1"])
        writer.writeheader()
        writer.writerows(rows)

    table = (
        "\\begin{tabular}{lcccc}\n"
        "\\toprule\n"
        "Trigger & Accuracy & Precision & Recall & F1 \\\\\n"
        "\\midrule\n"
        + "\n".join(
            f"{tex_escape(row['method'])} & {row['accuracy']:.3f} & {row['precision']:.3f} & {row['recall']:.3f} & {row['f1']:.3f} \\\\"
            for row in rows
        )
        + "\n\\bottomrule\n"
        "\\end{tabular}\n"
    )
    with open(table_path, "w", encoding="utf-8") as f:
        f.write(table)


def main():
    rows = summarize(evaluate_cases())
    write_outputs(rows)
    print(json.dumps(rows, indent=2))


if __name__ == "__main__":
    main()
