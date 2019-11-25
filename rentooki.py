import requests
from bs4 import BeautifulSoup

url = "http://rentooki.ru/moscow/1flat/?page=1"
allHrefs = []
html = requests.get(url).text
soup = BeautifulSoup(html, "html5lib")
flats = soup.findAll("div", {"class": "list-group-item"})
for flat in flats:
    href = flat.find("div", {"class": "media-left"})
    href = href.find("a").get("href")
    allHrefs.append(href)
print(allHrefs)