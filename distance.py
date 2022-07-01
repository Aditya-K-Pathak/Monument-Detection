import json
import requests
import urllib.parse
from geopy.distance import geodesic


def loc():
    api_key = "xn31p6uc7coycvh7"

    response = requests.get(f"https://api.ipregistry.co/?key={api_key}")
    content = response.content
    content = json.loads(content.decode())
    # print(content)
    return (content["location"]["latitude"], content["location"]["longitude"])

def get_result(place):
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(place) +'?format=json'
    response = requests.get(url).json()
    destination = (response[0]["lat"], response[0]["lon"])
    
    # Print the distance calculated in km
    return (geodesic(loc(), destination).km)
