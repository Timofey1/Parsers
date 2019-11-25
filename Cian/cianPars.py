import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
}

url = "https://www.cian.ru/cat.php?currency=2&deal_type=rent&engine_version=2&maxprice=50000&offer_type=flat&region=1&room1=1&type=4"
hrefs = []
html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, "html5lib")
infa = soup.find('div', {"class": "serp-list"})
alldivs = infa.findAll("div", {"class": "serp-item_not-inited"})
for d in alldivs:
    href = d.get("href")
    hrefs.append(href)


