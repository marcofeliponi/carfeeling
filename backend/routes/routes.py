from flask import Blueprint
from services import services

bp = Blueprint('routes', __name__)

@bp.route('/')
def get_cars():
    return services.get_cars_service()