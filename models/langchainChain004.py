from langchain.chains import LLMMathChain
from langchain_openai import ChatOpenAI
from langchain_experimental.utilities import PythonREPL
from dotenv import load_dotenv
import os
from rich import print as rprint

load_dotenv()


model = ChatOpenAI(
    base_url=os.getenv('OPENAI_API_BASE'),
    api_key=os.getenv('OPENROUTER_API_KEY'),
    model=os.getenv('OPENAI_MODEL')
)

llm_math = LLMMathChain.from_llm(model, verbose=True)

response = llm_math.invoke("10**3 + 500")

rprint(response)
