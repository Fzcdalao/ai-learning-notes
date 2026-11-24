from typing import Annotated
from langchain_core.tools import tool

"""
第二种定义工具参数的方式
"""


#return_direct=True #设置return_direct为true
@tool('calculate')
def calculate3(
        a:Annotated[float,'第一个需要输入数字'],
        b:Annotated[float,'第二个需要输入数字'],
        operator:Annotated[str,'运算类型只能是：add、subtract、multiply、divide中的任意一个']) -> float:
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

print(calculate3.name)
print(calculate3.description)
print(calculate3.args)
print(calculate3.args_schema.model_json_schema())
print(calculate3.return_direct)

s1 = calculate3.invoke({'a':40,'b':2,'operator':'divide'})
print(s1)