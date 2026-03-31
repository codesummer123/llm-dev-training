import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

from prompts import SYSTEM_PROMPT
from tools import estimate_study_time, lookup_concept, suggest_next_step

load_dotenv()

def build_model():
    """Initialize a tool-calling chat model from an environment variable."""
    model_name = os.getenv("DAY1_MODEL")
    if not model_name:
        raise ValueError("Please set the DAY1_MODEL environment variable.")

    # 返回Model，超时时间15秒，重试3次
    return init_chat_model(model_name, temperature=0, max_retries=3, timeout=15.0)


def build_agent():
    """Create the Day1 learning assistant agent."""
    tools = [lookup_concept, suggest_next_step, estimate_study_time]

    # 使用传实例的方式来创建Agent
    model = build_model()
    return create_agent(model=model, tools=tools, system_prompt=SYSTEM_PROMPT)


def run_demo(user_input: str):
    """Run one agent invocation and return the raw response."""
    agent = build_agent()

    # 提炼最终的回答内容，而不是中间的结果
    response = agent.invoke({"messages": [{"role": "user", "content": user_input}]})
    return response["messages"][-1].content


def main():
    sample_question = "请解释一下 LangChain 里的 tool 是什么，并给我一个今天适合的下一步练习。"
    response = run_demo(sample_question)
    print(response)


if __name__ == "__main__":
    main()
