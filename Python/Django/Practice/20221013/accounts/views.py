from django.shortcuts import render, redirect
from .forms import CustomUserForm, CustomUserChangeForm, CustomPasswordChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# 목록 페이지 (superuser만 접속 가능)
@login_required
def index(request):
  if request.user.is_superuser:
    context = {
      'users' : get_user_model().objects.all()
    }
    return render(request, 'accounts/index.html', context)
  else:
    return redirect('accounts:warning')

# 목록 페이지 통해 건너가는 계정의 디테일 페이지 (superuser만 접속 가능)
@login_required
def detail(request, pk):
  if request.user.is_superuser:
    user = get_user_model().objects.get(pk=pk)
    context = {
      'user' : user,
      'num' : user.pk,
    }
    return render(request, 'accounts/detail.html', context)
  else:
    return redirect('accounts:warning')


# 디테일 페이지에서 해당 계정을 수정하고 싶을 때
def detail_update(request, pk):
  if request.user.is_superuser:
    user = get_user_model().objects.get(pk=pk)
    if request.method == 'POST':
      update_form = CustomUserChangeForm(request.POST, instance=user)
      if update_form.is_valid():
        update_form.save()
        return redirect('accounts:index')
    else:
      update_form = CustomUserChangeForm(instance=user)
    context = {
      'update_form' : update_form,
    }
    return render(request, 'accounts/detail_update.html', context)
  else:
    return redirect('articles:index')


# 슈퍼유저가 아닌데, 페이지를 들어가면 나오는 페이지
def warning(request):
  return render(request, 'accounts/warning.html')


# 회원가입 페이지
def register(request):
  if request.method == 'POST':
    register_form = CustomUserForm(request.POST)
    
    if register_form.is_valid():
      user = register_form.save()
      auth_login(request, user)
      return redirect('articles:index')

  else:
    register_form = CustomUserForm()
  
  context = {
    'register_form': register_form,
  }

  return render(request, 'accounts/register.html', context)

# 로그인 페이지
def login(request):
  if request.method == 'POST':
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

# 로그아웃 
def logout(request):
  auth_logout(request)
  return redirect('articles:index')

# 로그인 후, 자신의 프로필을 들어감
@login_required
def profile(request):
  return render(request, 'accounts/profile.html')

# 자신의 프로필을 들어가, 정보를 수정
@login_required
def update(request):
  if request.method == 'POST':
    update_form = CustomUserChangeForm(request.POST, instance=request.user)
    if update_form.is_valid():
      update_form.save()
      return redirect('accounts:profile')
  else:
    update_form = CustomUserChangeForm(instance=request.user)
  context = {
    'update_form': update_form,
  }

  return render(request, 'accounts/update.html', context)


# 회원 탈퇴
def delete(request):
  request.user.delete()
  return redirect('articles:index')


# 비밀번호 변경
@login_required
def password(request):
  if request.method == 'POST':
    password_form = CustomPasswordChangeForm(request.user, request.POST)
    if password_form.is_valid():
      user = password_form.save()
      auth_login(request, user)
      return redirect('accounts:profile')
  else:
    password_form = CustomPasswordChangeForm(request.user)
  context = {
    'password_form' : password_form,
  }
  return render(request, 'accounts/password.html', context)