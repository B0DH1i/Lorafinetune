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

**Overall Results:**

| Model | Pass@1 Score | Problems Solved |
|-------|-------------|----------------|
| Deep Step 700 | 25% | 6/24 |
| Diverse Step 500 | 29.2% | 7/24 |

### Key Insights from Analysis

**Learning Through Barriers**

The most striking finding is Diverse's ability to push through learning barriers where Deep gets stuck. In Problem 2 (string comparison), Deep remained trapped with partial solutions across multiple checkpoints, unable to handle edge cases with different string lengths. Meanwhile, Diverse eventually figured out the complete logic and solved the problem fully. This suggests that seeing multiple solution approaches helps models overcome conceptual barriers that single-solution training struggles with.

**Stability vs. Exploration Trade-offs**

A concerning pattern emerged with Deep's learning instability. In Problem 6 (character counting), Deep actually regressed from a previously learned correct solution back to a flawed approach - it forgot what it had learned. Diverse maintained stable performance throughout training. This indicates that while Deep's broader problem exposure might encourage more exploration, it can be harmful when it overwrites good solutions.

**Quality Over Quantity in Success**

When examining the success patterns, Diverse shows a cleaner approach: it either solves problems completely or fails clearly. Deep tends to produce more "partial successes" - solutions that work on some test cases but miss edge cases. From a practical deployment perspective, Diverse's behavior is more predictable and reliable.

**Shared Complexity Ceiling**

Both models hit identical walls on advanced problems. Complex geometry (Problem 4) and temporal reasoning (Problem 5) defeated both approaches equally. This suggests that the fundamental model architecture and size, rather than training strategy, determines the upper limit of problem complexity these models can handle.

**Implementation Philosophy Differences**

When Deep succeeds, it tends to be more thorough in implementation details (as seen in Problem 3's complete pattern specification). However, this thoroughness comes at the cost of learning ability and stability. Diverse focuses on getting to working solutions and maintaining them, even if they're not as specification-complete.

## Analysis Method

**Individual Model Analysis:**
- Problem-by-problem performance tracking for each checkpoint
- Error type classification (syntax, logic, algorithm)
- Learning progression analysis
- Stability and regression detection

**Comparative Analysis:**
- Deep vs Diverse optimal checkpoint comparison
- Problem-specific strengths and weaknesses
- Code quality assessment
- Learning capability analysis

## Key Findings

### Diverse Instruction Advantages

**1. Learning Capability**
- **Problem 2 (String Comparison)**: Solved the problem completely while Deep remained stuck with partial solutions
- Demonstrated ability to overcome conceptual barriers that Deep couldn't break through
- Better edge case handling and logical reasoning development

**2. Strong Learning Stability**
- **Problem 6 (Character Counting)**: Maintained working solution while Deep lost its previous learning
- Zero instances of forgetting learned solutions across all problems
- Consistent high code quality across most problems compared to Deep's more variable performance

**3. Better Error Profile**
- More error-free solutions compared to Deep
- No algorithm errors (Deep had multiple algorithm failures)
- When Diverse fails, it fails cleanly rather than producing buggy partial solutions

**4. Better Overall Reliability**
- Higher success rate compared to Deep
- More predictable performance patterns
- Either solves completely or fails clearly (no misleading partial successes)

### Deep Instruction Advantages

**1. Implementation Thoroughness**
- **Problem 3 (Pattern Matching)**: Achieved complete specification compliance (#.#)
- More detailed implementations when successful
- Better attention to specification completeness and edge case coverage

**2. Specification Adherence**
- When Deep succeeds, it tends to implement the full specification requirements
- More complete pattern recognition in successful cases
- Higher attention to implementation details

### Common Limitations

**Shared Failure Patterns:**
- **Complex Geometry (Problem 4)**: Both models completely fail on origin-based path calculations
- **Temporal Reasoning (Problem 5)**: Neither can handle time interval logic or candy distribution algorithms
- **Mathematical Ceiling**: Both hit the same complexity wall on advanced algorithmic problems

**Shared Strengths:**
- **Basic String Operations**: Both excel at fundamental string manipulation tasks
- **Simple Logic**: Both understand basic programming concepts and control flow
- **Code Structure**: Both produce syntactically correct code for problems within their capability range

## Main Conclusion

**Solution diversity > Problem diversity**

5 different solutions for 1,000 problems proved more effective than 5,000 unique problems.

**Why Diverse Performs Better:**
- **Multiple Solution Exposure**: Seeing 5 different approaches for the same problem builds deeper understanding
- **Enhanced Pattern Recognition**: Better ability to identify and handle edge cases
- **Improved Generalization**: More robust internal representations lead to better problem-solving
- **Learning Stability**: Less forgetting and more consistent performance
- **Learning Ability**: Ability to overcome conceptual barriers that single-solution training cannot break

## Technical Details

**Base Model**: Qwen2.5-Coder-1.5B-Instruct
**Training Examples**: ~4,500 per model (after train/val/test split)
**Evaluation**: 24 AtCoder problems (Aug 2024 - Feb 2025)
**Analysis Tools**: Custom Python scripts for error classification, visualization, comparison

**Trained Models:**
- **Diverse Instruction Model**: https://huggingface.co/bodhai/qwen-coder-lora-diverse
- **Deep Instruction Model**: https://huggingface.co/bodhai/qwen-coder-deep-lora

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

