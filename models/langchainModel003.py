# 导入LangChain中的OpenAI模型接口

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain.prompts import PromptTemplate
from rich import print as rprint

load_dotenv()

# 创建模型实例
model = ChatOpenAI(
    base_url=os.getenv('OPENAI_API_BASE'),
    api_key=os.getenv('OPENROUTER_API_KEY'),
    model=os.getenv('OPENAI_MODEL')
)

prompts = PromptTemplate(
    input_variables=['text'],
    template="你是一名优秀的程序员。\n对于信息{text}进行简短的描述。"
)

# 输入提示
input = prompts.format(text='大模型 LangChain')

# 得到模型的输出
output = model.invoke(input=input)


# 打印输出内容
rprint(output)




