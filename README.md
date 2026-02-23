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

Each processed entry stored in the `preprocessed` column of `df_preprocessed.pkl` includes:

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

The loader expects a pickle file: `df_preprocessed.pkl`

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

bundle = load_dataset("df_preprocessed.pkl")

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


