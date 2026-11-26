from fastmcp import FastMCP

server = FastMCP(name='MyMCP',instructions='python代码实现的MCP服务器')
#工具
@server.tool(name='say_hello')
def say_hello(username:str)->str:
    """给指定的用户打招呼"""
    return f'Hello {username}'
#提示词
@server.prompt(name='ask_about_topic')
def ask_about_topic(topic:str)->str:
    """生成请求解释特定主题的用户消息模板"""
    return f'能否请您解释一下 {topic}这个概念'
#资源
@server.resource("resources://config")
def get_config()->dict:
    """以JSON个数返回应用配置"""
    return {
        "theme":"dark",
        "version":"1.2.0",
        "features":["tools","resources"],
    }