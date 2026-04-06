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

def main():
    """
    Preprocess the SwitchLingua dataset using a selected tokenizer model.

    Usage:
        python preprocess.py --model xlmr   # xlm-roberta-base  → preprocessed_data_xlmr.pkl
        python preprocess.py --model mbert  # bert-base-multilingual-cased → preprocessed_data_mbert.pkl
        python preprocess.py                # defaults to xlmr
    """
    parser = argparse.ArgumentParser(
        description="Preprocess SwitchLingua dataset for code-switching prediction.",
        epilog=(
            "Examples:\n"
            "  python preprocess.py --model xlmr   # uses xlm-roberta-base  → preprocessed_data_xlmr.pkl\n"
            "  python preprocess.py --model mbert  # uses bert-base-multilingual-cased → preprocessed_data_mbert.pkl\n"
            "  python preprocess.py                # defaults to xlmr"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--model",
        choices=list(MODEL_CONFIGS.keys()),
        default="xlmr",
        help="Tokenizer model to use: 'xlmr' (xlm-roberta-base) or 'mbert' (bert-base-multilingual-cased). Default: xlmr",
    )
    args = parser.parse_args()

    model_key = args.model
    model_name = MODEL_CONFIGS[model_key]
    output_path = f"./data_preprocess/preprocessed_data_{model_key}.pkl"

    print(f"Model: {model_name}")
    print(f"Output: {output_path}")

    # Authenticate with Hugging Face
    login()

    # Load dataset
    print("\nLoading dataset from Hugging Face...")
    dataset = load_dataset("Shelton1013/SwitchLingua_text")
    df = dataset["train"].to_pandas()
    print(f"Dataset shape: {df.shape}")

    # Create language pair column and filter to chosen pairs
    df["language_pair"] = df["first_language"] + "-" + df["second_language"]
    chosen_pairs = [("Chinese", "English"), ("Hindi", "English"), ("Spanish", "English"), ("Arabic", "English")]
    df_filtered = df[
        df["language_pair"].isin([f"{l1}-{l2}" for l1, l2 in chosen_pairs])
    ].reset_index(drop=True)
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
    print(f"\nPreprocessed dataset saved to {output_path} ({len(preprocessed_data)} samples)")

if __name__ == "__main__":
    main()
