# Day8 Code Scaffold

目标：把 Day7 的最小 LangGraph 工作流升级成可持久化、可查看历史的图。

你需要补完的文件：

- `main.py`
- `workflow.py`
- `inspect_utils.py`

建议步骤：

1. 先复制并简化 Day7 的图结构
2. 再接入 `InMemorySaver`
3. 再实现 snapshot / history 打印
4. 最后做两个 thread 的对照
5. 运行 `python main.py`
6. 运行 `python -m pytest tests/`

今天的关键不是“多跑几次 invoke”，而是理解：

- 哪些状态被保存了
- 它们按什么顺序保存
- 为什么这就是后续高级能力的地基
