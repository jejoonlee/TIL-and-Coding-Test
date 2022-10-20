from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm, CommentForm
from .models import Review, Comment

# Create your views here.
def index(request):
  context = {
    'reviews': Review.objects.all().order_by('-updated_at'),
  }
  return render(request, 'articles/index.html', context)

@login_required
def create(request):
  if request.method == "POST":
    review_form = ReviewForm(request.POST, request.FILES)
    if review_form.is_valid():
      review = review_form.save(commit=False)
      review.user = request.user
      review.save()
      return redirect('articles:index')
  else:
    review_form = ReviewForm()
  context = {
    'review_form': review_form,
  }
  return render(request, 'articles/create.html', context)

@login_required
def detail(request, pk):
  review = Review.objects.get(pk=pk)
  context = {
    'review': review,
  }
  return render(request, 'articles/detail.html', context)

@login_required
def update(request, pk):
  review = Review.objects.get(pk=pk)

  if request.user == review.user:
    if request.method == "POST":
      update_form = ReviewForm(request.POST, request.FILES, instance=review)
      if update_form.is_valid():
        review = update_form.save(commit=False)
        review.user = request.user
        review.save()
        return redirect('articles:detail', review.pk)
    else:
      update_form = ReviewForm(instance=review)

    context = {
      'num' : review.pk,
      'update_form': update_form,
    }
    return render(request, 'articles/update.html', context)

  else:
    return redirect('articles:index')

@login_required
def delete(request, pk):
  review = Review.objects.get(pk=pk)

  if review.user == request.user:
    review.delete()
    return redirect('article:index')
  
  else:
    return redirect('article:index')