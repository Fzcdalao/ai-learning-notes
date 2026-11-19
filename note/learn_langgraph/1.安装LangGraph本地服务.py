#先在命令行中下载：pip install virtualenv
#为什么 LangGraph 要在虚拟环境中运行？
#1、根本原因：Python 的依赖是全局的：Python 默认把所有包装在同一个 site-packages 里，虚拟环境就是**给每个项目一个独立的池子**。
#2.LangGraph 尤其需要：①版本迭代极快，依赖链条长
#                    ②往全局 Python 里一通 `pip install`，时间长了某个工具（比如 pipx 装的 CLI、Anaconda 的 base）会被拖坏，
#                     而且**卸载不干净**—— 你都不知道当初为了哪个项目装的。虚拟环境坏了删文件夹重来即可，零成本。
#创建python虚拟环境，powershell：PS D:\Program Files\python_env> & "D:\Program Files\python-3.14\Scripts\virtualenv.exe" "D:\Program Files\python_env\langGraph_env"
#进入虚拟环境文件夹中的\Scripts中的activate下
#
#安装langgraph CLI
#cmd输入；pip install --upgrade "langgraph-cli[inmem]"
#
#创建langGraph应用：
#  langgraph new langgraph_demo
# 读取 `pyproject.toml` 里的项目信息，安装项目声明的全部依赖，把当前项目注册成一个可导入的包，例如你的项目名是 `agent`
# pip install -e .

