from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader,JSONLoader,PyPDFLoader,CSVLoader


text_loader = TextLoader("text.txt") # 加载文本

JSONLoader = JSONLoader("data.json") # 加载json

PyPDFLoader = PyPDFLoader("pdf") # 加载pdf

CSVLoader = CSVLoader("data.csv") # 加载csv

#把数据变成document格式