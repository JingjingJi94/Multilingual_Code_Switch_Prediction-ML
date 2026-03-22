import os
import sys
sys.path.append(".")
from data.data_utils import load_dataset
import matplotlib.pyplot as plt

# This file is primarily for determining the appropriate window size of tokenized input.

bundle = load_dataset("./data_preprocess/preprocessed_data.pkl")

full_dataset = bundle.loader.dataset

# Get original sequence lengths
original_lengths = [len(entry['input_ids']) for entry in bundle.entries]

# Basic stats
print("Num sequences:", len(original_lengths))
print("Average length:", sum(original_lengths) / len(original_lengths))
print("Max length:", max(original_lengths))
print("Min length:", min(original_lengths))

# Create plot directory if it doesn't exist
plot_dir = "./plots"
os.makedirs(plot_dir, exist_ok=True)

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(original_lengths, bins=50, color='skyblue', edgecolor='black')
plt.title("Distribution of Original Sequence Lengths")
plt.xlabel("Sequence length (number of tokens)")
plt.ylabel("Count")
plt.grid(True, alpha=0.3)

# Save the figure
plot_path = os.path.join(plot_dir, "sequence_lengths_histogram.png")
plt.savefig(plot_path)
print(f"Plot saved to {plot_path}")
plt.close()