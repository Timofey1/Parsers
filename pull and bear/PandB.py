# coding=utf-8
import requests
import json

query = 'толстовка'  # input()
url = ["https://sbpullbear.empathybroker.com/sb-pullbear/services/search?%D1%87&q=",query, "&lang=ru&store=25009522&catalogue=20309410&warehouse=22109405&start=0&rows=3"]
url = ''.join(url)

headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
    "Host": "sbpullbear.empathybroker.com:443",
"Proxy-connection": "keep-alive"}

j = None
html = requests.get(url, headers=headers).text
html = json.loads(html)
numof = html['content']['numFound']
url = url.split("rows=")[0]
url = [url, str(numof)]
url = "rows=".join(url)
html = requests.get(url, headers=headers).text
html = json.loads(html)

for i in range(numof):
    infa = html['content']['docs'][i]
    img_infa = infa['img']  # https://static.pullandbear.net/2/photos/2017/V/0/2/p/9244/505/506/9244505506_2_1_2.jpg?t=1480964602726
    imgurl = img_infa['url']
    imgtimestamp = img_infa['timestamp']

    name = infa['name']
    id = infa['id']
    reference = infa['reference']
    price = infa['minPrice']
    mas = []
    for j in range(1, 7):
        imgarr = ["https://static.pullandbear.net/2/photos", imgurl, '_2_', str(j), '_2.jpg?t=', imgtimestamp]
        img = ''.join(imgarr)
        mas.append(img)
    jsn = {i: {"name": name, "id": id, "reference": reference, "price": price, "img": mas}}