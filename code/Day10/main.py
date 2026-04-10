from inspect_utils import find_checkpoint_before_node, format_history_brief
from workflow import build_graph


def main():
    graph = build_graph()
    config = {"configurable": {"thread_id": "day10-thread"}}

    initial_input = {
        "user_goal": "我想系统掌握 LangGraph 的 replay、fork 和 checkpoint 思维。",
        "user_level": "intermediate",
        "track": "",
        "plan": "",
        "final_summary": "",
    }

    print("=" * 60)
    print("[original run]")
    original_result = graph.invoke(initial_input, config)
    print(original_result["final_summary"])

    history = list(graph.get_state_history(config))
    print("\n[history]")
    for item in format_history_brief(history):
        print(item)

    checkpoint_before_draft = find_checkpoint_before_node(history, "draft_plan")

    print("\n[replay from before draft_plan]")
    replay_result = graph.invoke(None, checkpoint_before_draft.config)
    print(replay_result["final_summary"])

    print("\n[fork from before draft_plan]")
    fork_config = graph.update_state(
        checkpoint_before_draft.config,
        values={"track": "advanced"},
    )
    fork_result = graph.invoke(None, fork_config)
    print(fork_result["final_summary"])


if __name__ == "__main__":
    main()
