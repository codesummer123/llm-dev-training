from collections.abc import Callable

from langchain.agents import AgentState
from langchain.agents.middleware import ModelRequest, ModelResponse, before_model, wrap_model_call
from langchain.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.runtime import Runtime

def get_latest_user_text(messages: list[object]) -> str:
    """提取HumanMessage"""
    for message in reversed(messages):
        if isinstance(message,HumanMessage):
            content = message.content
            if isinstance(content, str):
                return content
            return str(content)
    return ""


def infer_user_level(text: str) -> str:
    """初步推断学习者水平"""
    lowered = text.lower()
    beginner_markers = ["入门", "基础偏弱", "刚开始", "新手", "初学"]
    advanced_markers = ["深入", "权衡", "架构", "生产", "优化", "对比"]

    if any(marker in text for marker in beginner_markers):
        return "beginner"
    if any(marker in text for marker in advanced_markers):
        return "advanced"
    return "general"


def build_dynamic_instruction(level: str) -> str:
    """根据不同水平，提供不同指令"""
    if level == "beginner":
        return "用更少术语、更多步骤化表达，优先给最小可执行下一步。"
    if level == "advanced":
        return "强调边界、权衡、失败模式和工程取舍，避免只给入门解释。"
    return "保持解释清晰，先给结论，再给一到两个最关键原因。"


def is_request_too_broad(text: str) -> bool:
    """判断请求是否过于宽泛"""
    frameworks = ["LangChain", "LangGraph", "Deep Agents", "DeepAgent", "DeepAgents"]
    broad_markers = ["全部", "一次学完", "今天讲完", "全部讲完", "全部写完"]

    hit_count = sum(1 for name in frameworks if name.lower() in text.lower())
    is_broad = any(marker in text for marker in broad_markers)

    return hit_count >= 2 and is_broad


@wrap_model_call
def inject_runtime_instruction(
    request: ModelRequest,
    handler: Callable[[ModelRequest], ModelResponse],
) -> ModelResponse:
    """动态注入Prompt"""
    latest_user_text = get_latest_user_text(list(request.messages))
    level = infer_user_level(latest_user_text)
    dynamic_instruction = build_dynamic_instruction(level)

    new_content = list(request.system_message.content_blocks) + [
        {"type": "text", "text": f"运行时补充要求：{dynamic_instruction}"}
    ]
    new_system_message = SystemMessage(content=new_content)
    return handler(request.override(system_message=new_system_message))


@before_model(can_jump_to=["end"])
def block_over_broad_request(state: AgentState, runtime: Runtime):
    """如果请求过于宽泛，则短路"""
    latest_user_text = get_latest_user_text(list(state["messages"]))
    if not is_request_too_broad(latest_user_text):
        return None

    return {
        "messages": [
            AIMessage(
                content = "这个请求范围过宽。我建议先只选 LangChain、LangGraph、Deep Agents 中的一个，再限定今天的目标，例如“只做工具设计”或“只做 memory”。"
            )
        ],
        "jump_to": "end",
    }