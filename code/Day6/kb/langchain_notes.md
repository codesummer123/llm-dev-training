# LangChain Notes

LangChain 是偏上层的 Agent 开发框架，适合快速搭建具备工具调用能力的大模型应用。

在训练主线里，LangChain 的重点包括：

- tools
- messages
- structured output
- short-term memory
- middleware

middleware 的价值，不只是“附加逻辑”，而是让系统在运行时动态改变 prompt、限制调用、控制边界。
