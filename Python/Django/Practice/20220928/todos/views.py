from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):

  # DB에 저장된 데이터 가지고 오기
  todo = Todo.objects.all().order_by('-priority')
  context = {
    'todo' : todo,
  }

  return render(request, 'todos/index.html', context)

def create(request):
  # DB에 입력한 데이터 저장하기

  title = request.GET.get('title')
  content = request.GET.get('content')
  priority = request.GET.get('priority')
  dday = request.GET.get('dday')

  Todo.objects.create(title=title, content=content, priority=priority, deadline=dday)

  return redirect('todos:index')

def delete(request, pk):

  todo = Todo.objects.get(id=pk)
  todo.delete()

  return redirect('todos:index')

def complete(request, pk):
  complete = Todo.objects.get(id=pk)

  if complete.completed == False:
    complete.completed = True
    complete.save()
  elif complete.completed == True:
    complete.completed = False
    complete.save()

  return redirect('todos:index')

# edit 수정하는 곳
def edit(request,pk):

  context = {
    'post' : Todo.objects.get(id=pk),
  }

  return render(request, 'todos/edit.html', context)

# update 수정
# request.GET.get으로 입력한 값들 가지고 오기
# todos/edit/14/?content=%EC%95%88%EB%85%95&priority=3&dday=2022-09-30
def update(request, pk):
  title = request.GET.get('edit_title')
  content = request.GET.get('edit_content')
  priority = request.GET.get('edit_priority')
  deadline = request.GET.get('edit_dday')

  post = Todo.objects.get(id=pk)

  post.title = title
  post.content = content
  post.priority = priority
  post.deadline = deadline
  post.save()

  return redirect('todos:index')

# detail 페이지
def detail(request, pk):

  context = {
    'allposts' : Todo.objects.all().order_by('-priority'),
    'post' : Todo.objects.get(id=pk)
  }

  return render(request, 'todos/detail.html', context)