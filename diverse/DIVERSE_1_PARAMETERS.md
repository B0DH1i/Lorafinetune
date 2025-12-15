# Training Parameters - DIVERSE Dataset

## LoRA Configuration

| Parameter | Value | Description |
|-----------|-------|-------------|
| **Rank (r)** | 32 | LoRA rank - adaptation capacity |
| **Alpha (α)** | 64 | Scaling factor (2 × rank) |
| **Dropout** | 0.1 | Regularization |
| **Target Modules** | 7 layers | q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj |

**Trainable Parameters**: 36.9M (2.34% of 1.54B total)

## Training Configuration

| Parameter | Value |
|-----------|-------|
| **Learning Rate** | 2e-4 (0.0002) |
| **LR Schedule** | Cosine with warmup |
| **Warmup Ratio** | 0.03 (3%) |
| **Optimizer** | AdamW (fused) |
| **Weight Decay** | 0.01 |
| **Gradient Clipping** | 1.0 |

## Batch Configuration

| Parameter | Value |
|-----------|-------|
| **Batch Size** | 4 |
| **Gradient Accumulation** | 4 steps |
| **Effective Batch Size** | 16 |

## Training Schedule

| Parameter | Value |
|-----------|-------|
| **Epochs** | 3 (planned) |
| **Total Steps** | 700 (early stopped) |
| **Early Stopping Patience** | 2 |

## Data Configuration

| Parameter | Value |
|-----------|-------|
| **Max Sequence Length** | 1024 tokens |
| **Training Field** | `solution` (code only) |
| **Padding** | max_length |
| **Truncation** | Enabled |

## System Configuration

| Parameter | Value |
|-----------|-------|
| **Mixed Precision** | BF16 |
| **Gradient Checkpointing** | Enabled |
| **GPU** | NVIDIA A100-SXM4-40GB |
| **Training Time** | ~32 minutes |

## System Prompt

```
You are an expert Python programmer. Please read the problem carefully before writing any Python code.
```

---

**Model**: Qwen2.5-Coder-1.5B-Instruct  
**Dataset**: CodeGen-Diverse-5K  
**Training Date**: December 7, 2024
