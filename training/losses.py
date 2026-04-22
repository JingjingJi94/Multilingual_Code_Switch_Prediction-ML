import torch
import torch.nn as nn
from typing import Optional

class MultiTaskLoss(nn.Module):
    def __init__(
        self,
        lambda_sw=1.0,
        lambda_dur=1.0,
        detach_dur=False,
        sw_weight: Optional[torch.Tensor] = None,
    ):
        super().__init__()
        self.lambda_sw = lambda_sw
        self.lambda_dur = lambda_dur
        self.detach_dur = detach_dur
        self.switch_loss_fn = nn.CrossEntropyLoss(weight=sw_weight)
        self.duration_loss_fn = nn.CrossEntropyLoss(ignore_index=-1)

    def forward(self, switch_logits, duration_logits, ysw, ydur):
        # Switch loss (always computed)
        L_sw = self.switch_loss_fn(switch_logits, ysw)

        # Duration loss (skip invalid targets)
        valid_mask = (ydur != -1)
        if valid_mask.sum() > 0:
            L_dur = self.duration_loss_fn(duration_logits[valid_mask], ydur[valid_mask])
            if self.detach_dur:
                L_dur = L_dur.detach()
        else:
            L_dur = torch.tensor(0., device=ydur.device)

        # Weighted total loss
        L_total = self.lambda_sw * L_sw + self.lambda_dur * L_dur
        return L_total, L_sw, L_dur