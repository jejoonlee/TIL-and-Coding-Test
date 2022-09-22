from django.shortcuts import render
import random

# Create your views here.

# request ==> 요청한 사람의 정보가 들어온다 
def index(request):

  names = ['이제준', 'Alex', 'Google', 'Naver', 'Instagram']
  name = random.choice(names)

  context = {
    'name' : name,
    'img' : 'https://mblogthumb-phinf.pstatic.net/20140717_84/koshablog_1405555375597zsVq8_JPEG/156088.jpg?type=w2',
  }

  # 환영하는 메인 페이지를 보여준다
  # HTML 파일을 render을 통해 보낸다
  return render(request, 'index.html',context)
  # request = URL / 'index.html' = template / context = dictionary

def welcome(request, name):
  # 사람들이 /welcome/본인이름/ 을 입력하면, 환영 인사와 이름을 동시에 보여준다
  # name은 url/welceom/<name>/ 이라는 사용자들의 입력값

  context = {
    'name' : name,
    'greetings' : ['안녕하세요', 'bonjour', 'hello'],
    'img' : 'https://mblogthumb-phinf.pstatic.net/20140717_84/koshablog_1405555375597zsVq8_JPEG/156088.jpg?type=w2',
  }

  return render(request, 'welcome.html', context)