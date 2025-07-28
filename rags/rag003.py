from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
import os
from rich import print as rprint
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

loader = PyPDFLoader('../笔记文档.pdf')
pages = loader.load_and_split()

# rprint(f'第3页：\n{pages[3]}')

# rprint(pages[3].page_content)


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=100,
    length_function=len,
    add_start_index=True,
)

# 文档切分
paragraphs = []
for page in pages:
    paragraphs.extend(text_splitter.create_documents([page.page_content]))
    
# rprint(paragraphs)

# 文档向量化，向量数据库存储
db = Chroma.from_documents(paragraphs, OpenAIEmbeddings(
    base_url=os.getenv('EMBEDDING_API_BASE'),
    api_key=os.getenv('EMBEDDING_API_KEY'),
    model=os.getenv('EMBEDDING_MODEL')
))

# 生成检索器
retriever = db.as_retriever(
    # search_type='similarity_score_threshold',
    # search_kwargs={'score_threshold': 0.5}
)


query = 'LoRA微调'
docs = retriever.invoke(query)

rprint(docs)






