# Streaming Demo Test Texts

## Chinese-English

Run command:
```bash
python streaming_demo.py \
  --model_path ../train_log_consistent/xlmr/lr1e-5_ldur0.1/checkpoints/xlmr_best_sw_f1.pt \
  --language_pair Chinese-English \
  --backbone xlmr \
  --text "<TEXT>"
```

| Length | Text | Translation |
|--------|------|-------------|
| Long (15+ tokens) | `我觉得这个 project 的 deadline 太紧了，我们需要 optimize 一下 workflow 才能 finish on time` | I think this project's deadline is too tight; we need to optimize the workflow a bit to finish on time. |
| Medium-long (10-14 tokens) | `今天的 meeting 讨论了 model performance，大家觉得 accuracy 还需要提升` | Today's meeting discussed model performance; everyone thinks the accuracy still needs improvement. |
| Medium (7-9 tokens) | `这个 feature 很有用，但是 implementation 有点复杂` | This feature is very useful, but the implementation is a bit complex. |
| Short (4-6 tokens) | `我在做 machine learning 的作业` | I'm working on my machine learning assignment. |
| Very short (2-3 tokens) | `这个 model 不错` | This model is pretty good. |

## Spanish-English

Run command:
```bash
python streaming_demo.py \
  --model_path ../train_log_consistent/xlmr/lr1e-5_ldur0.1/checkpoints/xlmr_best_sw_f1.pt \
  --language_pair Spanish-English \
  --backbone xlmr \
  --text "<TEXT>"
```

| Length | Text |
|--------|------|
| Long (15+ tokens) | `El cielo is very blue today and I think the weather will be perfect for our outdoor meeting` |
| Medium (7-9 tokens) | `Mi profesor said the deadline is tomorrow` |
| Short (3-5 tokens) | `El cielo is very blue` |
