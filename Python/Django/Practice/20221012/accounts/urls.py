from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
  path('', views.index, name='index'),
  path('register/', views.register, name='register'),
  path('<int:pk>/detail/', views.detail, name='detail'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
]