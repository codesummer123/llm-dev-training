# Day10-训练内容

主题：Time Travel 的本质不是“回到过去”，而是“从历史 checkpoint 重新执行或分叉实验”

## 1. 学习目标

今天的目标，是在 Day8 的 persistence 和 Day9 的 interrupt 之后，正式进入 `time travel / replay / fork`。

完成今天后，你应该能回答：

- 为什么 time travel 依赖 checkpoint history
- 为什么 replay 不是“读缓存”，而是“从某个 checkpoint 之后重新执行”
- 为什么 fork 不是“回滚线程”，而是“从过去某点创建新分支”

今天结束后，你应该具备的能力是：

- 能从 `get_state_history()` 找到指定 checkpoint
- 能用旧 checkpoint 的 config 做 replay
- 能用 `update_state()` 做 fork
- 能比较原始执行结果与 fork 后结果的差异

## 2. What

### 2.1 今天要学的知识点

- time travel 的整体概念
- replay
- fork
- prior checkpoint config
- `update_state()`
- `checkpoint_id`
- 为什么 checkpoint 之前的节点不会重跑
- 为什么 checkpoint 之后的节点会重跑

### 2.2 核心概念

#### Replay 是从某个历史 checkpoint 继续重新执行

Replay 不是简单读取历史结果。  
更准确地说：

- checkpoint 之前的节点不再执行
- checkpoint 之后的节点重新执行

所以 replay 的价值是：

- 从历史某点重新运行后续步骤
- 观察后续逻辑在新的运行中会发生什么

#### Fork 是在过去某点上创建一个新的分支

Fork 不是把原线程改掉。  
它的本质是：

- 保留原历史
- 在历史某个 checkpoint 上加一个新的 checkpoint
- 从这个分支继续往下跑

这意味着：

- 原轨迹仍然存在
- 新轨迹是一个实验分支

#### Time Travel 的价值是实验与调试

当你已经有：

- checkpoint history
- update_state
- replay / fork

你就能开始做这些很高级的事情：

- 比较不同决策下后续路径的差异
- 在不破坏原始执行的前提下做替代实验
- 从历史问题点继续分析，而不是每次从头跑

## 3. Why

### 3.1 为什么 Day10 要在 Day8 和 Day9 之后学

因为 time travel 不是孤立能力，它站在前面两天之上：

- Day8 让你理解 checkpoint 和 state history
- Day9 让你理解恢复与 thread 的连续性

Day10 的本质是把这些能力进一步升级：

- 不只是看历史
- 而是操作历史

### 3.2 为什么 replay / fork 是非常有工程价值的能力

因为复杂系统里常见的问题不是：

- “从头再跑一次”

而是：

- “我想从出问题的那一步继续看”
- “我想保留原结果，再试一个不同分支”

这正是 time travel 的意义。

## 4. How

### 4.1 今天的训练任务

你要实现一个“学习计划生成图”，然后在历史 checkpoint 上做：

1. replay
2. fork

要求至少展示：

- 原始执行结果
- replay 后结果
- fork 后结果

### 4.2 代码任务拆解

#### 任务 1：构建一个最小可分叉图

建议图结构：

- `generate_track`
- `draft_plan`
- `finalize`

思路：

- `generate_track` 先决定 track
- `draft_plan` 根据 track 生成计划
- `finalize` 输出最终总结

这样你就可以在 `draft_plan` 之前或之后挑 checkpoint 做 replay / fork。

#### 任务 2：查看历史 checkpoint

你需要从：

- `graph.get_state_history(config)`

中找到：

- 哪个 checkpoint 的 `next` 是 `("draft_plan",)`
- 或哪个 checkpoint 位于你想重放的位置前

#### 任务 3：做 replay

要求：

- 选一个历史 checkpoint
- 用它的 `config` 调 `graph.invoke(None, checkpoint_config)`
- 观察后续节点重新执行

#### 任务 4：做 fork

要求：

- 从某个 checkpoint 用 `graph.update_state(...)` 修改一部分状态
- 继续 `graph.invoke(None, fork_config)`
- 比较 fork 前后的结果差异

#### 任务 5：解释 replay 和 fork 的区别

你至少要能说明：

- replay 不改 state，只重跑后续
- fork 会引入新的 state 分支

### 4.3 推荐运行流程

1. 先跑原始执行
2. 再打印 state history
3. 再做 replay
4. 再做 fork
5. 最后比较三份结果

## 5. 代码设计说明

今天的脚手架已经放到 `code/Day10/`。

建议职责划分：

- `main.py`
  - 跑原始执行
  - 打印 history
  - 做 replay
  - 做 fork
- `workflow.py`
  - 放 state schema、nodes、graph builder
- `inspect_utils.py`
  - 放 history 查找和结果打印辅助函数
- `tests/test_inspect_utils.py`
  - 测试 checkpoint 查找与格式化逻辑

## 6. 验收标准

满足以下条件，Day10 就算基本过关：

- 你能解释 replay 和 fork 的区别
- 你能从 state history 找到目标 checkpoint
- 你能跑通 replay
- 你能跑通 fork
- 你能解释为什么 fork 不会覆盖原始历史

## 7. 常见坑

- 误以为 replay 只是读取历史结果
- 误以为 fork 会回滚并覆盖原历史
- 没有先看 history 就盲目选 checkpoint
- 不理解 checkpoint 之前和之后哪些节点会重跑
- 把原线程和 fork 分支混为一谈

## 8. 类比理解

可以把 Day10 类比成“从版本历史里做实验”：

- replay 像从旧版本重新跑构建
- fork 像从旧版本拉一个新分支继续开发

重点不是“回到过去”，而是：

`保留历史的同时，从历史上做新的实验。`

## 9. 今日交付物

今天你需要完成四件事：

1. 补完 `code/Day10/` 下的核心实现
2. 跑通原始执行、replay、fork 三组输出
3. 打印并解释目标 checkpoint
4. 回答 `answer/Day10-问题.md` 里的问题

## 10. 官网来源

今天主要对应这些官方页面：

- https://docs.langchain.com/oss/python/langgraph/use-time-travel
- https://docs.langchain.com/oss/python/langgraph/persistence
