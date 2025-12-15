# Training Results - DIVERSE Dataset

## Best Model

### Checkpoint-500 ⭐

| Metric | Value |
|--------|-------|
| **Validation Loss** | 0.8148 |
| **Test Loss** | 0.9336 |
| **Training Step** | 500 |
| **Epoch** | ~1.76 |

## All Checkpoints

| Checkpoint | Step | Validation Loss | Test Loss | Status |
|------------|------|----------------|-----------|--------|
| checkpoint-100 | 100 | 0.8506 | 0.9458 | - |
| checkpoint-200 | 200 | 0.8373 | 0.9370 | - |
| checkpoint-300 | 300 | 0.8300 | 0.9377 | - |
| checkpoint-400 | 400 | 0.8229 | 0.9370 | - |
| **checkpoint-500** | **500** | **0.8148** | **0.9336** | **✅ Best** |
| checkpoint-600 | 600 | 0.8203 | 0.9440 | ⚠️ Overfitting |
| checkpoint-700 | 700 | 0.8224 | 0.9513 | ⚠️ Overfitting |

## Training Progress

### Loss Reduction

| Metric | Initial | Final | Reduction |
|--------|---------|-------|-----------|
| **Train Loss** | 1.0605 | 0.6791 | 36% ↓ |
| **Validation Loss** | 0.8506 | 0.8148 | 4.2% ↓ |

