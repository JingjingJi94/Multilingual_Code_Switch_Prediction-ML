"""
Comparative evaluation of XLM-R and mBERT on the held-out test split.

Iterates test entries at the sequence level (not via DataLoader) to preserve
language_pair metadata. Computes per-pair and overall metrics for each model,
then saves results to JSON for plotting.

Usage:
    python3 evaluation/evaluate.py \
        --xlmr-checkpoint  checkpoints/xlmr_best_sw_f1.pt \
        --mbert-checkpoint checkpoints/mbert_best_sw_f1.pt \
        --test-entries      checkpoints/xlmr_test_entries.pkl \
        --mbert-test-entries checkpoints/mbert_test_entries.pkl \
        --results-dir results/best_sw_f1
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
from transformers import AutoTokenizer
from tqdm import tqdm

from models.dual_head_model import DualHeadCausalModel
from evaluation.metrics import (
    anticipatory_f1, anticipatory_precision, anticipatory_recall,
    duration_accuracy, universality_sigma,
)

BACKBONE_NAMES = {
    "xlmr":  "xlm-roberta-base",
    "mbert": "bert-base-multilingual-cased",
}
WINDOW_SIZE = 64

# ── Arguments ────────────────────────────────────────────────────────────────
parser = argparse.ArgumentParser(description="Evaluate XLM-R and mBERT on the test split.")
parser.add_argument("--xlmr-checkpoint",  type=str, required=True,
    help="Path to XLM-R .pt checkpoint")
parser.add_argument("--mbert-checkpoint", type=str, required=True,
    help="Path to mBERT .pt checkpoint")
parser.add_argument("--test-entries", type=str,
    default="checkpoints/xlmr_test_entries.pkl",
    help="Path to XLM-R test entries .pkl")
parser.add_argument("--mbert-test-entries", type=str,
    default=None,
    help="Path to mBERT test entries .pkl. If not set, falls back to --test-entries.")
parser.add_argument("--xlmr-zeroshot", type=str, default=None,
    help="Path to XLM-R zero-shot entries .pkl (French-English, Korean-English).")
parser.add_argument("--mbert-zeroshot", type=str, default=None,
    help="Path to mBERT zero-shot entries .pkl (French-English, Korean-English).")
parser.add_argument("--zeroshot-sample", type=int, default=800,
    help="Max samples per zero-shot language pair (default: 800). Set 0 to disable.")
parser.add_argument("--results-dir", default="results",
    help="Directory to save eval_results.json (default: results/)")
args = parser.parse_args()

os.makedirs(args.results_dir, exist_ok=True)
if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")
print(f"Device: {device}")

# ── Load test entries (each model uses its own pkl) ───────────────────────────
xlmr_test_path  = args.test_entries
mbert_test_path = args.mbert_test_entries or args.test_entries

print(f"\nLoading XLM-R  test entries: {xlmr_test_path}")
with open(xlmr_test_path, "rb") as f:
    xlmr_test_entries = pickle.load(f)

print(f"Loading mBERT  test entries: {mbert_test_path}")
with open(mbert_test_path, "rb") as f:
    mbert_test_entries = pickle.load(f)

def sample_zeroshot(entries, n, seed=42):
    import random, collections
    rng = random.Random(seed)
    by_pair = collections.defaultdict(list)
    for e in entries:
        by_pair[e["language_pair"]].append(e)
    sampled = []
    for pair, items in by_pair.items():
        rng.shuffle(items)
        sampled.extend(items[:n])
        print(f"  Zero-shot {pair}: {min(len(items), n)}/{len(items)} sampled")
    return sampled

# Append zero-shot entries if provided
if args.xlmr_zeroshot:
    print(f"Loading XLM-R  zero-shot entries: {args.xlmr_zeroshot}")
    with open(args.xlmr_zeroshot, "rb") as f:
        zs = pickle.load(f)
    if args.zeroshot_sample > 0:
        zs = sample_zeroshot(zs, args.zeroshot_sample)
    xlmr_test_entries = xlmr_test_entries + zs

if args.mbert_zeroshot:
    print(f"Loading mBERT  zero-shot entries: {args.mbert_zeroshot}")
    with open(args.mbert_zeroshot, "rb") as f:
        zs = pickle.load(f)
    if args.zeroshot_sample > 0:
        zs = sample_zeroshot(zs, args.zeroshot_sample)
    mbert_test_entries = mbert_test_entries + zs

print(f"XLM-R  test sequences (total): {len(xlmr_test_entries)}")
print(f"mBERT  test sequences (total): {len(mbert_test_entries)}")

test_entries_map = {
    "xlmr":  xlmr_test_entries,
    "mbert": mbert_test_entries,
}

# ── Inference ─────────────────────────────────────────────────────────────────
BATCH_SIZE = 128  # tune down to 64 if you get MPS out-of-memory errors

def build_windows(input_ids, pad_id):
    """Pre-build all sliding windows for one sequence as a 2-D list."""
    L = len(input_ids)
    windows = []
    for t in range(L - 1):
        start = t - WINDOW_SIZE + 1
        if start >= 0:
            window = input_ids[start:t + 1]
        else:
            window = [pad_id] * (-start) + input_ids[0:t + 1]
        window = window[-WINDOW_SIZE:]
        if len(window) < WINDOW_SIZE:
            window = [pad_id] * (WINDOW_SIZE - len(window)) + window
        windows.append(window)
    return windows  # shape: (L-1, WINDOW_SIZE)


def run_inference(entries, backbone_key, checkpoint_path):
    """
    Batched inference over all entries.
    Returns a dict: {language_pair -> {"ysw_true": [...], "ysw_pred": [...],
                                       "ydur_true": [...], "ydur_pred": [...]}}
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
            pair      = entry.get("language_pair", "UNK")
            input_ids = entry["input_ids"]
            ysw       = entry["ysw"]
            ydur      = entry["ydur"]

            windows = build_windows(input_ids, pad_id)  # (L-1, WINDOW_SIZE)
            n = len(windows)

            sw_preds, dur_preds = [], []
            for i in range(0, n, BATCH_SIZE):
                batch = windows[i:i + BATCH_SIZE]
                ids_tensor = torch.tensor(batch, dtype=torch.long).to(device)   # (B, W)
                attn_mask  = (ids_tensor != pad_id).long()                       # (B, W)

                switch_logits, dur_logits = model(ids_tensor, attn_mask)         # (B,2), (B,3)
                sw_preds.extend(switch_logits.argmax(dim=-1).cpu().tolist())
                dur_preds.extend(dur_logits.argmax(dim=-1).cpu().tolist())

            pair_data[pair]["ysw_true"].extend(ysw[:n])
            pair_data[pair]["ysw_pred"].extend(sw_preds)
            pair_data[pair]["ydur_true"].extend(ydur[:n])
            pair_data[pair]["ydur_pred"].extend(dur_preds)

    return pair_data


