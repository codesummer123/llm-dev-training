from pathlib import Path

from langchain_core.documents import Document


def load_markdown_documents(kb_dir: Path) -> list[Document]:
    """文件读取到Document"""

    result = []

    for file in kb_dir.glob("**/*.md"):
        with open(file, "r", encoding="utf-8") as f:
            document = Document(
                page_content=f.read(),
                metadata={"source": file.name},
            )
            result.append(document)

    return result


def format_retrieved_docs(docs: list[Document]) -> str:
    """检索到的文档转换成字符串"""

    formatted_blocks = []

    for idx, doc in enumerate(docs, 1):
        source = doc.metadata.get("source", "未知来源")
        content = doc.page_content.strip()
        formatted_blocks.append(f"【参考资料 {idx} | 来源：{source}】 \n {content}")

    return "\n".join(formatted_blocks)


def build_rag_user_prompt(question: str, context_block: str) -> str:
    """组装Prompt"""

    return f"""请你作为一名专业的知识库助手，基于以下 <context> 标签内的参考资料来回答用户的问题。
            请遵守以下规则：
            1. 你的回答必须完全基于参考资料，不要加入任何外界未提及的知识。
            2. 如果参考资料中没有包含足以回答问题的信息，或如果上下文不足，请直接回答“根据提供的资料，我无法回答该问题”，绝不能伪造事实。

            <context>
            {context_block}
            </context>

            <question>
            {question}
            </question>

            请给出清晰、准确的回答："""
