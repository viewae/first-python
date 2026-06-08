# 1. 导入所需库
import os
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts.charts import Pie, Bar, Line, Scatter
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# -------------------------- 全局设置：解决中文乱码 --------------------------
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heidi TC"]
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题

# 设置输出目录
OUTPUT_DIR = "data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------- 2. 数据加载与清洗（核心） --------------------------
# 手动构建数据集（和你提供的csv完全一致）
data = [
    [1, "肖申克的救赎", 9.7, 3037887, 1994, "美国", "剧情", "弗兰克·德拉邦特"],
    [2, "霸王别姬", 9.6, 2245306, 1993, "中国大陆", "剧情", "陈凯歌"],
    [3, "阿甘正传", 9.5, 2263516, 1994, "美国", "剧情/喜剧", "罗伯特·泽米吉斯"],
    [4, "泰坦尼克号", 9.5, 2302886, 1997, "美国", "剧情/灾难", "詹姆斯·卡梅隆"],
    [5, "千与千寻", 9.4, 2351770, 2001, "日本", "动画/奇幻/冒险", "宫崎骏"],
    [6, "这个杀手不太冷", 9.4, 2389070, 1994, "法国", "剧情/动作/犯罪", "吕克·贝松"],
    [7, "美丽人生", 9.5, 1385004, 1997, "意大利", "剧情/喜剧/战争", "罗伯托·贝尼尼"],
    [8, "星际穿越", 9.4, 1969495, 2014, "美国", "剧情/科幻/冒险", "克里斯托弗·诺兰"],
    [9, "盗梦空间", 9.4, 2165729, 2010, "美国", "剧情/科幻/悬疑", "克里斯托弗·诺兰"],
    [10, "楚门的世界", 9.4, 1823060, 1998, "美国", "剧情/喜剧", "彼得·威尔"],
    [11, "辛德勒的名单", 9.5, 1171642, 1993, "美国", "剧情/历史/战争", "史蒂文·斯皮尔伯格"],
    [12, "忠犬八公的故事", 9.4, 1451811, 2009, "美国", "剧情", "莱塞·霍尔斯道姆"],
    [13, "海上钢琴师", 9.3, 1439596, 1998, "意大利", "剧情/音乐", "朱塞佩·托纳多雷"],
    [14, "三傻大闹宝莱坞", 9.2, 1652434, 2009, "印度", "剧情/喜剧", "拉库马·希拉尼"],
    [15, "机器人总动员", 9.3, 1450000, 2008, "美国", "动画/科幻/冒险", "安德鲁·斯坦顿"],
    [16, "放牛班的春天", 9.3, 1440000, 2004, "法国", "剧情/音乐/儿童", "克里斯托夫·巴拉蒂"],
    [17, "触不可及", 9.3, 1258000, 2011, "法国", "剧情/喜剧", "奥利维耶·纳卡什"],
    [18, "熔炉", 9.3, 1015000, 2011, "韩国", "剧情/犯罪", "黄东赫"],
    [19, "指环王3：王者无敌", 9.3, 887000, 2003, "美国", "剧情/奇幻/冒险", "彼得·杰克逊"],
    [20, "素媛", 9.3, 759000, 2013, "韩国", "剧情/犯罪", "李俊益"],
    [21, "教父", 9.3, 1325689, 1972, "美国", "剧情/犯罪", "弗朗西斯·福特·科波拉"],
    [22, "龙猫", 9.2, 1689745, 1988, "日本", "动画/奇幻/冒险", "宫崎骏"],
    [23, "乱世佳人", 9.3, 968542, 1939, "美国", "剧情/历史", "维克多·弗莱明"],
    [24, "当幸福来敲门", 9.1, 1865248, 2006, "美国", "剧情/传记", "加布里尔·穆奇诺"],
    [25, "哈尔的移动城堡", 9.1, 1725689, 2004, "日本", "动画/奇幻/冒险", "宫崎骏"],
    [26, "让子弹飞", 9.0, 1986542, 2010, "中国大陆", "剧情/喜剧/动作", "姜文"],
    [27, "怦然心动", 9.1, 2015689, 2010, "美国", "剧情", "罗伯·莱纳"],
    [28, "末代皇帝", 9.3, 1025689, 1987, "英国/意大利/中国大陆", "剧情/传记/历史", "贝纳尔多·贝托鲁奇"],
    [29, "寻梦环游记", 9.1, 1896542, 2017, "美国", "动画/音乐/奇幻", "李·昂克里奇"],
    [30, "哈利·波特与魔法石", 9.1, 1756892, 2001, "美国", "奇幻/冒险", "克里斯·哥伦布"],
    [31, "大话西游之大圣娶亲", 9.2, 1865987, 1995, "中国香港", "剧情/喜剧", "刘镇伟"],
    [32, "我不是药神", 9.0, 2236598, 2018, "中国大陆", "剧情/喜剧", "文牧野"],
    [33, "指环王1：护戒使者", 9.1, 1125689, 2001, "美国", "奇幻/冒险", "彼得·杰克逊"],
    [34, "死亡诗社", 9.1, 1256987, 1989, "美国", "剧情", "彼得·威尔"],
    [35, "复仇者联盟4：终局之战", 8.5, 2659874, 2019, "美国", "动作/科幻/奇幻", "罗素兄弟"],
    [36, "指环王2：双塔奇兵", 9.0, 986542, 2002, "美国", "剧情/奇幻/冒险", "彼得·杰克逊"],
    [39, "蝙蝠侠：黑暗骑士", 9.2, 1856987, 2008, "美国", "剧情/动作/科幻", "克里斯托弗·诺兰"],
    [40, "阿凡达", 8.8, 2156987, 2009, "美国", "动作/科幻/冒险", "詹姆斯·卡梅隆"],
    [41, "寄生虫", 8.8, 1569874, 2019, "韩国", "剧情/喜剧/悬疑", "奉俊昊"],
    [42, "活着", 9.3, 1456987, 1994, "中国大陆", "剧情/历史", "张艺谋"],
    [43, "闻香识女人", 9.1, 1356987, 1992, "美国", "剧情", "马丁·布莱斯特"],
    [44, "罗马假日", 9.1, 1589654, 1953, "美国", "剧情", "威廉·惠勒"],
    [45, "何以为家", 9.1, 1489654, 2018, "黎巴嫩", "剧情", "娜丁·拉巴基"],
    [46, "飞屋环游记", 9.0, 1689654, 2009, "美国", "动画/剧情/冒险", "鲍勃·彼德森"],
    [47, "大话西游之月光宝盒", 9.0, 1589654, 1995, "中国香港", "剧情/喜剧/奇幻", "刘镇伟"],
    [48, "摔跤吧！爸爸", 9.0, 1789654, 2016, "印度", "剧情/传记/运动", "涅提·蒂瓦里"],
    [49, "少年派的奇幻漂流", 9.1, 1489654, 2012, "美国", "剧情/奇幻/冒险", "李安"],
    [51, "傲慢与偏见", 8.7, 1389654, 2005, "英国", "剧情", "乔·赖特"],
    [52, "美丽心灵", 9.1, 1289654, 2001, "美国", "剧情/传记", "朗·霍华德"],
    [53, "剪刀手爱德华", 8.7, 1689654, 1990, "美国", "剧情/奇幻", "蒂姆·波顿"],
    [54, "疯狂动物城", 9.2, 2089654, 2016, "美国", "动画/喜剧/冒险", "拜伦·霍华德"],
    [55, "穿条纹睡衣的男孩", 9.0, 989654, 2008, "美国", "剧情/战争", "马克·赫尔曼"],
    [56, "菊次郎的夏天", 9.3, 1289654, 1999, "日本", "剧情/喜剧", "北野武"],
    [57, "天使爱美丽", 8.7, 1489654, 2001, "法国", "剧情/喜剧", "让-皮埃尔·热内"],
    [58, "七宗罪", 8.8, 1589654, 1995, "美国", "剧情/悬疑/犯罪", "大卫·芬奇"],
    [59, "忠犬八公物语", 9.2, 889654, 1987, "日本", "剧情", "神山征二郎"],
    [61, "超能陆战队", 8.7, 1589654, 2014, "美国", "动画/喜剧/科幻", "唐·霍尔"],
    [93, "西西里的美丽传说", 8.7, 1489654, 2000, "意大利", "剧情/情色", "托纳多雷"],
    [94, "禁闭岛", 8.8, 1689654, 2010, "美国", "剧情/悬疑/惊悚", "马丁·斯科塞斯"],
    [95, "迷雾", 7.9, 1089654, 2007, "美国", "剧情/科幻/惊悚", "弗兰克·德拉邦特"],
    [96, "心灵捕手", 9.0, 1389654, 1997, "美国", "剧情", "格斯·范·桑特"],
    [98, "岁月神偷", 8.9, 1289654, 2010, "中国香港", "剧情/家庭", "罗启锐"],
    [99, "萤火虫之墓", 9.2, 989654, 1988, "日本", "动画/剧情/战争", "高畑勋"],
    [100, "源代码", 8.5, 1389654, 2011, "美国", "科幻/悬疑/惊悚", "邓肯·琼斯"]
]

