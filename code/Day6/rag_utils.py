from pathlib import Path

from langchain_core.documents import Document


def load_markdown_documents(kb_dir: Path) -> list[Document]:
    """Load local markdown files into Document objects with source metadata."""
    # TODO: Read all *.md files under kb_dir and convert them to Document objects.
    # Each document should preserve at least one metadata field: source.
    raise NotImplementedError("Implement load_markdown_documents() for Day6.")


def format_retrieved_docs(docs: list[Document]) -> str:
    """Format retrieved docs into a grounded context block."""
    # TODO: Build a stable string that includes source metadata and page_content.
    raise NotImplementedError("Implement format_retrieved_docs() for Day6.")


def build_rag_user_prompt(question: str, context_block: str) -> str:
    """Construct the final user prompt for 2-step RAG generation."""
    # TODO: Make the question and retrieved context explicit and easy for the model to use.
    raise NotImplementedError("Implement build_rag_user_prompt() for Day6.")
