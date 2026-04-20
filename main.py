from flask import Flask, redirect, render_template, request, url_for
import Pokedex 
import requests
import Pokemon

API_URL = "https://pokeapi.co/api/v2/pokemon/"
pokedex = Pokedex.Pokedex(API_URL)
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        pokemon = request.form["query"]
        return redirect(url_for("user", pokemon=pokemon))
    else:
        return render_template("home.html")

@app.route("/<pokemon>")
def user(pokemon):
    response = pokedex.getPokeemon(pokemon)
    print(response.status_code)
    if response.status_code != 200:
        return render_template("error.html")

    return render_template("pokemon.html", name=Pokemon.Pokemon(pokemon, response.json()))
    

if __name__ == "__main__":
    app.run(debug=True)