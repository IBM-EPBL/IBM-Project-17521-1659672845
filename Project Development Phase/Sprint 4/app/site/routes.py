from flask import Blueprint

site = Blueprint('site', __name__)


@site.route('/')
def index():
    return "<h1>Welcome to Our Waste Management System</h1>"


@site.route('/health')
def health_check():
    return "ok"
