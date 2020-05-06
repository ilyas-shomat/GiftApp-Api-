
class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = 'sisoft9&o4!$-<#ilyas&&iliyas'
    SQLALCHEMY_DATABASE_URI = 'postgres://nlcdeuiwwkpdqo:6d8752cce8036185f550b2abc2784e364f3ffee0898d495e2dc314d33df1f1d8@ec2-54-228-209-117.eu-west-1.compute.amazonaws.com:5432/d8mdouc33b6jq5'
#   postgres://name:password@host:port/db_name

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = 'sisoft9&o4!$-<#ilyas&&iliyas'
    SQLALCHEMY_DATABASE_URI = 'postgres://nlcdeuiwwkpdqo:6d8752cce8036185f550b2abc2784e364f3ffee0898d495e2dc314d33df1f1d8@ec2-54-228-209-117.eu-west-1.compute.amazonaws.com:5432/d8mdouc33b6jq5'

app_config = {
    'development': Development,
    'production': Production,
}