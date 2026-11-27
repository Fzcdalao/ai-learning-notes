#MCP的认证和安全#
"""
介绍
FastMCP 的 Bearer Token Authentication 认证机制基于 JWT (JSON Web Token) 标准实现，是一种无状态的、基于声明的安全验证体系。
认证验证流程
当请求到达服务端时，按以下顺序验证：
•存在性检查：确认请求头包含 Authorization: Bearer <token>
•结构验证：检查JWT格式是否符合规范
•签名验证：使用配置的公钥验证签名有效性
•声明校验：
    ￮ iss 必须匹配 BearerAuthProvider 配置的签发方
    ￮ aud 必须包含服务端指定的受众
    ￮ exp 必须未过期
•权限检查：Token中的 scopes 需满足工具要求的权限
这个token 可以 设置有效期
"""
#按照以下5个步骤去做就行
"""
1.生成 RSA 密钥对
    详细说明： 
        •生成一对 RSA 密钥（公钥和私钥）
        •公钥(public_key) 用于验证 Token 签名
        •私钥(private_key)用于签发 Token
         -- key_pair = RSAKeyPair.generate() --
    
2.配置 Bearer 认证提供方
    auth = BearerAuthProvider(
        public_key=key_pair.public_key,     # 公钥用于校验签名
        issuer="http://localhost",           # 令牌签发方标识
        audience="my-dev-server",            # 目标服务标识
    )
3.生成token
    token = key_pair.create_token(
        subject="dev-user",
        issuer="http://localhost",
        audience="my-dev-server",
        scopes=["read", "write"]  # token中包含的数据
        expires_in_seconds=3600  # 1小时后过期
    )
4.客户端Agent传入token
5.服务器验证和获取Token
    get_access_token()
        ￮ 作用：从当前请求中提取并解码 JWT
        ￮ 返回：AccessToken 对象，包含以下主要属性：
    class AccessToken:
        client_id: str    # 对应JWT的'sub'(subject)声明
        scopes: List[str] # 对应JWT的'scopes'声明
        issuer: str       # 对应JWT的'iss'声明
        token: str      # 对应JWT的Token字符串
        expires_at: int    # 对应JWT的'exp'声明
"""
