from typing import Annotated
from langchain_core.tools import tool

"""
第三种定义工具参数的方式
谷歌风格的注释，这种比较推荐
"""


#return_direct=True #设置return_direct为true
@tool('calculate', parse_docstring=True) #告诉解析器用谷歌风格的注释解析参数
def calculate4(
        a:float,
        b:float,
        operator:str) -> float:
    """这是一个工具函数:用来计算两个数字的运算结果

    Args:
        a: 第一个需要输入数字
        b: 第二个需要输入数字
        operator: 运算类型只能是：add、subtract、multiply、divide中的任意一个
    """
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

# print(calculate4.name)
# print(calculate4.description)
# print(calculate4.args)
# print(calculate4.args_schema.model_json_schema())
# print(calculate4.return_direct)
#
# s1 = calculate4.invoke({'a':40,'b':2,'operator':'divide'})
# print(s1)

