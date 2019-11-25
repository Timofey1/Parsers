import requests
from bs4 import BeautifulSoup
from avitoOneFlat import getsoup, getmetro, getprice, getadr, getroom_num, getpics, getdescr
from avitoPhone import Bot



def avito():
    main_url = "https://www.avito.ru/moskva/kvartiry/sdam/na_dlitelnyy_srok/1-komnatnye?pmax=35000&pmin=0&i=1&p="
    all_infa = []

    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'youremail@domain.com'  # This is another valid field
    }
    for i in range(1, 101):
        html = requests.get(main_url).text
        soup = BeautifulSoup(html, "html5lib")
        infa = soup.findAll("div", {"class": "item"})

        for i in infa:
            lin_k = i.find("a", {"class", "item-description-title-link"}).get("href")
            url = "https://www.avito.ru" + lin_k
            # print(url)
            # =====
            soup = getsoup(url)
            all_metro = getmetro(soup)
            price = getprice(soup)
            adr = getadr(soup)
            area = getarea(soup)
            room_num = getroom_num(soup)
            all_pics = getpics(soup)
            descr = getdescr(soup)
            phone = Bot(url)
            # =====

            x = {'room_num': room_num, 'metro': all_metro, 'pics': all_pics,
                 "cost": price, "contacts": {"phone": phone},
                 "url": url, "area": area, "adr": adr, "descr": descr}

        all_infa.append(x)