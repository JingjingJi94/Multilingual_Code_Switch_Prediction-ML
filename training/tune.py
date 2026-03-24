import argparse
import os
import pickle
import sys
sys.path.append(".")

import torch
from torch.utils.data import DataLoader
from transformers import AutoTokenizer
import matplotlib.pyplot as plt
from tqdm import tqdm

from data.data_utils import split_entries
from data.streaming_dataloader import SwitchLinguaStreamDataset
from models.dual_head_model import DualHeadCausalModel
from training.losses import MultiTaskLoss

# ---------------------------
# CLI arguments
# ---------------------------
parser = argparse.ArgumentParser(
    description="Hyperparameter tuning over (lr, lambda_dur) pairs. Dataset is loaded once.",
    epilog=(
        "Examples:\n"
        "  python3 training/tune.py --backbone xlmr --runs '1e-5,0.1 1e-5,0.5 2e-5,1.0'\n"
        "  python3 training/tune.py --backbone mbert --runs '1e-5,0.5' --epochs 5 --subset 30000"
    ),
    formatter_class=argparse.RawDescriptionHelpFormatter,
)
parser.add_argument("--runs", type=str, required=True,
    help="Space-separated lr,lambda_dur pairs e.g. '1e-5,0.1 2e-5,0.5'")
parser.add_argument("--backbone", choices=["xlmr", "mbert"], default="xlmr",
    help="Backbone model (default: xlmr)")
parser.add_argument("--epochs", type=int, default=10,
    help="Number of training epochs per run (default: 10)")
parser.add_argument("--log-dir", default=".",
    help="Directory for log files and loss curve plots (default: .)")
parser.add_argument("--subset", type=int, default=50000,
    help="Max number of train windows to use (default: 50000)")
parser.add_argument("--subset-val", type=int, default=5000,
    help="Max number of val windows to use (default: 5000)")
args = parser.parse_args()

runs = [(float(p.split(",")[0]), float(p.split(",")[1])) for p in args.runs.split()]

BACKBONE_NAMES = {
    "xlmr": "xlm-roberta-base",
    "mbert": "bert-base-multilingual-cased",
}
backbone_name = BACKBONE_NAMES[args.backbone]
num_epochs = args.epochs
os.makedirs(args.log_dir, exist_ok=True)

print(f"Backbone : {backbone_name}")
print(f"Epochs   : {num_epochs}")
print(f"Runs     : {runs}")
print(f"Log dir  : {args.log_dir}")

# ---------------------------
# Device
# ---------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ---------------------------
# Load & split dataset (once)
# ---------------------------
data_file = f"./data_preprocess/preprocessed_data_{args.backbone}.pkl"
print(f"\nLoading {data_file} ...")
with open(data_file, "rb") as f:
    all_entries = pickle.load(f)

train_entries, val_entries, _ = split_entries(all_entries)
print(f"Split: {len(train_entries)} train / {len(val_entries)} val sequences")

tokenizer = AutoTokenizer.from_pretrained(backbone_name)
train_ds = SwitchLinguaStreamDataset(train_entries, tokenizer=tokenizer)
val_ds   = SwitchLinguaStreamDataset(val_entries,   tokenizer=tokenizer)

if args.subset < len(train_ds):
    indices = torch.randperm(len(train_ds), generator=torch.Generator().manual_seed(42))[:args.subset].tolist()
    train_ds = torch.utils.data.Subset(train_ds, indices)
    print(f"Subset train: {len(train_ds)} windows")

if args.subset_val < len(val_ds):
    indices = torch.randperm(len(val_ds), generator=torch.Generator().manual_seed(42))[:args.subset_val].tolist()
    val_ds = torch.utils.data.Subset(val_ds, indices)
    print(f"Subset val:   {len(val_ds)} windows")

train_loader = DataLoader(train_ds, batch_size=128, shuffle=True)
val_loader   = DataLoader(val_ds,   batch_size=128, shuffle=False)
print(f"Train windows: {len(train_ds)} | Val windows: {len(val_ds)}")

