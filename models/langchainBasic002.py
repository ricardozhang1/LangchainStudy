from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import ChatPromptTemplate
from rich import print as rprint

load_dotenv()


llm = ChatOpenAI(
    base_url=os.getenv('OPENAI_API_BASE'),
    api_key=os.getenv('OPENROUTER_API_KEY'),
    model=os.getenv('OPENAI_MODEL')
)

# 使用提示词模版
prompt = ChatPromptTemplate.from_messages([
    ('system', '你是一个优秀的文档编辑者。'),
    ('user', "{input}") # input是变量
])

chain = prompt | llm
response = chain.invoke({'input': '大模型中的LangChain是什么？'})
rprint(response)
rprint(response.content)



