# Day2 Code Scaffold

目标：实现一个“学习任务设计 Agent”，重点训练工具描述、参数 schema 和工具选择。

你需要补完的文件：

- `main.py`
- `tools.py`
- `schemas.py`
- `prompts.py`

建议步骤：

1. 先定义工具边界，不要先写函数体
2. 先写 `schemas.py` 里的 Pydantic 模型
3. 再写 `tools.py`
4. 最后在 `main.py` 里创建 Agent 并观察调用轨迹
5. 运行 `python main.py`
6. 运行 `python -m pytest tests/`

今天的关键不是功能多少，而是这三件事：

- 工具边界是否清晰
- schema 是否明确
- 你能否看见工具调用过程
