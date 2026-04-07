# Day7 Code Scaffold

目标：实现一个最小 LangGraph 学习路径分流图。

你需要补完的文件：

- `main.py`
- `workflow.py`

建议步骤：

1. 先定义 state schema
2. 再实现 node
3. 再做条件路由
4. 最后打印 route_log 和最终状态
5. 运行 `python main.py`
6. 运行 `python -m pytest tests/`

今天的关键不是“图画得多复杂”，而是理解：

- 共享 state 怎么流动
- route function 怎么决定路径
- 为什么 LangGraph 适合带状态工作流
