# from project import Game, Player, Race, Prompt
#
# p1 = Player("alecgc", "a@hotmail.com", "luckycharms2")
# prompt1 = Prompt("The Fox", "The quick brown fox jumped over the lazy dog.")
import requests
from flask import Flask, json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def root():

    url = "http://localhost:5213/prompts/2"
    PARAMS = {'address': 'location'}

    r = requests.get(url=url, params=PARAMS)
    data = r.json()

    return data

# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted
    app.run(port=3000, debug=True)