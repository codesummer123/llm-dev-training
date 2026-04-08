def format_state_snapshot(snapshot) -> str:
    """Format a LangGraph StateSnapshot into a readable string."""
    # TODO: Include at least values / next / metadata.step / metadata.writes.
    raise NotImplementedError("Implement format_state_snapshot() for Day8.")


def extract_history_brief(history) -> list[dict]:
    """Extract a compact summary from a sequence of StateSnapshot objects."""
    # TODO: Return a list of small dicts with step / next / values / writes.
    raise NotImplementedError("Implement extract_history_brief() for Day8.")
