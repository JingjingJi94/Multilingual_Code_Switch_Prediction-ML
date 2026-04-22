#!/usr/bin/env bash
# Training script for mBERT (single-task: switch head only)
# Usage: bash scripts/train_mbert_singletask.sh [--debug]

set -euo pipefail

EXTRA_ARGS="$@"

RUN_DIR="train_log_singletask/mbert/lr1e-5"
echo "=========================================="
echo " [mbert train single-task] lr=1e-5"
echo " log-dir: ${RUN_DIR}"
echo "=========================================="
python3 training/train.py \
    --backbone mbert \
    --lr 1e-5 \
    --epochs 15 \
    --single-task \
    --log-dir "${RUN_DIR}" \
    ${EXTRA_ARGS}

echo "[mbert train single-task] Done. Logs saved under train_log_singletask/"
echo ""
echo "View all runs with:"
echo "  tensorboard --logdir train_log_singletask/"
