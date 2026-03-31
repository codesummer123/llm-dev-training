from langchain.tools import tool

@tool
def lookup_concept(concept: str) -> str:
    """查询框架概念的简短解释。"""

    # 建立一个微型的小词典 (Glossary)
    glossary = {
        "langchain": "一个用于开发由大语言模型驱动的应用程序的框架。",
        "langgraph": "LangChain的扩展，用于构建具有循环和状态的复杂 Agent 应用。",
        "tool": "赋予大模型与外部世界（如API、数据库）交互能力的功能接口。",
        "agent": "使用大语言模型作为推理引擎，来决定采取什么行动以及行动顺序的智能系统。",
        "prompt": "发送给大模型的输入提示词或指令。"
    }

    # 统一转小写进行匹配，如果找不到就返回默认提示
    return glossary.get(concept.lower(), f"抱歉，我的内置词典里没有关于 '{concept}' 的解释。")

@tool
def suggest_next_step(current_topic: str) -> str:
    """针对指定主题，建议下一步的具体实践步骤。"""

    # 根据不同的话题，返回一个简短、可操作的下一步建议
    steps = {
        "tool": "动手写一个能获取当前系统时间的 Python 函数，并用 @tool 装饰器把它变成工具。",
        "agent": "尝试把你写好的 tool 放进 create_agent 的列表中，并问 Agent '现在几点了'。",
        "langchain": "去阅读 LangChain 官方文档的 Quickstart 部分，并跑通第一个例子。"
    }
    return steps.get(current_topic.lower(), f"针对 '{current_topic}'，建议你先在 GitHub 上搜索相关的实战开源项目看看。")


@tool
def estimate_study_time(task_name: str, difficulty: str) -> str:
    """根据难度预估完成某项学习任务可能需要花费的时间。"""

    # 根据难度返回预估时间
    difficulty = difficulty.lower()
    if difficulty == "简单":
        return f"学习任务 [{task_name}] 难度较低，预计需要 15 分钟。"
    elif difficulty == "中等":
        return f"学习任务 [{task_name}] 难度中等，预计需要 30 分钟。"
    elif difficulty == "复杂":
        return f"学习任务 [{task_name}] 难度较高，预计需要 45 分钟。"
    else:
        return f"无法识别 [{task_name}] 的难度，建议预留至少 1 小时。"
