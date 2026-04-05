from pathlib import Path

from langchain_core.documents import Document

from rag_utils import build_rag_user_prompt, format_retrieved_docs, load_markdown_documents


def test_load_markdown_documents(tmp_path: Path):
    file_path = tmp_path / "sample.md"
    file_path.write_text("# Title\n\nhello rag", encoding="utf-8")

    docs = load_markdown_documents(tmp_path)
    assert len(docs) == 1
    assert docs[0].metadata["source"] == "sample.md"


def test_format_retrieved_docs():
    docs = [
        Document(page_content="LangChain supports middleware.", metadata={"source": "langchain_notes.md"}),
        Document(page_content="LangGraph supports interrupts.", metadata={"source": "langgraph_notes.md"}),
    ]
    result = format_retrieved_docs(docs)
    assert "langchain_notes.md" in result
    assert "middleware" in result
    assert "langgraph_notes.md" in result


def test_build_rag_user_prompt():
    prompt = build_rag_user_prompt(
        "什么是 middleware？",
        "Source: langchain_notes.md\nContent: middleware 的价值是运行时控制。",
    )
    assert "什么是 middleware？" in prompt
    assert "langchain_notes.md" in prompt
    assert "如果上下文不足" in prompt
