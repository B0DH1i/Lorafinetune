"""
DEEP Dataset LoRA Fine-Tuning Script
Model: Qwen2.5-Coder-1.5B-Instruct
Strategy: Solution-only (code generation without reasoning)
"""

from datasets import load_dataset, Dataset, DatasetDict
from sklearn.model_selection import train_test_split
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import (
    TrainingArguments, Trainer, EarlyStoppingCallback,
    DataCollatorForLanguageModeling, AutoModelForCausalLM, AutoTokenizer
)
import torch

# Load dataset
dataset = load_dataset("Naholav/CodeGen-Deep-5K")
all_data = dataset['train']

# Split data
train_examples = [ex for ex in all_data if ex['split'] == 'train']
test_examples = [ex for ex in all_data if ex['split'] == 'test']

# Create validation split (5%)
difficulties = [ex['difficulty'] for ex in train_examples]
train_idx, val_idx = train_test_split(
    range(len(train_examples)), test_size=0.05, random_state=42, stratify=difficulties
)

split_dataset = DatasetDict({
    'train': Dataset.from_list([train_examples[i] for i in train_idx]),
    'validation': Dataset.from_list([train_examples[i] for i in val_idx]),
    'test': Dataset.from_list(test_examples)
})

# Model setup
MODEL_NAME = "Qwen/Qwen2.5-Coder-1.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# LoRA config
lora_config = LoraConfig(
    r=32, lora_alpha=64, lora_dropout=0.15,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    bias="none", task_type="CAUSAL_LM"
)

# Training args
training_args = TrainingArguments(
    output_dir="./deep_v2_solution",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    learning_rate=3e-5,
    warmup_ratio=0.15,
    lr_scheduler_type="cosine",
    weight_decay=0.05,
    max_grad_norm=0.3,
    optim="adamw_torch_fused",
    eval_strategy="steps",
    eval_steps=100,
    save_strategy="steps",
    save_steps=100,
    save_total_limit=8,
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
    logging_steps=20,
    bf16=True,
    gradient_checkpointing=True,
)

# Tokenization
SYSTEM_PROMPT = "You are an expert Python programmer. Please read the problem carefully before writing any Python code."

def tokenize_solution_only(examples):
    prompts = [
        f"{SYSTEM_PROMPT}\n\nProblem:\n{inp}\n\nSolution:\n{sol}"
        for inp, sol in zip(examples['input'], examples['solution'])
    ]
    tokenized = tokenizer(prompts, truncation=True, max_length=1024, padding="max_length")
    tokenized["labels"] = tokenized["input_ids"].copy()
    return tokenized

train_dataset = split_dataset['train'].map(tokenize_solution_only, batched=True, remove_columns=split_dataset['train'].column_names)
val_dataset = split_dataset['validation'].map(tokenize_solution_only, batched=True, remove_columns=split_dataset['validation'].column_names)

# Model
base_model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.bfloat16, device_map="auto", trust_remote_code=True)
base_model.gradient_checkpointing_enable()
base_model = prepare_model_for_kbit_training(base_model)
model = get_peft_model(base_model, lora_config)

# Train
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    data_collator=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False),
    callbacks=[EarlyStoppingCallback(early_stopping_patience=2)]
)

trainer.train()
trainer.save_model(f"{training_args.output_dir}/final_model")
