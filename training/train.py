import argparse
import os
import sys
from typing import Callable, Optional

import numpy as np
import torch
import torch.nn.functional as F
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    balanced_accuracy_score,
    f1_score,
)
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm

sys.path.append(".")
from data.data_utils import load_dataset
from models.dual_head_model import DualHeadCausalModel
from training.losses import MultiTaskLoss


def run_epoch(
    model: torch.nn.Module,
    loader: torch.utils.data.DataLoader,
    optimizer: torch.optim.Optimizer,
    criterion: MultiTaskLoss,
    device: torch.device,
    scaler: Optional["torch.amp.GradScaler"],
    use_amp: bool,
) -> dict:
    """Run one training epoch. Returns a dict of averaged losses and collected arrays."""
    model.train()

    total_loss = 0.0
    total_Lsw = 0.0
    total_Ldur = 0.0
    num_batches = 0

    all_sw_preds, all_sw_labels, all_sw_probs = [], [], []
    all_dur_preds, all_dur_labels, all_dur_probs = [], [], []

    for batch in tqdm(loader, desc="  batches", leave=False):
        input_ids, _, attention_mask, ysw, ydur = batch
        input_ids = input_ids.to(device)
        attention_mask = attention_mask.to(device)
        ysw = ysw.to(device)
        ydur = ydur.to(device)

        optimizer.zero_grad()

        if use_amp:
            with torch.amp.autocast(device_type="cuda"):
                switch_logits, duration_logits = model(input_ids, attention_mask)
                loss, L_sw, L_dur = criterion(switch_logits, duration_logits, ysw, ydur)
            scaler.scale(loss).backward()
            scaler.step(optimizer)
            scaler.update()
        else:
            switch_logits, duration_logits = model(input_ids, attention_mask)
            loss, L_sw, L_dur = criterion(switch_logits, duration_logits, ysw, ydur)
            loss.backward()
            optimizer.step()

        total_loss += loss.item()
        total_Lsw += L_sw.item()
        total_Ldur += L_dur.item()
        num_batches += 1

        # .float() before softmax to avoid float16 metric noise under AMP
        sw_logits_f = switch_logits.detach().float()
        dur_logits_f = duration_logits.detach().float()

        sw_probs = F.softmax(sw_logits_f, dim=-1)
        dur_probs = F.softmax(dur_logits_f, dim=-1)

        all_sw_preds.extend(sw_logits_f.argmax(dim=-1).cpu().numpy())
        all_sw_labels.extend(ysw.cpu().numpy())
        all_sw_probs.extend(sw_probs[:, 1].cpu().numpy())

        all_dur_preds.extend(dur_logits_f.argmax(dim=-1).cpu().numpy())
        all_dur_labels.extend(ydur.cpu().numpy())
        all_dur_probs.extend(dur_probs.cpu().numpy())

    return {
        "avg_loss": total_loss / num_batches,
        "avg_Lsw": total_Lsw / num_batches,
        "avg_Ldur": total_Ldur / num_batches,
        "sw_preds": np.array(all_sw_preds),
        "sw_labels": np.array(all_sw_labels),
        "sw_probs": np.array(all_sw_probs),
        "dur_preds": np.array(all_dur_preds),
        "dur_labels": np.array(all_dur_labels),
        "dur_probs": np.array(all_dur_probs),
    }


