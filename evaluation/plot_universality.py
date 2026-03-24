"""
Bar chart comparing XLM-R and mBERT anticipatory F1 per language pair,
with universality σ annotations.

Usage:
    python3 evaluation/plot_universality.py --results-json results/eval_results.json
"""
import argparse
import json
import os

import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser(description="Plot per-pair F1 bar chart from eval results.")
parser.add_argument("--results-json", default="results/eval_results.json",
                    help="Path to eval_results.json (default: results/eval_results.json)")
parser.add_argument("--out", default=None,
                    help="Output PNG path (default: same dir as results-json, universality_bar_chart.png)")
args = parser.parse_args()

with open(args.results_json) as f:
    results = json.load(f)

out_path = args.out or os.path.join(os.path.dirname(args.results_json), "universality_bar_chart.png")

# Collect all language pairs
all_pairs = sorted({p for r in results.values() for p in r["per_pair"]})
models = ["xlmr", "mbert"]
model_labels = {"xlmr": "XLM-R", "mbert": "mBERT"}
colors = {"xlmr": "#4C72B0", "mbert": "#DD8452"}

x = np.arange(len(all_pairs))
width = 0.35

fig, ax = plt.subplots(figsize=(max(8, len(all_pairs) * 2), 5))

for i, model_key in enumerate(models):
    f1_values = [
        results[model_key]["per_pair"].get(pair, {}).get("anticipatory_f1", 0.0)
        for pair in all_pairs
    ]
    offset = (i - 0.5) * width
    bars = ax.bar(x + offset, f1_values, width, label=model_labels[model_key],
                  color=colors[model_key], alpha=0.85, edgecolor="white")
    for bar, val in zip(bars, f1_values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.005,
                f"{val:.3f}", ha="center", va="bottom", fontsize=8)

ax.set_xlabel("Language Pair")
ax.set_ylabel("Anticipatory F1")
ax.set_title("Anticipatory F1 per Language Pair: XLM-R vs mBERT")
ax.set_xticks(x)
ax.set_xticklabels(all_pairs, rotation=15, ha="right")
ax.set_ylim(0, min(1.05, ax.get_ylim()[1] + 0.1))
ax.legend()

# Annotate sigma
sigma_text = "  ".join(
    f"{model_labels[m]} σ={results[m]['universality_sigma']:.4f}"
    for m in models
)
ax.text(0.5, 0.97, sigma_text, transform=ax.transAxes,
        ha="center", va="top", fontsize=9,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", edgecolor="gray", alpha=0.8))

plt.tight_layout()
plt.savefig(out_path, dpi=150)
print(f"Saved: {out_path}")
