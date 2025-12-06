# LoRA Fine-Tuning: DEEP Dataset

LoRA fine-tuning of Qwen2.5-Coder-1.5B-Instruct on DEEP-5K dataset for competitive code generation.

## Model
- **Base Model:** [Qwen/Qwen2.5-Coder-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct)
- **Dataset:** [DEEP-5K](https://huggingface.co/datasets/Naholav/CodeGen-Deep-5K)
- **Strategy:** Solution-only (code generation without reasoning)

## Dataset Split

### Original Split
- **Total:** 4,985 examples
- **Train:** 4,505 examples (90.4%)
- **Test:** 480 examples (9.6%)

### Our Split (Stratified by Difficulty)
- **Train:** 4,279 examples (95%)
- **Validation:** 226 examples (5%)
- **Test:** 480 examples (9.6%)

### Difficulty Distribution

| Difficulty | Train | Validation | Test | Split Ratio |
|------------|-------|------------|------|-------------|
| 1 | 204 | 11 | 480 | 5.4% |
| 2 | 338 | 18 | - | 5.3% |
| 3 | 729 | 39 | - | 5.3% |
| 4 | 218 | 11 | - | 5.0% |
| 5 | 1,908 | 101 | - | 5.3% |
| 6 | 506 | 27 | - | 5.3% |
| 7 | 343 | 18 | - | 5.2% |
| 8 | 27 | 1 | - | 3.7% |
| 9 | 6 | 0 | - | 0.0% |
| **Total** | **4,279** | **226** | **480** | **5.0%** |

**Split Ratio:** Percentage of training data moved to validation (stratified by difficulty)

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

### Benchmark Performance
- **Accuracy:** 25% (2/8 correct)
- **Test Loss:** 0.7054

See [DEEP_BENCHMARK_COMPARISON.md](DEEP_BENCHMARK_COMPARISON.md) for detailed results.

## Files

- `train_deep.py` - Training script
- `DEEP_TRAINING_CONFIG.md` - Full hyperparameters
- `DEEP_BENCHMARK_COMPARISON.md` - Benchmark results
- `deep_training_visualization.png` - Training curves

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

# Load model
base_model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-Coder-1.5B-Instruct")
model = PeftModel.from_pretrained(base_model, "path/to/checkpoint-700")
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-Coder-1.5B-Instruct")

# Generate
prompt = "You are an expert Python programmer. Please read the problem carefully before writing any Python code.\n\nProblem:\n[problem]\n\nSolution:\n"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=512)
print(tokenizer.decode(outputs[0]))
```

## Training

```bash
python train_deep.py
```

## Requirements

```
transformers
peft
datasets
torch
sklearn
```
