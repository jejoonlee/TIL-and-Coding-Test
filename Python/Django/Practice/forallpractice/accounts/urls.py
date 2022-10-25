from django.urls import path 
from . import views

app_name = 'accounts'

urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('<int:pk>/profile/', views.profile, name='profile'),
  path('<int:pk>/update/', views.update, name='update'),
  path('<int:pk>/password_change/', views.password_change, name='password_change'),
  path('<int:pk>/delete', views.delete, name='delete'),
  path('<int:pk>/follow/', views.follow, name='follow'),
]