#!/usr/bin/env bash
# Training script for XLM-R (single-task: switch head only)
# Usage: bash scripts/train_xlmr_singletask.sh [--debug]

set -euo pipefail

EXTRA_ARGS="$@"

RUN_DIR="train_log_singletask/xlmr/lr1e-5"
echo "=========================================="
echo " [xlmr train single-task] lr=1e-5"
echo " log-dir: ${RUN_DIR}"
echo "=========================================="
python3 training/train.py \
    --backbone xlmr \
    --lr 1e-5 \
    --epochs 15 \
    --single-task \
    --log-dir "${RUN_DIR}" \
    ${EXTRA_ARGS}

echo "[xlmr train single-task] Done. Logs saved under train_log_singletask/"
echo ""
echo "View all runs with:"
echo "  tensorboard --logdir train_log_singletask/"
