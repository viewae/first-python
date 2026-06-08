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

vector_store.add_texts(["我要做运动","怎么样减肥","如何提高睡眠质量"])

info_text = "怎么减肥?"

#检索向量库
result = vector_store.similarity_search(info_text,2)

reference_text = "["
for doc in result:
    reference_text += doc.page_content
reference_text += "]"

def get_prompt(prompt):
    print(prompt.to_string())
    print("="*20)
    return prompt

chain = prompts | model | StrOutputParser()

res = chain.invoke({"topic": info_text , "info": reference_text})
print(res)