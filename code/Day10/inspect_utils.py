def find_checkpoint_before_node(history, node_name: str):
    return next((s for s in history if node_name in s.next), None)


def format_history_brief(history) -> list[dict]:
    summary = []

    for item in history:
        # 得到元数据
        metadata = item.metadata or {}

        # 得到checkpoint_id
        config = item.config or {}
        configurable = config.get("configurable", {})
        checkpoint_id = configurable.get("checkpoint_id", "未知ID")

        # 返回字典
        summary.append({
            "step": metadata.get("step"),
            "next": item.next,
            "checkpoint_id": checkpoint_id,
        })

    return summary