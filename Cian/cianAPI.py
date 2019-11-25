import requests
import json
from cianOneFlat import *


def inffromcian():
    all_infa = []
    link_template = 'https://cian.ru/rent/flat/'
    url = ["https://map.cian.ru/ajax/map/roundabout/?currency=2&deal_type=rent&engine_version=2&maxprice=35000&"
           "offer_type=flat&region=1&wp=1&room1=1&p=",
           "https://map.cian.ru/ajax/map/roundabout/?currency=2&deal_type=rent&engine_version=2&"
           "maxprice=45000&offer_type=flat&region=1&wp=1&room2=1&p=",
           "https://map.cian.ru/ajax/map/roundabout/?currency=2&deal_type=rent&engine_version=2&"
           "maxprice=55000&offer_type=flat&region=1&wp=1&room3=1&p="]
    for mainurl in url:
        for num in range(1, 6):
            url = mainurl + str(num)
            html = requests.get(url).text
            try:
                json_text = json.loads(html)
            except json.decoder.JSONDecodeError:
                print("json error")
                break
            if "data" in json_text:
                infa = json_text["data"]
                if "points" in infa:
                    infa = infa["points"]
                    for i in infa:
                        main = infa[i]
                        offers = main["offers"]
                        for j in offers:
                            room_num = j['property_type']
                            price = int(j['price_rur'][:-2])
                            floor = j["link_text"][3]
                            floor = floor[floor.find(" ") + 1:]
                            flat_id = j["id"]
                            area = j["link_text"][1]
                            area = area[:area.find(" ")]
                        url = link_template + flat_id
                        loc = i.replace(" ", ",")
                        adr = main["content"]["text"]

                        # ======
                        soup = getsoup(url)
                        all_pics = getpics(url)
                        all_metro = getmetro(soup)
                        phone = getphone(soup)
                        descr = getdescr(soup)
                        person_name = getpersonname(soup)
                        posttime = getposttime(soup)

                        # ======

                        x = {'room_num': room_num, 'metro': all_metro, 'pics': all_pics,
                         "cost": price, "floor": floor, "contacts": {"phone": phone, "person_name": person_name}, "loc": loc,
                         "url": url, "area": area, "adr": adr, "descr": descr, "date": posttime}

                        print(phone)
                        print(x)
                        # f = open("phone.txt", "w")
                        # f.write("%s\n" % phone)
                        # f.close()

                        all_infa.append(x)
            return all_infa

inffromcian()