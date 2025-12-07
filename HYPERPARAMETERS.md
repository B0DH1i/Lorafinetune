# Hyperparameters Documentation

Complete documentation of all hyperparameters used in the DIVERSE dataset training.

## Model Configuration

### Base Model
```python
model_name = "Qwen/Qwen2.5-Coder-1.5B-Instruct"
```

- **Total Parameters**: 1,543,710,000 (1.54B)
- **Architecture**: Qwen2 (Transformer-based)
- **Precision**: BFloat16
- **Device**: CUDA (A100 GPU)

### LoRA Configuration

```python
lora_config = {
    "r": 32,                    # LoRA rank
    "lora_alpha": 64,           # LoRA alpha (scaling factor)
    "lora_dropout": 0.1,        # Dropout probability
    "target_modules": [
        "q_proj",               # Query projection
        "k_proj",               # Key projection
        "v_proj",               # Value projection
        "o_proj",               # Output projection
        "gate_proj",            # Gate projection (MLP)
        "up_proj",              # Up projection (MLP)
        "down_proj"             # Down projection (MLP)
    ],
    "bias": "none",             # No bias training
    "task_type": "CAUSAL_LM"    # Causal language modeling
}
```

**Trainable Parameters**: 36,929,536 (2.34% of total)

**LoRA Design Choices**:
- **Rank (r=32)**: Balanced between capacity and efficiency
- **Alpha (α=64)**: Set to 2×r for stable training
- **Dropout (0.1)**: Moderate regularization
- **Target Modules**: All attention and MLP layers for maximum adaptation

## Training Hyperparameters

### Optimization

```python
optimizer = "adamw_torch_fused"
learning_rate = 2e-4
weight_decay = 0.01
max_grad_norm = 1.0
```

**Optimizer Details**:
- **Type**: AdamW with fused implementation
- **Beta1**: 0.9 (default)
- **Beta2**: 0.999 (default)
- **Epsilon**: 1e-8 (default)
- **Fused**: True (faster on CUDA)

**Learning Rate**:
- **Initial**: 2e-4 (0.0002)
- **Schedule**: Cosine decay with warmup
- **Warmup Ratio**: 0.03 (3% of total steps)
- **Warmup Steps**: ~25 steps
- **Final LR**: ~5.3e-5 (at step 700)

**Gradient Clipping**:
- **Max Norm**: 1.0
- **Purpose**: Prevent gradient explosion

### Batch Configuration

```python
batch_size = 4
gradient_accumulation_steps = 4
effective_batch_size = 16  # batch_size × gradient_accumulation_steps
```

**Rationale**:
- Small batch size (4) for memory efficiency
- Gradient accumulation (4) for effective batch size of 16
- Effective batch size of 16 provides stable gradients

### Training Schedule

```python
num_epochs = 3
max_steps = 852  # Calculated from dataset size
early_stopping_patience = 2
```

**Epoch Calculation**:
- Training samples: 4,530
- Steps per epoch: 284 (4,530 / 16)
- Total planned steps: 852 (284 × 3)
- Actual steps: 700 (early stopped)

**Early Stopping**:
- **Patience**: 2 evaluation cycles
- **Metric**: Validation loss
- **Mode**: Minimize
- **Triggered**: After checkpoint-500

### Sequence Configuration

```python
max_length = 1024
padding = "max_length"
truncation = True
```

**Context Length**:
- **Max Length**: 1024 tokens
- **Rationale**: Sufficient for solution-only training
- **Padding**: All sequences padded to max length
- **Truncation**: Longer sequences truncated

### Logging and Checkpointing

```python
logging_steps = 20
eval_steps = 100
save_steps = 100
save_total_limit = None  # Save all checkpoints
```

**Logging Frequency**:
- **Training Loss**: Every 20 steps
- **Validation Loss**: Every 100 steps
- **Checkpoint Saving**: Every 100 steps

**Checkpoint Management**:
- All checkpoints saved (no limit)
- Best checkpoint tracked by validation loss

## System Configuration

### Mixed Precision

```python
bf16 = True
fp16 = False
```

**BFloat16 Training**:
- **Enabled**: True
- **Hardware**: A100 supports BF16 natively
- **Benefits**: Faster training, lower memory usage
- **Stability**: Better than FP16 for training

### Memory Optimization

```python
gradient_checkpointing = True
optim = "adamw_torch_fused"
```

**Gradient Checkpointing**:
- **Enabled**: True
- **Trade-off**: Slower training for lower memory usage
- **Necessary**: For fitting model on GPU

**Fused Optimizer**:
- **Type**: Fused AdamW
- **Benefit**: Faster optimizer step on CUDA

### Attention Configuration

```python
attn_implementation = "eager"  # Flash Attention 2 not available
```

**Attention Type**:
- **Implementation**: Eager (standard PyTorch)
- **Reason**: Flash Attention 2 not installed
- **Impact**: Slower but stable

## Dataset Configuration

### Data Processing

```python
system_prompt = "You are an expert Python programmer. Please read the problem carefully before writing any Python code."

training_field = "solution"  # Not "output" (reasoning)
```

