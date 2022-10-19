from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm

class UserCustomForm(UserCreationForm):
  class Meta:
    model = get_user_model()
    fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'gender', 'profile_pic']

class UserCustomChangeForm(UserChangeForm):
  password=None
  class Meta:
    model = get_user_model()
    fields = ['username', 'email', 'first_name', 'last_name', 'gender', 'profile_pic']

class CustomPasswordChangeForm(PasswordChangeForm):
  class Meta:
    pass