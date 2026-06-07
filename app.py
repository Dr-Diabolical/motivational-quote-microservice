# Daniel Downes, downesda
# File: app.py
# Last Edited: 06/07/2026
# Description: REST server that handles getting a 
#              random motivational quote from the
#              quotes.json file
# Usage:
#   ./python3 app.py
# Example Request:
#   http://127.0.0.1:6465/quote
#   The example returns a random motivational quote from the
#   quotes.json file

from flask import Flask
import json
import random

app = Flask(__name__)

HOST = "127.0.0.1"
PORT = 6465
DEFAULT_PATH = "/quote"
QUOTES_PATH = "./quotes.json"


def read_json_file(filepath: str):
    with open(filepath) as file:
        return json.load(file)


### GET REQUESTS ###


# Responds to the client with a random motivational quote
@app.get(DEFAULT_PATH)
def get_default_response():
    quotes = read_json_file(QUOTES_PATH)
    return {"quote": random.choice(quotes["quotes"])}, 200


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
