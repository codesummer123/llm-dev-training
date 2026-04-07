from typing import Literal, TypedDict
from langgraph.graph import END, START, StateGraph


class StudyWorkflowState(TypedDict):
    """定义状态"""
    user_goal: str
    user_level: Literal["beginner", "intermediate", "advanced"]
    needs_foundation: bool
    track: str
    plan: list[str]
    route_log: list[str]
    final_summary: str


def analyze_request(state: StudyWorkflowState) -> dict:
    """Analyze user level and decide whether foundation work is needed."""

    if state["user_level"] == "beginner":
        return {
            "needs_foundation": True,
            "track": "foundation",
            "route_log": ["analyze_request"],
        }
    elif state["user_level"] == "intermediate":
        return {
            "needs_foundation": False,
            "track": "standard",
            "route_log": ["analyze_request"],
        }
    elif state["user_level"] == "advanced":
        return {
            "needs_foundation": False,
            "track": "advanced",
            "route_log": ["analyze_request"],
        }
    return {}


def foundation_plan(state: StudyWorkflowState) -> dict:
    """Build a plan for users who need foundations first."""

    new_log = state.get("route_log", []) + ["foundation_plan"]
    return {"plan": ["需要补充基础：先看官网打好基础。"], "route_log": new_log}


def standard_plan(state: StudyWorkflowState) -> dict:
    """Build a plan for standard learners."""

    new_log = state.get("route_log", []) + ["standard_plan"]
    return {"plan": ["常规计划：先看一遍官网，再找教程跟着学。"], "route_log": new_log}


def advanced_plan(state: StudyWorkflowState) -> dict:
    """Build a plan for advanced learners."""

    new_log = state.get("route_log", []) + ["advanced_plan"]
    return {"plan": ["高级计划：直接上手项目。"], "route_log": new_log}


def finalize(state: StudyWorkflowState) -> dict:
    """Create a final readable summary from the accumulated state."""

    track = state.get("track", "未知路线")
    plan_str = "\n".join(state.get("plan", []))
    path_str = "\n".join(state.get("route_log", []))

    summary = f"""--- 专属学习规划 ---
【选择路线】: {track}
【学习计划】: {plan_str}
【内部执行轨迹】: {path_str}"""

    return {"final_summary": summary}


def route_after_analysis(state: StudyWorkflowState) -> str:
    """Choose the next node based on the analyzed state."""

    if state.get("needs_foundation", False):
        return "foundation_plan"

    track = state.get("track", "")
    if track == "standard":
        return  "standard_plan"
    else:
        return "advanced_plan"


def build_graph():
    """创建图"""

    # 初始化图，添加状态
    graph = StateGraph(StudyWorkflowState)

    # 添加节点
    graph.add_node("analyze_request", analyze_request)
    graph.add_node("foundation_plan", foundation_plan)
    graph.add_node("standard_plan", standard_plan)
    graph.add_node("advanced_plan", advanced_plan)
    graph.add_node("finalize", finalize)

    # 添加边
    graph.add_edge(START, "analyze_request")
    graph.add_conditional_edges(
        "analyze_request",
        route_after_analysis,
        {
            "foundation_plan": "foundation_plan",
            "standard_plan": "standard_plan",
            "advanced_plan": "advanced_plan",
        }
    )
    graph.add_edge("foundation_plan", "finalize")
    graph.add_edge("standard_plan", "finalize")
    graph.add_edge("advanced_plan", "finalize")
    graph.add_edge("finalize", END)

    return graph.compile()
