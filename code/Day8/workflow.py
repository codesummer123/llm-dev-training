from typing import Literal, TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph


class PersistentStudyState(TypedDict):
    user_goal: str
    user_level: Literal["beginner", "intermediate", "advanced"]
    needs_foundation: bool
    track: str
    plan: list[str]
    route_log: list[str]
    final_summary: str


def analyze_request(state: PersistentStudyState) -> dict:
    """Analyze the request and choose a track."""
    # TODO: Reuse Day7 logic but keep it concise.
    raise NotImplementedError("Implement analyze_request() for Day8.")


def foundation_plan(state: PersistentStudyState) -> dict:
    """Build a foundation plan."""
    # TODO: Return plan + route_log update.
    raise NotImplementedError("Implement foundation_plan() for Day8.")


def standard_plan(state: PersistentStudyState) -> dict:
    """Build a standard plan."""
    # TODO: Return plan + route_log update.
    raise NotImplementedError("Implement standard_plan() for Day8.")


def advanced_plan(state: PersistentStudyState) -> dict:
    """Build an advanced plan."""
    # TODO: Return plan + route_log update.
    raise NotImplementedError("Implement advanced_plan() for Day8.")


def finalize(state: PersistentStudyState) -> dict:
    """Create a final summary."""
    # TODO: Summarize the final route and plan.
    raise NotImplementedError("Implement finalize() for Day8.")


def route_after_analysis(state: PersistentStudyState) -> str:
    """Choose the next node based on analyzed state."""
    # TODO: Route using needs_foundation and track.
    raise NotImplementedError("Implement route_after_analysis() for Day8.")


def build_graph():
    """Build and compile a persistent LangGraph workflow."""
    graph = StateGraph(PersistentStudyState)

    graph.add_node("analyze_request", analyze_request)
    graph.add_node("foundation_plan", foundation_plan)
    graph.add_node("standard_plan", standard_plan)
    graph.add_node("advanced_plan", advanced_plan)
    graph.add_node("finalize", finalize)

    graph.add_edge(START, "analyze_request")
    graph.add_conditional_edges(
        "analyze_request",
        route_after_analysis,
        {
            "foundation_plan": "foundation_plan",
            "standard_plan": "standard_plan",
            "advanced_plan": "advanced_plan",
        },
    )
    graph.add_edge("foundation_plan", "finalize")
    graph.add_edge("standard_plan", "finalize")
    graph.add_edge("advanced_plan", "finalize")
    graph.add_edge("finalize", END)

    checkpointer = InMemorySaver()
    return graph.compile(checkpointer=checkpointer)
