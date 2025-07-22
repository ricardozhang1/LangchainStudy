from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from rich import print as rprint

load_dotenv()

llm = ChatOpenAI(
    base_url=os.getenv('OPENAI_API_BASE'),
    api_key=os.getenv('OPENROUTER_API_KEY'),
    model=os.getenv('OPENAI_MODEL')
)

response = llm.invoke("什么是大模型？你的版本是什么版本？")
rprint(response)
rprint(response.content)

