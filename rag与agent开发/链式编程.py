from Demos.win32ts_logoff_disconnected import session
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_core.chat_history import InMemoryChatMessageHistory

model = ChatTongyi(model="qwen3-max")
prompt = PromptTemplate.from_template(
    "根据对话历史回答用户问题，对话历史{chat_history}，用户提问{question}，请回答"
)

str_parser = StrOutputParser()
base_chain = prompt | model | str_parser

store = {}
#创一个新链

def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


new_chain = RunnableWithMessageHistory(
    base_chain,
    get_history,
    input_messages_key="question",
    history_messages_key="chat_history",
)


if __name__ == "__main__":
        pass