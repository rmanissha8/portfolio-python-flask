#!/bin/python3

from flask_mail import Mail
from flask import *
from config import Config


mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    mail.init_app(app)
    @app.context_processor
    def inject_mapbox_token():
        return dict(MAPBOX_TOKEN=app.config["MAPBOX_TOKEN"])

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    
    return app