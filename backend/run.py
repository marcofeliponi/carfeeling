import os
from flask import Flask
import os
from routes import routes

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))
os.environ['FIRESTORE_EMULATOR_HOST'] = 'localhost:8080'

app.register_blueprint(routes.bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)