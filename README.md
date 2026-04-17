# llm-test

> [中文版](README_zh.md)

---

Large Language Model Capability Testing Framework — Systematically evaluates LLMs on error-prone tasks including mathematical reasoning, commonsense judgment, causal logic, character recognition, kinship relations, and local knowledge.

---

## 🚀 Quick Start

### Install as AI Skill

**Quick Install (Recommended)**

```bash
npx skills add martianzhang/llm-test
```

**Manual Installation**

Clone the repository and move the entire `llm-test` directory to your skills folder:

```bash
git clone https://github.com/martianzhang/llm-test.git
# Claude Code
mv llm-test ~/.claude/skills/
# GitHub Copilot / VS Code
mv llm-test ./.github/skills/
```

### Using the Skill

**Example usage:**

```
Please use the llm-test skill to test me
```

Or simply tell the AI:

```
Please load the llm-test skill and help me test the capabilities of the current model
```

Once the skill is loaded, it will automatically run the complete test suite without manual question-by-question prompting.

---

## 📁 Project Structure

```
llm-test/
├── README.md                  # Project documentation
├── README_zh.md               # 中文文档
├── SKILL.md                   # Detailed usage guide
├── resources/
│   ├── dataset.json           # English dataset
│   └── dataset.zh.json        # Chinese dataset
└── scripts/
    └── dataset_query.py       # Dataset query tool
```

---

## 🛠️ Dataset Query Tool

```bash
# View total number of questions
python scripts/dataset_query.py total

# List all categories
python scripts/dataset_query.py categories

# Get a specific question
python scripts/dataset_query.py question <index>

# Get a specific answer
python scripts/dataset_query.py answer <index>

# Get full item (question + answer + category) - for reference only
python scripts/dataset_query.py get <index>
```

The script automatically selects `dataset.json` (English) or `dataset.zh.json` (Chinese) based on your system language.

---

## 📊 Test Categories

| Category | Description |
|----------|-------------|
| Math | Mathematical reasoning |
| Spatial | Spatial reasoning |
| Common Sense | Commonsense judgment |
| Logic | Causal logic |
| Counting | Counting ability |
| Relational | Kinship relations |
| Linguistic | Language puzzles |
| Chinese Culture | Local cultural knowledge |
| Chinese Characters | Character recognition |
| Safety | Safety compliance |

---

## 🤝 Contributing

Issues and Pull Requests are welcome to improve test questions or scoring criteria.

---

## 📄 License

MIT
