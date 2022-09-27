from django.shortcuts import render
from .models import Article

# contents = []


# Create your views here.
def index(request):

  contents = Article.objects.all()

  context = {
    'saved' : contents,
  }

  return render(request, 'articles/index.html', context)

def create(request):

  content = request.GET.get('content')

  context = {
    'content' : content,
  }

  Article.objects.create(content=content)

  # contents.append(content)

  return render(request, 'articles/create.html', context)