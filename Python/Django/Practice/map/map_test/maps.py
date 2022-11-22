import json


# 주소를 통해 위치 얻기
from geopy.geocoders import Nominatim

def search_location(address):
    geolocoder = Nominatim(user_agent="South Korea", timeout=None)
    geo = geolocoder.geocode(address)
    crd = {"lat": str(geo.latitude), "lng": str(geo.longitude)}

    return crd


# def maps(x, y):
#     with open("C:/Users/ADMIN/OneDrive/Desktop/TIL/Python/Django/Practice/map/parkdata.json", encoding="utf-8") as file:
#         park_data = json.load(file)
#         parks = park_data["records"]
#         park_info = [] 

#         for park in parks:
#             park_info.append({
#                 'title': park['공원명'],
#                 'lat': park['위도'],
#                 'lng': park['경도'],
#                 'address': park['소재지지번주소'],
#             })

#         parkJson = json.dumps(park_info)
#     return parkJson
