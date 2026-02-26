from transformers import AutoModelForSequenceClassification
from tqdm import tqdm  # optional, for progress bar
import re
import ast
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException


def normalize_lang(lang):
    lang = lang.lower()
    
    if lang.startswith("zh"):
        return "zh"
    if lang.startswith("hi"):
        return "hi"
    if lang.startswith("es"):
        return "es"
    if lang.startswith("en"):
        return "en"
    
    # fallback for unexpected Latin predictions (sv, pt, it, etc.)
    return "en"

def is_chinese(word):
    """
    Return True if the word is Chinese or a Chinese punctuation like '。'
    """
    # Check for any CJK character
    if re.search(r'[\u4e00-\u9fff]', word):
        return True
    # Treat Chinese full stop as Chinese
    if word in {'。'}:
        return True
    return False

def is_hindi(word):
    return bool(re.search(r'[\u0900-\u097F]', word))

def detect_word_lang(word):
    word = word.strip()
    if not word:
        return "en"
    
    # Script-based heuristic for chinese and hindi
    if is_chinese(word):
        return "zh"
    if is_hindi(word):
        return "hi"
    
    # Use langdetect for Latin words
    try:
        lang = detect(word)
        return normalize_lang(lang)
    except LangDetectException:
        return "en"
    
DetectorFactory.seed = 0
def tokenize_with_lang_mapping(text, tokenizer):
    """
    Tokenize text with your model tokenizer and get lang_ids using transformer-based classifier.
    Returns:
        tokens: list of subword tokens (your model tokenizer)
        lang_ids: list of language IDs aligned with tokens
    """
    words = text.split() 
    tokens = [] 
    lang_ids = []

    for word in words: 
        word_lang = detect_word_lang(word) 
        # tokenize WITHOUT adding special tokens 
        sub_tokens = tokenizer.tokenize(word) 
        
        tokens.extend(sub_tokens) 
        # all_lang_ids.extend([word_lang] * len(sub_tokens)) 
        
        # Assign language to each subword 
        for sub in sub_tokens: 
            if is_chinese(sub): 
                lang_ids.append("zh") # override for Chinese char/punct 
            else: lang_ids.append(word_lang)

    return tokens, lang_ids

def generate_predictive_switch_labels(tokens, lang_ids):
    """
    Generate ysw and ydur labels for a token sequence.
    """
    n = len(tokens)
    ysw = [0] * n
    ydur = [-1] * n

    for t in range(n-1):
        if lang_ids[t+1] != lang_ids[t]:
            ysw[t] = 1
            # compute length of new language segment
            new_lang = lang_ids[t+1]
            seg_len = 1
            for k in range(t+2, n):
                if lang_ids[k] == new_lang:
                    seg_len += 1
                else:
                    break
            # duration class
            if seg_len <= 2:
                ydur[t] = 0
            elif seg_len <= 6:
                ydur[t] = 1
            else:
                ydur[t] = 2
        else:
            ysw[t] = 0
            ydur[t] = -1
    
    ysw[-1] = 0
    ydur[-1] = -1
    return ysw, ydur

def preprocess_and_label(df, tokenizer):
    """
    Preprocess df and store info in 'preprocessed' column with a progress bar.
    """
    # Create the column if it doesn't exist
    if "preprocessed" not in df.columns:
        df["preprocessed"] = None

    # Wrap iterrows with tqdm
    for idx, row in tqdm(df.iterrows(), total=len(df), desc="Preprocessing"):
        # Convert string to list
        try:
            text_list = ast.literal_eval(row["data_generation_result"])
        except:
            text_list = [row["data_generation_result"]]

        # skip samples at index 9910 and 13313 due to format errors in raw dataset
        try:
            text = " ".join(text_list)
        except:
            continue

        # Word-level detection + BPE mapping
        tokens, lang_ids = tokenize_with_lang_mapping(text, tokenizer)

        # Generate predictive switch & duration labels
        ysw, ydur = generate_predictive_switch_labels(tokens, lang_ids)

        # Store in dictionary
        preprocessed_row = {
            "original_text": text,
            "tokens": tokens,
            "lang_ids": lang_ids,
            "ysw": ysw,
            "ydur": ydur
        }

        # Assign to DataFrame
        df.at[idx, "preprocessed"] = preprocessed_row

    return df