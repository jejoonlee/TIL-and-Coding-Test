from django.shortcuts import render, redirect
from .forms import ReviewForm, CommentForm
from .models import Review, Comment

# Create your views here.
def index(request):
  context = {
    'reviews' : Review.objects.all(),
  }
  return render(request, 'article/index.html', context)

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

def comment_delete(request, pk, detail_pk):
  detail = Review.objects.get(pk=detail_pk)
  comment = Comment.objects.get(pk=pk)
  comment.delete()
  return redirect('article:detail', detail.pk)

def update(request, pk):
  review = Review.objects.get(pk=pk)
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

def delete(request, pk):
  Review.objects.get(pk=pk).delete()
  return redirect('article:index')