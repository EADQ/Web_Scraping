#IMPORTANDO LIBRERIAS
import requests
from bs4 import BeautifulSoup 
import pandas as pd

#URL BASE DE DONDE TOMARE LOS DATOS
baseurl = 'https://www.emprego.pt/en/jobs/costa-rica'

#BUSCAMOS EL USER AGENT PARA EL EXPLORADOR QUE VAYAMOS A USAR Y LO COLOCAMOS EN UNA VARIABLE LLAMADA HEADER
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Brave/91.1.25.70'

worklinks = []

for x in range(1,15):
#CREAMOS UNA VARIABLE QUE SE LLAMA R Y LE DAMOS EL METODO DE GET CON EL LINK QUE ME DA LA INFORMACION
    r = requests.get(f'https://www.emprego.pt/en/jobs/costa-rica?page={x}')
#CREANDO LA FUNCION CON EL ANALIZADOR QUE ESTAREMOS UTILIZANDO
    soup = BeautifulSoup(r.content, 'lxml')
    worklist = soup.find_all('h2', class_='h4 media-heading card-title m0 text-ellipsis')
# print(worklist)
    for item in worklist:
       for link in item.find_all('a', href=True):
           worklinks.append(link['href'])


# for link in worklinks:
    # print(link)

# testlink = 'https://www.emprego.pt/en/jobs/show/30390139949812550715069081920'

for link in worklinks:

    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    company_element = soup.find('span', class_='h4 font-weight-400 text-gray')
    if company_element is not None:
        company = company_element.text.strip()
    else:
        company = None

    job_element = soup.find('span', class_='card-title')
    if job_element is not None:
        job = job_element.text.strip()
    else:
        job = None

    description_element = soup.find('div', class_='card-body reader-block job-description')
    if description_element is not None:
        description = description_element.text.strip()
    else:
        description = None

    # company = soup.find('span', class_='h4 font-weight-400 text-gray').text.strip()
    # job = soup.find('span', class_='card-title').text.strip()
    # description = soup.find('div', class_='card-body reader-block job-description').text.strip()

    results = {
        'company': company,
        'job': job,
        'description': description
    }

    # print(results)
    # print(f"Link: {link}\nCompany: {company}\nJob: {job}\nDescription: {description}\n")

    worklist.append(results)
    # print('Saving: ', results['company'], results['job'])


df = pd.DataFrame()
print(df.head(15))


