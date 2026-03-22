import pickle
import random
from collections import Counter
from dataclasses import dataclass
from typing import Any, Dict, List

from transformers import AutoTokenizer
from torch.utils.data import DataLoader

from .streaming_dataloader import SwitchLinguaStreamDataset


@dataclass
class DataBundle:
    entries: List[Dict[str, Any]]          # sequence-level
    tokenizer: Any
    dataset: SwitchLinguaStreamDataset     # window-level
    loader: DataLoader


def load_dataset(
    data_file: str,
    model_name: str = "xlm-roberta-base",
    window_size: int = 64,
    batch_size: int = 8,
    shuffle: bool = True,
    pin_memory: bool = False,
) -> DataBundle:
    """
    Load preprocessed pickle -> cleaned entries -> SwitchLinguaStreamDataset -> DataLoader.

    Notes:
    - entries: sequence-level dicts from df['preprocessed']
    - dataset: window-level samples from entries
    """
    with open(data_file, "rb") as f:
        entries = pickle.load(f)

    if not isinstance(entries, list):
        raise ValueError(f"Expected a list of dicts, got {type(entries)}")

    required_keys = {"tokens", "lang_ids", "ysw", "ydur", "input_ids"}
    missing = sum(1 for e in entries if not required_keys.issubset(e.keys()))
    if missing:
        print(f"[load][WARN] {missing} entries missing some required keys {required_keys}.")

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    ds = SwitchLinguaStreamDataset(entries, tokenizer=tokenizer, window_size=window_size)

    loader = DataLoader(
        ds,
        batch_size=batch_size,
        shuffle=shuffle,
        pin_memory=pin_memory,
    )

    # quick shape check
    batch = next(iter(loader))
    input_ids, language_ids, attention_mask, ysw, ydur = batch
    print(
        "[load] batch shapes:",
        input_ids.shape,
        language_ids.shape,
        attention_mask.shape,
        ysw.shape,
        ydur.shape,
    )

    return DataBundle(entries=entries, tokenizer=tokenizer, dataset=ds, loader=loader)


def inspect_sample(
    ds: SwitchLinguaStreamDataset,
    tokenizer: Any,
    i: int,
    lang_pad_id: int = -1,
    show_last_k: int = 20,
) -> None:
    """
    Print a human-readable debug view of a single window-level sample ds[i].
    """
    if i < 0 or i >= len(ds):
        raise IndexError(f"i={i} out of range (0..{len(ds)-1})")

    x_ids, x_lang, attention_mask, y_sw, y_dur = ds[i]

    x_ids_list = x_ids.tolist()
    x_lang_list = x_lang.tolist()
    attn_list = attention_mask.tolist()
    y_sw = int(y_sw)
    y_dur = int(y_dur)

    unique_ids = len(set(x_ids_list))
    pad_id = tokenizer.pad_token_id

    token_pad_ratio = 1.0 - (sum(attn_list) / len(attn_list))
    lang_pad_ratio = sum(1 for v in x_lang_list if v == lang_pad_id) / len(x_lang_list)

    print(f"\n=== sample i={i} | ysw={y_sw} | ydur={y_dur} ===")
    print("input_ids shape:", getattr(x_ids, "shape", None))
    print("lang_ids shape:", getattr(x_lang, "shape", None))
    print("attention_mask shape:", getattr(attention_mask, "shape", None))
    print("unique ids:", unique_ids)
    print(f"pad_token_id: {pad_id} | token_pad_ratio: {token_pad_ratio:.3f} | lang_pad_ratio: {lang_pad_ratio:.3f}")

    tail_ids = x_ids_list[-show_last_k:]
    tail_lang = x_lang_list[-show_last_k:]
    tail_attn = attn_list[-show_last_k:]

    print(f"last {show_last_k} ids:", tail_ids)
    print(f"last {show_last_k} lang:", tail_lang)
    print(f"last {show_last_k} attention_mask:", tail_attn)
    print("valid tokens by mask:", sum(attn_list), "/", len(attn_list))

    print("decoded(no-skip):", tokenizer.decode(x_ids_list, skip_special_tokens=False))
    print("decoded(skip):", tokenizer.decode(x_ids_list, skip_special_tokens=True))

    try:
        print("last id token:", tokenizer.convert_ids_to_tokens([x_ids_list[-1]]))
    except Exception:
        pass


def dataset_stats(
    ds: SwitchLinguaStreamDataset,
    sample_n: int = 5000,
    lang_pad_id: int = -1,
) -> Dict[str, Any]:
    """
    Return quick stats for baseline/constraint folks:
    - switch rate
    - ydur distribution (valid only)
    - avg padding ratios
    """
    n = len(ds)
    k = min(sample_n, n)
    idxs = [random.randrange(n) for _ in range(k)]

    sw_cnt = 0
    ydur_counter = Counter()
    token_pad_ratios = []
    lang_pad_ratios = []

    for i in idxs:
        x_ids, x_lang, attention_mask, y_sw, y_dur = ds[i]
        y_sw = int(y_sw)
        y_dur = int(y_dur)

        sw_cnt += y_sw
        if y_dur != -1:
            ydur_counter[y_dur] += 1

        lang = x_lang.tolist()
        attn = attention_mask.tolist()

        lang_pad_ratios.append(sum(1 for v in lang if v == lang_pad_id) / len(lang))
        token_pad_ratios.append(1.0 - sum(attn) / len(attn))

    stats = {
        "num_windows": n,
        "sampled": k,
        "switch_rate": sw_cnt / k,
        "ydur_valid_rate": (sum(ydur_counter.values()) / k),
        "ydur_top10": ydur_counter.most_common(10),
        "avg_lang_pad_ratio": sum(lang_pad_ratios) / len(lang_pad_ratios),
        "avg_token_pad_ratio": sum(token_pad_ratios) / len(token_pad_ratios),
    }

    print("\n[stats]")
    for key, val in stats.items():
        print(f"  {key}: {val}")

    return stats


def find_and_inspect_switch_samples(ds, tokenizer, max_find=5, scan_limit=200000, K=12):
    found = 0
    for i in range(min(len(ds), scan_limit)):
        x_ids, x_lang, attention_mask, y_sw, y_dur = ds[i]
        if int(y_sw) == 1:
            ids = x_ids.tolist()
            lang = x_lang.tolist()
            attn = attention_mask.tolist()

            tail = [v for v in lang[-K:] if v != -1]
            print(f"\n[SWITCH i={i}] ydur={int(y_dur)} tail_lang={tail}")
            print("tail attention_mask:", attn[-K:])
            print("decoded:", tokenizer.decode(ids, skip_special_tokens=True)[:220])

            found += 1
            if found >= max_find:
                break
    print(f"found {found} switch samples")


def demo(data_file: str = "./data_preprocess/preprocessed_data.pkl") -> None:
    bundle = load_dataset(data_file=data_file)

    ds = bundle.dataset
    tok = bundle.tokenizer

    indices = [0, 100, 1000, len(ds) // 2, len(ds) - 1, random.randint(0, len(ds) - 1)]
    for i in indices:
        inspect_sample(ds, tok, i)

    dataset_stats(ds, sample_n=3000)
    find_and_inspect_switch_samples(ds, tok)


demo()