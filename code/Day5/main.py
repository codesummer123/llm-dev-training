import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

from middleware import block_over_broad_request, inject_runtime_instruction
from prompts import BASE_SYSTEM_PROMPT

load_dotenv()


def build_model():
    """初始化模型"""
    model_name = os.getenv("DAY5_MODEL")
    if not model_name:
        raise ValueError("Please set DAY5_MODEL, DAY4_MODEL, DAY3_MODEL, DAY2_MODEL, or DAY1_MODEL.")

    return init_chat_model(model_name, temperature=0, max_retries=3, timeout=20.0)


def build_agent():
    """创建Agent"""
    model = build_model()
    return create_agent(
        model=model,
        tools=[],
        system_prompt=BASE_SYSTEM_PROMPT,
        middleware=[block_over_broad_request, inject_runtime_instruction],
    )


def invoke_agent(agent, user_input: str):
    """Agent调用"""
    return agent.invoke({"messages": [{"role": "user", "content": user_input}]})


def print_last_answer(response):
    """打印最终返回的message"""
    messages = response.get("messages", [])
    if not messages:
        print("[no messages]")
        return
    print(messages[-1].content)


def main():
    agent = build_agent()

    sample_inputs = [
        "我是入门阶段，基础偏弱，今天只想学 LangChain middleware，给我一个最小练习步骤。",
        "我已经做过几个 agent demo，请从生产边界和工程权衡角度讲讲 middleware 的价值。",
        "今天把 LangChain、LangGraph、Deep Agents 全部讲完并写完代码。",
    ]

    for user_input in sample_inputs:
        print("=" * 60)
        print(f"User: {user_input}")
        response = invoke_agent(agent, user_input)
        print_last_answer(response)


if __name__ == "__main__":
    main()
