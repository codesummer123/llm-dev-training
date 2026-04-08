from types import SimpleNamespace

from inspect_utils import extract_history_brief, format_state_snapshot


def test_format_state_snapshot():
    snapshot = SimpleNamespace(
        values={"track": "foundation"},
        next=("finalize",),
        metadata={"step": 2, "writes": {"foundation_plan": {"plan": ["x"]}}},
    )
    text = format_state_snapshot(snapshot)
    assert "foundation" in text
    assert "step=2" in text
    assert "foundation_plan" in text


def test_extract_history_brief():
    history = [
        SimpleNamespace(
            values={"track": "advanced"},
            next=(),
            metadata={"step": 2, "writes": {"finalize": {"final_summary": "done"}}},
        ),
        SimpleNamespace(
            values={"track": "advanced"},
            next=("advanced_plan",),
            metadata={"step": 1, "writes": {"analyze_request": {"track": "advanced"}}},
        ),
    ]
    result = extract_history_brief(history)
    assert isinstance(result, list)
    assert result[0]["step"] == 2
    assert "advanced" in str(result[0]["values"])
