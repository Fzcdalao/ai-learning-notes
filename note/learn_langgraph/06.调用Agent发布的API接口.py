"""
1.使用python调用
这个api接口说的就是上次项目运行后生成的
先用SDK测试一下：pip install langgraph-sdk
写一个单元测试（异步测试）：
from langgraph_sdk import get_client
import asyncio

client = get_client(url="http://localhost:2024")

async def main():
    async for chunk in client.runs.stream(
        None,  # Threadless run
        "agent", # Name of assistant. Defined in langgraph.json.
        input={
        "messages": [{
            "role": "human",
            "content": "What is LangGraph?",
            }],
        },
    ):
        print(f"Receiving new event of type: {chunk.event}...")
        print(chunk.data)
        print("\n\n")

asyncio.run(main())
异步测试：程序发出一个耗时操作（如调用大模型 API）后**不傻等**，先去干别的，结果回来了再处理。对应 Python 的 `async def` / `await` 语法。
测试前记得： 关掉这个运行配置的 uv run
1. PyCharm 菜单：**运行 → 编辑配置**（Run → Edit Configurations）；
2. 左侧选中 **MyTest**；
3. 找到 **"Run with uv run"（使用 uv run 运行）** 复选框，**取消勾选**；
4. 确定，重新运行。
同步（调用）测试：
from langgraph_sdk import get_sync_client

client = get_sync_client(url="http://localhost:2024")

for chunk in client.runs.stream(
    None,  # Threadless run
    "agent", # Name of assistant. Defined in langgraph.json.
    input={
        "messages": [{
            "role": "human",
            "content": "What is LangGraph?",
        }],
    },
    stream_mode="messages-tuple",
):
    print(f"Receiving new event of type: {chunk.event}...")
    print(chunk.data)
    print("\n\n")


"""

## 这部分的测试看 MyTest.py 和 MyTest_async.py