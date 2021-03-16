import requests as r
from ybw.get import headers
import json
import sys

def trans(s):
    return bytes(s,encoding='unicode-escape').decode('unicode-escape')

h = """accept: text/plain, */*; q=0.01
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en;q=0.8
origin: https://www.ipip.net
referer: https://www.ipip.net/
sec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"
sec-ch-ua-mobile: ?0
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-site
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"""

ak = "hpbYUdHFY9XNRfwsb7QSwWF2bdMZfaqu"
url = 'https://v6r.ipip.net/?format=callback'
if not sys.argv[1]:
    pubip = r.get(url,headers=headers(h)).text[10:-2]
else:
    pubip = sys.argv[1]
    
url2 = "https://api.map.baidu.com/location/ip?ak={}&ip={}&coor=bd09ll".format(ak,pubip)

location = r.get(url2).text
info = json.loads(location)
x, y = info['content']['point'].values()
items = ['province','city','street','street_number']
addr = ' '.join([trans(j) for j in [info['content']['address_detail'][i] for i in items]])
print(pubip, addr, (x,y))

# {"address":"CN|\u91cd\u5e86|\u91cd\u5e86|None|CMNET|0|0",
# "content":{"address":"\u91cd\u5e86\u5e02",
#         "address_detail":{"city":"\u91cd\u5e86\u5e02","city_code":132,"district":"","province":"\u91cd\u5e86\u5e02","street":"","street_number":""},
#         "point":{"x":"106.53063501","y":"29.54460611"}
#         },
# "status":0}