import pytest
from pydantic import ValidationError

from schemas import PracticeTaskInput
from tools import create_practice_task, estimate_task_effort, lookup_topic_overview


def test_lookup_topic_overview():
    result = lookup_topic_overview.invoke({"topic": "tool"})
    assert isinstance(result, str)
    assert len(result) > 0


def test_estimate_task_effort():
    result = estimate_task_effort.invoke(
        {"task_name": "练习 tools", "difficulty": "中等"}
    )
    assert "30" in result


def test_create_practice_task():
    result = create_practice_task.invoke(
        {
            "topic": "LangChain tools",
            "current_level": "初级",
            "output_type": "代码",
            "minutes_available": 45,
        }
    )

    assert isinstance(result, str)
    assert "LangChain tools" in result


def test_practice_task_schema_validation():
    with pytest.raises(ValidationError):
        PracticeTaskInput(
            topic="LangChain tools",
            current_level="初级",
            output_type="代码",
            minutes_available=5,
        )
