from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_experimental.utilities import PythonREPL
from dotenv import load_dotenv
import os
from rich import print as rprint

load_dotenv()

template = """Write some python code to solve the user's promblem.

Return only Python code in Markdown format, e.d.:

```python
...
```

"""

prompt = ChatPromptTemplate.from_messages([('system', template), ('human', '{input}')])

def _sanitize_output(text: str) -> str:
    _, after = text.split('```python')
    return after.split('```')[0]


model = ChatOpenAI(
    base_url=os.getenv('OPENAI_API_BASE'),
    api_key=os.getenv('OPENROUTER_API_KEY'),
    model=os.getenv('OPENAI_MODEL')
)

# PythonRePL().run 就是调用一下 exec 函数执行代码
chain = prompt | model | StrOutputParser() | _sanitize_output | PythonREPL().run
response = chain.invoke({'input': 'what is 2 plus 2?'})

rprint(response)
