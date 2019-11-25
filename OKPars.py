import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': "User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7"}

url = "https://ok.ru/majakinfo"
html = requests.get(url, headers = headers).text
soup = BeautifulSoup(html, "html5lib")

allPosts = soup.findAll("div", {"class": "feed-w"})

print(allPosts)