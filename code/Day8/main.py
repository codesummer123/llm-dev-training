from inspect_utils import extract_history_brief, format_state_snapshot
from workflow import build_graph


def run_thread(graph, thread_id: str, payload: dict):
    """Invoke the graph under a given thread id."""
    config = {"configurable": {"thread_id": thread_id}}
    result = graph.invoke(payload, config)

    print("=" * 60)
    print(f"[thread] {thread_id}")
    print("[final result]")
    print(result["final_summary"])

    latest_snapshot = graph.get_state(config)
    print("\n[latest snapshot]")
    print(format_state_snapshot(latest_snapshot))

    history = list(graph.get_state_history(config))
    print("\n[history brief]")
    for item in extract_history_brief(history):
        print(item)


def main():
    graph = build_graph()

    payload_a = {
        "user_goal": "我刚开始学 LangGraph，基础偏弱，想先搞清 State 和 checkpoint。",
        "user_level": "beginner",
        "needs_foundation": False,
        "track": "",
        "plan": [],
        "route_log": [],
        "final_summary": "",
    }

    payload_b = {
        "user_goal": "我想深入研究 LangGraph 的 checkpoint、state history 和恢复机制。",
        "user_level": "advanced",
        "needs_foundation": False,
        "track": "",
        "plan": [],
        "route_log": [],
        "final_summary": "",
    }

    run_thread(graph, "day8-thread-a", payload_a)
    run_thread(graph, "day8-thread-b", payload_b)


if __name__ == "__main__":
    main()
