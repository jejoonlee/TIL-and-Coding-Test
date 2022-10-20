from django.shortcuts import render, redirect
from .forms import UserCustomForm, UserCustomChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
  if not request.user.is_authenticated:
    if request.method == "POST":
      signup_form = UserCustomForm(request.POST, request.FILES)
      if signup_form.is_valid():
        signup = signup_form.save()
        auth_login(request, user=signup)
        return redirect('articles:index')
    else:
      signup_form = UserCustomForm()
    context = {
      'signup_form': signup_form,
    }
    return render(request, 'accounts/signup.html', context)
  else:
    return redirect('articles:index')

def login(request):
  if request.method == "POST":
    login_form = AuthenticationForm(request, data=request.POST)
    if login_form.is_valid():
      auth_login(request, login_form.get_user())
      return redirect(request.GET.get('next') or 'articles:index')
  else:
    login_form = AuthenticationForm()
  context = {
    'login_form': login_form,
  }
  return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
  auth_logout(request)
  return redirect('articles:index')

def profile(request, pk):
  user = get_user_model().objects.get(pk=pk)
  context = {
    'user': user,
  }

  return render(request, 'accounts/profile.html', context)

@login_required
def update(request, pk):
  user = get_user_model().objects.get(pk=pk)
  if request.user == user:
    if request.method == "POST":
      update_form = UserCustomChangeForm(request.POST, request.FILES, instance=user)
      if update_form.is_valid():
        update = update_form.save()
        auth_login(request, user=update)
        return redirect('accounts:profile', user.pk)
    else:
      update_form = UserCustomChangeForm(instance=user)
    context = {
      'update_form': update_form,
    }
    return render(request, 'accounts/update.html', context)
  
  else:
    return redirect('articles:index')
