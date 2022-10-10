from django.shortcuts import render, redirect
from .models import Team, Uniform
from .forms import TeamForm, UniformForm

# Create your views here.
def index(request):
  return render(request, 'review/index.html')

def create_review(request):

  teams = Team.objects.all().order_by('team_name')

  if request.method == "POST":
    uniform_form = UniformForm(request.POST)
    if uniform_form.is_valid():
      uniform_form.save()
      return redirect('review:index')
  else:
    uniform_form = UniformForm()

  context = {
    'uniform_form': uniform_form,
    'teams': teams,
  }

  return render(request, 'review/create_review.html', context)

def create_team(request):
  if request.method == "POST":
    team_form = TeamForm(request.POST)
    if team_form.is_valid():
      team_form.save()
      return redirect('review:create_review')
  else:
    team_form = TeamForm()

  context = {
    'team_form': team_form,
  }
  return render(request, 'review/create_team.html', context)