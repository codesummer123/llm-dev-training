def format_state_snapshot(snapshot) -> str:
    """Format a LangGraph StateSnapshot into a readable string."""
    # 提前当前字典值
    values = snapshot.values

    # 下一步到哪个节点
    next_nodes = snapshot.next

    # 提取元数据
    metadata = snapshot.metadata or {}
    step = metadata.get("step", "未知")
    writes = metadata.get("writes", "无写入")

    # 拼字符串
    formatted_str = f"""
    step={step}
    next={next_nodes}
    values={values}
    writes={writes}
    """

    return formatted_str


def extract_history_brief(history) -> list[dict]:
    """Extract a compact summary from a sequence of StateSnapshot objects."""
    brief_list = []

    for snapshot in history:
        metadata = snapshot.metadata or {}
        print(f"metadata: {metadata}")
        snap_brief = {
            "step": metadata.get("step"),
            "next": snapshot.next,
            "values": snapshot.values,
            "writes": metadata.get("writes"),
        }
        brief_list.append(snap_brief)

    return brief_list

