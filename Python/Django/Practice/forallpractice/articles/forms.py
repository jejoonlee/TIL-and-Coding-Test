from .models import Review, Comment
from django import forms

class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = [
      'review_title',
      'sports',
      'match_title',
      'rating',
      'match_date',
      'match_info',
      'image',
    ]

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = [
      'content',
    ]