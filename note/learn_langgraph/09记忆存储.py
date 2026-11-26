# 二、记忆存储 *****
"""
这是一个强大的功能，允许您在多次调用中持久化代理的状态。否则，状态仅限于单次运行。
1.短期存储：线程级存储，‘会话’级别的存储——>解决多轮对话的问题
    短期存储使Agent能够跟踪多轮对话。
                  ① 使用内存存储
                  要使用它，您必须：1.在创建代理时提供checkpointer。checkpointer可以实现代理状态的持久性。
                                2.在运行代理时在配置中提供thread_id。thread_id是对话会话的唯一标识符。
                                代码看 my_agent2
                                注意：langgraph.checkpoint.memory.InMemorySaver ：开源库自带 checkpointer（旧名 MemorySaver）
                                    langgraph_runtime_inmem.checkpoint.InMemorySaver： dev 服务器内部实现，依赖服务器配置（REDIS_URI 等）
                  ②使用关系型数据库postgresql来实现短期存储
                                代码看 my_agent2
                                 注意：
                                    •首次使用 Postgres 存储时，您需要调用 store.setup()，checkpointer.setup()
                                    •首次使用 Redis 存储时，您需要调用 store.setup()，checkpointer.setup()
                                可以在PostgreSQL\17\pgAdmin 4\runtime目录下的pgAdmin4.exe可视化界面中查看

2.长期存储：跨线程存储，跨‘会话’存储
使用长期内存来跨会话存储用户特定或应用程序特定的数据。这对于聊天机器人等应用程序非常有用，您可能希望记住用户偏好或其他信息
        ①使用内存
        ②使用关系型数据库


在langgraph中，不管是开发智能体还是workflower，短期存储使用checkpoint，长期存储使用store
"""