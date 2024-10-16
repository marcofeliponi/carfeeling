from flask import Blueprint
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