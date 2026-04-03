from typing import Sequence


def trim_message_like_items(items: Sequence[object], keep_last: int = 4) -> list[object]:
    """截取逻辑"""

    # 如果总数不够，直接返回
    if len(items) <= keep_last + 1:
        return list(items)

    # 否则取第一条和最后keep_last条
    first_item = items[0]
    keep_items = items[-keep_last:]
    return [first_item] + list(keep_items)
