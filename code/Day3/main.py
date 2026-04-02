import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

from prompts import SYSTEM_PROMPT
from schemas import StudyTask

load_dotenv()


def build_model():
    """Initialize a chat model for Day3."""
    model_name = os.getenv("DAY3_MODEL") or os.getenv("DAY2_MODEL") or os.getenv("DAY1_MODEL")
    if not model_name:
        raise ValueError("Please set DAY3_MODEL, DAY2_MODEL, or DAY1_MODEL.")

    return init_chat_model(model_name, temperature=0, max_retries=3, timeout=20.0)


def build_text_agent():
    """Create a plain-text agent for comparison."""
    model = build_model()
    return create_agent(model=model, tools=[], system_prompt=SYSTEM_PROMPT)


def build_structured_agent():
    """Create an agent that returns structured output."""
    model = build_model()
    # TODO: Bind the StudyTask schema as the response_format.
    return create_agent(
        model=model,
        tools=[],
        system_prompt=SYSTEM_PROMPT,
        response_format=StudyTask,
    )


def invoke_text_mode(user_input: str):
    """Return the raw response for plain-text mode."""
    agent = build_text_agent()
    return agent.invoke({"messages": [{"role": "user", "content": user_input}]})


def invoke_structured_mode(user_input: str):
    """Return the raw response for structured mode."""
    agent = build_structured_agent()
    return agent.invoke({"messages": [{"role": "user", "content": user_input}]})


def print_messages(response):
    """Print a lightweight message trace."""
    messages = response.get("messages", [])
    print("[messages]")
    for idx, message in enumerate(messages, 1):
        print(f"{idx}. type={getattr(message, 'type', 'unknown')}")
        print(f"   content={message.content}")


def print_structured_result(response):
    """Print the structured result if present."""
    # TODO: Inspect the response dict and print the structured output field if it exists.
    structured_result = response.get("structured_response")
    print("[structured_response]")
    print(structured_result)


def main():
    user_input = "我今天有 45 分钟，想系统练习 LangChain messages，并且最后产出代码和简短文档。"

    print("=" * 60)
    print("Text mode")
    text_response = invoke_text_mode(user_input)
    print_messages(text_response)

    print("=" * 60)
    print("Structured mode")
    structured_response = invoke_structured_mode(user_input)
    print_messages(structured_response)
    print_structured_result(structured_response)


if __name__ == "__main__":
    main()
