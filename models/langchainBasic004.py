# 导入和使用WebBaseLoader
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
import os
import bs4
from rich import print as rprint
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain


load_dotenv()


loader = WebBaseLoader(
    web_path='https://www.gov.cn/xinwen/2020-06/01/content_5516649.htm',
    header_template={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'},
    bs_kwargs=dict(parse_only=bs4.SoupStrainer(id='UCAP-CONTENT'))
)

docs = loader.load()
# rprint(docs)

# 对于嵌入模型，这里使用API调用
embeddings = OpenAIEmbeddings(
    base_url=os.getenv('EMBEDDING_API_BASE'),
    api_key=os.getenv('EMBEDDING_API_KEY'),
    model=os.getenv('EMBEDDING_MODEL'),
    default_headers={"Authorization": f"Bearer {os.getenv('EMBEDDING_API_KEY')}"}
)

# 使用此嵌入模型将文档提取到矢量存储中
# 使用分割器分割文档
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
documents = text_splitter.split_documents(documents=docs)

# for d in documents:
#     rprint(d)

# 向量存储 embeddings 会将documents中的每个文本片段转换为向量，并将这些向量存储在FAISS向量数据库中
vector = FAISS.from_documents(documents=documents, embedding=embeddings)

# 提示词
prompts = ChatPromptTemplate.from_template("""仅根据提供的上下文回答以下问题：<context>{context}</context> Question: {input}""")

llm = ChatOpenAI(
    base_url=os.getenv('OPENAI_API_BASE'),
    api_key=os.getenv('OPENROUTER_API_KEY'),
    model=os.getenv('OPENAI_MODEL')
)

# 创建文档组合链 将文档内容和用户问题组合成一个完整的提示，然后传递给语言模型生成回答
document_chain = create_stuff_documents_chain(llm, prompts)


retriever = vector.as_retriever()
retriever.search_kwargs = {'k': 3}  # 限制为最多检索3个文档

# 创建检索链 该链结合了检索器和文档组合链，实现了从向量数据库中的检索相关文档，并将这些文档与用户问题组合成提示
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# 调用检索链并获取回答
response = retrieval_chain.invoke({
    'input': '建设用地的使用权是什么？'
})
rprint(response['answer'])
