from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

# 本地私有化部署的大模型
llm = ChatOpenAI(
    model='qwen3-8b',
    temperature=0.8,
    api_key='xx',
    base_url="http://localhost:6006/v1",
    extra_body={'chat_template_kwargs': {'enable_thinking': False}},
)

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"今天天气晴朗，在 {city}!"

graph = create_agent(
    model=llm,                      # 原来第一个位置参数 llm
    tools=[get_weather],
    system_prompt='你是智能助手' # 原来的 prompt 参数
)