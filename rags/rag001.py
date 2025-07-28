from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
import os
from rich import print as rprint
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

loader = PyPDFLoader('../笔记文档.pdf')
pages = loader.load_and_split()

rprint(f'第3页：\n{pages[3]}')

# rprint(pages[3].page_content)


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=100,
    length_function=len,
    add_start_index=True,
)

paragraphs = text_splitter.create_documents([pages[3].page_content])
for page in paragraphs:
    rprint(page)


