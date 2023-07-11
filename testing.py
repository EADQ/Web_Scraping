import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.unimart.com/' 

r = requests.get('https://www.unimart.com/collections/casa')
soup = BeautifulSoup(r.content, 'lxml')
elements = soup.find_all('div', class_='ls-title')

# PRINTS 
print('The Status Code is', r.status_code)
print(len(elements))
