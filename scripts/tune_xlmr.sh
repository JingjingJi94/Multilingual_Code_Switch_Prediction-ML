#!/usr/bin/env bash
# Hyperparameter sweep for XLM-R
# Usage: bash scripts/tune_xlmr.sh

set -euo pipefail

LR_VALUES=(1e-6 1e-5 1e-4)
LDUR_VALUES=(0.1 1 10)

RUNS=""
for LR in "${LR_VALUES[@]}"; do
    for LDUR in "${LDUR_VALUES[@]}"; do
        RUNS="${RUNS} ${LR},${LDUR}"
    done
done

python3 training/tune.py \
    --backbone xlmr \
    --log-dir logs/tune_xlmr \
    --runs "${RUNS}"

echo "[xlmr] Done. Logs saved under logs/tune_xlmr/"
