
from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
  path('', views.index, name='index'),
  path('create_review/', views.create_review, name='create_review'),
  path('create_team/', views.create_team, name='create_team'),
]