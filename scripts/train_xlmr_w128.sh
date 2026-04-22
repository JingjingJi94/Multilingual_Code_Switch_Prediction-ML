#!/usr/bin/env bash
# Training script for XLM-R with window_size=128, lr=1e-5, lambda-dur=0.1
# Usage: bash scripts/train_xlmr_w128.sh [--debug]

set -euo pipefail

EXTRA_ARGS="$@"

RUNS=(
    "1e-5 0.1"
)

for RUN in "${RUNS[@]}"; do
    LR=$(echo "$RUN" | awk '{print $1}')
    LDUR=$(echo "$RUN" | awk '{print $2}')
    RUN_DIR="train_log_w128/xlmr/w128_lr${LR}_ldur${LDUR}"
    echo "=========================================="
    echo " [xlmr train] window=128  lr=${LR}  lambda-dur=${LDUR}"
    echo " log-dir: ${RUN_DIR}"
    echo "=========================================="
    python3 training/train.py \
        --backbone xlmr \
        --window-size 128 \
        --lr "${LR}" \
        --lambda-dur "${LDUR}" \
        --log-dir "${RUN_DIR}" \
        ${EXTRA_ARGS}
done

echo "[xlmr train] Done. Logs saved under train_log_w128/"
echo ""
echo "View all runs with:"
echo "  tensorboard --logdir train_log_w128/"
