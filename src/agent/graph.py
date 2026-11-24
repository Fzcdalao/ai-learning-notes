from dotenv import load_dotenv
from agent.tools.tool_demo4 import calculate4
from agent.tools.tool_demo6 import runnable_tool
load_dotenv()
from langchain.agents import create_agent
from agent.my_llm import llm
# 本地私有化部署的大模型
# llm = ChatOpenAI(
#     model='deepseek-flash',
#     temperature=0.8,
#     api_key=SecretStr(os.environ['DASHSCOPE_API_KEY']),
#     base_url="https://api.deepseek.com",
# )
# def get_weather(city: str) -> str:
#     """Get weather for a given city."""
#     return f"今天天气晴朗，在 {city}!"
graph = create_agent(
    model=llm,                      # 原来第一个位置参数 llm
    tools=[calculate4,runnable_tool],
    system_prompt='你是智能助手，尽可能调用工具回答用户的问题' # 原来的 prompt 参数
)
#执行智能体，不需要严格的目录结构
# graph.invoke()
# graph.ainvoke()