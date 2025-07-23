# 导入Langchain中的提示模版
from langchain.prompts import PromptTemplate
from rich import print as rprint

# 创建原始模版
template = "你是一名优秀的程序员。\n对于信息{text}进行简短的描述。"

# 根据原始模版创建LangChain提示模版
prompts = PromptTemplate.from_template(template=template)

# 打印LangChain提示模版
rprint(prompts)

rprint(prompts.format(text='langchain'))



