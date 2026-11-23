from langchain_core.tools import tool
#return_direct=True #设置return_direct为true
@tool()
def calculate(a:float,b:float,operator:str) -> float:
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

print(calculate.name)
print(calculate.description)
print(calculate.args)
print(calculate.args_schema.model_json_schema())
print(calculate.return_direct)