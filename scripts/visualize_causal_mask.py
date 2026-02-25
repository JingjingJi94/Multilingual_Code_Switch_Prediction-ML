"""
Generate causal mask visualizations for PPT.

Run from project root:
    python scripts/visualize_causal_mask.py

Outputs:
  - causal_mask_matrix.png     : raw mask matrix (white=allowed, blue=blocked)
  - attention_comparison.png   : attention weights before vs after causal mask
"""
import sys
sys.path.append(".")

from models.causal_mask_builder import CausalMaskBuilder

TOKENS = ["I", "went", "to", "mercado", "and", "left"]

if __name__ == "__main__":
    print("Generating causal mask visualizations...")

    CausalMaskBuilder.plot_mask_matrix(
        seq_len=6,
        tokens=TOKENS,
        save_path="causal_mask_matrix.png"
    )

    CausalMaskBuilder.plot_attention_comparison(
        seq_len=6,
        tokens=TOKENS,
        save_path="attention_comparison.png"
    )

    print("Done. Files saved:")
    print("  causal_mask_matrix.png")
    print("  attention_comparison.png")