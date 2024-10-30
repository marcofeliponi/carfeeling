from flask import Blueprint, request
from services import services

bp = Blueprint('routes', __name__)

@bp.route('/')
def hello_world():
    return 'Hello, World!'

@bp.route('/api/cars')
def get_cars():
    return services.get_cars_service()

@bp.route('/api/brands')
def get_brands():
    return services.get_brands_service()

@bp.route('/api/analysis/<path:car>')
def get_car_analysis(car):
    query_params = request.args
    return services.get_car_analysis_service(car, query_params)

# TODO: This route will be used to simulate the scraping process in real time.
@bp.route('/api/scrape/<car>')
def scrape_reviews(car):
    return 'Scraping...'