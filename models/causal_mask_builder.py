
import torch
import matplotlib.pyplot as plt


class CausalMaskBuilder:

    """
    Builds and validates causal (look-ahead) attention masks.

    Enforces prefix-only context at the model level:
    - Position t can only attend to positions 1..t
    - Upper triangle is set to -inf (blocked)
    - After softmax, blocked positions become 0.0
see
    Supports both 2D (seq_len, seq_len) and 4D (batch, heads, seq_len, seq_len)
    attention score tensors in apply().

    Note: Full integration into XLM-R attention layers is planned for Phase 2,
    via either (a) causal LM backbone or (b) attention score injection.
    """

    @staticmethod
    def build(seq_len: int, device: torch.device = torch.device("cpu")) -> torch.Tensor:
        """
        Returns a (seq_len, seq_len) causal mask.
        Upper triangle = -inf, lower triangle including diagonal = 0.
        """
        mask = torch.triu(
            torch.full((seq_len, seq_len), float('-inf')),
            diagonal=1
        ).to(device)
        return mask

    @staticmethod
    def apply(attention_scores: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
        """
        Add causal mask to attention scores, then apply softmax.

        Supports:
          - 2D scores: (seq_len, seq_len)
          - 4D scores: (batch, heads, seq_len, seq_len)

        mask is always (seq_len, seq_len) and will be broadcast automatically.
        """
        if attention_scores.dim() == 4:
            # Explicit broadcast: (seq_len, seq_len) -> (1, 1, seq_len, seq_len)
            mask = mask.unsqueeze(0).unsqueeze(0)
        elif attention_scores.dim() == 2:
            pass  # mask shape (seq_len, seq_len) matches directly
        else:
            raise ValueError(f"attention_scores must be 2D or 4D, got {attention_scores.dim()}D")

        return torch.softmax(attention_scores + mask, dim=-1)

    @staticmethod
    def plot_mask_matrix(seq_len: int = 6, tokens: list = None, save_path: str = "causal_mask_matrix.png"):
        """
        Visualize the raw causal mask matrix (before softmax).
        Green = 0 (allowed), Blue = -inf (blocked).
        """
        if tokens is None:
            tokens = [f"t{i+1}" for i in range(seq_len)]

        mask = CausalMaskBuilder.build(seq_len)
        # blocked (-inf) -> 1.0 (dark blue), allowed (0) -> 0.0 (white)
        display = torch.zeros_like(mask)
        display[mask == float('-inf')] = 1.0

        fig, ax = plt.subplots(figsize=(6, 5))
        ax.imshow(display.numpy(), cmap='Blues', vmin=0, vmax=1)

        ax.set_xticks(range(seq_len))
        ax.set_xticklabels(tokens, rotation=45, ha='right')
        ax.set_yticks(range(seq_len))
        ax.set_yticklabels(tokens)
        ax.set_xlabel("Key position (attends to)")
        ax.set_ylabel("Query position (current token)")
        ax.set_title("Causal Mask Matrix\n(white=0 allowed, blue=-inf blocked)")

        for i in range(seq_len):
            for j in range(seq_len):
                val = "0" if j <= i else "-inf"
                color = "black" if j <= i else "white"
                ax.text(j, i, val, ha='center', va='center', fontsize=9, color=color)

        plt.tight_layout()
        plt.savefig(save_path, dpi=150)
        plt.close()
        print(f"Causal mask matrix saved: {save_path}")

    @staticmethod
    def plot_attention_comparison(seq_len: int = 6, tokens: list = None, save_path: str = "attention_comparison.png"):
        """
        Compare attention weights with and without causal mask (after softmax).
        Uses 4D scores (1, 1, seq_len, seq_len) consistent with apply() interface.
        Visualizes head 0 of batch 0.
        """
        if tokens is None:
            tokens = [f"t{i+1}" for i in range(seq_len)]

        # Base: random scores to show bidirectional attention spreads everywhere
        # Add diagonal boost so self-attention is visually strongest
        torch.manual_seed(42)
        scores = torch.randn(1, 1, seq_len, seq_len) * 0.5  # smaller variance = more even distribution
        diagonal_boost = torch.eye(seq_len) * 0.8  # subtle boost, not overwhelming
        scores = scores + diagonal_boost.unsqueeze(0).unsqueeze(0)
        mask = CausalMaskBuilder.build(seq_len)

        bidirectional = torch.softmax(scores, dim=-1)[0, 0].detach().numpy()
        causal = CausalMaskBuilder.apply(scores, mask)[0, 0].detach().numpy()

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

        ax1.imshow(bidirectional, cmap='Oranges', vmin=0, vmax=1)
        ax1.set_title("Bidirectional Attention (No Mask)\nEach token attends to ALL positions")
        ax1.set_xticks(range(seq_len))
        ax1.set_xticklabels(tokens, rotation=45, ha='right')
        ax1.set_yticks(range(seq_len))
        ax1.set_yticklabels(tokens)
        ax1.set_xlabel("Attends to")
        ax1.set_ylabel("Query token")

        ax2.imshow(causal, cmap='Oranges', vmin=0, vmax=1)
        ax2.set_title("Causal Attention (With Mask)\nEach token attends to PAST only")
        ax2.set_xticks(range(seq_len))
        ax2.set_xticklabels(tokens, rotation=45, ha='right')
        ax2.set_yticks(range(seq_len))
        ax2.set_yticklabels(tokens)
        ax2.set_xlabel("Attends to")
        ax2.set_ylabel("Query token")

        plt.tight_layout()
        plt.savefig(save_path, dpi=150)
        plt.close()
        print(f"Attention comparison saved: {save_path}")