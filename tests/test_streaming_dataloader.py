# tests/test_streaming_dataloader.py
import pytest
import torch

from data.streaming_dataloader import SwitchLinguaStreamDataset


class DummyTokenizer:
    """
    Minimal tokenizer stub for tests.
    We assume tokens are already unique strings and map them deterministically.
    """
    pad_token_id = 0

    def __init__(self, vocab):
        self.vocab = vocab

    def convert_tokens_to_ids(self, tokens):
        return [self.vocab[t] for t in tokens]


def _make_dummy_entry():
    """
    Create a short token sequence with known switch points.

    tokens:   A  B  C  D  E
    lang:    en en es es en
    ysw(t):  0  1  0  1  X   (X is unused if drop_last_token=True)
    ydur(t): -1 0 -1 0  X

    Meaning:
      - at t=1, next token (t+1=2) switches to 'es', and the new segment length is 2 tokens (C,D) => small bin 0
      - at t=3, next token (t+1=4) switches to 'en', segment length is 1 token (E) => small bin 0
    """
    return {
        "original_text": "A B C D E",
        "tokens": ["A", "B", "C", "D", "E"],
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

    # L=5, valid t are 0..3 => 4 samples
    assert len(ds) == 4

    # t=0 window should be [PAD, PAD, PAD, A]
    input_ids, lang_ids, ysw, ydur = ds[0]
    assert input_ids.tolist() == [99, 99, 99, 10]
    assert lang_ids.tolist() == [-1, -1, -1, ds.lang2id["en"]]
    assert ysw == 0
    assert ydur == -1

    # t=1 window should be [PAD, PAD, A, B]
    input_ids, lang_ids, ysw, ydur = ds[1]
    assert input_ids.tolist() == [99, 99, 10, 11]
    assert ysw == 1
    assert ydur == 0


def test_no_future_leakage():
    """
    Core causal test: the window must end at token t and contain no token from t+1 onward.
    """
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

    # Map from sample index -> expected last token id
    # ds[0] is t=0 ends with A(10)
    # ds[1] is t=1 ends with B(11)
    # ds[2] is t=2 ends with C(12)
    # ds[3] is t=3 ends with D(13)
    expected_last = [10, 11, 12, 13]
    future_tokens_by_t = {
        0: {11, 12, 13, 14},  # future after A
        1: {12, 13, 14},      # future after B
        2: {13, 14},          # future after C
        3: {14},              # future after D
    }

    for sample_idx, last_id in enumerate(expected_last):
        input_ids, _, ysw, ydur = ds[sample_idx]
        # window ends at current token
        assert input_ids[-1].item() == last_id

        # no future token ids should appear in the window
        leaked = future_tokens_by_t[sample_idx].intersection(set(input_ids.tolist()))
        assert leaked == set(), f"Leakage detected at sample {sample_idx}: {leaked}"


def test_label_alignment():
    """
    Verify returned ysw/ydur equals original labels at position t.
    """
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

    # sample idx corresponds to t (since only one sequence and we enumerate t=0..3)
    for t in range(4):
        _, _, ysw, ydur = ds[t]
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

    # each entry yields 4 samples => total 8
    assert len(ds) == 8

    # last sample should still be well-formed
    input_ids, lang_ids, ysw, ydur = ds[-1]
    assert input_ids.numel() == 4
    assert lang_ids.numel() == 4
    assert isinstance(ysw, int)
    assert isinstance(ydur, int)