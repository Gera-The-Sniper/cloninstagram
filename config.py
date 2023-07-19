class Config:
    SECRET_KEY = 'filipenses38'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'igflaskusers'
    
config = {
    'development': DevelopmentConfig
}