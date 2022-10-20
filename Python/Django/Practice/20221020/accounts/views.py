from django.shortcuts import render, redirect
from .forms import UserCustomCreationForm
from django.contrib.auth import login as auth_login

# Create your views here.
def signup(request):
  if request.method == "POST":
    signup_form = UserCustomCreationForm(request.POST, request.FILES)
    if signup_form.is_valid():
      signup = signup_form.save
      auth_login(request, signup)
      return redirect('articles/index')
  else:
    signup_form = UserCustomCreationForm()
  context = {
    'signup_form': signup_form,
  }
  return render(request, 'accounts/signup.html', context)