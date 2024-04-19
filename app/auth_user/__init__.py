from flask import Blueprint

bp = Blueprint('auth_user', __name__)

from app.auth_user import routes
