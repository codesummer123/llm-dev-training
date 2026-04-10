from typing import Literal, TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph


class TimeTravelState(TypedDict):
    user_goal: str
    user_level: Literal["beginner", "intermediate", "advanced"]
    track: str
    plan: str
    final_summary: str


def generate_track(state: TimeTravelState) -> dict:
    level = state.get("user_level")

    if level == "beginner":
        return {"track": "foundation"}
    elif level == "intermediate":
        return {"track": "standard"}
    else:
        return {"track": "advanced"}




def draft_plan(state: TimeTravelState) -> dict:
    plan = ""
    track = state.get("track")
    if track == "foundation":
        plan = "foundation plan"
    elif track == "standard":
        plan = "standard plan"
    else:
        plan = "advanced plan"

    return {"plan": plan}


def finalize(state: TimeTravelState) -> dict:
    """Create a final summary from the generated plan."""

    summary = f"""
        === 学习档案生成完毕 ===
        【目标】: {state.get("user_goal")}
        【原始水平】: {state.get("user_level")}
        【分配路线】: {state.get("track")}
        【定制计划】: {state.get("plan")}
        ========================
        """

    return {"final_summary": summary.strip()}


def build_graph():
    """Build and compile the Day10 workflow with checkpointing."""
    graph = StateGraph(TimeTravelState)
    graph.add_node("generate_track", generate_track)
    graph.add_node("draft_plan", draft_plan)
    graph.add_node("finalize", finalize)
    graph.add_edge(START, "generate_track")
    graph.add_edge("generate_track", "draft_plan")
    graph.add_edge("draft_plan", "finalize")
    graph.add_edge("finalize", END)

    checkpointer = InMemorySaver()
    return graph.compile(checkpointer=checkpointer)
