# Day3-训练内容

主题：Messages 是上下文载体，Structured Output 是把 Agent 从“会说”推进到“可控”

## 1. 学习目标

今天的目标，是把训练从“工具设计”推进到“输出可控”。

完成今天后，你应该能回答：

- 为什么很多 Agent 看起来答得不错，但系统接不住它的输出
- 为什么 `structured output` 会显著提升系统可控性
- 为什么 messages 不只是聊天记录，而是模型决策的上下文结构

今天结束后，你应该具备的能力是：

- 能读懂 `response["messages"]` 的基本结构
- 能基于 `Pydantic` schema 让 Agent 输出结构化结果
- 能比较自由文本输出和结构化输出的差别

## 2. What

### 2.1 今天要学的知识点

- `SystemMessage`、`HumanMessage`、`AIMessage`、`ToolMessage` 的角色
- 为什么 messages 是 Agent 的运行轨迹
- `response["messages"]` 和 `structured_response` 的区别
- `response_format` 的作用
- `ProviderStrategy` 和 `ToolStrategy` 的基本认知
- schema 校验失败意味着什么
- 为什么“模型能答对”和“系统能消费”不是一回事

### 2.2 核心概念

#### Messages 是上下文结构，不只是对话文本

传统理解里，messages 像聊天记录。  
更准确的理解是：

- messages 是模型当前可见的上下文
- messages 也是 Agent 执行过程的轨迹
- 工具调用、工具返回、最终回答都会体现在消息流里

也就是说，messages 同时承担两种职责：

- 给模型看的上下文
- 给开发者看的执行轨迹

#### Structured Output 是系统契约

自由文本适合人阅读，但不一定适合程序消费。  
一旦系统想把模型输出接到下游逻辑，就会遇到一个核心问题：

`模型说得像对的，不等于输出结构真的稳定。`

Structured output 的价值在于：

- 让输出字段可预期
- 让程序更容易接收结果
- 让失败更早暴露
- 让“模型行为”更接近“系统组件”

#### Schema 是对输出的约束

在 Day2，你已经用 schema 约束输入。  
今天你要进一步看到：

- schema 也可以约束输出
- 输出 schema 越清晰，系统越容易稳定集成
- schema 校验失败不是坏事，而是系统在帮你尽早发现不稳定行为

## 3. Why

### 3.1 为什么 Day3 要训练结构化输出

因为从工程角度看，很多真实系统都不只是“把模型回答打印出来”。

更常见的需求是：

- 抽取任务字段
- 生成 JSON 结果
- 给下游服务传结构化数据
- 把结果写入数据库
- 让 workflow 根据字段分支

如果没有结构化输出，系统就会很脆弱：

- 依赖字符串解析
- 容易被措辞波动打崩
- 不利于自动化测试

### 3.2 为什么 messages 要和 structured output 一起学

因为今天你要建立一个更完整的认知：

- messages 决定了模型看到什么
- structured output 决定了系统接到什么

前者是输入上下文，后者是输出契约。  
把这两端连起来，你才开始真正理解 Agent 不是“会聊天”，而是“可编排的信息处理单元”。

## 4. How

### 4.1 今天的训练任务

你要实现一个“学习任务抽取 Agent”，至少支持两种模式：

1. 自由文本回答模式
2. 结构化输出模式

它的核心任务是：  
从用户的自然语言学习需求中，提取出一个标准化学习任务对象。

建议包含字段：

- `topic`
- `goal`
- `difficulty`
- `minutes_available`
- `deliverable`

### 4.2 代码任务拆解

#### 任务 1：定义输出 schema

请在 `schemas.py` 中定义一个 `Pydantic` 输出模型，例如：

- `StudyTask`

要求：

- 至少 5 个字段
- 至少 1 个 `Literal`
- 至少 1 个数值范围约束
- 每个字段都要写清楚 description

#### 任务 2：实现自由文本模式

先做一个不使用 structured output 的版本。  
它只返回普通文本，用来做对照实验。

目的：

- 让你直观看到“人看起来还行”的回答，不一定适合程序使用

#### 任务 3：实现结构化输出模式

使用 `response_format` 把输出绑定到 `StudyTask`。

要求：

- 明确区分“文本模式”和“结构化模式”
- 结构化模式下，读取并打印结构化结果
- 观察 response 里除了 messages 之外是否还有结构化结果字段

#### 任务 4：观察消息流

你至少要做两类观察：

- 文本模式下，`messages` 长什么样
- 结构化模式下，`messages` 和 `structured_response` 有什么差异

#### 任务 5：准备失败样本

你可以主动设计一个容易失败的输入，例如：

- 分钟数说得很模糊
- 同时说了多个目标
- 输出格式要求不明确

目的不是一定要让它报错，而是训练你开始思考：

- schema 在哪里帮你兜底
- 哪些模糊输入会放大不稳定性

### 4.3 推荐运行流程

1. 先完成自由文本模式
2. 再定义输出 schema
3. 再接 structured output
4. 最后打印 messages 和 structured result 做对比

不要一开始就只盯着“结构化输出有没有成功”，要同时观察它和自由文本模式的差异。

## 5. 代码设计说明

今天的脚手架已经放到 `code/Day3/`。

建议职责划分：

- `main.py`
  - 初始化模型
  - 构建文本模式 agent
  - 构建结构化模式 agent
  - 打印结果和消息轨迹
- `schemas.py`
  - 放输出 schema
- `prompts.py`
  - 放 system prompt
- `tests/test_structured_output.py`
  - 验证 schema 和辅助函数

## 6. 验收标准

满足以下条件，Day3 就算基本过关：

- 你能解释 messages 为什么不是单纯聊天记录
- 你实现了至少一个结构化输出 schema
- 你能区分自由文本模式和结构化模式的差异
- 你能指出 structured output 为什么更利于系统集成
- 你能解释 schema 校验失败为什么是一种保护

## 7. 常见坑

- 只关注最终文本，不看 `messages`
- 以为 structured output 只是“自动转 JSON”
- schema 字段描述太弱，导致模型输出不稳定
- 没有区分“给人看”和“给系统接”的输出目标
- 没有观察失败样本，只在顺风输入上测试

## 8. 类比理解

可以把今天的训练类比成“把口头需求变成标准表单”：

- 自由文本像口头描述，适合交流
- structured output 像标准表单，适合进入系统
- messages 像整个沟通过程记录
- schema 像表单字段规则

如果只有口头描述，没有表单规则，系统后面就很难稳定处理。

## 9. 今日交付物

今天你需要完成四件事：

1. 补完 `code/Day3/` 下的核心实现
2. 对比跑通文本模式和结构化模式
3. 记录至少 1 组 messages 与 structured result 的差异
4. 回答 `answer/Day3-问题.md` 里的问题

## 10. 官网来源

今天主要对应这些官方页面：

- https://docs.langchain.com/oss/python/langchain/messages
- https://docs.langchain.com/oss/python/langchain/structured-output
- https://docs.langchain.com/oss/python/langchain/agents
