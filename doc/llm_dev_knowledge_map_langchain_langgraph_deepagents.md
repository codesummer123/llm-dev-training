# 大模型开发训练知识地图

基于官网最新公开文档整理，覆盖 `LangChain`、`LangGraph`、`Deep Agents` 三个 Python 框架。

- 整理日期：2026-03-30
- 语言栈：Python
- 目标：为后续生成“每日学习计划”提供可拆分、可排期、可验收的细颗粒度知识点清单
- 说明：你提到的 `DeepAgent`，这里按 LangChain 官网中的 `Deep Agents` 处理

## 1. 三个框架的定位

### 1.1 LangChain

LangChain 是偏上层的 Agent 开发框架，重点在于：

- 快速搭建可用 Agent
- 标准化模型、消息、工具、结构化输出等接口
- 用 middleware 做上下文工程
- 在不直接操作底层图编排的情况下获得 LangGraph 的持久化、流式输出、人类介入等能力

适合你训练的重点：

- Agent 基础能力
- 工具调用
- 上下文工程
- 检索 / RAG
- Memory
- Middleware

### 1.2 LangGraph

LangGraph 是偏底层的编排框架和运行时，重点在于：

- 长运行、可恢复、带状态的 Agent / Workflow
- 图式编排
- 持久化 checkpoint
- 中断、恢复、时间回溯
- 子图、多代理、可观测性、生产部署

适合你训练的重点：

- State / Node / Edge / Reducer
- Graph API / Functional API
- 持久化与 durable execution
- interrupt / resume / replay / fork
- 复杂流程编排

### 1.3 Deep Agents

Deep Agents 是构建复杂 Agent 的“agent harness / SDK”，建立在 LangChain + LangGraph 之上，重点在于：

- 内置规划能力
- 文件系统式上下文管理
- 内置 subagent 委派
- 可插拔后端
- 长期记忆
- 沙箱执行
- CLI 形态的 coding / task agent

适合你训练的重点：

- 复杂任务分解
- 上下文隔离
- 文件系统与 backend
- 同步 / 异步 subagent
- sandbox 与 CLI 能力

## 2. 推荐学习顺序

建议按下面顺序学：

1. LangChain 基础能力
2. LangChain 的 context engineering / middleware / retrieval / memory
3. LangGraph 的图编排与运行时
4. LangGraph 的 persistence / durable execution / interrupts / time travel
5. Deep Agents 的 agent harness、backend、subagent、sandbox、CLI

原因：

- LangChain 负责“怎么快速把 agent 跑起来”
- LangGraph 负责“怎么把 agent 做成稳定、可恢复、可编排的系统”
- Deep Agents 负责“怎么把复杂任务 agent 做成产品级工作流和终端代理”

## 3. LangChain 细颗粒度知识点

## 3.1 入门与框架认知

- LangChain 的定位、边界与适用场景
- LangChain、LangGraph、Deep Agents 三者关系
- `create_agent` 的作用与适用边界
- 何时只用 LangChain，何时下沉到 LangGraph
- Python 安装方式与 provider 扩展包安装方式
- LangSmith tracing 的基本启用方法

## 3.2 Agents

- Agent 的本质：模型 + 工具 + 循环执行
- stop condition 的概念
- Agent loop 的核心阶段
- model node 与 tools node 的职责划分
- `create_agent` 的核心参数
- 只传模型不传工具时的行为
- Agent graph 与 LangGraph 的关系
- agent invoke 的输入消息格式
- agent 输出结构的理解

### 3.2.1 模型配置

- 静态模型配置
- 通过模型字符串初始化模型
- provider 自动推断
- 直接实例化 provider 模型类
- provider 参数配置
- timeout / temperature / max_tokens 等参数控制
- base URL、自定义 endpoint、代理配置

### 3.2.2 动态模型选择

- 运行时动态切换模型的价值
- 基于 state 选择模型
- 基于对话复杂度选择模型
- 使用 middleware 包装 model call
- `wrap_model_call` 的使用方式
- 动态模型与结构化输出共用时的限制
- 默认模型与覆盖模型的关系

### 3.2.3 工具使用模式

