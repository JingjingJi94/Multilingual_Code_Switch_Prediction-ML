#!/usr/bin/env bash
# Evaluation script for XLM-R and mBERT
# Usage: bash scripts/evaluate.sh

set -euo pipefail

XLMR_CKPT="train_log_new/xlmr/lr1e-5_ldur0.1/checkpoints/xlmr_best_sw_f1.pt"
MBERT_CKPT="train_log_new/mbert/lr1e-5_ldur0.1/checkpoints/mbert_best_sw_f1.pt"

XLMR_TEST="train_log_new/xlmr/lr1e-5_ldur0.1/checkpoints/xlmr_test_entries.pkl"
MBERT_TEST="train_log_new/mbert/lr1e-5_ldur0.1/checkpoints/mbert_test_entries.pkl"

XLMR_ZEROSHOT="data_preprocess/preprocessed_zeroshot_xlmr.pkl"
MBERT_ZEROSHOT="data_preprocess/preprocessed_zeroshot_mbert.pkl"

RESULTS_DIR="results/eval"

python3 evaluation/evaluate.py \
    --xlmr-checkpoint  "${XLMR_CKPT}" \
    --mbert-checkpoint "${MBERT_CKPT}" \
    --test-entries      "${XLMR_TEST}" \
    --mbert-test-entries "${MBERT_TEST}" \
    --xlmr-zeroshot  "${XLMR_ZEROSHOT}" \
    --mbert-zeroshot "${MBERT_ZEROSHOT}" \
    --results-dir "${RESULTS_DIR}"

echo ""
echo "Results saved to ${RESULTS_DIR}/eval_results.json"
