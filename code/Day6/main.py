import os
from pathlib import Path

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel
from langchain_core.vectorstores import InMemoryVectorStore, VectorStoreRetriever
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings import init_embeddings

from prompts import RAG_SYSTEM_PROMPT
from rag_utils import build_rag_user_prompt, format_retrieved_docs, load_markdown_documents

load_dotenv()

BASE_DIR = Path(__file__).parent
KB_DIR = BASE_DIR / "kb"


def build_model():
    """初始化模型"""
    model_name = os.getenv("DAY6_MODEL")
    if not model_name:
        raise ValueError("请设置模型.")

    return init_chat_model(model_name, temperature=0, max_retries=3, timeout=20.0)


def build_embeddings():
    """设置embeddings模型"""
    embedding_model = os.getenv("EMBEDDING_MODEL")
    if not embedding_model:
        raise ValueError("请设置Embedding_model.")

    return init_embeddings(embedding_model)


def build_retriever():
    """加载文档，分割、索引"""
    docs = load_markdown_documents(KB_DIR)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=80,
    )

    splits = text_splitter.split_documents(docs)

    embeddings = build_embeddings()
    vector_store = InMemoryVectorStore(embedding=embeddings)
    vector_store.add_documents(splits)
    return  vector_store.as_retriever(search_kwargs={"k": 3})


def answer_without_rag(model: BaseChatModel, question: str):
    """无RAG检索"""
    return model.invoke(question)


def answer_with_rag(model: BaseChatModel, retriever: VectorStoreRetriever, question: str):
    """使用RAG检索"""
    retriever_docs = retriever.invoke(question)
    context_block = format_retrieved_docs(retriever_docs)
    final_prompt = build_rag_user_prompt(question, context_block)

    response = model.invoke([
        {"role": "system", "content": RAG_SYSTEM_PROMPT},
        {"role": "user", "content": final_prompt},
    ])
    return response, retriever_docs


def print_retrieved_docs(docs):
    """打印检索文档名称"""
    print("[retrieved docs]")
    for idx, doc in enumerate(docs, 1):
        source = doc.metadata.get("source", "unknown")
        print(f"{idx}. source={source}")
        print(doc.page_content[:180])
        print()


def main():

    model = build_model()
    retriever = build_retriever()

    questions = [
        "LangChain middleware 的核心价值是什么？",
        "Deep Agents 的异步 subagents 适合什么场景？",
        "天气晴朗，我是溜猫还是溜狗？",
    ]

    for question in questions:
        print("=" * 60)
        print(f"Question: {question}")

        print("\n[without rag]")
        direct = answer_without_rag(model, question)
        print(direct.content)

        print("\n[with rag]")
        rag_response, retrieved_docs = answer_with_rag(model, retriever, question)
        print_retrieved_docs(retrieved_docs)
        print(rag_response.content)


if __name__ == "__main__":
    main()