- 静态工具集
- 动态工具集
- 根据权限过滤工具
- 根据状态过滤工具
- 根据对话阶段过滤工具
- 运行时注册工具
- 工具错误处理与重试
- tool calling loop 中的工具使用顺序
- 并行工具调用的概念

### 3.2.4 提示词控制

- system prompt 的作用
- 动态 system prompt
- 在 middleware 中修改 prompt
- 为不同用户 / 任务定制 prompt
- prompt 与 state 的关系

### 3.2.5 代理状态与调用

- agent `name` 的作用
- `invoke` / `ainvoke`
- 单轮与多轮消息调用
- 与 streaming 的配合
- 与 memory 的配合

## 3.3 Models

- LangChain 标准模型接口的价值
- chat model 的初始化方式
- 支持的模型族与 provider 抽象
- 常用 key methods：`invoke`、`stream`、`batch`
- 批量调用场景
- 工具绑定 `bind_tools`
- 结构化输出绑定
- model profiles
- 可配置模型 configurable models
- 调用时 config 的传递
- token usage 获取
- log probabilities
- reasoning 模型能力
- multimodal 模型调用
- 本地模型接入
- prompt caching
- server-side tool use
- rate limiting

## 3.4 Messages

- 文本 prompt 与 message prompt 的区别
- dict 消息格式与 Message 对象格式
- 各类消息类型的职责
- `SystemMessage`
- `HumanMessage`
- `AIMessage`
- `ToolMessage`
- AIMessage 中 tool_calls 的结构
- message metadata
- token usage 在 message 上的体现
- streaming chunk 的消息拼接
- 标准 content blocks
- 多模态 content blocks
- 文本、图片等内容块的表示方式
- 消息与 chat model 的交互方式

## 3.5 Tools

- 用普通函数定义工具
- 用 `@tool` 装饰器定义工具
- 自定义工具名称
- 自定义工具描述
- 参数 schema 设计
- 高级 schema 定义
- 预留参数名限制
- 在工具内部访问 context
- 在工具中访问 short-term state
- 在工具中更新 state
- 在工具中访问 long-term store
- `StreamWriter` 的作用
- `ToolNode` 的作用
- 工具返回字符串
- 工具返回对象
- 工具返回 `Command`
- 工具错误处理
- `tools_condition` 路由

## 3.6 Short-term Memory

- 短期记忆的作用范围
- thread 级别 memory 概念
- 开发环境 vs 生产环境中的 memory 差异
- 自定义 agent memory
- 常见 memory 管理模式
- trim messages
- delete messages
- summarize messages
- 在工具中读短期记忆
- 在工具中写短期记忆
- 在 prompt 中使用短期记忆
- before model 阶段修改 memory
- after model 阶段修改 memory

## 3.7 Streaming

- 为什么 agent 需要流式输出
- 支持的 stream modes
- agent progress stream
- LLM tokens stream
- custom updates stream
- 多模式同时 streaming
- reasoning token streaming
- tool call streaming
- 获取最终完整消息
- HITL 场景下的 streaming
- sub-agent streaming
- 针对特定模型禁用 streaming
- v2 streaming format

## 3.8 Structured Output

- 为什么需要结构化输出
- response_format 的配置
- ProviderStrategy
- ToolStrategy
- provider 原生结构化输出与工具调用结构化输出的差异
- 自定义工具消息内容
- schema 校验失败的处理
- multiple structured outputs error
- error handling strategies

## 3.9 Middleware

### 3.9.1 中间件总览

- middleware 在 agent loop 中的位置
- node-style hooks
- wrap-style hooks
- 生命周期钩子
- 状态更新能力
- middleware 组合顺序
- agent jumps

### 3.9.2 预置中间件

- Summarization middleware
- Human-in-the-loop middleware
- Model call limit
- Tool call limit
- Model fallback
- PII detection
- 自定义 PII types
- To-do list middleware
- LLM tool selector
- Tool retry
- Model retry
- LLM tool emulator
- Context editing
- Shell tool middleware
- File search middleware
- Filesystem middleware
- 短期文件系统 vs 长期文件系统
- Subagent middleware
- provider-specific middleware

### 3.9.3 自定义中间件

- 装饰器式 middleware
- 类式 middleware
- 自定义 state schema
- 动态模型选择
- 工具调用监控
- 动态选择工具
- 动态修改系统消息
- 多个 middleware 的执行顺序
- 编写 middleware 的最佳实践

