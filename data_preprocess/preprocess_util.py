from tqdm import tqdm  # optional, for progress bar
import re
import ast
from lingua import Language, LanguageDetectorBuilder

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

spanish_chars = set("áéíóúüñÁÉÍÓÚÜÑ")
spanish_stopwords = {
    "de","la","el","y","los","las","en","un","una","por","para","con",
    "del","al","se","que","como","su","es","está","este","esta","son"
}
punctuation_chars = set(".,!?;:()[]{}“”‘’\"…")

def is_spanish(word):
    """
    Heuristic to detect if a word is Spanish:
    - Contains Spanish accented characters or 'ñ'
    - Or matches a Spanish stopword
    """
    word_lower = word.lower()
    # check for accented characters
    if any(c in spanish_chars for c in word):
        return True
    # check stopwords
    if word_lower in spanish_stopwords:
        return True

    return False


# Build a detector for English and Spanish
detector = (
    LanguageDetectorBuilder.from_languages(Language.ENGLISH, Language.SPANISH)
    .build()
)

def detect_word_lang(word):
    """
    Detect language of a word:
    - Chinese / Hindi heuristics first
    - Spanish heuristic (accent + stopword)
    - Lingua fallback for short/ambiguous words
    """
    word = word.strip()

    # Chinese / Hindi
    if is_chinese(word):
        return "zh"
    if is_hindi(word):
        return "hi"

    # Spanish heuristic
    if is_spanish(word):
        return "es"

    # Fallback with Lingua
    try:
        lang = detector.detect_language_of(word)
        if lang == Language.SPANISH:
            return "es"
        elif lang == Language.ENGLISH:
            return "en"
        else:
            return "en"  # fallback
    except:
        return "en"

def tokenize_with_lang_mapping(text, tokenizer, language_pair):
    """
    Tokenize text and assign language IDs using:
    - is_spanish() heuristic
    - Lingua fallback
    - Chinese/Hindi heuristics
    """
    tokens = []
    lang_ids = []
    if language_pair == "Spanish-English":
        words = text.split()
        for word in words:
            word_lang = detect_word_lang(word)
            sub_tokens = tokenizer.tokenize(word)
            tokens.extend(sub_tokens)

            # Assign the detected language to ALL subwords
            lang_ids.extend([word_lang] * len(sub_tokens))
    else:
        tokens = tokenizer.tokenize(text)
        for tok in tokens:
            lang_ids.append(detect_word_lang(tok))

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
        
        language_pair = row.get("language_pair", None)
        # Word-level detection + BPE mapping
        tokens, lang_ids = tokenize_with_lang_mapping(text, tokenizer, language_pair)

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