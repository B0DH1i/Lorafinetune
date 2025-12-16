# LoRA Fine-tuning for Code Generation

A comprehensive project for fine-tuning the Qwen2.5-Coder-1.5B-Instruct model using LoRA (Low-Rank Adaptation) on competitive programming datasets. This repository implements two distinct training strategies: **DEEP** (focused, solution-only training) and **DIVERSE** (broad, comprehensive training).

## 🎯 Project Overview

This project explores different approaches to fine-tuning code generation models for competitive programming tasks:

- **DEEP Strategy**: Intensive training on a smaller, focused dataset (5K samples) with solution-only approach
- **DIVERSE Strategy**: Comprehensive training on a larger, varied dataset (5K samples) with full problem context
- **Evaluation Pipeline**: Automated evaluation using LiveCodeBench benchmark with AtCoder problems

## 📁 Repository Structure

```
Lorafinetune/
├── CodeGen/                    # Evaluation pipeline
│   ├── livecodebench_eval.py  # Main evaluation script
│   ├── run_all_evaluations.py # Batch evaluation runner
│   ├── requirements.txt       # Dependencies
│   └── common/                # Utility modules
├── deep/                      # DEEP training strategy
│   ├── train_deep.py         # Training script
│   ├── DEEP_TRAINING_CONFIG.md # Configuration details
│   └── dataset.md            # Dataset information
├── diverse/                   # DIVERSE training strategy
│   ├── train_diverse.py      # Training script
│   ├── DIVERSE_1_PARAMETERS.md # Training parameters
│   ├── DIVERSE_2_DATASET.md   # Dataset details
│   └── DIVERSE_3_RESULTS.md   # Results analysis
└── *.md                      # Benchmark results and comparisons
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- CUDA-compatible GPU (8GB+ VRAM recommended)
- PyTorch 2.0+

### Installation

1. Clone the repository:
```bash
git clone https://github.com/B0DH1i/Lorafinetune.git
cd Lorafinetune
```

2. Install dependencies:
```bash
cd CodeGen
pip install -r requirements.txt
```

3. Additional dependencies for training:
```bash
pip install peft datasets accelerate
```

## 🔧 Training Strategies

### DEEP Strategy
- **Dataset**: CodeGen-Deep-5K (Naholav/CodeGen-Deep-5K)
- **Approach**: Solution-only training without problem context
- **Focus**: Intensive learning on core coding patterns
- **LoRA Config**: r=32, α=64, dropout=0.15

```bash
cd deep
python train_deep.py
```

### DIVERSE Strategy  
- **Dataset**: CodeGen-Diverse-5K (Naholav/CodeGen-Diverse-5K)
- **Approach**: Full context training with problem descriptions
- **Focus**: Broad understanding across different problem types
- **LoRA Config**: r=32, α=64, dropout=0.1

```bash
cd diverse
python train_diverse.py
```

## 📊 Model Configuration

### Base Model
- **Model**: Qwen2.5-Coder-1.5B-Instruct
- **Parameters**: 1.54B total, ~37M trainable (2.34%)
- **Architecture**: Transformer-based code generation model

### LoRA Configuration
| Parameter | DEEP | DIVERSE |
|-----------|------|---------|
| Rank (r) | 32 | 32 |
| Alpha (α) | 64 | 64 |
| Dropout | 0.15 | 0.1 |
| Target Modules | 7 layers | 7 layers |
| Learning Rate | 3e-5 | 2e-4 |

## 🧪 Evaluation

### LiveCodeBench Evaluation

The project includes a comprehensive evaluation pipeline using LiveCodeBench benchmark:

```bash
cd CodeGen

# Evaluate specific model
python livecodebench_eval.py \
    --model_type deep_think \
    --steps 600 \
    --difficulty easy \
    --platform atcoder

# Run all evaluations
python run_all_evaluations.py \
    --models_dir ./models \
    --output_dir ./results
```

## 📊 Benchmark Results

### Model Performance Comparison (24 AtCoder Easy Problems)

| Model | Best Checkpoint | Pass@1 | Solved Problems |
|-------|----------------|--------|-----------------|
| **Deep Instruction** | step-700 | **25.0%** | **6/24** |
| **Diverse Instruction** | step-500 | **29.2%** | **7/24** |

## 📈 Training Results

### DEEP Strategy Results
- **Training Time**: ~45 minutes on A100
- **Best Checkpoint**: step-700-epoch-3
- **Dataset Split**: 85.9% train, 4.5% validation, 9.6% test

### DIVERSE Strategy Results  
- **Best Checkpoint**: step-500-epoch-2
- **Training Time**: ~32 minutes on A100
- **Dataset Split**: 90.6% train, 0.4% validation, 9.0% test


## 🔍 Key Features

### Training Features
- **LoRA Fine-tuning**: Efficient parameter adaptation
- **Mixed Precision**: BF16 for faster training
- **Gradient Checkpointing**: Memory optimization
- **Early Stopping**: Prevents overfitting
- **Cosine LR Scheduling**: Optimal learning rate decay

### Evaluation Features
- **Automated Testing**: Safe code execution environment
- **Multiple Metrics**: Pass@1, similarity scoring
- **Batch Processing**: Efficient evaluation pipeline
- **Detailed Logging**: Comprehensive result tracking

## 📋 Usage Examples

### Training a Custom Model
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import LoraConfig, get_peft_model

# Load base model
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-Coder-1.5B-Instruct")
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-Coder-1.5B-Instruct")

# Configure LoRA
lora_config = LoraConfig(
    r=32, lora_alpha=64, lora_dropout=0.15,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", 
                   "gate_proj", "up_proj", "down_proj"],
    bias="none", task_type="CAUSAL_LM"
)

# Apply LoRA
model = get_peft_model(model, lora_config)
```

### Evaluating Models
```python
# Single model evaluation
python livecodebench_eval.py --model_type deep_instruction --steps 600

# Platform-specific evaluation  
python livecodebench_eval.py --platform atcoder --difficulty easy

# Include base model comparison
python livecodebench_eval.py --include_base --difficulty easy
```

## 🛠️ Configuration

### System Requirements
- **GPU**: NVIDIA A100 (40GB) or equivalent
- **Memory**: 16GB+ RAM recommended
- **Storage**: 10GB+ for models and datasets
- **OS**: Linux (recommended), macOS, Windows







