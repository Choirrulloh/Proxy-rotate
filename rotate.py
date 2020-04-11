from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import random
import re
import urllib
import requests

ua = UserAgent()

def rotate_agent():
    return ua.random

def getProxies():
    Req = requests.get('https://www.sslproxies.org/',
                       headers={'User-Agent': rotate_agent()})
    bs = BeautifulSoup(Req.content, features="html.parser")
    Proxies = []
    for row in bs.tbody.find_all('tr'):
        cols = row.find_all('td')
        Proxies.append({'IP': cols[0].text, 'Port': cols[1].text})
    return Proxies

i = 0
Proxies = getProxies()

for k in range(50):
    i += 1
    ip = Proxies[k]['IP']
    port = Proxies[k]['Port']
    proxiz ={'http': 'http://'+ip+':'+port}
    try:
        Req = requests.get('http://icanhazip.com/', headers={
                        'User-Agent': rotate_agent()}, proxies=proxiz, timeout=5)
        myip = re.sub(r'[^0-9^\.:]', '', str(Req.content))
        print(myip)
    except requests.exceptions.RequestException as e:
        i += 1
