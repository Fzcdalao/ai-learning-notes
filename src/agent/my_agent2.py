from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.prebuilt import create_react_agent
from agent.my_llm import llm
from agent.tools.tool_demo6 import runnable_tool
"""
短期存储
# 在生产环境中，使用由数据库支持的检查点
DB_URI = "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable"
with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
# 必须安装：pip install -U "psycopg[binary,pool]" langgraph-checkpoint-postgres

# 生产环境：Redis
# pip install -U langgraph-checkpoint-redis
DB_URI = "redis://:6379"
with RedisSaver.from_conn_string(DB_URI) as checkpointer:

注意：
•首次使用 Postgres 存储时，您需要调用 store.setup()，checkpointer.setup()
•首次使用 Redis 存储时，您需要调用 store.setup()，checkpointer.setup()
"""

# checkpointer = InMemorySaver() #短期记忆，保存到内存中
DB_URI ='postgresql://postgres:root@localhost:5432/postgres'
with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
    checkpointer.setup() #第一次使用时，记得建表
    def get_weather(city: str) -> str:
        """Get weather for a given city."""
        return f"今天天气晴朗，在 {city}!"
    agent = create_react_agent(
        llm,
        tools=[runnable_tool,get_weather],
        prompt="你是一个智能助手，尽量调用工具回答用户的问题",
        checkpointer=checkpointer,
    )

    config = {
        "configurable":{
            "thread_id":"1"
        }
    }

    resp1 =agent.invoke(
        {"messages":[{"role":"user","content":"西安今天天气怎么样"}]},
        config,
    )

    print(resp1['messages'][-1].content)

    resp2 =agent.invoke(
        {"messages":[{"role":"user","content":"那北京今天天气怎么样？"}]},
        config,
    )
    print(resp2['messages'][-1].content)