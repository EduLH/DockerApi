class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 8001


class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False


app_config = {
    'development': Development,
    'production': Production,
}
