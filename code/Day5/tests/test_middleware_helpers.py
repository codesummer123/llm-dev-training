from middleware import (
    build_dynamic_instruction,
    infer_user_level,
    is_request_too_broad,
)


def test_infer_user_level_beginner():
    level = infer_user_level("我是入门阶段，基础偏弱，刚开始学 LangChain。")
    assert level == "beginner"


def test_infer_user_level_advanced():
    level = infer_user_level("请从架构权衡和生产优化角度分析 middleware。")
    assert level == "advanced"


def test_build_dynamic_instruction():
    text = build_dynamic_instruction("beginner")
    assert "步骤化" in text


def test_is_request_too_broad():
    assert is_request_too_broad("今天把 LangChain、LangGraph、Deep Agents 全部讲完并写完代码。") is True


def test_is_request_not_too_broad():
    assert is_request_too_broad("今天我只想练 LangChain middleware。") is False
