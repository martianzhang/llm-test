# llm-test

> [English Version](README.md)

---

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
├── README.md                  # 项目说明文档
├── README_zh.md              # English documentation
├── SKILL.md                   # 详细使用指南
├── resources/
│   ├── dataset.json           # 英文数据集
│   └── dataset.zh.json       # 中文数据集
└── scripts/
    └── dataset_query.py       # 数据集查询工具
```

---

## 🛠️ 数据集查询工具

```bash
# 查看问题总数
python scripts/dataset_query.py total

# 列出所有分类
python scripts/dataset_query.py categories

# 获取指定问题
python scripts/dataset_query.py question <index>

# 获取指定答案
python scripts/dataset_query.py answer <index>

# 获取完整条目（问题 + 答案 + 分类）- 仅供人类参考
python scripts/dataset_query.py get <index>
```

脚本会自动根据系统语言选择 `dataset.json`（英文）或 `dataset.zh.json`（中文）。

---

## 📊 测试分类

| 分类 | 说明 |
|------|------|
| Math | 数学计算能力 |
| Spatial | 空间推理能力 |
| Common Sense | 常识判断能力 |
| Logic | 因果逻辑能力 |
| Counting | 计数能力 |
| Relational | 亲属关系推理 |
| Linguistic | 语言文字游戏 |
| Chinese Culture | 本土文化知识 |
| Chinese Characters | 汉字识别能力 |
| Safety | 安全合规检测 |

---

## 📚 参考资料

本测试框架的灵感来源与扩展参考：

- [Easy Problems That LLMs Get Wrong](https://github.com/autogenai/easy-problems-that-llms-get-wrong) - 收集看似简单但大语言模型经常出错的问题
- [arXiv:2405.19616v2](https://arxiv.org/html/2405.19616v2) - 研究论文，记录大语言模型的失败模式

---

## 🤝 贡献

欢迎提交 Issue 或 Pull Request 来改进测试题目或评分标准。

---

## 📄 License

MIT
