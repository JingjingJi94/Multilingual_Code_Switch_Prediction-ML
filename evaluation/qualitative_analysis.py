"""
Qualitative analysis: Inter-sentential vs Intra-sentential code-switching.

Steps:
  1. Augment test entries with switch_types labels (inter/intra/None)
  2. Run inference once on all entries (both models)
  3. Token-level bucketing by switch_type → compute F1 per type
  4. Collect Successful Predictions and False Alarms as concrete examples

Usage:
    python3 evaluation/qualitative_analysis.py \
        --xlmr-checkpoint   testdata_model/xlmr_best_sw_f1.pt \
        --mbert-checkpoint  testdata_model/mbert_best_sw_f1.pt \
        --xlmr-entries      testdata_model/xlmr_test_entries.pkl \
        --mbert-entries     testdata_model/mbert_test_entries.pkl \
        --xlmr-zeroshot     testdata_model/preprocessed_zeroshot_xlmr.pkl \
        --mbert-zeroshot    testdata_model/preprocessed_zeroshot_mbert.pkl \
        --results-dir       results/qualitative
"""

import argparse
import json
import os
import pickle
import sys
sys.path.append(".")

import numpy as np
import torch
from transformers import AutoTokenizer
from tqdm import tqdm

from models.dual_head_model import DualHeadCausalModel
from evaluation.metrics import anticipatory_f1, anticipatory_precision, anticipatory_recall, duration_accuracy

# ── Constants ─────────────────────────────────────────────────────────────────
BACKBONE_NAMES = {
    "xlmr":  "xlm-roberta-base",
    "mbert": "bert-base-multilingual-cased",
}
WINDOW_SIZE = 64
BATCH_SIZE  = 128

SENT_END = {".", "!", "?", "।", "。", "！", "？", "؟", "..."}

# ── Args ──────────────────────────────────────────────────────────────────────
parser = argparse.ArgumentParser()
parser.add_argument("--xlmr-checkpoint",  required=True)
parser.add_argument("--mbert-checkpoint", required=True)
parser.add_argument("--xlmr-entries",     required=True)
parser.add_argument("--mbert-entries",    required=True)
parser.add_argument("--xlmr-zeroshot",    default=None)
parser.add_argument("--mbert-zeroshot",   default=None)
parser.add_argument("--zeroshot-sample",  type=int, default=800,
                    help="Max samples per zero-shot language pair (default: 800). Set 0 to disable.")
parser.add_argument("--max-entries", type=int, default=0,
                    help="Sample this many entries per language pair for quick testing (default: 0 = no limit).")
parser.add_argument("--results-dir",      default="results/qualitative")
parser.add_argument("--examples-per-type", type=int, default=50,
                    help="Number of examples to collect per category")
args = parser.parse_args()

os.makedirs(args.results_dir, exist_ok=True)

if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")
print(f"Device: {device}")


# ── Step 1: Augment entries with switch_types ─────────────────────────────────
def classify_switch_types(entry):
    """
    For every token position t:
      - Find j = next non-punct token after t
      - If any token in tokens[t+1 : j] is a sentence-ending punctuation → "inter"
      - Otherwise → "intra"
    Applies to all positions so false alarms can also be classified by context.
    """
    tokens   = entry["tokens"]
    lang_ids = entry["lang_ids"]
    n        = len(tokens)

    switch_types = [None] * n

    for t in range(n):
        if lang_ids[t] == "punct":
            continue
        j = t + 1
        while j < n and lang_ids[j] == "punct":
            j += 1
        is_inter = any(
            tokens[i].replace("▁", "").strip() in SENT_END
            for i in range(t + 1, j)
        )
        switch_types[t] = "inter" if is_inter else "intra"

    entry["switch_types"] = switch_types
    return entry


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

def load_and_augment(main_path, zeroshot_path=None, sample_per_pair=800):
    with open(main_path, "rb") as f:
        entries = pickle.load(f)
    if zeroshot_path:
        with open(zeroshot_path, "rb") as f:
            zs = pickle.load(f)
        if sample_per_pair > 0:
            zs = sample_zeroshot(zs, sample_per_pair)
        entries = entries + zs
    entries = [classify_switch_types(e) for e in entries]
    return entries


