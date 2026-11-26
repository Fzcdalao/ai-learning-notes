from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.prebuilt import create_react_agent
from langgraph.store.postgres import PostgresStore

from agent.my_llm import llm
from agent.tools.tool_demo6 import runnable_tool
"""
长期存储
# 开发环境中： 内存
store = InMemoryStore()

# 在生产环境中，使用由数据库支持的存储
postgresql:
DB_URI = "postgresql://postgres:postgres@localhost:5442/postgres?sslmode=disable"
with (
    PostgresStore.from_conn_string(DB_URI) as store,    //做长期存储
    PostgresSaver.from_conn_string(DB_URI) as checkpointer, //做短期存储
):    
    # store.setup()    
    # checkpointer.setup()
    
redis:
DB_URI = "redis://:6379"
with (    
    RedisStore.from_conn_string(DB_URI) as store,  //做长期存储  
    RedisSaver.from_conn_string(DB_URI) as checkpointer, //做短期存储
):    
    store.setup()    
    checkpointer.setup()
"""

DB_URI ='postgresql://postgres:root@localhost:5432/postgres'
with (
    PostgresStore.from_conn_string(DB_URI) as store,
    PostgresSaver.from_conn_string(DB_URI) as checkpointer
):
    store.setup()
    checkpointer.setup() #第一次使用时，记得建表
    def get_weather(city: str) -> str:
        """Get weather for a given city."""
        return f"今天天气晴朗，在 {city}!"
    agent = create_react_agent(
        llm,
        tools=[runnable_tool,get_weather],
        prompt="你是一个智能助手，尽量调用工具回答用户的问题",
        checkpointer=checkpointer,
        store=store,
    )

    config = {
        "configurable":{
            "thread_id":"1"
        }
    }

    resp1 =agent.invoke(
        {"messages":[{"role":"user","content":"给我一个关系相声的报幕词"}]},
        config,
    )

    print(resp1['messages'][-1].content)

    resp2 =agent.invoke(
        {"messages":[{"role":"user","content":"再给我一个关于流行歌曲《花海》的"}]},
        config,
    )
    print(resp2['messages'][-1].content)