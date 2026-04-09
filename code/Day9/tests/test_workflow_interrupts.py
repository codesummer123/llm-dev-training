from langgraph.types import Command

from workflow import build_graph


def test_interrupt_and_approve():
    graph = build_graph()
    config = {"configurable": {"thread_id": "test-approve"}}

    initial = graph.invoke(
        {
            "plan_title": "plan",
            "plan_details": "details",
            "status": "pending",
            "review_note": "",
        },
        config=config,
    )
    assert "__interrupt__" in initial

    final_state = graph.invoke(Command(resume=True), config=config)
    assert final_state["status"] == "approved"


def test_interrupt_and_reject():
    graph = build_graph()
    config = {"configurable": {"thread_id": "test-reject"}}

    initial = graph.invoke(
        {
            "plan_title": "plan",
            "plan_details": "details",
            "status": "pending",
            "review_note": "",
        },
        config=config,
    )
    assert "__interrupt__" in initial

    final_state = graph.invoke(Command(resume=False), config=config)
    assert final_state["status"] == "rejected"
