# chat 提示词模版

from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
import os
from rich import print as rprint
from langchain_openai import ChatOpenAI

load_dotenv()


template = "你是一个翻译专家，擅长将{input_language}语言翻译成{output_language}语言。"
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ('system', template),
    ('human', human_template)
])


# rprint(chat_prompt)


# 创建模型实例
model = ChatOpenAI(
    base_url=os.getenv('OPENAI_API_BASE'),
    api_key=os.getenv('OPENROUTER_API_KEY'),
    model=os.getenv('OPENAI_MODEL')
)

# 输入提示
msgs = chat_prompt.format(input_language='英语', output_language='中文', text='i love Large Language Model.')
rprint(msgs)

# 得到模型输出
output = model.invoke(msgs)

# 打印输出内容
rprint(output)






