#IMPORTANDO LIBRERIAS
import requests
from bs4 import BeautifulSoup 
# import pandas as pd
# from datetime import datetime
def extract():
    url = 'https://www.buscojobs.cr/ofertas/_costa-rica'
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
    ]

    r = requests.get(url, headers={'User-Agent': random.choice(user_agents)})
    soup = BeautifulSoup(r.content, 'html.parser')
    if r.status_code == 200:
        print('La solicitud fue exitosa')
    else:
        print('La solicitud no fue exitosa')
        print('Codigo de estado: ', r.status_code)
        print('Contenido de la respuesta', r.text)
        return soup

# def transform(soup):
    # divs = soup.find_all('div', class_='card card__job')
    # for item in divs:
        # title = item.find('a').text.strip()
        # company = item.find('div', class_='card__job-empname-label').text.strip()

        # elemento = item.find('button', {'class': 'button button--primary button--applyJobPreview'})
        # if elemento:
            # onclick_value = elemento.get('onclick')
            # inicio = onclick_value.index("'") + 1
            # fin = onclick_value.index("'", inicio)
            # url_extraida = onclick_value[inicio:fin]

            # print(f"Title: {title}")
            # print(f"Company: {company}")
            # print(f"URL: {url_extraida}")
            # print("--------------------")

# c = extract(0)
# transform(c)

# baseurl = 'https://www.buscojobs.cr/ofertas/_costa-rica'

# headers = {}
# headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Brave/91.1.25.70'

# r = requests.get('https://www.buscojobs.cr/ofertas/_costa-rica')
# soup = BeautifulSoup(r.content, 'html.parser')
# worklist = soup.find_all('a', class_='ListadoOfertas_above__TFBOi')

# if r.status_code == 200:
    # print('La solicitud fue exitosa')
# else:
    # print('La solicitud no fue exitosa')
    # print('Codigo de estado: ', r.status_code)
    # print('Contenido de la respuesta', r.text)

# print(worklist)
# worklinks = []
# data = []
# current_date = datetime.now().strftime('%d-%m-%Y')

# for x in range(1,3):
    # print(f'Fetching page {x}...')  # Nueva línea
    # r = requests.get(f'https://www.emprego.pt/en/jobs/costa-rica?page={x}')
    # soup = BeautifulSoup(r.content, 'lxml')
    # worklist = soup.find_all('h2', class_='h4 media-heading card-title m0 text-ellipsis')
    # for item in worklist:
        # for link in item.find_all('a', href=True):
            # worklinks.append(link['href'])

# results = []  

# for link in worklinks:
    # r = requests.get(link, headers=headers)
    # soup = BeautifulSoup(r.content, 'lxml')

    # company_element = soup.find('span', class_='h4 font-weight-400 text-gray')
    # company = company_element.text.strip() if company_element else None

    # job_element = soup.find('span', class_='card-title')
    # job = job_element.text.strip() if job_element else None

    # description_element = soup.find('div', class_='card-body reader-block job-description')
    # description = description_element.text.strip() if description_element else None

    # result = {  
        # 'company': company,
        # 'job': job,
        # 'description': description,
        # 'link': link
    # }

    # results.append(result)  

# df = pd.DataFrame(results)
# df.to_csv(f'jobs_emprego{current_date}.csv', index=False)  

# print('Scraping completed. CSV file saved.')  # Nueva línea
