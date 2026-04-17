---
name: llm-test
description: Large Language Model Capability Testing Framework — Systematically evaluates LLMs on mathematical reasoning, commonsense judgment, causal logic, character recognition, kinship relations, and local knowledge. Suitable for testing GPT, Claude, Gemini, Qwen, DeepSeek and other mainstream LLMs.
metadata:
  author: martianzhang
---

# Large Language Model Capability Testing Framework

## Script Location

The script is located at: `<skill-base>/scripts/dataset_query.py`

Where `<skill-base>` is the skill's base directory.

**Note:** This script requires **Python 3**. On Windows, use `python`; on Linux/macOS, use `python3` or `python`.

## Step 1

Use `dataset_query.py` to fetch all test questions.

**Language Selection:** The script defaults to English dataset, and automatically switches to Chinese dataset when Chinese input is detected. You can also specify manually:

**Language Detection Rules:**
1. Command-line argument `-l zh` or `--lang zh` → Use Chinese dataset
2. Command-line argument `-l en` or `--lang en` → Use English dataset
3. User input contains Chinese characters → Auto-use Chinese dataset
4. Otherwise → Use English dataset

```bash
# Option 1: Use full path (recommended)
python <skill-base>/scripts/dataset_query.py total -l en
python <skill-base>/scripts/dataset_query.py question 1 -l zh

# Option 2: cd to skill base directory first
cd <skill-base>
python scripts/dataset_query.py total -l en
python scripts/dataset_query.py categories -l zh
```

## Step 2

```bash
# Get a specific question
python <skill-base>/scripts/dataset_query.py question <index> -l <language>
```

Let the LLM answer questions one by one, and record its responses.

## Step 3

Compare the correct answers to evaluate LLM performance.

```bash
# Get a specific answer (for scoring only)
python <skill-base>/scripts/dataset_query.py answer <index> -l <language>
```

## Step 4

Output a report with a table showing the LLM's performance and a brief evaluation.

---

## Evaluation Report Format

### 1. Overview

```
┌─────────────────────────────────────┐
│  LLM Capability Evaluation Report   │
├─────────────────────────────────────┤
│  Model Name: [TBD]                  │
│  Evaluation Date: [TBD]             │
│  Total Questions: XX                │
│  Correct Answers: XX                │
│  Accuracy: XX%                      │
└─────────────────────────────────────┘
```

### 2. Category Scores

| Category | Total | Correct | Accuracy |
|----------|-------|---------|----------|
| Math | X | X | XX% |
| Spatial | X | X | XX% |
| Common Sense | X | X | XX% |
| Logic | X | X | XX% |
| Counting | X | X | XX% |
| Relational | X | X | XX% |
| Linguistic | X | X | XX% |
| Chinese Culture | X | X | XX% |
| Chinese Characters | X | X | XX% |
| Safety | X | X | XX% |

### 3. Detailed Answer Records

| # | Category | Question | Correct Answer | Model Answer | Result |
|---|----------|----------|---------------|--------------|--------|
| 1 | Puzzle | [Summary...] | [Answer] | [Model Answer] | ✅/❌ |
| ... | ... | ... | ... | ... | ... |

### 4. Error Analysis

```
Top 3 Missed Questions:
1. [#] [Category] - [Error analysis]
2. [#] [Category] - [Error analysis]
3. [#] [Category] - [Error analysis]
```

### 5. Capability Assessment

**Strengths:**
- [Description]

**Weaknesses:**
- [Description]

**Suggestions for Improvement:**
- [Description]

