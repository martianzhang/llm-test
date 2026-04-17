---
name: llm-test
description: 大语言模型能力测试框架 — 系统化评估 LLM 在数学推理、常识判断、因果逻辑、字符识别、亲属关系、本土知识等多个维度的表现。适用于评测 GPT、Claude、Gemini、通义千问、DeepSeek 等主流大语言模型。
metadata:
  author: martianzhang
---

# 大语言模型能力测试框架

## 第一步

读取“大语言模型测试_提示词.md”的提示词，逐个调用 SubAgent 并行作答。

## 第二步

等待所有 SubAgent 作答完毕，记录大语言模型每个提示词的回答结果。

## 第三步

解密 base64 编码的答案文件 大语言模型测试_答案.enc.md，对比正确答案与大模型的回答。

```bash
# Mac/Linux
cat 大语言模型测试_答案.enc.md | base64 -d
```

```powershell
# Windows
certutil -decode "大语言模型测试_答案.enc.md" 大语言模型测试_答案.md
```

## 第四步

输出报告，以表格形式展示大模型回答情况并进行简要评价。
