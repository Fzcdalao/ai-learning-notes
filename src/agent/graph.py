from dotenv import load_dotenv
from langchain_core.messages import AnyMessage
from langchain_core.runnables import RunnableConfig
from langgraph.prebuilt import create_react_agent

from agent.my_state import CustomState
from agent.tools.tool_demo4 import calculate4
from agent.tools.tool_demo6 import runnable_tool
from agent.tools.tool_demo8 import get_user_by_name
from agent.tools.tool_demo9 import get_user_name, greet_user

load_dotenv()
from langchain.agents import create_agent, AgentState
from agent.my_llm import llm
# 本地私有化部署的大模型
# llm = ChatOpenAI(
#     model='deepseek-flash',
#     temperature=0.8,
#     api_key=SecretStr(os.environ['DASHSCOPE_API_KEY']),
#     base_url="https://api.deepseek.com",
# )
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"今天天气晴朗，在 {city}!"

#提示词模板函数---由用户传入内容生成一个动态的系统提示词:
def prompt(state: AgentState,config: RunnableConfig) -> list[AnyMessage]:
    user_name = config['configurable'].get('user_name','zs')
    print(user_name)
    system_message = f'你是一个智能助手，尽可能调用工具回答用户的问题,当前用户名字是:{user_name}'
    return [{'role':'system','content':system_message}]+state['messages']

graph = create_react_agent(
    llm,                      # 原来第一个位置参数 llm
    tools=[calculate4,runnable_tool,get_weather,get_user_name,greet_user],
    prompt=prompt, # 原来的 prompt 参数
    state_schema=CustomState
)
#执行智能体，不需要严格的目录结构
# graph.invoke()
# graph.ainvoke()