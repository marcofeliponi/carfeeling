from flask import Blueprint, request
from services import services
# from scripts import web_scraping
# import asyncio

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@bp.route('/api/cars', methods=['GET'])
def get_cars():
    return services.get_cars_service()

@bp.route('/api/brands', methods=['GET'])
def get_brands():
    return services.get_brands_service()

@bp.route('/api/analysis/<path:car>', methods=['GET'])
def get_car_analysis(car):
    query_params = request.args
    return services.get_car_analysis_service(car, query_params)

@bp.route('/api/comparison/<path:car>', methods=['GET'])
def get_car_comparison(car):
    return services.get_car_comparison_service(car)

# @bp.route('/api/scrape/<path:car>', methods=['POST'])
# def scrape_reviews(car):
#     year = request.args.get('year')
#     response = asyncio.run(web_scraping.run(car, year))
    
#     if response:
#         return { 'status': 'success', 'data': response }
    
#     return { 'status': 'error', 'message': 'Scraped failed' }