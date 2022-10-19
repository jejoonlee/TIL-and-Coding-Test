from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.conf import settings

# Create your models here.
class Review(models.Model):
  grade_choice = (
    ('1','⭐'),
    ('2','⭐⭐'),
    ('3','⭐⭐⭐'),
    ('4','⭐⭐⭐⭐'),
    ('5','⭐⭐⭐⭐⭐'),
  )

  title = models.CharField(max_length=100)
  movie_title = models.CharField(max_length=100)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  content = models.TextField()
  grade = models.CharField(max_length=2, choices=grade_choice, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  image = models.ImageField(upload_to='media', default='no_image.jpg')
  thumbnail = ImageSpecField(source='image',
                            processors=[ResizeToFill(295, 295)],
                            format='JPEG',
                            options={'quality': 80})


class Comment(models.Model):
  content = models.TextField()
  updated_at = models.DateTimeField(auto_now=True)
  review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)