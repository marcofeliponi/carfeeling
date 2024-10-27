import os
from flask import Flask
from flask_cors import CORS
from routes import routes
from scripts import web_scraping

app = Flask(__name__)

env = os.environ.get('FLASK_ENV', 'development')

if env != 'production':
    os.environ['FIRESTORE_EMULATOR_HOST'] = 'localhost:8080'

app.register_blueprint(routes.bp)
CORS(app, resources={r"/*": {"origins": ['http://localhost:5173', 'https://carfeeling-33182721445.southamerica-east1.run.app']}})

# web_scraping.run()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
