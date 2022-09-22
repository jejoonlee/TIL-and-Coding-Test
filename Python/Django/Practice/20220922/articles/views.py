from django.shortcuts import render

# Create your views here.
import random

def eat(request):

  foods = ['삼겹살', '냉면', '치킨', '떡볶이', '라면', '김밥', '스파게티',] 
  idx = random.randrange(len(foods))

  food_img = [
    'http://samda.com/shopimages/samdacom1/0200020000012.jpg?1599823022',
    'https://diadiemhanquoc.com/wp-content/uploads/2020/06/M%C3%B3n-mi%E1%BA%BFn-l%E1%BA%A1nh-H%C3%A0n-Qu%E1%BB%91c-thanh-m%C3%A1t-c%E1%BA%A3-n%C6%B0%E1%BB%9Bc-s%C3%BAp-%EA%B5%AD%EB%AC%BC%EA%B9%8C%EC%A7%80-%EC%8B%9C%EC%9B%90%ED%95%9C-%EB%83%89%EB%A9%B4.jpg',
    'https://img.hankyung.com/photo/202202/99.11408152.1.jpg',
    'https://desion.kr/web/product/tiny/202101/7b8394ed298eafcde0ad47a0bc64de83.jpg',
    'http://res.heraldm.com/content/image/2022/01/07/20220107000641_0.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/0/0e/Gimbap_%28pixabay%29.jpg',
    'https://mblogthumb-phinf.pstatic.net/MjAxNzA4MTVfMTcy/MDAxNTAyNzg4NjkwNzY3.9ia3sQyIwubuRt26dLRoZIfFY0o-vkICMgsAEt2iUCog.VcoA1clnb5t27z01QWQl1OAoI3iCmCCnxkAl8e4DsE4g.JPEG.pyoun0181/%ED%86%A0%EB%A7%88%ED%86%A0%EC%8A%A4%ED%8C%8C%EA%B2%8C%ED%8B%B0DSC04185-022.jpg?type=w800',
  ]

  context = {
    'food' : foods[idx],
    'image' : food_img[idx],
  }

  return render(request, 'index.html', context)

def lotto(request):
  num1 = random.sample(range(1, 46), 6)
  num2 = random.sample(range(1, 46), 6)
  num3 = random.sample(range(1, 46), 6)
  num4 = random.sample(range(1, 46), 6)
  num5 = random.sample(range(1, 46), 6)

  last_week = random.sample(range(1, 46), 7)

  cnt = [0, 0, 0, 0, 0]

  print(last_week)
  for num in range(len(last_week)):
    # 6개가 연속해서 있다면, 1등
    if num != 6:
      if last_week[num] in num1:
        cnt[0] += 1
        if cnt[0] == 6:
          cnt[0] = '1등!!!!!'

      if last_week[num] in num2:
        cnt[1] += 1
        if cnt[1] == 6:
          cnt[1] = '1등!!!!!'

      if last_week[num] in num3:
        cnt[2] += 1
        if cnt[2] == 6:
          cnt[2] = '1등!!!!!'

      if last_week[num] in num4:
        cnt[3] += 1
        if cnt[3] == 6:
          cnt[3] = '1등!!!!!'

      if last_week[num] in num5:
        cnt[4] += 1
        if cnt[4] == 6:
          cnt[4] = '1등!!!!!'
    
    # 그외는 2등 아래
    else:
      if last_week[num] in num1:
        cnt[0] += 1

      if last_week[num] in num2:
        cnt[1] += 1

      if last_week[num] in num3:
        cnt[2] += 1

      if last_week[num] in num4:
        cnt[3] += 1

      if last_week[num] in num5:
        cnt[4] += 1

  print(cnt)

  for i in range(len(cnt)):
    if cnt[i] == 0:
      cnt[i] = '꽝! 같은 숫자 0개'
    elif cnt[i] == 1:
      cnt[i] = '꽝! 같은 숫자 1개'
    elif cnt[i] == 2:
      cnt[i] = '꽝! 같은 숫자 2개'
    elif cnt[i] == 3:
      cnt[i] = '5등! 같은 숫자 3개'
    elif cnt[i] == 4:
      cnt[i] = '4등! 같은 숫자 4개'
    elif cnt[i] == 5:
      cnt[i] = '3등!! 같은 숫자 5개'
    elif cnt[i] == 6:
      cnt[i] = '2등!!! 같은 숫자 6개'
    

  context = {
    'lotto1' : num1,
    'lotto2' : num2,
    'lotto3' : num3,
    'lotto4' : num4,
    'lotto5' : num5,

    'lastWeek' : last_week[:6],
    'bonus' : last_week[6],
    'cnt1' : cnt[0],
    'cnt2' : cnt[1],
    'cnt3' : cnt[2],
    'cnt4' : cnt[3],
    'cnt5' : cnt[4],
  }

  return render(request, 'lotto.html', context)