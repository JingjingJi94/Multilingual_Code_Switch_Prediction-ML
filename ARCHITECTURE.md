# Architecture: Multilingual Code-Switch Prediction

## Overview

This project predicts **token-level language switches** in multilingual (code-switched) text in a streaming, causal manner. Given a prefix of tokens, the model outputs:

1. **Switch probability** — will the next token switch language?
2. **Duration class** — if a switch occurs, how long will the new-language segment be? (short: 1–2, medium: 3–6, long: 7+ tokens)

Supported language pairs: Spanish–English, Chinese–English, Hindi–English, Arabic–English (trained); French–English, Korean–English (zero-shot).

---

## System Architecture Diagram

```mermaid
flowchart TD
    subgraph PRE["📦 Preprocessing  (data_preprocess/)"]
        direction TB
        A1([SwitchLingua\nHugging Face]) --> A2[Filter Language Pairs]
        A2 --> A3[Tokenize\nXLM-R BPE / mBERT WordPiece]
        A3 --> A4[Per-token Language Detection\nscript heuristics + Lingua]
        A4 --> A5["Label Generation\nysw = binary switch\nydur = duration class 0/1/2"]
        A5 --> A6[(preprocessed_data.pkl)]
    end

    subgraph DATA["🗂 Data Loading  (data/)"]
        direction TB
        A6 --> B1["80 / 10 / 10 Sequence Split\n(sequence-level — no window leakage)"]
        B1 --> B2["SwitchLinguaStreamDataset\nsliding window size = 64\nleft-padded, causal"]
        B2 --> B3[DataLoader\nbatch size = 128]
    end

    subgraph MODEL["🧠 Model  (models/)"]
        direction TB
        B3 --> C1["input_ids  (B, 64)\nattention_mask  (B, 64)"]
        C1 --> C2["XLM-R or mBERT Backbone\npretrained transformer"]
        C2 --> C3["Extract last token h_t\n(B, 768)"]
        C3 --> C4["Switch Head\nLinear(768 → 2)"]
        C3 --> C5["Duration Head\nLinear(768 → 3)"]
    end

    subgraph TRAIN["⚙️ Training  (training/)"]
        direction TB
        C4 --> D1[switch_logits]
        C5 --> D2[duration_logits]
        D1 --> D3["MultiTaskLoss\nλ_sw · L_sw  +  λ_dur · L_dur"]
        D2 --> D3
        D3 --> D4[AdamW + AMP]
        D4 --> D5[(xlmr_best_sw_f1.pt\nmbert_best_sw_f1.pt)]
        D4 --> D6[(xlmr_best_dur_acc.pt\nmbert_best_dur_acc.pt)]
    end

    subgraph EVAL["📊 Evaluation  (evaluation/)"]
        direction TB
        D5 --> E1[Anticipatory F1\nper language pair]
        D5 --> E2[Duration Accuracy]
        E1 --> E3["Universality σ\nstd dev of per-pair F1"]
        E1 --> E4[Inter / Intra-sentential\nQualitative Analysis]
    end

    subgraph DEMO["🎤 Demo  (demo/)"]
        D5 --> F1["streaming_demo.py\ntoken-by-token prediction\nP(switch) + duration class"]
    end

    PRE --> DATA --> MODEL --> TRAIN --> EVAL
    TRAIN --> DEMO
```

---

## Model Architecture Detail

```mermaid
flowchart LR
    subgraph INPUT["Input Window (size = 64)"]
        I1["[PAD ... tok_{t-k} ... tok_t]"]
    end

    subgraph BACKBONE["Transformer Backbone"]
        B1["Embedding Layer"]
        B2["12× Transformer Block\nMulti-head Self-Attention\n+ FFN"]
        B3["Hidden States\n(B, 64, 768)"]
        B1 --> B2 --> B3
    end

    subgraph HEADS["Output Heads"]
        H0["Extract h_t\n= last position\n(B, 768)"]
        H1["Switch Head\nLinear(768 → 2)\nsoftmax → P(switch)"]
        H2["Duration Head\nLinear(768 → 3)\nargmax → {short, medium, long}"]
        H0 --> H1
        H0 --> H2
    end

    INPUT --> BACKBONE --> HEADS
```

---

## Label Schema

```mermaid
flowchart LR
    subgraph SEQ["Token Sequence"]
        T0["tok_0\n(en)"] --- T1["tok_1\n(en)"] --- T2["tok_2\n(es)"] --- T3["tok_3\n(es)"] --- T4["tok_4\n(es)"] --- T5["tok_5\n(en)"]
    end

    subgraph YSW["ysw  (binary switch)"]
        S0["0"] --- S1["1"] --- S2["0"] --- S3["0"] --- S4["1"] --- S5["0"]
    end

    subgraph YDUR["ydur  (duration class)"]
        D0["-1"] --- D1["0\nshort 1–2"] --- D2["-1"] --- D3["-1"] --- D4["2\nlong 7+"] --- D5["-1"]
    end

    T1 -.->|"next token switches lang"| S1
    T1 -.->|"segment length = 3"| D1
```

