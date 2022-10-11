from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns=[
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('<int:pk>/profile/', views.profile, name='profile'),
  path('<int:pk>/delete/', views.delete, name='delete'),
]