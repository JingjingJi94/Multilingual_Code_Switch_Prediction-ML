import torch.nn as nn
from transformers import AutoModel


class SingleHeadModel(nn.Module):

    def __init__(self, backbone_name="xlm-roberta-base"):
        super().__init__()
        self.encoder = AutoModel.from_pretrained(backbone_name)
        hidden_size = self.encoder.config.hidden_size
        self.switch_head = nn.Linear(hidden_size, 2)

    def forward(self, input_ids, attention_mask):
        outputs = self.encoder(input_ids=input_ids, attention_mask=attention_mask)
        h_t = outputs.last_hidden_state[:, -1, :]
        return self.switch_head(h_t)
