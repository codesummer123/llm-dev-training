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
    """暂停执行，等待外部决策"""

    # 外部展示信息
    payload_for_human = {
        "审批请求": "请审核以下计划",
        "标题": state.get("plan_title"),
        "详情": state.get("plan_details")
    }

    # 获取外部决策
    decision = interrupt(payload_for_human)
    print(f"decision={decision}")

    # 决定走哪个分支
    if decision:
        return Command(goto="approve_node")
    else:
        return Command(goto="reject_node")



def approve_node(state: ApprovalState) -> dict:
    """批准"""
    return {
        "status": "approved",
        "review_note": "审批通过"
    }



def reject_node(state: ApprovalState) -> dict:
    """拒绝"""
    return {
        "status": "rejected",
        "review_note": "审批失败"
    }


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
