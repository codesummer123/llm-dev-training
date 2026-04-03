# Day5 Code Scaffold

目标：实现一个带 custom middleware 的学习教练 Agent。

你需要补完的文件：

- `main.py`
- `middleware.py`
- `prompts.py`

建议步骤：

1. 先写辅助函数并通过测试
2. 再接 `wrap_model_call` 做动态 prompt
3. 再接 `before_model` 做过宽请求短路
4. 运行 `python main.py`
5. 运行 `python -m pytest tests/`

今天的关键不是“把 prompt 再写长一点”，而是理解：

- 运行时如何临时改变上下文
- 运行时如何拦截和控制执行流
