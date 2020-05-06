import os


class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = 'sisoft9&o4!$-<#ilyas&&iliyas'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
#   postgres://name:password@host:port/db_name

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = 'sisoft9&o4!$-<#ilyas&&iliyas'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

app_config = {
    'development': Development,
    'production': Production,
}