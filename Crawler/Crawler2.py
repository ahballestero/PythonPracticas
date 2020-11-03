from bs4 import BeautifulSoup
import requests

miDoc=requests.get("http://python.beispiel.programmierenlernen.io/index.php")


DocFinal=BeautifulSoup(miDoc.text, "html.parser")

iconos=DocFinal.select(".emoji")

print(iconos[0].text)

