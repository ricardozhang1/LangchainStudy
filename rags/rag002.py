from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
from rich import print as rprint

load_dotenv()

embeddings_model = OpenAIEmbeddings(
    base_url=os.getenv('EMBEDDING_API_BASE'),
    api_key=os.getenv('EMBEDDING_API_KEY'),
    model=os.getenv('EMBEDDING_MODEL')
)

embeddings = embeddings_model.embed_documents([
    "Hi there!",
    "Oh, hello!",
    "Ahat's your name?",
    "My friend call me World!",
    "Hello world!"
])

rprint(len(embeddings), len(embeddings[0]))
rprint(embeddings[0][:10])






