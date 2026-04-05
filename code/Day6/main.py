import os
from pathlib import Path

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

from prompts import RAG_SYSTEM_PROMPT
from rag_utils import build_rag_user_prompt, format_retrieved_docs, load_markdown_documents

load_dotenv()

BASE_DIR = Path(__file__).parent
KB_DIR = BASE_DIR / "kb"


def build_model():
    """Initialize the chat model used for answer generation."""
    model_name = os.getenv("DAY6_MODEL")
    if not model_name:
        raise ValueError("Please set DAY6_MODEL or a previous DAY*_MODEL.")

    return init_chat_model(model_name, temperature=0, max_retries=3, timeout=20.0)


def build_embeddings():
    """Initialize an embeddings model for indexing and retrieval."""
    # TODO: Pick an embeddings provider that matches your local environment.
    # Example official directions include OpenAIEmbeddings / Google / HuggingFace / Fake embeddings.
    raise NotImplementedError("Implement build_embeddings() for Day6.")


def build_retriever():
    """Load local docs, split them, index them, and return a retriever."""
    docs = load_markdown_documents(KB_DIR)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=80,
    )
    splits = text_splitter.split_documents(docs)

    embeddings = build_embeddings()
    vector_store = InMemoryVectorStore(embedding=embeddings)
    vector_store.add_documents(splits)
    return vector_store.as_retriever(search_kwargs={"k": 3})


def answer_without_rag(question: str):
    """Ask the model directly without retrieval."""
    model = build_model()
    return model.invoke(question)


def answer_with_rag(question: str):
    """Run a minimal 2-step RAG flow."""
    retriever = build_retriever()
    retrieved_docs = retriever.invoke(question)
    context_block = format_retrieved_docs(retrieved_docs)
    final_prompt = build_rag_user_prompt(question, context_block)

    model = build_model()
    response = model.invoke(
        [
            {"role": "system", "content": RAG_SYSTEM_PROMPT},
            {"role": "user", "content": final_prompt},
        ]
    )
    return response, retrieved_docs


def print_retrieved_docs(docs):
    """Print retrieved docs for inspection."""
    print("[retrieved docs]")
    for idx, doc in enumerate(docs, 1):
        source = doc.metadata.get("source", "unknown")
        print(f"{idx}. source={source}")
        print(doc.page_content[:180])
        print()


def main():
    questions = [
        "LangChain middleware 的核心价值是什么？",
        "Deep Agents 的异步 subagents 适合什么场景？",
    ]

    for question in questions:
        print("=" * 60)
        print(f"Question: {question}")

        print("\n[without rag]")
        direct = answer_without_rag(question)
        print(direct.content)

        print("\n[with rag]")
        rag_response, retrieved_docs = answer_with_rag(question)
        print_retrieved_docs(retrieved_docs)
        print(rag_response.content)


if __name__ == "__main__":
    main()
