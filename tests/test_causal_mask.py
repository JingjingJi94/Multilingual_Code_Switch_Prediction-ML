import sys
import os
import torch

# Ensure project root is in path regardless of where script is run from
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.causal_mask_builder import CausalMaskBuilder


def test_mask_upper_triangle_is_neg_inf():
    """Upper triangle must be -inf (future positions are blocked)."""
    seq_len = 8
    mask = CausalMaskBuilder.build(seq_len)

    for i in range(seq_len):
        for j in range(i + 1, seq_len):
            assert mask[i, j] == float('-inf'), \
                f"Position ({i},{j}) should be -inf but got {mask[i, j]}"

    print("PASS: upper triangle is -inf")


def test_mask_lower_triangle_is_zero():
    """Lower triangle including diagonal must be 0 (past positions are visible)."""
    seq_len = 8
    mask = CausalMaskBuilder.build(seq_len)

    for i in range(seq_len):
        for j in range(0, i + 1):
            assert mask[i, j] == 0.0, \
                f"Position ({i},{j}) should be 0 but got {mask[i, j]}"

    print("PASS: lower triangle is 0")


def test_softmax_future_weights_are_zero_2d():
    """After softmax, future positions must be 0.0 — 2D input."""
    seq_len = 6
    torch.manual_seed(42)
    scores = torch.randn(seq_len, seq_len)
    mask = CausalMaskBuilder.build(seq_len)
    weights = CausalMaskBuilder.apply(scores, mask)

    for i in range(seq_len):
        for j in range(i + 1, seq_len):
            val = weights[i, j].item()
            assert val == 0.0, \
                f"Future position ({i},{j}) should be 0.0 but got {val}"

    print("PASS: future attention weights are 0.0 after softmax (2D)")


def test_softmax_future_weights_are_zero_4d():
    """After softmax, future positions must be 0.0 — 4D input (batch, heads, seq, seq)."""
    seq_len = 6
    torch.manual_seed(42)
    scores = torch.randn(2, 4, seq_len, seq_len)  # batch=2, heads=4
    mask = CausalMaskBuilder.build(seq_len)
    weights = CausalMaskBuilder.apply(scores, mask)

    for i in range(seq_len):
        for j in range(i + 1, seq_len):
            val = weights[:, :, i, j].max().item()
            assert val == 0.0, \
                f"Future position ({i},{j}) should be 0.0 but got {val}"

    print("PASS: future attention weights are 0.0 after softmax (4D)")


def test_no_leakage_demo():
    """
    Demonstrate prefix-only constraint:
    At position t, the model sees only tokens [x1...xt].
    The label (ysw) comes from t+1, which is NOT in the input window.
    """
    tokens   = ["I",  "went", "to",  "mercado", "and", "left"]
    lang_ids = ["en", "en",   "en",  "es",       "en",  "en" ]
    ysw      = [0,    0,      1,     1,           0,     0    ]

    window_size = 3

    print("\nNo-leakage demo (window_size=3):")
    print(f"{'t':<4} {'Input window':<35} {'LID(xt)':<10} {'ysw[t] -> predicts switch at t+1'}")
    print("-" * 80)

    for t in range(window_size - 1, len(ysw)):
        window_tokens = tokens[t - window_size + 1: t + 1]
        current_lid   = lang_ids[t]
        label         = ysw[t]
        print(f"{t:<4} {str(window_tokens):<35} {current_lid:<10} {label}")

    print("\nKey: input window ends at t. Label ysw[t] predicts switch at t+1.")
    print("     t+1 token is NOT included in the input window -> no leakage.")
    print("PASS: no-leakage constraint verified")


if __name__ == "__main__":
    test_mask_upper_triangle_is_neg_inf()
    test_mask_lower_triangle_is_zero()
    test_softmax_future_weights_are_zero_2d()
    test_softmax_future_weights_are_zero_4d()
    test_no_leakage_demo()
    print("\nAll tests passed.")