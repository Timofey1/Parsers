from bs4 import BeautifulSoup
import requests
url = "https://www.pullandbear.com/m/ru/%D0%B4%D0%BB%D1%8F-%D0%BC%D1%83%D0%B6%D1%87%D0%B8%D0%BD/%D0%BE%D0%B4%D0%B5%D0%B6%D0%B4%D0%B0/%D0%BC%D0%B0%D0%B9%D0%BA%D0%B8-c29070.html?isMobile=True"
headers = {'User-Agent': "User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7"}

html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, "html5lib")
noscript = soup.find_all('noscript')
allHref = []
for url in noscript[-1].find_all('a'):
    href = url.get('href')
    allHref.append(href)
print(allHref[3])
print(len(allHref))