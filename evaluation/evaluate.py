"""
Comparative evaluation of XLM-R and mBERT on the held-out test split.

Iterates test entries at the sequence level (not via DataLoader) to preserve
language_pair metadata. Computes per-pair and overall metrics for each model,
then saves results to JSON for plotting.

Usage:
    python3 evaluation/evaluate.py \
        --xlmr-checkpoint checkpoints/xlmr_epoch5.pt \
        --mbert-checkpoint checkpoints/mbert_epoch5.pt
"""
import argparse
import json
import os
import pickle
import sys
sys.path.append(".")

from collections import defaultdict

import numpy as np
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer
from tqdm import tqdm

from models.dual_head_model import DualHeadCausalModel
from evaluation.metrics import (
    anticipatory_f1, anticipatory_precision, anticipatory_recall,
    duration_accuracy, universality_sigma,
)

BACKBONE_NAMES = {
    "xlmr": "xlm-roberta-base",
    "mbert": "bert-base-multilingual-cased",
}
WINDOW_SIZE = 64

parser = argparse.ArgumentParser(description="Evaluate XLM-R and mBERT on the test split.")
parser.add_argument("--xlmr-checkpoint", type=str, required=True, help="Path to XLM-R .pt checkpoint")
parser.add_argument("--mbert-checkpoint", type=str, required=True, help="Path to mBERT .pt checkpoint")
parser.add_argument("--results-dir", default="results", help="Directory to save eval_results.json (default: results/)")
args = parser.parse_args()

os.makedirs(args.results_dir, exist_ok=True)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Device: {device}")

# Load test entries (both models share the same seed=42 split — use xlmr's)
test_pkl = "checkpoints/xlmr_test_entries.pkl"
print(f"\nLoading test entries: {test_pkl}")
with open(test_pkl, "rb") as f:
    test_entries = pickle.load(f)
print(f"Test sequences: {len(test_entries)}")


def run_inference(entries, backbone_key, checkpoint_path):
    """
    Run model inference over all entries, collecting predictions per language pair.
    Returns a dict: {language_pair -> {"ysw_true": [...], "ysw_pred": [...], "ydur_true": [...], "ydur_pred": [...]}}
    """
    backbone_name = BACKBONE_NAMES[backbone_key]
    tokenizer = AutoTokenizer.from_pretrained(backbone_name)
    pad_id = tokenizer.pad_token_id or 0

    model = DualHeadCausalModel(backbone_name=backbone_name).to(device)
    model.load_state_dict(torch.load(checkpoint_path, map_location=device))
    model.eval()
    print(f"  Loaded checkpoint: {checkpoint_path}")

    pair_data = defaultdict(lambda: {"ysw_true": [], "ysw_pred": [], "ydur_true": [], "ydur_pred": []})

    with torch.no_grad():
        for entry in tqdm(entries, desc=f"  [{backbone_key}] inference"):
            pair = entry.get("language_pair", "UNK")
            input_ids = entry["input_ids"]
            ysw = entry["ysw"]
            ydur = entry["ydur"]
            L = len(input_ids)

            for t in range(L - 1):  # predict switch at t+1, label is ysw[t]
                # Build left-padded window ending at t
                start = t - WINDOW_SIZE + 1
                if start >= 0:
                    window = input_ids[start:t + 1]
                    pad_len = 0
                else:
                    window = input_ids[0:t + 1]
                    pad_len = -start

                if pad_len > 0:
                    window = [pad_id] * pad_len + window

                window = window[-WINDOW_SIZE:]  # ensure exact length
                if len(window) < WINDOW_SIZE:
                    window = [pad_id] * (WINDOW_SIZE - len(window)) + window

                ids_tensor = torch.tensor(window, dtype=torch.long).unsqueeze(0).to(device)
                attn_mask = (ids_tensor != pad_id).long()

                switch_logits, dur_logits = model(ids_tensor, attn_mask)
                sw_pred = int(switch_logits.argmax(dim=-1).item())
                dur_pred = int(dur_logits.argmax(dim=-1).item())

                pair_data[pair]["ysw_true"].append(ysw[t])
                pair_data[pair]["ysw_pred"].append(sw_pred)
                pair_data[pair]["ydur_true"].append(ydur[t])
                pair_data[pair]["ydur_pred"].append(dur_pred)

    return pair_data


