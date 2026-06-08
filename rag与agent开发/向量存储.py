from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_chroma import Chroma

# vector_store = InMemoryVectorStore(
#     embedding=DashScopeEmbeddings()
# )

vector_store = Chroma(
    collection_name="movie", # 数据库名称
    embedding_function = DashScopeEmbeddings(),  # 嵌入函数
    persist_directory="./chroma_db"   # 持久化目录
)

loader = CSVLoader(
   file_path = "./data.csv",
    encoding = "utf-8",
    source_column="title",
)

documents = loader.load()
#添加
vector_store.add_documents(
    documents=documents,
    ids=["id"+str(i) for i in range(1,len(documents) + 1)]  #type : list[str]
)
#删除
vector_store.delete(["id1","id2"])
#搜索
result =  vector_store.similarity_search(
    query="哪个电影评分最高",
    k=1,
)

print(result)

