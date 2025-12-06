# 🚀 DEEP Training Configuration

## LoRA Configuration
| Parameter | Value |
|-----------|-------|
| r | 32 |
| alpha | 64 |
| dropout | 0.15 |
| target_modules | q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj |
| bias | none |
| task_type | CAUSAL_LM |

## Training Arguments
| Parameter | Value |
|-----------|-------|
| output_dir | ./deep_v2_solution_a100 |
| num_train_epochs | 3 |
| per_device_train_batch_size | 4 |
| gradient_accumulation_steps | 4 |
| learning_rate | 3e-5 |
| warmup_ratio | 0.15 |
| lr_scheduler_type | cosine |
| weight_decay | 0.05 |
| max_grad_norm | 0.3 |
| optim | adamw_torch_fused |
| eval_strategy | steps |
| eval_steps | 100 |
| save_strategy | steps |
| save_steps | 100 |
| save_total_limit | 8 |
| load_best_model_at_end | True |
| metric_for_best_model | eval_loss |
| logging_dir | ./logs |
| logging_strategy | steps |
| logging_steps | 20 |
| report_to | none |
| bf16 | True |
| fp16 | False |
| tf32 | True |
| gradient_checkpointing | True |
| group_by_length | True |
| dataloader_num_workers | 4 |

## Early Stopping
| Parameter | Value |
|-----------|-------|
| early_stopping_patience | 2 |
| early_stopping_threshold | 0.0 |

## Tokenization
| Parameter | Value |
|-----------|-------|
| max_length | 1024 |
| padding | max_length |
| truncation | True |
| strategy | solution_only |
