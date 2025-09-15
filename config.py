#!/bin/python3

from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    @staticmethod
    def init_app(app):
        pass


class TestConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False    


config = {
    'development': Config,
    'testing': TestConfig,
    'production': ProdConfig,
    # 'heroku': HerokuConfig,
    # 'docker': DockerConfig,
    # 'unix': UnixConfig,

    'default': Config
}