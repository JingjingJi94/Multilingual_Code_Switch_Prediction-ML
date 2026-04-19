#!/usr/bin/env bash
# Training script for mBERT
# Usage: bash scripts/train_mbert.sh [--debug]

set -euo pipefail

EXTRA_ARGS="$@"

RUNS=(
    "1e-5 1.0"
)

for RUN in "${RUNS[@]}"; do
    LR=$(echo "$RUN" | awk '{print $1}')
    LDUR=$(echo "$RUN" | awk '{print $2}')
    RUN_DIR="train_log_new/mbert/lr${LR}_ldur${LDUR}"
    echo "=========================================="
    echo " [mbert train] lr=${LR}  lambda-dur=${LDUR}"
    echo " log-dir: ${RUN_DIR}"
    echo "=========================================="
    python3 training/train.py \
        --backbone mbert \
        --lr "${LR}" \
        --lambda-dur "${LDUR}" \
        --log-dir "${RUN_DIR}" \
        ${EXTRA_ARGS}
done

echo "[mbert train] Done. Logs saved under train_log/"
echo ""
echo "View all runs with:"
echo "  tensorboard --logdir train_log/"
