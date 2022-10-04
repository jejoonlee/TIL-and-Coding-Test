from django.shortcuts import render, redirect
from .forms import reviewForm
from .models import Review



# Create your views here.

# index 페이지에는 Review DB에 저장된 모든 데이터를 가지고 오고
# 수정한 날짜에 맞춰 오름차순으로 정렬을 한다
def index(request):
  context = {
    'reviews' : Review.objects.all().order_by('updated_at')
  }
  return render(request, 'article/index.html', context)


def create(request):
  # request 메서드가 POST일 경우
  if request.method == 'POST':
    # review_form에 reviewForm에서 request.POST를 통해 가지고 온 입력값을 저장한다
    review_form = reviewForm(request.POST)
    
    # review_form이 유효하면
    if review_form.is_valid():
      # review_form에 저장된 데이터를 Review DB에 저장한다
      review_form.save()
      return redirect('article:index')

  # request 메서드가 POST가 아닐 경우
  else:
    # review_form에 reviewForm이라는 ModelForm을 저장한다
    review_form = reviewForm()
  context = {
    'review_form' : review_form,
  }

  # 그리고 HTML 문서에 ModelForm을 사용할 수 있도록 context를 통해 보낸다
  return render(request, 'article/create.html', context)


# 삭제 버튼을 클릭한 특정 데이터의 pk값을 URL을 통해 가지고 온다
# 그리고 DB의 PK값과 일치를 시켜, .delete()를 통해 해당 데이터를 지운다
def delete(request, pk):
  Review.objects.get(id = pk).delete()
  return redirect('article:index')


# URL을 통해 버튼을 클릭한 데이터의 pk값을 가지고 온다
# 그 숫자를 Review DB의 pk값과 일치시킨 후, 
# 해당 pk값을 가진 데이터의 Detail 페이지로 이동한다
def detail(request, pk):
  context = {
    'review' : Review.objects.get(id=pk),
  }
  return render(request, 'article/detail.html', context)


# create와 똑같다
# 다른 점은 특정 데이터를 수정하는 것
# 그러기 위해 instance=review를 통해 특정 데이터를 가지고 온다
def edit(request,pk):
  review = Review.objects.get(id=pk)

  if request.method == 'POST':
    review_form = reviewForm(request.POST, instance=review)

    if review_form.is_valid():
      review_form.save()
      return redirect('article:detail', review.pk)

  else:
    review_form = reviewForm(instance=review)

  context = {
    'review_form' : review_form,
  }
  return render(request, 'article/edit.html', context)