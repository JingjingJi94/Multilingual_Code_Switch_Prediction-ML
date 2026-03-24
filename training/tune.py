import argparse
import os
import pickle
import sys
sys.path.append(".")

import torch
from torch.utils.data import DataLoader
from transformers import AutoTokenizer
import matplotlib.pyplot as plt

from data.data_utils import split_entries
from data.streaming_dataloader import SwitchLinguaStreamDataset
from models.dual_head_model import DualHeadCausalModel
from training.losses import MultiTaskLoss
from training.train import run_epoch, eval_epoch, _compute_metrics

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
parser.add_argument("--epochs", type=int, default=5,
    help="Number of training epochs per run (default: 10)")
parser.add_argument("--log-dir", default=".",
    help="Directory for log files and loss curve plots (default: .)")
parser.add_argument("--subset", type=int, default=50000,
    help="Max number of train windows to use (default: 50000)")
parser.add_argument("--subset-val", type=int, default=5000,
    help="Max number of val windows to use (default: 5000)")
parser.add_argument("--sample-rate", type=float, default=0.2,
    help="Fraction of training positions sampled per epoch (default: 0.2)")
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
# Device / AMP
# ---------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
use_amp = device.type == "cuda"

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
train_ds = SwitchLinguaStreamDataset(train_entries, tokenizer=tokenizer, sample_rate=args.sample_rate)
val_ds   = SwitchLinguaStreamDataset(val_entries,   tokenizer=tokenizer)

if args.subset < len(train_ds):
    indices = torch.randperm(len(train_ds), generator=torch.Generator().manual_seed(42))[:args.subset].tolist()
    train_ds = torch.utils.data.Subset(train_ds, indices)
    print(f"Subset train: {len(train_ds)} windows")

if args.subset_val < len(val_ds):
    indices = torch.randperm(len(val_ds), generator=torch.Generator().manual_seed(42))[:args.subset_val].tolist()
    val_ds = torch.utils.data.Subset(val_ds, indices)
    print(f"Subset val:   {len(val_ds)} windows")

train_loader = DataLoader(train_ds, batch_size=128, shuffle=True,  pin_memory=True)
val_loader   = DataLoader(val_ds,   batch_size=128, shuffle=False, pin_memory=True)
print(f"Train windows: {len(train_ds)} | Val windows: {len(val_ds)}")

# ---------------------------
# Sweep over (lr, lambda_dur)
# ---------------------------
for lr, lambda_dur in runs:
    run_dir   = os.path.join(args.log_dir, f"tune_lr{lr}_ldur{lambda_dur}")
    os.makedirs(run_dir, exist_ok=True)
    log_path  = os.path.join(run_dir, "log.txt")
    plot_path = os.path.join(run_dir, "plot.png")

    model     = DualHeadCausalModel(backbone_name=backbone_name).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
    criterion = MultiTaskLoss(lambda_sw=1.0, lambda_dur=lambda_dur)
    scaler    = torch.amp.GradScaler() if use_amp else None

    train_L_sw_list, train_L_dur_list = [], []
    val_L_sw_list,   val_L_dur_list   = [], []

    with open(log_path, "w") as log_file:
        def log_fn(msg: str, _f=log_file) -> None:
            print(msg)
            _f.write(msg + "\n")
            _f.flush()

        log_fn(f"\n=== lr={lr}  λ_dur={lambda_dur}  backbone={args.backbone} ===")

        for epoch in range(num_epochs):
            results = run_epoch(model, train_loader, optimizer, criterion, device, scaler, use_amp)
            m = _compute_metrics(results)

            train_L_sw_list.append(results["avg_Lsw"])
            train_L_dur_list.append(results["avg_Ldur"])

            log_fn(
                f"Epoch {epoch+1}/{num_epochs} [train] | "
                f"Loss {results['avg_loss']:.4f} (sw {results['avg_Lsw']:.4f}, dur {results['avg_Ldur']:.4f})\n"
                f"  Switch   — F1 {m['sw_f1']:.4f}  Acc {m['sw_acc']:.4f}\n"
                f"  Duration — F1 {m['dur_f1']:.4f}  Acc {m['dur_acc']:.4f}"
            )

            val_results = eval_epoch(model, val_loader, criterion, device)
            vm = _compute_metrics(val_results)

            val_L_sw_list.append(val_results["avg_Lsw"])
            val_L_dur_list.append(val_results["avg_Ldur"])

            log_fn(
                f"Epoch {epoch+1}/{num_epochs} [val]   | Loss {val_results['avg_loss']:.4f}\n"
                f"  Switch   — F1 {vm['sw_f1']:.4f}  Acc {vm['sw_acc']:.4f}\n"
                f"  Duration — F1 {vm['dur_f1']:.4f}  Acc {vm['dur_acc']:.4f}"
            )

            if hasattr(train_loader.dataset, "resample"):
                train_loader.dataset.resample()

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
    print(f"Saved: {run_dir}/")

print(f"\nAll runs done. Logs saved under {args.log_dir}")