# 构建DataFrame
columns = ["rank", "title", "rating", "rate_count", "year", "country", "genre", "director"]
df = pd.DataFrame(data, columns=columns)

# 数据清洗：删除重复电影、重置索引
df = df.drop_duplicates(subset=["title"], keep="first").reset_index(drop=True)


# -------------------------- 第一部分：基础信息可视化（Matplotlib） --------------------------
def part1_base_visual():
    # 创建DataFrame副本，避免修改原始数据
    df_temp = df.copy()
    
    # 1.1 电影评分分布
    plt.figure(figsize=(10, 5))
    rating_bins = [7.5, 8.5, 9.0, 9.5, 10.0]
    rating_labels = ["7.5-8.5", "8.5-9.0", "9.0-9.5", "9.5-10.0"]
    df_temp["rating_bin"] = pd.cut(df_temp["rating"], bins=rating_bins, labels=rating_labels, right=False)
    rating_count = df_temp["rating_bin"].value_counts().sort_index()

    plt.bar(rating_count.index, rating_count.values, color="#4472C4")
    plt.title("电影评分分布", fontsize=14)
    plt.xlabel("评分区间")
    plt.ylabel("电影数量")
    plt.savefig(os.path.join(OUTPUT_DIR, "1_评分分布.png"), dpi=300, bbox_inches="tight")
    plt.show()

    # 1.2 发行年份分布
    plt.figure(figsize=(12, 5))
    year_count = df["year"].value_counts().sort_index()
    plt.plot(year_count.index, year_count.values, marker="o", color="#ED7D31", linewidth=2)
    plt.title("电影发行年份分布", fontsize=14)
    plt.xlabel("年份")
    plt.ylabel("电影数量")
    plt.grid(alpha=0.3)
    plt.savefig(os.path.join(OUTPUT_DIR, "2_年份分布.png"), dpi=300, bbox_inches="tight")
    plt.show()

    # 1.3 制片国家分布
    plt.figure(figsize=(8, 8))
    country_count = df["country"].value_counts().head(6)
    plt.pie(country_count.values, labels=country_count.index, autopct="%.1f%%",
            colors=["#4472C4", "#ED7D31", "#A5A5A5", "#70AD47", "#FFC000", "#5B9BD5"])
    plt.title("主要制片国家/地区占比", fontsize=14)
    plt.savefig(os.path.join(OUTPUT_DIR, "3_国家分布.png"), dpi=300, bbox_inches="tight")
    plt.show()


