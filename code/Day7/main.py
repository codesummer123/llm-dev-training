from workflow import build_graph


def print_result(result: dict):
    """Print the final summary and route log."""
    print("[route_log]")
    for step in result.get("route_log", []):
        print(f"- {step}")

    print("\n[plan]")
    for idx, item in enumerate(result.get("plan", []), 1):
        print(f"{idx}. {item}")

    print("\n[final_summary]")
    print(result.get("final_summary", ""))


def main():
    graph = build_graph()

    sample_inputs = [
        {
            "user_goal": "我刚开始学 LangGraph，基础偏弱，想先搞清 State 和 Node。",
            "user_level": "beginner",
            "needs_foundation": False,
            "track": "",
            "plan": [],
            "route_log": [],
            "final_summary": "",
        },
        {
            "user_goal": "我想按正常节奏练 LangGraph 的 routing 和 graph compile。",
            "user_level": "intermediate",
            "needs_foundation": False,
            "track": "",
            "plan": [],
            "route_log": [],
            "final_summary": "",
        },
        {
            "user_goal": "我想深入研究 LangGraph 的设计边界、状态建模和复杂流程编排。",
            "user_level": "advanced",
            "needs_foundation": False,
            "track": "",
            "plan": [],
            "route_log": [],
            "final_summary": "",
        },
    ]

    for sample in sample_inputs:
        print("=" * 60)
        print(f"Goal: {sample['user_goal']}")
        result = graph.invoke(sample)
        print_result(result)


if __name__ == "__main__":
    main()
