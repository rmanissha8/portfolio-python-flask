#!/bin/python3

from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    FLASK_ENV=os.getenv("FLASK_ENV")
    FLASK_APP=os.getenv("FLASK_APP")
    FLASK_RUN_PORT=os.getenv("FLASK_RUN_PORT")

    @staticmethod
    def init_app(app):
        pass