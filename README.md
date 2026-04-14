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
├── README.md              # Project documentation
├── README_zh.md           # 中文文档
├── SKILL.md               # Detailed test questions and scoring criteria
├── 大语言模型测试_提示词.md   # Test prompts (Chinese)
└── 大语言模型测试_答案.md    # Reference answers (Chinese)
```

---

## 🤝 Contributing

Issues and Pull Requests are welcome to improve test questions or scoring criteria.

---

## 📄 License

MIT
