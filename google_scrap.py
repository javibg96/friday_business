import urllib
import requests
from bs4 import BeautifulSoup

ciudad = "Dublin"
query = "hora en " + ciudad
query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}"

# desktop user-agent, no es solo de mac es que google es asi
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) " \
                    "Chrome/59.0.3071.125 Mobile Safari/537.36 "

headers = {"user-agent": USER_AGENT}
resp = requests.get(URL, headers=headers)
if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
else:
    print(resp)
    soup = None

resp = soup.find_all('div', class_='gsrt')
resp2 = soup.find_all('div', class_='vk_gy vk_sh')
print(resp2)
for i in resp2:
    print(f"Hora en {ciudad}: ", i.text)
# print(resp)
# [<div aria-level="3" class="gsrt vk_bk dDoNo" role="heading">17:44</div>]
for i in resp:
    print(f"Hora en {ciudad}: ", i.text)
results = []
# for g in soup.find_all('div', class_='r'):
#    anchors = g.find_all('a')
#    if anchors:
#        link = anchors[0]['href']
#        title = g.find('h3').text
#        item = {
#            "title": title,
#            "link": link
#        }
#        results.append(item)
# print(results)  # los resultados son titulo y enlace
