from flask import Flask, redirect, render_template, request, url_for
import requests

API_URL = "https://pokeapi.co/api/v2/pokemon/"
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
    query = API_URL + pokemon

    response = requests.get(query)

    if response.status_code != 200:
        return render_template("pokemon.html", name="Pokemon not found")

    return render_template("pokemon.html", name=response.json())

if __name__ == "__main__":
    app.run(debug=True)