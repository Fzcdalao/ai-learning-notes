"""
FastMCP：构建模型上下文协议（MCP）服务器的快速Python方案

安装 langchain-mcp-adapters 库以在LangGraph中使用 MCP工具
    【pip install langchain-mcp-adapters】

这部分的内容需要一个智能体中同时可以调用  python写的、java写的和其他公司发布的MCP工具
 ·python； FastMCP ：【pip install fastmcp】 注意：【python -m pip install "mcp>=1.24,<2.0" "langchain-mcp-adapters"】`langchain-mcp-adapters 0.3.2` 锁死要求 `mcp>=1.24,<2.0`；
 这部分可以看：tool_server.py | start_see_server.py |   start_streamable_server.py
 ·java；spring ai、spring claud
 ·其他公司的MCP


"""