print("\nLoading and augmenting entries...")
xlmr_entries  = load_and_augment(args.xlmr_entries,  args.xlmr_zeroshot,  args.zeroshot_sample)
mbert_entries = load_and_augment(args.mbert_entries, args.mbert_zeroshot, args.zeroshot_sample)
def sample_per_pair(entries, n, seed=42):
    import random, collections
    rng = random.Random(seed)
    by_pair = collections.defaultdict(list)
    for e in entries:
        by_pair[e["language_pair"]].append(e)
    sampled = []
    for pair, items in sorted(by_pair.items()):
        rng.shuffle(items)
        sampled.extend(items[:n])
        print(f"  {pair}: {min(len(items), n)}/{len(items)} sampled")
    rng.shuffle(sampled)  # interleave all pairs so examples aren't dominated by one pair
    return sampled

if args.max_entries > 0:
    print(f"\n[--max-entries] sampling {args.max_entries} entries per language pair...")
    xlmr_entries  = sample_per_pair(xlmr_entries,  args.max_entries)
    mbert_entries = sample_per_pair(mbert_entries, args.max_entries)
print(f"XLM-R  entries: {len(xlmr_entries)}")
print(f"mBERT  entries: {len(mbert_entries)}")

# Print switch type distribution
inter_c = sum(1 for e in xlmr_entries for t in e["switch_types"] if t == "inter")
intra_c = sum(1 for e in xlmr_entries for t in e["switch_types"] if t == "intra")
total_c = inter_c + intra_c
print(f"\nSwitch type distribution (XLM-R entries):")
print(f"  Inter-sentential: {inter_c:5d}  ({100*inter_c/total_c:.1f}%)")
print(f"  Intra-sentential: {intra_c:5d}  ({100*intra_c/total_c:.1f}%)")


# ── Step 2: Inference (returns per-entry token predictions) ───────────────────
def build_windows(input_ids, pad_id):
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
    return windows


def run_inference_per_entry(entries, backbone_key, checkpoint_path):
    """
    Returns list of dicts, one per entry:
      {"sw_preds": [...], "dur_preds": [...]}
    Length of each list = len(entry["ysw"]) - 1  (same as windows count)
    """
    backbone_name = BACKBONE_NAMES[backbone_key]
    tokenizer = AutoTokenizer.from_pretrained(backbone_name)
    pad_id = tokenizer.pad_token_id or 0

    model = DualHeadCausalModel(backbone_name=backbone_name).to(device)
    model.load_state_dict(torch.load(checkpoint_path, map_location=device))
    model.eval()
    print(f"  Loaded: {checkpoint_path}")

    results = []
    with torch.no_grad():
        for entry in tqdm(entries, desc=f"  [{backbone_key}] inference"):
            input_ids = entry["input_ids"]
            windows   = build_windows(input_ids, pad_id)
            n         = len(windows)

            sw_preds, dur_preds = [], []
            for i in range(0, n, BATCH_SIZE):
                batch      = windows[i:i + BATCH_SIZE]
                ids_tensor = torch.tensor(batch, dtype=torch.long).to(device)
                attn_mask  = (ids_tensor != pad_id).long()
                sw_logits, dur_logits = model(ids_tensor, attn_mask)
                sw_preds.extend(sw_logits.argmax(dim=-1).cpu().tolist())
                dur_preds.extend(dur_logits.argmax(dim=-1).cpu().tolist())

            results.append({"sw_preds": sw_preds, "dur_preds": dur_preds, "n": n})
    return results


