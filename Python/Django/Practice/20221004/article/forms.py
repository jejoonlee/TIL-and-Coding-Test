from django import forms
from .models import Review

class reviewForm(forms.ModelForm):

  class Meta:
    # models.py에 저장된 class 중 Review라는 DB를 가지고 온다
    model = Review
    # 필드는 모든 필드를 가지고 온다
    fields = '__all__'