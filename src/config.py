
class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = 'sisoft9&o4!$-<#ilyas&&iliyas'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:8648@localhost:5432/gift_app'
#   postgres://name:password@host:port/db_name

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = 'sisoft9&o4!$-<#ilyas&&iliyas'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:8648@localhost:5432/gift_app'

app_config = {
    'development': Development,
    'production': Production,
}