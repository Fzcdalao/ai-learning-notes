# 放在 src/agent/my_llm.py（和 graph.py 同目录）
import os
from pathlib import Path
from dotenv import load_dotenv
# 显式指定 .env 路径：默认 load_dotenv() 依赖当前工作目录，cwd 不在项目根时读不到
load_dotenv(Path(__file__).resolve().parents[2] / ".env")

from langchain_openai import ChatOpenAI
from pydantic import SecretStr

llm = ChatOpenAI(
    model=os.getenv("LLM_MODEL", "deepseek-flash"),
    temperature=0.8,
    api_key=SecretStr(os.environ["DASHSCOPE_API_KEY"]),
    base_url=os.getenv("LLM_BASE_URL", "https://api.deepseek.com"),
)

if __name__ == "__main__":
    print(llm.invoke("你好").content)
