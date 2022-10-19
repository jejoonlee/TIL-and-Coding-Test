from django.shortcuts import render,redirect
from .models import User
from .forms import UserCustomForm, UserCustomChangeForm, CustomPasswordChangeForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
  if request.user.is_superuser:
    return render(request, 'accounts/index.html')
  else:
    return redirect('article:index')

def profile(request, pk):
  user = User.objects.get(pk = pk)
  reviews = user.review_set.all()
  context = {
    'profile': user,
    'reviews' : reviews,
  }
  return render(request, 'accounts/profile.html', context)

def signup(request):
  if request.method == 'POST':
    signup_form = UserCustomForm(request.POST, request.FILES)
    if signup_form.is_valid():
      signup = signup_form.save()
      auth_login(request, user=signup)
      messages.success(request, '성공적으로 회원가입을 하셨습니다!')
      return redirect('article:index')
  else:
    signup_form = UserCustomForm()
  context = {
    'signup_form': signup_form,
  }
  return render(request, 'accounts/signup.html', context)

def login(request):
  if request.method == 'POST':
    login_form = AuthenticationForm(request, data=request.POST)
    if login_form.is_valid():
      auth_login(request, login_form.get_user())
      return redirect(request.GET.get('next') or 'article:index')
  else:
    login_form = AuthenticationForm()
  context = {
    'login_form' : login_form,
  }
  return render(request, 'accounts/login.html', context)

def logout(request):
  auth_logout(request)
  return redirect('article:index')

@login_required
def update(request, pk):
  if request.user.pk == pk:
    
    if request.method == 'POST':
      change_form = UserCustomChangeForm(request.POST, request.FILES, instance=request.user)
      if change_form.is_valid():
        change = change_form.save()
        auth_login(request, user=change)
        return redirect('accounts:profile', request.user.pk)
    else:
      change_form = UserCustomChangeForm(instance=request.user)
    
    context = {
      'change_form': change_form,
    }

    return render(request, 'accounts/update.html', context)
  
  else:
    return redirect('article:index')

@login_required
def delete(request):
  request.user.delete()
  return redirect('articles:index')

@login_required
def password_update(request):
  if request.method == 'POST':
    password_form = CustomPasswordChangeForm(request.POST, request.user)
    if password_form.is_valid():
      user = password_form.save()
      auth_login(request, user)
      return redirect('accounts:update', request.user.pk)
  else:
    password_form = CustomPasswordChangeForm(request.user)

  context = {
    'password_form': password_form,
  }
  
  return render(request, 'accounts/password.html', context)