# ---------------------------
# Sweep over (lr, lambda_dur)
# ---------------------------
for lr, lambda_dur in runs:
    log_path  = os.path.join(args.log_dir, f"tune_lr{lr}_ldur{lambda_dur}.txt")
    plot_path = os.path.join(args.log_dir, f"loss_curve_lr{lr}_ldur{lambda_dur}.png")

    model     = DualHeadCausalModel(backbone_name=backbone_name).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
    criterion = MultiTaskLoss(lambda_sw=1.0, lambda_dur=lambda_dur)

    train_L_sw_list, train_L_dur_list = [], []
    val_L_sw_list,   val_L_dur_list   = [], []

    with open(log_path, "w") as log_file:
        print(f"\n=== lr={lr}  λ_dur={lambda_dur}  backbone={args.backbone} ===")
        log_file.write(f"lr={lr}  lambda_dur={lambda_dur}  backbone={args.backbone}\n\n")

        for epoch in range(num_epochs):
            # Training
            model.train()
            epoch_L_sw, epoch_L_dur = 0.0, 0.0

            for batch in tqdm(train_loader, desc=f"Epoch {epoch+1}/{num_epochs} [train]"):
                input_ids, _, attention_mask, ysw, ydur = batch
                input_ids      = input_ids.to(device)
                attention_mask = attention_mask.to(device)
                ysw            = ysw.to(device)
                ydur           = ydur.to(device)

                optimizer.zero_grad()
                switch_logits, duration_logits = model(input_ids, attention_mask)
                loss, L_sw, L_dur = criterion(switch_logits, duration_logits, ysw, ydur)
                loss.backward()
                optimizer.step()

                epoch_L_sw  += L_sw.item()
                epoch_L_dur += L_dur.item()

            train_L_sw_list.append(epoch_L_sw  / len(train_loader))
            train_L_dur_list.append(epoch_L_dur / len(train_loader))

            # Validation
            model.eval()
            val_epoch_L_sw, val_epoch_L_dur = 0.0, 0.0

            with torch.no_grad():
                for batch in tqdm(val_loader, desc=f"Epoch {epoch+1}/{num_epochs} [val]", leave=False):
                    input_ids, _, attention_mask, ysw, ydur = batch
                    input_ids      = input_ids.to(device)
                    attention_mask = attention_mask.to(device)
                    ysw            = ysw.to(device)
                    ydur           = ydur.to(device)

                    switch_logits, duration_logits = model(input_ids, attention_mask)
                    _, L_sw, L_dur = criterion(switch_logits, duration_logits, ysw, ydur)
                    val_epoch_L_sw  += L_sw.item()
                    val_epoch_L_dur += L_dur.item()

            val_L_sw_list.append(val_epoch_L_sw  / len(val_loader))
            val_L_dur_list.append(val_epoch_L_dur / len(val_loader))

            msg = (
                f"Epoch {epoch+1}/{num_epochs}: "
                f"Train L_sw={train_L_sw_list[-1]:.4f}, L_dur={train_L_dur_list[-1]:.4f} | "
                f"Val L_sw={val_L_sw_list[-1]:.4f}, L_dur={val_L_dur_list[-1]:.4f}"
            )
            print(msg)
            log_file.write(msg + "\n")
            log_file.flush()

    # Loss curve plot
    epochs_range = range(1, num_epochs + 1)
    plt.figure(figsize=(8, 5))
    plt.plot(epochs_range, train_L_sw_list,  label="Train Switch Loss")
    plt.plot(epochs_range, train_L_dur_list, label="Train Duration Loss")
    plt.plot(epochs_range, val_L_sw_list,  "--", label="Val Switch Loss")
    plt.plot(epochs_range, val_L_dur_list, "--", label="Val Duration Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title(f"Loss Curves  lr={lr}  λ_dur={lambda_dur}  backbone={args.backbone}")
    plt.legend()
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close()
    print(f"Saved: {log_path} | {plot_path}")

print(f"\nAll runs done. Logs saved under {args.log_dir}")
