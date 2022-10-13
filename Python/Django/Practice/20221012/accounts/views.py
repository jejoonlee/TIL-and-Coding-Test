from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

from accounts.models import User
from .forms import UserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
      auth_login(request, form.get_user())
      return redirect(request.GET.get('next') or 'articles:index')
  
  else:
    form = AuthenticationForm()

  context={
    'form' : form,
  }

  return render(request, 'accounts/login.html', context)

def logout(request):
  auth_logout(request)
  return redirect('articles:index')


def register(request):
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      user = form.save()
      auth_login(request, user)
      return redirect('articles:index')
  else:
    form = UserForm()
  context = {
    'form': form,
  }

  return render(request, 'accounts/register.html', context)

@login_required
def index(request):
  context={
    'users': get_user_model().objects.all(),
  }
  return render(request, 'accounts/index.html', context)

def detail(request,pk):
  context={
    'user': get_user_model().objects.get(pk=pk)
  }
  return render(request, 'accounts/detail.html', context)
