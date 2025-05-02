from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend (GitHub Pages) to access this backend

@app.route("/joke")
def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    data = response.json()
    joke = f"{data['setup']} - {data['punchline']}"
    return jsonify({"joke": joke})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
