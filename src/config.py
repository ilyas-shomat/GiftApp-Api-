import os


class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = 'sisoft9&o4!$-<#ilyas&&iliyas'
    SQLALCHEMY_DATABASE_URI = 'postgres://tydhyhhsglltnb:78d71d678e3e69f78a298d610b4d753ba82ccd5cefa103a855fc6bc66f24db0f@ec2-3-231-16-122.compute-1.amazonaws.com:5432/da44o9ph1k7n3v'
#   postgres://name:password@host:port/db_name

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = 'sisoft9&o4!$-<#ilyas&&iliyas'
    SQLALCHEMY_DATABASE_URI = 'postgres://tydhyhhsglltnb:78d71d678e3e69f78a298d610b4d753ba82ccd5cefa103a855fc6bc66f24db0f@ec2-3-231-16-122.compute-1.amazonaws.com:5432/da44o9ph1k7n3v'

app_config = {
    'development': Development,
    'production': Production,
}