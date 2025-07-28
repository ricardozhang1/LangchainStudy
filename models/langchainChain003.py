from langchain_openai import ChatOpenAI
from langchain.chains.llm import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
import bs4
from rich import print as rprint
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain

load_dotenv()

# 创建提示模版
prompt = ChatPromptTemplate.from_messages([
    ('system', '根据提供的上下文：{context}\n\n回答问题：{input}')
])

# 创建实例
model = ChatOpenAI(
    base_url=os.getenv('OPENAI_API_BASE'),
    api_key=os.getenv('OPENROUTER_API_KEY'),
    model=os.getenv('OPENAI_MODEL')
)

# 构建链 这个链文档作为输入，并使用之前定义的提示词模版和初始化大模型来生成答案
chain = create_stuff_documents_chain(model, prompt)

# 加载文档
loader = WebBaseLoader(
    web_path='https://www.gov.cn/xinwen/2020-06/01/content_5516649.htm',
    header_template={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'},
    bs_kwargs=dict(parse_only=bs4.SoupStrainer(id='UCAP-CONTENT'))
)

docs = loader.load()

# 分割文档
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=50)
documents = text_splitter.split_documents(documents=docs)

# rprint(len(documents))


# 执行链 检索
res = chain.invoke({'input': '什么是民事法律行为？', 'context': documents[:5]})

rprint(res)


