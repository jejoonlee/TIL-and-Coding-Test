from django.urls  import path
from . import views

app_name = 'article'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('<int:pk>/', views.detail, name='detail'),
  path('<int:pk>/update/', views.update, name='update'),
  path('<int:pk>/delete/', views.delete, name='delete'),
  path('comment_create/<int:pk>/', views.comment_create, name='comment_create'),
  path('comment_delete/<int:pk>/<int:detail_pk>', views.comment_delete, name='comment_delete'),
]