import streamlit as st
from rag项目.knowledge_base import knowledge

st.title("知识库更新服务")

uploader_file = st.file_uploader(
    "上传文件",
    type=["txt", "pdf", "csv", "json"],
    accept_multiple_files=True,
)

if "service" not in st.session_state:
    st.session_state["service"] = knowledge()

if uploader_file is not None:
    file_name = uploader_file.name
    file_content = uploader_file.read()
    file_type = uploader_file.type
    file_size = uploader_file.size / 1024

    st.subheader("文件信息")
    st.write(f"文件名: {file_name}|格式：{file_type:.2f} KB")
    uploader_file.getvalue().decode("utf-8")
    st.write(file_content)

    result = st.session_state["service"].upload_by_str(file_content,file_name)
    st.write(result)