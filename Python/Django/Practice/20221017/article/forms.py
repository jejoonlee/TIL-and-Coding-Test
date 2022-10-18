from .models import Review, Comment
from django import forms

class ReviewForm(forms.ModelForm):

  class Meta:
    model = Review
    fields = '__all__'
    exclude=['user']

    labels = {
      'movie_title': '영화 제목',
      'title': '리뷰 제목',
      'content': '내용 작성',
      'image': '사진 첨부',
      'grade': '별점',
    }

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['content']

    labels = {
      'content' : '댓글 쓰기',
    }

    widgets = {
      'content': forms.Textarea(attrs={'class': 'form-control'}),
    }