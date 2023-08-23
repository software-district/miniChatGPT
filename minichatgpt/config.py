import os
from os.path import abspath, dirname, join
from dotenv import load_dotenv

basedir = abspath(dirname(__file__))
load_dotenv(join(basedir, '.env'))


class Config:
    """Base config."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = join(basedir, 'frontend', 'assets')
    TEMPLATES_FOLDER = join(basedir, 'frontend', 'pages')


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
