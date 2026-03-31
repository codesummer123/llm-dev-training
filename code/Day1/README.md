# Day1 Code Scaffold

目标：实现一个基于 `LangChain` 的最小工具型 Agent。

你需要补完的文件：

- `main.py`
- `tools.py`
- `prompts.py`

建议步骤：

1. 安装你要用的 provider 集成，例如：
   - `pip install -U "langchain[openai]"`
   - `pip install -U "langchain[anthropic]"`
   - `pip install -U "langchain[google-genai]"`
2. 设置模型环境变量，例如：
   - `DAY1_MODEL=openai:gpt-5.2`
   - `DAY1_MODEL=anthropic:claude-sonnet-4-6`
   - `DAY1_MODEL=google_genai:gemini-2.5-flash-lite`
3. 完成工具实现
4. 完成 agent 创建与调用
5. 运行 `python main.py`

今天的目标不是炫技，而是把这 4 个点写清楚：

- 模型怎么初始化
- 工具怎么定义
- prompt 怎么约束行为
- agent 怎么组合并调用

建议你自己至少测试两类问题：

- 不需要工具的问题
- 需要工具的问题
