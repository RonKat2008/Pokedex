import Ability

class Pokemon:
    def __init__(self, name, pokemon_json):
        self.name = name
        self.abilities = []
        self.front_default = pokemon_json["sprites"]["front_default"]
        self.back_default = pokemon_json["sprites"]["back_default"]
        self.hp = pokemon_json["stats"][0]["base_stat"]
        self.attack = pokemon_json["stats"][1]["base_stat"]
        self.defense = pokemon_json["stats"][2]["base_stat"]
        self.special_attack = pokemon_json["stats"][3]["base_stat"]
        self.special_defense = pokemon_json["stats"][4]["base_stat"]
        self.speed = pokemon_json["stats"][5]["base_stat"]
        self.height = pokemon_json["height"]
        self.base_experience = pokemon_json["base_experience"]
        self.types = []
        self.moves = []
        for ability in pokemon_json["abilities"]:
            self.abilities.append(Ability.Ability(ability["ability"]["name"], ability["ability"]["url"]))
        for index in range(len(pokemon_json["types"])):
            self.types.append(pokemon_json["types"][index]["type"]["name"])
        for index in range(len(pokemon_json["moves"])):
            self.moves.append(pokemon_json["moves"][index]["move"]["name"])

