from typing import Literal

from pydantic import BaseModel, Field


class PracticeTaskInput(BaseModel):
    """Input schema for generating a focused practice task."""

    topic: str = Field(
        ...,
        description="要练习的主题，例如 LangChain tools、prompt design、messages。",
    )
    current_level: Literal["入门", "初级", "中级"] = Field(
        ...,
        description="用户当前熟练度，用于控制任务难度。",
    )
    output_type: Literal["代码", "文档", "测试"] = Field(
        ...,
        description="期望输出形式，用于决定练习任务更偏实现还是更偏表达。",
    )
    minutes_available: int = Field(
        ...,
        ge=10,
        le=120,
        description="今天可投入的学习时间，单位为分钟，建议限制在 10 到 120 之间。",
    )
