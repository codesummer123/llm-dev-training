# Day6-训练内容

主题：Retrieval / RAG 的本质不是“让模型会搜索”，而是“在回答前先拿对上下文”

## 1. 学习目标

今天的目标，是把训练从“控制 Agent 行为”推进到“给 Agent 外部知识来源”。

完成今天后，你应该能回答：

- 为什么 retrieval 解决的是“上下文获取”问题，而不是“模型智力增强”问题
- 为什么 2-step RAG 常常比 agentic RAG 更简单、更稳定
- 为什么一个好的知识库不等于“塞很多文档”，而是“能被有效检索”

今天结束后，你应该具备的能力是：

- 能从本地文档构建一个最小知识库
- 能完成 `文档加载 -> 切分 -> 向量化 -> 存储 -> 检索 -> 生成` 的最小闭环
- 能比较“无 retrieval”与“有 retrieval”的回答差异

## 2. What

### 2.1 今天要学的知识点

- retrieval 的基本目标
- 2-step RAG 与 agentic RAG 的区别
- knowledge base 的意义
- `Document`
- text splitter
- embeddings
- vector store
- retriever
- 检索结果如何拼接成模型上下文

### 2.2 核心概念

#### Retrieval 是在运行时获取相关上下文

LLM 的两个天然限制是：

- 上下文窗口有限
- 知识不是实时更新的

retrieval 的核心不是“让模型变聪明”，而是：

`在问题发生时，把最相关的外部信息拿进来。`

#### 2-step RAG 是最小、稳定、可控的 RAG 形态

2-step RAG 的流程非常明确：

1. 先检索
2. 再把检索结果给模型生成答案

它的优点是：

- 调试简单
- 调用次数可控
- 成本与延迟更可预测

这非常适合今天的训练。

#### 知识库不是“文件堆”，而是“可检索语料”

今天你要建立一个很重要的认知：

- 文档本身不等于知识库
- 只有在被切分、向量化、存储、可检索之后，它才变成对 RAG 有价值的知识来源

## 3. Why

### 3.1 为什么 Day6 要开始做 retrieval

因为到 Day5 为止，你做的 Agent 还主要依赖：

- 内部 prompt
- 内部工具
- 内部 state

而真实系统经常需要：

- 回答私有知识
- 回答本地文档
- 回答项目文档
- 回答训练资料

这时真正关键的不是“再写更强的 prompt”，而是：

`让系统能把正确的外部上下文带进来。`

### 3.2 为什么先学 2-step RAG，而不是一上来 agentic RAG

因为训练要讲顺序。

如果你还没把以下链路吃透：

- 文档怎么切
- embedding 怎么起作用
- 检索结果怎么进上下文
- 为什么会检错

那直接上 agentic RAG，只会把复杂性叠在一起。

所以今天先训练：

- 2-step RAG
- 最小知识库
- 可对比实验

## 4. How

### 4.1 今天的训练任务

你要实现一个“训练资料问答器”，基于本地知识库回答问题。

要求至少支持两种模式：

1. 不做 retrieval，直接问模型
2. 先 retrieval，再回答

你的任务不是只让它“能答”，而是要能观察：

- retrieval 到底拿回来了什么
- 这些内容是否真的帮助了回答

### 4.2 代码任务拆解

#### 任务 1：构建本地知识库

今天不用上数据库，也不用外部 SaaS。

直接用 `code/Day6/kb/` 里的本地 Markdown 文档做知识源。

你要完成：

- 读取本地文档
- 转成 `Document`
- 保留来源 metadata

#### 任务 2：完成 indexing 流程

至少包括：

- text splitter
- embeddings
- vector store

建议优先用：

- `RecursiveCharacterTextSplitter`
- `InMemoryVectorStore`

这样复杂度最低，最适合训练主线。

#### 任务 3：完成 2-step RAG

你需要显式写出两个阶段：

1. `retriever.invoke(question)`
2. 把 retrieved docs 拼进 prompt / messages，再调用模型

要求：

- 检索结果要能打印出来
- 最终回答要尽量引用检索内容，而不是自由发挥
- 如果检索内容不足，要鼓励模型诚实回答

#### 任务 4：做无 RAG / 有 RAG 对比

至少准备两类问题：

- 能从本地知识库回答的问题
- 本地知识库里没有明确信息的问题

观察：

- 无 retrieval 时模型怎么答
- 有 retrieval 时模型怎么答
- 当资料不足时，系统是否会更诚实

### 4.3 推荐运行流程

1. 先让本地文档加载成功
2. 再让 split / embeddings / vector store 跑通
3. 再单独测试 retriever
4. 最后接生成环节
5. 最后做有无 RAG 的对照实验

## 5. 代码设计说明

今天的脚手架已经放到 `code/Day6/`。

建议职责划分：

- `main.py`
  - 初始化模型和 embeddings
  - 构建索引
  - 运行无 RAG / 有 RAG 对照
- `rag_utils.py`
  - 放知识库加载、文档格式化、上下文拼接等辅助函数
- `prompts.py`
  - 放 grounded answering 的 system prompt
- `kb/`
  - 放本地训练资料
- `tests/test_rag_utils.py`
  - 测试辅助函数

## 6. 验收标准

满足以下条件，Day6 就算基本过关：

- 你能解释 2-step RAG 和 agentic RAG 的区别
- 你能跑通最小 indexing 流程
- 你能展示 retriever 实际拿回了哪些文档
- 你能展示无 RAG / 有 RAG 的回答差异
- 你能解释 retrieval 为什么本质上是在做上下文获取

## 7. 常见坑

- 把 retrieval 理解成“模型自动联网”
- 不打印检索结果，只看最终答案
- 文档不加 metadata，后面看不到来源
- split 太粗或太细，影响检索质量
- 没有做无 RAG 对照，导致看不出 retrieval 的真实价值

## 8. 类比理解

可以把 retrieval 类比成“开卷考试前先翻资料”：

- 模型像答题者
- 知识库像资料柜
- retriever 像找资料的人
- RAG 像把找到的资料摊到桌面上再作答

重点不是答题者突然变聪明，而是：

`答题前拿到了更相关的资料。`

## 9. 今日交付物

今天你需要完成四件事：

1. 补完 `code/Day6/` 下的核心实现
2. 跑通最小 2-step RAG
3. 做有无 retrieval 的对照实验
4. 回答 `answer/Day6-问题.md` 里的问题

## 10. 官网来源

今天主要对应这些官方页面：

- https://docs.langchain.com/oss/python/langchain/retrieval
- https://docs.langchain.com/oss/python/langchain/knowledge-base
- https://docs.langchain.com/oss/python/langchain/rag
