import os
from typing import Any

from dotenv import load_dotenv
from langchain.agents import AgentState, create_agent
from langchain.agents.middleware import before_model
from langchain.chat_models import init_chat_model
from langchain.messages import RemoveMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import REMOVE_ALL_MESSAGES
from langgraph.runtime import Runtime
from memory_utils import trim_message_like_items
from prompts import SYSTEM_PROMPT

load_dotenv()


@before_model
def trim_short_term_memory(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
    """每次调用模型前先修剪消息"""
    messages = state["messages"]
    trimmed = trim_message_like_items(messages, keep_last=4)

    if len(trimmed) == len(messages):
        return None

    return {
        "messages": [
            RemoveMessage(id=REMOVE_ALL_MESSAGES),
            *trimmed,
        ]
    }


def build_model():
    """初始化模型"""
    model_name = os.getenv("DAY4_MODEL")

    if not model_name:
        raise ValueError("Please set Model Name")

    return init_chat_model(model_name, temperature=0, max_retries=3, timeout=20.0)


def build_agent():
    """创建支持短期记忆的Agent"""
    model = build_model()
    checkpointer = InMemorySaver()

    # 给Agent添加 checkpointer，并在每次模型调用前自动裁剪消息并写回线程状态
    return create_agent(
        model=model,
        tools=[],
        system_prompt=SYSTEM_PROMPT,
        middleware=[trim_short_term_memory],
        checkpointer=checkpointer,
    )


def build_agent_without_checkpointer():
    """创建不带checkpointer的Agent"""
    model = build_model()

    return create_agent(
        model=model,
        tools=[],
        system_prompt=SYSTEM_PROMPT,
    )


def invoke_with_thread(agent, user_input: str, thread_id: str):
    """区分thread_id的方式调用Agent"""
    return agent.invoke(
        {"messages": [{"role": "user", "content": user_input}]},
        config={"configurable": {"thread_id": thread_id}},
    )


def print_last_answer(response):
    """打印最终的messages内容"""
    messages = response.get("messages", [])
    if not messages:
        print("[no messages]")
        return
    print(messages[-1].content)


def print_thread_state_size(agent, thread_id: str):
    """查看当前 thread 中实际持久化下来的消息数量。"""
    snapshot = agent.get_state({"configurable": {"thread_id": thread_id}})
    messages = snapshot.values.get("messages", [])
    print(f"[persisted thread state] thread_id={thread_id} message_count={len(messages)}")


def main():
    agent = build_agent()

    print("=" * 60)

    print("\n[短期记忆-第一次回答]")
    thread_a = "day4-thread-a"
    response1 = invoke_with_thread(
        agent,
        "我现在正在学 LangChain，基础偏弱，每天只有 2 小时。",
        thread_a,
    )
    print_last_answer(response1)

    print("\n[短期记忆-第二次回答]")
    response2 = invoke_with_thread(
        agent,
        "基于我刚才的情况，今天适合练什么？",
        thread_a,
    )
    print_last_answer(response2)

    print("\n[短期记忆-第三次回答]")
    response21 = invoke_with_thread(
        agent,
        "针对今天适合的练习，我需要做哪些技术准备",
        thread_a,
    )
    print_last_answer(response21)
    print_thread_state_size(agent, thread_a)

    print("\n[短期记忆-裁剪后继续回答]")
    response22 = invoke_with_thread(
        agent,
        "结合我们前面的讨论，给我一个今天的最小练习闭环。",
        thread_a,
    )
    print_last_answer(response22)
    print_thread_state_size(agent, thread_a)

    print("=" * 60)
    print("[短期记忆-新thread]")
    thread_b = "day4-thread-b"
    response3 = invoke_with_thread(
        agent,
        "基于我刚才的情况，今天适合练什么？",
        thread_b,
    )
    print_last_answer(response3)

    print("=" * 60)
    print("\n[无短期记忆-第一次回答]")
    thread_c = "day4-thread-c"
    agent_without_checkpointer = build_agent_without_checkpointer()
    response4 = invoke_with_thread(
        agent_without_checkpointer,
        "我先在打算学习DeepAgent，基础偏弱，每天两个小时",
        thread_c,
    )
    print_last_answer(response4)

    print("\n[无短期记忆-第二次回答]")
    response5 = invoke_with_thread(
        agent_without_checkpointer,
        "基于我刚说的情况，我该如何练习？",
        thread_c,
    )
    print_last_answer(response5)

if __name__ == "__main__":
    main()
