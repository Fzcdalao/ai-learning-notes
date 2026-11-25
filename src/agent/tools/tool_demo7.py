from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field


class Search_args(BaseModel):
    topic: str = Field(description="需要进行网络搜索的信息")


#网络搜索的工具
class MySearchTool(BaseTool):
    #工具名
    name = 'Search_Tool'
    description = '搜索互联上公开的内容的工具'
    return_direct = False
    args_schema = Search_args
    #def run(self, query) -> str:
