from django.shortcuts import render
import json


# Create your views here.
def map(request):
    with open("C:/Users/ADMIN/OneDrive/Desktop/TIL/Python/Django/Practice/map/map_test/parkdata.json", encoding="utf-8") as file:
        park_data = json.load(file)
        parks = park_data["records"]
        park_info = [] 

        for park in parks:
            park_info.append({
                'title': park['공원명'],
                'lat': park['위도'],
                'lng': park['경도'],
                'address': park['소재지지번주소'],
            })

        parkJson = json.dumps(park_info)
    return render(request, "map/map.html", {'parkJson': park_info})