---

## Directory Structure

```
Multilingual_Code_Switch_Prediction-ML/
├── data/                       # Dataset loading & windowing
│   ├── data_utils.py           # Load pickle, split sequences, dataset stats
│   └── streaming_dataloader.py # SwitchLinguaStreamDataset (window-level)
├── data_preprocess/            # Raw → pickle preprocessing
│   ├── preprocess.py           # Main pipeline (Hugging Face → pickle)
│   ├── preprocess_util.py      # Language detection, tokenization, label generation
│   ├── preprocess_zeroshot.py  # Zero-shot pair preprocessing
│   └── duration_distribution.py
├── models/                     # Model architectures
│   ├── dual_head_model.py      # DualHeadCausalModel (main)
│   ├── single_head_model.py    # SingleHeadModel (ablation: switch only)
│   ├── naive_baseline.py       # Frequency-based baselines
│   └── causal_mask_builder.py  # Causal attention mask utilities
├── training/                   # Training & tuning
│   ├── train.py                # Main training loop + checkpointing
│   ├── losses.py               # MultiTaskLoss
│   └── tune.py                 # Hyperparameter sweep harness
├── evaluation/                 # Metrics & analysis
│   ├── evaluate.py             # Test-set evaluation (XLM-R vs mBERT)
│   ├── metrics.py              # Anticipatory F1, universality sigma
│   ├── qualitative_analysis.py # Inter/intra-sentential switch analysis
│   └── plot_universality.py
├── demo/                       # Interactive prediction demo
│   └── streaming_demo.py
├── scripts/                    # Shell scripts for training/eval runs
├── checkpoints/                # Saved model weights (.pt)
├── results/                    # Evaluation outputs (JSON, markdown, charts)
└── tests/
    └── test_streaming_dataloader.py
```

---

## ML Pipeline

```
Raw SwitchLingua data (Hugging Face)
         │
         ▼
  ┌─────────────────────────────────────────┐
  │  Preprocessing  (data_preprocess/)      │
  │  • Filter by language pair              │
  │  • Tokenize (XLM-R BPE / mBERT WP)     │
  │  • Detect per-token language            │
  │  • Generate ysw and ydur labels         │
  └──────────────────┬──────────────────────┘
                     │  preprocessed_data_*.pkl
                     ▼
  ┌─────────────────────────────────────────┐
  │  Data Loading  (data/)                  │
  │  • 80/10/10 sequence-level split        │
  │  • SwitchLinguaStreamDataset            │
  │    – sliding windows of size 64         │
  │    – each sample predicts token t+1     │
  │    – epoch-level dynamic resampling     │
  └──────────────────┬──────────────────────┘
                     │  (input_ids, attn_mask, ysw, ydur)
                     ▼
  ┌─────────────────────────────────────────┐
  │  Model  (models/)                       │
  │  Backbone: XLM-R or mBERT              │
  │    ↓ last hidden state h_t (B, 768)    │
  │  Switch head: Linear(768 → 2)          │
  │  Duration head: Linear(768 → 3)        │
  └──────────────────┬──────────────────────┘
                     │  (switch_logits, duration_logits)
                     ▼
  ┌─────────────────────────────────────────┐
  │  Training  (training/)                  │
  │  MultiTaskLoss:                         │
  │    L = λ_sw·L_sw + λ_dur·L_dur         │
  │  AdamW + AMP; save best F1 / best Acc  │
  └──────────────────┬──────────────────────┘
                     │
                     ▼
  ┌─────────────────────────────────────────┐
  │  Evaluation  (evaluation/)              │
  │  • Anticipatory F1 per language pair    │
  │  • Duration accuracy                    │
  │  • Universality sigma (σ of per-pair F1)│
  │  • Inter/intra-sentential analysis      │
  └─────────────────────────────────────────┘
```

---

## Key Components

### Data: `SwitchLinguaStreamDataset`

Each sequence is converted into overlapping windows of width 64. Window `t` ends at position `t`; labels describe position `t+1`. Left-padding is applied when the prefix is shorter than the window size. Sequences are split at the **sequence level** before windowing to prevent leakage.

```
sequence:  [tok_0, tok_1, ..., tok_N]
window t:  [PAD, PAD, ..., tok_{t-63}, ..., tok_t]  → predicts (ysw[t], ydur[t])
```

