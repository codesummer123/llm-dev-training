# Day6 Code Scaffold

目标：实现一个基于本地知识库的最小 2-step RAG 问答器。

你需要补完的文件：

- `main.py`
- `rag_utils.py`
- `prompts.py`

建议步骤：

1. 先加载 `kb/` 里的本地文档
2. 再完成 split / embeddings / vector store
3. 再单独测试 retriever
4. 最后完成无 RAG / 有 RAG 对照
5. 运行 `python main.py`
6. 运行 `python -m pytest tests/`

今天的关键不是“做一个会回答的机器人”，而是看清：

- retrieval 到底拿回了什么
- 为什么拿对上下文比“让模型多想一会儿”更重要
