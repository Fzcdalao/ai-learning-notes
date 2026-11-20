#不使用工程自带的graph.py，从网上找了个好用的：
#下载openai的langchain包：pip install langchain-openai
#`create_react_agent` 是旧版写法（来自 `langgraph.prebuilt`）。LangChain 1.x 把它整合进了 `langchain.agents`，官方推荐改用新的 `create_agent`。旧写法目前一般还能跑，但已标记废弃，建议直接换成新 API。
#启动langgraph服务器： langgraph dev
#langgraph.json 是langgraph的配置文件
#启动前缺少了colorama包 ：python -m pip install colorama
#启动前要注意：UnicodeDecodeError: 'gbk' codec can't decode byte 0x94 in position 1660: illegal multibyte sequence
#  Windows 默认用 GBK 读文件，撞上了 UTF-8 中文
#强制 Python 用 UTF-8 模式：$env:PYTHONUTF8 = "1"
#把它设成用户级环境变量，以后所有终端都生效：setx PYTHONUTF8 1
#
"""
启动后
- 🚀 API: http://127.0.0.1:2024   ： 这个是给前端提供的对外开放的API接口
- 🎨 Studio UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024 ： 这个是langgraph自动生成的web页面
- 📚 API Docs: http://127.0.0.1:2024/docs  ： 这个是智能体的接口文档
"""