# ── Step 3: Token-level bucketing → F1 per switch type ────────────────────────
def compute_type_metrics(entries, infer_results, n_examples=3):
    """
    Buckets predictions at token level by switch_types.

    inter / intra buckets each contain ALL token positions (including ysw=0
    positions) so that false alarms are counted correctly for F1.

    Also collects concrete examples:
      - successful_inter/intra: ysw_true=1, ysw_pred=1
      - false_alarm_inter/intra: ysw_true=0, ysw_pred=1
      - missed_inter/intra: ysw_true=1, ysw_pred=0
    """
    inter = {"true": [], "pred": [], "dur_true": [], "dur_pred": []}
    intra = {"true": [], "pred": [], "dur_true": [], "dur_pred": []}

    examples = {
        "successful_inter": [], "successful_intra": [],
        "false_alarm_inter": [], "false_alarm_intra": [],
        "missed_inter":     [], "missed_intra":     [],
    }

    for entry, res in zip(entries, infer_results):
        tokens       = entry["tokens"]
        lang_ids     = entry["lang_ids"]
        ysw          = entry["ysw"]
        ydur         = entry["ydur"]
        switch_types = entry["switch_types"]
        pair         = entry.get("language_pair", "UNK")
        orig_text    = entry.get("original_text", "")
        n            = res["n"]
        sw_preds     = res["sw_preds"]
        dur_preds    = res["dur_preds"]

        for t in range(n):
            true_label = ysw[t]
            pred_label = sw_preds[t]
            sw_type    = switch_types[t]   # "inter", "intra", or None

            # ── Assign to inter bucket ──
            if sw_type == "inter":
                inter["true"].append(true_label)
                inter["pred"].append(pred_label)
                inter["dur_true"].append(ydur[t])
                inter["dur_pred"].append(dur_preds[t])
            elif sw_type == "intra":
                intra["true"].append(true_label)
                intra["pred"].append(pred_label)
                intra["dur_true"].append(ydur[t])
                intra["dur_pred"].append(dur_preds[t])
            else:
                # ysw_true=0: false alarms have no switch type, share to both
                inter["true"].append(0)
                inter["pred"].append(pred_label)
                inter["dur_true"].append(-1)
                inter["dur_pred"].append(dur_preds[t])
                intra["true"].append(0)
                intra["pred"].append(pred_label)
                intra["dur_true"].append(-1)
                intra["dur_pred"].append(dur_preds[t])

            # ── Collect qualitative examples ──
            ctx_start  = max(0, t - 4)
            ctx_end    = min(len(tokens), t + 6)
            t_idx      = t - ctx_start
            switch_tok = tokens[t]
            example = {
                "language_pair":  pair,
                "switch_type":    sw_type,
                "position":       t,
                "switch_token":   switch_tok,
                "context_tokens": tokens[ctx_start:ctx_end],
                "context_langs":  lang_ids[ctx_start:ctx_end],
                "ysw_true":       true_label,
                "ysw_pred":       pred_label,
                "ydur_true":      ydur[t],
            }
            if sw_type in ("inter", "intra"):
                tag = sw_type
                if true_label == 1 and pred_label == 1:
                    key = f"successful_{tag}"
                elif true_label == 0 and pred_label == 1:
                    key = f"false_alarm_{tag}"
                elif true_label == 1 and pred_label == 0:
                    key = f"missed_{tag}"
                else:
                    key = None
                if key and len(examples[key]) < n_examples:
                    examples[key].append(example)

    metrics = {
        "inter": {
            "anticipatory_f1":       anticipatory_f1(inter["true"], inter["pred"]),
            "anticipatory_precision": anticipatory_precision(inter["true"], inter["pred"]),
            "anticipatory_recall":    anticipatory_recall(inter["true"], inter["pred"]),
            "duration_accuracy":      duration_accuracy(inter["dur_true"], inter["dur_pred"]),
            "n_switch_points":        sum(inter["true"]),
        },
        "intra": {
            "anticipatory_f1":       anticipatory_f1(intra["true"], intra["pred"]),
            "anticipatory_precision": anticipatory_precision(intra["true"], intra["pred"]),
            "anticipatory_recall":    anticipatory_recall(intra["true"], intra["pred"]),
            "duration_accuracy":      duration_accuracy(intra["dur_true"], intra["dur_pred"]),
            "n_switch_points":        sum(intra["true"]),
        },
    }
    return metrics, examples


# ── Run for both models ────────────────────────────────────────────────────────
all_results = {}

for backbone_key, checkpoint, entries in [
    ("xlmr",  args.xlmr_checkpoint,  xlmr_entries),
    ("mbert", args.mbert_checkpoint, mbert_entries),
]:
    print(f"\n=== {backbone_key.upper()} ===")
    infer_results = run_inference_per_entry(entries, backbone_key, checkpoint)
    metrics, examples = compute_type_metrics(entries, infer_results, args.examples_per_type)
    all_results[backbone_key] = {"metrics": metrics, "examples": examples}


# ── Print results table ────────────────────────────────────────────────────────
print(f"\n{'='*70}")
print("MACRO-AVERAGE ACCURACY: Inter-sentential vs Intra-sentential")
print(f"{'='*70}")
print(f"{'Model':<8} {'Type':<8} {'F1':>6} {'Prec':>6} {'Rec':>6} {'DurAcc':>8} {'#Switches':>10}")
print("-" * 60)
for model_key in ["xlmr", "mbert"]:
    for sw_type in ["inter", "intra"]:
        m = all_results[model_key]["metrics"][sw_type]
        print(f"{model_key:<8} {sw_type:<8} "
              f"{m['anticipatory_f1']:>6.4f} "
              f"{m['anticipatory_precision']:>6.4f} "
              f"{m['anticipatory_recall']:>6.4f} "
              f"{m['duration_accuracy']:>8.4f} "
              f"{m['n_switch_points']:>10d}")
    print()


