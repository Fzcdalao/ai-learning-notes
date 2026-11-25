from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool


@tool
def get_user_by_name(config: RunnableConfig) ->str:
   """获取用户的所有信息"""
   user_name = config['configurable'].get('user_name', 'zs')
   print(f"调用工具，传入的用户名是：{user_name}")
   return {'user_name': user_name,'sex':'男','age':18}
