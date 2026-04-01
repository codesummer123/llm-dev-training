import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

from prompts import SYSTEM_PROMPT
from tools import create_practice_task, estimate_task_effort, lookup_topic_overview

load_dotenv()


def build_model():
    """Initialize a tool-calling chat model for Day2."""
    model_name = os.getenv("DAY2_MODEL") or os.getenv("DAY1_MODEL")
    if not model_name:
        raise ValueError("Please set DAY2_MODEL or DAY1_MODEL.")

    return init_chat_model(model_name, temperature=0, max_retries=3, timeout=20.0)


def build_agent():
    """Create the Day2 learning task design agent."""
    tools = [lookup_topic_overview, estimate_task_effort, create_practice_task]
    model = build_model()
    return create_agent(model=model, tools=tools, system_prompt=SYSTEM_PROMPT)


def invoke_agent(user_input: str):
    """Return the raw agent response so you can inspect tool-calling behavior."""
    agent = build_agent()
    return agent.invoke({"messages": [{"role": "user", "content": user_input}]})


def print_trace(response):
    """Print the final answer and a minimal trace of tool calls."""
    # TODO: Read the response structure and print:
    # 1) final assistant content
    # 2) any tool calls found in AI messages
    # Suggested path to inspect first: response["messages"]
    raise NotImplementedError("Implement print_trace() for Day2.")


def main():
    sample_inputs = [
        "请解释一下 LangGraph 是什么。",
        "我今天有 30 分钟，想练工具设计，这个任务大概算什么难度？",
        "请给我设计一个关于 LangChain tools 的代码练习任务，我现在是初级，还能投入 45 分钟。",
    ]

    for user_input in sample_inputs:
        print("=" * 60)
        print(f"User: {user_input}")
        response = invoke_agent(user_input)
        print_trace(response)


if __name__ == "__main__":
    main()