## 3.10 Guardrails

- 内置 guardrails
- PII detection guardrail
- human-in-the-loop guardrail
- before agent guardrail
- after agent guardrail
- 多 guardrail 组合
- guardrail 与 middleware 的边界

## 3.11 Runtime

- runtime 的概念
- runtime 与 agent execution 的关系
- 在工具中访问 runtime
- 在 middleware 中访问 runtime
- runtime 适合承载哪些信息
- runtime 与 state/store 的区别

## 3.12 Context Engineering

- 为什么 agent 失败更多是 context 问题
- agent loop 中可控的三个上下文层
- Model Context
- Tool Context
- Life-cycle Context
- transient context 与 persistent context
- 数据源划分：runtime context / state / store
- 如何控制 messages、tools、system prompt、response format
- 如何控制工具的读写能力
- 如何在生命周期钩子中做 summarization / guardrails / logging
- 如何面向可靠性设计 context
- context engineering 的最佳实践

## 3.13 MCP

- MCP 的定位与作用
- `langchain-mcp-adapters` 的作用
- `MultiServerMCPClient`
- 多 MCP server 接入
- HTTP transport
- stdio transport
- stateful sessions
- MCP tools 的加载
- structured content
- multimodal tool content
- resources 加载
- prompts 加载
- tool interceptors
- 访问 runtime context
- state updates / commands
- progress notifications
- logging
- elicitation
- MCP server/client 的基本搭建

## 3.14 Human-in-the-loop

- interrupt decision types
- interrupt 配置方式
- 对 interrupt 的响应方式
- decision types 设计
- HITL 与 streaming 联动
- execution lifecycle
- 自定义 HITL 逻辑

## 3.15 Retrieval

- knowledge base 构建流程
- retrieval 到 RAG 的关系
- retrieval pipeline
- retrieval building blocks
- 2-step RAG
- agentic RAG
- hybrid RAG
- 检索在 LangChain Agent 中的接入方式

## 3.16 Long-term Memory

- long-term memory 与 short-term memory 的边界
- 基于 LangGraph store 的长期记忆
- namespace / key 的组织方式
- 长期记忆的读写
- 在工具中读取长期记忆
- 在工具中写入长期记忆
- 面向用户偏好、历史信息、知识积累的设计方式

## 3.17 Agent 开发与生产化

- LangSmith Studio 的作用
- Agent Chat UI 的作用
- Deployment 的基本认知
- Observability 的基本认知
- trace、debug、evaluation 的基本工作流

## 4. LangGraph 细颗粒度知识点

## 4.1 入门与框架认知

- LangGraph 的定位与边界
- 什么是低层编排框架
- LangGraph 与 LangChain 的关系
- 长运行、带状态 agent 的典型场景
- 为什么 LangGraph 适合复杂任务

## 4.2 两套 API

### 4.2.1 Graph API

- Graph API 的适用场景
- State / Nodes / Edges 三元组
- `StateGraph` 的基本使用
- `START` / `END`
- `add_node`
- `add_edge`
- `add_conditional_edges`
- 序列、分支、循环结构
- graph compile
- graph visualize

### 4.2.2 Functional API

- Functional API 的适用场景
- `@entrypoint`
- `@task`
- 用普通 Python 控制流编排
- Functional API 与 Graph API 的差异
- task result checkpointing
- Functional API 的限制与优势

### 4.2.3 选型

- Graph API 适合图结构显式建模
- Functional API 适合已有代码轻量接入
- 两套 API 可混用的理解
- 如何根据项目复杂度选型

## 4.3 Thinking in LangGraph

- 从业务流程出发设计 agent
- 把 workflow 拆成离散步骤
- 为每个步骤识别职责
- LLM step
- data step
- action step
- user input step
- 先设计 state 再写代码
- state 中应该放什么
- 保持 state 原始、按需格式化 prompt
- 节点错误处理策略
- 先 wire，再优化的开发思路

## 4.4 State 设计

- 用 `TypedDict` 定义 state schema
- 用 dataclass 提供默认值
- 用 Pydantic 做递归校验
- reducer 的作用
- append 型 reducer
- 覆盖型更新
- 公共 state 与私有 state
- 输入 schema 与输出 schema
- runtime context schema
- 状态迁移兼容性
- 新增 / 删除 state key 的兼容影响
- 重命名 state key 的风险

