from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review

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
      review_form.save()
      return redirect('article:index')

  else:
    review_form = ReviewForm()
  context = {
    'review_form': review_form,
  }
  return render(request, 'article/create.html', context)

def detail(request, pk):
  context = {
    'review' : Review.objects.get(pk=pk),
  }
  return render(request, 'article/detail.html', context)

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