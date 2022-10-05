from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.

# article/ 을 불러왔을 때, index.html을 넘겨준다
def index(request):
  # index.html에는 생성, 변경, 삭제 url로 연결해주는 버튼들이 있다
  # 그리고 index.html은 보기 기능도 있다 (데이터들을 생성/저장하면, index.html에서 보이게 한다)

  context = {
    'reviews': Article.objects.all().order_by('-updated_at'),
  } 
   
  return render(request, 'article/index.html', context)

# article/create/ 라는 요청이 url로 들어왔을 때에,
# create라는 함수로 해당 요청을 처리한다
def create(request):
  # 요청 메서드가 POST으면 사용자가 입력한 값을 가지고 온다
  if request.method == 'POST':
    article_form = ArticleForm(request.POST)

    # 입력한 값이 유효할 때만 Article DB에 저장을 한다
    # 저장 후 바로 index 페이지로 이동한다
    # redirect 덕분에 HTML <form> action에 공백처리를 해도 된다
    if article_form.is_valid():
      article_form.save()
      return redirect('article:index')

  # 요청 메서드가 GET일 경우 ModelForm을 가지고온다
  else:
    article_form = ArticleForm()

  # 입력한 값이 유효하지 않을 경우 에러메세지와 ModelForm을 가지고 오고
  # 메서드가 GET일 경우 ModelForm을 HTML 문서를 통해 보여준다
  context = {
    'article_form' : article_form,
  }

  return render(request, 'article/create.html', context)

# 데이터를 삭제하기 위해서는 특정 데이터를 가지고 와야한다
# 그러기 위해 특정 데이터의 pk값을 url로 가지고 온다
def delete(request, pk):

  # url을 통해 가지고 온 pk값을 DB의 pk값과 일치시킨다
  review = Article.objects.get(pk=pk)
  # .delete()을 통해 특정 데이터를 삭제한다
  review.delete()

  return redirect('article:index')

# create와 똑같은 로직이다
# 다만 edit에서는 특정 데이터를 인스턴스로 가지고 와야 한다
def edit(request, pk):
  # 특정 데이터를 가지고 오기. url에서 가지고 온 pk와 DB의 pk를 일치시키기
  review = Article.objects.get(pk=pk)
  if request.method == 'POST':
    # 위에 url에서 가지고 온 pk와 DB의 pk를 일치시킨 review를 instance=review
    # 를 통해 ModelForm에서 인스턴스로 가지고 온다
    article_form = ArticleForm(request.POST, instance=review)

    if article_form.is_valid():
      article_form.save()
      return redirect('article:index')

  else:
    article_form = ArticleForm(instance=review)
    
  context = {
    'article_form' : article_form,
  }

  return render(request, 'article/edit.html', context)