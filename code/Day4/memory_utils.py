from typing import Sequence


def trim_message_like_items(items: Sequence[object], keep_last: int = 4) -> list[object]:
    """Keep the most relevant recent items while preserving the first item when possible."""
    # TODO: Implement a simple trimming rule:
    # 1) If the total number of items is small enough, return all items.
    # 2) Otherwise preserve the first item and keep only the last N remaining items.
    # 3) Return a new list instead of mutating the input.
    raise NotImplementedError("Implement trim_message_like_items() for Day4.")
