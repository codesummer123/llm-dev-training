from typing import Literal, TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt


class ApprovalState(TypedDict):
    plan_title: str
    plan_details: str
    status: Literal["pending", "approved", "rejected"]
    review_note: str


def approval_node(state: ApprovalState) -> Command[Literal["approve_node", "reject_node"]]:
    """Pause execution and wait for an external approval decision."""
    # TODO: Call interrupt(...) with a JSON-serializable payload that includes the plan.
    # The resume value should become the decision here.
    raise NotImplementedError("Implement approval_node() for Day9.")


def approve_node(state: ApprovalState) -> dict:
    """Mark the plan as approved."""
    # TODO: Update status and review_note.
    raise NotImplementedError("Implement approve_node() for Day9.")


def reject_node(state: ApprovalState) -> dict:
    """Mark the plan as rejected."""
    # TODO: Update status and review_note.
    raise NotImplementedError("Implement reject_node() for Day9.")


def build_graph():
    """Build and compile the Day9 approval workflow."""
    builder = StateGraph(ApprovalState)
    builder.add_node("approval_node", approval_node)
    builder.add_node("approve_node", approve_node)
    builder.add_node("reject_node", reject_node)

    builder.add_edge(START, "approval_node")
    builder.add_edge("approve_node", END)
    builder.add_edge("reject_node", END)

    checkpointer = InMemorySaver()
    return builder.compile(checkpointer=checkpointer)
