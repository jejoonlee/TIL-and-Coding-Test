from django.shortcuts import render, redirect
from articles.forms import ReviewForm
from .models import Review
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
  context= {
    'reviews': Review.objects.all()
  }
  return render(request, 'articles/index.html', context)

@login_required
def create(request):
  if request.method == 'POST':
    form = ReviewForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('articles:index')

  else:
    form = ReviewForm()
  
  context = {
    'form': form,
  }
  return render(request, 'articles/create.html', context)

def detail(request, pk):
  context = {
    'review': Review.objects.get(pk=pk)
  }
  return render(request, 'articles/detail.html', context)

def delete(request, pk):
  Review.objects.get(pk=pk).delete()
  return redirect('articles:index')

def update(request, pk):

  review = Review.objects.get(pk=pk)

  if request.method == 'POST':
    form = ReviewForm(request.POST, instance=review)
    if form.is_valid():
      form.save()
      return redirect('articles:detail', review.pk)

  else:
    form = ReviewForm(instance=review)
  context = {
    'form' : form,
    'index' : review.pk,
  }

  return render(request, 'articles/update.html',context)