## 4.5 Node 与 Edge

- node 的输入输出约定
- node 中的副作用管理
- edge 的固定跳转
- conditional edge
- 动态路由函数
- node 命名
- 异步 node
- 并行 node 的理解
- graph 中的 loop 设计

## 4.6 Workflows + Agents 模式

- workflow 与 agent 的区别
- prompt chaining
- parallelization
- routing
- orchestrator-worker
- evaluator-optimizer
- agent 模式
- 何时选择 workflow
- 何时选择 agent
- 如何组合确定性流程与 agentic 流程

## 4.7 Persistence

- 为什么 persistence 是 LangGraph 的核心能力
- thread 概念
- checkpoint 概念
- super-step 概念
- checkpoint namespace
- get state
- `StateSnapshot` 的字段理解
- get state history
- 查找指定 checkpoint
- replay
- update state
- memory store
- semantic search
- 在 LangGraph 中使用 store
- checkpointer libraries
- checkpointer interface
- serializer
- pickle 序列化
- encryption

## 4.8 Durable Execution

- durable execution 的定义
- 为什么需要 durable execution
- deterministic replay
- 一致性恢复
- durability modes
- 在 node 中使用 task
- resuming workflows
- 从不同起点恢复工作流
- 长时间暂停后的恢复
- 失败后继续执行而非重跑全部步骤
- 幂等性设计

## 4.9 Streaming

- graph 级流式输出
- v2 输出格式
- stream modes
- graph state streaming
- LLM tokens streaming
- 按 LLM invocation 过滤
- 按 node 过滤
- custom data streaming
- subgraph outputs
- checkpoint streaming
- tasks streaming
- debug streaming
- 多模式同时 streaming
- 与任意 LLM 配合的 streaming 思路
- 对特定 chat model 关闭 streaming
- Python < 3.11 的异步注意事项

## 4.10 Interrupts

- `interrupt` 的概念
- 在图执行中暂停
- interrupt 后如何 resume
- 多个 interrupt 的处理
- approve / reject 模式
- review / edit state 模式
- 在工具中 interrupt
- 验证人工输入
- interrupt 使用规则
- 不要把 interrupt 包在 try/except 中
- 不要在 node 内改变 interrupt 调用顺序
- interrupt 返回值不要设计得过于复杂
- interrupt 前副作用要幂等
- subgraph 中使用 interrupt
- 用 LangSmith Studio 调试 interrupt

## 4.11 Time Travel

- time travel 的价值
- replay
- fork
- 从指定 node 恢复
- 与 interrupt 结合
- 多 interrupt 时间回溯
- subgraph 时间回溯
- 历史 checkpoint 上分叉实验

## 4.12 Memory

- LangGraph memory 的两种类型
- short-term memory 接入
- long-term memory 接入
- 在子图中使用 memory
- semantic search memory
- trim messages
- delete messages
- summarize messages
- checkpoint 管理
- 查看 thread state
- 查看 thread history
- 删除 thread checkpoints
- 数据库管理

## 4.13 Subgraphs

- 什么是 subgraph
- subgraph 作为 node
- 子图与父图的通信设计
- 在 node 内调用 subgraph
- 直接把 subgraph 加为节点
- subgraph persistence
- stateful subgraph
- per-invocation 默认模式
- per-thread 模式
- stateless subgraph
- checkpointer 传递与引用
- 查看 subgraph state
- streaming subgraph outputs
- 多团队协作开发中的 subgraph 价值

## 4.14 Runtime

- Pregel runtime 的定位
- actor + channel 模型
- BSP / super-step 思想
- step 内三个阶段的理解
- graph compile 后得到 Pregel 实例
- `@entrypoint` 背后的 runtime
- 直接基于 Pregel 实现应用的认知

## 4.15 生产化

- application structure
- `langgraph.json`
- 依赖文件与 `.env`
- 本地 server 认知
- 测试思路
- LangSmith Studio
- Agent Chat UI
- Deployment
- Observability
- 生产部署时的结构化项目组织

## 5. Deep Agents 细颗粒度知识点

