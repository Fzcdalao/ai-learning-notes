from langchain_core.tools import tool
from pydantic import BaseModel, Field
"""
第一种定义工具参数的方式
"""

#定义了一个数据模型类
class CalculateArgs(BaseModel):
    a:float =Field(description="第一个需要输入数字")
    b:float = Field(description="第二个需要输入数字")
    operator: str = Field(description="运算类型只能是：add、subtract、multiply、divide中的任意一个")


#return_direct=True #设置return_direct为true
@tool('calculate', args_schema=CalculateArgs)
def calculate2(a:float,b:float,operator:str) -> float:
    """这是一个工具函数:用来计算两个数字的运算结果"""
    print(f"调用calculate工具,第一个数字：{a},第二个数字:{b},运算类型：{operator}")

    reselt = 0.0
    match operator:
        case "add":
            reselt = a + b
        case "subtract":
            reselt = a - b
        case "multiply":
            reselt = a * b
        case "divide":
            if b != 0:
                reselt = a / b
            else:
                raise ValueError("除数不能为0")
    return reselt

print(calculate2.name)
print(calculate2.description)
print(calculate2.args)
print(calculate2.args_schema.model_json_schema())
print(calculate2.return_direct)