from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm

class CustomUserForm(UserCreationForm):

  class Meta:
    model = get_user_model()
    fields = [
      'username', 
      'password1', 
      'password2',
      'last_name',
      'first_name',
      'gender',
      'email',
      ]

class CustomUserChangeForm(UserChangeForm):
  password=None
  class Meta:
    model = get_user_model()
    fields = [
      'last_name',
      'first_name',
      'gender',
      'email',
      ]
    exclude = ['password']

class CustomPasswordChangeForm(PasswordChangeForm):
  class Meta:
    pass