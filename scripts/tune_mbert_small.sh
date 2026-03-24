#!/usr/bin/env bash
# Hyperparameter sweep for mBERT small — all runs in one call
# Dataset is loaded once; all runs share the same subset.
# Usage: bash scripts/tune_mbert_small.sh [--epochs N] [--subset N] [--subset-val N]

set -euo pipefail

echo "=========================================="
echo " [mbert small] runs: 1e-5,0.1 1e-5,0.5 1e-5,1.0 1e-5,5.0"
echo "               2e-5,0.1 2e-5,0.5 2e-5,1.0 2e-5,3.0 2e-5,5.0"
echo "               5e-4,0.5 5e-4,1.0 5e-4,5.0 5e-4,10.0"
echo " log-dir: logs/tune_mbert_small"
echo "=========================================="

python3 training/tune.py \
    --backbone mbert \
    --runs "1e-5,0.1 1e-5,0.5 1e-5,1.0 1e-5,5.0 2e-5,0.1 2e-5,0.5 2e-5,1.0 2e-5,3.0 2e-5,5.0 5e-4,0.5 5e-4,1.0 5e-4,5.0 5e-4,10.0" \
    --log-dir "logs/tune_mbert_small" \
    "$@"

echo "[mbert small] Done. Logs saved under logs/tune_mbert_small/"
echo ""
echo "View all runs with:"
echo "  tensorboard --logdir logs/tune_mbert_small"
