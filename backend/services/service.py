import requests
import os
from flask import Flask, jsonify
import os
from firebase_admin import firestore, initialize_app

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))

initialize_app()
db = firestore.client()

@app.route("/")
def home():
    return "Hello, this is a Flask Microservice"
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)