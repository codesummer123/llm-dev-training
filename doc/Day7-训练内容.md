# Day7-训练内容

主题：LangGraph 的本质不是“更复杂的 Agent”，而是“带状态的可控工作流”

## 1. 学习目标

今天的目标，是正式进入 `LangGraph`，先把最底层的图编排抽象吃透。

完成今天后，你应该能回答：

- 为什么 LangGraph 的关键不是“图长什么样”，而是“状态怎么流动”
- 为什么 `State / Node / Edge` 比“写一堆 if/else”更适合复杂 Agent 系统
- 为什么 LangGraph 不是只给 LLM 用，而是给“带状态的工作流”用

今天结束后，你应该具备的能力是：

- 能独立写一个最小 `StateGraph`
- 能定义 `State`
- 能写多个 `Node`
- 能通过 `add_conditional_edges` 做条件路由
- 能打印并解释最终状态

## 2. What

### 2.1 今天要学的知识点

- `StateGraph`
- `START` / `END`
- `TypedDict` state schema
- node 的输入输出约定
- edge 与 conditional edge
- compile 的作用
- graph invoke 的结果结构
- route function 的角色

### 2.2 核心概念

#### State 是图中的“共享事实”

LangGraph 的核心不是节点本身，而是：

`节点如何读取和更新同一份状态。`

也就是说：

- node 不是孤立函数
- edge 不是单纯跳转线
- 整个图真正串起来的是 state

#### Node 是“一个明确职责步骤”

一个 node 最好只做一件清晰的事，例如：

- 分析输入
- 判断是否需要补基础
- 生成某类计划
- 输出最终总结

这和我们前面说的工具单一职责很像。  
区别是：

- tool 更像模型可调用能力
- node 更像 workflow 的一个步骤

#### Edge 决定执行流

固定 edge 表示：

- 一定按顺序走

条件 edge 表示：

- 根据当前 state 决定下一步去哪

这就是 LangGraph 和“顺手写一坨流程代码”最大的差别之一：

`流程结构被显式建模了。`

## 3. Why

### 3.1 为什么 Day7 不急着上复杂 LLM 图

因为刚进入 LangGraph，最容易犯的错误是：

- 一边学图
- 一边学模型调用
- 一边学 memory
- 一边学 routing

最后什么都混在一起。

今天故意把 LLM 复杂度降下来，是为了先抓住 LangGraph 最底层的骨架：

- state
- node
- edge
- route

这层一旦清楚，后面再往图里塞 LLM、memory、interrupt，才不会乱。

### 3.2 为什么 LangGraph 值得单独学

因为到 LangChain 为止，你主要是在学：

- 模型怎么用
- 工具怎么设计
- 输出怎么约束
- memory 怎么治理

而 LangGraph 解决的是另一个层面的问题：

- 多步骤流程怎么编排
- 带状态执行怎么控制
- 执行中断、恢复、持久化怎么设计

也就是说，LangGraph 不是“又一个 API”，而是：

`把 Agent 系统从单次调用提升到工作流系统的底层框架。`

## 4. How

### 4.1 今天的训练任务

你要实现一个“学习路径分流图”，根据用户水平和目标，把请求路由到不同的学习计划节点。

至少包含：

1. 输入分析节点
2. 条件路由函数
3. 基础补强节点
4. 常规训练节点
5. 进阶深挖节点
6. 收尾节点

### 4.2 代码任务拆解

#### 任务 1：定义 State

建议至少包含这些字段：

- `user_goal`
- `user_level`
- `needs_foundation`
- `track`
- `plan`
- `route_log`

要求：

- 用 `TypedDict`
- 某些列表字段可以设计成累加式结果

#### 任务 2：实现多个 Node

建议节点职责如下：

- `analyze_request`
  - 判断用户水平
  - 判断是否要补基础
  - 产出 track 信息
- `foundation_plan`
  - 给基础薄弱用户补基建计划
- `standard_plan`
  - 给常规用户生成标准训练路径
- `advanced_plan`
  - 给进阶用户生成深挖路径
- `finalize`
  - 汇总状态，输出最终可读结果

#### 任务 3：实现条件路由

至少做一个明确的 route function：

- 如果 `needs_foundation` 为真，去 `foundation_plan`
- 如果 `user_level` 是进阶，去 `advanced_plan`
- 否则去 `standard_plan`

#### 任务 4：打印路由结果

今天不要只看最终计划内容。

你至少要打印：

- 最终状态
- `route_log`
- 最终走了哪条路径

### 4.3 推荐运行流程

1. 先只写 state schema 和 node
2. 再把固定 edge 串起来
3. 再补 conditional edge
4. 最后跑 3 组不同输入做路径对照

## 5. 代码设计说明

今天的脚手架已经放到 `code/Day7/`。

建议职责划分：

- `main.py`
  - 构建 graph
  - 跑多个样例输入
  - 打印最终状态与路由
- `workflow.py`
  - 放 state schema、nodes、route function、graph builder
- `tests/test_workflow.py`
  - 测试路由函数和关键 node 的行为

## 6. 验收标准

满足以下条件，Day7 就算基本过关：

- 你能解释 `State / Node / Edge` 三者关系
- 你能跑通最小 `StateGraph`
- 你实现了至少一个条件路由
- 你能展示不同输入走出不同路径
- 你能解释 LangGraph 为什么不是单纯“把 if/else 画成图”

## 7. 常见坑

- 把 state 写成随意变量堆
- node 职责过重
- route function 读不清 state
- 只看最终答案，不看 route_log
- 学 LangGraph 时把所有复杂能力一起上，导致抽象混乱

## 8. 类比理解

可以把 LangGraph 类比成“带共享白板的项目流程图”：

- state 像团队共享白板
- node 像一个个岗位步骤
- edge 像流转规则
- conditional edge 像根据白板当前内容决定下一步交给谁

重点不是画图本身，而是：

`每一步都基于同一份共享事实做决策。`

## 9. 今日交付物

今天你需要完成四件事：

1. 补完 `code/Day7/` 下的核心实现
2. 跑通最小 LangGraph 工作流
3. 用不同输入做路径对照
4. 回答 `answer/Day7-问题.md` 里的问题

## 10. 官网来源

今天主要对应这些官方页面：

- https://docs.langchain.com/oss/python/langgraph/quickstart
- https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph
- https://docs.langchain.com/oss/python/langgraph/graph-api
- https://docs.langchain.com/oss/python/langgraph/workflows-agents
