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

  content = request.GET.get('content')
  priority = request.GET.get('priority')
  dday = request.GET.get('dday')

  Todo.objects.create(content=content, priority=priority, deadline=dday)

  return redirect('todos:index')

def delete(request, pk):

  todo = Todo.objects.get(id=pk)
  todo.delete()

  return redirect('todos:index')

def complete(request, pk):
  complete = Todo.objects.get(id=pk)
  complete.completed = True
  complete.save()

  return redirect('todos:index')