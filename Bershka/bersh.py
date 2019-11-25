# coding=utf-8
import requests
import json

query = "футболка"
url = ["https://sbbershka.empathybroker.com/sb-bershka/services/search?jsonCallback=jsonCallback_1486559467488_4&rows=3&start=0&q=",query ,"&jsonCallback=JSON_CALLBACK&lang=ru&store=45109522&topTrends.rows=10&catalogue=40259536&warehouse=42109504"]
url = ''.join(url)

headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"}

html = requests.get(url, headers=headers).text
html = html[html.find("(")+1: html.rfind(")")]
html = json.loads(html)
numof = html['content']['numFound']
url = url.split("rows=")
url[1] = str(numof) + url[1][url[1].find("&"):]
url = "rows=".join(url)
html = requests.get(url, headers=headers).text
html = html[html.find("(")+1: html.rfind(")")]
html = json.loads(html)

j = None
for i in range(numof):
    infa = html['content']['docs'][i]
    name = infa['name']
    colorId = infa['colorId']
    price = infa['minPrice']
    id = infa['id']
    displayReference = infa['displayReference']
    reference = infa['reference']
    img_infa = infa['img']  # https://static.bershka.net/4/photos2/2017/V/0/1/p/2187/900/800/2187900800_2_1_2.jpg?t=1491580114892
    imgurl = img_infa['url']
    imgtimestamp = img_infa['timestamp']
    mas = []
    for j in range(1, 6):
        imgarr = ["https://static.bershka.net/4/photos2", imgurl, '_2_', str(j), '_2.jpg?t=', imgtimestamp]
        img = ''.join(imgarr)
        mas.append(img)
    jsn = {i: {"name": name, "colorId": colorId, "price": price, "id": id, "displayReference": displayReference, "reference": reference, "img": mas}}

