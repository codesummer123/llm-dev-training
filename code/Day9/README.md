# Day9 Code Scaffold

目标：实现一个最小 LangGraph 审批流，体验 interrupt / resume 的完整闭环。

你需要补完的文件：

- `main.py`
- `workflow.py`
- `inspect_utils.py`

建议步骤：

1. 先定义 state
2. 再实现审批 interrupt 节点
3. 再实现批准 / 拒绝路径
4. 最后分别跑 `resume=True` 和 `resume=False`
5. 运行 `python main.py`
6. 运行 `python -m pytest tests/`

今天的关键不是“会调用 interrupt”，而是理解：

- interrupt 为什么依赖 checkpoint
- resume 为什么必须回到同一条 thread
- 为什么 node 恢复后会重新从头执行
