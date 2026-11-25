from langgraph_sdk import get_sync_client

client = get_sync_client(url="http://127.0.0.1:2024")

for chunk in client.runs.stream(
    None,  # Threadless run
    "agent", # Name of assistant. Defined in langgraph.json.
    input={
        "messages": [{
            "role": "human",
            "content": "告诉我当前用户的年龄",
        }],
    },
    stream_mode="messages", #输出的每个消息 包含了chunk的内容，也包含了chunk的元数据，直接加messages就是直接返回chunk的内容
    config={"configurable":{"user_name":"user_123"}}
):
    print(f"Receiving new event of type: {chunk.event}...")
    print(chunk.data)
    print("\n\n")

