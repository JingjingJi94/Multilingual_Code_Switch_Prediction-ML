import os
import sys
sys.path.append(".")
import torch
from torch.utils.data import DataLoader, Subset, random_split
from data.data_utils import load_dataset
from models.dual_head_model import DualHeadCausalModel
from training.losses import MultiTaskLoss
import matplotlib.pyplot as plt


# ---------------------------
# 1️⃣ Device
# ---------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ---------------------------
# 2️⃣ Load dataset
# ---------------------------
bundle = load_dataset("./data_preprocess/preprocessed_data.pkl")
full_dataset = bundle.loader.dataset  # assuming loader has dataset attribute

# Split into train / validation
subset_size = 50000
dataset, _ = random_split(full_dataset, [subset_size, len(full_dataset) - subset_size])
val_frac = 0.1
val_size = int(len(dataset) * val_frac) # 5k windows
train_size = len(dataset) - val_size # 45k windows
train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

train_loader = DataLoader(train_dataset, batch_size=8, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=8)

# ---------------------------
# 3️⃣ Hyperparameters
# ---------------------------
lambda_sw = 1.0
lambda2_values = [1, 5]  # candidate duration weights
num_epochs = 3
lr = 2e-5

# Folder to save plots
plot_dir = "./plots"
os.makedirs(plot_dir, exist_ok=True)

# Store results
results = {}

# ---------------------------
# 4️⃣ Loop over λ2 values
# ---------------------------
for lambda_dur in lambda2_values:
    print(f"\n=== Training with λ2={lambda_dur} ===")
    
    # Fresh model
    model = DualHeadCausalModel(backbone_name="xlm-roberta-base").to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
    criterion = MultiTaskLoss()
    criterion.lambda_sw = lambda_sw
    criterion.lambda_dur = lambda_dur
    
    # Track losses
    train_L_sw_list, train_L_dur_list = [], []
    val_L_sw_list, val_L_dur_list = [], []
    
    for epoch in range(num_epochs):
        # ----- Training -----
        model.train()
        epoch_L_sw, epoch_L_dur = 0, 0
        for batch in train_loader:
            input_ids, language_ids, attention_mask, ysw, ydur = batch
            input_ids = input_ids.to(device)
            attention_mask = attention_mask.to(device)
            ysw = ysw.to(device)
            ydur = ydur.to(device)
            
            optimizer.zero_grad()
            switch_logits, duration_logits = model(input_ids, attention_mask)
            loss, L_sw, L_dur = criterion(switch_logits, duration_logits, ysw, ydur)
            loss.backward()
            optimizer.step()
            
            epoch_L_sw += L_sw.item()
            epoch_L_dur += L_dur.item()
        
        train_L_sw_list.append(epoch_L_sw / len(train_loader))
        train_L_dur_list.append(epoch_L_dur / len(train_loader))
        
        # ----- Validation -----
        model.eval()
        val_epoch_L_sw, val_epoch_L_dur = 0, 0
        with torch.no_grad():
            for batch in val_loader:
                input_ids, language_ids, attention_mask, ysw, ydur = batch
                input_ids = input_ids.to(device)
                attention_mask = attention_mask.to(device)
                ysw = ysw.to(device)
                ydur = ydur.to(device)
                
                switch_logits, duration_logits = model(input_ids, attention_mask)
                loss, L_sw, L_dur = criterion(switch_logits, duration_logits, ysw, ydur)
                val_epoch_L_sw += L_sw.item()
                val_epoch_L_dur += L_dur.item()
        
        val_L_sw_list.append(val_epoch_L_sw / len(val_loader))
        val_L_dur_list.append(val_epoch_L_dur / len(val_loader))

        #save result to log file
        log_file = open("lambda_tuning_results.txt", "w")
        msg = (
            f"Epoch {epoch+1}: "
            f"Train L_sw={train_L_sw_list[-1]:.4f}, L_dur={train_L_dur_list[-1]:.4f} | "
            f"Val L_sw={val_L_sw_list[-1]:.4f}, L_dur={val_L_dur_list[-1]:.4f}"
        )

        print(msg)
        log_file.write(msg + "\n")
        log_file.close()

    # Store results
    results[lambda_dur] = {
        "train_L_sw": train_L_sw_list,
        "train_L_dur": train_L_dur_list,
        "val_L_sw": val_L_sw_list,
        "val_L_dur": val_L_dur_list
    }

    # Plot and save figure
    epochs = range(1, num_epochs+1)
    plt.figure(figsize=(8,5))
    plt.plot(epochs, train_L_sw_list, label="Train Switch Loss")
    plt.plot(epochs, train_L_dur_list, label="Train Duration Loss")
    plt.plot(epochs, val_L_sw_list, '--', label="Val Switch Loss")
    plt.plot(epochs, val_L_dur_list, '--', label="Val Duration Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title(f"Loss Curves for λ2={lambda_dur}")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(plot_dir, f"loss_curve_lambda2_{lambda_dur}.png"))
    plt.close()

print("\n✅ Hyperparameter search complete. Loss curves saved in './plots'.")