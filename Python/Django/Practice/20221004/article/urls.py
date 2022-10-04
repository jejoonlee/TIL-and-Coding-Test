from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('delete/<int:pk>/', views.delete, name='delete'),
  path('<int:pk>/', views.detail, name='detail'),
  path('<int:pk>/edit/', views.edit, name='edit')
]