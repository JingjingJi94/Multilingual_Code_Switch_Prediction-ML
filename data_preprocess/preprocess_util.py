from tqdm import tqdm
import re
import ast
from lingua import Language, LanguageDetectorBuilder
from collections import Counter

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

def is_korean(word):
    """
    Detect Hangul syllables, jamo, or compatibility jamo.
    """
    return bool(re.search(r'[\uAC00-\uD7AF\u1100-\u11FF\u3130-\u318F]', word))

spanish_chars = set("áéíóúüñÁÉÍÓÚÜÑ")
spanish_stopwords = {
    "de","la","el","y","los","las","en","un","una","por","para","con",
    "del","al","se","que","como","su","es","está","este","esta","son"
}
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
    if word_lower in spanish_stopwords and word_lower not in french_stopwords:
        return True

    return False

# French-specific chars and words
french_only_chars = set("àâêîôûùœæçÀÂÊÎÔÛÙŒÆÇèÈëËïÏ")
french_stopwords = {
    "le","la","les","de","du","des","un","une","et","en","au","aux",
    "est","sont","je","tu","il","elle","nous","vous","ils","elles",
    "que","qui","quoi","ne","pas","se","ce","pour","sur","dans","par","avec",
    "mais","ou","donc", "dont","or","ni","car","je","mon","ton","son","ma","ta","sa",
    "mais","très","plus","bien","aussi","comme","où", "était", "avoir", 
    "être", "fait", "va","après", "victoire", "contre", "sûr"
}

def is_french(word):
    """
    Heuristic to detect if a word is French:
    - Contains French-only accented characters (à, â, ê, î, ô, û, ù, œ, æ, è, ë, ï)
    - Or matches a French stopword (but not a Spanish stopword)
    """
    word_lower = word.lower().strip().lstrip('_')
    # Characters that appear in French but not Spanish
    if any(c in french_only_chars for c in word):
        return True
    # French stopwords not shared with Spanish
    if word_lower in french_stopwords and word_lower not in spanish_stopwords:
        return True
    return False

hardcode_english = {
    "a","an","the","i","me","my","we","us","he","she","it","they","them",
    "is","am","are","was","be","do","did","does","in","on","at","by","of","to","for",
    "and","or","but","t","d","m",
    "roamed","ancient",
    # add common words Lingua misclassifies as French
    "tomorrow","yesterday","today","morning","evening","night",
    "good","great","very","just","now","here","there","when","what","how",
    "about","after","before","because","between","through","without",
    "expert","analysis","analyse",
}

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
        Language.ARABIC,
        Language.FRENCH,
        Language.KOREAN
    )
    .build()
)

def detect_word_lang(word, language_pair=None):
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
    if is_korean(word):
        return "ko"

    # Spanish heuristic
    if is_spanish(word):
        return "es"
    if is_french(word):
        return "fr"
    
    # Pair-aware fallback for shared stopwords before hitting Lingua
    if language_pair == "French-English" and word in french_stopwords:
        return "fr"
    if language_pair == "Spanish-English" and word in spanish_stopwords:
        return "es"
    
    # Fallback with Lingua
    try:
        lang = detector.detect_language_of(word)
        if lang == Language.SPANISH:
            return "es"
        elif lang == Language.ARABIC:
            return "ar"
        elif lang == Language.FRENCH:
            return "fr"
        elif lang == Language.KOREAN:
            return "ko"
        elif lang == Language.ENGLISH:
            return "en"
        else:
            return "en"  # fallback
    except:
        return "en"

