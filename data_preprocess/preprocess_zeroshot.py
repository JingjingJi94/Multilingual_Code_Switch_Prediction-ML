import argparse
import pickle
import pandas as pd
from preprocess_util import preprocess_and_label
from transformers import AutoTokenizer
from huggingface_hub import login
from datasets import load_dataset

MODEL_CONFIGS = {
    "xlmr": "xlm-roberta-base",
    "mbert": "bert-base-multilingual-cased",
}

# Zero-shot language pairs — unseen during training, used only for testing
ZEROSHOT_PAIRS = [("Korean", "English"), ("French", "English")]


def main():
    """
    Preprocess the SwitchLingua dataset for zero-shot evaluation language pairs
    (Korean-English, French-English) using a selected tokenizer model.

    Usage:
        python ./data_preprocess/preprocess_zeroshot.py --model xlmr   # → preprocessed_zeroshot_xlmr.pkl
        python ./data_preprocess/preprocess_zeroshot.py --model mbert  # → preprocessed_zeroshot_mbert.pkl
        python ./data_preprocess/preprocess_zeroshot.py                # defaults to xlmr
    """
    parser = argparse.ArgumentParser(
        description="Preprocess zero-shot (unseen) language pairs for code-switching evaluation.",
        epilog=(
            "Examples:\n"
            "  python ./data_preprocess/preprocess_zeroshot.py --model xlmr   # xlm-roberta-base  → preprocessed_zeroshot_xlmr.pkl\n"
            "  python ./data_preprocess/preprocess_zeroshot.py --model mbert  # bert-base-multilingual-cased → preprocessed_zeroshot_mbert.pkl\n"
            "  python ./data_preprocess/preprocess_zeroshot.py                # defaults to xlmr"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--model",
        choices=list(MODEL_CONFIGS.keys()),
        default="xlmr",
        help=(
            "Tokenizer model to use: 'xlmr' (xlm-roberta-base) or "
            "'mbert' (bert-base-multilingual-cased). Default: xlmr"
        ),
    )
    args = parser.parse_args()

    model_key = args.model
    model_name = MODEL_CONFIGS[model_key]
    output_path = f"./data_preprocess/preprocessed_zeroshot_{model_key}.pkl"

    print(f"Model:  {model_name}")
    print(f"Output: {output_path}")
    print(f"Zero-shot pairs: {[f'{l1}-{l2}' for l1, l2 in ZEROSHOT_PAIRS]}")

    # Authenticate with Hugging Face
    login()

    # Load dataset
    print("\nLoading dataset from Hugging Face...")
    dataset = load_dataset("Shelton1013/SwitchLingua_text")
    df = dataset["train"].to_pandas()
    print(f"Full dataset shape: {df.shape}")

    # Build language_pair column and filter to zero-shot pairs only
    df["language_pair"] = df["first_language"] + "-" + df["second_language"]
    pair_strings = [f"{l1}-{l2}" for l1, l2 in ZEROSHOT_PAIRS]
    df_filtered = df[df["language_pair"].isin(pair_strings)].reset_index(drop=True)

    print(f"Filtered dataset shape: {df_filtered.shape}")
    print("Language pair counts:")
    print(df_filtered["language_pair"].value_counts())

    # Load tokenizer
    print(f"\nLoading tokenizer: {model_name}")
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Preprocess
    print("\nStarting preprocessing...")
    preprocessed_data = preprocess_and_label(df_filtered, tokenizer)

    # Validate: check for samples with >2 languages
    print("\nChecking sequences for >2 languages...")
    bad_count = 0
    for i, sample in enumerate(preprocessed_data):
        langs = set(sample["lang_ids"]) - {"punct"}
        if len(langs) > 2:
            bad_count += 1
            print(f"  Sample {i} has >2 languages: {langs}")
            print(f"  Language pair: {sample['language_pair']}")
    print(f"Total problematic sequences: {bad_count}")

    # Save
    with open(output_path, "wb") as f:
        pickle.dump(preprocessed_data, f)
    print(
        f"\nZero-shot preprocessed dataset saved to {output_path} "
        f"({len(preprocessed_data)} samples)"
    )

    # Per-pair summary
    pair_counts = {}
    for s in preprocessed_data:
        pair_counts[s["language_pair"]] = pair_counts.get(s["language_pair"], 0) + 1
    print("\nSamples per language pair:")
    for pair, count in pair_counts.items():
        print(f"  {pair}: {count}")


if __name__ == "__main__":
    main()
