import os
from flask import Flask
from flask_cors import CORS
from routes import routes

app = Flask(__name__)

print('entrou no run.py !!!!!!!!')

env = os.environ.get('FLASK_ENV', 'development')

print('!!!!!!!env ===>', env)

if env != 'production':
    port = int(os.environ.get('PORT', 5000))
    os.environ['FIRESTORE_EMULATOR_HOST'] = 'localhost:8080'
else:
    port = int(os.environ.get('PORT', 8080))

app.register_blueprint(routes.bp)
CORS(app, origins=['http://localhost:5173'])

print('!!!!!port ===>', port)

if __name__ == "__main__":
    app.run(debug=(env != 'production'), host="0.0.0.0", port=port)
