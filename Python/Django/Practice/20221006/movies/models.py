from django.db import models

# Create your models here.
class Movies(models.Model):
  movie_title = models.CharField(max_length=80)
  title = models.CharField(max_length=40)
  summary = models.TextField()
  running_time = models.IntegerField(default=0)
  image = models.ImageField(null=True, blank=True, upload_to='cover/')
  # 저장경로 : MEDIA_ROOT/cover/xxxx.jpg 경로에 저장
	# DB필드 : 'MEDIA_URL/cover/xxxx.jpg' 문자열 저장
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)