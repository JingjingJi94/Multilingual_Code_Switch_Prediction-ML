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
    df = pd.read_pickle("df_preprocessed.pkl")
    print(f"Total rows: {len(df)}")
    print(f"Language pairs: {df['language_pair'].unique()}")

    # Step 1: Row-level shuffle with fixed seed (reproducible)
    df = df.sample(frac=1, random_state=RANDOM_SEED).reset_index(drop=True)

    # Step 2: Row-level train/test split (no sentence boundary leakage)
    split_idx = int(len(df) * TRAIN_RATIO)
    train_df = df.iloc[:split_idx]
    test_df  = df.iloc[split_idx:]
    print(f"Train rows: {len(train_df)}, Test rows: {len(test_df)}")

    # Step 3: Extract tokens from train rows and fit naive model
    print("\n=== Fitting Naive Baseline on Train Rows ===")
    train_lids, train_ysw = extract_samples(train_df)
    print(f"Train tokens: {len(train_lids)}")

    naive = NaiveSwitchPredictor(threshold=0.5)
    naive.fit(train_lids, train_ysw)

    zero = ZeroBaseline()

    # Step 4: Overall evaluation on held-out test rows
    print("\n=== Overall Results (held-out test rows) ===")
    test_lids, test_ysw = extract_samples(test_df)
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
    print("\n=== Per Language Pair Results (same held-out test rows) ===")
    print(f"{'Language Pair':<20} {'Model':<10} {'F1':>6} {'Precision':>10} {'Recall':>8}")
    print("-" * 60)

    for pair in sorted(df['language_pair'].unique()):
        pair_test_df = test_df[test_df['language_pair'] == pair]
        pair_lids, pair_ysw = extract_samples(pair_test_df)

        naive_r = naive.evaluate(pair_lids, pair_ysw)
        zero_r  = zero.evaluate(pair_lids, pair_ysw)

        print(f"{pair:<20} {'Naive':<10} {naive_r['anticipatory_f1']:>6.4f} "
              f"{naive_r['precision']:>10.4f} {naive_r['recall']:>8.4f}")
        print(f"{'':<20} {'Zero':<10} {zero_r['anticipatory_f1']:>6.4f} "
              f"{zero_r['precision']:>10.4f} {zero_r['recall']:>8.4f}")
        print()


if __name__ == "__main__":
    run()