#!/usr/bin/env bash
# Hyperparameter sweep for XLM-R — part 2 of 2 (7 runs)
# Run in parallel with tune_xlmr_part1.sh
# Usage: bash scripts/tune_xlmr_part2.sh [--debug]

set -euo pipefail

EXTRA_ARGS="$@"

RUNS=(
    "1e-5 0.5"
)

for RUN in "${RUNS[@]}"; do
    LR=$(echo "$RUN" | awk '{print $1}')
    LDUR=$(echo "$RUN" | awk '{print $2}')
    RUN_DIR="logs/train_xlmr2/lr${LR}_ldur${LDUR}"
    echo "=========================================="
    echo " [xlmr train2] lr=${LR}  lambda-dur=${LDUR}"
    echo " log-dir: ${RUN_DIR}"
    echo "=========================================="
    python3 training/train.py \
        --backbone xlmr \
        --lr "${LR}" \
        --lambda-dur "${LDUR}" \
        --log-dir "${RUN_DIR}" \
        ${EXTRA_ARGS}
done

echo "[xlmr train2] Done. Logs saved under logs/train_xlmr2/"
echo ""
echo "View all runs with:"
echo "  tensorboard --logdir logs/train_xlmr2"
