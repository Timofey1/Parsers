import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
}

url = "https://www.avito.ru/moskva/kvartiry/1-k_kvartira_18_m_33_et._575430586"

def getsoup(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html5lib")
    return soup

soup = getsoup(url)

def getmetro(soup):
    metro = []
    infa = soup.findAll("span", {"class": "item-map-metro"})
    if infa is None:
        metro.append("No metro near")
        return metro
    else:
        for i in infa:
            mtr = i.text
            mtr = mtr[6:]
            mtr = mtr[:mtr.find(" ")-1]
            metro.append(mtr)
        return metro

def getprice(soup):
    infa = soup.find("span", {"class": "price-value-string js-price-value-string"}).text
    if infa is None:
        price = "no infa"
        return price
    else:

        integ = []
        i = 0
        while i < len(infa):
            infa_int = ''
            a = infa[i]
            while '0' <= a <= '9':
                infa_int += a
                i += 1
                if i < len(infa):
                    a = infa[i]
                else:
                    break
            i += 1
            if infa_int != '':
                integ.append(int(infa_int))
        price = str(integ)
        pr = int(re.sub(r'[\[\], ]', '', price))
        return pr

def getadr(soup):
    infa = soup.find("div", {"class": "item-view-seller-info"})
    if infa is None:
        adr = ""
        return adr
    else:
        infa = infa.findAll("div", {"class": "seller-info-value"})
        adr = infa[2].text
        return adr

def getarea(soup):
    infa = soup.findAll("li", {"class": "item-params-list-item"})
    if infa is None:
        area = "no area"
        return area
    else:
        area = infa[4].text
        integ = []
        i = 0
        while i < len(area):
            area_int = ''
            a = area[i]
            while '0' <= a <= '9':
                area_int += a
                i += 1
                if i < len(area):
                    a = area[i]
                else:
                    break
            i += 1
            if area_int != '':
                integ.append(int(area_int))
        return integ[0]

def getroom_num(soup):
    infa = soup.findAll("li", {"class": "item-params-list-item"})
    if infa is None:
        area = "no area"
        return area
    else:
        area = infa[0].text
        integ = []
        i = 0
        while i < len(area):
            area_int = ''
            a = area[i]
            while '0' <= a <= '9':
                area_int += a
                i += 1
                if i < len(area):
                    a = area[i]
                else:
                    break
            i += 1
            if area_int != '':
                integ.append(int(area_int))
        return integ[0]

def getpics(soup):
    all_pics = []
    infa = soup.find("ul", {"class": "gallery-list js-gallery-list"})
    if infa is None:
        return all_pics
    else:
        infa = infa.findAll("li")
        for i in infa:
            pic = i.find("span").get("style")
            pic = "https:" + pic[pic.find("//"):pic.rfind(");")]
            all_pics.append(pic)
    return all_pics

def getdescr(soup):
    infa = soup.find("div", {"class": "item-description-text"})
    if infa is None:
        descr = ""
        return descr
    else:
        return infa.text

