# Day5-训练内容

主题：Middleware 是把 Context Engineering 变成“可执行控制”的关键层

## 1. 学习目标

今天的目标，是把训练从“管理输入输出”推进到“主动改变 Agent 的运行行为”。

完成今天后，你应该能回答：

- 为什么 middleware 是 context engineering 的执行层
- 为什么有些上下文修改应该是瞬时的，而不是持久写进 state
- 为什么有些请求应该在模型调用前就被拦住

今天结束后，你应该具备的能力是：

- 能写一个动态 system prompt middleware
- 能写一个调用前短路的 middleware
- 能解释 transient context 和 persistent context 的差别

## 2. What

### 2.1 今天要学的知识点

- middleware 的两类 hook
- node-style hooks
- wrap-style hooks
- `before_model`
- `wrap_model_call`
- 动态 system prompt
- 短路返回 `jump_to="end"`
- transient context 与 persistent context

### 2.2 核心概念

#### Middleware 是执行时控制层

如果说：

- prompt 决定“默认行为”
- tools 决定“可用能力”
- memory 决定“保留哪些上下文”

那么 middleware 决定的是：

`在运行时，系统怎样主动修改、限制、增强这些行为。`

它不只是“附加逻辑”，而是 Agent 控制面的重要组成部分。

#### Wrap-style Hook 适合做瞬时上下文修改

`wrap_model_call` 的典型价值是：

- 改 system prompt
- 改模型
- 改 tools
- 做 transient context 修改

重点在于：

- 这类修改只影响当前这次模型调用
- 不一定写回 state

这非常适合做“按当前情况动态调整”的控制逻辑。

#### Node-style Hook 适合做顺序控制和状态更新

`before_model` 的典型价值是：

- 调用前检查
- 限制请求
- 做 guardrail
- 必要时提前结束

今天你会用它来做一个很典型的动作：

- 当用户请求过于宽泛时，不进入模型调用，直接给出更合理的边界提示

## 3. Why

### 3.1 为什么 Day5 要学 middleware

因为到现在为止，你已经会：

- 设计工具
- 约束输出
- 管理短期记忆

但你还没有真正掌握：

- 如何在运行时改变 Agent 的行为

现实中的 Agent 系统很少是“固定 prompt + 固定流程”就够了。  
更常见的需求是：

- 新手和熟手看到不同风格的回答
- 请求太宽泛时先收窄范围
- 某些条件下切换模型或切换工具
- 在调用前后做日志、校验、限制、增强

这就是 middleware 发挥作用的地方。

### 3.2 为什么今天要同时练动态 prompt 和短路控制

因为这两件事刚好能让你理解：

- 什么是 transient context 修改
- 什么是运行时控制流拦截

前者偏“增强”
后者偏“限制”

两者合在一起，你才开始真正理解 middleware 不只是“加点辅助代码”，而是：

`系统运行时的控制面。`

## 4. How

### 4.1 今天的训练任务

你要实现一个“学习教练 Agent”，至少具备两类 middleware 能力：

1. 根据用户水平动态注入不同 system prompt
2. 当用户请求过于宽泛时，在模型调用前直接短路结束

### 4.2 代码任务拆解

#### 任务 1：动态 prompt middleware

你需要写一个 `wrap_model_call` middleware。

它至少做到：

- 根据用户输入判断当前更像“入门者”还是“进阶者”
- 对入门者注入更偏步骤化、低认知负担的 instruction
- 对进阶者注入更偏抽象、边界、权衡的 instruction

要求：

- 这种修改是 transient 的
- 不把这段动态 prompt 永久写进 state

#### 任务 2：短路 middleware

你需要写一个 `before_model` middleware。

它至少做到：

- 当请求明显过宽，例如“今天把 LangChain、LangGraph、Deep Agents 全部讲完并写完代码”
- 不进入模型调用
- 直接返回一个更合理的范围建议

要求：

- 用 `jump_to="end"` 提前结束
- 让你看到 middleware 可以直接改变执行流

#### 任务 3：设计可测试的辅助函数

今天不要把所有判断逻辑都塞进装饰器函数里。

建议拆出至少 3 个辅助函数：

- 判断用户水平
- 生成动态 instruction
- 判断请求是否过宽

这样你可以独立测试逻辑，而不是只能靠完整 Agent 验证。

#### 任务 4：准备演示样例

至少跑三类输入：

- 入门型请求
- 进阶型请求
- 过宽请求

并观察：

- 最终回答是否风格不同
- 过宽请求是否被提前拦截

### 4.3 推荐运行流程

1. 先只写辅助函数并通过测试
2. 再接动态 prompt middleware
3. 再接短路 middleware
4. 最后跑三类输入做观察

## 5. 代码设计说明

今天的脚手架已经放到 `code/Day5/`。

建议职责划分：

- `main.py`
  - 初始化模型
  - 创建 agent
  - 跑三类演示输入
- `middleware.py`
  - 放 middleware 和可测试辅助函数
- `prompts.py`
  - 放基础 system prompt
- `tests/test_middleware_helpers.py`
  - 测试辅助函数逻辑

## 6. 验收标准

满足以下条件，Day5 就算基本过关：

- 你能解释 `before_model` 和 `wrap_model_call` 的区别
- 你实现了一个动态 system prompt middleware
- 你实现了一个调用前短路 middleware
- 你能解释为什么动态 prompt 更适合做 transient 修改
- 你能解释为什么短路控制属于运行时控制流能力

## 7. 常见坑

- 把 transient prompt 修改错误地当成 persistent state
- 动态 prompt 写得太长，反而污染上下文
- 过宽请求判断逻辑过于随意
- 短路逻辑没有明确告诉用户“为什么被拦截”
- 只做 middleware，不做可测试辅助函数

## 8. 类比理解

可以把 middleware 类比成“会议主持人”：

- 动态 prompt 像主持人根据听众水平调整表达方式
- 短路控制像主持人发现议题太散时，先要求收窄范围再继续

也就是说，middleware 不只是记录会议内容，而是在主动控制会议怎么进行。

## 9. 今日交付物

今天你需要完成四件事：

1. 补完 `code/Day5/` 下的核心实现
2. 跑通入门型、进阶型、过宽型三类输入
3. 观察短路是否真的在模型调用前发生
4. 回答 `answer/Day5-问题.md` 里的问题

## 10. 官网来源

今天主要对应这些官方页面：

- https://docs.langchain.com/oss/python/langchain/middleware/overview
- https://docs.langchain.com/oss/python/langchain/middleware/custom
- https://docs.langchain.com/oss/python/langchain/context-engineering
