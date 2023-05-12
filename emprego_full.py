
#IMPORTANDO LIBRERIAS
import requests
from bs4 import BeautifulSoup 
import pandas as pd

#URL BASE DE DONDE TOMARE LOS DATOS
baseurl = 'https://www.emprego.pt/en/jobs/costa-rica'

#BUSCAMOS EL USER AGENT PARA EL EXPLORADOR QUE VAYAMOS A USAR Y LO COLOCAMOS EN UNA VARIABLE LLAMADA HEADER
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Brave/91.1.25.70'

# Obteniendo la primera página para encontrar el número total de páginas
r = requests.get('https://www.emprego.pt/en/jobs/costa-rica?page=1', headers=headers)
soup = BeautifulSoup(r.content, 'lxml')


# Buscando el número de la última página
pagination = soup.find('nav', class_='pagination')

# Comprobando si la paginación existe
if pagination is not None:
    all_pages = pagination.find_all('a', class_='page-link')
    last_page = int(all_pages[-2].text)  # el último elemento es 'Siguiente', por lo que usamos el penúltimo
else:
    last_page = 1  # Si no hay paginación, entonces asumimos que solo hay una página


worklinks = []
data = []


# Ahora puedes usar este valor en tu bucle for:
for x in range(1, last_page + 1):
    r = requests.get(f'https://www.emprego.pt/en/jobs/costa-rica?page={x}')
    soup = BeautifulSoup(r.content, 'lxml')
    worklist = soup.find_all('h2', class_='h4 media-heading card-title m0 text-ellipsis')
    for item in worklist:
        for link in item.find_all('a', href=True):
            worklinks.append(link['href'])

results = []  # Crear una lista vacía para almacenar los resultados

for link in worklinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    company_element = soup.find('span', class_='h4 font-weight-400 text-gray')
    company = company_element.text.strip() if company_element else None

    job_element = soup.find('span', class_='card-title')
    job = job_element.text.strip() if job_element else None

    description_element = soup.find('div', class_='card-body reader-block job-description')
    description = description_element.text.strip() if description_element else None

    result = {  # Crear un diccionario para cada conjunto de datos
        'company': company,
        'job': job,
        'description': description,
        'link': link
    }

    results.append(result)  # Agregar el diccionario a la lista de resultados

# Ahora que tienes todos los resultados, puedes crear un DataFrame y exportarlo a CSV
df = pd.DataFrame(results)
df.to_csv('jobs.csv', index=False)  # Guardar el DataFrame como un archivo CSV
