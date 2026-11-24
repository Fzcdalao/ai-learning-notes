# import os
# from dotenv import load_dotenv
#
# from agent.tools.tool_dome3 import calculate3
# from agent.tools.tool_dome4 import calculate4
#
# load_dotenv()
# from langchain_openai import ChatOpenAI
# from langchain.agents import create_agent
# from pydantic import SecretStr
#
#
# # 本地私有化部署的大模型
# llm = ChatOpenAI(
#     model='deepseek-flash',
#     temperature=0.8,
#     api_key=SecretStr(os.environ['DASHSCOPE_API_KEY']),
#     base_url="https://api.deepseek.com",
# )
#
# # def get_weather(city: str) -> str:
# #     """Get weather for a given city."""
# #     return f"今天天气晴朗，在 {city}!"
#
# graph = create_agent(
#     model=llm,                      # 原来第一个位置参数 llm
#     tools=[calculate4],
#     system_prompt='你是智能助手，尽可能调用工具回答用户的问题' # 原来的 prompt 参数
# )



