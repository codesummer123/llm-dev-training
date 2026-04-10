from types import SimpleNamespace

from inspect_utils import find_checkpoint_before_node, format_history_brief


def test_find_checkpoint_before_node():
    history = [
        SimpleNamespace(next=(), metadata={"step": 2}, config={"configurable": {"checkpoint_id": "c3"}}),
        SimpleNamespace(next=("draft_plan",), metadata={"step": 1}, config={"configurable": {"checkpoint_id": "c2"}}),
        SimpleNamespace(next=("generate_track",), metadata={"step": 0}, config={"configurable": {"checkpoint_id": "c1"}}),
    ]
    result = find_checkpoint_before_node(history, "draft_plan")
    assert result.config["configurable"]["checkpoint_id"] == "c2"


def test_format_history_brief():
    history = [
        SimpleNamespace(next=(), metadata={"step": 2}, config={"configurable": {"checkpoint_id": "c3"}}),
        SimpleNamespace(next=("draft_plan",), metadata={"step": 1}, config={"configurable": {"checkpoint_id": "c2"}}),
    ]
    result = format_history_brief(history)
    assert result[0]["step"] == 2
    assert result[0]["checkpoint_id"] == "c3"