## 5.1 入门与框架认知

- Deep Agents 的定位
- 它是 LangChain 之上的 agent harness
- 它依赖 LangGraph runtime
- 何时用 Deep Agents 而不是直接用 LangChain
- 何时用 Deep Agents CLI
- Deep Agents 适合的任务类型
- 复杂多步任务的典型场景

## 5.2 Quickstart 基础

- 安装 `deepagents`
- 工具调用模型的前提要求
- API key 配置
- 自定义搜索工具
- `create_deep_agent`
- `tools` 参数
- `system_prompt` 参数
- `model` 参数
- `invoke` 调用格式
- quickstart 中研究型 agent 的基本结构

## 5.3 核心能力总览

- 内置 `write_todos`
- 文件系统工具 `ls`
- 文件系统工具 `read_file`
- 文件系统工具 `write_file`
- 文件系统工具 `edit_file`
- subagent `task` 工具
- 长期记忆
- 流式输出
- 人类介入
- pluggable backend

## 5.4 Customization

- connection resilience
- 模型自定义
- 工具自定义
- system prompt 自定义
- middleware 自定义
- 预置 middleware
- 自定义 middleware
- subagents 自定义
- backend 自定义
- sandbox 自定义
- HITL 自定义
- skills 自定义
- memory 自定义
- structured output 自定义

## 5.5 Models

- Deep Agents 依赖 LangChain chat model
- 模型必须支持 tool calling
- 通过 model string 指定模型
- 配置模型参数
- 运行时选择模型
- supported models
- suggested models
- 模型选择与任务类型匹配

## 5.6 Context Engineering

- Deep Agents 中的 context 类型
- input context
- system prompt
- memory
- skills
- tool prompts
- complete system prompt
- runtime context
- context compression
- offloading
- summarization
- 用 subagents 做 context isolation
- long-term memory 在 context 中的作用
- Deep Agents 上下文设计最佳实践

## 5.7 Backends

- backend 的职责
- `StateBackend`
- `FilesystemBackend`
- `LocalShellBackend`
- `StoreBackend`
- `CompositeBackend`
- 指定 backend
- backend 路由
- 虚拟文件系统
- policy hooks
- backend protocol
- 不同 backend 的适用场景

## 5.8 同步 Subagents

- 为什么要用 subagent
- context quarantine
- 何时用 subagent
- 何时不该用 subagent
- `subagents` 参数
- 字典式 `SubAgent`
- `CompiledSubAgent`
- `name`
- `description`
- `system_prompt`
- `tools`
- `model`
- 使用同步 subagent
- 同步 subagent streaming
- 同步 subagent 结构化输出
- general-purpose subagent
- 覆盖默认通用 subagent
- skills 继承
- 设计清晰 description
- system prompt 详细化
- 最小化工具集合
- 按任务选模型
- 返回简洁结果
- 多专业 subagent 协作
- per-subagent context
- 识别哪个 subagent 调用了工具
- subagent 不被调用时的排查
- context 仍膨胀时的排查
- 错误 subagent 被选中的排查

## 5.9 异步 Subagents

- async subagent 的适用场景
- 同步 vs 异步 subagent 差异
- 后台并发执行
- 立即返回 job ID
- mid-flight steering
- 取消任务
- 状态持久化
- 作为预览特性的认知
- 需要部署在 LangSmith Deployments
- `AsyncSubAgent` 配置
- `graph_id`
- transport 选择
- ASGI transport
- HTTP transport
- deployment topology
- single deployment
- split deployment
- hybrid deployment
- worker pool 配置
- thread ID 跟踪
- stale status 等排障点

## 5.10 Human-in-the-loop

- 基础配置
- decision types
- interrupt handling
- 多工具调用时的 decision 对齐
- 编辑工具参数
- subagent interrupts
- 在工具调用前中断
- 在工具内部中断
- 必须使用 checkpointer
- 使用相同 thread ID
- 按风险定制 HITL 配置

## 5.11 Long-term Memory

- 短期文件系统与长期文件系统的区别
- `CompositeBackend` 路由持久化路径
- `/memories/` 约定
- 跨 thread 持久化
- 用 LangGraph Store 存长期记忆
- 从外部代码访问 memory
- 用户偏好
- 自我改进指令
- 知识库
- 研究项目记忆
- `InMemoryStore`
- `PostgresStore`
- `FileData` schema
- 记忆路径命名规范
- 记忆结构文档化
- 旧数据裁剪

