"""
FastMCP：构建模型上下文协议（MCP）服务器的快速Python方案

安装 langchain-mcp-adapters 库以在LangGraph中使用 MCP工具
    【pip install langchain-mcp-adapters】

这部分的内容需要一个智能体中同时可以调用  python写的、java写的和其他公司发布的MCP工具
 ·python； FastMCP ：【pip install fastmcp】 注意：【python -m pip install "mcp>=1.24,<2.0" "langchain-mcp-adapters"】`langchain-mcp-adapters 0.3.2` 锁死要求 `mcp>=1.24,<2.0`；
 这部分可以看：tool_server.py | start_see_server.py |   start_streamable_server.py
 ·java；spring ai、spring claud
 ·其他公司的MCP

·Agent调用Python服务器
    这里先用python 来做了个 mcp服务器：tool_server.py
    通过 start_see_server.py 可以启动 tool_server.py 的服务
    在mcp_agent中： 通过配置 MultiServerMCPClient 可以获取python服务器中的提示词、工具、数据 ，再异步构建智能体，将其配置到langgraph中使用
    先打开 start_see_server.py 让python服务器启动，再跑langgraph dev 构建智能体
·Agent调用Java服务器
这部分的代码在 AI实战工具课->Authropic MCP协议->JavaAPI - MCP
"""

"""
python: await函数
`await` 的意思是：**把这个协程（或可等待对象）挂起，把 CPU 交还给事件循环，等结果出来了再继续往下执行**。

它解决的是 IO 等待的问题。网络请求、读数据库、调 MCP 工具这类操作，99% 的时间都在等对方返回，线程本身是闲着的。用 `await` 等待的写法，
就能让线程在等待期间去处理别的任务，而不是一直占着 CPU 空转。
"""
