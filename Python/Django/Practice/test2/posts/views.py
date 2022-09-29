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

# 상세 내용
def detail(request, pk):

    context = {
        'detail' : Post.objects.get(id=pk),
    }

    return render(request, 'posts/detail.html', context)

# Update은 edit과 update 페이지가 있어야 함
def edit(request, pk):

    context = {
        'edit' : Post.objects.get(id=pk),
    }

    return render(request, 'posts/edit.html', context)

def update(request, pk):
    new_title = request.GET.get('title_edit')
    new_content = request.GET.get('content_edit')

    post = Post.objects.get(id=pk)

    # 수정 후 저장
    post.title = new_title
    post.content = new_content
    post.save()

    return redirect('posts:detail', post.pk)