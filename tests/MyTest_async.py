from langgraph_sdk import get_client
import asyncio

#调用智能体发布的API接口
client = get_client(url="http://127.0.0.1:2024") #接口地址

async def main():
    async for chunk in client.runs.stream(
        None,  # Threadless run
        "agent", # Name of assistant. Defined in langgraph.json.
        input={
        "messages": [{
            "role": "human",
            "content": "今天西安天气如何?",
            }],
        },
    ):
        print(f"Receiving new event of type: {chunk.event}...")
        print(chunk.data)
        print("\n\n")

if __name__ == "__main__":

    asyncio.run(main())