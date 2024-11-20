import os
from flask import Flask
from flask_cors import CORS
from routes import routes
# import schedule
# from scripts import web_scraping

app = Flask(__name__)

app.register_blueprint(routes.bp)
CORS(app, resources={r"/*": {"origins": ['http://localhost:5173', 'https://carfeeling-33182721445.southamerica-east1.run.app']}})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

    # schedule.every().monday.do(web_scraping.run())