| Output field | Shape | Description |
|---|---|---|
| `input_ids` | `(B, 64)` | Subword token IDs |
| `attention_mask` | `(B, 64)` | 1 = real token, 0 = padding |
| `lang_ids` | `(B, 64)` | Integer language ID per token |
| `ysw_label` | `(B,)` | Binary: 1 if next token switches language |
| `ydur_label` | `(B,)` | Duration class (0/1/2), or -1 if no switch |

### Labels: generation logic

```
ysw[t] = 1  if next non-punctuation token differs in detected language
ydur[t] = 0  (1–2 tokens)    if ysw[t] == 1
           1  (3–6 tokens)
           2  (7+ tokens)
          -1  if ysw[t] == 0   (ignored in duration loss)
```

Language detection uses Unicode script ranges (Chinese, Hindi, Arabic) and accent/stopword heuristics (Spanish), with Lingua library as a fallback. A smoothing pass corrects isolated single-token misdetections.

### Model: `DualHeadCausalModel`

```
input_ids + attention_mask
        │
   XLM-R / mBERT backbone
        │
last hidden state (B, 64, 768)
        │  extract position -1
       h_t  (B, 768)
      ┌─┴─┐
      │   │
  Linear  Linear
  (768,2) (768,3)
      │       │
switch_logits  duration_logits
```

The last-position hidden state encodes the full left context under the pretrained transformer's attention, making a separate causal mask unnecessary for inference correctness.

### Loss: `MultiTaskLoss`

```
L_sw  = CrossEntropyLoss(switch_logits, ysw, weight=sqrt_inv_freq)
L_dur = CrossEntropyLoss(duration_logits, ydur, ignore_index=-1)
L     = λ_sw · L_sw + λ_dur · L_dur
```

Default: `λ_sw = 1.0`, `λ_dur = 0.5`. Class weights are optional (activated with `--weighted-loss`).

### Evaluation: `metrics.py`

| Metric | Definition |
|---|---|
| `anticipatory_f1` | Binary F1 with `pos_label=1` (switch class) |
| `duration_accuracy` | Accuracy over positions where `ydur != -1` |
| `universality_sigma` | Std dev of per-pair F1 (lower = more consistent across pairs) |

---

## Checkpoints

| File | Backbone | Optimized for | Size |
|---|---|---|---|
| `xlmr_best_sw_f1.pt` | XLM-R | Switch F1 | ~1.1 GB |
| `mbert_best_sw_f1.pt` | mBERT | Switch F1 | ~711 MB |
| `xlmr_best_dur_acc.pt` | XLM-R | Duration accuracy | ~1.1 GB |
| `mbert_best_dur_acc.pt` | mBERT | Duration accuracy | ~711 MB |

---

## Training Configuration

| Argument | Default | Description |
|---|---|---|
| `--backbone` | `both` | `xlmr`, `mbert`, or `both` |
| `--epochs` | `10` | Training epochs |
| `--lr` | `1e-5` | AdamW learning rate |
| `--lambda-sw` | `1.0` | Switch loss weight |
| `--lambda-dur` | `0.5` | Duration loss weight |
| `--window-size` | `64` | Sliding window length |
| `--sample-rate` | `0.2` | Fraction of windows per epoch |
| `--weighted-loss` | off | Enable sqrt inverse-freq class weights |
| `--single-task` | off | Ablation: switch head only |
| `--detach-dur` | off | Ablation: stop gradient from duration head |
| `--debug` | off | 1% data subsampling for fast iteration |

---

## Ablations & Baselines

| Variant | Description |
|---|---|
| `DualHeadCausalModel` | Full model (switch + duration heads) |
| `SingleHeadModel` | Switch head only |
| `--detach-dur` | Duration loss does not backprop into backbone |
| `NaiveSwitchPredictor` | Frequency table P(switch \| language_id) |
| `ZeroBaseline` | Always predicts no switch |

---

## Demo Usage

```bash
# Interactive
python demo/streaming_demo.py --model_path checkpoints/xlmr_best_sw_f1.pt

# Single command
python demo/streaming_demo.py \
  --model_path checkpoints/xlmr_best_sw_f1.pt \
  --language_pair "Spanish-English" \
  --text "Hola, how are you doing today?"

# Pipeline test (no checkpoint needed)
python demo/streaming_demo.py --dummy
```

Output table columns: `token | lang | P(switch) | anticipated_duration | flag`

---

## Dependencies

```
torch, transformers, datasets, scikit-learn, pandas, numpy,
lingua-language-detector, tqdm, tensorboard, matplotlib, seaborn,
huggingface_hub, pytest
```
