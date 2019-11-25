from bs4 import BeautifulSoup
import requests
import sqlite3
from time import sleep
import json


class UsersDB:
    name = 'pullAndBear.db'

    _db_connection = None
    _db_cur = None

    def __init__(self):
        self._db_connection = sqlite3.connect(self.name)
        self._db_cur = self._db_connection.cursor()

    def query(self, query):
        self._db_cur.execute(query)
        self._db_connection.commit()
        return

    def fetch(self, query):
        return self._db_cur.execute(query).fetchall()

    def save(self):
        self._db_connection.commit()

    def __del__(self):
        self._db_connection.close()


def addProduct(linkToProduct, price, title, article, images):
    db = UsersDB()
    db.query('INSERT INTO Products(linkToProduct, price, title, article) values(\'%s\', \'%s\', \'%s\', \'%s\')' % (
       linkToProduct, price, title, article))
    prId = db.fetch("Select id from products order by id DESC limit 1")
    for img in images:
        db.query('INSERT INTO Images(linkToImage, productId) values(\'%s\', %d)' % (img, prId[0][0]))



url = "https://sbpullbear.empathybroker.com/sb-pullbear/services/search?%D1%87&q=%D1%84%D1%83%D1%82%D0%B1%D0%BE%D0%BB%D0%BA%D0%B0&lang=ru&store=25009522&catalogue=20309410&warehouse=22109405&start=0&rows=15"

headers = {
    'User-Agent': "User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7"}

html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, "html5lib")  # html5lib
noscript = soup.find_all('noscript')
for url in noscript[-1].find_all('a'):
    ps = url.find_all('p')
    if ps[0].text != '' and not (64 < ord(ps[0].text[0]) < 123):
        href = url.get('href')
        cur_html_obj = requests.get(href, headers=headers).text
        sleep(2)
        obj_soup = BeautifulSoup(cur_html_obj, "html5lib")  # html5lib
        info = obj_soup.find("script", {"type": "application/ld+json"}).text
        left = info.find("{")
        right = info.rfind("}")
        info = info[left:right + 1]
        info = json.loads(info)
        title = info["name"]
        price = info["offers"]["price"] + " " + info["offers"]["priceCurrency"]
        images = []
        img = info["image"]
        img = img[:img.rfind('?')]
        for i in range(1, 11):
            img = img.split("_")
            img[1] = '2'
            img[2] = str(i)
            img = "_".join(img)
            if str(requests.get(img, headers=headers)) == '<Response [200]>':
                sleep(1)
                images.append(img)
            else:
                break
        article = info["mpn"]
        # addProduct(href, price, title, article, images)
        print('[+]')