def compute_pair_metrics(pair_data):
    """Compute metrics per language pair from collected predictions."""
    per_pair = {}
    for pair, d in sorted(pair_data.items()):
        per_pair[pair] = {
            "anticipatory_f1":        anticipatory_f1(d["ysw_true"], d["ysw_pred"]),
            "anticipatory_precision":  anticipatory_precision(d["ysw_true"], d["ysw_pred"]),
            "anticipatory_recall":     anticipatory_recall(d["ysw_true"], d["ysw_pred"]),
            "duration_accuracy":       duration_accuracy(d["ydur_true"], d["ydur_pred"]),
            "n_tokens":                len(d["ysw_true"]),
        }
    # Overall across all pairs
    all_ysw_true = sum((d["ysw_true"] for d in pair_data.values()), [])
    all_ysw_pred = sum((d["ysw_pred"] for d in pair_data.values()), [])
    all_ydur_true = sum((d["ydur_true"] for d in pair_data.values()), [])
    all_ydur_pred = sum((d["ydur_pred"] for d in pair_data.values()), [])

    overall = {
        "anticipatory_f1":        anticipatory_f1(all_ysw_true, all_ysw_pred),
        "anticipatory_precision":  anticipatory_precision(all_ysw_true, all_ysw_pred),
        "anticipatory_recall":     anticipatory_recall(all_ysw_true, all_ysw_pred),
        "duration_accuracy":       duration_accuracy(all_ydur_true, all_ydur_pred),
        "n_tokens":                len(all_ysw_true),
    }
    sigma = universality_sigma({p: v["anticipatory_f1"] for p, v in per_pair.items()})
    return per_pair, overall, sigma


# Run inference for both models
results = {}
for backbone_key, checkpoint in [("xlmr", args.xlmr_checkpoint), ("mbert", args.mbert_checkpoint)]:
    print(f"\n=== {backbone_key.upper()} ===")
    pair_data = run_inference(test_entries, backbone_key, checkpoint)
    per_pair, overall, sigma = compute_pair_metrics(pair_data)
    results[backbone_key] = {"per_pair": per_pair, "overall": overall, "universality_sigma": sigma}

# Print comparison table
print(f"\n{'='*80}")
print("RESULTS — Anticipatory F1 / Precision / Recall / Duration Accuracy")
print(f"{'='*80}")
header = f"{'Language Pair':<22} {'Model':<8} {'F1':>6} {'Prec':>6} {'Rec':>6} {'DurAcc':>8}"
print(header)
print("-" * 60)

all_pairs = sorted({p for r in results.values() for p in r["per_pair"]})
for pair in all_pairs:
    for model_key in ["xlmr", "mbert"]:
        m = results[model_key]["per_pair"].get(pair, {})
        print(f"{pair:<22} {model_key:<8} "
              f"{m.get('anticipatory_f1', 0):>6.4f} "
              f"{m.get('anticipatory_precision', 0):>6.4f} "
              f"{m.get('anticipatory_recall', 0):>6.4f} "
              f"{m.get('duration_accuracy', 0):>8.4f}")
    print()

print("-" * 60)
for model_key in ["xlmr", "mbert"]:
    o = results[model_key]["overall"]
    s = results[model_key]["universality_sigma"]
    print(f"{'OVERALL':<22} {model_key:<8} "
          f"{o['anticipatory_f1']:>6.4f} "
          f"{o['anticipatory_precision']:>6.4f} "
          f"{o['anticipatory_recall']:>6.4f} "
          f"{o['duration_accuracy']:>8.4f}  "
          f"σ={s:.4f}")

# Save JSON for plotting
out_path = os.path.join(args.results_dir, "eval_results.json")
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nResults saved to {out_path}")
