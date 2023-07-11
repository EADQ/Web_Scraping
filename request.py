import requests

r = requests.get('https://api.github.com/events')

headers = r.headers['content-type']

# print(r.status_code)

# print(headers)


