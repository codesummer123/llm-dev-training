from typing import Literal, TypedDict

from langgraph.graph import END, START, StateGraph


class StudyWorkflowState(TypedDict):
    user_goal: str
    user_level: Literal["beginner", "intermediate", "advanced"]
    needs_foundation: bool
    track: str
    plan: list[str]
    route_log: list[str]
    final_summary: str


def analyze_request(state: StudyWorkflowState) -> dict:
    """Analyze user level and decide whether foundation work is needed."""
    # TODO: Infer whether the user needs foundation and assign a track.
    # Suggested output keys: needs_foundation, track, route_log
    raise NotImplementedError("Implement analyze_request() for Day7.")


def foundation_plan(state: StudyWorkflowState) -> dict:
    """Build a plan for users who need foundations first."""
    # TODO: Return a small plan list and append a route log entry.
    raise NotImplementedError("Implement foundation_plan() for Day7.")


def standard_plan(state: StudyWorkflowState) -> dict:
    """Build a plan for standard learners."""
    # TODO: Return a small plan list and append a route log entry.
    raise NotImplementedError("Implement standard_plan() for Day7.")


def advanced_plan(state: StudyWorkflowState) -> dict:
    """Build a plan for advanced learners."""
    # TODO: Return a small plan list and append a route log entry.
    raise NotImplementedError("Implement advanced_plan() for Day7.")


def finalize(state: StudyWorkflowState) -> dict:
    """Create a final readable summary from the accumulated state."""
    # TODO: Summarize the chosen track and plan.
    raise NotImplementedError("Implement finalize() for Day7.")


def route_after_analysis(state: StudyWorkflowState) -> str:
    """Choose the next node based on the analyzed state."""
    # TODO: Route to foundation_plan / standard_plan / advanced_plan.
    raise NotImplementedError("Implement route_after_analysis() for Day7.")


def build_graph():
    """Build and compile the Day7 LangGraph workflow."""
    graph = StateGraph(StudyWorkflowState)

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

    return graph.compile()
