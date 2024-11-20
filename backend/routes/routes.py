"""
All the routes for the backend application.
"""

from flask import Blueprint, request
from services import services
# from scripts import web_scraping
# import asyncio

bp = Blueprint('routes', __name__)

@bp.route('/api/cars', methods=['GET'])
def get_cars():
    """Get all cars from database."""
    return services.get_cars_service()

@bp.route('/api/brands', methods=['GET'])
def get_brands():
    """Get all car brands from database."""
    return services.get_brands_service()

@bp.route('/api/analysis/<path:car>', methods=['GET'])
def get_car_analysis(car):
    """Get analysis for a specific car."""
    query_params = request.args
    return services.get_car_analysis_service(car, query_params)

@bp.route('/api/comparison/<path:car>', methods=['GET'])
def get_car_comparison(car):
    """Get comparison for a specific car."""
    return services.get_car_comparison_service(car)

# @bp.route('/api/scrape/', methods=['POST'])
# def scrape_reviews():
#     """Scrape reviews for a specific car and year."""
#     car = request.args.get('car')
#     year = request.args.get('year')
#     response = asyncio.run(web_scraping.run(car, year))
#     if response:
#       return { 'status': 'success', 'data': response }
#     return { 'status': 'error', 'message': 'Scraped failed' }

@bp.route('/api/ai-chat/', methods=['POST'])
def ai_chat():
    """Handle AI chat requests."""
    body = request.json
    token = request.headers.get('Authorization')
    return services.ai_chat_service(token, messages=body['messages'])
