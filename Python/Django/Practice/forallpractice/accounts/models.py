from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  gender_choice = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
  )

  gender = models.CharField(max_length=6, choices=gender_choice)
  profile_img = models.ImageField(upload_to='image/profile_pic', default='no_profile_pic.png')
  following = models.ManyToManyField('self', symmetrical=False, related_name='follower')
  pass