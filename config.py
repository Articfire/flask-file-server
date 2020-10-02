class Config(object):
    DEBUG = False
    TESTING = False
    UPLOAD_FOLDER = 'files/'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    HOST = '127.0.0.1'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True