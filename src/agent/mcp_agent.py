import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv
# 显式指定 .env 路径：load_dotenv() 默认是从“当前工作目录”往上找，
# 脚本在 src/agent 下而 cwd 在别处时会找不到，于是 os.environ[...] 直接 KeyError
load_dotenv(Path(__file__).resolve().parents[2] / ".env")

from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

from agent.my_llm import llm

#Python MCP服务端连接配置
python_mcp_server_config = {
    #'url': 'http://127.0.0.1:8080/stramable',
    #'transport': 'stramable_http',
    'url': 'http://127.0.0.1:8080/sse',
    'transport': 'sse',
}
#JAVA MCP服务端连接配置
"""
这部分需要在java那边把服务启动，注意端口号记得不要占用
JAVA_mcp_server_config = {
    #'url': 'http://127.0.0.1:8086/stramable',
    #'transport': 'stramable_http',
    'url': 'http://127.0.0.1:8086/sse',
    'transport': 'sse',
}
"""
zhipu_api_key = os.getenv("ZHIPU_API_KEY")
if not zhipu_api_key:
    raise RuntimeError("缺少 ZHIPU_API_KEY，请检查项目根目录的 .env")

#外网上公开的 MCP服务端连接配置（智谱 AI 的 web-search 是 streamable-http，不是 sse）
zhipu_web_search = {
    "url": "https://open.bigmodel.cn/api/mcp-broker/proxy/web-search/mcp",
    "transport": "streamable_http",
    "headers": {"Authorization": zhipu_api_key},
}
#MCP客户端
mcp_client = MultiServerMCPClient({
    'python_mcp': python_mcp_server_config,
    # 'zhipu_mcp': zhipu_web_search,
})

#使用异步函数创建agent智能体（必须是异步环境）
async def create_my_agent():
    mcp_tools = await mcp_client.get_tools()
    print(mcp_tools)
    # prompt / resources 是"有就取、没有就跳过"，避免缺资源时整个 graph 加载失败
    try:
        p = await mcp_client.get_prompt(server_name='python_mcp',prompt_name='ask_about_topic',arguments={'topic':'深度学习'})
        print(p)
    except Exception as e:
        print(f"[skip] 获取 prompt 失败: {type(e).__name__}: {e}")
    try:
        datas = await mcp_client.get_resources(server_name='python_mcp',uris='resources://config')
        print(datas)
    except Exception as e:
        print(f"[skip] 获取 resources 失败: {type(e).__name__}: {e}")


    return create_agent(
        llm,                      # 原来第一个位置参数 llm
        tools=mcp_tools,
        system_prompt="你是一个智能助手，尽量调用工具回答用户的问题",
    )

agent = asyncio.run(create_my_agent()) #异步函数不能在非异步的环境中执行，这样写就可以把智能体对外暴露出来了