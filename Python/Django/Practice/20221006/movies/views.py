from django.shortcuts import render, redirect
from .models import Movies
from .forms import MoviesForm

# Create your views here.
# index 페이지
def index(request):
  context = {
    'reviews' : Movies.objects.all(),
  }
  return render(request, 'movies/index.html', context)


def create(request):
  if request.method == 'POST':
    movies_form = MoviesForm(request.POST)

    if movies_form.is_valid():
      movies_form.save()
      return redirect('movies:index')

  else:
    movies_form = MoviesForm()

  context={
    'movies_form' : movies_form,
  }
  return render(request, 'movies/create.html', context)

def detail(request, pk):
  context = {
    'review' : Movies.objects.get(pk=pk),
  }
  return render(request, 'movies/detail.html', context)


def delete(request,pk):
  Movies.objects.get(pk=pk).delete()
  return redirect('movies:index')


def update(request,pk):
  movie = Movies.objects.get(pk=pk)

  if request.method == "POST":
    movies_form = MoviesForm(request.POST, instance=movie)

    if movies_form.is_valid():
      movies_form.save()
      return redirect('movies:detail', movie.pk)

  else:
    movies_form = MoviesForm(instance=movie)
  context = {
    'index': movie.pk,
    'movies_form': movies_form,
  }
  return render(request, 'movies/update.html', context)