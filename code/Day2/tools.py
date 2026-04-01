from langchain.tools import tool

from schemas import PracticeTaskInput


@tool
def lookup_topic_overview(topic: str) -> str:
    """查询某个大模型开发主题的简短介绍，适合概念解释类问题。"""
    topics = {
        "langchain": "一个用于开发由大语言模型驱动的应用程序的框架。",
        "langgraph": "langchain的扩展，用于构建具有循环和状态的复杂 Agent 应用。",
        "tool": "赋予大模型与外部世界（如API、数据库）交互能力的功能接口。",
        "agent": "使用大语言模型作为推理引擎，来决定采取什么行动以及行动顺序的智能系统。",
        "prompt": "发送给大模型的输入提示词或指令。",
        "schema": "tools参数解释，组合到大模型的Prompt里",
        "message": "限制大模型回答边界，有system、user等"
    }
    return topics.get(topic.lower(), "没有找到对应的主题的解释")


@tool
def estimate_task_effort(task_name: str, difficulty: str) -> str:
    """根据任务名称和难度，返回一个稳定的时间预估结果。难度请使用：简单、中等、复杂。"""
    time_map = {
        "简单": "15分钟",
        "中等": "30分钟",
        "复杂": "45分钟",
    }
    return f"经过评估，[{task_name}] 任务的难度为：[{difficulty}，需要练习时间：{time_map.get(difficulty, "至少60分钟")}]"


@tool(args_schema=PracticeTaskInput)
def create_practice_task(
    topic: str,
    current_level: str,
    output_type: str,
    minutes_available: int,
) -> str:
    """根据主题、当前水平、输出形式和可用时间，生成一个聚焦且可执行的练习任务。"""
    task_plan = f"""
    生成的专属计划如下：
    【核心主题】: {topic}
    【难度适配】: {current_level}
    【时间限制】: {minutes_available} 分钟
    【交付形式】: {output_type}
    
    【执行步骤推荐】:
    1. 概念热身 (建议占总时间 20%): 快速回顾 {topic} 的核心原理。
    2. 动手实操 (建议占总时间 60%): 结合你当前的 {current_level} 水平，开始编写代码或梳理逻辑。
    3. 整理输出 (建议占总时间 20%): 将你的成果转化为标准的 {output_type} 并检查。
    """
    return task_plan.strip()