# ── Metrics ───────────────────────────────────────────────────────────────────
def compute_pair_metrics(pair_data):
    """Compute metrics per language pair and overall from collected predictions."""
    per_pair = {}
    for pair, d in sorted(pair_data.items()):
        per_pair[pair] = {
            "anticipatory_f1":        anticipatory_f1(d["ysw_true"], d["ysw_pred"]),
            "anticipatory_precision":  anticipatory_precision(d["ysw_true"], d["ysw_pred"]),
            "anticipatory_recall":     anticipatory_recall(d["ysw_true"], d["ysw_pred"]),
            "duration_accuracy":       duration_accuracy(d["ydur_true"], d["ydur_pred"]),
            "n_tokens":                len(d["ysw_true"]),
        }

    all_ysw_true  = sum((d["ysw_true"]  for d in pair_data.values()), [])
    all_ysw_pred  = sum((d["ysw_pred"]  for d in pair_data.values()), [])
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


# ── Run inference for both models ─────────────────────────────────────────────
results = {}
for backbone_key, checkpoint in [("xlmr", args.xlmr_checkpoint), ("mbert", args.mbert_checkpoint)]:
    print(f"\n=== {backbone_key.upper()} ===")
    pair_data            = run_inference(test_entries_map[backbone_key], backbone_key, checkpoint)
    per_pair, overall, sigma = compute_pair_metrics(pair_data)
    results[backbone_key] = {"per_pair": per_pair, "overall": overall, "universality_sigma": sigma}


# ── Print comparison table ────────────────────────────────────────────────────
print(f"\n{'='*80}")
print("RESULTS — Anticipatory F1 / Precision / Recall / Duration Accuracy")
print(f"{'='*80}")
print(f"{'Language Pair':<22} {'Model':<8} {'F1':>6} {'Prec':>6} {'Rec':>6} {'DurAcc':>8}")
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

# ── Save JSON ─────────────────────────────────────────────────────────────────
out_path = os.path.join(args.results_dir, "eval_results.json")
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nResults saved to {out_path}")