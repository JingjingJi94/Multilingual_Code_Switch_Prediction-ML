import torch
import sys
sys.path.append(".")
from models.dual_head_model import DualHeadCausalModel
from data.data_utils import load_dataset
from losses import MultiTaskLoss
import os

log_path = os.path.join(save_dir, "training_log.txt")
log_file = open(log_path, "w")
# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load dataset
bundle = load_dataset("./data_preprocess/preprocessed_data.pkl")
loader = bundle.loader

# List of backbones to compare
backbones = [
    ("xlmr", "xlm-roberta-base"),
    ("mbert", "bert-base-multilingual-cased")
]

# Training settings
num_epochs = 3
lr = 2e-5
save_dir = "./checkpoints"
os.makedirs(save_dir, exist_ok=True)
log_path = os.path.join(save_dir, "training_log.txt")
log_file = open(log_path, "w")

# Multi-task loss
criterion = MultiTaskLoss()

for model_name, backbone_name in backbones:
    print(f"\n=== Training {model_name} ({backbone_name}) ===")
    
    # Initialize model and optimizer, add two prediction heads
    model = DualHeadCausalModel(backbone_name=backbone_name).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)

    # Training loop
    for epoch in range(num_epochs):
        model.train()
        total_loss = 0.0
        total_Lsw = 0.0
        total_Ldur = 0.0
        num_batches = 0
        
        # Batch loop
        for batch in loader:
            input_ids, lang_ids, attention_mask, ysw, ydur = batch
            input_ids = input_ids.to(device)
            attention_mask = attention_mask.to(device)
            ysw = ysw.to(device)
            ydur = ydur.to(device)

            # Clears gradients from previous batch, ensuring each batch updates the model independently.
            optimizer.zero_grad() 
            
            # Forward pass, produces raw predictions for both heads
            switch_logits, duration_logits = model(input_ids, attention_mask)
            
            # Compute multi-task loss
            loss, L_sw, L_dur = criterion(switch_logits, duration_logits, ysw, ydur)
            #calculates gradients of all model parameters w.r.t loss.
            loss.backward()
            optimizer.step()
            
            # Accumulate losses for logging
            total_loss += loss.item()
            total_Lsw += L_sw.item()
            total_Ldur += L_dur.item()
            num_batches += 1

        avg_loss = total_loss / num_batches
        avg_Lsw = total_Lsw / num_batches
        avg_Ldur = total_Ldur / num_batches

        #save output to file
        msg = (
            f"Epoch {epoch+1}/{num_epochs} | "
            f"Total Loss: {avg_loss:.4f} | "
            f"Switch Loss: {avg_Lsw:.4f} | "
            f"Duration Loss: {avg_Ldur:.4f}"
        )
        print(msg)              # console
        log_file.write(msg + "\n")  # file
        log_file.close()
        print(f"Training log saved to {log_path}")

        # Save checkpoint
        ckpt_path = os.path.join(save_dir, f"{model_name}_epoch{epoch+1}.pt")
        torch.save(model.state_dict(), ckpt_path)
        print(f"Saved checkpoint: {ckpt_path}")