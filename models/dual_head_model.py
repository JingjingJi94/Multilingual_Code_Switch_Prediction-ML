import torch.nn as nn
from transformers import AutoModel


class DualHeadCausalModel(nn.Module):

    def __init__(
        self,
        backbone_name="xlm-roberta-base",
        num_duration_classes=3
    ):
        super().__init__()

        # Transformer backbone
        self.encoder = AutoModel.from_pretrained(backbone_name)
        # count of numbers are used to represent each token’s hidden state after passing through the transformer.
        hidden_size = self.encoder.config.hidden_size

        # Switch prediction head - binary
        self.switch_head = nn.Linear(hidden_size, 2)

        # Duration prediction head - 3 bins
        self.duration_head = nn.Linear(hidden_size, num_duration_classes)

    # input -> predictions
    def forward(self, input_ids, attention_mask):

        # send batch of windows into transformer backbone with dimension (B for batch size, N for window length)
        outputs = self.encoder(
            input_ids=input_ids,
            attention_mask=attention_mask
        )
        # extract the hidden states produced by the final transformer layer
        # shape: (B, N, H)
        hidden_states = outputs.last_hidden_state

        # select the hidden state of the last token in each window in all batches = position t
        # last token’s representation contains contextual information from the entire prefix of the window
        h_t = hidden_states[:, -1, :]
        # shape: (B, H)

        # switch_logits = W_switch * h_t + b_switch, shape: (B, 2)
        switch_logits = self.switch_head(h_t)

        # duration_logits = W_duration * h_t + b_duration, shape: (B, 3)
        duration_logits = self.duration_head(h_t)

        return switch_logits, duration_logits