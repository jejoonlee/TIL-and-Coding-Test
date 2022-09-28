from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):

    # 모든 글 목록을 가지고 오기
    posts = Post.objects.all()

    context = {
        "posts": posts,
    }

    return render(request, "posts/index.html", context)


def new(request):
    return render(request, "posts/new.html")


def create(request):
    # DB에 저장
    # parameter로 날라온 데이터를 DB에 저장
    title = request.GET.get("title")
    content = request.GET.get("content")

    context = {
        "title": title,
        "content": content,
    }

    Post.objects.create(title=title, content=content)

    return redirect("posts:index")


def delete(request, pk):

    post = Post.objects.get(id=pk)
    post.delete()

    return redirect("posts:index")