def train(
    model: torch.nn.Module,
    loader: torch.utils.data.DataLoader,
    optimizer: torch.optim.Optimizer,
    criterion: MultiTaskLoss,
    num_epochs: int,
    device: torch.device,
    writer: SummaryWriter,
    model_name: str,
    save_dir: str,
    log_fn: Callable[[str], None],
    use_amp: bool = True,
    scaler: Optional["torch.amp.GradScaler"] = None,
) -> None:
    """Full training loop over num_epochs. Logs metrics and saves checkpoints."""
    epoch_bar = tqdm(range(num_epochs), desc=f"[{model_name}] epochs")
    for epoch in epoch_bar:
        results = run_epoch(model, loader, optimizer, criterion, device, scaler, use_amp)

        avg_loss = results["avg_loss"]
        avg_Lsw = results["avg_Lsw"]
        avg_Ldur = results["avg_Ldur"]

        sw_f1 = f1_score(results["sw_labels"], results["sw_preds"], average="macro", zero_division=0)
        sw_acc = accuracy_score(results["sw_labels"], results["sw_preds"])
        sw_bal_acc = balanced_accuracy_score(results["sw_labels"], results["sw_preds"])
        sw_auprc = average_precision_score(results["sw_labels"], results["sw_probs"])

        dur_valid = results["dur_labels"] != -1
        dur_labels_v = results["dur_labels"][dur_valid]
        dur_preds_v = results["dur_preds"][dur_valid]
        dur_probs_v = results["dur_probs"][dur_valid]  # shape (N_valid, 3)

        dur_f1 = f1_score(dur_labels_v, dur_preds_v, average="macro", zero_division=0)
        dur_acc = accuracy_score(dur_labels_v, dur_preds_v)
        dur_bal_acc = balanced_accuracy_score(dur_labels_v, dur_preds_v)
        dur_auprc = average_precision_score(dur_labels_v, dur_probs_v, average="macro")

        epoch_bar.set_postfix(loss=f"{avg_loss:.4f}", sw_f1=f"{sw_f1:.4f}", dur_f1=f"{dur_f1:.4f}")

        global_step = epoch + 1

        writer.add_scalar("Loss/total", avg_loss, global_step)
        writer.add_scalar("Loss/switch", avg_Lsw, global_step)
        writer.add_scalar("Loss/duration", avg_Ldur, global_step)

        writer.add_scalar("Switch/F1", sw_f1, global_step)
        writer.add_scalar("Switch/Accuracy", sw_acc, global_step)
        writer.add_scalar("Switch/BalAcc", sw_bal_acc, global_step)
        writer.add_scalar("Switch/AUPRC", sw_auprc, global_step)

        writer.add_scalar("Duration/F1", dur_f1, global_step)
        writer.add_scalar("Duration/Accuracy", dur_acc, global_step)
        writer.add_scalar("Duration/BalAcc", dur_bal_acc, global_step)
        writer.add_scalar("Duration/AUPRC", dur_auprc, global_step)

        log_fn(
            f"Epoch {epoch+1}/{num_epochs} | "
            f"Loss {avg_loss:.4f} (sw {avg_Lsw:.4f}, dur {avg_Ldur:.4f})\n"
            f"  Switch   — F1 {sw_f1:.4f}  Acc {sw_acc:.4f}  "
            f"BalAcc {sw_bal_acc:.4f}  AUPRC {sw_auprc:.4f}\n"
            f"  Duration — F1 {dur_f1:.4f}  Acc {dur_acc:.4f}  "
            f"BalAcc {dur_bal_acc:.4f}  AUPRC {dur_auprc:.4f}"
        )

        ckpt_path = os.path.join(save_dir, f"{model_name}_epoch{epoch+1}.pt")
        torch.save(model.state_dict(), ckpt_path)
        log_fn(f"Saved checkpoint: {ckpt_path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--log-dir", default=".", help="Directory for training result log files")
    parser.add_argument(
        "--backbone",
        choices=["xlmr", "mbert", "both"],
        default="both",
        help="Which backbone to train: xlmr, mbert, or both (default: both)",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Subsample 1%% of training data for quick debugging",
    )
    parser.add_argument("--epochs", type=int, default=None,
        help="Number of training epochs (default: 2 in debug mode, 5 otherwise)")
    parser.add_argument("--lr", type=float, default=1e-5,
        help="AdamW learning rate (default: 1e-5)")
    parser.add_argument("--lambda-sw", type=float, default=1.0,
        help="Loss weight for switch head (default: 1.0)")
    parser.add_argument("--lambda-dur", type=float, default=0.5,
        help="Loss weight for duration head (default: 0.5)")
    args = parser.parse_args()
    log_dir = args.log_dir
    os.makedirs(log_dir, exist_ok=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    use_amp = device.type == "cuda"

    bundle = load_dataset("./data_preprocess/preprocessed_data.pkl", batch_size=256)

    if args.debug:
        n_total = len(bundle.dataset)
        n_sub = max(1, n_total // 100)
        indices = torch.randperm(n_total)[:n_sub].tolist()
        sub_ds = torch.utils.data.Subset(bundle.dataset, indices)
        debug_loader = torch.utils.data.DataLoader(
            sub_ds, batch_size=256, shuffle=True, pin_memory=False
        )
        bundle = bundle.__class__(
            entries=bundle.entries,
            tokenizer=bundle.tokenizer,
            dataset=sub_ds,
            loader=debug_loader,
        )
        print(f"[debug] Using {n_sub}/{n_total} samples (1%)")

    all_backbones = [
        ("xlmr", "xlm-roberta-base"),
        ("mbert", "bert-base-multilingual-cased"),
    ]
    backbones = all_backbones if args.backbone == "both" else [b for b in all_backbones if b[0] == args.backbone]

    num_epochs = args.epochs if args.epochs is not None else (2 if args.debug else 5)
    lr = args.lr
    save_dir = "./checkpoints"
    os.makedirs(save_dir, exist_ok=True)

    for model_name, backbone_name in backbones:
        with open(os.path.join(log_dir, f"training_results_{model_name}.txt"), "w") as log_file:
            def log_fn(msg: str, _f=log_file) -> None:
                print(msg)
                _f.write(msg + "\n")
                _f.flush()

            log_fn(f"\n=== Training {model_name} ({backbone_name}) ===")
            writer = SummaryWriter(log_dir=os.path.join(log_dir, "tensorboard", model_name))

            criterion = MultiTaskLoss(lambda_sw=args.lambda_sw, lambda_dur=args.lambda_dur)

            model = DualHeadCausalModel(backbone_name=backbone_name).to(device)

            # torch.compile: must come after .to(device) and before AdamW
            # if hasattr(torch, "compile"):
            #     try:
            #         model = torch.compile(model)
            #         log_fn("[info] torch.compile enabled")
            #     except Exception as e:
            #         log_fn(f"[warn] torch.compile skipped: {e}")

            optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
            scaler = torch.amp.GradScaler() if use_amp else None

            train(
                model=model,
                loader=bundle.loader,
                optimizer=optimizer,
                criterion=criterion,
                num_epochs=num_epochs,
                device=device,
                writer=writer,
                model_name=model_name,
                save_dir=save_dir,
                log_fn=log_fn,
                use_amp=use_amp,
                scaler=scaler,
            )

            writer.close()


# Usage examples:
#   Run both backbones with default settings:
#     python3 training/train.py
#
#   Run a single backbone:
#     python3 training/train.py --backbone xlmr
#     python3 training/train.py --backbone mbert
#
#   Save logs to a custom directory (created if absent):
#     python3 training/train.py --log-dir ./logs/run1
#
#   Combine options:
#     python3 training/train.py --backbone xlmr --log-dir ./logs/xlmr_run1
#
#   Debug mode (1% data subsample, 2 epochs by default):
#     python3 training/train.py --debug
#     python3 training/train.py --debug --backbone xlmr
#     python3 training/train.py --debug --backbone xlmr --log-dir ./logs/debug
#
#   Override hyperparameters:
#     python3 training/train.py --epochs 10 --lr 2e-5
#     python3 training/train.py --lambda-sw 1.0 --lambda-dur 0.3
#     python3 training/train.py --debug --backbone xlmr --epochs 1 --lr 2e-5 --lambda-sw 1.0 --lambda-dur 0.3
if __name__ == "__main__":
    main()