## 5.12 Skills

- 什么是 skills
- skills 的工作方式
- skills 的目录 / 文件组织
- 完整示例的理解
- source precedence
- subagent 使用 skills
- agent 实际看到的 skill 内容
- skills 与 memory 的区别
- 何时用 skills
- 何时用 tools
- 何时用 skills + tools 组合

## 5.13 Sandboxes

- 为什么复杂 agent 需要 sandbox
- sandbox 与普通 backend 的差异
- `execute` 工具
- 文件工具与执行工具的组合
- 安全边界
- coding agent 场景
- data analysis agent 场景
- agent in sandbox pattern
- sandbox as tool pattern
- 可用 provider
- sandbox 基本使用
- execute 方法
- 两层文件访问平面
- seed sandbox
- retrieve artifacts
- 生命周期管理
- per-conversation 生命周期
- cleanup
- secrets 安全处理
- sandbox 最佳实践

## 5.14 Streaming

- 启用 subgraph streaming
- namespace
- subagent progress
- LLM tokens
- tool calls
- custom updates
- 多模式流式输出
- subagent lifecycle 跟踪
- v2 streaming format

## 5.15 Frontend

- frontend 架构认知
- Deep Agents 前端模式
- 与 graph execution 的关系
- 适合前端暴露哪些事件流

## 5.16 ACP

- Agent Client Protocol 的定位
- quickstart
- ACP client 形态
- 与 Zed / Toad 等客户端集成的认知
- protocol 型集成与 SDK 型集成的区别

## 5.17 CLI

### 5.17.1 CLI 基础

- interactive mode
- non-interactive mode
- 管道输入
- 切换模型
- teach project conventions
- 提供项目上下文 / 用户上下文
- 使用 skills
- 自定义 subagent
- 使用 MCP tools
- 使用 remote sandbox
- LangSmith tracing
- command reference

### 5.17.2 CLI 配置

- `~/.deepagents/` 配置目录
- `config.toml`
- `hooks.json`
- `.mcp.json`
- default model
- recent model
- provider configuration
- model constructor params
- per-model overrides
- `--model-params`
- profile overrides
- `--profile-override`
- custom base URL
- compatible APIs
- interactive switcher 中添加模型
- arbitrary providers
- 外部编辑器设置

### 5.17.3 CLI Hooks

- hooks 的作用
- setup
- hook configuration
- payload format
- events reference
- `session.start`
- `session.end`
- `user.prompt`
- `input.required`
- `permission.request`
- `tool.error`
- `task.complete`
- `context.compact`
- execution model
- 事件记录到文件
- 任务完成通知
- Python handler
- security considerations

### 5.17.4 CLI MCP Tools

- quickstart
- auto-discovery
- discovery locations
- flags
- Claude Code compatibility
- 配置格式
- stdio servers
- SSE / HTTP servers
- 多 server
- project-level trust
- trust store
- system prompt awareness
- troubleshooting

## 6. 训练时的“掌握标准”建议

后续做每日计划时，可以把每个知识点按下面 4 个层次来排：

- L1 认知：能解释概念、边界、适用场景
- L2 使用：能按官网示例独立跑通
- L3 改造：能在已有示例基础上改 prompt、tool、memory、state、graph
- L4 设计：能根据一个真实任务独立做框架选型与系统设计

建议你后续做每日计划时，不是只按“章节”排，而是按“章节 x 掌握标准”排。

例如：

- LangChain Tools - L1 到 L3
- LangGraph Persistence - L1 到 L4
- Deep Agents Subagents - L1 到 L4

这样训练会更贴近工程能力，而不是只停留在“看过文档”。

## 7. 后续拆解每日计划时建议使用的维度

每天可以固定拆成 5 个块：

1. 官网精读
2. 代码复现
3. 改造练习
4. 小结输出
5. 第二天的复习回顾

后面我们生成每日计划时，我建议按下面维度一起编码：

- 知识点名称
- 所属框架
- 难度
- 依赖前置
- 预计耗时
- 官网原始页面
- 训练目标
- 练习题
- 产出物
- 验收标准

