# 🧑‍💻 2022년 10월 17일 ~ 19일 정리

## 기능 구현 설명

### ACCOUNTS

> 회원 가입부터, 로그인, 회원 정보 수정, 삭제 등을 구현했다

#### 회원 가입

> views.py

```python
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
```

- models.py에서 'User'라는 회원들 정보를 저장하는 모델을 만들었다
- 그리고 forms.py에 'UserCustomForm'을 만들어, 회원 가입용 폼을 만들었다
- 회원가입을 한 후, 바로 로그인이 가능할 수 있도록 `auth_login(request, user=signup)`을 넣었다
- 그리고 회원가입이 성공적으로 끝나면 메세지로 `messages.success(request, '성공적으로 회원가입을 하셨습니다!')` 를 띄우게 했다



#### 로그인/ 로그아웃

> views.py

```python
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
```

- 로그인 할 때에는 `AuthenticationForm`을 가지고 와야 한다
- 그리고 로그인/ 로그아웃 할 때에는 `login` 과 `logout` 모듈을 가지고 와야한다



#### 회원 정보 수정 / 삭제

> views.py

```python
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
```

- `if request.user.pk == pk:` 을 통해, 자신의 정보만 수정을 할 수 있도록 만들었다
- 회원 정보 수정은 forms.py에서 UserChangeForm을 가지고 와야한다
- 가지고 오면, 비밀번호 외에, 다른 목록들이 수정 될 수 있도록 나와있다



#### 비밀번호 수정

> views.py

```python
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
```

- 비밀번호도 forms.py에서 PasswordChangeForm을 가지고 와야 한다
- 비밀번호 변동 후, 계속 로그인을 유지하기 위해서 회원가입 때 처럼, `auth_login(request, user)`을 해준다

-------

## ARTICLE

사이트의 메인 기능이다. 리뷰 작성, 댓글 쓰기 등을 할 수 있다

#### 리뷰작성

> views.py

```python
@login_required
def create(request):
  if request.method == 'POST':
    review_form = ReviewForm(request.POST, request.FILES)
    if review_form.is_valid():
      review = review_form.save(commit=False)
      review.user = request.user
      review.save()
      return redirect('article:index')

  else:
    review_form = ReviewForm()
  context = {
    'review_form': review_form,
  }
  return render(request, 'article/create.html', context)
```

- `@login-required`를 통해, 로그인을 한 사람만 게시글을 작성 할 수 있도록 만들었다
- 사진을 자기고 오기 때문에, 원래 `request.POST`만 했는데, `request.FILES`까지 해준다
  - HTML `<form>`의 `enctype`에서 파일 형태로 입력되는 값들은 `request.FILES`로 만든다
- 원래 `review = review_form.save()`만 했어도 됐는데, `review` 인스턴스를 만들어, `review.user` 에 현제 로그인 한 유저(`request.user`)의 정보를 넣고, 저장을 했다



#### 리뷰 보기

> views.py

```python
def index(request):
  context = {
    'reviews' : Review.objects.all().order_by('-updated_at'),
  }
  return render(request, 'article/index.html', context)
```

- 리뷰 DB에 있는 모든 정보를 수정된 순으로 내림차순으로 정렬을 해서 가지고 온다



#### 리뷰 수정/삭제

> views.py

```python
@login_required
def update(request, pk):
  review = Review.objects.get(pk=pk)

  if review.user == request.user:
    if request.method == 'POST':
      update_form = ReviewForm(request.POST, request.FILES, instance=review)
      if update_form.is_valid():
        update_form.save()
        return redirect('article:detail', review.pk)
    else:
      update_form = ReviewForm(instance=review)
    context = {
      'update_form' : update_form,
      'num' : review.pk,
    }
    return render(request, 'article/update.html', context)
  else:
    return redirect('article:detail', review.pk)

@login_required
def delete(request, pk):
  review = Review.objects.get(pk=pk)
  if request.user == review.user:
    review.delete()
    return redirect('article:index')
  else:
    return redirect('article:detail', review.pk)
```





#### 리뷰 상세 페이지

> views.py

```python
@login_required
def detail(request, pk):
  review = Review.objects.get(pk=pk)
  # 댓글을 써야할 모델폼을 가지고 온다
  comment_form = CommentForm()

  # 댓글 보여주기 (최신 업로드 순으로)
  comments = review.comment_set.all().order_by('-updated_at')

  # 댓글 갯수
  comment_num = review.comment_set.all().count()

  context = {
    'review' : review,
    'comment_form': comment_form,
    'comments' : comments,
    'comment_num' : comment_num,
  }
  return render(request, 'article/detail.html', context)
```

- 상세 페이지에 댓글 기능을 넣었다
  - 따로 댓글 만들기 페이지를 안 만들고, `detail` 페이지에 댓글을 쓸 폼을 가지고 왔다
  - HTML에서는 form 태그의 action에 댓글 url로 가는 경로를 만들어 준다



#### 댓글 작성

> views.py

```python
@login_required
def comment_create(request, pk):
  review = Review.objects.get(pk=pk)
  if request.method == 'POST':
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
      comment = comment_form.save(commit=False)
      comment.review = review
      comment.user = request.user
      comment.save()
  return redirect('article:detail', review.pk)
```

- 댓글을 작성을 하는데, 댓글 안에 `review`의 ForeignKey와  `user`의 ForeignKey가 들어가야한다
  - 그래서 `comment`라는 인스턴스를 만들어준다
    - `comment.review` 안에 위에 가지고 온 review 인스턴스를 넣는다
      - `review = Review.objects.get(pk=pk)`
    - `comment.user`는 로그인한 사람 (request.user)의 정보를 넣는다



#### 그 외

> 이미지 같은 경우 저장은 알아서 되는데, 만약 이미지 또는 파일을 웹 서비스에서 삭제를 하려면 따로 설정을 해줘야 한다

```python
pip install django-cleanup
# 이미지 또는 파일이 삭제되었을 때, 로컬에 저장되어 있는 파일들도 지워준다

# settings.py
INSTALLED_APPS = (
    ...,
    'django_cleanup.apps.CleanupConfig',
)
```









