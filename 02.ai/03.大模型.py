import streamlit as st
import os
import json
from datetime import datetime
from openai import OpenAI


st.set_page_config(
    page_title="02.ai 智能伴侣",
    page_icon="👾",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)
st.title("02.ai 智能伴侣")


# 会话管理相关函数
def save_current_session():
    """保存当前会话"""
    if "messages" in st.session_state and st.session_state.messages:
        session_name = f"会话 {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        sessions = get_all_sessions()
        sessions[session_name] = st.session_state.messages.copy()
        save_sessions_to_file(sessions)
        return session_name
    return None

def get_all_sessions():
    """获取所有保存的会话"""
    try:
        with open('resources/sessions.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_sessions_to_file(sessions):
    """保存会话到文件，新建一个json文件"""
    with open('resources/sessions.json', 'w', encoding='utf-8') as f:
        json.dump(sessions, f, ensure_ascii=False, indent=2)

def load_session(session_name):
    """加载指定会话"""
    sessions = get_all_sessions()
    if session_name in sessions:
        st.session_state.messages = sessions[session_name]


# 添加侧边栏功能
with st.sidebar:
    st.header("✨ 功能面板")
    
    # 功能1: 会话管理
    st.subheader("📌 会话管理")
    
    # 新建会话按钮
    if st.button("🆕 新建会话",width="stretch"):
        st.session_state.messages = []
        st.rerun()
    
    # 保存当前会话
    if st.button("💾 保存当前会话",width="stretch"):
        session_name = save_current_session()
        if session_name:
            st.success(f"已保存为: {session_name}")
        else:
            st.info("没有内容需要保存")
    st.divider()
    
    # 历史会话列表
    st.subheader("📜 历史会话")
    sessions = get_all_sessions()
    if sessions:
        sorted_session_names = sorted(sessions.keys(), reverse=True)
        selected_session = st.selectbox(
            "选择历史会话", 
            sorted_session_names,
            format_func=lambda x: x
        )
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📤 加载"):
                load_session(selected_session)
        with col2:
            if st.button("🗑️ 删除"):
                if selected_session in sessions:
                    del sessions[selected_session]
                    save_sessions_to_file(sessions)
                    st.rerun()
    else:
        st.info("暂无历史会话")

    st.divider()#分隔符

    # 功能2: 使用建议
    st.subheader("使用建议")
    theme = st.radio("选择体验模式", ["日常交流", "浪漫时刻"], help="选择不同的交流氛围")
    if theme == "浪漫时刻":
        st.markdown("💫 建议开启柔和的灯光，享受温馨的对话时光")

    st.divider()#分隔符

    # 功能3: AI 设置
    st.subheader("AI 设置")
    temperature = st.slider("回答多样性", 0.1, 1.0, 0.7, help="值越高回答越有创意和随机性")
    max_tokens = st.slider("最大回复长度", 100, 2000, 1000, help="控制AI单次回复的最大字数")


# 创建OpenAI客户端
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

#=提示词
my_prompt = "你是我的女朋友，名叫涵涵。请用温柔的语言回答用户的问题。"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

#提问问题
prompt = st.chat_input("你要问的问题是")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    print("调用模型，并返回结果", prompt)

#ai回答
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": my_prompt},
            *st.session_state.messages
        ],
        stream=True,
        temperature=temperature,
        max_tokens=max_tokens
    )

    # 创建一个空的占位符来显示AI的回复
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # 流式接收并显示响应
        for chunk in response:
            assistant_content = chunk.choices[0].delta.content
            if assistant_content:
                full_response += assistant_content
                # 更新占位符内容，实现流式显示效果
                message_placeholder.markdown(full_response + "▌")
        
        # 最终移除光标
        message_placeholder.markdown(full_response)
    
    # 将完整回复保存到会话状态
    st.session_state.messages.append({"role": "assistant", "content": full_response})
