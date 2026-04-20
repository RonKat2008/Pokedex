import requests

class Ability:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.effect = ""
        response = requests.get(self.url)

        json = response.json()

        effect = ""
        for effect in json["effect_entries"]:
            if effect["language"]["name"] == "en":
                effect = effect["effect"]
        self.effect = effect
    def __str__(self):
        return self.name + ": " + self.effect
