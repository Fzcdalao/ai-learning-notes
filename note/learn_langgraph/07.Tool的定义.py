"""
工具的定义：
##在构建Agent 时，您需要为其提供一个它可以使用的 工具 列表。除了实际调用的函数之外，工具还包括几个组件：
属性           类型                         描述
名称              str                      在提供给LLM或代理的一组工具中必须是唯一的。
描述              str                      描述工具的作用。被LLM或代理用作上下文。
args_schema      pydantic.BaseModel       可选但推荐，如果使用回调处理程序则为必需。它可用于为预期参数提供更多信息(例如，少量示例)或验证。
return_direct    boolean                  仅与代理相关。当为True时，在调用给定工具后，代理将停止并将结果直接返回给用户。

如果一个tool的名称、描述和args_schema 是精心准备的，那么模型将表现的更好

工具的创建：
LangChain 支持从以下对象创建工具
1.函数；demo1-5
2.LangChain Runnables；所有的langchain Runnable对象都可以直接变成工具使用
    runnable_tool = chain.as_tool(
        name=
        description=
        args_schema=
    )
   demo6
3.通过从 BaseTool 子类化 -- 这是最灵活的方法，它提供了最大的控制程度，但代价是需要付出更多的努力和编写更多的代码。



Tool工具在部署在服务器上的时候需要按照以下目录结构：
my-app/
    my_agent # all project code lies within here
        utils # utilities for your graph
            __init__.py
            tools.py # tools for your graph
            nodes.py # node functions for you graph
            state.py # state definition of your graph
        __init__.py
    agent.py # code for constructing your graph.env # environment variables
    langgraph.json # configuration file for LangGraph
    pyproject.toml # dependencies for your project

Stream message chunks:
LangGraph 的流式模式之一。`messages` 模式下，大模型每生成一小段文字（一个 token 或几个 token）就推一个 **message chunk**（消息片段）给你，
而不是等整条回答生成完再发。这就是聊天软件里 "字一个个往外蹦" 的效果来源。


"""

