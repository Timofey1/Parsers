import requests
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
}


def getsoup(url):
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "html5lib")
    return soup


def getarea(soup):
    area_info = soup.find("table", {"class": "object_descr_props"})
    if area_info is None:
        area = "No info"
        return area
    else:
        area_tr = area_info.findAll("tr")
        area = area_tr[2].text
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
        try:
            area = integ[0]
            return area
        except IndexError:
            area = "No info"
            return area


def getadr(soup):
    adr_info = soup.find("address", {"class": "address--D3O4n"})
    if adr_info is None:
        adr = "Error"
        return adr
    else:
        adr = adr_info.text
        return adr


def getpics(url):
     all_images = []
     html = requests.get(url,  headers=headers).text
     left = html.find("window._cianConfig['offer-card'] = ")
     infa = html[left+35:]
     infa = infa[:infa.find("<")-2]
     try:
        jsont = json.loads(infa)
     except json.decoder.JSONDecodeError:
         all_images = ["no photo"]
         return all_images
     if "defaultState" in jsont:
         maininfa = jsont["defaultState"]
         if "offerData" in maininfa:
             maininfa = maininfa["offerData"]
             if "offer" in maininfa:
                 maininfa = maininfa["offer"]
                 if "photos" in maininfa:
                     maininfa = maininfa["photos"]
                 for i in maininfa:
                     img = i["fullUrl"]
                     all_images.append(img)
     return all_images


def getmetro(soup):
    all_metro = []
    metro_infa = soup.findAll("a", {"class": "underground_link--1qgA6"})
    if metro_infa is None:
        all_metro = ["No metro near"]
        return all_metro
    else:
        for i in metro_infa:
            metro = i.text
            all_metro.append(metro)
            return all_metro


def getphone(soup):
    ph_infa = soup.find("a", {"class": "phone--1OSCA"})
    if ph_infa is None:
        phone = "No Phone"
        return phone
    else:
        phone = ph_infa.text
        return phone


def getdescr(soup):
    descr_info = soup.find("p", {"class": "description-text--3SshI"})
    if descr_info is None:
        descr = "No descr"
        return descr
    else:
        descr_info = str(descr_info)[1:]
        bord_r = descr_info.find("<")
        bord_l = descr_info.find(">")
        descr = descr_info[bord_l+1:bord_r]
        return descr


def getpersonname(soup):
    person_name_info = soup.find("div", {"class": "link-wrapper--EDwrd"})
    if person_name_info is None:
        person_name = "no name"
        return person_name
    else:
        person_name = person_name_info.find("h2", {"class": "title--2iUH-"}).text
        return person_name


def getposttime(soup):
    infa = soup.find("div", {"class": "container--3Y9rb"})
    if infa is None:
        posttime = ""
        return posttime
    else:
        posttime = infa.text
        return posttime
