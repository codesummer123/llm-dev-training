from workflow import (
    advanced_plan,
    foundation_plan,
    route_after_analysis,
    standard_plan,
)


def test_route_after_analysis_foundation():
    state = {
        "user_goal": "基础偏弱",
        "user_level": "beginner",
        "needs_foundation": True,
        "track": "foundation",
        "plan": [],
        "route_log": ["analyze_request"],
        "final_summary": "",
    }
    assert route_after_analysis(state) == "foundation_plan"


def test_route_after_analysis_advanced():
    state = {
        "user_goal": "深入研究",
        "user_level": "advanced",
        "needs_foundation": False,
        "track": "advanced",
        "plan": [],
        "route_log": ["analyze_request"],
        "final_summary": "",
    }
    assert route_after_analysis(state) == "advanced_plan"


def test_foundation_plan():
    state = {
        "user_goal": "基础偏弱",
        "user_level": "beginner",
        "needs_foundation": True,
        "track": "foundation",
        "plan": [],
        "route_log": [],
        "final_summary": "",
    }
    result = foundation_plan(state)
    assert isinstance(result["plan"], list)
    assert len(result["plan"]) > 0


def test_standard_plan():
    state = {
        "user_goal": "常规练习",
        "user_level": "intermediate",
        "needs_foundation": False,
        "track": "standard",
        "plan": [],
        "route_log": [],
        "final_summary": "",
    }
    result = standard_plan(state)
    assert isinstance(result["plan"], list)
    assert len(result["plan"]) > 0


def test_advanced_plan():
    state = {
        "user_goal": "深入研究",
        "user_level": "advanced",
        "needs_foundation": False,
        "track": "advanced",
        "plan": [],
        "route_log": [],
        "final_summary": "",
    }
    result = advanced_plan(state)
    assert isinstance(result["plan"], list)
    assert len(result["plan"]) > 0
