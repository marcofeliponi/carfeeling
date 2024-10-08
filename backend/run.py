import os
from flask import Flask
from flask_cors import CORS
import os
from routes import routes

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))
os.environ['FIRESTORE_EMULATOR_HOST'] = 'localhost:8080'

app.register_blueprint(routes.bp)
CORS(app, origins=['http://localhost:5173'])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)