## 8. 官网来源索引

以下是本版知识地图主要依据的官网页面：

### 8.1 LangChain

- https://docs.langchain.com/oss/python/langchain/overview
- https://docs.langchain.com/oss/python/langchain/agents
- https://docs.langchain.com/oss/python/langchain/models
- https://docs.langchain.com/oss/python/langchain/messages
- https://docs.langchain.com/oss/python/langchain/tools
- https://docs.langchain.com/oss/python/langchain/short-term-memory
- https://docs.langchain.com/oss/python/langchain/streaming
- https://docs.langchain.com/oss/python/langchain/structured-output
- https://docs.langchain.com/oss/python/langchain/middleware/overview
- https://docs.langchain.com/oss/python/langchain/middleware/built-in
- https://docs.langchain.com/oss/python/langchain/middleware/custom
- https://docs.langchain.com/oss/python/langchain/guardrails
- https://docs.langchain.com/oss/python/langchain/runtime
- https://docs.langchain.com/oss/python/langchain/context-engineering
- https://docs.langchain.com/oss/python/langchain/mcp
- https://docs.langchain.com/oss/python/langchain/human-in-the-loop
- https://docs.langchain.com/oss/python/langchain/retrieval
- https://docs.langchain.com/oss/python/langchain/long-term-memory

### 8.2 LangGraph

- https://docs.langchain.com/oss/python/langgraph/overview
- https://docs.langchain.com/oss/python/langgraph/quickstart
- https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph
- https://docs.langchain.com/oss/python/langgraph/workflows-agents
- https://docs.langchain.com/oss/python/langgraph/graph-api
- https://docs.langchain.com/oss/python/langgraph/use-graph-api
- https://docs.langchain.com/oss/python/langgraph/functional-api
- https://docs.langchain.com/oss/python/langgraph/use-functional-api
- https://docs.langchain.com/oss/python/langgraph/choosing-apis
- https://docs.langchain.com/oss/python/langgraph/persistence
- https://docs.langchain.com/oss/python/langgraph/durable-execution
- https://docs.langchain.com/oss/python/langgraph/streaming
- https://docs.langchain.com/oss/python/langgraph/interrupts
- https://docs.langchain.com/oss/python/langgraph/use-time-travel
- https://docs.langchain.com/oss/python/langgraph/add-memory
- https://docs.langchain.com/oss/python/langgraph/use-subgraphs
- https://docs.langchain.com/oss/python/langgraph/application-structure
- https://docs.langchain.com/oss/python/langgraph/pregel

### 8.3 Deep Agents

- https://docs.langchain.com/oss/python/deepagents/overview
- https://docs.langchain.com/oss/python/deepagents/quickstart
- https://docs.langchain.com/oss/python/deepagents/customization
- https://docs.langchain.com/oss/python/deepagents/comparison
- https://docs.langchain.com/oss/python/deepagents/models
- https://docs.langchain.com/oss/python/deepagents/context-engineering
- https://docs.langchain.com/oss/python/deepagents/backends
- https://docs.langchain.com/oss/python/deepagents/subagents
- https://docs.langchain.com/oss/python/deepagents/async-subagents
- https://docs.langchain.com/oss/python/deepagents/human-in-the-loop
- https://docs.langchain.com/oss/python/deepagents/long-term-memory
- https://docs.langchain.com/oss/python/deepagents/skills
- https://docs.langchain.com/oss/python/deepagents/sandboxes
- https://docs.langchain.com/oss/python/deepagents/streaming
- https://docs.langchain.com/oss/python/deepagents/frontend/overview
- https://docs.langchain.com/oss/python/deepagents/acp
- https://docs.langchain.com/oss/python/deepagents/cli/overview
- https://docs.langchain.com/oss/python/deepagents/cli/configuration
- https://docs.langchain.com/oss/python/deepagents/cli/mcp-tools

## 9. 下一步建议

下一步最适合做的是：把这份知识地图转成“按天执行的训练计划”，并且为每一天补齐：

- 学习目标
- 官网阅读顺序
- 最小代码练习
- 当日作业
- 验收标准
- 次日复习点

这样你就能从“知识清单”直接进入“训练节奏”。
