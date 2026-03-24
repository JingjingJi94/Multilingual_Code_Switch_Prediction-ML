from __future__ import annotations

from dataclasses import dataclass
import random
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

    Input sequence format (from ./data_preprocess/preprocessed_data.pkl):
        {
            "original_text": str,
            "tokens": List[str],   # subword tokens
            "input_ids": List[int]
            "lang_ids": List[str], # token-level language tags aligned to tokens (e.g., "en", "es")
            "ysw": List[int],      # switch labels per position t (predicts t+1 switch)
            "ydur": List[int],     # duration labels per position t (predicts upcoming segment length), -1 if not switch
        }

    Each example corresponds to a position t in a sequence (0 <= t <= L-2 by default),
    and yields a fixed-length left-padded context window [x(t-N+1), ..., x(t)] where N=window_size.

    Output:
        (input_token_ids, language_ids, attention_mask, ysw_label, ydur_label)

    Shapes:
        input_token_ids: (N,)
        language_ids:    (N,)
        attention_mask:  (N,)   # 1 for real tokens, 0 for padding
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
        sample_rate=1.0,
        lang2id: Optional[Dict[str, int]] = None,
        pad_token_id: Optional[int] = None,
        pad_lang_id: int = -1,
        drop_last_token: bool = True,
        enforce_equal_lengths: bool = True,
    ) -> None:
        if window_size <= 0:
            raise ValueError("window_size must be > 0")
        if tokenizer is None:
            raise ValueError("tokenizer is required.")

        self.tokenizer = tokenizer
        self.window_size = window_size
        self.sample_rate = sample_rate
        self.pad_lang_id = pad_lang_id
        self.drop_last_token = drop_last_token
        self.enforce_equal_lengths = enforce_equal_lengths

        if pad_token_id is None:
            pad_token_id = getattr(tokenizer, "pad_token_id", None)
            if pad_token_id is None:
                pad_token_id = 0
        self.pad_token_id = int(pad_token_id)

        self.lang2id = lang2id or self._build_lang2id(sequences)

        self._seqs: List[Dict[str, torch.Tensor]] = []
        self._all_indices: List[StreamSampleIndex] = []

        for i, seq in enumerate(sequences):
            tokens = seq.get("tokens")
            input_ids = seq.get("input_ids")
            langs = seq.get("lang_ids")
            ysw = seq.get("ysw")
            ydur = seq.get("ydur")

            if tokens is None or input_ids is None or langs is None or ysw is None or ydur is None:
                raise ValueError(f"Seq {i}: missing required fields among tokens/input_ids/lang_ids/ysw/ydur")

            if enforce_equal_lengths:
                if not (len(tokens) == len(input_ids) == len(langs) == len(ysw) == len(ydur)):
                    raise ValueError(
                        f"Seq {i}: length mismatch: "
                        f"tokens={len(tokens)}, input_ids={len(input_ids)}, "
                        f"lang_ids={len(langs)}, ysw={len(ysw)}, ydur={len(ydur)}"
                    )
            else:
                if len(tokens) != len(langs):
                    raise ValueError(f"Seq {i}: tokens length {len(tokens)} != lang_ids length {len(langs)}")

            L = len(tokens)
            if drop_last_token and L < 2:
                continue

            try:
                language_ids = [self.lang2id[x] for x in langs]
            except KeyError as e:
                raise ValueError(f"Seq {i}: unknown lang tag {e}. Provide lang2id covering all tags.") from e

            ysw_t = torch.tensor(ysw, dtype=torch.long)
            ydur_t = torch.tensor(ydur, dtype=torch.long)

            self._seqs.append(
                {
                    "input_ids": torch.tensor(input_ids, dtype=torch.long),
                    "language_ids": torch.tensor(language_ids, dtype=torch.long),
                    "ysw": ysw_t,
                    "ydur": ydur_t,
                }
            )

            seq_idx = len(self._seqs) - 1  # dense index into _seqs, not the raw loop index i
            max_t = (L - 2) if drop_last_token else (L - 1)
            for t in range(0, max_t + 1):
                self._all_indices.append(StreamSampleIndex(seq_idx=seq_idx, t=t))

        self._index: List[StreamSampleIndex] = []
        self.resample()

    def resample(self) -> None:
        """Draw a fresh random subset of positions (sample_rate fraction of all positions).
        Call at the end of each training epoch for dynamic sampling.
        When sample_rate == 1.0, uses all positions without random sampling."""
        if self.sample_rate >= 1.0:
            self._index = list(self._all_indices)
        else:
            k = max(1, int(len(self._all_indices) * self.sample_rate))
            self._index = random.sample(self._all_indices, k)

    @staticmethod
    def _build_lang2id(sequences: Sequence[Dict[str, Any]]) -> Dict[str, int]:
        """Build deterministic lang2id in order of first appearance."""
        lang2id: Dict[str, int] = {}
        for seq in sequences:
            for l in seq.get("lang_ids", []):
                if l not in lang2id:
                    lang2id[l] = len(lang2id)
        if not lang2id:
            lang2id = {"UNK": 0}
        return lang2id

    def __len__(self) -> int:
        return len(self._index)

    def __getitem__(
        self, idx: int
    ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, int, int]:
        meta = self._index[idx]
        seq = self._seqs[meta.seq_idx]
        t = meta.t

        input_ids: torch.Tensor = seq["input_ids"]
        language_ids: torch.Tensor = seq["language_ids"]
        ysw_label = int(seq["ysw"][t].item())
        ydur_label = int(seq["ydur"][t].item())

        # Build window [t-N+1 ... t]
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

        # Keep only most recent N if needed
        if win_tokens.numel() > self.window_size:
            win_tokens = win_tokens[-self.window_size :]
            win_langs = win_langs[-self.window_size :]

        # Safety pad
        if win_tokens.numel() < self.window_size:
            missing = self.window_size - win_tokens.numel()
            win_tokens = torch.cat(
                [torch.full((missing,), self.pad_token_id, dtype=torch.long), win_tokens], dim=0
            )
            win_langs = torch.cat(
                [torch.full((missing,), self.pad_lang_id, dtype=torch.long), win_langs], dim=0
            )

        # 1 = real token, 0 = padding
        attention_mask = (win_tokens != self.pad_token_id).long()

        return win_tokens, win_langs, attention_mask, ysw_label, ydur_label
