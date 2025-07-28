# 导入Langchain中的提示模版
from langchain.prompts import PromptTemplate
from rich import print as rprint


prompts = PromptTemplate(
    input_variables=['text'],
    template="你是一名优秀的程序员。\n对于信息{text}进行简短的描述。"
)

# 打印LangChain提示模版
rprint(prompts)

rprint(prompts.format(text='langchain'))