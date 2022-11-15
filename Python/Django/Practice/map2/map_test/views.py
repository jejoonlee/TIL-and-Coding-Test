from django.shortcuts import render
from django.http import JsonResponse
from .models import Map
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
    return render(request, 'map/map.html')

@query_debugger
def map_search(request, x, y):
    parks = Map.objects.all()
    parkJson = []

    for park in parks:
        parkJson.append({
            'name' : park.parkNm,
            'addr' : park.lnmadr,
            'lat' : park.latitude,
            'long': park.longitude,

        })

    data = {
        'parkJson': parkJson,
    }
    return JsonResponse(data)