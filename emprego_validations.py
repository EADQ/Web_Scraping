# IMPORTANDO LIBRERIAS
import requests
from bs4 import BeautifulSoup 
import pandas as pd
from datetime import datetime

baseurl = 'https://www.emprego.pt/en/jobs/costa-rica'

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Brave/91.1.25.70'

worklinks = []
data = []
current_date = datetime.now().strftime('%d-%m-%Y')

for x in range(1,200):
    print(f'Fetching page {x}...')  # Nueva línea
    r = requests.get(f'https://www.emprego.pt/en/jobs/costa-rica?page={x}') 
    r.encoding='utf-8'
    soup = BeautifulSoup(r.content, 'lxml')
    worklist = soup.find_all('h2', class_='h4 media-heading card-title m0 text-ellipsis')
    for item in worklist:
        for link in item.find_all('a', href=True):
            worklinks.append(link['href'])


results = []  

for link in worklinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    company_element = soup.find('span', class_='h4 font-weight-400 text-gray')
    company = company_element.text.strip() if company_element else None

    job_element = soup.find('span', class_='card-title')
    job = job_element.text.strip() if job_element else None

    description_element = soup.find('div', class_='card-body reader-block job-description')
    description = description_element.text.strip() if description_element else None

    # Verificar el estado del enlace
    try:
        response = requests.head(link, headers=headers)
        link_status = 'existe' if response.status_code == 200 else 'no existe'
    except requests.exceptions.RequestException:
        link_status = 'no existe'

    result = {  
        'company': company,
        'job': job,
        'description': description,
        'link': link,
        'link_status': link_status
    }

    results.append(result)  

df = pd.DataFrame(results)
df.to_csv(f'jobs_emprego{current_date}.csv', index=False)  

print('Scraping completed. CSV file saved.')  # Nueva línea

