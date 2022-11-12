from django.urls import path, include
from . import views

app_name = 'map'

urlpatterns = [
    path('map/', views.map, name="map")
]