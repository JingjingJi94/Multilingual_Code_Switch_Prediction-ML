#!/usr/bin/env bash
# Training script for XLM-R (ablation: sqrt-weighted switch CE)
# Usage: bash scripts/train_xlmr_weighted_sqrt.sh [--debug]

set -euo pipefail

EXTRA_ARGS="$@"

RUNS=(
    "1e-5 0.1"
)

for RUN in "${RUNS[@]}"; do
    LR=$(echo "$RUN" | awk '{print $1}')
    LDUR=$(echo "$RUN" | awk '{print $2}')
    RUN_DIR="train_log_weighted_sqrt/xlmr/lr${LR}_ldur${LDUR}_sqrtw"
    echo "=========================================="
    echo " [xlmr train weighted] lr=${LR}  lambda-dur=${LDUR}"
    echo " log-dir: ${RUN_DIR}"
    echo "=========================================="
    python3 training/train.py \
        --backbone xlmr \
        --lr "${LR}" \
        --lambda-dur "${LDUR}" \
        --epochs 15 \
        --log-dir "${RUN_DIR}" \
        ${EXTRA_ARGS}
done

echo "[xlmr train weighted] Done. Logs saved under train_log_weighted_sqrt/"
echo ""
echo "View all runs with:"
echo "  tensorboard --logdir train_log_weighted_sqrt/"
