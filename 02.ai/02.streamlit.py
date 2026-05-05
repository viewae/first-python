import streamlit as st
import pandas as pd
import plotly.express as px

# 设置网页标题和副标题
st.title("我的第一个 Streamlit 网页应用")
st.subheader("这是用纯 Python 开发的交互式网页")

# 添加文本和交互组件
name = st.text_input("请输入你的名字")
age = st.slider("请选择你的年龄", 0, 100, 25)

# 按钮交互
if st.button("提交信息"):
    st.success(f"你好 {name}！你的年龄是 {age} 岁")

# 数据可视化示例
st.subheader("数据可视化展示")
# 生成示例数据
df = pd.DataFrame({
    "月份": ["1月", "2月", "3月", "4月", "5月"],
    "销售额": [120, 200, 150, 300, 280]
})
# 绘制柱状图
fig = px.bar(df, x="月份", y="销售额", title="月度销售额")
st.plotly_chart(fig, use_container_width=True)

# 显示数据表格
st.dataframe(df, use_container_width=True)