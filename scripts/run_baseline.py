from collections import defaultdict
import pickle
import sys
import pandas as pd
sys.path.append(".")

from models.naive_baseline import NaiveSwitchPredictor, ZeroBaseline

RANDOM_SEED = 42
TRAIN_RATIO = 0.8


def extract_samples(df):
    """
    Extract all (lang_id, ysw) pairs from a dataframe of rows.
    Skips rows where preprocessed is None.
    """
    all_lids = []
    all_ysw = []
    for _, row in df.iterrows():
        p = row['preprocessed']
        if p is None:
            continue
        for lid, label in zip(p['lang_ids'], p['ysw']):
            all_lids.append(lid)
            all_ysw.append(label)
    return all_lids, all_ysw


def run():
    print("=== Loading Data ===")
    # Load the pickle list-of-dicts
    with open("./data_preprocess/preprocessed_data.pkl", "rb") as f:
        entries = pickle.load(f)

    print(f"Total samples: {len(entries)}")
    # Extract all language pairs
    language_pairs = set(e.get("language_pair", "UNK") for e in entries)
    print(f"Language pairs: {language_pairs}")

    # Step 1: Shuffle
    import random
    random.seed(RANDOM_SEED)
    entries = random.sample(entries, len(entries))

    # Step 2: Row-level train/test split (no sentence boundary leakage)
    split_idx = int(len(entries) * TRAIN_RATIO)
    train_entries = entries[:split_idx]
    test_entries  = entries[split_idx:]
    print(f"Train samples: {len(train_entries)}, Test samples: {len(test_entries)}")

    # Step 3: Extract tokens from train rows and fit naive model
    print("\n=== Fitting Naive Baseline on Train Samples ===")
    train_lids = []
    train_ysw = []
    for e in train_entries:
        train_lids.extend(e["lang_ids"])
        train_ysw.extend(e["ysw"])
    print(f"Train tokens: {len(train_lids)}")

    naive = NaiveSwitchPredictor(threshold=0.2)
    naive.fit(train_lids, train_ysw)

    zero = ZeroBaseline()

    # Step 4: Overall evaluation on held-out test rows
    print("\n=== Overall Results (held-out test samples) ===")
    test_lids = []
    test_ysw = []
    for e in test_entries:
        test_lids.extend(e["lang_ids"])
        test_ysw.extend(e["ysw"])

    print(f"Test tokens: {len(test_lids)}")
    print(f"Test switch rate: {sum(test_ysw) / len(test_ysw):.4f}")

    naive_result = naive.evaluate(test_lids, test_ysw)
    zero_result  = zero.evaluate(test_lids, test_ysw)

    print(f"[Naive Baseline] Anticipatory F1: {naive_result['anticipatory_f1']:.4f} "
          f"| Precision: {naive_result['precision']:.4f} "
          f"| Recall: {naive_result['recall']:.4f}")
    print(f"[Zero Baseline]  Anticipatory F1: {zero_result['anticipatory_f1']:.4f} "
          f"| Precision: {zero_result['precision']:.4f} "
          f"| Recall: {zero_result['recall']:.4f}")

    # Step 5: Per language pair evaluation on same held-out test rows
    # (universal naive baseline: trained on all pairs, tested per pair)
    print("\n=== Per Language Pair Results (same held-out test samples) ===")
    print(f"{'Language Pair':<20} {'Model':<10} {'F1':>6} {'Precision':>10} {'Recall':>8}")
    print("-" * 60)

    # Group test samples by language pair
    pair_to_samples = defaultdict(list)
    for e in test_entries:
        lp = e.get("language_pair", "UNK")
        pair_to_samples[lp].append(e)

    for pair in sorted(pair_to_samples.keys()):
        pair_entries = pair_to_samples[pair]
        pair_lids = []
        pair_ysw = []
        for e in pair_entries:
            pair_lids.extend(e["lang_ids"])
            pair_ysw.extend(e["ysw"])

        naive_r = naive.evaluate(pair_lids, pair_ysw)
        zero_r  = zero.evaluate(pair_lids, pair_ysw)

        print(f"{pair:<20} {'Naive':<10} {naive_r['anticipatory_f1']:>6.4f} "
              f"{naive_r['precision']:>10.4f} {naive_r['recall']:>8.4f}")
        print(f"{'':<20} {'Zero':<10} {zero_r['anticipatory_f1']:>6.4f} "
              f"{zero_r['precision']:>10.4f} {zero_r['recall']:>8.4f}")
        print()


if __name__ == "__main__":
    run()