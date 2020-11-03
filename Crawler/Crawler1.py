import requests

r = requests.get("https://www.movistar.es/")

print(r.status_code)

print(r.headers)