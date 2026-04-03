from memory_utils import trim_message_like_items


def test_trim_keeps_all_when_short():
    items = ["system", "u1", "a1"]
    result = trim_message_like_items(items, keep_last=4)
    assert result == items


def test_trim_preserves_first_and_recent_items():
    items = ["system", "u1", "a1", "u2", "a2", "u3", "a3"]
    result = trim_message_like_items(items, keep_last=3)
    assert result == ["system", "a2", "u3", "a3"]


def test_trim_returns_new_list():
    items = ["system", "u1", "a1", "u2", "a2"]
    result = trim_message_like_items(items, keep_last=2)
    assert result is not items
