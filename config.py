
class Config(object):
    DEBUG= False
    TESTING= False
    
class DevelopmentConfig(Config):
    MONGO_DB= 'mongodb://host.docker.internal:27018/configuration-bag'
    
class LocalDBConfig(Config):
    MONGO_DB= 'mongodb://localhost/configuration-bag'
    JWT_SECRET_KEY = "t1NP63m4wnBg6nyHYKfmc2TpCOGI4ns1"
