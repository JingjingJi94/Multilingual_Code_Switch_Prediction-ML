"""
Streaming Simulation Demo
=========================
Processes input text word-by-word, printing the next-token switch probability
and anticipated duration after each token using a trained DualHeadCausalModel.

Usage:
    python streaming_demo.py --model_path checkpoints/model.pt \
                             --language_pair French-English \
                             --backbone xlmr

    python streaming_demo.py --model_path checkpoints/model.pt \
                             --language_pair Spanish-English \
                             --backbone mbert \
                             --text "El cielo is very blue today"

Arguments:
    --model_path      Path to the saved model checkpoint (.pt file)
    --language_pair   Language pair of the input text, e.g. French-English
    --backbone        Tokenizer/backbone to use: xlmr or mbert (default: xlmr)
    --text            Text to process (optional — prompts interactively if omitted)
    --window_size     Number of tokens in each sliding window (default: 64)
"""

import argparse
import torch
import torch.nn.functional as F
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'data_preprocess'))
from transformers import AutoTokenizer
from dual_head_model import DualHeadCausalModel
from preprocess_util import tokenize_with_lang_mapping

# ── Constants ────────────────────────────────────────────────────────────────

BACKBONE_CONFIGS = {
    "xlmr":  "xlm-roberta-base",
    "mbert": "bert-base-multilingual-cased",
}

DURATION_LABELS = {
    0: "Short  (1-2 tokens)",
    1: "Medium (3-6 tokens)",
    2: "Long   (7+ tokens)",
}

# ANSI colours for terminal output
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
CYAN   = "\033[96m"
RESET  = "\033[0m"
BOLD   = "\033[1m"


# ── Model loading ─────────────────────────────────────────────────────────────

def load_model(model_path, backbone_name, device):
    """Load DualHeadCausalModel from a checkpoint file."""
    model = DualHeadCausalModel(backbone_name=backbone_name)
    checkpoint = torch.load(model_path, map_location=device)

    # Support both raw state_dict and wrapped checkpoint dicts
    state_dict = checkpoint.get("model_state_dict", checkpoint)
    model.load_state_dict(state_dict)
    model.to(device)
    model.eval()
    return model


# ── Streaming simulation ──────────────────────────────────────────────────────

