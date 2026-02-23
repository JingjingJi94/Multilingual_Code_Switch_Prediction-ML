# data/streaming_dataloader.py
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Sequence, Tuple

import torch
from torch.utils.data import Dataset


@dataclass(frozen=True)
class StreamSampleIndex:
    """Maps a global dataset index -> (sequence_idx, t)."""
    seq_idx: int
    t: int  # position in the original sequence; label at t predicts token t+1


class SwitchLinguaStreamDataset(Dataset):
    """
    Streaming (prefix-only) dataset for next-token code-switch prediction.

    Input sequence format (from df_preprocessed.pkl 'preprocessed' column):
        {
            "original_text": str,
            "tokens": List[str],   # subword tokens
            "lang_ids": List[str], # token-level language tags aligned to tokens (e.g., "en", "es")
            "ysw": List[int],      # switch labels per position t (predicts t+1 switch)
            "ydur": List[int],     # duration labels per position t (predicts upcoming segment length), -1 if not switch
        }

    Each example corresponds to a position t in a sequence (0 <= t <= L-2 by default),
    and yields a fixed-length left-padded context window [x(t-N+1), ..., x(t)] where N=window_size.

    Output:
        (input_token_ids, language_ids, ysw_label, ydur_label)

    Shapes:
        input_token_ids: (N,)
        language_ids:    (N,)
        ysw_label:       int scalar
        ydur_label:      int scalar

    No leakage guarantee:
        Window ends at token t (never includes t+1 or beyond).
    """

    def __init__(
        self,
        sequences: Sequence[Dict[str, Any]],
        tokenizer: Any,
        window_size: int = 64,
        lang2id: Optional[Dict[str, int]] = None,
        pad_token_id: Optional[int] = None,
        pad_lang_id: int = -1,
        drop_last_token: bool = True,
        enforce_equal_lengths: bool = True,
    ) -> None:
        """
        Args:
            sequences: list of preprocessed entries
            tokenizer: tokenizer that supports convert_tokens_to_ids(List[str]) -> List[int]
                      (e.g., transformers AutoTokenizer)
            window_size: context window length N
            lang2id: mapping for lang tag strings -> int ids. If None, will be built from data.
            pad_token_id: token padding id; if None, tries tokenizer.pad_token_id, else 0
            pad_lang_id: padding id for language_ids (usually -1)
            drop_last_token: if True, only create samples for t in [0..L-2] so t+1 exists
            enforce_equal_lengths: if True, require tokens/lang_ids/ysw/ydur to have exactly same length
        """
        if window_size <= 0:
            raise ValueError("window_size must be > 0")
        if tokenizer is None:
            raise ValueError("tokenizer is required (needs convert_tokens_to_ids).")

        self.tokenizer = tokenizer
        self.window_size = window_size
        self.pad_lang_id = pad_lang_id
        self.drop_last_token = drop_last_token
        self.enforce_equal_lengths = enforce_equal_lengths

        if pad_token_id is None:
            pad_token_id = getattr(tokenizer, "pad_token_id", None)
            if pad_token_id is None:
                pad_token_id = 0
        self.pad_token_id = int(pad_token_id)

        # Build lang2id if not provided
        self.lang2id = lang2id or self._build_lang2id(sequences)

        # Internal storage (converted to tensors)
        self._seqs: List[Dict[str, torch.Tensor]] = []
        self._index: List[StreamSampleIndex] = []

        for i, seq in enumerate(sequences):
            tokens = seq.get("tokens")
            langs = seq.get("lang_ids")
            ysw = seq.get("ysw")
            ydur = seq.get("ydur")

            if tokens is None or langs is None or ysw is None or ydur is None:
                raise ValueError(f"Seq {i}: missing required fields among tokens/lang_ids/ysw/ydur")

            if enforce_equal_lengths:
                if not (len(tokens) == len(langs) == len(ysw) == len(ydur)):
                    raise ValueError(
                        f"Seq {i}: length mismatch: "
                        f"tokens={len(tokens)}, lang_ids={len(langs)}, ysw={len(ysw)}, ydur={len(ydur)}"
                    )
            else:
                # still require at least token/lang alignment
                if len(tokens) != len(langs):
                    raise ValueError(f"Seq {i}: tokens length {len(tokens)} != lang_ids length {len(langs)}")

            L = len(tokens)
            if drop_last_token and L < 2:
                # no valid next-token prediction
                continue

            # Convert tokens -> ids
            input_ids = self._tokens_to_ids(tokens, seq_idx=i)

            # Convert lang tags -> ints
            try:
                language_ids = [self.lang2id[x] for x in langs]
            except KeyError as e:
                raise ValueError(f"Seq {i}: unknown lang tag {e}. Provide lang2id covering all tags.") from e

            # Convert labels to tensors
            ysw_t = torch.tensor(ysw, dtype=torch.long)
            ydur_t = torch.tensor(ydur, dtype=torch.long)

            if enforce_equal_lengths:
                if len(input_ids) != L or len(language_ids) != L:
                    raise ValueError(f"Seq {i}: conversion mismatch, got input_ids={len(input_ids)}, L={L}")

            self._seqs.append(
                {
                    "input_ids": torch.tensor(input_ids, dtype=torch.long),
                    "language_ids": torch.tensor(language_ids, dtype=torch.long),
                    "ysw": ysw_t,
                    "ydur": ydur_t,
                }
            )

            max_t = (L - 2) if drop_last_token else (L - 1)
            for t in range(0, max_t + 1):
                self._index.append(StreamSampleIndex(seq_idx=i, t=t))

    @staticmethod
    def _build_lang2id(sequences: Sequence[Dict[str, Any]]) -> Dict[str, int]:
        """Build deterministic lang2id in order of first appearance."""
        lang2id: Dict[str, int] = {}
        for seq in sequences:
            for l in seq.get("lang_ids", []):
                if l not in lang2id:
                    lang2id[l] = len(lang2id)
        if not lang2id:
            # fallback, though in practice you should always have language tags
            lang2id = {"UNK": 0}
        return lang2id

    def _tokens_to_ids(self, tokens: List[str], seq_idx: int) -> List[int]:
        ids = self.tokenizer.convert_tokens_to_ids(tokens)
        # Some tokenizers may return None for unknowns; guard
        if any(x is None for x in ids):
            bad_positions = [j for j, x in enumerate(ids) if x is None][:5]
            raise ValueError(
                f"Seq {seq_idx}: tokenizer returned None for some tokens at positions {bad_positions}. "
                f"Check tokenizer vocab / tokenization consistency."
            )
        return [int(x) for x in ids]

    def __len__(self) -> int:
        return len(self._index)

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor, int, int]:
        meta = self._index[idx]
        seq = self._seqs[meta.seq_idx]
        t = meta.t

        input_ids: torch.Tensor = seq["input_ids"]
        language_ids: torch.Tensor = seq["language_ids"]
        ysw_label = int(seq["ysw"][t].item())
        ydur_label = int(seq["ydur"][t].item())

        # Build window [t-N+1 ... t] (end-exclusive slice is t+1)
        start = t - self.window_size + 1
        end = t + 1

        if start >= 0:
            win_tokens = input_ids[start:end]
            win_langs = language_ids[start:end]
            pad_len = 0
        else:
            pad_len = -start
            win_tokens = input_ids[0:end]
            win_langs = language_ids[0:end]

        # Left pad to fixed length N
        if pad_len > 0:
            pad_tokens = torch.full((pad_len,), self.pad_token_id, dtype=torch.long)
            pad_langs = torch.full((pad_len,), self.pad_lang_id, dtype=torch.long)
            win_tokens = torch.cat([pad_tokens, win_tokens], dim=0)
            win_langs = torch.cat([pad_langs, win_langs], dim=0)

        # If longer than window, keep the most recent N tokens
        if win_tokens.numel() > self.window_size:
            win_tokens = win_tokens[-self.window_size :]
            win_langs = win_langs[-self.window_size :]

        # If still shorter, pad (shouldn't happen, but guard)
        if win_tokens.numel() < self.window_size:
            missing = self.window_size - win_tokens.numel()
            win_tokens = torch.cat(
                [torch.full((missing,), self.pad_token_id, dtype=torch.long), win_tokens], dim=0
            )
            win_langs = torch.cat(
                [torch.full((missing,), self.pad_lang_id, dtype=torch.long), win_langs], dim=0
            )

        return win_tokens, win_langs, ysw_label, ydur_label