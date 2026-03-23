#!/usr/bin/env bash
# Hyperparameter sweep — part 2 of 2 (7 runs)
# Run in parallel with tune_part1.sh
# Usage: bash scripts/tune_part2.sh [--backbone xlmr|mbert|both] [--debug]

set -euo pipefail

EXTRA_ARGS="$@"

RUNS=(
    "5e-4 5"
    "5e-4 10"
    "1e-5 0.1"
    "1e-5 0.5"
    "1e-5 1"
    "1e-5 5"
    "1e-5 10"
)

for RUN in "${RUNS[@]}"; do
    LR=$(echo "$RUN" | awk '{print $1}')
    LDUR=$(echo "$RUN" | awk '{print $2}')
    RUN_DIR="logs/tune/lr${LR}_ldur${LDUR}"
    echo "=========================================="
    echo " [part2] lr=${LR}  lambda-dur=${LDUR}"
    echo " log-dir: ${RUN_DIR}"
    echo "=========================================="
    python3 training/train.py \
        --lr "${LR}" \
        --lambda-dur "${LDUR}" \
        --log-dir "${RUN_DIR}" \
        ${EXTRA_ARGS}
done

echo "[part2] Done. Logs saved under logs/tune/"
echo ""
echo "View all runs with:"
echo "  tensorboard --logdir logs/tune"
