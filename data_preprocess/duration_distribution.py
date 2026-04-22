import pickle
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from collections import Counter

# ── Load preprocessed data ────────────────────────────────────────────────────
# Update path to your preprocessed pkl file
PKL_PATH = "./data_preprocess/preprocessed_data_xlmr.pkl"

with open(PKL_PATH, "rb") as f:
    preprocessed_data = pickle.load(f)

# ── Collect ydur labels per language pair ─────────────────────────────────────
TRAINING_PAIRS = [
    "Spanish-English",
    "Chinese-English",
    "Hindi-English",
    "Arabic-English",
]

DURATION_LABELS = {
    0: "Short\n(1–2 tokens)",
    1: "Medium\n(3–6 tokens)",
    2: "Long\n(7+ tokens)",
}

COLORS = ["#4C72B0", "#DD8452", "#55A868"]
BAR_LABELS = [DURATION_LABELS[i] for i in range(3)]

# Build counts: {language_pair: Counter({0: n, 1: n, 2: n})}
counts = {pair: Counter() for pair in TRAINING_PAIRS}

for sample in preprocessed_data:
    pair = sample["language_pair"]
    if pair not in TRAINING_PAIRS:
        continue
    for label in sample["ydur"]:
        if label != -1:   # ignore non-switch tokens
            counts[pair][label] += 1

# ── Plot — single bar chart across all 4 pairs combined ──────────────────────
combined = Counter()
for pair in TRAINING_PAIRS:
    combined += counts[pair]

total = sum(combined.values())
pcts  = [combined[i] / total * 100 for i in range(3)]
vals  = [combined[i] for i in range(3)]

fig, ax = plt.subplots(figsize=(7, 5))
fig.suptitle("Switch Duration Distribution Across All Training Pairs",
             fontsize=13, fontweight="bold")

bars = ax.bar(BAR_LABELS, pcts, color=COLORS, edgecolor="white", linewidth=0.8, width=0.5)

for bar, pct, count in zip(bars, pcts, vals):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.5,
        f"{pct:.1f}%\n({count:,})",
        ha="center", va="bottom", fontsize=10, color="#333333"
    )

ax.set_ylabel("Percentage of Switch Tokens (%)", fontsize=10)
ax.set_xlabel("Duration Class", fontsize=10)
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.0f%%"))
ax.set_ylim(0, max(pcts) * 1.25)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.text(1.0, -0.12, f"Total switch tokens: {total:,}",
        ha="center", transform=ax.transAxes, fontsize=9, color="gray")

plt.tight_layout()
plt.savefig("duration_distribution.png", dpi=150, bbox_inches="tight")
plt.show()