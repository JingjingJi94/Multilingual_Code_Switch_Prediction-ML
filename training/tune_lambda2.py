import os
import sys
sys.path.append(".")
import torch
from torch.utils.data import DataLoader, random_split
from data.data_utils import load_dataset
from models.dual_head_model import DualHeadCausalModel
from training.losses import MultiTaskLoss
import matplotlib.pyplot as plt
from tqdm import tqdm

# ---------------------------
# 1️⃣ Device
# ---------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ---------------------------
# 2️⃣ Load dataset
# ---------------------------
bundle = load_dataset("./data_preprocess/preprocessed_data.pkl")
full_dataset = bundle.loader.dataset

# Fix random seed for reproducibility
generator = torch.Generator().manual_seed(42)

subset_size = 50000
dataset, _ = random_split(full_dataset, [subset_size, len(full_dataset) - subset_size],
                           generator=generator)

val_frac = 0.1
val_size = int(len(dataset) * val_frac)   # 5k windows
train_size = len(dataset) - val_size       # 45k windows
train_dataset, val_dataset = random_split(dataset, [train_size, val_size],
                                           generator=generator)

bs=256
train_loader = DataLoader(train_dataset, batch_size=bs, shuffle=True)
val_loader   = DataLoader(val_dataset,   batch_size=bs)

# ---------------------------
# 3️⃣ Hyperparameters
# ---------------------------
lambda_sw      = 1.0
lambda2_values = [0.5, 1, 3, 5]
num_epochs     = 10
lr             = 1e-5

plot_dir = "./plots"
os.makedirs(plot_dir, exist_ok=True)

results = {}

# ---------------------------
# 4️⃣ Loop over λ2 values
# ---------------------------
for lambda_dur in lambda2_values:
    with open(f"lambda_tuning_results_{lambda_dur}.txt", "w") as log_file:
        print(f"\n=== Training with λ2={lambda_dur} ===")

        model     = DualHeadCausalModel(backbone_name="xlm-roberta-base").to(device)
        optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
        criterion = MultiTaskLoss()
        criterion.lambda_sw  = lambda_sw
        criterion.lambda_dur = lambda_dur

        train_L_sw_list, train_L_dur_list = [], []
        val_L_sw_list,   val_L_dur_list   = [], []

        for epoch in range(num_epochs):
            # ----- Training -----
            model.train()
            epoch_L_sw, epoch_L_dur = 0.0, 0.0

            for batch in tqdm(train_loader, desc=f"Training Epoch {epoch+1}"):
                input_ids, _, attention_mask, ysw, ydur = batch   # language_ids unused
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

            # ----- Validation -----
            model.eval()
            val_epoch_L_sw, val_epoch_L_dur = 0.0, 0.0

            with torch.no_grad():
                for batch in val_loader:
                    input_ids, _, attention_mask, ysw, ydur = batch   # language_ids unused
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
                f"Epoch {epoch+1}: "
                f"Train L_sw={train_L_sw_list[-1]:.4f}, L_dur={train_L_dur_list[-1]:.4f} | "
                f"Val L_sw={val_L_sw_list[-1]:.4f}, L_dur={val_L_dur_list[-1]:.4f}"
            )
            print(msg)
            log_file.write(msg + "\n")
            log_file.flush()

        # Store results
        results[lambda_dur] = {
            "train_L_sw":  train_L_sw_list,
            "train_L_dur": train_L_dur_list,
            "val_L_sw":    val_L_sw_list,
            "val_L_dur":   val_L_dur_list,
        }

        # Per-λ loss curve
        epochs_range = range(1, num_epochs + 1)
        plt.figure(figsize=(8, 5))
        plt.plot(epochs_range, train_L_sw_list,  label="Train Switch Loss")
        plt.plot(epochs_range, train_L_dur_list, label="Train Duration Loss")
        plt.plot(epochs_range, val_L_sw_list,  "--", label="Val Switch Loss")
        plt.plot(epochs_range, val_L_dur_list, "--", label="Val Duration Loss")
        plt.xlabel("Epoch")
        plt.ylabel("Loss")
        plt.title(f"Loss Curves for λ2={lambda_dur}")
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(plot_dir, f"loss_curve_lambda2_{lambda_dur}.png"))
        plt.close()

# ---------------------------
# 5️⃣ Summary comparison plot
# ---------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for lambda_dur, res in results.items():
    epochs_range = range(1, num_epochs + 1)
    axes[0].plot(epochs_range, res["val_L_sw"],  label=f"λ2={lambda_dur}")
    axes[1].plot(epochs_range, res["val_L_dur"], label=f"λ2={lambda_dur}")

axes[0].set_title("Val Switch Loss vs λ2")
axes[1].set_title("Val Duration Loss vs λ2")
for ax in axes:
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Loss")
    ax.legend()

plt.tight_layout()
plt.savefig(os.path.join(plot_dir, "lambda_comparison.png"))
plt.close()

print("\n✅ Hyperparameter search complete. Loss curves saved in './plots'.")