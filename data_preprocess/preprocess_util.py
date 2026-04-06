from tqdm import tqdm
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
    # if word in {"。", "、","，"}:
    #     return True
    if re.search(r'[\u3000-\u303F]', word):
        return True
    return False

def is_hindi(word):
    return bool(re.search(r'[\u0900-\u097F]', word))

spanish_chars = set("áéíóúüñÁÉÍÓÚÜÑ")
spanish_stopwords = {
    "de","la","el","y","los","las","en","un","una","por","para","con",
    "del","al","se","que","como","su","es","está","este","esta","son"
}
hardcode_english = {
    "a","an","the","i","me","my","we","us","he","she","it","they","them",
    "is","am","are","was","be","do","did","does","in","on","at","by","of","to","for",
    "and","or","but","so",
    "s","t","d","m",
    "roamed","ancient"
}

def is_punctuation(token):
    """
    Detect punctuation (ASCII + Unicode + Arabic punctuation).
    """
    arabic_punct = {"،", "؛", "؟"}  # comma, semicolon, question mark

    # If it's explicitly Arabic punctuation
    if token in arabic_punct:
        return True

    # General punctuation (no letters/digits)
    return bool(re.fullmatch(r"[^\w\s]+", token))

def is_number(subword):
    """
    Detect if a subword is numeric or mostly numeric.
    Examples: ▁150
    """
    # Remove SentencePiece underscore if present
    s = subword.lstrip('▁')
    return s.replace('.', '', 1).isdigit()

def is_spanish(word):
    """
    Heuristic to detect if a word is Spanish:
    - Contains Spanish accented characters or 'ñ'
    - Or matches a Spanish stopword
    """
    word_lower = word.lower().strip().lstrip('_')
    # check for accented characters
    if any(c in spanish_chars for c in word):
        return True
    # check stopwords
    if word_lower in spanish_stopwords:
        return True

    return False

def is_arabic(word):
    """
    Detect Arabic script.
    """
    return bool(re.search(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]', word))

# Build a detector for English, Arabic and Spanish
detector = (
    LanguageDetectorBuilder.from_languages(
        Language.ENGLISH,
        Language.SPANISH,
        Language.ARABIC
    )
    .build()
)

def detect_word_lang(word):
    """
    Detect language of a word:
    - Chinese / Hindi heuristics first
    - Spanish heuristic (accent + stopword)
    - Lingua fallback for short/ambiguous words
    - Hardcode common English words to prevent misdetection
    """
    word = word.strip().lstrip('▁').lower()
    if not word:
        return "en"
    
    # Hardcode common English words
    if word in hardcode_english:
        return "en"

    # punctuation
    if is_punctuation(word):
        return "punct"
    
    # Chinese / Hindi
    if is_chinese(word):
        return "zh"
    if is_hindi(word):
        return "hi"
    if is_arabic(word):
        return "ar"

    # Spanish heuristic
    if is_spanish(word):
        return "es"

    # Fallback with Lingua
    try:
        lang = detector.detect_language_of(word)
        if lang == Language.SPANISH:
            return "es"
        elif lang == Language.ARABIC:
            return "ar"
        elif lang == Language.ENGLISH:
            return "en"
        else:
            return "en"  # fallback
    except:
        return "en"

def tokenize_with_lang_mapping(text, tokenizer, language_pair):
    """
    Tokenize text and assign language IDs for subwords.
    Guarantees at most two languages per sequence.
    """

    tokens = []
    lang_ids = []

    # Define allowed languages
    if language_pair == "Spanish-English":
        allowed_langs = {"es", "en"}
    elif language_pair == "Chinese-English":
        allowed_langs = {"zh", "en"}
    elif language_pair == "Hindi-English":
        allowed_langs = {"hi", "en"}
    elif language_pair == "Arabic-English":
        allowed_langs = {"ar", "en"}
    else:
        allowed_langs = {"en"}

    def clamp_lang(lang):
        """Force language into allowed set."""
        if lang in allowed_langs or lang == "punct":
            return lang
        # fallback to English if available
        if "en" in allowed_langs:
            return "en"
        return list(allowed_langs)[0]

    if language_pair == "Spanish-English":
        words = text.split()

        for word in words:
            word_lang = clamp_lang(detect_word_lang(word))

            sub_tokens = tokenizer.tokenize(word)
            tokens.extend(sub_tokens)

            for sub in sub_tokens:
                if is_punctuation(sub):
                    lang_ids.append("punct")

                elif is_number(sub):
                    if lang_ids:
                        lang_ids.append(lang_ids[-1])
                    else:
                        lang_ids.append(word_lang)

                else:
                    lang_ids.append(word_lang)

    else:
        sub_tokens = tokenizer.tokenize(text)

        for sub in sub_tokens:

            if is_punctuation(sub):
                lang_ids.append("punct")

            elif is_number(sub):
                if lang_ids:
                    lang_ids.append(lang_ids[-1])
                else:
                    lang_ids.append(clamp_lang(detect_word_lang(sub)))

            else:
                lang_ids.append(clamp_lang(detect_word_lang(sub)))

        tokens = sub_tokens

    return tokens, lang_ids

def generate_predictive_switch_labels(tokens, lang_ids):
    """
    Generate ysw and ydur labels while ignoring punctuation tokens.
    """
    n = len(tokens)
    ysw = [0] * n
    ydur = [-1] * n

    for t in range(n):

        if lang_ids[t] == "punct":
            continue

        # find next non-punctuation token
        j = t + 1
        while j < n and lang_ids[j] == "punct":
            j += 1

        if j >= n:
            continue

        if lang_ids[j] != lang_ids[t]:
            ysw[t] = 1

            new_lang = lang_ids[j]
            seg_len = 1
            k = j + 1

            while k < n:
                if lang_ids[k] == "punct":
                    k += 1
                    continue
                if lang_ids[k] == new_lang:
                    seg_len += 1
                    k += 1
                else:
                    break

            if seg_len <= 2:
                ydur[t] = 0
            elif seg_len <= 6:
                ydur[t] = 1
            else:
                ydur[t] = 2

    return ysw, ydur

def preprocess_and_label(df, tokenizer):
    """
    Preprocess df and store info in 'preprocessed' column with a progress bar.
    """
    preprocessed_data = []

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
        # tokenize + language detection, and convert tokens to input ids
        tokens, lang_ids = tokenize_with_lang_mapping(text, tokenizer, language_pair)
        # Convert tokens to IDs, replacing unknown tokens with tokenizer.unk_token_id
        input_ids = []
        for tok in tokens:
            id_ = tokenizer.convert_tokens_to_ids(tok)
            if id_ is None:
                id_ = tokenizer.unk_token_id  # fallback for unknowns
            input_ids.append(id_)

        # Generate predictive switch & duration labels
        ysw, ydur = generate_predictive_switch_labels(tokens, lang_ids)

        # Store in dictionary
        sample = {
            "language_pair": language_pair,
            "original_text": text,
            "tokens": tokens,
            "input_ids": input_ids,
            "lang_ids": lang_ids,
            "ysw": ysw,
            "ydur": ydur
        }

        preprocessed_data.append(sample)

    return preprocessed_data