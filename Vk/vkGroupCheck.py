import json
import requests
from itertools import groupby


vkapi = "https://api.vk.com/method/groups.getMembers?group_id="
offset = "&offset="
groups = ["29403745", "rentm", "novoseliye", "1060484"]

A=[]
for group in groups:
    print(group)
    val = json.loads(requests.get(vkapi+group).text)["response"]["count"]
    print(val)
    for i in range(0,val,1000):
        users = json.loads(requests.get(vkapi+group+offset+str(i)).text)["response"]["users"]
        A+=users

A.sort()
print(len(A))

new_A = [el for el, _ in groupby(A)]
print(len(new_A))

f=open("id.txt", "w")
for item in new_A:
    f.write("%s\n" % item)
f.close()

counter = {}
for elem in new_A:
    counter[elem] = counter.get(elem, 0) + 1
doubles = {element: count for element, count in counter.items() if count > 1}
print(doubles)