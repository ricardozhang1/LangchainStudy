from langchain_openai import ChatOpenAI
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
from rich import print as rprint

load_dotenv()

# 原始字符串模版
template = "桌上有{number}个苹果，四个桃子和3本书，一共有多少个水果？"

prompt = PromptTemplate.from_template(template)

# 创建实例
model = ChatOpenAI(
    base_url=os.getenv('OPENAI_API_BASE'),
    api_key=os.getenv('OPENROUTER_API_KEY'),
    model=os.getenv('OPENAI_MODEL')
)

# 创建Chain
# chain = prompt | model

# response = chain.invoke({'number': '5'})
# rprint(response)


chain = LLMChain(llm=model, prompt=prompt)
response = chain.predict(number=5)
rprint(response)


# chain = LLMChain(llm=model, prompt=prompt)
# response = chain.batch(number=5)
# rprint(response)