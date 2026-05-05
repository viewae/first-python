import requests
from lxml import html
import csv
import re

BASE_URL = "https://www.themoviedb.org"
NEED_URL = "https://www.themoviedb.org/movie/top-rated"#第一页
NEXT_URL = "https://www.themoviedb.org/discover/movie/items"#下一页

#获取电影信息
def get_movie_year(movie_year):
    if not movie_year:
        return None
    year = movie_year[0].strip()
    year = year.replace("(").replace(")").strip()
    return year


def get_movie_start(movie_start):
    if not movie_start:
        return None
    start_text = movie_start[0].strip()
    match = re.search(r"\d{4}-\d{2}-\d{2}", start_text)
    return match.group() if match else None


def get_movie_info(movie_url):
    response = requests.get(movie_url,timeout=60)

    print(f"发送请求{movie_url},获取电影信息...")

    document = html.fromstring(response.text)
    movie_name = document.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()")#名字
    movie_year = document.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()")#年份
    movie_start = document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='release']/text()")#上映时间
    movie_type = document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='genres']/a/text()")# 类型
    movie_time = document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='runtime']/text()")# 时长
    movie_jianjie = document.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")#简介
    movie_signal =document.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[1]/text()")#名句
    #构建字典
    movie_info = {
        "名字":movie_name[0].strip() if movie_name else None,
        "年份":get_movie_year(movie_year),
        "上映时间":get_movie_start(movie_start),
        "类型":",".join(movie_type) if movie_type else None,
        "时长":movie_time[0].strip() if movie_time else None,
        "名句": movie_signal[0].strip() if movie_signal else '',
        "简介":movie_jianjie[0].strip() if movie_jianjie else '',
    }
    return movie_info

#保存数据
def save_all_movie(all_movie):
    with open('../04.数据分析/data/movie.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["名字", "年份", "上映时间", "类型", "时长", "名句", "简介"]) #type
        writer.writeheader()
        writer.writerows(all_movie)


#主函数

def main():

    all_movie = []#空值

    for page in range(1, 6):   #  循环
        if page > 1:
           response = requests.post(NEXT_URL,
                                   data=f"air_date.gte=&air_date.lte=&certification=&certification_country=CN&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2026-09-30&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=CN&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400",
                                   timeout=60)
        # 解析网页
        else:
           response = requests.get(NEED_URL, timeout=60)

        print("正在解析高分电影网页中...")

        document = html.fromstring(response.text)

        movie_list = document.xpath(f"//*[@id='page_{page}']/div[@class='card style_1']")

        # 遍历网站，获取电影信息
        for movie in movie_list:
            # 获取电影链接
            tare = movie.xpath(".//div/a/@href")
            # 遍历
            if tare:
                movie_url = BASE_URL + tare[0]
                # 调用get_movie_info函数
                movie_info = get_movie_info(movie_url)
                # 添加信息
                all_movie.append(movie_info)




    #保存数据
    print("保存数据中到csv中...")
    save_all_movie(all_movie)





if __name__ == '__main__':
    main()
    



