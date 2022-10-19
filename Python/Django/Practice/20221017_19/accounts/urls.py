from django.urls import path 
from . import views

app_name = 'accounts'

urlpatterns = [
  path('', views.index, name='index'),
  path('signup/', views.signup, name='signup'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('<int:pk>/profile/', views.profile, name='profile'),
  path('<int:pk>/update/', views.update, name='update'),
  path('delete/', views.delete, name='delete'),
  path('password_update/', views.password_update, name='password_update'),
]