from langchain.tools import tool

from schemas import PracticeTaskInput


@tool
def lookup_topic_overview(topic: str) -> str:
    """查询某个大模型开发主题的简短介绍，适合概念解释类问题。"""
    # TODO: 用一个小型词典实现。
    # Suggested topics: langchain, langgraph, tool, message, prompt, schema.
    raise NotImplementedError("Implement lookup_topic_overview() for Day2.")


@tool
def estimate_task_effort(task_name: str, difficulty: str) -> str:
    """根据任务名称和难度，返回一个稳定的时间预估结果。难度请使用：简单、中等、复杂。"""
    # TODO: 用确定性规则实现。
    # Example: 简单 -> 15 分钟, 中等 -> 30 分钟, 复杂 -> 45 分钟。
    raise NotImplementedError("Implement estimate_task_effort() for Day2.")


@tool(args_schema=PracticeTaskInput)
def create_practice_task(
    topic: str,
    current_level: str,
    output_type: str,
    minutes_available: int,
) -> str:
    """根据主题、当前水平、输出形式和可用时间，生成一个聚焦且可执行的练习任务。"""
    # TODO: 返回一个结构清楚、一步一步的练习任务。
    # Keep it deterministic and concise.
    raise NotImplementedError("Implement create_practice_task() for Day2.")
