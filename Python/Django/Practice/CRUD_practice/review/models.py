from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Team(models.Model):
  nationality = models.CharField(max_length = 100)
  team_name = models.CharField(max_length = 60)
  logo = models.ImageField(blank=True, upload_to='image/logo/')

class Uniform(models.Model):
  # on_delete=models.CASCADE 은 만약 위에 Team 모델이 지워지면, 그에 해당하는 모든 uniform의 정보들이 지워지는 것이다
  # on_delete=models.SET_NULL, Team 모델에서, 하나의 팀이 지워지면, 그에 연관된 모든 uniform의 team 정보들은 NULL 값으로 변경된다
  team_pk = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, db_column='team_pk')
  season = models.CharField(max_length = 60)
  price = models.IntegerField()
  rating = models.IntegerField()
  content = models.TextField(validators=[MinValueValidator(0), MaxValueValidator(5)])
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  picture = models.ImageField(blank=True, upload_to='image/uniform')