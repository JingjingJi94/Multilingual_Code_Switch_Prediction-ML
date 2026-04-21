#!/usr/bin/env bash
# Training script for mBERT (ablation: sqrt-weighted switch CE)
# Usage: bash scripts/train_mbert_weighted_sqrt.sh [--debug]

set -euo pipefail

EXTRA_ARGS="$@"

RUNS=(
    "1e-5 0.1"
)

for RUN in "${RUNS[@]}"; do
    LR=$(echo "$RUN" | awk '{print $1}')
    LDUR=$(echo "$RUN" | awk '{print $2}')
    RUN_DIR="train_log_weighted_sqrt/mbert/lr${LR}_ldur${LDUR}_sqrtw"
    echo "=========================================="
    echo " [mbert train weighted] lr=${LR}  lambda-dur=${LDUR}"
    echo " log-dir: ${RUN_DIR}"
    echo "=========================================="
    python3 training/train.py \
        --backbone mbert \
        --lr "${LR}" \
        --lambda-dur "${LDUR}" \
        --epochs 15 \
        --log-dir "${RUN_DIR}" \
        ${EXTRA_ARGS}
done

echo "[mbert train weighted] Done. Logs saved under train_log_weighted_sqrt/"
echo ""
echo "View all runs with:"
echo "  tensorboard --logdir train_log_weighted_sqrt/"
