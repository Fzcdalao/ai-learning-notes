from fastmcp import FastMCP
from fastmcp.server.auth.providers.jwt import RSAKeyPair, StaticTokenVerifier, JWTVerifier

#1.生成RSA密钥对
key_pair = RSAKeyPair.generate()
# print(key_pair.public_key)

#2.配置认证的提供方
verifier = JWTVerifier(
    public_key=open("public.pem", encoding="utf-8").read(),  # 注意是 PEM 字符串，不是 key 对象
    issuer="http://www.fzc.com",
    audience="mg-dev-server",
)

#服务器，模拟生成一个token
token = key_pair.create_token(
    subject='dev_user',             #主题
    issuer='http://www.fzc.com',    # 签发方的标识，一般填公司域名
    audience='mg-dev-server',       # 服务商的标识
    scopes=['fzc','invoke_tools'],  #可以存放一些数据和操作还有其他的
    expires_in=3600,                #有效时间
)

print(f'token: {token}')

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