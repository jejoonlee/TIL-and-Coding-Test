from django.shortcuts import render
import json
from django.http import JsonResponse



# Create your views here.
def map(request):
    with open("C:/Users/ADMIN/OneDrive/Desktop/TIL/Python/Django/Practice/map/map_test/parkdata.json", encoding="utf-8") as file:
        park_data = json.load(file)
        parks = park_data["records"]
        park_info = []
        for park in parks:
            context = {
                "lat": park['위도'],
                "long": park['경도'],
                "addr": park['소재지지번주소'],
                "name": park['공원명'],
            }
            park_info.append(context)

        parkJson = json.dumps(park_info, ensure_ascii=False)
    return render(request, "map/map.html", {'parkJson': parkJson})

def map_locate(request):
    return JsonResponse()

def map2(request):
    return render(request, 'map2.html')