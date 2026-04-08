# Day8-问题

主题：为什么 checkpoint 不是“存档功能”，而是 LangGraph 高级能力的地基

## 1. 常见问题

### Q1. `thread_id` 和 checkpoint 的关系是什么？

参考作答方向：

- `thread_id` 标识一条执行轨迹
- checkpoint 是这条轨迹上的状态快照
- 没有 thread，就没有可持续追踪的状态历史

### Q2. 为什么 persistence 不是只保存最终结果？

参考作答方向：

- LangGraph 会按执行步骤保存 checkpoint
- 这让系统能查看过程，而不只是终态
- 过程可见，后续才有恢复、调试、回放的基础

### Q3. 为什么 `graph.get_state_history()` 很重要？

参考作答方向：

- 因为它让你看到状态是怎么一步步演化的
- 很多 bug 只看终态是看不出来的

## 2. 面试问题

### Q1. 为什么说 checkpoint 是 LangGraph 高级能力的基础？

作答要点：

- interrupt、memory、time travel、durable execution 都依赖 checkpoint
- 没有 checkpoint，这些能力就缺少状态基础

### Q2. 为什么 thread 和 graph 不是一个概念？

作答要点：

- graph 是流程定义
- thread 是某次具体执行轨迹
- 同一个 graph 可以对应多个不同 thread

### Q3. `graph.get_state()` 和 `graph.get_state_history()` 的区别是什么？

作答要点：

- `get_state()` 看当前最新 snapshot
- `get_state_history()` 看完整历史轨迹
- 一个看终点附近，一个看演化过程

## 3. 开脑问题

### Q1. 如果一个系统只能看到最终状态，看不到中间 checkpoint，会失去什么？

思考方向：

- 很难调试
- 很难解释执行过程
- 很难做恢复与回放

### Q2. 为什么很多工程问题其实都不是“结果错了”，而是“中间某一步偏了”？

思考方向：

- 因为复杂系统是逐步演化的
- 终态只是最后表现，问题往往更早发生

### Q3. 如果未来要做 interrupt / human-in-the-loop，现在为什么必须先理解 checkpoint？

思考方向：

- 因为中断之后要恢复，就必须知道恢复到哪一个状态快照
- 没有 checkpoint，中断就只是“停住”，而不是“可恢复”

## 4. 今日输出要求

请你在完成代码后，至少自己回答下面两个问题：

1. 为什么说 checkpoint 让 LangGraph 从“可执行流程”变成“可追踪、可恢复流程”？
2. 如果两个 thread 跑的是同一张图，但历史不同，这说明了什么？
