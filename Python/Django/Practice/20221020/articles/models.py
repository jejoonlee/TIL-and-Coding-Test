from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Review(models.Model):
  sports_choice = (
    ('Football', 'Football'),
    ('Basketball', 'Basketball'),
    ('American Football', 'American Football'),
    ('Baseball', 'Baseball'),
    ('Others', 'Others')
  )

  rating_choice = (
    ('1', '⭐'),
    ('2', '⭐⭐'),
    ('3', '⭐⭐⭐'),
    ('4', '⭐⭐⭐⭐'),
    ('5', '⭐⭐⭐⭐⭐'),
  )

  review_title = models.CharField(max_length=100)
  sports = models.CharField(max_length=50, choices=sports_choice)
  match_title = models.CharField(max_length=100)
  match_info = models.TextField()
  rating = models.CharField(max_length=50, choices=rating_choice)
  match_date = models.DateField()
  image = models.ImageField(upload_to='image/article_image', default='no_img.png')
  image_thumbnail = ImageSpecField(source='image',
                                  processors=[ResizeToFill(295, 295)],
                                  format='JPEG',
                                  options={'quality': 80})
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

class Comment(models.Model):
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
  review = models.ForeignKey(Review, on_delete=models.CASCADE)