from django.shortcuts import render
import json
from django.http import JsonResponse
import functools, time
from django.db import connection, reset_queries
from django.conf import settings

def query_debugger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        reset_queries()
        number_of_start_queries = len(connection.queries)
        start  = time.perf_counter()
        result = func(*args, **kwargs)
        end    = time.perf_counter()
        number_of_end_queries = len(connection.queries)
        print(f"------------------------------------------------------")
        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {number_of_end_queries-number_of_start_queries}")
        print(f"Finished in : {(end - start):.2f}s")
        print(f"------------------------------------------------------")
        return result
    return wrapper


# Create your views here.
@query_debugger
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