# Code-Switching Prediction with Multilingual Transformers

## 1. Introduction

This project investigates **token-level code-switching prediction** using multilingual transformer models.  
The objective is to preprocess mixed-language conversational data and generate structured labels for modeling language switching behavior.

The preprocessing pipeline supports multilingual input (e.g., Chinese–English code-switching) and prepares data for downstream predictive modeling.

---

## 2. Dataset Acquisition and Preprocessing

**Source:** Access the dataset via Hugging Face ([Shelton1013/SwitchLingua_text](https://huggingface.co/datasets/Shelton1013/SwitchLingua_text)).

**Language Coverage:** Selected diverse pairs from the 12 supported languages: Hindi–English, Mandarin–English, Spanish–English.

The dataset is preprocessed to include:

- **Tokenized sequences** of each `data_generation_result` entry.
- **Token-level language identification:** Use model-specific tokenizers (e.g., BPE for RoBERTa variants). For each tokenized sequence, we generate `lang_ids` — language label per subword token. Ensure subword segments are correctly mapped to their respective Language IDs.

---

## 3. Predictive Label Generation

Two types of labels for each token in a sequence:

1. **`ysw` (Switch Label):**  
   Binary indicator (0/1) of whether the next token (`t+1`) switches to a different language.

2. **`ydur` (Duration Label):**  
   Categorical label indicating the length of the upcoming code-switch segment.

| Class ID | Class Name | Burst Length | Rationale |
|----------|------------|--------------|-----------|
| 0        | Small      | 1–2 tokens   | Short, lexical insertions |
| 1        | Medium     | 3–6 tokens   | Phrase-level segments (NP/VP) |
| 2        | Large      | 7+ tokens    | Clausal or full-sentence switches |

### 3.1 Token-Level Output Structure

Each processed entry stored in the `preprocessed` column of `preprocessed_data.pkl` includes:

```python
{
    "original_text": str,
    "tokens": List[str],
    "lang_ids": List[str],
    "ysw": List[int],
    "ydur": List[int]
}
```
Visualized sample of token level output:
![DataLabelSample](DataLabelSample.png)

---
### 4. Installation
### 4.1 Clone Repository

```bash
git clone <https://github.com/JingjingJi94/Multilingual_Code_Switch_Prediction-ML->
cd <repository-name>
```

### 4.2 Create Virtual Environment (Recommended)
```bash
python -m venv ML-code-prediction
source ML-code-prediction/bin/activate      # macOS/Linux
venv\Scripts\activate           # Windows
```

### 4.3 Install Dependencies
```bash
pip install -r requirement.txt
```

---

## 5. Streaming Demo

The streaming demo predicts the **next-token switch probability** and **anticipated duration** from a bilingual text prefix using a trained model checkpoint.

### 5.1 Setup

Place your trained model checkpoint (`.pt` file) inside the `demo/` folder:

```
demo/
├── streaming_demo.py
└── xlmr_best_sw_f1.pt      ← your checkpoint here
```

### 5.2 Run the Demo

Navigate into the `demo/` folder and run:

```bash
cd demo
python streaming_demo.py --model_path xlmr_best_sw_f1.pt --backbone xlmr
```

The demo will prompt you interactively for a language pair and input text each round. Type `exit` or press `Ctrl+C` to quit.

### 5.3 Interactive Input

Each round the demo prompts for:

1. **Language pair** — choose from the supported pairs listed
2. **Text** — enter a bilingual prefix sentence

```
  Available pairs: French-English, Spanish-English, Chinese-English, Hindi-English, Arabic-English, Korean-English
Language pair > Hindi-English
Text        > आजकल technology बहुत तेजी से बदल रही है, right? Smartphones और laptops के बिना life imagine करना मुश्किल है
```

### 5.4 Example Output

The demo walks through 5 steps — tokenization, input ID conversion, prediction point identification, sliding window construction, and model forward pass — before printing the final result:

```
────────────────────────────────────────────────────────────────────────────────
  Prediction Result  |  Hindi-English
────────────────────────────────────────────────────────────────────────────────
  TOKEN                LANG   | NEXT-TOKEN SWITCH PROB   | ANTICIPATED DURATION   | FLAG
────────────────────────────────────────────────────────────────────────────────
  है                   hi     | 0.823                    | Short (1-2 tokens)     | ⚠ HIGH SWITCH
────────────────────────────────────────────────────────────────────────────────
```

### 5.5 Supported Language Pairs

| Language Pair     | Trained | Notes                        |
|-------------------|---------|------------------------------|
| Spanish-English   | ✅      | Training pair                |
| Chinese-English   | ✅      | Training pair                |
| Hindi-English     | ✅      | Training pair                |
| Arabic-English    | ✅      | Training pair                |
| Korean-English    | ❌      | Zero-shot (unseen)           |
| French-English    | ❌      | Zero-shot (unseen)           |

### 5.6 Arguments

| Argument          | Required | Default | Description                                      |
|-------------------|----------|---------|--------------------------------------------------|
| `--model_path`    | Yes*     | None    | Path to `.pt` checkpoint file                    |
| `--backbone`      | No       | `xlmr`  | Tokenizer: `xlmr` or `mbert`                     |
| `--text`          | No       | None    | Pass text directly (skips interactive prompt)    |
| `--language_pair` | No       | None    | Pass language pair directly (skips prompt)       |
| `--window_size`   | No       | 64      | Sliding window size in tokens                    |
| `--dummy`         | No       | False   | Use randomly initialized model for pipeline test |

*Not required when `--dummy` is passed.

### 5.7 Single-Command Mode

To run a single prediction without interactive prompts:

```bash
python streaming_demo.py \
    --model_path xlmr_best_sw_f1.pt \
    --backbone xlmr \
    --language_pair Korean-English \
    --text "WWE가 이번에 Bloodline 재결합 경기를 발표했어. It's a big event for SmackDown"
```

### 5.8 Pipeline Testing (No Checkpoint Required)

To verify the pipeline runs correctly without a trained checkpoint:

```bash
python streaming_demo.py --dummy --language_pair French-English --text "Après la victoire du Real Madrid, je vais lire tous les articles sur le match"
```

> **Note:** `--dummy` uses randomly initialized prediction heads — output probabilities will be meaningless but the full pipeline (tokenization → windowing → forward pass → output) is exercised end to end.

---

## Streaming Data Loader Interface
This module provides a unified interface for loading and inspecting the **SwitchLingua streaming dataset** used for next-token code-switch prediction.

It converts sequence-level preprocessed data into **window-level training samples**.

### Task Definition

Given a prefix window ending at position **t**: `[x(t-N+1) … x(t)]`

The model predicts:

- `ysw[t]` → whether the next token (t+1) switches language  
- `ydur[t]` → the duration class of the upcoming language segment

At timestep t, the model predicts properties of the upcoming transition between t and t+1 using only prefix context. This is a **streaming / causal prediction** setup.

---

### Input Data Format

The loader expects a pickle file: `preprocessed_data.pkl`

Each row contains a `preprocessed` dictionary:

```json
{
  "original_text": str,
  "tokens": List[str],
  "lang_ids": List[str],
  "ysw": List[int],
  "ydur": List[int],
}
```
---

### Quick Start

```python

from data_utils import load_dataset

bundle = load_dataset("preprocessed_data.pkl")

ds = bundle.dataset
loader = bundle.loader
tokenizer = bundle.tokenizer
```

Batch format:
```python
input_ids, language_ids, ysw, ydur
```
Shapes:
```python
input_ids:   (B, window_size)  
language_ids:(B, window_size)  
ysw:         (B,)  
ydur:        (B,)
```
---

### Dataset Statistics

Use:
```python
from data_utils import dataset_stats
stats = dataset_stats(ds)
```
This prints switch rate, duration distribution, and padding ratio.

Or use:
```python
from data_utils import demo
demo()
```
This demos a 3000-sampling process and results.


### Notes

- Left padding is used for early timesteps.
- Switch is predicted for the next token (t+1).
- Duration labels are bucketed:
  - 0 → short (1–2 tokens)
  - 1 → medium (3–6 tokens)
  - 2 → long (≥7 tokens)
  - -1 → not a switch


