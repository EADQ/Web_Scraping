import requests
from bs4 import BeautifulSoup
import random

def extract(page):
    url = f'https://cr.indeed.com/jobs?q=&l=Costa+Rica&start={page}&pp=gQAPAAAAAAAAAAAAAAACAzfamgAmAQEBBgbtgRxJLmlxnE8yAOiPH4_PJw73BEvM92GC3fM_Sc8iPnwAAA'
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
    ]
    r = requests.get(url, headers={'User-Agent': random.choice(user_agents)})
    return r.status_code

print(extract(0))

# Investigar para solucionar el estado de 403 que estamos teniendo para poder continuar
