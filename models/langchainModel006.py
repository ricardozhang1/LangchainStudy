# 使用少量模版实现Chat
from langchain.prompts import PromptTemplate
from rich import print as rprint
from langchain.prompts import FewShotPromptTemplate
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()

examples = [
    {'input': '2+2', 'output': '4', 'description': '加法运算'},
    {'input': '5-2', 'output': '3', 'description': '减法运算'},
]

# 创建提示词模版，配置一个提示词模版，将一个示例格式化为字符串
prompt_template = "算式：{input} 值：{output} 使用：{description}"

# 这是一个提示词模版，用于设置每个示例的格式
prompt_sample = PromptTemplate.from_template(prompt_template)


# 创建一个FewShotPromptTemplate对象
prompts = FewShotPromptTemplate(
    examples=examples,
    example_prompt=prompt_sample,
    suffix="你是一个优秀的计算专家， 算式：{input}  使用：{oudescriptiontput}",
    input_variables=['input', 'oudescriptiontput']
)

llm = ChatOpenAI(
    base_url=os.getenv('OPENAI_API_BASE'),
    api_key=os.getenv('OPENROUTER_API_KEY'),
    model=os.getenv('OPENAI_MODEL')
)


response = llm.invoke(prompts.format(input='2*5', oudescriptiontput='乘法运算'))
rprint(response)

# AIMessage(
#     content='算式：2*5  \n值：10  \n使用：乘法运算',
#     additional_kwargs={'refusal': None},
#     response_metadata={
#         'token_usage': {'completion_tokens': 18, 'prompt_tokens': 62, 'total_tokens': 80, 'completion_tokens_details': None, 'prompt_tokens_details': None},
#         'model_name': 'qwen/qwen3-235b-a22b-07-25',
#         'system_fingerprint': None,
#         'finish_reason': 'stop',
#         'logprobs': None
#     },
#     id='run--84edb7a7-b93a-4aee-819c-b5fe8229e314-0',
#     usage_metadata={'input_tokens': 62, 'output_tokens': 18, 'total_tokens': 80, 'input_token_details': {}, 'output_token_details': {}}
# )


