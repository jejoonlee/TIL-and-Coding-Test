from django.shortcuts import render,redirect
from .models import User
from .forms import UserCustomForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def index(request):
  return render(request, 'accounts/index.html')

def profile(request, pk):
  user = User.objects.get(pk=pk)
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
      signup_form.save()
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
      return redirect('article:index')
  else:
    login_form = AuthenticationForm()
  context = {
    'login_form' : login_form,
  }
  return render(request, 'accounts/login.html', context)

def logout(request):
  auth_logout(request)
  return redirect('article:index')