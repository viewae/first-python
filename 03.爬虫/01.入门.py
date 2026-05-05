import requests
from lxml import html




response = requests.get(need_url)

document = html.fromstring(response.text)

paixu = document.xpath("//table[@id = 'top20']/thead/tr/th/text()")

print(paixu)

biao_tou = document.xpath("//table[@id = 'top20']/tbody/tr")

for i in biao_tou:
    biao_tou = i.xpath("./td/text()")
    print(biao_tou)