# -------------------------- 第二部分：类型与导演可视化（Pyecharts） --------------------------
def part2_type_director_visual():
    # 2.1 电影类型分布（拆分复合类型）
    genre_list = []
    for g in df["genre"]:
        genre_list.extend(g.split("/"))
    genre_count = pd.Series(genre_list).value_counts().head(8)

    pie = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
        .add("", list(zip(genre_count.index.tolist(), genre_count.values.tolist())),
             radius=["30%", "70%"])
        .set_global_opts(title_opts=opts.TitleOpts(title="经典电影类型分布"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}部 ({d}%)"))
    )
    pie.render(os.path.join(OUTPUT_DIR, "4_电影类型环形图.html"))  # 生成可交互HTML文件

    # 2.2 高产导演作品数量
    director_count = df["director"].value_counts().head(6)
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
        .add_xaxis(director_count.index.tolist())
        .add_yaxis("作品数量", director_count.values.tolist())
        .set_global_opts(title_opts=opts.TitleOpts(title="高产导演作品数量"),
                         xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=15)))
    )
    bar.render(os.path.join(OUTPUT_DIR, "5_高产导演柱状图.html"))


# -------------------------- 第三部分：热度与综合影响力可视化 --------------------------
def part3_hot_influence_visual():
    # 3.1 评分-热度关联散点图
    scatter = (
        Scatter(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
        .add_xaxis(df["rating"].tolist())
        .add_yaxis("评分人数", df["rate_count"].tolist(), symbol_size=10)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="评分-热度关联"),
            xaxis_opts=opts.AxisOpts(name="评分"),
            yaxis_opts=opts.AxisOpts(name="评分人数（热度）"),
            tooltip_opts=opts.TooltipOpts(formatter="评分：{c[0]}<br/>热度：{c[1]}"))
    )
    scatter.render(os.path.join(OUTPUT_DIR, "6_评分-热度散点图.html"))

    # 3.2 综合影响力TOP10
    df_temp = df.copy()
    df_temp["influence"] = df_temp["rating"] * df_temp["rate_count"] / 10000  # 标准化计算
    top10 = df_temp.sort_values("influence", ascending=False).head(10)

    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
        .add_xaxis(top10["title"].tolist())
        .add_yaxis("综合影响力", top10["influence"].tolist())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="电影综合影响力TOP10"),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)))
    )
    bar.render(os.path.join(OUTPUT_DIR, "7_综合影响力TOP10.html"))


# -------------------------- 一键运行所有可视化 --------------------------
if __name__ == "__main__":
    print("=== 开始生成第一部分：基础信息图表 ===")
    part1_base_visual()
    print("=== 开始生成第二部分：类型与导演交互图表 ===")
    part2_type_director_visual()
    print("=== 开始生成第三部分：热度与影响力图表 ===")
    part3_hot_influence_visual()
    print("=== 所有图表生成完成！ ===")