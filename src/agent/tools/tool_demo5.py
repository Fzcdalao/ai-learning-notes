
"""
通过StructuredTool.from_function创建工具
"""
from langchain_core.tools import StructuredTool


def calculate5(
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

async def calculate6(
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
#得到工具
calculater = StructuredTool.from_function(
    func=calculate5,
    name="calculater",
    description="工具函数,计算两个数字的运算结果",
    return_direct=False,
    coroutine=calculate6
)
print(calculater.description)


