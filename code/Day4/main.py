import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver

from memory_utils import trim_message_like_items
from prompts import SYSTEM_PROMPT

load_dotenv()


def build_model():
    """Initialize a chat model for Day4."""
    model_name = (
        os.getenv("DAY4_MODEL")
        or os.getenv("DAY3_MODEL")
        or os.getenv("DAY2_MODEL")
        or os.getenv("DAY1_MODEL")
    )
    if not model_name:
        raise ValueError("Please set DAY4_MODEL, DAY3_MODEL, DAY2_MODEL, or DAY1_MODEL.")

    return init_chat_model(model_name, temperature=0, max_retries=3, timeout=20.0)


def build_agent():
    """Create a Day4 agent with short-term memory support."""
    model = build_model()
    checkpointer = InMemorySaver()

    # TODO: Connect the checkpointer to the agent so the same thread_id can retain context.
    return create_agent(
        model=model,
        tools=[],
        system_prompt=SYSTEM_PROMPT,
        checkpointer=checkpointer,
    )


def invoke_with_thread(agent, user_input: str, thread_id: str):
    """Invoke the agent under a specific thread id."""
    return agent.invoke(
        {"messages": [{"role": "user", "content": user_input}]},
        config={"configurable": {"thread_id": thread_id}},
    )


def print_last_answer(response):
    """Print the final message content."""
    messages = response.get("messages", [])
    if not messages:
        print("[no messages]")
        return
    print(messages[-1].content)


def inspect_trim_preview(response, keep_last: int = 4):
    """Preview how your trimming rule would behave on the current message list."""
    messages = response.get("messages", [])
    trimmed = trim_message_like_items(messages, keep_last=keep_last)
    print(f"[trim preview] before={len(messages)} after={len(trimmed)}")


def main():
    agent = build_agent()

    print("=" * 60)
    print("Same thread demo")
    thread_a = "day4-thread-a"
    response1 = invoke_with_thread(
        agent,
        "我现在正在学 LangChain，基础偏弱，每天只有 2 小时。",
        thread_a,
    )
    print_last_answer(response1)

    response2 = invoke_with_thread(
        agent,
        "基于我刚才的情况，今天适合练什么？",
        thread_a,
    )
    print_last_answer(response2)
    inspect_trim_preview(response2)

    print("=" * 60)
    print("Different thread demo")
    thread_b = "day4-thread-b"
    response3 = invoke_with_thread(
        agent,
        "基于我刚才的情况，今天适合练什么？",
        thread_b,
    )
    print_last_answer(response3)


if __name__ == "__main__":
    main()
