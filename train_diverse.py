"""
LoRA Fine-Tuning - DIVERSE Dataset
Qwen2.5-Coder-1.5B-Instruct modelini CodeGen-Diverse-5K ile eğitir
"""

import os
import json
import torch
from datetime import datetime
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling,
    EarlyStoppingCallback
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

# ============================================================================
# AYARLAR
# ============================================================================

# Model ve Dataset
MODEL_NAME = "Qwen/Qwen2.5-Coder-1.5B-Instruct"
DATASET_NAME = "Naholav/CodeGen-Diverse-5K"

# LoRA Parametreleri
LORA_R = 32              # LoRA rank
LORA_ALPHA = 64          # Scaling (2 × rank)
LORA_DROPOUT = 0.1       # Regularization

# Training Parametreleri
LEARNING_RATE = 2e-4     # Öğrenme hızı
EPOCHS = 3               # Epoch sayısı
BATCH_SIZE = 4           # Batch size (A100 için)
GRAD_ACCUM = 4           # Gradient accumulation (effective batch = 16)
MAX_LENGTH = 1024        # Maksimum token sayısı

# Diğer Ayarlar
OUTPUT_DIR = "./lora_diverse_output"
LOG_FILE = "./training_logs_diverse.jsonl"
SYSTEM_PROMPT = "You are an expert Python programmer. Please read the problem carefully before writing any Python code."

# ============================================================================
# KURULUM
# ============================================================================

print("=" * 80)
print("🚀 LoRA Fine-Tuning: DIVERSE Dataset")
print("=" * 80)

# Output klasörü oluştur
os.makedirs(OUTPUT_DIR, exist_ok=True)

# GPU kontrolü
if torch.cuda.is_available():
    print(f"✅ GPU: {torch.cuda.get_device_name(0)}")
    print(f"💾 Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
else:
    print("⚠️ GPU bulunamadı!")

# ============================================================================
# MODEL YÜKLEME
# ============================================================================

print("\n🤖 Model yükleniyor...")

# Tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Base model
try:
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
        attn_implementation="flash_attention_2"
    )
    print("✅ Flash Attention 2 aktif")
except:
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True
    )
    print("⚠️ Flash Attention 2 yok, normal attention kullanılıyor")

# Gradient checkpointing (memory tasarrufu için)
model.gradient_checkpointing_enable()
model = prepare_model_for_kbit_training(model)

# LoRA konfigürasyonu
lora_config = LoraConfig(
    r=LORA_R,
    lora_alpha=LORA_ALPHA,
    lora_dropout=LORA_DROPOUT,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

# ============================================================================
# DATASET YÜKLEME
# ============================================================================

print("\n📚 Dataset yükleniyor...")

dataset = load_dataset(DATASET_NAME)
full_dataset = dataset['train']

# Split kolonuna göre ayır
train_data = full_dataset.filter(lambda x: x['split'] == 'train')
valid_data = full_dataset.filter(lambda x: x['split'] == 'valid')
test_data = full_dataset.filter(lambda x: x['split'] == 'test')

print(f"✅ Train: {len(train_data)} | Valid: {len(valid_data)} | Test: {len(test_data)}")

# ============================================================================
# TOKENIZATION
# ============================================================================

print("\n🔄 Tokenization yapılıyor...")

def format_prompt(example):
    """Prompt formatı: System + Problem + Solution"""
    return f"{SYSTEM_PROMPT}\n\nProblem:\n{example['input']}\n\nSolution:\n{example['solution']}"

def tokenize_batch(examples):
    """Batch tokenization"""
    prompts = [format_prompt(ex) for ex in examples]
    tokenized = tokenizer(
        prompts,
        truncation=True,
        max_length=MAX_LENGTH,
        padding="max_length",
        return_tensors="pt"
    )
    tokenized["labels"] = tokenized["input_ids"].clone()
    return tokenized

# Dataset'leri hazırla
train_list = [{"input": ex["input"], "solution": ex["solution"]} for ex in train_data]
valid_list = [{"input": ex["input"], "solution": ex["solution"]} for ex in valid_data]
test_list = [{"input": ex["input"], "solution": ex["solution"]} for ex in test_data]

train_tokenized = tokenize_batch(train_list)
valid_tokenized = tokenize_batch(valid_list)
test_tokenized = tokenize_batch(test_list)

# PyTorch Dataset
class SimpleDataset(torch.utils.data.Dataset):
    def __init__(self, encodings):
        self.encodings = encodings
    
    def __len__(self):
        return len(self.encodings["input_ids"])
    
    def __getitem__(self, idx):
        return {key: val[idx] for key, val in self.encodings.items()}

train_dataset = SimpleDataset(train_tokenized)
valid_dataset = SimpleDataset(valid_tokenized)
test_dataset = SimpleDataset(test_tokenized)

print("✅ Tokenization tamamlandı")

# ============================================================================
# TRAINING
# ============================================================================

print("\n🚀 Training başlıyor...")

# Training arguments
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    num_train_epochs=EPOCHS,
    per_device_train_batch_size=BATCH_SIZE,
    per_device_eval_batch_size=BATCH_SIZE,
    gradient_accumulation_steps=GRAD_ACCUM,
    learning_rate=LEARNING_RATE,
    warmup_ratio=0.03,
    weight_decay=0.01,
    max_grad_norm=1.0,
    logging_steps=20,
    eval_steps=100,
    save_steps=100,
    eval_strategy="steps",
    save_strategy="steps",
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
    greater_is_better=False,
    bf16=True,
    optim="adamw_torch_fused",
    lr_scheduler_type="cosine",
    report_to="none",
    save_total_limit=None,  # Tüm checkpoint'leri kaydet
)

# Data collator
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=valid_dataset,  # Validation ile eğit
    data_collator=data_collator,
    callbacks=[EarlyStoppingCallback(early_stopping_patience=2)]
)

# Training başlat
train_result = trainer.train()

# Final model'i kaydet
print("\n💾 Model kaydediliyor...")
trainer.save_model(os.path.join(OUTPUT_DIR, "final_model"))
tokenizer.save_pretrained(os.path.join(OUTPUT_DIR, "final_model"))

# Test set ile final evaluation
print("\n🎯 Test set evaluation...")
test_results = trainer.evaluate(test_dataset)
print(f"Test Loss: {test_results['eval_loss']:.4f}")

# Sonuçları kaydet
with open(os.path.join(OUTPUT_DIR, "training_summary.json"), "w") as f:
    json.dump({
        "train_result": train_result.metrics,
        "test_result": test_results,
        "config": {
            "model": MODEL_NAME,
            "dataset": DATASET_NAME,
            "lora_r": LORA_R,
            "lora_alpha": LORA_ALPHA,
            "learning_rate": LEARNING_RATE,
            "batch_size": BATCH_SIZE,
            "epochs": EPOCHS
        }
    }, f, indent=2)

print("\n" + "=" * 80)
print("✅ Training tamamlandı!")
print("=" * 80)
print(f"📁 Model: {OUTPUT_DIR}/final_model")
print(f"📊 Test Loss: {test_results['eval_loss']:.4f}")
print(f"⏱️ Süre: {train_result.metrics['train_runtime'] / 60:.1f} dakika")
