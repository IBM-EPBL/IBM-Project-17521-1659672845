from flask import Flask
from flask_cors import CORS
from app.site.routes import site
from app.api.routes import api
from app.models import setup_db


def create_app():
    app = Flask(__name__)
    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")
    CORS(app)
    app.register_blueprint(site)
    app.register_blueprint(api)
    setup_db(app)
    return app
