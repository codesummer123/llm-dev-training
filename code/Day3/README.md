# Day3 Code Scaffold

目标：实现一个“学习任务抽取 Agent”，对比自由文本输出与结构化输出。

你需要补完的文件：

- `main.py`
- `schemas.py`
- `prompts.py`

建议步骤：

1. 先定义输出 schema
2. 再写自由文本模式
3. 再接 structured output
4. 最后打印 `messages` 和结构化结果做对比
5. 运行 `python main.py`
6. 运行 `python -m pytest tests/`

今天的关键不是多做功能，而是把“给人读”和“给系统接”的输出差别彻底看清楚。
