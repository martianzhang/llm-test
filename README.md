# llm-test

大语言模型能力测试框架 — 系统化评估 LLM 在数学推理、常识判断、因果逻辑、字符识别、亲属关系、本土知识等易犯错问题的表现。

---

## 🚀 快速开始

### 安装为 AI 技能

**快速安装（推荐）**

```bash
npx skills add martianzhang/llm-test
```

**手动安装**

克隆仓库，将整个 `llm-test` 目录移动到对应工具的 skills 目录下：

```bash
git clone https://github.com/martianzhang/llm-test.git
# Claude Code
mv llm-test ~/.claude/skills/
# GitHub Copilot / VS Code
mv llm-test ./.github/skills/
```

### 调用 Skill

**示例调用方式：**

```
请使用 llm-test skill 对我进行测试
```

或直接告诉 AI：

```
请加载 llm-test skill，帮助我测试当前模型的各项能力
```

Skill 加载后会自动执行完整的测试流程，无需手动逐题提问。

---

## 📁 项目结构

```
llm-test/
├── README.md              # 项目说明文档
├── SKILL.md               # 详细测试题目与评分标准
├── 大语言模型测试_提示词.md   # 测试用提示词
└── 大语言模型测试_答案.md    # 参考答案
```

---

## 🤝 贡献

欢迎提交 Issue 或 Pull Request 来改进测试题目或评分标准。

---

## 📄 License

MIT
