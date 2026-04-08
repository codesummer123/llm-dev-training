# Day8-训练内容

主题：LangGraph 的真正分水岭，不是“会画图”，而是“每一步都能被保存、查看、恢复”

## 1. 学习目标

今天的目标，是把 Day7 的最小图工作流升级成“可持久化、可回看状态历史”的 LangGraph 系统。

完成今天后，你应该能回答：

- 为什么 persistence 才是 LangGraph 和普通流程代码真正拉开差距的地方
- 为什么 `thread_id`、`checkpoint`、`state history` 是一套系统，而不是几个零散 API
- 为什么 checkpoint 不是“为了存档”，而是为了后续恢复、调试、memory、interrupt、time travel 打基础

今天结束后，你应该具备的能力是：

- 能给 graph 接入 `checkpointer`
- 能用 `thread_id` 保持一次执行轨迹
- 能查看最新 state snapshot
- 能查看完整 state history
- 能解释 checkpoint 是如何随执行步骤产生的

## 2. What

### 2.1 今天要学的知识点

- persistence 的价值
- `thread_id`
- `checkpointer`
- checkpoint
- `StateSnapshot`
- `graph.get_state`
- `graph.get_state_history`
- super-step 的基本理解

### 2.2 核心概念

#### Thread 是执行轨迹的主键

在 LangGraph 中，持久化不是“随便存一份状态”，而是：

- 每次执行都挂在某个 thread 下
- 这个 thread 对应一条持续演化的状态轨迹

所以：

- graph 是流程定义
- thread 是某条具体执行轨迹

#### Checkpoint 是每个关键步骤后的状态快照

checkpoint 不是只在流程结束后才有。  
LangGraph 的核心设计是：

- 在执行过程中按 super-step 产生 checkpoint

这意味着你可以：

- 看当前状态
- 看历史状态
- 以后还能做恢复、回放、分叉

#### Persistence 是高级能力的地基

很多 LangGraph 的高级能力，本质上都站在 persistence 上：

- memory
- human-in-the-loop
- time travel
- durable execution

今天要建立的关键认知是：

`如果没有 checkpoint，很多高级能力都只是概念，不是系统能力。`

## 3. Why

### 3.1 为什么 Day8 要紧接着 Day7 学 persistence

因为你昨天已经理解了：

- graph 是怎么跑的
- state 怎么流动
- route 怎么分支

那今天最自然的下一步就是：

- 这条状态流动轨迹如何被保存下来

如果跳过 persistence，LangGraph 很容易被误学成：

- “就是个更结构化的流程图”

而实际上，LangGraph 真正的力量在于：

- 带状态
- 可持久化
- 可恢复
- 可追踪

### 3.2 为什么今天不直接上 time travel / interrupt

因为这些高级能力虽然很酷，但它们背后的前提都是：

- 你先理解 thread
- 先理解 checkpoint
- 先理解 state history

先把这些最底层概念吃透，后面再学 interrupt、time travel，就会非常顺。

## 4. How

### 4.1 今天的训练任务

你要把 Day7 的学习路径分流图升级成一个“可持久化学习路径图”，至少支持：

1. 同一个 `thread_id` 下执行一次图并产出 checkpoint
2. 获取最新 state snapshot
3. 获取完整 state history
4. 打印每个 checkpoint 的关键字段

### 4.2 代码任务拆解

#### 任务 1：接入 checkpointer

要求：

- 使用一个最小可运行的 checkpointer
- compile graph 时挂上 checkpointer
- 调用 graph 时传入 `thread_id`

#### 任务 2：查看最新 state

在图执行完成后，调用：

- `graph.get_state(config)`

并观察：

- `values`
- `next`
- `metadata`
- `config`

目的：

- 建立对 `StateSnapshot` 的第一印象

#### 任务 3：查看 state history

调用：

- `graph.get_state_history(config)`

要求：

- 至少打印每个 checkpoint 的 `step`
- 至少打印 `writes`
- 至少打印当前 `values`

目的：

- 看到状态不是只有终态，而是一步步演化出来的

#### 任务 4：对比不同 thread

至少跑两个不同 thread：

- `thread-a`
- `thread-b`

观察：

- 两条轨迹是否隔离
- 历史是否独立

### 4.3 推荐运行流程

1. 先在 Day7 图的基础上挂上 checkpointer
2. 再跑一次 graph.invoke
3. 再看最新 state
4. 再看 state history
5. 最后做 thread 隔离对照

## 5. 代码设计说明

今天的脚手架已经放到 `code/Day8/`。

建议职责划分：

- `main.py`
  - 构建图
  - 运行两个 thread
  - 打印 snapshot 和 history
- `workflow.py`
  - 放 state schema、nodes、route function、graph builder
- `inspect_utils.py`
  - 放 snapshot / history 的格式化打印辅助函数
- `tests/test_inspect_utils.py`
  - 测试辅助函数逻辑

## 6. 验收标准

满足以下条件，Day8 就算基本过关：

- 你能解释 `thread_id` 和 `checkpoint` 的关系
- 你能给 graph 接入 checkpointer
- 你能获取并解释 `graph.get_state()` 的结果
- 你能获取并解释 `graph.get_state_history()` 的结果
- 你能证明不同 thread 的历史是隔离的

## 7. 常见坑

- 忘了传 `thread_id`
- 以为 persistence 只保存最终结果
- 只看终态，不看历史
- 混淆 graph 定义和 thread 执行轨迹
- 没有意识到 checkpoint 是后续高级能力的地基

## 8. 类比理解

可以把 Day8 的 persistence 类比成“版本化项目记录”：

- graph 像项目流程模板
- thread 像某个具体项目实例
- checkpoint 像每个阶段的版本快照
- state history 像完整版本历史

重点不是“存了一份文件”，而是：

`你能回看项目是怎么一步步演化到现在的。`

## 9. 今日交付物

今天你需要完成四件事：

1. 补完 `code/Day8/` 下的核心实现
2. 跑通带 checkpointer 的 graph
3. 展示 snapshot 与 history
4. 回答 `answer/Day8-问题.md` 里的问题

## 10. 官网来源

今天主要对应这些官方页面：

- https://docs.langchain.com/oss/python/langgraph/persistence
- https://docs.langchain.com/oss/python/langgraph/durable-execution
- https://docs.langchain.com/oss/python/langgraph/graph-api
