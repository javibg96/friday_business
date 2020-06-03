import urllib
import requests
from bs4 import BeautifulSoup
import random


# desktop user-agent, no es solo de mac es que google es asi
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) " \
                    "Chrome/59.0.3071.125 Mobile Safari/537.36 "

headers = {"user-agent": USER_AGENT}

URL = "https://www.buzzfeed.com/awesomer/64-datos-alucinantes-que-te-haran-increiblemente-f"
resp = requests.get(URL, headers=headers)
if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
else:
    print(resp)
    soup = None

results = []
for g in soup.find_all('div', class_="subbuzz subbuzz-text xs-mb4 xs-relative"):
    for datos in g.find_all('p'):
        dato = datos.text
        if any(char.isdigit() for char in dato):
            result = ''.join(i for i in dato if not i.isdigit())
            result = result.replace(". ", "")
            results.append(result)

print(random.choice(results))  # los resultados son titulo y enlace
