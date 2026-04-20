import requests
import Pokemon

class Pokedex:
    def __init__(self, api_url):
        self.api_url = api_url
    

    def getPokeemon(self, name):
        query = self.api_url + name

        response = requests.get(query)

     
        return response