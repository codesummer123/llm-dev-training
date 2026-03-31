
import pytest
from tools import estimate_study_time, lookup_concept, suggest_next_step

def test_lookup_concept():
    result = lookup_concept.invoke({"concept": "tool"})
    assert "交互能力" in result or "功能接口" in result


def test_suggest_next_step():
    result = suggest_next_step.invoke({"current_topic": "agent"})
    assert isinstance(result, str)
    assert len(result) > 0


def test_estimate_study_time():
    result = estimate_study_time.invoke(
        {"task_name": "learn tools", "difficulty": "中等"}
    )
    assert "30" in result

# 执行测试：python -m pytest tests/