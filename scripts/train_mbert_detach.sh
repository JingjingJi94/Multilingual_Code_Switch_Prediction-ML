#!/usr/bin/env bash
# Training script for mBERT (ablation: detached duration loss)
# Usage: bash scripts/train_mbert_detach.sh [--debug]

set -euo pipefail

EXTRA_ARGS="$@"

RUNS=(
    "1e-5 0.1"
)

for RUN in "${RUNS[@]}"; do
    LR=$(echo "$RUN" | awk '{print $1}')
    LDUR=$(echo "$RUN" | awk '{print $2}')
    RUN_DIR="train_log_detach/mbert/lr${LR}_ldur${LDUR}_detach"
    echo "=========================================="
    echo " [mbert train detach] lr=${LR}  lambda-dur=${LDUR}"
    echo " log-dir: ${RUN_DIR}"
    echo "=========================================="
    python3 training/train.py \
        --backbone mbert \
        --lr "${LR}" \
        --lambda-dur "${LDUR}" \
        --detach-dur \
        --log-dir "${RUN_DIR}" \
        ${EXTRA_ARGS}
done

echo "[mbert train detach] Done. Logs saved under train_log/"
echo ""
echo "View all runs with:"
echo "  tensorboard --logdir train_log/"
