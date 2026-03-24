import argparse
import os
import pickle
import sys
from typing import Callable, Optional

import numpy as np
import torch
from sklearn.metrics import (
    accuracy_score,
    f1_score,
)
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from transformers import AutoTokenizer
from tqdm import tqdm

sys.path.append(".")
from data.data_utils import load_dataset, split_entries
from data.streaming_dataloader import SwitchLinguaStreamDataset
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

    all_sw_preds, all_sw_labels = [], []
    all_dur_preds, all_dur_labels = [], []

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

        sw_logits_f = switch_logits.detach().float()
        dur_logits_f = duration_logits.detach().float()

        all_sw_preds.extend(sw_logits_f.argmax(dim=-1).cpu().numpy())
        all_sw_labels.extend(ysw.cpu().numpy())

        all_dur_preds.extend(dur_logits_f.argmax(dim=-1).cpu().numpy())
        all_dur_labels.extend(ydur.cpu().numpy())

    return {
        "avg_loss": total_loss / num_batches,
        "avg_Lsw": total_Lsw / num_batches,
        "avg_Ldur": total_Ldur / num_batches,
        "sw_preds": np.array(all_sw_preds),
        "sw_labels": np.array(all_sw_labels),
        "dur_preds": np.array(all_dur_preds),
        "dur_labels": np.array(all_dur_labels),
    }


def eval_epoch(
    model: torch.nn.Module,
    loader: torch.utils.data.DataLoader,
    criterion: MultiTaskLoss,
    device: torch.device,
) -> dict:
    """Run one evaluation epoch (no gradient updates). Returns same dict shape as run_epoch."""
    model.eval()

    total_loss = 0.0
    total_Lsw = 0.0
    total_Ldur = 0.0
    num_batches = 0

    all_sw_preds, all_sw_labels = [], []
    all_dur_preds, all_dur_labels = [], []

    with torch.no_grad():
        for batch in tqdm(loader, desc="  val", leave=False):
            input_ids, _, attention_mask, ysw, ydur = batch
            input_ids = input_ids.to(device)
            attention_mask = attention_mask.to(device)
            ysw = ysw.to(device)
            ydur = ydur.to(device)

            switch_logits, duration_logits = model(input_ids, attention_mask)
            loss, L_sw, L_dur = criterion(switch_logits, duration_logits, ysw, ydur)

            total_loss += loss.item()
            total_Lsw += L_sw.item()
            total_Ldur += L_dur.item()
            num_batches += 1

            sw_logits_f = switch_logits.float()
            dur_logits_f = duration_logits.float()

            all_sw_preds.extend(sw_logits_f.argmax(dim=-1).cpu().numpy())
            all_sw_labels.extend(ysw.cpu().numpy())

            all_dur_preds.extend(dur_logits_f.argmax(dim=-1).cpu().numpy())
            all_dur_labels.extend(ydur.cpu().numpy())

    return {
        "avg_loss": total_loss / num_batches,
        "avg_Lsw": total_Lsw / num_batches,
        "avg_Ldur": total_Ldur / num_batches,
        "sw_preds": np.array(all_sw_preds),
        "sw_labels": np.array(all_sw_labels),
        "dur_preds": np.array(all_dur_preds),
        "dur_labels": np.array(all_dur_labels),
    }


def _compute_metrics(results: dict) -> dict:
    """Compute classification metrics from a results dict."""
    sw_f1 = f1_score(results["sw_labels"], results["sw_preds"], average="macro", zero_division=0)
    sw_acc = accuracy_score(results["sw_labels"], results["sw_preds"])

    dur_valid = results["dur_labels"] != -1
    dur_labels_v = results["dur_labels"][dur_valid]
    dur_preds_v = results["dur_preds"][dur_valid]

    dur_f1 = f1_score(dur_labels_v, dur_preds_v, average="macro", zero_division=0)
    dur_acc = accuracy_score(dur_labels_v, dur_preds_v)

    return dict(
        sw_f1=sw_f1, sw_acc=sw_acc,
        dur_f1=dur_f1, dur_acc=dur_acc,
    )


