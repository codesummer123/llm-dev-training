# Day9-训练内容

主题：Interrupt 不是“暂停一下”，而是把 LangGraph 变成“可人工介入、可恢复执行”的系统

## 1. 学习目标

今天的目标，是把 Day8 的 persistence 真正用起来，完成一个最小的 `interrupt / resume` 闭环。

完成今天后，你应该能回答：

- 为什么 interrupt 一定依赖 checkpointer 和 `thread_id`
- 为什么恢复时必须使用同一个 `thread_id`
- 为什么 `Command(resume=...)` 不是普通参数，而是“把外部输入送回暂停点”的机制

今天结束后，你应该具备的能力是：

- 能在 node 中正确调用 `interrupt()`
- 能获取 `__interrupt__` 或对应中断信息
- 能用 `Command(resume=...)` 恢复执行
- 能解释“暂停点恢复后，node 会从头重新执行”这件事意味着什么

## 2. What

### 2.1 今天要学的知识点

- `interrupt()`
- `Command(resume=...)`
- 中断 payload 必须 JSON-serializable
- 同一 `thread_id` 恢复执行
- approval / reject 模式
- review / edit 模式的基本认知
- interrupt 发生后 state 如何被 checkpoint 保存

### 2.2 核心概念

#### Interrupt 是动态暂停点

和“静态断点”不同，LangGraph 的 interrupt 可以放在 node 内部任意位置。  
它的意义不是“调试暂停”，而是：

`流程运行到这里，需要外部输入才能继续。`

这就是 human-in-the-loop 的基础能力。

#### Resume 不是“重新调用”，而是“把答案送回暂停位置”

当图在 `interrupt()` 处停住后，外部再次调用：

- `graph.invoke(Command(resume=...), config=...)`

这个 `resume` 的值会变成：

- node 内部 `interrupt()` 的返回值

这是 Day9 最关键的机制。

#### 同一个 thread 才是同一条暂停轨迹

今天你必须彻底理解：

- graph 是流程模板
- thread 是某次具体执行
- interrupt 暂停的是某条 thread
- resume 也必须继续这条 thread

如果换了 `thread_id`，就不是恢复，而是新开了一条执行轨迹。

## 3. Why

### 3.1 为什么 Day9 要在 Day8 之后立刻学 interrupt

因为 interrupt 不是一个孤立功能，它是 persistence 的直接应用。

没有 Day8 的 checkpoint 认知，Day9 很容易学成：

- “哦，就是停一下再继续”

但真正的本质是：

- 流程停住时，当前 state 被保存
- 外部稍后再回来
- 系统还能从原来的位置继续

这才是可恢复执行系统。

### 3.2 为什么今天先做 approval workflow

因为 approval / reject 是最清晰、最稳定、最容易观察的 interrupt 模式。

它能让你直观看到：

- interrupt payload 是什么
- resume 值如何进入节点
- 不同 resume 值如何改变后续路径

这个闭环看懂了，后面做 review/edit state、tool interrupts 就会顺很多。

## 4. How

### 4.1 今天的训练任务

你要实现一个“学习计划审批流”，至少支持：

1. 生成待审批的学习计划
2. 在审批节点中断
3. 用 `resume=True` 走批准路径
4. 用 `resume=False` 走拒绝路径

### 4.2 代码任务拆解

#### 任务 1：定义 State

建议至少包含：

- `plan_title`
- `plan_details`
- `status`
- `review_note`

其中 `status` 可以用：

- `pending`
- `approved`
- `rejected`

#### 任务 2：实现 interrupt 节点

审批节点至少要做到：

- 调用 `interrupt(...)`
- 把计划内容作为 payload 暴露出去
- 接收恢复值
- 根据恢复值决定走批准还是拒绝

要求：

- payload 必须 JSON-serializable
- 不要把复杂对象直接塞进 interrupt

#### 任务 3：实现批准与拒绝路径

你至少实现两个节点：

- `approve_node`
- `reject_node`

要求：

- 明确更新 `status`
- 写入 `review_note`

#### 任务 4：跑完整闭环

至少做两组演示：

- 一组 `resume=True`
- 一组 `resume=False`

观察：

- 初次 invoke 得到的中断信息是什么
- 恢复之后最终状态是什么

### 4.3 推荐运行流程

1. 先写图结构
2. 再写 interrupt 节点
3. 再写 approve / reject 路径
4. 最后分别跑批准和拒绝两组 thread

## 5. 代码设计说明

今天的脚手架已经放到 `code/Day9/`。

建议职责划分：

- `main.py`
  - 运行批准与拒绝两组演示
  - 打印中断信息和最终结果
- `workflow.py`
  - 放 state schema、interrupt node、route logic、graph builder
- `inspect_utils.py`
  - 放中断信息和最终状态的格式化函数
- `tests/test_workflow_interrupts.py`
  - 测试 interrupt / resume 的最小闭环

## 6. 验收标准

满足以下条件，Day9 就算基本过关：

- 你能解释 `interrupt()` 和 `Command(resume=...)` 的关系
- 你能跑通最小 approval / reject 流程
- 你能证明恢复使用的是同一个 `thread_id`
- 你能解释为什么 interrupt 依赖 checkpoint
- 你能说明“恢复后 node 会从头执行”意味着什么

## 7. 常见坑

- 忘了使用 checkpointer
- 恢复时换了 `thread_id`
- 把不可序列化对象塞进 interrupt payload
- 误以为 resume 是普通参数，不理解它会变成 `interrupt()` 的返回值
- 忽视“恢复后 node 从头执行”，导致副作用重复

## 8. 类比理解

可以把 Day9 的 interrupt 类比成“审批流中的待签字环节”：

- graph 像流程模板
- thread 像某个具体审批单
- interrupt 像卡在“等待签字”这一步
- `resume=True/False` 像签字通过或驳回

重点不是流程停了一下，而是：

`这张审批单被保存下来，之后还能接着处理。`

## 9. 今日交付物

今天你需要完成四件事：

1. 补完 `code/Day9/` 下的核心实现
2. 跑通 interrupt / resume 最小闭环
3. 展示批准和拒绝两条路径
4. 回答 `answer/Day9-问题.md` 里的问题

## 10. 官网来源

今天主要对应这些官方页面：

- https://docs.langchain.com/oss/python/langgraph/interrupts
- https://docs.langchain.com/oss/python/langgraph/persistence
