
class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = 'sisoft9&o4!$-<#ilyas&&iliyas'
    SQLALCHEMY_DATABASE_URI = 'postgres://lxkhfdrzdjsfgo:958a7405fcf7839af51187d3881b448c34fa3b1cfc60748081b349454123e338@ec2-3-231-16-122.compute-1.amazonaws.com:5432/dcf6l2rpdh87nc'
#   postgres://name:password@host:port/db_name

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = 'sisoft9&o4!$-<#ilyas&&iliyas'
    SQLALCHEMY_DATABASE_URI = 'postgres://lxkhfdrzdjsfgo:958a7405fcf7839af51187d3881b448c34fa3b1cfc60748081b349454123e338@ec2-3-231-16-122.compute-1.amazonaws.com:5432/dcf6l2rpdh87nc'

app_config = {
    'development': Development,
    'production': Production,
}