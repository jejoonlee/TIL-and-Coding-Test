from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:pk>/detail/', views.detail, name='detail'),
  path('register/', views.register, name='register'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('update/', views.update, name='update'),
  path('detail_update/<int:pk>', views.detail_update, name='detail_update'),
  path('profile/', views.profile, name='profile'),
  path('warning/', views.warning, name='warning'),
  path('delete/', views.delete, name='delete'),
  path('password/', views.password, name='password'),
]