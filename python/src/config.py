"""
Module containing environment configurations
"""
from os import getenv, environ


class Development:
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{0}:{1}@{2}:5432/{3}'.format(environ.get('dbuser'),environ.get('dbpass'),environ.get('dbhost'),environ.get('dbname'))


class Production:
    """
    Production environment configuration
    """
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{0}:{1}@{2}:5432/{3}'.format(environ.get('dbuser'),environ.get('dbpass'),environ.get('dbhost'),environ.get('dbname'))


app_config = {
    'development': Development,
    'production': Production,
}
