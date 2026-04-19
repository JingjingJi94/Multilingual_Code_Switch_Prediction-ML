# Switch Prediction: Softmax + Threshold 优化方案

## 背景

`dual_head_model.py` 中 switch prediction head 定义如下：

```python
self.switch_head = nn.Linear(hidden_size, 2)
```

输出 2 个原始 logits，范围 (-∞, +∞)，分别对应 class 0（不切换）和 class 1（切换）。

## 当前 evaluate.py 的做法

```python
switch_logits, dur_logits = model(ids_tensor, attn_mask)
sw_pred = int(switch_logits.argmax(dim=-1).item())
```

直接对 logits 做 `argmax`，选值更大的索引作为预测结果。

- `logits[0] > logits[1]` → predict **0**（不切换）
- `logits[1] > logits[0]` → predict **1**（切换）

## 问题

没有 softmax，无法调节决策阈值，precision / recall 无法灵活权衡。

## 优化方案

加 softmax 后用可调阈值替代 argmax：

```python
SWITCH_THRESHOLD = 0.5  # 可调节

switch_logits, dur_logits = model(ids_tensor, attn_mask)
sw_prob = F.softmax(switch_logits, dim=-1)[0, 1].item()  # class 1 的概率，范围 (0, 1)
sw_pred = int(sw_prob > SWITCH_THRESHOLD)
dur_pred = int(dur_logits.argmax(dim=-1).item())  # dur 是多分类，保持 argmax
```

## 阈值对指标的影响

| 阈值 | 预测 1 的频率 | Precision | Recall | F1 |
|------|-------------|-----------|--------|----|
| 调低（如 0.3） | 更多 | 下降 | 上升 | 可能下降 |
| 0.5（默认） | 中等 | 平衡 | 平衡 | 基准 |
| 调高（如 0.7） | 更少 | 上升 | 下降 | 可能上升 |

F1 = 2 × P × R / (P + R)，当 P ≈ R 时 F1 最高。

## 当前测试集表现及调整建议

当前指标：**Precision = 0.49，Recall = 0.80，F1 = 0.59**

问题：模型过度预测 class 1（切换点），recall 虚高，precision 偏低。

**建议：调高阈值（0.5 → 0.6～0.7）**，减少误报，使 P 和 R 更接近。

| 阈值 | 预期效果 |
|------|---------|
| 0.55 | P 小幅上升，R 小幅下降，F1 略有改善 |
| 0.60 | P 明显上升，R 下降，F1 改善较明显 |
| 0.65～0.70 | P 接近 R，F1 达到最优区间 |

**F1 能提升多少？**

当前 P=0.49 和 R=0.80 差距很大，理论上 F1 存在较大提升空间。若调整后 P ≈ R ≈ 0.63，则：

```
F1 = 2 × 0.63 × 0.63 / (0.63 + 0.63) ≈ 0.63
```

粗略估计 F1 可从 **0.59 提升到 0.62～0.65**，具体数值需在验证集上扫描阈值确定。

**推荐做法**：在验证集上遍历阈值（如 0.5～0.8，步长 0.05），画出 P-R 曲线，选 F1 最高的阈值，再在测试集上评估。

## 注意

- `argmax` 和 softmax 后 `argmax` **结果永远一致**（softmax 不改变大小顺序），默认阈值 0.5 时两种写法等价
- 只有当阈值不是 0.5 时才有实质差异
- `ydur`（duration）是多分类任务，不适用此方案，保持 `argmax` 即可
