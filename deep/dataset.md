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