def smooth_lang_ids(lang_ids, confirmed, window=2, threshold=0.65):
    """
    Post-hoc smoothing pass over token-level language IDs.
 
    For each non-punct token, look at up to `window` non-punct neighbours on
    each side. If those neighbours agree on a single language with a proportion
    >= threshold, override the current label with that language.
 
    This corrects two classes of error without special-casing:
      - Isolated misdetections inside a monolingual run
        (e.g. 'I' or 'm' tagged 'fr' surrounded by 'en' tokens)
      - Loanwords absorbed into the dominant language
        (e.g. 'match' tagged 'en' surrounded by 'fr' tokens)
 
    Genuine multi-token switches survive because enough neighbours agree on
    the switched language, so the majority does not vote against them.
 
    Args:
        lang_ids:  list of per-token language strings, e.g. ["fr","fr","en","fr"]
        window:    number of non-punct neighbours to collect on each side (default 2)
        threshold: minimum fraction of neighbours that must agree to trigger an
                   override (default 0.65)
 
    Returns:
        smoothed list of language strings, same length as lang_ids
    """
    smoothed = lang_ids[:]
    n = len(lang_ids)

    for i, lang in enumerate(lang_ids):
        if lang == "punct":
            continue
        if i in confirmed:
            continue

        # Collect up to `window` non-punct neighbours on each side
        left_neighbors = []
        right_neighbors = []

        count, j = 0, i - 1
        while j >= 0 and count < window:
            if lang_ids[j] != "punct":
                left_neighbors.append(smoothed[j])
                count += 1
            j -= 1

        count, j = 0, i + 1
        while j < n and count < window:
            if lang_ids[j] != "punct":
                right_neighbors.append(smoothed[j])
                count += 1
            j += 1

        neighbors = left_neighbors + right_neighbors

        if not neighbors:
            continue

        top_lang, top_count = Counter(neighbors).most_common(1)[0]

        if top_lang != lang and top_count / len(neighbors) >= threshold:
            # Clear majority — override
            smoothed[i] = top_lang

        elif left_neighbors and right_neighbors:
            # Tie / no majority — token sits at a boundary
            # Use the immediately preceding neighbour's language
            left_lang = left_neighbors[0]   # closest left non-punct
            right_lang = right_neighbors[0]  # closest right non-punct
            if left_lang != right_lang:
                smoothed[i] = left_lang

    return smoothed

def tokenize_with_lang_mapping(text, tokenizer, language_pair):
    """
    Tokenize text and assign language IDs for subwords.
    Guarantees at most two languages per sequence.

    A smoothing pass is applied after initial detection to correct isolated
    misdetections and loanwords without disrupting genuine switches.
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
    elif language_pair == "Korean-English":
        allowed_langs = {"ko", "en"}
    elif language_pair == "French-English":
        allowed_langs = {"fr", "en"}
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

    # Spanish uses word-level splitting for better accent-based detection.
    # French is similar (Romance, space-delimited) so apply the same strategy.
    if language_pair in ("Spanish-English", "French-English"):
        words = text.split()

        for word in words:
            word_lang = clamp_lang(detect_word_lang(word, language_pair))

            sub_tokens = tokenizer.tokenize(word)
            tokens.extend(sub_tokens)

            for sub in sub_tokens:
                sub_clean = sub.strip().lstrip('▁').lower()

                if is_punctuation(sub):
                    lang_ids.append("punct")

                elif is_number(sub):
                    lang_ids.append(lang_ids[-1] if lang_ids else word_lang)

                elif sub_clean in hardcode_english:
                    # subword is itself a hardcoded English token (e.g. "i", "m" from "I'm")
                    lang_ids.append("en")

                else:
                    lang_ids.append(word_lang)
    else:
        # Script-based languages (Chinese, Hindi, Arabic, Korean) tokenize directly —
        # the script heuristic is reliable at the subword level.
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
    
    # Build set of indices confirmed by heuristic for french-english — these are never overridden
    if language_pair == "French-English":
        confirmed = set()
        for i, tok in enumerate(tokens):
            word = tok.strip().lstrip('▁').lower()
            if word in hardcode_english or is_french(word) or word in french_stopwords:
                confirmed.add(i)
        lang_ids = smooth_lang_ids(lang_ids, confirmed)


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