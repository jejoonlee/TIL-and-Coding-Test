from django.contrib import admin
from .models import Review, Comment

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
  list_display = ['user', 'title', 'movie_title', 'content', 'grade']

class CommentAdmin(admin.ModelAdmin):
  list_display = ['user', 'review', 'content']

admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)