from typing import Literal

from pydantic import BaseModel, Field


class StudyTask(BaseModel):
    """Structured output schema for a normalized study task."""

    topic: str = Field(..., description="学习主题，例如 LangChain tools、messages、structured output。")
    goal: str = Field(..., description="本次学习的核心目标，应简洁明确。")
    difficulty: Literal["入门", "初级", "中级"] = Field(
        ..., description="当前任务难度等级。"
    )
    minutes_available: int = Field(
        ...,
        ge=10,
        le=180,
        description="本次可投入的学习时间，单位为分钟，范围建议在 10 到 180 之间。",
    )
    deliverable: Literal["代码", "文档", "测试", "代码+文档"] = Field(
        ..., description="本次学习任务的主要产出物。"
    )
