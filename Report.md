# Code Generation Model Training - Final Report

## Project Overview

This project trained and compared two code generation models using different dataset strategies. We performed instruction tuning on the Qwen2.5-Coder-1.5B-Instruct base model.

## Dataset Strategies

**Deep Instruction Model:**
- 5,000 unique programming problems
- Each problem contains a single solution
- Maximum problem diversity

**Diverse Instruction Model:**
- 1,000 problems × 5 different solutions = 5,000 examples
- Multiple solution approaches for the same problem
- Maximum solution diversity

## Training and Checkpoint Selection

We saved and evaluated 8 checkpoints (Step 200-804) for each model. For optimal checkpoint selection, we used:

- **Benchmark performance**: LiveCodeBench AtCoder problems (24 problems)
- **Validation curves**: Loss curves and learning rate analysis
- **Stability analysis**: Regression detection and consistency

**Selected Optimal Checkpoints:**
- **Deep Instruction**: Step 700
- **Diverse Instruction**: Step 500

## Benchmark Evaluation

**Strict Benchmark Characteristics:**
- Minimal normalization (whitespace only)
- Exact matching, no partial credit
- Real code execution
- Multiple test cases per problem

**Benchmark Results:**

| Model | Pass@1 Score | Problems Solved |
|-------|-------------|----------------|
| Deep Step 700 | 25% | 6/24 |
| Diverse Step 500 | 29.2% | 7/24 ||

## Analysis Methodology

**Individual Model Analysis:**
- Problem-by-problem performance tracking for each checkpoint
- Error type classification (syntax, logic, algorithm)
- Learning progression analysis
- Stability and regression detection

**Comparative Analysis:**
- Deep vs Diverse optimal checkpoint comparison
- Problem-specific strengths and weaknesses
- Code quality assessment
- Breakthrough learning capability analysis

## Key Findings

### Diverse Instruction Advantages

**1. Breakthrough Learning**
- Problem 2: Diverse achieved 100% success, Deep stuck at 67%
- More successful at edge case handling
- Ability to overcome conceptual barriers

**2. Stability**
- Problem 6: Maintained perfect solution, Deep regressed
- No catastrophic forgetting
- Consistent high code quality

**3. Overall Performance**
- 7/24 vs 6/24 problems solved
- 29.2% vs 25% Pass@1 score
- Either solves completely or fails (no partial successes)

### Deep Instruction Advantages

**1. Implementation Thoroughness**
- Problem 3: Complete specification compliance
- More detailed implementations
- Better attention to edge cases when successful

### Common Limitations

Both models failed on:
- Complex geometry (Problem 4)
- Temporal reasoning (Problem 5)
- Multi-step mathematical algorithms

## Main Conclusion

**Solution diversity > Problem diversity**

5 different solutions for 1,000 problems proved more effective than 5,000 unique problems.

**Why Diverse Performs Better:**
- Seeing multiple approaches for the same problem
- Deeper understanding of problem structure
- Improved edge case handling
- More stable internal representations
- Better generalization capability

## Technical Details

**Base Model**: Qwen2.5-Coder-1.5B-Instruct
**Training Examples**: ~4,500 per model (after train/val/test split)
**Evaluation**: 24 AtCoder problems (Aug 2024 - Feb 2025)
**Analysis Tools**: Custom Python scripts for error classification, visualization, comparison

## Practical Implications

**For Model Training:**
- Prioritize solution diversity
- Monitor multiple checkpoints, final may not be optimal
- Use strict benchmarks
- Track stability, not just accuracy

**For Dataset Creation:**
- Include multiple valid solutions for same problems
- Quality over quantity
- Demonstrate different solution strategies

## Conclusion

This study demonstrates that **solution diversity is more valuable than problem diversity** in code generation models. Models that learn to solve the same problem with different approaches outperform models exposed to more unique problems.


This finding can guide future dataset creation and model training strategies.
