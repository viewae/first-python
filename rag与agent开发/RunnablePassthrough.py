from idlelib.searchengine import search_reverse

from langchain_core.runnables import RunnablePassthrough
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatTongyi

model = ChatTongyi(model="qwen3-max")
prompts = ChatPromptTemplate.from_messages(
    [
        ("system", "请根据以下信息，生成一个关于{topic}的提示词"),
        ("user", "信息：{info}")
    ]
)

vector_store = InMemoryVectorStore(
    embedding=DashScopeEmbeddings(model="text-embedding-v4")
)

vector_store.add_texts(["我要做运动","怎么样减肥","如何提高睡眠质量"])#添加向量数据

info_text = "怎么减肥?"#检索信息

retriever = vector_store.as_retriever(search_kwargs = {"k":2})#检索向量库

def format_func(docs):  #定义函数format，作用是数据格式转化
    if not docs:
        return "无数据"
    formatted_str = "["
    for doc in docs:
        formatted_str += doc.page_content + ", "
    formatted_str += "]"
    return formatted_str

chain = (
    {"info": RunnablePassthrough(), "topic": retriever | format_func} | prompts | model | StrOutputParser()
)

res = chain.invoke(info_text)
print(res)