def stream_text(text, language_pair, model, tokenizer, window_size, device):
    """
    Process a bilingual prefix and predict the next-token switch probability
    and anticipated duration at the final token position.

    Pipeline:
      1. Tokenize input text and assign per-token language IDs
      2. Convert tokens to input IDs
      3. Find the last non-punctuation token as the prediction point
      4. Build a sliding window of up to window_size tokens ending there
      5. Run the window through the model backbone → dual-head predictions
      6. Apply softmax to switch logits → P(switch=1)
         Apply argmax to duration logits → duration bin
    """

    # ── Step 1: Tokenization + language detection ─────────────────────────────
    print(f"\n{BOLD}{'─' * 80}{RESET}")
    print(f"{BOLD}  Step 1 — Tokenization & Language Detection{RESET}")
    print(f"{'─' * 80}")
    print(f"  Input text   : {text}")
    print(f"  Language pair: {language_pair}")

    tokens, lang_ids = tokenize_with_lang_mapping(text, tokenizer, language_pair)

    print(f"  Total tokens : {len(tokens)}")
    print(f"\n  {'TOKEN':<20} {'LANG':<8} {'INPUT ID'}")
    print(f"  {'─'*20} {'─'*8} {'─'*10}")

    # ── Step 2: Token → input ID conversion ──────────────────────────────────
    input_ids_full = []
    for tok, lang in zip(tokens, lang_ids):
        id_ = tokenizer.convert_tokens_to_ids(tok)
        if id_ is None:
            id_ = tokenizer.unk_token_id
        input_ids_full.append(id_)
        print(f"  {tok:<20} {lang:<8} {id_}")

    n = len(tokens)
    if n == 0:
        print("No tokens found in input text.")
        return

    # ── Step 3: Find last non-punctuation token ───────────────────────────────
    print(f"\n{BOLD}{'─' * 80}{RESET}")
    print(f"{BOLD}  Step 2 — Identify Prediction Point{RESET}")
    print(f"{'─' * 80}")

    last_idx = n - 1
    while last_idx > 0 and lang_ids[last_idx] == "punct":
        last_idx -= 1

    last_token = tokens[last_idx]
    last_lang  = lang_ids[last_idx]

    if last_idx < n - 1:
        skipped = tokens[last_idx + 1:]
        print(f"  Last token is punctuation — stepping back.")
        print(f"  Skipped     : {skipped}")

    print(f"  Predict from: {last_token!r}  (lang={last_lang}, index={last_idx})")
    print(f"  This is the token whose hidden state h_t drives both predictions.")

    # ── Step 4: Build sliding window ─────────────────────────────────────────
    print(f"\n{BOLD}{'─' * 80}{RESET}")
    print(f"{BOLD}  Step 3 — Sliding Window Construction{RESET}")
    print(f"{'─' * 80}")

    start      = max(0, last_idx + 1 - window_size)
    window_ids = input_ids_full[start : last_idx + 1]
    window_tok = tokens[start : last_idx + 1]

    print(f"  Window size (max)  : {window_size} tokens")
    print(f"  Actual window len  : {len(window_ids)} tokens  (indices {start}–{last_idx})")
    print(f"  Window tokens      : {' '.join(window_tok)}")
    print(f"  Window input IDs   : {window_ids}")

    # ── Step 5: Model forward pass ────────────────────────────────────────────
    print(f"\n{BOLD}{'─' * 80}{RESET}")
    print(f"{BOLD}  Step 4 — Model Forward Pass{RESET}")
    print(f"{'─' * 80}")
    print(f"  Passing window through {model.encoder.config._name_or_path}...")
    print(f"  input_ids shape    : (1, {len(window_ids)})")
    print(f"  attention_mask     : all ones  (no padding)")
    print(f"  backbone outputs   : last_hidden_state  shape (1, {len(window_ids)}, {model.encoder.config.hidden_size})")
    print(f"  prediction token   : h_t = hidden_states[:, -1, :]  → shape (1, {model.encoder.config.hidden_size})")
    print(f"  switch_head        : Linear({model.encoder.config.hidden_size}, 2)  → switch logits")
    print(f"  duration_head      : Linear({model.encoder.config.hidden_size}, 3)  → duration logits")

    with torch.no_grad():
        ids_tensor  = torch.tensor([window_ids], dtype=torch.long).to(device)
        mask_tensor = torch.ones_like(ids_tensor).to(device)
        switch_logits, duration_logits = model(ids_tensor, mask_tensor)

    # ── Step 6: Decode predictions ────────────────────────────────────────────
    print(f"\n{BOLD}{'─' * 80}{RESET}")
    print(f"{BOLD}  Step 5 — Decoding Predictions{RESET}")
    print(f"{'─' * 80}")

    sw_probs = F.softmax(switch_logits, dim=-1)[0]
    print(f"  Switch logits      : [{switch_logits[0,0].item():.4f}, {switch_logits[0,1].item():.4f}]")
    print(f"  Switch probs       : [P(no switch)={sw_probs[0].item():.4f},  P(switch)={sw_probs[1].item():.4f}]")

    dur_probs = F.softmax(duration_logits, dim=-1)[0]
    print(f"  Duration logits    : [{duration_logits[0,0].item():.4f}, {duration_logits[0,1].item():.4f}, {duration_logits[0,2].item():.4f}]")
    print(f"  Duration probs     : [Short={dur_probs[0].item():.4f},  Medium={dur_probs[1].item():.4f},  Long={dur_probs[2].item():.4f}]")

    switch_prob    = sw_probs[1].item()
    duration_class = torch.argmax(duration_logits, dim=-1).item()
    duration_label = DURATION_LABELS[duration_class]

    prob_pad = f"{switch_prob:.3f}"
    if switch_prob >= 0.7:
        prob_str = f"{RED}{prob_pad}{RESET}"
        flag     = f"{RED}⚠ HIGH SWITCH{RESET}"
    elif switch_prob >= 0.4:
        prob_str = f"{YELLOW}{prob_pad}{RESET}"
        flag     = f"{YELLOW}~ possible switch{RESET}"
    elif switch_prob >= 0.2:
        prob_str = f"{GREEN}{prob_pad}{RESET}"
        flag     = f"{GREEN}✓ likely same language{RESET}"
    else:
        prob_str = f"{GREEN}{prob_pad}{RESET}"
        flag     = f"{GREEN}✓ no switch{RESET}"

    dur_str = f"{duration_label} (low confidence)" if switch_prob < 0.4 else duration_label

    display_token = last_token.lstrip('▁')

    # ── Final prediction output ───────────────────────────────────────────────
    print(f"\n{BOLD}{'─' * 80}{RESET}")
    print(f"{BOLD}  Prediction Result  |  {language_pair}{RESET}")
    print(f"{'─' * 80}")
    print(f"  {'TOKEN':<20} {'LANG':<6} | {'NEXT-TOKEN SWITCH PROB':<24} | {'ANTICIPATED DURATION':<22} | {'FLAG'}")
    print(f"{'─' * 80}")
    print(f"  {display_token:<20} {last_lang:<6} | {prob_str}{'':>{24 - len(prob_pad)}}  | {dur_str:<22} | {flag}")
    print(f"{BOLD}{'─' * 80}{RESET}\n")


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Streaming simulation of next-token switch prediction.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python streaming_demo.py --model_path checkpoints/model.pt "
            "--language_pair French-English\n"
            "  python streaming_demo.py --model_path checkpoints/model.pt "
            "--language_pair Spanish-English --backbone mbert "
            "--text \"El cielo is very blue\""
        ),
    )
    parser.add_argument("--dummy", action="store_true", help="Use randomly initialized model for pipeline testing")

    parser.add_argument(
    "--model_path",
    default=None,
    help="Path to saved model checkpoint (.pt file). Not required when --dummy is used.",
)
    parser.add_argument(
        "--language_pair",
        required=True,
        choices=[
            "French-English", "Spanish-English",
            "Chinese-English", "Hindi-English",
            "Arabic-English", "Korean-English",
        ],
        help="Language pair of the input text",
    )

    

    parser.add_argument(
        "--backbone",
        choices=list(BACKBONE_CONFIGS.keys()),
        default="xlmr",
        help="Backbone tokenizer to use: xlmr or mbert (default: xlmr)",
    )
    parser.add_argument(
        "--text",
        default=None,
        help="Text to process. If omitted, prompts interactively.",
    )
    parser.add_argument(
        "--window_size",
        type=int,
        default=64,
        help="Sliding window size in tokens (default: 64)",
    )
    args = parser.parse_args()

    if not args.dummy and not args.model_path:
        parser.error("--model_path is required unless --dummy is passed")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    # Load tokenizer and model
    backbone_name = BACKBONE_CONFIGS[args.backbone]
    print(f"Loading tokenizer: {backbone_name}")
    tokenizer = AutoTokenizer.from_pretrained(backbone_name)

    if args.dummy:
        # creates a DualHeadCausalModel with randomly initialized switch and duration heads
        # (but pretrained backbone weights from HuggingFace), 
        # moves it to the correct device (CPU or GPU), and sets it to evaluation mode.
        model = DualHeadCausalModel(backbone_name=backbone_name).to(device)
        model.eval()
    else:
        print(f"Loading model from: {args.model_path}")
        model = load_model(args.model_path, backbone_name, device)


    # Get input text
    if args.text:
        stream_text(
            text=args.text,
            language_pair=args.language_pair,
            model=model,
            tokenizer=tokenizer,
            window_size=args.window_size,
            device=device,
        )
        return

    print(f"\nEnter {args.language_pair} text to process. Type 'exit' or press Ctrl+C to quit.\n")
    while True:
        try:
            text = input("> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break

        if not text:
            continue
        if text.lower() in ("exit", "quit"):
            print("Exiting.")
            break

        stream_text(
            text=text,
            language_pair=args.language_pair,
            model=model,
            tokenizer=tokenizer,
            window_size=args.window_size,
            device=device,
        )


if __name__ == "__main__":
    main()
