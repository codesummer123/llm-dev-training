# Day10 Code Scaffold

目标：实现一个最小 LangGraph time travel 实验，展示 replay 与 fork。

你需要补完的文件：

- `main.py`
- `workflow.py`
- `inspect_utils.py`

建议步骤：

1. 先跑一遍原始执行
2. 再打印 checkpoint history
3. 再做 replay
4. 再做 fork
5. 运行 `python main.py`
6. 运行 `python -m pytest tests/`

今天的关键不是“API 调通”，而是理解：

- replay 重跑了什么
- fork 改变了什么
- 为什么原始历史仍然保留
