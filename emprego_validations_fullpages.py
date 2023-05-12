# IMPORTANDO LIBRERIAS
import requests
from bs4 import BeautifulSoup 
import pandas as pd
from datetime import datetime
import time  # Nueva importación

baseurl = 'https://www.emprego.pt/en/jobs/costa-rica'

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Brave/91.1.25.70'

worklinks = []
data = []
current_date = datetime.now().strftime('%d-%m-%Y')

page = 1

# Crea una sesión de requests
with requests.Session() as s:
    s.headers.update(headers)
    
    while True:
        print(f'Fetching page {page}...')  # Nueva línea
        r = s.get(f'https://www.emprego.pt/en/jobs/costa-rica?page={page}')
        soup = BeautifulSoup(r.content, 'lxml')
        worklist = soup.find_all('h2', class_='h4 media-heading card-title m0 text-ellipsis')

        # Verifica si hay un botón de "siguiente página". Si no lo hay, termina el bucle.
        next_page = soup.find('a', rel='next')
        if not next_page:
            print('No more pages found. Breaking the loop.')  # Nueva línea
            break

        for item in worklist:
            for link in item.find_all('a', href=True):
                worklinks.append(link['href'])
            time.sleep(5)  # Añade un retraso aquí para después de cada solicitud de página individual
        page += 1  # Incrementa la página para la próxima iteración

    results = []  

    for link in worklinks:
        print(f'Fetching job details for {link}...')  # Nueva línea
        r = s.get(link)
        soup = BeautifulSoup(r.content, 'lxml')

        company_element = soup.find('span', class_='h4 font-weight-400 text-gray')
        company = company_element.text.strip() if company_element else None

        job_element = soup.find('span', class_='card-title')
        job = job_element.text.strip() if job_element else None

        description_element = soup.find('div', class_='card-body reader-block job-description')
        description = description_element.text.strip() if description_element else None

        # Verificar el estado del enlace
        try:
            response = s.head(link)
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
        time.sleep(5)  # Añade un retraso aquí para después de cada solicitud de trabajo individual

df = pd.DataFrame(results)
df.to_csv(f'jobs_emprego{current_date}.csv', index=False)  

print('Scraping completed. CSV file saved.')  # Nueva línea
