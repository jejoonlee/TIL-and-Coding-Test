from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

class UserCustomForm(UserCreationForm):
  class Meta:
    model = get_user_model()
    fields = [
      'username',
      'password1',
      'password2',
      'first_name',
      'last_name',
      'email',
      'gender',
      'profile_img',
    ]

class UserCustomChangeForm(UserChangeForm):
  password=None
  class Meta:
    model = get_user_model()
    fields = [
      'username',
      'first_name',
      'last_name',
      'email',
      'gender',
      'profile_img',
    ]