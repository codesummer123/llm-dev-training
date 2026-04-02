from pydantic import ValidationError
import pytest

from schemas import StudyTask


def test_study_task_valid():
    task = StudyTask(
        topic="LangChain messages",
        goal="理解消息结构并观察执行轨迹",
        difficulty="初级",
        minutes_available=45,
        deliverable="代码+文档",
    )
    assert task.minutes_available == 45


def test_study_task_minutes_validation():
    with pytest.raises(ValidationError):
        StudyTask(
            topic="LangChain messages",
            goal="理解消息结构并观察执行轨迹",
            difficulty="初级",
            minutes_available=5,
            deliverable="代码",
        )


def test_study_task_difficulty_validation():
    with pytest.raises(ValidationError):
        StudyTask(
            topic="LangChain messages",
            goal="理解消息结构并观察执行轨迹",
            difficulty="高级",
            minutes_available=45,
            deliverable="代码",
        )