def train(
    model: torch.nn.Module,
    loader: torch.utils.data.DataLoader,
    val_loader: torch.utils.data.DataLoader,
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
    """Full training loop over num_epochs. Logs train + val metrics and saves checkpoints."""
    best_val_sw_f1 = -1.0
    best_val_dur_acc = -1.0
    best_sw_f1_state: Optional[dict] = None
    best_dur_acc_state: Optional[dict] = None
    best_sw_f1_ckpt_path = os.path.join(save_dir, f"{model_name}_best_sw_f1.pt")
    best_dur_acc_ckpt_path = os.path.join(save_dir, f"{model_name}_best_dur_acc.pt")

    epoch_bar = tqdm(range(num_epochs), desc=f"[{model_name}] epochs")
    for epoch in epoch_bar:
        results = run_epoch(model, loader, optimizer, criterion, device, scaler, use_amp)
        m = _compute_metrics(results)

        avg_loss = results["avg_loss"]
        avg_Lsw = results["avg_Lsw"]
        avg_Ldur = results["avg_Ldur"]

        epoch_bar.set_postfix(loss=f"{avg_loss:.4f}", sw_f1=f"{m['sw_f1']:.4f}", dur_f1=f"{m['dur_f1']:.4f}")

        global_step = epoch + 1

        writer.add_scalar("Train/Loss_total", avg_loss, global_step)
        writer.add_scalar("Train/Loss_switch", avg_Lsw, global_step)
        writer.add_scalar("Train/Loss_duration", avg_Ldur, global_step)
        writer.add_scalar("Train/Switch_F1", m["sw_f1"], global_step)
        writer.add_scalar("Train/Switch_Accuracy", m["sw_acc"], global_step)
        writer.add_scalar("Train/Duration_F1", m["dur_f1"], global_step)
        writer.add_scalar("Train/Duration_Accuracy", m["dur_acc"], global_step)

        log_fn(
            f"Epoch {epoch+1}/{num_epochs} [train] | "
            f"Loss {avg_loss:.4f} (sw {avg_Lsw:.4f}, dur {avg_Ldur:.4f})\n"
            f"  Switch   — F1 {m['sw_f1']:.4f}  Acc {m['sw_acc']:.4f}\n"
            f"  Duration — F1 {m['dur_f1']:.4f}  Acc {m['dur_acc']:.4f}"
        )

        # Validation
        val_results = eval_epoch(model, val_loader, criterion, device)
        vm = _compute_metrics(val_results)
        val_loss = val_results["avg_loss"]

        writer.add_scalar("Val/Loss_total", val_loss, global_step)
        writer.add_scalar("Val/Switch_F1", vm["sw_f1"], global_step)
        writer.add_scalar("Val/Switch_Accuracy", vm["sw_acc"], global_step)
        writer.add_scalar("Val/Duration_F1", vm["dur_f1"], global_step)
        writer.add_scalar("Val/Duration_Accuracy", vm["dur_acc"], global_step)

        log_fn(
            f"Epoch {epoch+1}/{num_epochs} [val]   | Loss {val_loss:.4f}\n"
            f"  Switch   — F1 {vm['sw_f1']:.4f}  Acc {vm['sw_acc']:.4f}\n"
            f"  Duration — F1 {vm['dur_f1']:.4f}  Acc {vm['dur_acc']:.4f}"
        )

        if vm["sw_f1"] > best_val_sw_f1:
            best_val_sw_f1 = vm["sw_f1"]
            best_sw_f1_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
            log_fn(f"  [best sw_f1] Val Switch F1 {best_val_sw_f1:.4f} → updated in-memory checkpoint")

        if vm["dur_acc"] > best_val_dur_acc:
            best_val_dur_acc = vm["dur_acc"]
            best_dur_acc_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
            log_fn(f"  [best dur_acc] Val Duration Acc {best_val_dur_acc:.4f} → updated in-memory checkpoint")

        if hasattr(loader.dataset, "resample"):
            loader.dataset.resample()

    if best_sw_f1_state is not None:
        torch.save(best_sw_f1_state, best_sw_f1_ckpt_path)
        log_fn(f"Best checkpoint (val sw_f1={best_val_sw_f1:.4f}) saved: {best_sw_f1_ckpt_path}")

    if best_dur_acc_state is not None:
        torch.save(best_dur_acc_state, best_dur_acc_ckpt_path)
        log_fn(f"Best checkpoint (val dur_acc={best_val_dur_acc:.4f}) saved: {best_dur_acc_ckpt_path}")


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
    parser.add_argument("--sample-rate", type=float, default=0.2,
        help="Fraction of training positions sampled per epoch (default: 0.2)")
    args = parser.parse_args()
    log_dir = args.log_dir
    os.makedirs(log_dir, exist_ok=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    use_amp = device.type == "cuda"

    all_backbones = [
        ("xlmr", "xlm-roberta-base"),
        ("mbert", "bert-base-multilingual-cased"),
    ]
    backbones = all_backbones if args.backbone == "both" else [b for b in all_backbones if b[0] == args.backbone]

    num_epochs = args.epochs if args.epochs is not None else (2 if args.debug else 5)
    lr = args.lr
    save_dir = os.path.join(log_dir, "checkpoints")
    os.makedirs(save_dir, exist_ok=True)

    for model_name, backbone_name in backbones:
        data_file = f"./data_preprocess/preprocessed_data_{model_name}.pkl"

        # Load and split at sequence level (prevents window leakage across splits)
        with open(data_file, "rb") as f:
            all_entries = pickle.load(f)
        train_entries, val_entries, test_entries = split_entries(all_entries)
        print(f"[{model_name}] Split: {len(train_entries)} train / {len(val_entries)} val / {len(test_entries)} test sequences")

        # Save test split for later evaluation (never used during training)
        test_split_path = os.path.join(save_dir, f"{model_name}_test_entries.pkl")
        with open(test_split_path, "wb") as f:
            pickle.dump(test_entries, f)
        print(f"[{model_name}] Test split saved to {test_split_path}")

        tokenizer = AutoTokenizer.from_pretrained(backbone_name)

        if args.debug:
            # Subsample train entries (1%) for quick debugging
            n_sub = max(1, len(train_entries) // 100)
            train_entries = train_entries[:n_sub]
            val_entries = val_entries[:max(1, len(val_entries) // 100)]
            print(f"[debug] Using {len(train_entries)} train / {len(val_entries)} val sequences (1%)")

        train_ds = SwitchLinguaStreamDataset(train_entries, tokenizer=tokenizer, sample_rate=args.sample_rate)
        val_ds = SwitchLinguaStreamDataset(val_entries, tokenizer=tokenizer)
        train_loader = DataLoader(train_ds, batch_size=128, shuffle=True, pin_memory=False)
        val_loader = DataLoader(val_ds, batch_size=128, shuffle=False, pin_memory=False)
        print(f"[{model_name}] Train windows: {len(train_ds)} | Val windows: {len(val_ds)}")

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
                loader=train_loader,
                val_loader=val_loader,
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
