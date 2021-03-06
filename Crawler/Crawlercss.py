from bs4 import BeautifulSoup
import requests

from urllib.parse import urljoin

class PostCrawled():

    def __init__(self, titulo, emoticono, contenido, imagen):

        self.titulo=titulo
        self.emoticono=emoticono
        self.contenido=contenido
        self.imagen=imagen

class PostExtractor():

    def extraeInfo(self):

        urlBase="http://python.beispiel.programmierenlernen.io/index.php"
    

        miDoc=requests.get("http://python.beispiel.programmierenlernen.io/index.php")
    
        DocFinal=BeautifulSoup(miDoc.text, "html.parser")

        posts=[]

        for card in DocFinal.select(".card"):
            
            titulo=card.select(".card-title span")[1].text #Selecciono el indice 1 del tag span que es donde esta el titulo
            emoticono=card.select_one(".emoji").text
            contenido=card.select_one(".card-text").text
            imagen=urljoin(urlBase, card.select_one("img").attrs["src"])

            crawled=PostCrawled(titulo, emoticono, contenido, imagen)

            posts.append(crawled)

        return posts

unPost=PostExtractor()

listaPosts=unPost.extraeInfo()

for elPost in listaPosts:

    print(elPost.emoticono)
    print(elPost.titulo)
    print(elPost.contenido)
    print(elPost.imagen)
    print()

#print(listaPosts)
