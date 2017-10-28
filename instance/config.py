import os


class Config(object):
    """Main configuration"""
    DEBUG = False
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    DEBUG = True


app_config = {
    'development':DevelopmentConfig
}