from flask import *
from src.main import main
from src.main.utils import get_my_location, haversine, get_test_location
from datetime import datetime
import geocoder


@main.route('/', methods=["GET"])
def index():

    
    ip = request.environ['REMOTE_ADDR']
    
    g = geocoder.ip(ip)

    now = datetime.now().strftime("%A, %d %B %Y | %H:%M:%S")
    if get_my_location() is not None:
        user_lat, user_lon = get_test_location()
        # print(f"User Location: {user_lat}, {user_lon}")
        lat, lon = get_my_location()
        # print(f"Current Location: {lat}, {lon}")
        dist_km = round(haversine(lat, lon, user_lat, user_lon), 1)

    else:
        user_lat, user_lon, dist_km = None, None, None


    return render_template('index.html', now=now,
                           user_lat=user_lat,
                           user_lon=user_lon,
                           dist_km=dist_km)



@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/projects')
def projects():
    return render_template('projects.html')