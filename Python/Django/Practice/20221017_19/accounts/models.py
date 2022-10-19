from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
  gender_choice = (
    ('Male', 'Male'),
    ('Female', 'Female')
  )

  gender = models.CharField(max_length=10, choices=gender_choice)
  profile_pic = models.ImageField(upload_to='profile_pic', default='no_profile_pic.png')
  pass
