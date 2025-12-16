# LoRA Fine-Tuning: DEEP Dataset

LoRA fine-tuning of Qwen2.5-Coder-1.5B-Instruct on DEEP-5K dataset for competitive code generation.

## Model
- **Base Model:** [Qwen/Qwen2.5-Coder-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct)
- **Dataset:** [DEEP-5K](https://huggingface.co/datasets/Naholav/CodeGen-Deep-5K)
- **Strategy:** Solution-only (code generation without reasoning)

## Dataset Split

- **Train:** 4,279 examples
- **Validation:** 226 examples
- **Test:** 480 examples
- **Total:** 4,985 examples

### Difficulty Distribution

| Difficulty | Train | Validation | Test |
|------------|-------|------------|------|
| 1 | 204 | 11 | 20 |
| 2 | 338 | 18 | 36 |
| 3 | 729 | 39 | 67 |
| 4 | 218 | 11 | 18 |
| 5 | 1,908 | 101 | 238 |
| 6 | 506 | 27 | 61 |
| 7 | 343 | 18 | 24 |
| 8 | 27 | 1 | 16 |
| 9 | 6 | 0 | 0 |
| **Total** | **4,279** | **226** | **480** |

Stratified split by difficulty to maintain balanced distribution.

**Split Method:** Stratified sampling to maintain difficulty distribution across train/validation/test sets.

## Training Configuration

### LoRA Parameters
- **r:** 32
- **alpha:** 64
- **dropout:** 0.15
- **target_modules:** q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj

### Training Parameters
- **epochs:** 3
- **learning_rate:** 3e-5
- **batch_size:** 4 × 4 = 16 (effective)
- **max_length:** 1024 tokens
- **optimizer:** AdamW (fused)
- **scheduler:** Cosine with 15% warmup
- **early_stopping:** patience=2

See [DEEP_TRAINING_CONFIG.md](DEEP_TRAINING_CONFIG.md) for full configuration.

## Results

### Training Metrics
- **Best Checkpoint:** checkpoint-700
- **Best Validation Loss:** 0.7054
- **Training Time:** 33 minutes
- **Total Steps:** 804