**Prompt Format**:
```
{system_prompt}

Problem:
{input}

Solution:
{solution}
```

### Data Split

```python
train_split = "train"  # Filtered by split column
valid_split = "valid"  # Filtered by split column
test_split = "test"    # Filtered by split column
```

**Split Sizes**:
- Train: 4,530 samples (90.6%)
- Validation: 19 samples (0.4%)
- Test: 451 samples (9.0%)

**Split Method**:
- Pre-defined in dataset
- Filtered by `split` column
- No manual splitting required

## Evaluation Configuration

### Metrics

```python
metric_for_best_model = "eval_loss"
greater_is_better = False
load_best_model_at_end = True
```

**Evaluation Metrics**:
- **Primary**: Cross-entropy loss
- **Direction**: Lower is better
- **Best Model**: Loaded at end of training

### Evaluation Strategy

```python
eval_strategy = "steps"
eval_steps = 100
```

**Evaluation Frequency**:
- Every 100 training steps
- On validation set (19 samples)
- Used for early stopping and checkpoint selection

## Hardware Configuration

### GPU

```
Device: NVIDIA A100-SXM4-40GB
Memory: 40 GB
CUDA Version: 12.x
```

**Memory Usage**:
- Model: ~6 GB
- Optimizer States: ~12 GB
- Activations: ~7 GB
- Total: ~25 GB / 40 GB

### CPU

```
Platform: Linux (Google Colab)
CPU: Intel Xeon (exact model varies)
RAM: ~12 GB available
```

## Reproducibility Settings

### Random Seeds

```python
seed = 42  # Default transformers seed
dataset_split_seed = 42
```

**Seeded Components**:
- PyTorch random number generator
- NumPy random number generator
- Python random module
- Dataset shuffling

### Deterministic Operations

```python
torch.backends.cudnn.deterministic = False  # Default
torch.backends.cudnn.benchmark = True       # Default
```

**Note**: Full determinism not enforced for performance reasons.

## Summary Table

| Category | Parameter | Value |
|----------|-----------|-------|
| **Model** | Base Model | Qwen2.5-Coder-1.5B-Instruct |
| | Total Parameters | 1.54B |
| | Trainable Parameters | 36.9M (2.34%) |
| **LoRA** | Rank (r) | 32 |
| | Alpha (α) | 64 |
| | Dropout | 0.1 |
| | Target Modules | 7 (all attn + MLP) |
| **Optimization** | Optimizer | AdamW (fused) |
| | Learning Rate | 2e-4 |
| | LR Schedule | Cosine with warmup |
| | Warmup Ratio | 0.03 |
| | Weight Decay | 0.01 |
| | Gradient Clipping | 1.0 |
| **Batch** | Batch Size | 4 |
| | Gradient Accumulation | 4 |
| | Effective Batch Size | 16 |
| **Training** | Epochs | 3 (planned) |
| | Max Steps | 852 (planned) |
| | Actual Steps | 700 (early stopped) |
| | Early Stopping Patience | 2 |
| **Sequence** | Max Length | 1024 |
| | Padding | max_length |
| | Truncation | True |
| **Precision** | Mixed Precision | BF16 |
| | Gradient Checkpointing | Enabled |
| **Logging** | Train Log Steps | 20 |
| | Eval Steps | 100 |
| | Save Steps | 100 |
| **Dataset** | Train Samples | 4,530 |
| | Validation Samples | 19 |
| | Test Samples | 451 |
| **Hardware** | GPU | A100-SXM4-40GB |
| | Memory Used | ~25 GB / 40 GB |

## Hyperparameter Choices Rationale

### Why These Values?

1. **Learning Rate (2e-4)**:
   - Standard for LoRA fine-tuning
   - Higher than full fine-tuning (typically 1e-5)
   - Allows faster adaptation with LoRA

2. **LoRA Rank (32)**:
   - Balanced between capacity and efficiency
   - Sufficient for code generation tasks
   - Could increase to 64 for more capacity

3. **Batch Size (4) + Accumulation (4)**:
   - Memory efficient on A100
   - Effective batch size of 16 is standard
   - Stable gradient estimates

4. **Max Length (1024)**:
   - Sufficient for solution-only training
   - Most solutions fit within this limit
   - Would need 8192 for reasoning training

5. **Early Stopping (Patience=2)**:
   - Prevents overfitting
   - 2 evaluation cycles = 200 steps
   - Successfully stopped at optimal point

## Alternative Configurations

### For Better Performance

```python
# Higher capacity
lora_r = 64
lora_alpha = 128

# More stable training
learning_rate = 1e-4
warmup_ratio = 0.05

# More epochs
num_epochs = 4
```

### For Reasoning Training

```python
# Longer context
max_length = 8192

# Smaller batch for memory
batch_size = 2
gradient_accumulation_steps = 8

# Use output field
training_field = "output"
```

### For Faster Training

```python
# Flash Attention 2
attn_implementation = "flash_attention_2"

# Larger batch
batch_size = 8
gradient_accumulation_steps = 2

# Fewer checkpoints
save_steps = 200
```

---

**Document Version**: 1.0  
**Last Updated**: December 7, 2024  
**Training Date**: December 7, 2024
