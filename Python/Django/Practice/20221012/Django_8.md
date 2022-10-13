# 📋Django 10, 11

#### Category

[Django Auth](#%EF%B8%8F-django-auth)

[회원가입](#%EF%B8%8F-회원가입)

[로그인](#%EF%B8%8F-로그인)



## ✔️ Django Auth

> Django authorization system
>
> 인증 (Authentication) : 신원 확인 / 사용자가 자신이 누구인지 확인
>
> 권한 (Authorization) : 권한 부여

인증과 권한 기능은 장고 내부에 이미 구현이 되어 있다 (예. Admin 페이지)

- ​	`User` / `권한 및 그룹` / `암호 해시 시스템` / `Form 및 View 도구` / `기타 적용가능한 시스템`



## ✔️ 회원가입

> django에서 제공하는 기본적인 `User Model`을 사용하게 되면 사용할 수 있는 필드들이 제한이 된다
>
> - `username` : 로그인 할 때에 필요한 username (글자수 150개로 제한)
> - `first_name` :  150 글자수로 제한된 이름 (optional / blank=True)
> - `last_name` :  150 글자수로 제한된 성 (optional / blank=True)
> - `email` : 이메일 (optional / blank=True)
> - `password` : 비밀번호 / 암호화가 되어 hash로 저장된다
>   - 비밀번호 같은 경우 암호화 되어 저장되지만, 암호화 된 것을 비밀번호로 바꿀 수 없다
>   - 암호화한 것을 원래 비밀번호로 바꾸게 되는 경우 비밀번호의 역할을 못 하는 것
> - `groups` : 서비스에 주어진 그룹에 속해있는지
> - `user_permissions` : 서비스에서 주어진 권한들을 가지고 있는지
> - `is_staff` : user가 admin 페이지를 사용할 수 있는지 없는지 권한을 주는 것
> - `is_active` : 참/거짓 (계정을 활성화 또는 비활성화)
> - `is_superuser` : 참/거짓 (웹 서비스 관련, 모든 것을 관여할 수 있음)
> - `last_login` : 마지막으로 로그인을 한 날짜/시간
> - `date_joined` : 회원가입을 한 날짜/시간
>
> 위에 있는 내용보다 더 추가적인 내용을 회원가입을 통해 알고 싶을 때에는 `custom user model`을 사용하게 된다
>
> 그래서 주로 시작할 때에도 `custom user model`을 이용한다



> ### 기본적으로 회원 정보를 관리하는 어플리케이션을 만든다

![회원가입2](Django_8.assets/회원가입2.png)



![회원가입3](Django_8.assets/회원가입3.png)

> #### 📌 `from .models import user` 는 `from django.contrib.auth import get_user_model` 로 바꾼다



## ✔️ 로그인

> import을 통해서 로그인 관련된 기능들을 가지고 온다
>
> `from django.contrib.auth import login`
>
> `from django.contrib.auth import logout`
>
> `from django.contribe.auth.forms import AuthenticationForm`

![로그인1](Django_8.assets/로그인1.png)



> `request.user.is_authenticated` 라는 것을 사용하여, 로그인이 된 상태면, 어떤 기능을 쓸 수 있도록 가능하게 해준다

```python
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            auth_login(form, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
        	# 로그인을 할 경우 next 이후에 나오는 url로 이동하거나
            # next 이후에 url이 없으면 articles의 index 페이지로 이동하게 된다
    else:
    	form = AuthenticationForm()
    context = {
        'form' : form,
    }
    
    return render(request, 'accounts/login.html', context)
```



#### 회원가입 후 바로 로그인이 될 수 있도록 만들기

```python
from .forms import UserForm
from django.contrib.auth import login as auth_login

def register(request):
    if reqeust.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
# 저장된 인스턴스를 user로 저장하고
# 바로 auth_login에 가지고 와서 회원 가입을 하면
# 바로 로그인이 되도록 한다
        
    else:
        form = UserForm()
    context = {
        'form' : form,
    }
    
    return render(request, 'accounts/register.html', context)
```



#### 로그인을 해야하는 기능일 때에

```python
from django.shortcuts import render, redirect
from articles.forms import ReviewForm
from django.contrib.auth.decorators import login_required

# login_required를 가지고 오고, 로그인이 필요한 함수 위에 설정을 한다
@login_required
def create(request):
  if request.method == 'POST':
    form = ReviewForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('articles:index')

  else:
    form = ReviewForm()
  
  context = {
    'form': form,
  }
  return render(request, 'articles/create.html', context)
```

> `return redirect(request.GET.get('next') or 'articles:index')` 
>
> 로그인 함수에 로그인이 필요한 기능에 들어갔을 때에, 로그인을 했다면, url에 `next` 이후에 있는 url로 가도록 설정한다
