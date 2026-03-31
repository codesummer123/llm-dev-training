import os

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

from prompts import SYSTEM_PROMPT
from tools import estimate_study_time, lookup_concept, suggest_next_step


def build_model():
    """Initialize a tool-calling chat model from an environment variable."""
    model_name = os.getenv("DAY1_MODEL")
    if not model_name:
        raise ValueError("Please set the DAY1_MODEL environment variable.")

    # TODO: Adjust model kwargs if you want tighter control over retries/timeouts.
    return init_chat_model(model_name, temperature=0)


def build_agent():
    """Create the Day1 learning assistant agent."""
    tools = [lookup_concept, suggest_next_step, estimate_study_time]

    # TODO: Confirm whether you want to pass the model instance or a model string.
    # Recommended for today: pass the initialized model instance.
    model = build_model()
    return create_agent(model=model, tools=tools, system_prompt=SYSTEM_PROMPT)


def run_demo(user_input: str):
    """Run one agent invocation and return the raw response."""
    agent = build_agent()

    # TODO: Inspect the returned structure carefully.
    # Hint: the input shape follows the LangChain agent docs.
    return agent.invoke({"messages": [{"role": "user", "content": user_input}]})


def main():
    sample_question = "请解释一下 LangChain 里的 tool 是什么，并给我一个今天适合的下一步练习。"
    response = run_demo(sample_question)
    print(response)


if __name__ == "__main__":
    main()
