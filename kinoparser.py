from bs4 import BeautifulSoup
import requests

url = "http://mar4uk.com/"

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
}

html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, "html5lib")
infa = soup.findAll('article', {"class": "actor-item"})
for row in infa:
    href = row.find("a", {"class": "no-hover"}).get("href")
    html = requests.get(href, headers=headers).text
    soup = BeautifulSoup(html, "html5lib")
    images = soup.find("div", {"class": "galery-rows"})
    img = images.findAll("img")
    imgs = []
    for i in img:
        src = i.get('src')
        imgs.append(src)
    name = soup.find("h1", {"class": "post-title"}).text
    print(name)
    infa = soup.find("div", {"class": "section-content"})
    infa = infa.findAll("span")
    for i in infa:
        text = i.text
        print(text)
    print(imgs)
    print("="*50)
