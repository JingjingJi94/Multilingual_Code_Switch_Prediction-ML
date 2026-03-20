# tests/test_streaming_dataloader.py
import pytest
import torch

from data.streaming_dataloader import SwitchLinguaStreamDataset


class DummyTokenizer:
    pad_token_id = 0

    def __init__(self, vocab):
        self.vocab = vocab

    def convert_tokens_to_ids(self, tokens):
        return [self.vocab[t] for t in tokens]


def _make_dummy_entry():
    return {
        "original_text": "A B C D E",
        "tokens": ["A", "B", "C", "D", "E"],
        "input_ids": [10, 11, 12, 13, 14],   # 这里要补上
        "lang_ids": ["en", "en", "es", "es", "en"],
        "ysw": [0, 1, 0, 1, 0],
        "ydur": [-1, 0, -1, 0, -1],
    }


def test_padding_and_window_shape():
    entry = _make_dummy_entry()
    tok = DummyTokenizer(vocab={"A": 10, "B": 11, "C": 12, "D": 13, "E": 14})
    ds = SwitchLinguaStreamDataset(
        [entry],
        tokenizer=tok,
        window_size=4,
        pad_token_id=99,
        pad_lang_id=-1,
        drop_last_token=True,
    )

    assert len(ds) == 4

    input_ids, lang_ids, attention_mask, ysw, ydur = ds[0]
    assert input_ids.tolist() == [99, 99, 99, 10]
    assert lang_ids.tolist() == [-1, -1, -1, ds.lang2id["en"]]
    assert attention_mask.tolist() == [0, 0, 0, 1]
    assert ysw == 0
    assert ydur == -1

    input_ids, lang_ids, attention_mask, ysw, ydur = ds[1]
    assert input_ids.tolist() == [99, 99, 10, 11]
    assert attention_mask.tolist() == [0, 0, 1, 1]
    assert ysw == 1
    assert ydur == 0


def test_no_future_leakage():
    entry = _make_dummy_entry()
    tok = DummyTokenizer(vocab={"A": 10, "B": 11, "C": 12, "D": 13, "E": 14})
    ds = SwitchLinguaStreamDataset(
        [entry],
        tokenizer=tok,
        window_size=4,
        pad_token_id=99,
        pad_lang_id=-1,
        drop_last_token=True,
    )

    expected_last = [10, 11, 12, 13]
    future_tokens_by_t = {
        0: {11, 12, 13, 14},
        1: {12, 13, 14},
        2: {13, 14},
        3: {14},
    }

    for sample_idx, last_id in enumerate(expected_last):
        input_ids, _, attention_mask, ysw, ydur = ds[sample_idx]
        assert input_ids[-1].item() == last_id

        leaked = future_tokens_by_t[sample_idx].intersection(set(input_ids.tolist()))
        assert leaked == set(), f"Leakage detected at sample {sample_idx}: {leaked}"


def test_label_alignment():
    entry = _make_dummy_entry()
    tok = DummyTokenizer(vocab={"A": 10, "B": 11, "C": 12, "D": 13, "E": 14})
    ds = SwitchLinguaStreamDataset(
        [entry],
        tokenizer=tok,
        window_size=4,
        pad_token_id=99,
        pad_lang_id=-1,
        drop_last_token=True,
    )

    for t in range(4):
        _, _, _, ysw, ydur = ds[t]
        assert ysw == entry["ysw"][t]
        assert ydur == entry["ydur"][t]


def test_multiple_sequences_total_length():
    entry1 = _make_dummy_entry()
    entry2 = _make_dummy_entry()
    tok = DummyTokenizer(vocab={"A": 10, "B": 11, "C": 12, "D": 13, "E": 14})

    ds = SwitchLinguaStreamDataset(
        [entry1, entry2],
        tokenizer=tok,
        window_size=4,
        pad_token_id=99,
        pad_lang_id=-1,
        drop_last_token=True,
    )

    assert len(ds) == 8

    input_ids, lang_ids, attention_mask, ysw, ydur = ds[-1]
    assert input_ids.numel() == 4
    assert lang_ids.numel() == 4
    assert attention_mask.numel() == 4
    assert isinstance(ysw, int)
    assert isinstance(ydur, int)