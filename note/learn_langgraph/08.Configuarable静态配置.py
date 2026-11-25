# Agent的上下文和记忆
# 一、上下文
"""
上下文包括消息列表之外的任何数据，这些数据可以影响代理行为或工具执行
有两个概念：
1. Configurable ： 这是用于做静态配置的对象；配置适用于不可变数据，如用户元数据或 API 密钥。当您有在运行期间不会更改的值时使用。
    agent.invoke(
    {"messages": [{"role": "user", "content": "hi!"}]},
    config={"configurable": {"user_id": "user_123"}})------动态的设置提示词模板
    demo8 -> 获取用户信息的工具
2. 状态AgentState（可变上下文）:状态在运行期间充当Agent的记忆，可以短期存储也可以长期存储。它保存可在执行期间演变的动态数据，例如从工具或 LLM 输出派生的值
    AgentState（类）的作用: **图里所有节点共同读写的那份数据结构**——Agent 运行过程中 "记得什么、传什么"，全由它定义。
                            messages: Annotated[list[AnyMessage], add_messages]
                            每个节点的输入是 state、输出是对 state 的更新。AgentState 就是节点之间的**接口约定**：大家都按这个结构读写，不会各说各话。
                            主要是通过Command指令来更新state

    案例：（给用户发出一个祝福语句）输入username ---> config----> 工具1---> 把username修改到State中------> 工具2----->获取State的username得到最终答案。
    这里的工具1是demo9中的get_user_name，工具2是demo9中的greet_user
    记得在智能体中指定graph = create_react_agent(model=llm, tools=[...], state_schema=CustomState)
"""

#二、记忆存储 *****
"""
这是一个强大的功能，允许您在多次调用中持久化代理的状态。否则，状态仅限于单次运行。
1.短期存储：线程级存储，会话级别的存储——>解决多轮对话的问题
    短期存储使Agent能够跟踪多轮对话。
    要使用它，您必须：1.在创建代理时提供checkpointer。checkpointer可以实现代理状态的持久性。
                  2.在运行代理时在配置中提供thread_id。thread_id是对话会话的唯一标识符。
2.长期存储：跨线程存储，跨会话存储
"""