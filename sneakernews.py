from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
}


class Sneakers_release:
    title = ""
    img_url = ""
    price = ""
    release_date = ""

    def __init__(self, title, img, price, date):
        self.title = title
        self.img_url = img
        self.price = price
        self.release_date = date


class Description:
    descrption = " "
    imgs = []
    def __init__(self, description, imgs):
        self.descrption = description
        self.imgs = imgs


url = "http://sneakernews.com/air-jordan-release-dates/"
# url = "http://sneakernews.com/release-dates/"
html = requests.get(url, headers=headers).text


def pars_release(html):
    soup = BeautifulSoup(html, "html5lib")
    post_main = soup.findAll('section', {"class": "sneaker-post-main"})
    nomer = 0
    cross = []
    for row in post_main:
        title = row.find('h2', {"class": "header-title"}).text
        img_url = row.find('img').get("src")
        price = row.find('p', {"class": "release-price"}).text
        release_date = row.find('span', {"class": "release-date"}).text
        print("№:%s " % nomer, title)
        print("Release date is : ", release_date)
        print("Prise is : ", price)
        print("Img : ", img_url)
        print("="*125)
        cross[nomer] = Sneakers_release(title, img_url, price, release_date)
        nomer += 1


def pars_with_descript(html):
    soup = BeautifulSoup(html, "html5lib")
    post_main = soup.findAll('section', {"class": "sneaker-post-main"})
    for row in post_main:
        sneakers_href = row.find('h2', {"class": "header-title"})
        try:
            sneakers_url = sneakers_href.find('a').get("href")
            if sneakers_url[:4] != "http":
                sneakers_url = "HREF ERROR"
        except AttributeError:
            sneakers_url = "NO HREF"
        if sneakers_url == "NO HREF" or sneakers_url == "HREF ERROR":
            pass
        else:
            html2 = requests.get(sneakers_url, headers=headers).text
            soup2 = BeautifulSoup(html2, "html5lib")
            description_class = soup2.findAll('div', {"class": "pagination-content content-page-1"})
            imgs = []
            nomer = 0
            desc = []
            for r in description_class:
                try:
                    description = r.find('blockquote').text
                except AttributeError:
                    description = "NO DESCRIPTION"
                print(description)
                print()
                images = r.findAll("img")
                for i in images:
                    img_url = i.get("src")
                    if img_url.find("ebay") == -1:
                        print(img_url)
                        imgs.append(img_url)
                desc[nomer] = Description(description, imgs)
                print('='*100)


pars_release(html)
# pars_with_descript(html)
