from langchain.tools import tool


@tool
def lookup_concept(concept: str) -> str:
    """Look up a short explanation for a framework concept."""
    # TODO: Replace this placeholder with a small hard-coded glossary.
    # Suggested concepts: langchain, langgraph, tool, agent, prompt.
    raise NotImplementedError("Implement lookup_concept() for Day1.")


@tool
def suggest_next_step(current_topic: str) -> str:
    """Suggest the next concrete practice step for the given topic."""
    # TODO: Return one practical next action, not a long essay.
    raise NotImplementedError("Implement suggest_next_step() for Day1.")


@tool
def estimate_study_time(task_name: str, difficulty: str) -> str:
    """Estimate how long a study task may take based on its difficulty."""
    # TODO: Design a simple deterministic rule.
    # Example: easy -> 15m, medium -> 30m, hard -> 45m.
    raise NotImplementedError("Implement estimate_study_time() for Day1.")
