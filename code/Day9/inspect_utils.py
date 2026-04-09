import json


def format_interrupts(result) -> str:
    return result.get("__interrupt__")


def format_final_state(state: dict) -> str:
    return f"""
        plan_title={state.get('plan_title')},
        plan_details={state.get('plan_details')},
        status={state.get('status')},
        review_note={state.get('review_note')},
    """
