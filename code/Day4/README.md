# Day4 Code Scaffold

目标：实现一个带 short-term memory 的学习陪练 Agent，并加入最小消息裁剪策略。

你需要补完的文件：

- `main.py`
- `memory_utils.py`
- `prompts.py`

建议步骤：

1. 先实现无记忆对比
2. 再接入 checkpointer
3. 再验证同一 thread 和记忆隔离
4. 最后加上消息裁剪
5. 运行 `python main.py`
6. 运行 `python -m pytest tests/`

今天的关键是理解：

- 记忆为什么需要 thread
- 记忆为什么需要治理
- 为什么“记住更多”不等于“效果更好”
