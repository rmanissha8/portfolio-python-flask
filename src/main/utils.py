import math
from geopy.geocoders import *

def get_my_location():
    geolocator = Photon(user_agent="measurements")
    location = geolocator.geocode("Wattala, Sri Lanka")
    return location.latitude, location.longitude

def get_test_location():
    geolocator = Photon(user_agent="measurements")
    location = geolocator.geocode("London, United Kingodm")
    return location.latitude, location.longitude  

def haversine(lat1, lon1, lat2, lon2):
    """Calculate distance in km between two coordinates"""
    R = 6371  # km
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return R * (2*math.atan2(math.sqrt(a), math.sqrt(1-a)))

