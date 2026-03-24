#!/usr/bin/env bash
# Hyperparameter sweep for XLM-R small — part 2 of 2 (4 runs)
# Run in parallel with tune_xlmr_small.sh
# Dataset is loaded once; all runs share the same subset.
# Usage: bash scripts/tune_xlmr_small_part2.sh [--epochs N] [--subset N] [--subset-val N]

set -euo pipefail

echo "=========================================="
echo " [xlmr small part2] runs: 1e-5,1.0  1e-5,5.0  2e-5,1.0  2e-5,0.5"
echo " log-dir: logs/tune_xlmr_small"
echo "=========================================="

python3 training/tune.py \
    --backbone xlmr \
    --runs "1e-5,1.0 1e-5,5.0 2e-5,1.0 2e-5,0.5" \
    --log-dir "logs/tune_xlmr_small" \
    "$@"

echo "[xlmr small part2] Done. Logs saved under logs/tune_xlmr_small/"
echo ""
echo "View all runs with:"
echo "  tensorboard --logdir logs/tune_xlmr_small"
