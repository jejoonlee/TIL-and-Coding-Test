from . import views
from django.urls import path

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index')
]