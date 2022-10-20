from django.contrib import admin
from .models import Review, Comment

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
  pass

class CommentAdmin(admin.ModelAdmin):
  pass

admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)