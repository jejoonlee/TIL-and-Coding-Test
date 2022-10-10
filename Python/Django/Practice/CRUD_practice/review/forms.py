from django import forms
from .models import Team, Uniform

class TeamForm(forms.ModelForm):
  class Meta:
    model = Team
    fields = '__all__'

class UniformForm(forms.ModelForm):
  class Meta:
    model = Uniform
    fields = fields = '__all__'
    exclude = ('team_pk',)