from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html')

def ping(request):
  return render(request, 'ping.html')

def pong(request):
  # request으로 할 수 있는 것을 search (터미널 내에서)
  print(dir(request))
  # request의 타입
  print(type(request))

  context = {
    'name' : request.GET.get('ball'),
  }
  return render(request, 'pong.html', context)