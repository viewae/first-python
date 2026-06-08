import os
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
import config_data as config
import hashlib
from datetime import datetime
from langchain_text_splitters import RecursiveCharacterTextSplitter

def check_md5(md5_str:str):
    if not os.path.exists(config.md5_path):
        open(config.md5_path, 'w', encoding='utf-8').close()
        return False
    else:
        for line in open(config.md5_path, 'r', encoding='utf-8').readlines():
            line = line.strip()
            if line == md5_str:
                return True
        return False

def save_md5(md5_str):
    with open(config.md5_path, 'a', encoding='utf-8') as f:
        f.write(md5_str + '\n')

def get_string_md5(input_str:str, encoding='utf-8'):
    str_bytes = input_str.encode(encoding=encoding)
    md5_obj = hashlib.md5()
    md5_obj.update(str_bytes)  # type: ignore[arg-type]
    md5_hex = md5_obj.hexdigest()
    return md5_hex


class knowledge(object):
    def __init__(self):

        os.makedirs(config.persist_directory, exist_ok=True)

        self.knowledge_base = {}

        self.chroma = Chroma(
            collection_name = config.collection_name,
            persist_directory = config.persist_directory,
            embedding_function = DashScopeEmbeddings(model = "text-embedding-v4"),

        )
        self.spliter = RecursiveCharacterTextSplitter(
            chunk_size = config.chunk_size,
            chunk_overlap = config.chunk_overlap,
            separators=config.separators,
            length_function = len,
        )

    def upload_by_str(self,data,filename):
        md5_hex = get_string_md5(data)  # 获取md5数据
        if check_md5(md5_hex):
            print("数据已存在")
        if len(data) > config.max_split_cahr_number: # 判断数据是否大于最大分词数
           text_splits = self.spliter.split_text(data) # 分词
        else :
            text_splits = [data] #不用分词

        metadata = {
            "filename": filename,
            "md5": md5_hex,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        self.chroma.add_texts(
            text_splits,
            metadata=[metadata for _ in text_splits],
        )

        save_md5(md5_hex)
        return "上传成功"

if __name__ == "__main__":
    service = knowledge()
    a = service.upload_by_str("今天天气不错", "test.txt")
    print(a)