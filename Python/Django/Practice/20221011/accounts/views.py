from django.shortcuts import render,redirect
# from .models import User
from django.contrib.auth import get_user_model
from .forms import UserForm

# Create your views here.

def index(request):
  context = {
    'users': get_user_model().objects.all(),
  }
  return render(request, 'accounts/index.html', context)

def create(request):
  if request.method == "POST":
    user_form = UserForm(request.POST)

    if user_form.is_valid():
      user_form.save()
      return redirect('accounts:index')
  
  else:
    user_form = UserForm()

  context = {
    'user_form' : user_form,
  }

  return render(request, 'accounts/create.html', context)

def profile(request, pk):
  context = {'user' : get_user_model().objects.get(pk=pk)}
  return render(request, 'accounts/profile.html', context)

def delete(request, pk):
  get_user_model().objects.get(pk=pk).delete()
  return redirect(request, 'accounts/index.html')