# ── Print qualitative examples ─────────────────────────────────────────────────
YDUR_DESC = {-1: "n/a", 0: "short (≤2 tok)", 1: "medium (3-6 tok)", 2: "long (>6 tok)"}

def format_example(ex):
    t        = ex["position"]
    tokens   = ex["context_tokens"]
    langs    = ex["context_langs"]
    t_idx    = min(t, 4)   # index of position-t token within the context window

    # Build token display: mark position t with >>...<<
    parts = []
    for i, (tok, lng) in enumerate(zip(tokens, langs)):
        label = f"{tok}[{lng}]"
        parts.append(f">>{label}<<" if i == t_idx else label)
    context_str = "  ".join(parts)

    ysw_true_desc = "switch occurs after this token" if ex["ysw_true"] == 1 else "no switch"
    ysw_pred_desc = "predicted switch" if ex["ysw_pred"] == 1 else "predicted no switch"
    ydur_desc     = YDUR_DESC.get(ex["ydur_true"], "?")

    return (
        f"  [{ex['language_pair']}]  switch_type={ex['switch_type']}  switch_token='{ex['switch_token']}'\n"
        f"  context : {context_str}\n"
        f"  ysw_true={ex['ysw_true']} ({ysw_true_desc})\n"
        f"  ysw_pred={ex['ysw_pred']} ({ysw_pred_desc})\n"
        f"  ydur_true={ex['ydur_true']} ({ydur_desc})\n"
    )


for model_key in ["xlmr", "mbert"]:
    print(f"\n{'='*70}")
    print(f"QUALITATIVE EXAMPLES — {model_key.upper()}")
    print(f"{'='*70}")
    exs = all_results[model_key]["examples"]

    for category, label in [
        ("successful_inter",  "Successful Predictions — Inter-sentential"),
        ("successful_intra",  "Successful Predictions — Intra-sentential"),
        ("false_alarm_inter", "False Alarms — Inter-sentential"),
        ("false_alarm_intra", "False Alarms — Intra-sentential"),
        ("missed_inter",      "Missed Switches — Inter-sentential"),
        ("missed_intra",      "Missed Switches — Intra-sentential"),
    ]:
        items = exs[category]
        print(f"\n--- {label} ({len(items)} examples) ---")
        for ex in items:
            print(format_example(ex))


# ── Save JSON ──────────────────────────────────────────────────────────────────
# Convert examples to JSON-serializable format
save_data = {}
for model_key in ["xlmr", "mbert"]:
    save_data[model_key] = {
        "metrics":  all_results[model_key]["metrics"],
        "examples": all_results[model_key]["examples"],
    }

out_path = os.path.join(args.results_dir, "qualitative_results.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(save_data, f, indent=2, ensure_ascii=False)
print(f"\nSaved to {out_path}")

# ── Save MD ────────────────────────────────────────────────────────────────────
md_lines = []

md_lines.append("# Qualitative Analysis Results\n")

md_lines.append("## Macro-Average Accuracy: Inter-sentential vs Intra-sentential\n")
md_lines.append("| Model | Type | F1 | Prec | Rec | DurAcc | #Switches |")
md_lines.append("|---|---|---|---|---|---|---|")
for model_key in ["xlmr", "mbert"]:
    for sw_type in ["inter", "intra"]:
        m = all_results[model_key]["metrics"][sw_type]
        md_lines.append(
            f"| {model_key} | {sw_type} "
            f"| {m['anticipatory_f1']:.4f} "
            f"| {m['anticipatory_precision']:.4f} "
            f"| {m['anticipatory_recall']:.4f} "
            f"| {m['duration_accuracy']:.4f} "
            f"| {m['n_switch_points']} |"
        )
md_lines.append("")

for model_key in ["xlmr", "mbert"]:
    md_lines.append(f"## Qualitative Examples — {model_key.upper()}\n")
    exs = all_results[model_key]["examples"]
    for category, label in [
        ("successful_inter",  "Successful Predictions — Inter-sentential"),
        ("successful_intra",  "Successful Predictions — Intra-sentential"),
        ("false_alarm_inter", "False Alarms — Inter-sentential"),
        ("false_alarm_intra", "False Alarms — Intra-sentential"),
        ("missed_inter",      "Missed Switches — Inter-sentential"),
        ("missed_intra",      "Missed Switches — Intra-sentential"),
    ]:
        items = exs[category]
        md_lines.append(f"### {label} ({len(items)} examples)\n")
        for ex in items:
            md_lines.append("```")
            md_lines.append(format_example(ex).strip())
            md_lines.append("```\n")

md_path = os.path.join(args.results_dir, "qualitative_results.md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))
print(f"Saved to {md_path}")
