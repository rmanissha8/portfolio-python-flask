from flask import *
from werkzeug.utils import *
from settings import * 

authentication = Blueprint("authentication", __name__)

@authentication.route("/")
def index():
    return redirect(url_for('authentication.home')) 

@authentication.route("/home", methods=["POST","GET"])
def home():
    return render_template('base.html')
