import requests
from lxml import html
import csv

with open('../04.数据分析/data/movie.csv', 'w', encoding='utf-8', newline='') as csv_writer:
    csv.DictWriter(csv_writer, fieldnames=['名字', '年份', '上映时间', '类型', '时长', '名句', '简介'])
    csv_writer