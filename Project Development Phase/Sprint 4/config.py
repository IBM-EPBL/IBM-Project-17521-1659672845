import os
from dotenv import load_dotenv

load_dotenv()

CONFIG_PATH = os.path.abspath(__file__)
ROOT_DIR = os.path.dirname(CONFIG_PATH)
UPLOAD_DIRECTORY = os.path.join(ROOT_DIR, 'uploads')


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
