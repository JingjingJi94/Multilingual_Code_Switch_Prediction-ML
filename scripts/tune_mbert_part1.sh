#!/usr/bin/env bash
# Hyperparameter sweep for mBERT — part 1 of 2 (8 runs)
# Run in parallel with tune_mbert_part2.sh
# Usage: bash scripts/tune_mbert_part1.sh [--debug]

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
    RUN_DIR="logs/tune_mbert/lr${LR}_ldur${LDUR}"
    echo "=========================================="
    echo " [mbert part1] lr=${LR}  lambda-dur=${LDUR}"
    echo " log-dir: ${RUN_DIR}"
    echo "=========================================="
    python3 training/train.py \
        --backbone mbert \
        --lr "${LR}" \
        --lambda-dur "${LDUR}" \
        --log-dir "${RUN_DIR}" \
        ${EXTRA_ARGS}
done

echo "[mbert part1] Done. Logs saved under logs/tune_mbert/"
