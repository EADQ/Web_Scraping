# import requests
# from bs4 import BeautifulSoup
# import random

# def extract(page):
    # url = f'https://cr.talent.com/jobs?k=Software+Engineer&l=Costa+Rica&radius=15&p={page}&context=serp_pagination'
    # user_agents = [
        # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        # 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
        # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4',
        # 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
        # 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
    # ]
    # r = requests.get(url, headers={'User-Agent': random.choice(user_agents)})
    # soup = BeautifulSoup(r.content, 'html.parser')
    # return soup

# def transform(soup):
    # divs = soup.find_all('div', class_ ='card card__job')
    # for item in divs:
        # tittle = item.find('a').text.strip()
        # company = item.find('div', class_='card__job-empname-label').text.strip()
        # # description = soup.select_one("jobsPreview")
        # # description = item.find('div', id='jobPreview__body--description').text.strip() 
        # # description = item.find('div', {'class' : 'card card--preview acsb-active'}).text.strip()
        # # print(description)
# # Encontrar el elemento que contiene la URL
        # elemento = soup.find('button', {'class': 'button button--primary button--ctaApply'})

# # Obtener el valor del atributo onclick
        # onclick_value = elemento.get('onclick')

# # Extraer la URL de la cadena onclick
        # inicio = onclick_value.index("'") + 1
        # fin = onclick_value.index("'", inicio)
        # url_extraida = onclick_value[inicio:fin]

# # Imprimir la URL extraída

# c = extract(0)
# transform(c)

# print(url_extraida)

# print(url_extraida(transform(c)))

import requests
from bs4 import BeautifulSoup
import random

def extract(page):
    url = f'https://cr.talent.com/jobs?k=Software+Engineer&l=Costa+Rica&radius=15&p={page}&context=serp_pagination'
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
    ]
    r = requests.get(url, headers={'User-Agent': random.choice(user_agents)})
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_='card card__job')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('div', class_='card__job-empname-label').text.strip()

        elemento = item.find('button', {'class': 'button button--primary button--applyJobPreview'})
        if elemento:
            onclick_value = elemento.get('onclick')
            inicio = onclick_value.index("'") + 1
            fin = onclick_value.index("'", inicio)
            url_extraida = onclick_value[inicio:fin]

            print(f"Title: {title}")
            print(f"Company: {company}")
            print(f"URL: {url_extraida}")
            print("--------------------")

c = extract(0)
transform(c)


