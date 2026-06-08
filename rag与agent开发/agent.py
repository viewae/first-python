from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.tools import tool
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate

# 定义工具函数
@tool
def add_numbers(a: int, b: int) -> int:
    """将两个数字相加"""
    return a + b

@tool
def multiply_numbers(a: int, b: int) -> int:
    """将两个数字相乘"""
    return a * b

@tool
def get_weather(city: str) -> str:
    """获取指定城市的天气信息（模拟）"""
    weather_data = {
        "北京": "晴天，温度25°C",
        "上海": "多云，温度28°C",
        "广州": "雨天，温度30°C",
        "深圳": "晴天，温度32°C"
    }
    return weather_data.get(city, f"抱歉，我没有{city}的天气信息")

# 创建工具列表
tools = [add_numbers, multiply_numbers, get_weather]

# 初始化模型
model = ChatTongyi(model="qwen-turbo", streaming=False)

# 创建提示模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个智能助手，可以使用工具来帮助用户解决问题。"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# 创建Agent
agent = create_tool_calling_agent(model, tools, prompt)

# 创建Agent执行器
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

if __name__ == "__main__":
    # 测试1: 使用计算工具
    print("=== 测试1: 数学计算 ===")
    response = agent_executor.invoke({"input": "请计算 25 加 37 等于多少？"})
    print(f"结果: {response['output']}\n")
    
    # 测试2: 使用乘法工具
    print("=== 测试2: 乘法计算 ===")
    response = agent_executor.invoke({"input": "15 乘以 8 是多少？"})
    print(f"结果: {response['output']}\n")
    
    # 测试3: 使用天气查询工具
    print("=== 测试3: 天气查询 ===")
    response = agent_executor.invoke({"input": "北京的天气怎么样？"})
    print(f"结果: {response['output']}\n")
    
    # 测试4: 简单对话（不使用工具）
    print("=== 测试4: 简单对话 ===")
    response = agent_executor.invoke({"input": "你好，请介绍一下你自己"})
    print(f"结果: {response['output']}")