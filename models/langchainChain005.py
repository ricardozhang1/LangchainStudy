from langchain_community.utilities import SQLDatabase
from rich import print as rprint
from langchain_openai import ChatOpenAI
from langchain.chains import create_sql_query_chain
from dotenv import load_dotenv
import os

load_dotenv()

# 连接sqlite数据库
# db = SQLDatabase.from_uri("sqlite://demo.db")


# 连接Mysql数据库
db_user = "root"
db_passwd = "root"
db_host = "127.0.0.1"
db_port = "3306"
db_name = "db_cteam"
db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_passwd}@{db_host}:{db_port}/{db_name}")

rprint(f"哪种数据库: {db.dialect}")
rprint(f"获取数据表: {db.get_usable_table_names()}")


# 执行查询
# res = db.run('SELECT count(*) FROM c_team')
# rprint(f"查询结果: {res}")


# 初始化大模型
llm = ChatOpenAI(
    base_url=os.getenv('OPENAI_API_BASE'),
    api_key=os.getenv('OPENROUTER_API_KEY'),
    model=os.getenv('OPENAI_MODEL')
)

chain = create_sql_query_chain(llm=llm, db=db)

# response = chain.invoke({'question': '查询一共有多少条数据？'})

# 
# 使用限制的表
response = chain.invoke({'question': '查询一共有多少条数据？', 'table_names_to_use':['c_team']})

rprint(response)
