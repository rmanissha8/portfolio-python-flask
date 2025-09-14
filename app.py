from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect
from flask_wtf import *
from pymysql import *
import pymysql
import os
from flask_mail import Mail, Message
from flask import *
from settings import *

app = Flask(__name__)

app.config['SECRET_KEY'] = "powerful secretkey"

mail = Mail(app)


from blueprint import authentication

app.register_blueprint(authentication)

if __name__ == '__main__':
    app.run(debug=True, port=FLASK_RUN_PORT,host='0.0.0.0')