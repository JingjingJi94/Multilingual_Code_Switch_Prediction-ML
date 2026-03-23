#!/usr/bin/env bash
# Hyperparameter sweep — part 1 of 2 (8 runs)
# Run in parallel with tune_part2.sh
# Usage: bash scripts/tune_part1.sh [--backbone xlmr|mbert|both] [--debug]

set -euo pipefail

EXTRA_ARGS="$@"

RUNS=(
    "1e-4 0.1"
    "1e-4 0.5"
    "1e-4 1"
    "1e-4 5"
    "1e-4 10"
    "5e-4 0.1"
    "5e-4 0.5"
    "5e-4 1"
)

for RUN in "${RUNS[@]}"; do
    LR=$(echo "$RUN" | awk '{print $1}')
    LDUR=$(echo "$RUN" | awk '{print $2}')
    RUN_DIR="logs/tune/lr${LR}_ldur${LDUR}"
    echo "=========================================="
    echo " [part1] lr=${LR}  lambda-dur=${LDUR}"
    echo " log-dir: ${RUN_DIR}"
    echo "=========================================="
    python3 training/train.py \
        --lr "${LR}" \
        --lambda-dur "${LDUR}" \
        --log-dir "${RUN_DIR}" \
        ${EXTRA_ARGS}
done

echo "[part1] Done. Logs saved under logs/tune/"
