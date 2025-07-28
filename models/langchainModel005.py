# 少量样例提示模版
from langchain.prompts import PromptTemplate
from rich import print as rprint
from langchain.prompts import FewShotPromptTemplate

examples = [
    {'input': '2+2', 'output': '4', 'description': '加法运算'},
    {'input': '5-2', 'output': '3', 'description': '减法运算'},
]

# 创建提示词模版，配置一个提示词模版，将一个示例格式化为字符串
prompt_template = "算式：{input} 值：{output} 使用：{description}"

# 这是一个提示词模版，用于设置每个示例的格式
prompt_sample = PromptTemplate.from_template(prompt_template)


# rprint(prompt_sample.format_prompt(**examples[1]))

# 创建一个FewShotPromptTemplate对象
prompts = FewShotPromptTemplate(
    examples=examples,
    example_prompt=prompt_sample,
    suffix="你是一个优秀的计算专家， 算式：{input}  值：{output}",
    input_variables=['input', 'output']
)

rprint(prompts.format(input='2*5', output='10'))



