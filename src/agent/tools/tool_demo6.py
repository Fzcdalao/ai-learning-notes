from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import Field, BaseModel
from agent.my_llm import llm

prompt = (
    PromptTemplate.from_template("帮我生成一个简短的，关于{topic}的字幕词。")
    + ",要求: 1、内容搞笑一点"
    + ",2、输出内容采用{language}。"
)

chain = prompt | llm | StrOutputParser()

class ToolArgs(BaseModel):
    topic:str =Field(description="报幕词的主题")
    language:str = Field(description="报幕词采用的语言")

runnable_tool = chain.as_tool(
    name='chain_tool',
    description='这是一个专门呢用来生成报幕词的工具',
    args_schema=ToolArgs,
)

print(runnable_tool.args_schema.model_json_schema())
print(runnable_tool.name)
print(runnable_tool.description)
