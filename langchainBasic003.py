# s使用输出解析器
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from rich import print as rprint

# 加载环境变量
load_dotenv()

# 初始化模型
llm = ChatOpenAI(
    base_url=os.getenv('OPENAI_API_BASE'),
    api_key=os.getenv('OPENROUTER_API_KEY'),
    model=os.getenv('OPENAI_MODEL')
)

# 创建提示模版
prompt = ChatPromptTemplate.from_messages([
    ('system', '你是优秀的的技术文档编写者。'),
    ('user', '{input}')
])


# 使用输出解析器
# output_parse = StrOutputParser()
output_parse = JsonOutputParser()


# 将其添加到上一个链中
chain = prompt | llm | output_parse

# 调用它
response = chain.invoke({'input': 'LangChain是什么？问题用question 回答用answer 用json格式回复'})
rprint(response)


