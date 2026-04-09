from langgraph.types import Command

from inspect_utils import format_final_state, format_interrupts
from workflow import build_graph


def run_approval_flow(graph, thread_id: str, resume_value: bool):
    """Run one approval flow and then resume it with the provided decision."""
    config = {"configurable": {"thread_id": thread_id}}
    initial_input = {
        "plan_title": "Day9 LangGraph Interrupt 训练计划",
        "plan_details": "实现一个审批流，理解 interrupt / resume / thread_id / checkpoint 的关系。",
        "status": "pending",
        "review_note": "",
    }

    initial_result = graph.invoke(initial_input, config=config)
    print("=" * 60)
    print(f"[thread] {thread_id}")
    print("[interrupt]")
    print(format_interrupts(initial_result))

    final_state = graph.invoke(Command(resume=resume_value), config=config)
    print("\n[final state]")
    print(format_final_state(final_state))


def main():
    graph = build_graph()
    run_approval_flow(graph, "day9-approve-thread", True)
    run_approval_flow(graph, "day9-reject-thread", False)


if __name__ == "__main__":
    main()
