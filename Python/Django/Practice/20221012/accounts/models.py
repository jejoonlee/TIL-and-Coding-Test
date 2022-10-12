from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  gender_choice = (
    ('M', 'Male'),
    ('F', 'Female')
  )
  gender = models.CharField(max_length=10, choices=gender_choice)